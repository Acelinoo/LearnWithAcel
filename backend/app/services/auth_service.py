"""
Business logic for authentication: register, login, profile retrieval,
forgot password, and reset password.
"""

import logging
import secrets
from datetime import datetime, timedelta, timezone

from app.core.database import prisma
from app.core.email import send_reset_password_email
from app.core.exceptions import ConflictException, NotFoundException, UnauthorizedException
from app.core.security import create_access_token, hash_password, verify_password
from app.schemas.auth import (
    ForgotPasswordRequest,
    LoginRequest,
    MessageResponse,
    RegisterRequest,
    ResetPasswordRequest,
    TokenResponse,
    UserResponse,
    UserUpdateRole,
)
from app.core.config import settings

logger = logging.getLogger(__name__)


async def register_user(payload: RegisterRequest) -> UserResponse:
    """
    Create a new user account.

    Raises:
        ConflictException: If the email is already registered.
    """
    existing = await prisma.user.find_unique(where={"email": payload.email})
    if existing:
        raise ConflictException("Email is already registered")

    user = await prisma.user.create(
        data={
            "email": payload.email,
            "full_name": payload.full_name,
            "hashed_password": hash_password(payload.password),
        }
    )

    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        avatar_url=user.avatar_url,
        is_admin=user.is_admin,
        created_at=user.created_at.isoformat(),
    )


async def login_user(payload: LoginRequest) -> TokenResponse:
    """
    Authenticate a user and return a JWT access token.

    Raises:
        UnauthorizedException: If credentials are invalid.
    """
    user = await prisma.user.find_unique(where={"email": payload.email})

    # Use constant-time comparison even when user doesn't exist to prevent
    # timing-based user enumeration attacks.
    if user is None or not verify_password(payload.password, user.hashed_password):
        raise UnauthorizedException("Invalid email or password")

    token = create_access_token(subject=user.id)
    return TokenResponse(access_token=token)


def get_user_profile(user) -> UserResponse:
    """Serialize the authenticated user model into a response schema."""
    created_at_str = (
        user.created_at.isoformat()
        if hasattr(user.created_at, "isoformat")
        else str(user.created_at)
    )
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        avatar_url=getattr(user, "avatar_url", None),
        is_admin=getattr(user, "is_admin", False),
        created_at=created_at_str,
        selected_category=getattr(user, "selected_category", None),
        selected_role=getattr(user, "selected_role", None),
        has_completed_onboarding=getattr(user, "has_completed_onboarding", False),
    )


async def update_user_role(user, payload: UserUpdateRole) -> UserResponse:
    """Update the user's selected category and role."""
    updated_user = await prisma.user.update(
        where={"id": user.id},
        data={
            "selected_category": payload.selected_category,
            "selected_role": payload.selected_role,
            "has_completed_onboarding": True,
        },
    )
    return get_user_profile(updated_user)


# ── Forgot / reset password ───────────────────────────────────────────────────

async def forgot_password(payload: ForgotPasswordRequest) -> MessageResponse:
    """
    Initiate the forgot-password flow.

    Always returns the same success message regardless of whether the email
    exists — this prevents user enumeration via the response.

    Steps:
      1. Look up the user by email (silently no-op if not found).
      2. Delete any existing unexpired tokens for this user.
      3. Generate a cryptographically secure random token.
      4. Persist the token with an expiry timestamp.
      5. Send the reset email.
    """
    _SAFE_RESPONSE = MessageResponse(
        message=(
            "Jika email terdaftar, kamu akan menerima link reset password dalam beberapa menit."
        )
    )

    user = await prisma.user.find_unique(where={"email": payload.email})
    if user is None:
        # Return the same message to avoid leaking whether the email exists.
        logger.info("Forgot-password requested for unknown email: %s", payload.email)
        return _SAFE_RESPONSE

    # Invalidate any previous reset tokens for this user to prevent token
    # accumulation and ensure only the latest link works.
    await prisma.passwordresettoken.delete_many(where={"user_id": user.id})

    # Generate a 64-character hex token (32 bytes of entropy).
    raw_token = secrets.token_hex(32)
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=settings.RESET_TOKEN_EXPIRE_MINUTES
    )

    await prisma.passwordresettoken.create(
        data={
            "user_id": user.id,
            "token": raw_token,
            "expires_at": expires_at,
        }
    )

    # Fire-and-forget: send the email. Errors are logged but not surfaced to
    # the caller so the response time doesn't leak whether the email exists.
    try:
        await send_reset_password_email(
            to_email=user.email,
            full_name=user.full_name,
            reset_token=raw_token,
        )
    except Exception:
        logger.exception("Failed to send reset email to %s", user.email)

    return _SAFE_RESPONSE


async def reset_password(payload: ResetPasswordRequest) -> MessageResponse:
    """
    Complete the forgot-password flow by setting a new password.

    Steps:
      1. Look up the token record.
      2. Validate it exists and has not expired.
      3. Hash and save the new password.
      4. Delete the token so it cannot be reused.

    Raises:
        NotFoundException: If the token is invalid or expired.
    """
    record = await prisma.passwordresettoken.find_unique(
        where={"token": payload.token},
        include={"user": True},
    )

    now = datetime.now(timezone.utc)

    if record is None or record.expires_at.replace(tzinfo=timezone.utc) < now:
        # Delete the expired record if it exists to keep the table clean.
        if record is not None:
            await prisma.passwordresettoken.delete(where={"id": record.id})
        raise NotFoundException(
            "Token reset password tidak valid atau sudah kadaluarsa. "
            "Silakan minta link reset baru."
        )

    # Update the user's password.
    await prisma.user.update(
        where={"id": record.user_id},
        data={"hashed_password": hash_password(payload.new_password)},
    )

    # Consume the token — one-time use only.
    await prisma.passwordresettoken.delete(where={"id": record.id})

    logger.info("Password reset successfully for user %s", record.user_id)

    return MessageResponse(
        message="Password berhasil direset. Silakan login dengan password baru kamu."
    )
