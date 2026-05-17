"""
Universal view-tracking service.

Each call records an event in `EntityView` and bumps the aggregate
`views` counter on the matching entity table when one exists. A small
handler registry keeps support per entity type isolated, so adding new
types stays mechanical.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Awaitable, Callable

from app.core.database import prisma
from app.core.exceptions import NotFoundException
from app.schemas.views import EntityType, TrackViewResponse


# ─────────────────────────────────────────────────────────────────────────────
# Per-entity bump handlers
# ─────────────────────────────────────────────────────────────────────────────


async def _bump_lesson(entity_id: str) -> int:
    record = await prisma.lesson.find_unique(where={"id": entity_id})
    if record is None:
        raise NotFoundException(f"Lesson '{entity_id}' not found")
    updated = await prisma.lesson.update(
        where={"id": entity_id},
        data={"views": {"increment": 1}},
    )
    return updated.views or 0


async def _bump_level(entity_id: str) -> int:
    record = await prisma.level.find_unique(where={"id": entity_id})
    if record is None:
        raise NotFoundException(f"Level '{entity_id}' not found")
    updated = await prisma.level.update(
        where={"id": entity_id},
        data={"views": {"increment": 1}},
    )
    return updated.views or 0


async def _bump_category(entity_id: str) -> int:
    record = await prisma.category.find_unique(where={"id": entity_id})
    if record is None:
        raise NotFoundException(f"Category '{entity_id}' not found")
    updated = await prisma.category.update(
        where={"id": entity_id},
        data={"views": {"increment": 1}},
    )
    return updated.views or 0


async def _bump_event_only(entity_id: str) -> int:
    """For entity types that don't have an aggregate column on their own
    table (e.g. arbitrary `page` URLs). We compute the count from
    `EntityView` rows directly."""
    return await prisma.entityview.count(
        where={"entity_type_id": entity_id},  # placeholder, see below
    ) if False else 0  # noqa: SIM222 — kept for clarity


# Type → handler. The handler is responsible for validating the entity
# exists (or skipping that check for `page`-style entities) and bumping
# any aggregate column. Returns the new view count for the entity.
ENTITY_HANDLERS: dict[EntityType, Callable[[str], Awaitable[int]]] = {
    "lesson": _bump_lesson,
    "level": _bump_level,
    "category": _bump_category,
}


# ─────────────────────────────────────────────────────────────────────────────
# Public API
# ─────────────────────────────────────────────────────────────────────────────


async def track_view(
    *,
    entity_type: EntityType,
    entity_id: str,
    user_id: str | None,
    pathname: str | None,
) -> TrackViewResponse:
    """Record a single view event.

    1. Append a row in `EntityView` for analytics.
    2. Bump the aggregate counter on the entity's own table when one
       exists (lesson/level/category have their own `views` column).
    3. Return the new aggregate count.

    The handler registry makes adding new types trivial — register a
    new entry in `ENTITY_HANDLERS` and the rest of the pipeline (event
    logging, validation, route surface) keeps working.
    """
    now = datetime.now(timezone.utc)

    # 1. Append the event log row first. Always do this — it's the
    #    foundation for analytics and recommendations later.
    await prisma.entityview.create(
        data={
            "entity_type": entity_type,
            "entity_id": entity_id,
            "user_id": user_id,
            "pathname": pathname,
            "created_at": now,
        },
    )

    # 2. Bump the aggregate column for known entity types.
    handler = ENTITY_HANDLERS.get(entity_type)
    if handler is not None:
        try:
            views = await handler(entity_id)
        except NotFoundException:
            # Entity disappeared between auth and the bump — fall back
            # to counting events for this id.
            views = await prisma.entityview.count(
                where={"entity_type": entity_type, "entity_id": entity_id},
            )
    else:
        # No aggregate column for this entity type — just count events.
        views = await prisma.entityview.count(
            where={"entity_type": entity_type, "entity_id": entity_id},
        )

    return TrackViewResponse(
        entity_type=entity_type,
        entity_id=entity_id,
        views=views,
        pathname=pathname,
        tracked_at=now.isoformat(),
    )
