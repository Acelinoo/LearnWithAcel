"use client";

/**
 * Viewer badge that live-updates when its entity is tracked.
 *
 * Subscribes to the global view-update event bus, so when the user
 * lands on a page that fires `useViewTracker` for the same entity,
 * the count animates up without a refresh.
 *
 * The variants mirror the older static `<ViewerBadge>` and
 * `<LessonViewerBadge>` so existing layouts keep working — just swap
 * the import and pass `entityType` + `entityId`.
 */

import { useEffect, useState } from "react";
import { Eye } from "lucide-react";
import type { EntityType } from "@/lib/api/views";
import { onViewUpdate } from "@/lib/progress-events";
import { formatNumber, cn } from "@/lib/utils";

type Variant = "pill" | "compact" | "inline";

type Props = {
  entityType: EntityType;
  entityId: string | null | undefined;
  /** Initial count from the server (e.g. lesson.views or
   *  lesson.base_viewers). The badge animates upward from this number. */
  initial: number;
  /** Show the "viewers" label after the number. */
  showLabel?: boolean;
  /** Visual variant. `pill` matches the original `ViewerBadge`,
   *  `compact` matches `LessonViewerBadge`, `inline` is plain text. */
  variant?: Variant;
  className?: string;
  iconSize?: number;
};

const PILL_CLASS =
  "inline-flex items-center gap-2 rounded-full border border-border bg-black/30 px-3 py-1.5 backdrop-blur-sm";
const COMPACT_CLASS =
  "inline-flex items-center gap-1.5 rounded-full border border-border bg-black/30 px-2.5 py-1 text-xs text-muted";
const INLINE_CLASS =
  "inline-flex items-center gap-1.5 text-xs text-muted";

export default function LiveViewerBadge({
  entityType,
  entityId,
  initial,
  showLabel = true,
  variant = "pill",
  className = "",
  iconSize = 12,
}: Props) {
  const [count, setCount] = useState(initial);

  // Re-sync if a new server-side render brings a different baseline.
  useEffect(() => setCount(initial), [initial]);

  useEffect(() => {
    if (!entityId) return;
    return onViewUpdate((u) => {
      if (u.entityType === entityType && u.entityId === entityId) {
        // Only ever move the badge upward — protects against stale
        // events that might arrive out of order.
        setCount((prev) => Math.max(prev, u.views));
      }
    });
  }, [entityType, entityId]);

  if (variant === "pill") {
    return (
      <div className={cn(PILL_CLASS, className)}>
        <span className="relative flex h-2 w-2">
          <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400/60" />
          <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-400" />
        </span>
        <Eye size={iconSize} className="text-muted" />
        <span className="text-xs text-muted">
          <span className="font-mono tabular-nums text-foreground transition-all duration-300">
            {formatNumber(count)}
          </span>
          {showLabel && " viewers"}
        </span>
      </div>
    );
  }

  if (variant === "compact") {
    return (
      <span className={cn(COMPACT_CLASS, className)}>
        <Eye size={iconSize} />
        <span className="font-mono tabular-nums text-foreground transition-all duration-300">
          {formatNumber(count)}
        </span>
        {showLabel && <span>viewers</span>}
      </span>
    );
  }

  return (
    <span className={cn(INLINE_CLASS, className)}>
      <Eye size={iconSize} />
      <span className="font-mono tabular-nums text-foreground transition-all duration-300">
        {formatNumber(count)}
      </span>
      {showLabel && <span>viewers</span>}
    </span>
  );
}
