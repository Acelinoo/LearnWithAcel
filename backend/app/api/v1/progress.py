"""
Progress tracking routes: mark lessons complete, fetch stats,
and remember which lesson the user opened most recently.
"""

from fastapi import APIRouter, Depends

from app.core.deps import get_current_user
from app.schemas.progress import (
    LessonOpenResponse,
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
    response_model=LessonOpenResponse,
    summary="Remember that the user opened a lesson",
)
async def remember_open_lesson(
    lesson_id: str,
    current_user=Depends(get_current_user),
) -> LessonOpenResponse:
    """
    Remember that the user opened this lesson so the dashboard's
    "Continue learning" can resume exactly where they left off.

    Frontend should call this once per lesson page load (debounced, not
    on every render). The endpoint deliberately does not track view
    counts anymore — see git history for the previous behaviour.
    """
    payload = await progress_service.open_lesson(
        user_id=current_user.id,
        lesson_id=lesson_id,
    )
    return LessonOpenResponse(**payload)


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
