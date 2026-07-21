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

    # Engagement details — populated only when this completion was the
    # one that flipped is_completed from false to true (so frontend can
    # show celebration / XP burst). Otherwise these fields stay zero.
    xp_earned: int = 0
    new_total_xp: int = 0
    streak: int = 0
    just_completed: bool = False

    model_config = {"from_attributes": True}


class LevelStats(BaseModel):
    level_id: str
    level_title: str
    level_slug: str
    category_slug: str | None = None
    total_lessons: int
    completed_lessons: int
    percentage: float


class ContinueLesson(BaseModel):
    """Resolved 'continue learning' target for a user."""

    lesson_id: str
    lesson_slug: str
    lesson_title: str
    level_id: str
    level_slug: str
    level_title: str
    level_number: int
    category_slug: str | None = None


class StatsResponse(BaseModel):
    total_lessons: int
    completed_lessons: int
    overall_percentage: float
    by_level: list[LevelStats]

    # Flat list of lesson IDs the user has completed. Lets the lesson
    # sidebar light up the right rows without an extra fetch.
    completed_lesson_ids: list[str] = []

    # Engagement
    xp_total: int = 0
    current_streak: int = 0
    longest_streak: int = 0
    last_activity_at: str | None = None

    # Resolved next lesson the user should continue with. Null if there
    # is no obvious continuation (e.g. user just signed up).
    continue_lesson: ContinueLesson | None = None


class LessonOpenResponse(BaseModel):
    """Returned by POST /progress/view/{lesson_id}.

    Remembers which lesson the user opened so the dashboard's
    "Continue learning" stays accurate.
    """

    lesson_id: str
    views: int = 0
    last_opened_at: str
