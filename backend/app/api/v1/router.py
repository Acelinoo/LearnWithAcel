"""
Aggregate all v1 routers into a single APIRouter.
"""

from fastapi import APIRouter

from app.api.v1 import admin, auth, content, progress, views

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router)
api_router.include_router(content.router)
api_router.include_router(progress.router)
api_router.include_router(views.router)
api_router.include_router(admin.router)
