"""
Pydantic schemas for roadmap and lesson content endpoints.
"""

from typing import Any

from pydantic import BaseModel


# ── Lesson ────────────────────────────────────────────────────────────────────
class LessonSummary(BaseModel):
    """Lightweight lesson info used inside level listings."""

    id: str
    title: str
    slug: str
    summary: str
    duration: str
    order_index: int
    xp_reward: int = 50
    is_project: bool = False

    model_config = {"from_attributes": True}


class LessonDetail(BaseModel):
    """Full lesson detail including markdown content."""

    id: str
    title: str
    slug: str
    summary: str
    content: str
    duration: str
    order_index: int
    level_id: str
    xp_reward: int = 50
    is_project: bool = False
    criteria: list[str] | None = None
    hints: str | None = None

    model_config = {"from_attributes": True}


# ── Level ─────────────────────────────────────────────────────────────────────
class LevelSummary(BaseModel):
    """Level info used inside category/roadmap listings."""

    id: str
    number: int
    title: str
    slug: str
    subtitle: str
    description: str
    duration: str
    difficulty: str
    accent_color: str
    mini_project: str
    quiz_count: int
    tags: Any  # JSON array of strings
    coming_soon: bool
    lessons: list[LessonSummary]

    model_config = {"from_attributes": True}


# ── Category ──────────────────────────────────────────────────────────────────
class CategoryResponse(BaseModel):
    id: str
    name: str
    slug: str
    available: bool
    role: str
    side: str
    description: str
    tasks: str
    techs: Any  # JSON array of objects

    model_config = {"from_attributes": True}


class RoadmapResponse(BaseModel):
    """Full roadmap for a single category, including all levels and lessons."""

    category: CategoryResponse
    levels: list[LevelSummary]
