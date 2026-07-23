"""
Business logic for admin / CMS operations.

Covers full CRUD for Category, Level, and Lesson.
All write operations validate foreign-key existence and slug uniqueness
before touching the database.
"""

import json
from typing import Any

from app.core.database import prisma
from app.core.exceptions import ConflictException, NotFoundException
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


# ── Helpers ───────────────────────────────────────────────────────────────────
def _to_json_str(value: Any) -> str:
    """Ensure a value is stored as a JSON string (Prisma Json field)."""
    if isinstance(value, str):
        return value  # already serialised
    return json.dumps(value)


def _serialize_category(c) -> CategoryResponse:
    return CategoryResponse(
        id=c.id,
        name=c.name,
        slug=c.slug,
        available=c.available,
        role=c.role,
        side=c.side,
        description=c.description,
        tasks=c.tasks,
        techs=c.techs,
    )


def _serialize_level(level) -> LevelSummary:
    from app.services.content_service import _serialize_lesson_summary

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


def _serialize_lesson(lesson) -> LessonDetail:
    return LessonDetail(
        id=lesson.id,
        title=lesson.title,
        slug=lesson.slug,
        summary=lesson.summary,
        content=lesson.content,
        duration=lesson.duration,
        order_index=lesson.order_index,
        level_id=lesson.level_id,
        video_url=lesson.video_url,
    )


# ── Category CRUD ─────────────────────────────────────────────────────────────
async def create_category(payload: CategoryCreateRequest) -> CategoryResponse:
    """
    Create a new learning path category.

    Raises:
        ConflictException: If the slug is already taken.
    """
    existing = await prisma.category.find_unique(where={"slug": payload.slug})
    if existing:
        raise ConflictException(f"Category slug '{payload.slug}' is already in use")

    category = await prisma.category.create(
        data={
            "name": payload.name,
            "slug": payload.slug,
            "available": payload.available,
            "role": payload.role,
            "side": payload.side,
            "description": payload.description,
            "tasks": payload.tasks,
            "techs": _to_json_str(payload.techs),
        }
    )
    return _serialize_category(category)


async def update_category(category_id: str, payload: CategoryUpdateRequest) -> CategoryResponse:
    """
    Partially update a category. Only provided fields are changed.

    Raises:
        NotFoundException: If the category does not exist.
        ConflictException: If the new slug is already taken by another category.
    """
    existing = await prisma.category.find_unique(where={"id": category_id})
    if existing is None:
        raise NotFoundException(f"Category '{category_id}' not found")

    if payload.slug and payload.slug != existing.slug:
        slug_taken = await prisma.category.find_unique(where={"slug": payload.slug})
        if slug_taken:
            raise ConflictException(f"Category slug '{payload.slug}' is already in use")

    update_data: dict[str, Any] = {}
    if payload.name is not None:
        update_data["name"] = payload.name
    if payload.slug is not None:
        update_data["slug"] = payload.slug
    if payload.available is not None:
        update_data["available"] = payload.available
    if payload.role is not None:
        update_data["role"] = payload.role
    if payload.side is not None:
        update_data["side"] = payload.side
    if payload.description is not None:
        update_data["description"] = payload.description
    if payload.tasks is not None:
        update_data["tasks"] = payload.tasks
    if payload.techs is not None:
        update_data["techs"] = _to_json_str(payload.techs)

    category = await prisma.category.update(
        where={"id": category_id},
        data=update_data,
    )
    return _serialize_category(category)


async def delete_category(category_id: str) -> DeleteResponse:
    """
    Delete a category and all its child levels/lessons (cascade).

    Raises:
        NotFoundException: If the category does not exist.
    """
    existing = await prisma.category.find_unique(where={"id": category_id})
    if existing is None:
        raise NotFoundException(f"Category '{category_id}' not found")

    await prisma.category.delete(where={"id": category_id})
    return DeleteResponse(message="Category deleted successfully", id=category_id)


# ── Level CRUD ────────────────────────────────────────────────────────────────
async def create_level(payload: LevelCreateRequest) -> LevelSummary:
    """
    Create a new level inside a category.

    Raises:
        NotFoundException: If the parent category does not exist.
        ConflictException: If the slug already exists within the same category.
    """
    category = await prisma.category.find_unique(where={"id": payload.category_id})
    if category is None:
        raise NotFoundException(f"Category '{payload.category_id}' not found")

    existing = await prisma.level.find_first(
        where={"category_id": payload.category_id, "slug": payload.slug}
    )
    if existing:
        raise ConflictException(
            f"Level slug '{payload.slug}' already exists in this category"
        )

    level = await prisma.level.create(
        data={
            "category_id": payload.category_id,
            "number": payload.number,
            "title": payload.title,
            "slug": payload.slug,
            "subtitle": payload.subtitle,
            "description": payload.description,
            "duration": payload.duration,
            "difficulty": payload.difficulty,
            "accent_color": payload.accent_color,
            "mini_project": payload.mini_project,
            "quiz_count": payload.quiz_count,
            "tags": _to_json_str(payload.tags),
            "coming_soon": payload.coming_soon,
        },
        include={"lessons": True},
    )
    return _serialize_level(level)


