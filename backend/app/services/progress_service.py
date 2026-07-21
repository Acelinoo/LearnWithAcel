"""
Business logic for tracking and querying user learning progress.

Side-effects on completion:
- Lesson XP is added to User.xp_total exactly once per lesson.
- Daily streak is incremented when a user completes their first lesson
  on a calendar day. Resets to 1 if more than a day has passed since
  their last activity, otherwise stays the same.
"""

from datetime import date, datetime, timedelta, timezone

from app.core.database import prisma
from app.core.exceptions import NotFoundException
from app.schemas.progress import LevelStats, ProgressResponse, StatsResponse


def _to_iso(dt: datetime | None) -> str | None:
    return dt.isoformat() if dt else None


async def _bump_user_engagement(user_id: str, xp_earned: int) -> tuple[int, int]:
    """Update User.xp_total and User.current_streak / longest_streak.

    Returns (new_total_xp, new_current_streak).
    """
    user = await prisma.user.find_unique(where={"id": user_id})
    if user is None:
        return 0, 0

    now = datetime.now(timezone.utc)
    today = now.date()
    last = user.last_activity_at
    last_day: date | None = last.date() if last else None

    if last_day is None:
        new_streak = 1
    elif last_day == today:
        new_streak = user.current_streak or 1
    elif last_day == today - timedelta(days=1):
        new_streak = (user.current_streak or 0) + 1
    else:
        new_streak = 1

    new_total_xp = (user.xp_total or 0) + xp_earned
    new_longest = max(user.longest_streak or 0, new_streak)

    await prisma.user.update(
        where={"id": user_id},
        data={
            "xp_total": new_total_xp,
            "current_streak": new_streak,
            "longest_streak": new_longest,
            "last_activity_at": now,
        },
    )

    return new_total_xp, new_streak


async def open_lesson(user_id: str, lesson_id: str) -> dict:
    """Remember that the user opened a lesson.

    Updates user.last_opened_lesson_id + last_opened_at so the dashboard's
    "Continue learning" can resume exactly where they left off. View
    counters are intentionally not tracked anymore — see git history for
    the previous EntityView-based implementation.
    """
    now = datetime.now(timezone.utc)
    
    # -----------------------------------------------------------
    # Support for static "jalur" lessons
    # -----------------------------------------------------------
    if lesson_id.startswith("jalur-"):
        await prisma.user.update(
            where={"id": user_id},
            data={
                "last_opened_lesson_id": lesson_id,
                "last_opened_at": now,
            },
        )
        return {
            "lesson_id": lesson_id,
            "last_opened_at": _to_iso(now),
        }

    lesson = await prisma.lesson.find_unique(where={"id": lesson_id})
    if lesson is None:
        raise NotFoundException(f"Lesson '{lesson_id}' not found")

    await prisma.user.update(
        where={"id": user_id},
        data={
            "last_opened_lesson_id": lesson_id,
            "last_opened_at": now,
        },
    )

    return {
        "lesson_id": lesson_id,
        "last_opened_at": _to_iso(now),
    }


async def complete_lesson(user_id: str, lesson_id: str) -> ProgressResponse:
    """
    Mark a lesson as completed for the authenticated user.

    The endpoint is idempotent — calling it twice will not award XP
    twice. The first transition from false → true is what awards XP and
    bumps the streak.
    """
    now = datetime.now(timezone.utc)

    # -----------------------------------------------------------
    # Support for static "jalur" lessons
    # -----------------------------------------------------------
    if lesson_id.startswith("jalur-"):
        user = await prisma.user.find_unique(where={"id": user_id})
        if user is None:
            raise NotFoundException("User not found")
            
        import json
        jalur_lessons = []
        if user.completed_jalur_lessons:
            try:
                if isinstance(user.completed_jalur_lessons, str):
                    jalur_lessons = json.loads(user.completed_jalur_lessons)
                elif isinstance(user.completed_jalur_lessons, list):
                    jalur_lessons = user.completed_jalur_lessons
            except json.JSONDecodeError:
                pass
                
        just_completed = lesson_id not in jalur_lessons
        
        new_total_xp = user.xp_total or 0
        new_streak = user.current_streak or 0
        xp_reward = 50  # Hardcoded reward for jalur lessons
        
        if just_completed:
            jalur_lessons.append(lesson_id)
            await prisma.user.update(
                where={"id": user_id},
                data={
                    "completed_jalur_lessons": json.dumps(jalur_lessons)
                }
            )
            new_total_xp, new_streak = await _bump_user_engagement(user_id, xp_reward)
            
        return ProgressResponse(
            id=f"prog-{lesson_id}",
            user_id=user_id,
            lesson_id=lesson_id,
            is_completed=True,
            completed_at=_to_iso(now),
            xp_earned=xp_reward if just_completed else 0,
            new_total_xp=new_total_xp,
            streak=new_streak,
            just_completed=just_completed,
        )

    lesson = await prisma.lesson.find_unique(where={"id": lesson_id})
    if lesson is None:
        raise NotFoundException(f"Lesson '{lesson_id}' not found")

    existing = await prisma.userprogress.find_unique(
        where={"user_id_lesson_id": {"user_id": user_id, "lesson_id": lesson_id}},
    )

    just_completed = existing is None or not existing.is_completed
    xp_reward = lesson.xp_reward or 0

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

    new_total_xp = 0
    new_streak = 0
    if just_completed:
        new_total_xp, new_streak = await _bump_user_engagement(user_id, xp_reward)
    else:
        user = await prisma.user.find_unique(where={"id": user_id})
        if user:
            new_total_xp = user.xp_total or 0
            new_streak = user.current_streak or 0

    return ProgressResponse(
        id=progress.id,
        user_id=progress.user_id,
        lesson_id=progress.lesson_id,
        is_completed=progress.is_completed,
        completed_at=_to_iso(progress.completed_at),
        xp_earned=xp_reward if just_completed else 0,
        new_total_xp=new_total_xp,
        streak=new_streak,
        just_completed=just_completed,
    )


