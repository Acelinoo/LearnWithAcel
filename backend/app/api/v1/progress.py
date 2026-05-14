"""
Progress tracking routes: mark lessons complete and fetch stats.
"""

from fastapi import APIRouter, Depends

from app.core.deps import get_current_user
from app.schemas.progress import ProgressResponse, StatsResponse
from app.services import progress_service

router = APIRouter(prefix="/progress", tags=["Progress"])


@router.post(
    "/complete/{lesson_id}",
    response_model=ProgressResponse,
    summary="Mark a lesson as completed",
)
async def complete_lesson(
    lesson_id: str,
    current_user=Depends(get_current_user),
) -> ProgressResponse:
    """
    Mark the specified lesson as completed for the authenticated user.
    This endpoint is idempotent — calling it multiple times is safe.
    """
    return await progress_service.complete_lesson(
        user_id=current_user.id,
        lesson_id=lesson_id,
    )


@router.get(
    "/stats",
    response_model=StatsResponse,
    summary="Get learning progress statistics",
)
async def get_stats(current_user=Depends(get_current_user)) -> StatsResponse:
    """
    Return overall and per-level completion statistics for the authenticated user.
    """
    return await progress_service.get_user_stats(user_id=current_user.id)