async def update_level(level_id: str, payload: LevelUpdateRequest) -> LevelSummary:
    """
    Partially update a level.

    Raises:
        NotFoundException: If the level or new category_id does not exist.
        ConflictException: If the new slug conflicts within the same category.
    """
    existing = await prisma.level.find_unique(
        where={"id": level_id}, include={"lessons": True}
    )
    if existing is None:
        raise NotFoundException(f"Level '{level_id}' not found")

    target_category_id = payload.category_id or existing.category_id

    if payload.category_id and payload.category_id != existing.category_id:
        cat = await prisma.category.find_unique(where={"id": payload.category_id})
        if cat is None:
            raise NotFoundException(f"Category '{payload.category_id}' not found")

    if payload.slug and payload.slug != existing.slug:
        slug_taken = await prisma.level.find_first(
            where={"category_id": target_category_id, "slug": payload.slug}
        )
        if slug_taken:
            raise ConflictException(
                f"Level slug '{payload.slug}' already exists in this category"
            )

    update_data: dict[str, Any] = {}
    if payload.category_id is not None:
        update_data["category_id"] = payload.category_id
    if payload.number is not None:
        update_data["number"] = payload.number
    if payload.title is not None:
        update_data["title"] = payload.title
    if payload.slug is not None:
        update_data["slug"] = payload.slug
    if payload.subtitle is not None:
        update_data["subtitle"] = payload.subtitle
    if payload.description is not None:
        update_data["description"] = payload.description
    if payload.duration is not None:
        update_data["duration"] = payload.duration
    if payload.difficulty is not None:
        update_data["difficulty"] = payload.difficulty
    if payload.accent_color is not None:
        update_data["accent_color"] = payload.accent_color
    if payload.mini_project is not None:
        update_data["mini_project"] = payload.mini_project
    if payload.quiz_count is not None:
        update_data["quiz_count"] = payload.quiz_count
    if payload.tags is not None:
        update_data["tags"] = _to_json_str(payload.tags)
    if payload.coming_soon is not None:
        update_data["coming_soon"] = payload.coming_soon

    level = await prisma.level.update(
        where={"id": level_id},
        data=update_data,
        include={"lessons": True},
    )
    return _serialize_level(level)


async def delete_level(level_id: str) -> DeleteResponse:
    """
    Delete a level and all its child lessons (cascade).

    Raises:
        NotFoundException: If the level does not exist.
    """
    existing = await prisma.level.find_unique(where={"id": level_id})
    if existing is None:
        raise NotFoundException(f"Level '{level_id}' not found")

    await prisma.level.delete(where={"id": level_id})
    return DeleteResponse(message="Level deleted successfully", id=level_id)


# ── Lesson CRUD ───────────────────────────────────────────────────────────────
async def create_lesson(payload: LessonCreateRequest) -> LessonDetail:
    """
    Create a new lesson inside a level.

    Raises:
        NotFoundException: If the parent level does not exist.
        ConflictException: If the slug already exists within the same level.
    """
    level = await prisma.level.find_unique(where={"id": payload.level_id})
    if level is None:
        raise NotFoundException(f"Level '{payload.level_id}' not found")

    existing = await prisma.lesson.find_first(
        where={"level_id": payload.level_id, "slug": payload.slug}
    )
    if existing:
        raise ConflictException(
            f"Lesson slug '{payload.slug}' already exists in this level"
        )

    lesson = await prisma.lesson.create(
        data={
            "level_id": payload.level_id,
            "title": payload.title,
            "slug": payload.slug,
            "summary": payload.summary,
            "content": payload.content,
            "duration": payload.duration,
            "order_index": payload.order_index,
            "video_url": payload.video_url,
        }
    )
    return _serialize_lesson(lesson)


async def update_lesson(lesson_id: str, payload: LessonUpdateRequest) -> LessonDetail:
    """
    Partially update a lesson, including its markdown content.

    Raises:
        NotFoundException: If the lesson or new level_id does not exist.
        ConflictException: If the new slug conflicts within the same level.
    """
    existing = await prisma.lesson.find_unique(where={"id": lesson_id})
    if existing is None:
        raise NotFoundException(f"Lesson '{lesson_id}' not found")

    target_level_id = payload.level_id or existing.level_id

    if payload.level_id and payload.level_id != existing.level_id:
        lvl = await prisma.level.find_unique(where={"id": payload.level_id})
        if lvl is None:
            raise NotFoundException(f"Level '{payload.level_id}' not found")

    if payload.slug and payload.slug != existing.slug:
        slug_taken = await prisma.lesson.find_first(
            where={"level_id": target_level_id, "slug": payload.slug}
        )
        if slug_taken:
            raise ConflictException(
                f"Lesson slug '{payload.slug}' already exists in this level"
            )

    update_data: dict[str, Any] = {}
    if payload.level_id is not None:
        update_data["level_id"] = payload.level_id
    if payload.title is not None:
        update_data["title"] = payload.title
    if payload.slug is not None:
        update_data["slug"] = payload.slug
    if payload.summary is not None:
        update_data["summary"] = payload.summary
    if payload.content is not None:
        update_data["content"] = payload.content
    if payload.duration is not None:
        update_data["duration"] = payload.duration
    if payload.order_index is not None:
        update_data["order_index"] = payload.order_index
    if payload.video_url is not None:
        update_data["video_url"] = payload.video_url

    lesson = await prisma.lesson.update(
        where={"id": lesson_id},
        data=update_data,
    )
    return _serialize_lesson(lesson)


async def delete_lesson(lesson_id: str) -> DeleteResponse:
    """
    Delete a lesson.

    Raises:
        NotFoundException: If the lesson does not exist.
    """
    existing = await prisma.lesson.find_unique(where={"id": lesson_id})
    if existing is None:
        raise NotFoundException(f"Lesson '{lesson_id}' not found")

    await prisma.lesson.delete(where={"id": lesson_id})
    return DeleteResponse(message="Lesson deleted successfully", id=lesson_id)
