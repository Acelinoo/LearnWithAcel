"use client";

/**
 * Backwards-compatible wrapper around the universal `<ViewTracker>`.
 * Existing imports keep working — internally it now goes through the
 * shared tracking infrastructure so view counts increment uniformly
 * across the app.
 */

import ViewTracker from "@/components/ui/ViewTracker";

type Props = { lessonId: string };

export default function LessonViewTracker({ lessonId }: Props) {
  return <ViewTracker entityType="lesson" entityId={lessonId} />;
}
