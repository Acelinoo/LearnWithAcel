"""
Business logic for roadmap and lesson content retrieval.
"""

from app.core.cache import cache_manager
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
    is_project = "Mini Project" in lesson.title
    return LessonSummary(
        id=lesson.id,
        title=lesson.title,
        slug=lesson.slug,
        summary=lesson.summary,
        duration=lesson.duration,
        order_index=lesson.order_index,
        xp_reward=150 if is_project else 50,
        is_project=is_project,
        video_url=lesson.video_url,
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
    """Return all learning path categories (cached for 1 hour)."""
    cache_key = "content:categories"

    async def _fetch():
        categories = await prisma.category.find_many(
            order={"name": "asc"},
        )
        return [_serialize_category(c).model_dump() for c in categories]

    raw_list = await cache_manager.get_or_set(cache_key, _fetch, ttl=3600)
    return [CategoryResponse(**item) for item in raw_list]


async def get_roadmap(category_slug: str) -> RoadmapResponse:
    """
    Return a full roadmap for the given category slug, including all levels
    and their lessons ordered by level number (cached for 30 minutes).

    Raises:
        NotFoundException: If the category slug does not exist.
    """
    cache_key = f"content:roadmap:{category_slug}"

    async def _fetch():
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

        res = RoadmapResponse(
            category=_serialize_category(category),
            levels=levels,
        )
        return res.model_dump()

    raw_res = await cache_manager.get_or_set(cache_key, _fetch, ttl=1800)
    return RoadmapResponse(**raw_res)


async def get_lesson_detail(level_slug: str, lesson_slug: str) -> LessonDetail:
    """
    Return the full detail of a single lesson (cached for 30 minutes).

    Raises:
        NotFoundException: If the level or lesson slug does not exist.
    """
    cache_key = f"content:lesson:{level_slug}:{lesson_slug}"

    async def _fetch():
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

        is_project = "Mini Project" in lesson.title
        res = LessonDetail(
            id=lesson.id,
            title=lesson.title,
            slug=lesson.slug,
            summary=lesson.summary,
            content=lesson.content,
            duration=lesson.duration,
            order_index=lesson.order_index,
            level_id=lesson.level_id,
            xp_reward=150 if is_project else 50,
            is_project=is_project,
            video_url=lesson.video_url,
            criteria=lesson.criteria,
            hints=lesson.hints,
        )
        return res.model_dump()

    raw_res = await cache_manager.get_or_set(cache_key, _fetch, ttl=1800)
    return LessonDetail(**raw_res)
