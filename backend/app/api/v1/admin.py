"""
Admin / CMS routes — requires is_admin = true on the authenticated user.

All endpoints are prefixed with /admin and protected by the
get_current_admin dependency.

Section 5.4 of the PRD:
  Categories : POST / PUT / DELETE /admin/categories
  Levels     : POST / PUT / DELETE /admin/levels
  Lessons    : POST / PUT / DELETE /admin/lessons
"""

from fastapi import APIRouter, Depends, status

from app.core.deps import get_current_admin
from app.schemas.admin import (
    CategoryCreateRequest,
    CategoryUpdateRequest,
    DeleteResponse,
    LessonCreateRequest,
    LessonUpdateRequest,
    LevelCreateRequest,
    LevelUpdateRequest,
)
from app.schemas.content import CategoryResponse, LessonDetail, LevelSummary
from app.services import admin_service

router = APIRouter(
    prefix="/admin",
    tags=["Admin — Content Management"],
    dependencies=[Depends(get_current_admin)],  # every route requires admin
)


# ── Categories ────────────────────────────────────────────────────────────────
@router.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new category",
)
async def create_category(payload: CategoryCreateRequest) -> CategoryResponse:
    """
    Create a new learning path category (e.g. Frontend, Backend, Vibe).

    - `slug` must be unique and lowercase-kebab-case.
    - `techs` is a JSON array: `[{ "label": "Dasar", "items": ["HTML"] }]`
    """
    return await admin_service.create_category(payload)


@router.put(
    "/categories/{category_id}",
    response_model=CategoryResponse,
    summary="Update a category",
)
async def update_category(
    category_id: str, payload: CategoryUpdateRequest
) -> CategoryResponse:
    """
    Partially update a category. Only the fields you send will be changed.
    """
    return await admin_service.update_category(category_id, payload)


@router.delete(
    "/categories/{category_id}",
    response_model=DeleteResponse,
    summary="Delete a category",
)
async def delete_category(category_id: str) -> DeleteResponse:
    """
    Permanently delete a category and all its child levels and lessons.
    This action is irreversible.
    """
    return await admin_service.delete_category(category_id)


# ── Levels ────────────────────────────────────────────────────────────────────
@router.post(
    "/levels",
    response_model=LevelSummary,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new level",
)
async def create_level(payload: LevelCreateRequest) -> LevelSummary:
    """
    Create a new level inside an existing category.

    - `category_id` must reference an existing category UUID.
    - `slug` must be unique within the category.
    - `tags` is a JSON array of strings: `["HTML5", "CSS3"]`
    """
    return await admin_service.create_level(payload)


@router.put(
    "/levels/{level_id}",
    response_model=LevelSummary,
    summary="Update a level",
)
async def update_level(level_id: str, payload: LevelUpdateRequest) -> LevelSummary:
    """
    Partially update a level. Only the fields you send will be changed.
    """
    return await admin_service.update_level(level_id, payload)


@router.delete(
    "/levels/{level_id}",
    response_model=DeleteResponse,
    summary="Delete a level",
)
async def delete_level(level_id: str) -> DeleteResponse:
    """
    Permanently delete a level and all its child lessons.
    This action is irreversible.
    """
    return await admin_service.delete_level(level_id)


# ── Lessons ───────────────────────────────────────────────────────────────────
@router.post(
    "/lessons",
    response_model=LessonDetail,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new lesson",
)
async def create_lesson(payload: LessonCreateRequest) -> LessonDetail:
    """
    Create a new lesson inside an existing level.

    - `level_id` must reference an existing level UUID.
    - `slug` must be unique within the level.
    - `content` accepts full **Markdown** — this is the main lesson body.
    - `order_index` controls the display order within the level (1-based).
    """
    return await admin_service.create_lesson(payload)


@router.put(
    "/lessons/{lesson_id}",
    response_model=LessonDetail,
    summary="Update a lesson",
)
async def update_lesson(lesson_id: str, payload: LessonUpdateRequest) -> LessonDetail:
    """
    Partially update a lesson, including its Markdown content.
    Only the fields you send will be changed.
    """
    return await admin_service.update_lesson(lesson_id, payload)


@router.delete(
    "/lessons/{lesson_id}",
    response_model=DeleteResponse,
    summary="Delete a lesson",
)
async def delete_lesson(lesson_id: str) -> DeleteResponse:
    """
    Permanently delete a lesson.
    This action is irreversible.
    """
    return await admin_service.delete_lesson(lesson_id)
