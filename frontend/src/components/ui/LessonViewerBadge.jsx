import { Eye } from "lucide-react";
import { formatNumber } from "@/lib/utils";

/**
 * Static lesson viewer badge backed by the lesson's `base_viewers` field
 * on the backend.
 */
export default function LessonViewerBadge({
  count = 0,
  showLabel = true,
  bordered = true,
  iconSize = 12,
  className = "",
}) {
  const base = bordered
    ? "inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/[0.03] px-2.5 py-1 text-xs text-muted"
    : "inline-flex items-center gap-1.5 text-xs text-muted";

  return (
    <span className={base + " " + className}>
      <Eye size={iconSize} />
      <span className="font-mono tabular-nums text-foreground">
        {formatNumber(count)}
      </span>
      {showLabel && <span>viewers</span>}
    </span>
  );
}
