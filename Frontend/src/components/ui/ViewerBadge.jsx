import { Eye } from "lucide-react";
import { formatNumber } from "@/lib/utils";

/**
 * Static viewer badge backed by the `base_viewers` field returned by the
 * FastAPI backend. There is no shared counter / polling — the number is
 * the authored value from the CMS, which is what the dashboard already
 * exposes via /progress/stats.
 */
export default function ViewerBadge({
  count = 0,
  compact = false,
  className = "",
}) {
  return (
    <div
      className={
        "inline-flex items-center gap-2 rounded-full border border-border bg-black/30 px-3 py-1.5 backdrop-blur-sm " +
        className
      }
    >
      <span className="relative flex h-2 w-2">
        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400/60" />
        <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-400" />
      </span>
      <Eye size={12} className="text-muted" />
      <span className="text-xs text-muted">
        <span className="font-mono text-foreground tabular-nums">
          {formatNumber(count)}
        </span>
        {!compact && " viewers"}
      </span>
    </div>
  );
}
