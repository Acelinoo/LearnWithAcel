/**
 * Universal view-tracking API client.
 *
 *   POST /api/v1/views/track
 *
 * Token is optional — anonymous visitors still get tracked. The server
 * records `user_id = null` for them and the call succeeds either way.
 */

import { apiFetch } from "./client";

/** Allowed entity types — keep in sync with `app/schemas/views.py`. */
export type EntityType =
  | "lesson"
  | "level"
  | "category"
  | "page"
  | "project";

export type TrackViewRequest = {
  entity_type: EntityType;
  entity_id: string;
  pathname?: string | null;
};

export type TrackViewResponse = {
  entity_type: EntityType;
  entity_id: string;
  views: number;
  pathname?: string | null;
  tracked_at: string;
};

export function trackView(
  payload: TrackViewRequest,
  token?: string | null,
): Promise<TrackViewResponse> {
  return apiFetch<TrackViewResponse>("/api/v1/views/track", {
    method: "POST",
    body: payload,
    token: token ?? null,
  });
}
