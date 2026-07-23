"""
Authentication routes: register, login, current user profile,
forgot password, and reset password.
"""

from fastapi import APIRouter, Depends, status, Response

from app.core.deps import get_current_user
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
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(payload: RegisterRequest) -> UserResponse:
    """Create a new user account and return the created profile."""
    return await auth_service.register_user(payload)


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login and receive a JWT token",
)
async def login(payload: LoginRequest, response: Response) -> TokenResponse:
    """Authenticate with email and password, returns a Bearer token."""
    response.headers["Cache-Control"] = "no-store, max-age=0"
    return await auth_service.login_user(payload)


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user profile",
)
async def me(current_user=Depends(get_current_user)) -> UserResponse:
    """Return the profile of the currently authenticated user."""
    return auth_service.get_user_profile(current_user)


@router.put(
    "/role",
    response_model=UserResponse,
    summary="Update user's selected category and role",
)
async def update_role(
    payload: UserUpdateRole, current_user=Depends(get_current_user)
) -> UserResponse:
    """Update the current user's selected category and role."""
    return await auth_service.update_user_role(current_user, payload)


@router.post(
    "/forgot-password",
    response_model=MessageResponse,
    summary="Request a password reset link",
)
async def forgot_password(payload: ForgotPasswordRequest) -> MessageResponse:
    """
    Send a password-reset email to the given address.

    **Always returns 200** regardless of whether the email is registered —
    this prevents user enumeration attacks.

    The email contains a link valid for `RESET_TOKEN_EXPIRE_MINUTES` minutes
    (default: 15 min). The link points to the frontend reset-password page
    with the token as a query parameter: `?token=<token>`.
    """
    return await auth_service.forgot_password(payload)


@router.post(
    "/reset-password",
    response_model=MessageResponse,
    summary="Reset password using a token from email",
)
async def reset_password(payload: ResetPasswordRequest) -> MessageResponse:
    """
    Set a new password using the one-time token received via email.

    - The token is **single-use** — it is deleted immediately after a
      successful reset.
    - Returns `404` if the token is invalid or has expired.
    - After a successful reset the user must log in again with the new password.
    """
    return await auth_service.reset_password(payload)
