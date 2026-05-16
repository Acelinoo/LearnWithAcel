"use client";

/**
 * Fires a single `POST /progress/view/{lesson_id}` per page open.
 *
 * Behaviour:
 *   - Only fires when the user is logged in.
 *   - Debounced via sessionStorage so quick refreshes don't inflate
 *     view counts. The same lesson can only be re-counted once per
 *     browser session.
 *   - Silently swallows 401 — view tracking is best-effort, not a
 *     blocker.
 *
 * Mount once per lesson page. The component itself renders nothing.
 */

import { useEffect } from "react";
import { trackLessonView } from "@/lib/api/progress";
import { ApiError } from "@/lib/api/client";
import { emitViewUpdate } from "@/lib/progress-events";
import { useAuth } from "@/components/providers/AuthProvider";

const SESSION_KEY = "learnwithacel:viewed";

function readViewedSet(): Set<string> {
  if (typeof window === "undefined") return new Set();
  try {
    const raw = sessionStorage.getItem(SESSION_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw);
    return new Set(Array.isArray(arr) ? arr : []);
  } catch {
    return new Set();
  }
}

function writeViewedSet(set: Set<string>): void {
  if (typeof window === "undefined") return;
  try {
    sessionStorage.setItem(SESSION_KEY, JSON.stringify([...set]));
  } catch {
    // Ignore quota errors — graceful degradation.
  }
}

type Props = {
  lessonId: string;
};

export default function LessonViewTracker({ lessonId }: Props) {
  const { token, loading } = useAuth();

  useEffect(() => {
    if (loading || !token || !lessonId) return;
    const viewed = readViewedSet();
    if (viewed.has(lessonId)) return;

    let cancelled = false;
    (async () => {
      try {
        const result = await trackLessonView(lessonId, token);
        if (cancelled) return;
        viewed.add(lessonId);
        writeViewedSet(viewed);
        emitViewUpdate({
          lessonId: result.lesson_id,
          views: result.views,
        });
      } catch (err) {
        // 401 is fine — view tracking shouldn't block reading.
        if (err instanceof ApiError && err.status === 401) return;
        // Anything else: best-effort, don't surface to user.
        if (process.env.NODE_ENV !== "production") {
          console.warn("[LessonViewTracker] failed:", err);
        }
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [token, loading, lessonId]);

  return null;
}
