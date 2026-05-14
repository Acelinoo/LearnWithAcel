"""
Content routes: categories, roadmap, and lesson detail.
"""

from fastapi import APIRouter

from app.schemas.content import CategoryResponse, LessonDetail, RoadmapResponse
from app.services import content_service

router = APIRouter(tags=["Content"])


@router.get(
    "/categories",
    response_model=list[CategoryResponse],
    summary="List all learning path categories",
)
async def list_categories() -> list[CategoryResponse]:
    """Return all available learning path categories (Frontend, Backend, Fullstack, Vibe)."""
    return await content_service.get_all_categories()


@router.get(
    "/roadmap/{category_slug}",
    response_model=RoadmapResponse,
    summary="Get full roadmap for a category",
)
async def get_roadmap(category_slug: str) -> RoadmapResponse:
    """
    Return all levels and their lessons for the given category slug.

    Example slugs: `frontend`, `backend`, `fullstack`, `vibe`
    """
    return await content_service.get_roadmap(category_slug)


@router.get(
    "/lessons/{level_slug}/{lesson_slug}",
    response_model=LessonDetail,
    summary="Get full lesson content",
)
async def get_lesson(level_slug: str, lesson_slug: str) -> LessonDetail:
    """
    Return the full markdown content and metadata for a single lesson.

    Example: `/lessons/html-css/mengenal-html`
    """
    return await content_service.get_lesson_detail(level_slug, lesson_slug)
