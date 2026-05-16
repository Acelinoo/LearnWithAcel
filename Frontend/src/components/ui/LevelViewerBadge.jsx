import { Eye } from "lucide-react";
import { formatNumber } from "@/lib/utils";

/**
 * Static level viewer badge — the count comes straight from the level's
 * `base_viewers` field on the backend.
 */
export default function LevelViewerBadge({
  count = 0,
  size = "sm",
  className = "",
}) {
  const sizes = {
    xs: "px-2 py-0.5 text-[10px]",
    sm: "px-2 py-0.5 text-[11px]",
  };

  return (
    <span
      className={
        "inline-flex items-center gap-1.5 rounded-full border border-border bg-black/30 text-muted " +
        sizes[size] +
        " " +
        className
      }
    >
      <Eye size={10} />
      <span className="font-mono text-foreground tabular-nums">
        {formatNumber(count)}
      </span>
      viewers
    </span>
  );
}
