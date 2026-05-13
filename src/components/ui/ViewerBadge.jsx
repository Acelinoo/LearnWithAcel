"use client";

import { Eye } from "lucide-react";
import { useViewerCount } from "@/hooks/useViewerCount";
import { formatNumber } from "@/lib/utils";

export default function ViewerBadge({ compact = false, className = "" }) {
  const { count, ready } = useViewerCount();

  return (
    <div
      className={
        "inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.03] px-3 py-1.5 backdrop-blur-sm " +
        className
      }
    >
      <span className="relative flex h-2 w-2">
        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400/60" />
        <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-400" />
      </span>
      <Eye size={12} className="text-muted" />
      <span className="text-xs text-muted">
        <span
          className="font-mono text-foreground tabular-nums"
          aria-live="polite"
        >
          {ready ? formatNumber(count) : "1,000"}
        </span>
        {!compact && " viewers"}
      </span>
    </div>
  );
}
