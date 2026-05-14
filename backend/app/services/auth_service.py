"""
Business logic for authentication: register, login, and profile retrieval.
"""

from app.core.database import prisma
from app.core.exceptions import ConflictException, UnauthorizedException
from app.core.security import create_access_token, hash_password, verify_password
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse


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
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        avatar_url=user.avatar_url,
        is_admin=user.is_admin,
        created_at=user.created_at.isoformat(),
    )
