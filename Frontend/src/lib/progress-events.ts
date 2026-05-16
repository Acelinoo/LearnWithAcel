/**
 * Browser-only event bus for progression updates.
 *
 * The mark-as-complete flow needs to ripple through several disjoint
 * components (lesson sidebar progress, dashboard XP, "continue learning"
 * card, navbar streak chip, …). They all live in different parts of the
 * render tree, so we use a thin window-scoped CustomEvent to broadcast
 * the new totals after a successful completion.
 *
 * Server-component pages still need `router.refresh()` to re-fetch the
 * canonical state from the API, but listeners can apply optimistic
 * updates instantly so the UI never feels laggy.
 */

export const PROGRESS_EVENT = "learnwithacel:progress-updated";
export const VIEW_EVENT = "learnwithacel:view-tracked";

export type ProgressUpdate = {
  lessonId: string;
  levelId?: string;
  /** True when this completion just flipped is_completed false → true. */
  justCompleted: boolean;
  /** XP earned by this specific completion (0 if it was a no-op). */
  xpEarned: number;
  /** Authoritative new XP total after the update. */
  newTotalXp: number;
  /** Daily streak count after the update. */
  streak: number;
};

export type ViewUpdate = {
  lessonId: string;
  views: number;
};

export function emitProgressUpdate(update: ProgressUpdate): void {
  if (typeof window === "undefined") return;
  window.dispatchEvent(
    new CustomEvent<ProgressUpdate>(PROGRESS_EVENT, { detail: update }),
  );
}

export function emitViewUpdate(update: ViewUpdate): void {
  if (typeof window === "undefined") return;
  window.dispatchEvent(
    new CustomEvent<ViewUpdate>(VIEW_EVENT, { detail: update }),
  );
}

export function onProgressUpdate(
  handler: (update: ProgressUpdate) => void,
): () => void {
  if (typeof window === "undefined") return () => {};
  const listener = (e: Event) => {
    const detail = (e as CustomEvent<ProgressUpdate>).detail;
    if (detail) handler(detail);
  };
  window.addEventListener(PROGRESS_EVENT, listener);
  return () => window.removeEventListener(PROGRESS_EVENT, listener);
}

export function onViewUpdate(
  handler: (update: ViewUpdate) => void,
): () => void {
  if (typeof window === "undefined") return () => {};
  const listener = (e: Event) => {
    const detail = (e as CustomEvent<ViewUpdate>).detail;
    if (detail) handler(detail);
  };
  window.addEventListener(VIEW_EVENT, listener);
  return () => window.removeEventListener(VIEW_EVENT, listener);
}
