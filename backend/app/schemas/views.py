"""
Pydantic schemas for the universal view-tracking API.
"""

from typing import Literal

from pydantic import BaseModel, Field


# Allowed entity types. Add new types here when expanding tracking
# coverage (project pages, blog posts, etc.). Backend rejects anything
# outside this allowlist to keep the table tidy.
EntityType = Literal[
    "lesson",
    "level",
    "category",
    "page",
    "project",
]


class TrackViewRequest(BaseModel):
    """Body for POST /api/v1/views/track."""

    entity_type: EntityType
    entity_id: str = Field(..., min_length=1, max_length=128)
    pathname: str | None = Field(None, max_length=512)


class TrackViewResponse(BaseModel):
    """Returned after successfully recording a view."""

    entity_type: EntityType
    entity_id: str
    views: int
    pathname: str | None = None
    tracked_at: str
