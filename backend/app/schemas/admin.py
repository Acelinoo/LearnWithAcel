"""
Pydantic schemas for admin / CMS endpoints.

All write operations (create / update) use separate request models so that
optional fields on update don't bleed into create validation.
"""

from typing import Any

from pydantic import BaseModel, Field


# ── Category ──────────────────────────────────────────────────────────────────
class CategoryCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=100, pattern=r"^[a-z0-9-]+$")
    available: bool = False
    role: str = Field(..., min_length=1, max_length=100)
    side: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    tasks: str = Field(..., min_length=1)
    # JSON array: [{ "label": "Dasar", "items": ["HTML", "CSS"] }]
    techs: Any = Field(..., description="JSON array of tech groups")


class CategoryUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    slug: str | None = Field(None, min_length=1, max_length=100, pattern=r"^[a-z0-9-]+$")
    available: bool | None = None
    role: str | None = Field(None, min_length=1, max_length=100)
    side: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, min_length=1)
    tasks: str | None = Field(None, min_length=1)
    techs: Any | None = None


# ── Level ─────────────────────────────────────────────────────────────────────
class LevelCreateRequest(BaseModel):
    category_id: str = Field(..., description="UUID of the parent category")
    number: int = Field(..., ge=0)
    title: str = Field(..., min_length=1, max_length=200)
    slug: str = Field(..., min_length=1, max_length=200, pattern=r"^[a-z0-9-]+$")
    subtitle: str = Field(..., min_length=1, max_length=300)
    description: str = Field(..., min_length=1)
    duration: str = Field(..., min_length=1, max_length=100)
    difficulty: str = Field(..., min_length=1, max_length=100)
    accent_color: str = Field(..., min_length=1, max_length=200)
    mini_project: str = Field(..., min_length=1, max_length=300)
    quiz_count: int = Field(0, ge=0)
    base_viewers: int = Field(0, ge=0)
    # JSON array of strings: ["HTML5", "CSS3"]
    tags: Any = Field(default=[], description="JSON array of tag strings")
    coming_soon: bool = False


class LevelUpdateRequest(BaseModel):
    category_id: str | None = None
    number: int | None = Field(None, ge=0)
    title: str | None = Field(None, min_length=1, max_length=200)
    slug: str | None = Field(None, min_length=1, max_length=200, pattern=r"^[a-z0-9-]+$")
    subtitle: str | None = Field(None, min_length=1, max_length=300)
    description: str | None = Field(None, min_length=1)
    duration: str | None = Field(None, min_length=1, max_length=100)
    difficulty: str | None = Field(None, min_length=1, max_length=100)
    accent_color: str | None = Field(None, min_length=1, max_length=200)
    mini_project: str | None = Field(None, min_length=1, max_length=300)
    quiz_count: int | None = Field(None, ge=0)
    base_viewers: int | None = Field(None, ge=0)
    tags: Any | None = None
    coming_soon: bool | None = None


# ── Lesson ────────────────────────────────────────────────────────────────────
class LessonCreateRequest(BaseModel):
    level_id: str = Field(..., description="UUID of the parent level")
    title: str = Field(..., min_length=1, max_length=300)
    slug: str = Field(..., min_length=1, max_length=300, pattern=r"^[a-z0-9-]+$")
    summary: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1, description="Lesson body in Markdown format")
    duration: str = Field(..., min_length=1, max_length=100)
    base_viewers: int = Field(0, ge=0)
    order_index: int = Field(..., ge=1, description="Display order within the level (1-based)")


class LessonUpdateRequest(BaseModel):
    level_id: str | None = None
    title: str | None = Field(None, min_length=1, max_length=300)
    slug: str | None = Field(None, min_length=1, max_length=300, pattern=r"^[a-z0-9-]+$")
    summary: str | None = Field(None, min_length=1)
    content: str | None = Field(None, min_length=1, description="Lesson body in Markdown format")
    duration: str | None = Field(None, min_length=1, max_length=100)
    base_viewers: int | None = Field(None, ge=0)
    order_index: int | None = Field(None, ge=1)


# ── Shared response ───────────────────────────────────────────────────────────
class DeleteResponse(BaseModel):
    message: str
    id: str
