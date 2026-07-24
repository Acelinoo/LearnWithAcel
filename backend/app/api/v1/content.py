"""
Content routes: categories, roadmap, and lesson detail.
"""

from fastapi import APIRouter, Response

from app.schemas.content import CategoryResponse, LessonDetail, RoadmapResponse
from app.services import content_service

router = APIRouter(tags=["Content"])


@router.get(
    "/categories",
    response_model=list[CategoryResponse],
    summary="List all learning path categories",
)
async def list_categories(response: Response) -> list[CategoryResponse]:
    """Return all available learning path categories (Frontend, Backend, Fullstack, Vibe)."""
    response.headers["Cache-Control"] = "public, s-maxage=3600, stale-while-revalidate=86400"
    return await content_service.get_all_categories()


@router.get(
    "/roadmap/{category_slug}",
    response_model=RoadmapResponse,
    summary="Get full roadmap for a category",
)
async def get_roadmap(category_slug: str, response: Response) -> RoadmapResponse:
    """
    Return all levels and their lessons for the given category slug.

    Example slugs: `frontend`, `backend`, `fullstack`, `vibe`
    """
    response.headers["Cache-Control"] = "public, s-maxage=1800, stale-while-revalidate=86400"
    return await content_service.get_roadmap(category_slug)


@router.get(
    "/lessons/{level_slug}/{lesson_slug}",
    response_model=LessonDetail,
    summary="Get full lesson content",
)
async def get_lesson(level_slug: str, lesson_slug: str, response: Response) -> LessonDetail:
    """
    Return the full markdown content and metadata for a single lesson.

    Example: `/lessons/html-css/mengenal-html`
    """
    response.headers["Cache-Control"] = "public, s-maxage=1800, stale-while-revalidate=86400"
    return await content_service.get_lesson_detail(level_slug, lesson_slug)

