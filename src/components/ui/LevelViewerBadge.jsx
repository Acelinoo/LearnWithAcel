"use client";

import { Eye } from "lucide-react";
import { useLevelViewerCount } from "@/hooks/useViewerCount";
import { formatNumber } from "@/lib/utils";

export default function LevelViewerBadge({
  levelSlug,
  seed,
  size = "sm",
  className = "",
}) {
  const { count, ready } = useLevelViewerCount(levelSlug, seed);

  const sizes = {
    xs: "px-2 py-0.5 text-[10px]",
    sm: "px-2 py-0.5 text-[11px]",
  };

  return (
    <span
      className={
        "inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/[0.03] text-muted " +
        sizes[size] +
        " " +
        className
      }
    >
      <Eye size={10} />
      <span className="font-mono text-foreground tabular-nums">
        {ready ? formatNumber(count) : formatNumber(seed)}
      </span>
      viewers
    </span>
  );
}
