"""
Business logic for roadmap and lesson content retrieval.
"""

from app.core.database import prisma
from app.core.exceptions import NotFoundException
from app.schemas.content import (
    CategoryResponse,
    LessonDetail,
    LessonSummary,
    LevelSummary,
    RoadmapResponse,
)


def _serialize_lesson_summary(lesson) -> LessonSummary:
    return LessonSummary(
        id=lesson.id,
        title=lesson.title,
        slug=lesson.slug,
        summary=lesson.summary,
        duration=lesson.duration,
        base_viewers=lesson.base_viewers,
        views=getattr(lesson, "views", 0) or 0,
        order_index=lesson.order_index,
        xp_reward=getattr(lesson, "xp_reward", 50) or 50,
        is_project=getattr(lesson, "is_project", False) or False,
    )


def _serialize_level_summary(level) -> LevelSummary:
    lessons = sorted(level.lessons or [], key=lambda l: l.order_index)
    return LevelSummary(
        id=level.id,
        number=level.number,
        title=level.title,
        slug=level.slug,
        subtitle=level.subtitle,
        description=level.description,
        duration=level.duration,
        difficulty=level.difficulty,
        accent_color=level.accent_color,
        mini_project=level.mini_project,
        quiz_count=level.quiz_count,
        base_viewers=level.base_viewers,
        tags=level.tags,
        coming_soon=level.coming_soon,
        lessons=[_serialize_lesson_summary(l) for l in lessons],
    )


def _serialize_category(category) -> CategoryResponse:
    return CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        available=category.available,
        role=category.role,
        side=category.side,
        description=category.description,
        tasks=category.tasks,
        techs=category.techs,
    )


async def get_all_categories() -> list[CategoryResponse]:
    """Return all learning path categories."""
    categories = await prisma.category.find_many(
        order={"name": "asc"},
    )
    return [_serialize_category(c) for c in categories]


async def get_roadmap(category_slug: str) -> RoadmapResponse:
    """
    Return a full roadmap for the given category slug, including all levels
    and their lessons ordered by level number.

    Raises:
        NotFoundException: If the category slug does not exist.
    """
    category = await prisma.category.find_unique(
        where={"slug": category_slug},
        include={
            "levels": {
                "include": {"lessons": True},
                "order_by": {"number": "asc"},
            }
        },
    )

    if category is None:
        raise NotFoundException(f"Category '{category_slug}' not found")

    levels = [_serialize_level_summary(lvl) for lvl in (category.levels or [])]

    return RoadmapResponse(
        category=_serialize_category(category),
        levels=levels,
    )


async def get_lesson_detail(level_slug: str, lesson_slug: str) -> LessonDetail:
    """
    Return the full detail of a single lesson.

    Raises:
        NotFoundException: If the level or lesson slug does not exist.
    """
    # Find the level first to give a clear error if it doesn't exist.
    level = await prisma.level.find_first(where={"slug": level_slug})
    if level is None:
        raise NotFoundException(f"Level '{level_slug}' not found")

    lesson = await prisma.lesson.find_first(
        where={"level_id": level.id, "slug": lesson_slug}
    )
    if lesson is None:
        raise NotFoundException(
            f"Lesson '{lesson_slug}' not found in level '{level_slug}'"
        )

    return LessonDetail(
        id=lesson.id,
        title=lesson.title,
        slug=lesson.slug,
        summary=lesson.summary,
        content=lesson.content,
        duration=lesson.duration,
        base_viewers=lesson.base_viewers,
        views=getattr(lesson, "views", 0) or 0,
        order_index=lesson.order_index,
        level_id=lesson.level_id,
        xp_reward=getattr(lesson, "xp_reward", 50) or 50,
        is_project=getattr(lesson, "is_project", False) or False,
    )
