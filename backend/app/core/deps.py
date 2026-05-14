"""
FastAPI dependency injection helpers.
"""

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.database import prisma
from app.core.exceptions import ForbiddenException, UnauthorizedException
from app.core.security import decode_access_token

bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    """
    Validate the Bearer token and return the authenticated User record.

    Raises:
        UnauthorizedException: If the token is missing, expired, or invalid,
                               or if the user no longer exists in the database.
    """
    try:
        user_id = decode_access_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise UnauthorizedException("Token has expired")
    except jwt.InvalidTokenError:
        raise UnauthorizedException("Invalid token")

    user = await prisma.user.find_unique(where={"id": user_id})
    if user is None:
        raise UnauthorizedException("User not found")

    return user


async def get_current_admin(current_user=Depends(get_current_user)):
    """
    Extend get_current_user by also asserting the user has admin privileges.

    Raises:
        ForbiddenException: If the authenticated user is not an admin.
    """
    if not current_user.is_admin:
        raise ForbiddenException("Admin access required")
    return current_user