async def get_user_stats(user_id: str) -> StatsResponse:
    """
    Return overall and per-level completion statistics for the user,
    plus engagement metrics (XP, current/longest streak), and the
    resolved "next lesson" the user should continue with.
    """
    levels = await prisma.level.find_many(
        include={
            "lessons": {"order_by": {"order_index": "asc"}},
            "category": True,
        },
        order={"number": "asc"},
    )

    completed_records = await prisma.userprogress.find_many(
        where={"user_id": user_id, "is_completed": True},
    )
    
    user = await prisma.user.find_unique(where={"id": user_id})
    
    completed_ids: set[str] = {r.lesson_id for r in completed_records}
    
    import json
    if user and user.completed_jalur_lessons:
        try:
            if isinstance(user.completed_jalur_lessons, str):
                jalur_lessons = json.loads(user.completed_jalur_lessons)
            elif isinstance(user.completed_jalur_lessons, list):
                jalur_lessons = user.completed_jalur_lessons
            else:
                jalur_lessons = []
            
            for jl in jalur_lessons:
                completed_ids.add(jl)
        except json.JSONDecodeError:
            pass

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

        category_slug = level.category.slug if level.category else None

        by_level.append(
            LevelStats(
                level_id=level.id,
                level_title=level.title,
                level_slug=level.slug,
                category_slug=category_slug,
                total_lessons=level_total,
                completed_lessons=level_completed,
                percentage=round(level_completed / level_total * 100, 1),
            )
        )

    overall_pct = (
        round(total_completed / total_lessons * 100, 1) if total_lessons > 0 else 0.0
    )

    # Streak grace period: if the user hasn't done anything in 2+ days,
    # surface 0 in the response — the actual reset happens next time
    # they complete a lesson.
    current_streak = user.current_streak if user else 0
    if user and user.last_activity_at:
        gap = datetime.now(timezone.utc).date() - user.last_activity_at.date()
        if gap.days > 1:
            current_streak = 0

    # Resolve continue-learning target.
    continue_lesson = await _resolve_continue_lesson(
        user=user,
        levels=levels,
        completed_ids=completed_ids,
    )

    return StatsResponse(
        total_lessons=total_lessons,
        completed_lessons=total_completed,
        overall_percentage=overall_pct,
        by_level=by_level,
        completed_lesson_ids=sorted(completed_ids),
        xp_total=(user.xp_total if user else 0) or 0,
        current_streak=current_streak or 0,
        longest_streak=(user.longest_streak if user else 0) or 0,
        last_activity_at=_to_iso(user.last_activity_at) if user else None,
        continue_lesson=continue_lesson,
    )


async def _resolve_continue_lesson(
    *,
    user,
    levels: list,
    completed_ids: set[str],
) -> dict | None:
    """Decide which lesson the user should pick up next.

    Resolution order:
      1. The lesson they last opened — if it exists, isn't completed, and
         hasn't been deleted.
      2. The next incomplete lesson within the level of the last-opened
         lesson (if last-opened is already completed).
      3. The first incomplete lesson in the first level that has any
         progress recorded.
      4. None — fall through; UI can decide what to show.
    """
    if not levels:
        return None

    # Index lessons by id and by level for quick lookups.
    lesson_by_id = {}
    lessons_by_level: dict[str, list] = {}
    for level in levels:
        ordered = sorted(level.lessons or [], key=lambda l: l.order_index)
        lessons_by_level[level.id] = ordered
        for l in ordered:
            lesson_by_id[l.id] = (l, level)

    def _format(lesson, level) -> dict:
        return {
            "lesson_id": lesson.id,
            "lesson_slug": lesson.slug,
            "lesson_title": lesson.title,
            "level_id": level.id,
            "level_slug": level.slug,
            "level_title": level.title,
            "level_number": level.number,
            "category_slug": level.category.slug if level.category else None,
        }

    # 1. Last opened lesson, if still incomplete.
    if user and user.last_opened_lesson_id:
        entry = lesson_by_id.get(user.last_opened_lesson_id)
        if entry:
            lesson, level = entry
            if lesson.id not in completed_ids:
                return _format(lesson, level)
            # 2. Same level next incomplete lesson.
            for sibling in lessons_by_level.get(level.id, []):
                if sibling.id not in completed_ids:
                    return _format(sibling, level)

    # 3. First incomplete lesson in any level that has progress.
    levels_with_progress = [
        lvl
        for lvl in levels
        if any(l.id in completed_ids for l in (lvl.lessons or []))
    ]
    for lvl in levels_with_progress:
        for lesson in lessons_by_level.get(lvl.id, []):
            if lesson.id not in completed_ids:
                return _format(lesson, lvl)

    # No suggestion — let the UI handle empty state.
    return None

