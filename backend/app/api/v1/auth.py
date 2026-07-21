"""
Authentication routes: register, login, and current user profile.
"""

from fastapi import APIRouter, Depends, status

from app.core.deps import get_current_user
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse, UserUpdateRole
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
async def login(payload: LoginRequest) -> TokenResponse:
    """Authenticate with email and password, returns a Bearer token."""
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
    summary="Update selected category and role",
)
async def update_role(payload: UserUpdateRole, current_user=Depends(get_current_user)) -> UserResponse:
    """Update the user's selected category and role."""
    return await auth_service.update_user_role(current_user.id, payload)
