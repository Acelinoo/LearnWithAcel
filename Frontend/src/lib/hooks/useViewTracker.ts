"use client";

/**
 * Universal view-tracking hook.
 *
 * Usage:
 *
 *   useViewTracker({ entityType: "lesson", entityId: lesson.id });
 *
 * Behaviour:
 *   - Fires `POST /api/v1/views/track` once per session per
 *     (entityType, entityId) pair. Repeat refreshes within the same
 *     browser session are deduped via sessionStorage.
 *   - Optional cooldown (in minutes) for cases where the same visitor
 *     legitimately reopens an entity throughout a long session — e.g.
 *     dashboard tabs left open for hours.
 *   - 401s are swallowed silently (anonymous tracking still works).
 *   - On success, broadcasts a global event so other components (badge,
 *     hero, leaderboard) can sync optimistically without re-fetching.
 */

import { useEffect } from "react";
import { trackView, type EntityType } from "@/lib/api/views";
import { ApiError } from "@/lib/api/client";
import { emitViewUpdate } from "@/lib/progress-events";
import { useAuth } from "@/components/providers/AuthProvider";

type Options = {
  entityType: EntityType;
  entityId: string | undefined | null;
  /** Pathname the tracker should record. Defaults to current location. */
  pathname?: string;
  /** Skip tracking entirely (e.g. while loading). */
  enabled?: boolean;
  /** Cooldown in minutes before the same entity can be re-tracked in
   *  the same session. Default: never re-track within a session. */
  cooldownMinutes?: number;
};

const STORAGE_KEY = "learnwithacel:viewed-entities";

type ViewedRecord = {
  /** Unix ms timestamp of last successful track for this entity. */
  ts: number;
};

function readViewed(): Record<string, ViewedRecord> {
  if (typeof window === "undefined") return {};
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return {};
    const parsed = JSON.parse(raw);
    return typeof parsed === "object" && parsed !== null ? parsed : {};
  } catch {
    return {};
  }
}

function writeViewed(record: Record<string, ViewedRecord>): void {
  if (typeof window === "undefined") return;
  try {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(record));
  } catch {
    /* quota exhausted — graceful degradation */
  }
}

function debugLog(
  scope: string,
  payload: Record<string, unknown>,
): void {
  if (process.env.NODE_ENV !== "production") {
    // eslint-disable-next-line no-console
    console.debug(`[viewTracker] ${scope}`, payload);
  }
}

export function useViewTracker({
  entityType,
  entityId,
  pathname,
  enabled = true,
  cooldownMinutes,
}: Options): void {
  const { token, loading } = useAuth();

  useEffect(() => {
    if (!enabled || !entityId || loading) return;
    if (typeof window === "undefined") return;

    const key = `${entityType}:${entityId}`;
    const viewed = readViewed();
    const last = viewed[key];

    if (last) {
      if (cooldownMinutes && cooldownMinutes > 0) {
        const elapsed = (Date.now() - last.ts) / 60_000;
        if (elapsed < cooldownMinutes) {
          debugLog("skipped (cooldown)", { key, elapsed, cooldownMinutes });
          return;
        }
      } else {
        debugLog("skipped (already tracked this session)", { key });
        return;
      }
    }

    let cancelled = false;
    const resolvedPath =
      pathname ??
      (typeof window !== "undefined" ? window.location.pathname : undefined);

    debugLog("tracking", { key, pathname: resolvedPath, hasToken: !!token });

    (async () => {
      try {
        const result = await trackView(
          {
            entity_type: entityType,
            entity_id: entityId,
            pathname: resolvedPath ?? null,
          },
          token,
        );
        if (cancelled) return;

        debugLog("ok", {
          key,
          views: result.views,
          tracked_at: result.tracked_at,
        });

        // Persist debounce.
        viewed[key] = { ts: Date.now() };
        writeViewed(viewed);

        // Broadcast for optimistic UI bumps.
        emitViewUpdate({
          entityType,
          entityId,
          views: result.views,
        });
      } catch (err) {
        if (err instanceof ApiError && err.status === 401) {
          debugLog("anonymous track (401 swallowed)", { key });
          return;
        }
        debugLog("error", { key, err });
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [entityType, entityId, pathname, enabled, cooldownMinutes, token, loading]);
}
