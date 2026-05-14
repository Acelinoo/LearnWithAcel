"""
Pydantic schemas for user progress endpoints.
"""

from pydantic import BaseModel


class ProgressResponse(BaseModel):
    id: str
    user_id: str
    lesson_id: str
    is_completed: bool
    completed_at: str | None

    model_config = {"from_attributes": True}


class LevelStats(BaseModel):
    level_id: str
    level_title: str
    level_slug: str
    total_lessons: int
    completed_lessons: int
    percentage: float


class StatsResponse(BaseModel):
    total_lessons: int
    completed_lessons: int
    overall_percentage: float
    by_level: list[LevelStats]
