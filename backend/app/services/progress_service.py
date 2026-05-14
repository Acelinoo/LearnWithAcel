"""
Business logic for tracking and querying user learning progress.
"""

from datetime import datetime, timezone

from app.core.database import prisma
from app.core.exceptions import NotFoundException
from app.schemas.progress import LevelStats, ProgressResponse, StatsResponse


async def complete_lesson(user_id: str, lesson_id: str) -> ProgressResponse:
    """
    Mark a lesson as completed for the authenticated user.

    Uses upsert so calling this endpoint multiple times is idempotent.

    Raises:
        NotFoundException: If the lesson_id does not exist.
    """
    lesson = await prisma.lesson.find_unique(where={"id": lesson_id})
    if lesson is None:
        raise NotFoundException(f"Lesson '{lesson_id}' not found")

    now = datetime.now(timezone.utc)

    progress = await prisma.userprogress.upsert(
        where={"user_id_lesson_id": {"user_id": user_id, "lesson_id": lesson_id}},
        data={
            "create": {
                "user_id": user_id,
                "lesson_id": lesson_id,
                "is_completed": True,
                "completed_at": now,
            },
            "update": {
                "is_completed": True,
                "completed_at": now,
            },
        },
    )

    return ProgressResponse(
        id=progress.id,
        user_id=progress.user_id,
        lesson_id=progress.lesson_id,
        is_completed=progress.is_completed,
        completed_at=progress.completed_at.isoformat() if progress.completed_at else None,
    )


async def get_user_stats(user_id: str) -> StatsResponse:
    """
    Return overall and per-level completion statistics for the user.
    """
    # Fetch all lessons grouped by level (only levels that have lessons)
    levels = await prisma.level.find_many(
        include={"lessons": True},
        order={"number": "asc"},
    )

    # Fetch all completed lesson IDs for this user in one query
    completed_records = await prisma.userprogress.find_many(
        where={"user_id": user_id, "is_completed": True},
    )
    completed_ids: set[str] = {r.lesson_id for r in completed_records}

    total_lessons = 0
    total_completed = 0
    by_level: list[LevelStats] = []

    for level in levels:
        lessons = level.lessons or []
        if not lessons:
            continue

        level_total = len(lessons)
        level_completed = sum(1 for l in lessons if l.id in completed_ids)

        total_lessons += level_total
        total_completed += level_completed

        by_level.append(
            LevelStats(
                level_id=level.id,
                level_title=level.title,
                level_slug=level.slug,
                total_lessons=level_total,
                completed_lessons=level_completed,
                percentage=round(level_completed / level_total * 100, 1),
            )
        )

    overall_pct = (
        round(total_completed / total_lessons * 100, 1) if total_lessons > 0 else 0.0
    )

    return StatsResponse(
        total_lessons=total_lessons,
        completed_lessons=total_completed,
        overall_percentage=overall_pct,
        by_level=by_level,
    )
