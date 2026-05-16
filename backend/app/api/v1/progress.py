"""
Progress tracking routes: mark lessons complete, fetch stats, track views.
"""

from fastapi import APIRouter, Depends

from app.core.deps import get_current_user
from app.schemas.progress import (
    LessonViewResponse,
    ProgressResponse,
    StatsResponse,
)
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
    Idempotent — calling multiple times is safe.

    On the first transition from incomplete → complete, awards lesson XP
    and bumps the user's daily streak.
    """
    return await progress_service.complete_lesson(
        user_id=current_user.id,
        lesson_id=lesson_id,
    )


@router.post(
    "/view/{lesson_id}",
    response_model=LessonViewResponse,
    summary="Track that the user opened a lesson",
)
async def track_view(
    lesson_id: str,
    current_user=Depends(get_current_user),
) -> LessonViewResponse:
    """
    Increment the view counter for a lesson and remember it as the
    user's last opened lesson. Frontend should call this once per
    lesson page load (debounced, not on every render).
    """
    payload = await progress_service.open_lesson(
        user_id=current_user.id,
        lesson_id=lesson_id,
    )
    return LessonViewResponse(**payload)


@router.get(
    "/stats",
    response_model=StatsResponse,
    summary="Get learning progress statistics",
)
async def get_stats(current_user=Depends(get_current_user)) -> StatsResponse:
    """
    Return overall and per-level completion statistics, engagement
    metrics, and a resolved "continue learning" target.
    """
    return await progress_service.get_user_stats(user_id=current_user.id)
