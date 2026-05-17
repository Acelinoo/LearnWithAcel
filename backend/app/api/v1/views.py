"""
Universal view-tracking route.

Frontend posts to this endpoint from any page that wants to count a
visit toward an entity (lesson, level, category, project, …). Auth is
optional — anonymous visitors still get tracked, the user_id column is
just left null in the event log.
"""

from fastapi import APIRouter, Depends, Request

from app.core.database import prisma
from app.core.security import decode_access_token
from app.schemas.views import TrackViewRequest, TrackViewResponse
from app.services import views_service

router = APIRouter(prefix="/views", tags=["Views"])


async def _resolve_user(request: Request) -> str | None:
    """Best-effort user resolution. Reads the Authorization header if
    present, otherwise returns None for anonymous visitors."""
    auth = request.headers.get("authorization") or request.headers.get(
        "Authorization"
    )
    if not auth or not auth.lower().startswith("bearer "):
        return None
    token = auth.split(" ", 1)[1].strip()
    try:
        user_id = decode_access_token(token)
    except Exception:
        return None
    user = await prisma.user.find_unique(where={"id": user_id})
    return user.id if user else None


@router.post(
    "/track",
    response_model=TrackViewResponse,
    summary="Track a view of any entity (lesson, level, category, page, …)",
)
async def track_view(
    payload: TrackViewRequest,
    request: Request,
    user_id: str | None = Depends(_resolve_user),
) -> TrackViewResponse:
    """
    Record a single view of the given entity. Logs an event row and,
    when an aggregate column exists, increments it.

    Frontend should debounce per `(entity_type, entity_id)` so a quick
    refresh of the same page doesn't inflate the count.
    """
    return await views_service.track_view(
        entity_type=payload.entity_type,
        entity_id=payload.entity_id,
        user_id=user_id,
        pathname=payload.pathname,
    )
