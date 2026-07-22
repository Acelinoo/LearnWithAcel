"use client";

import { useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";
import { formatNumber } from "@/lib/utils";

/**
 * Visualises per-level completion percentage from /api/v1/progress/stats.
 * Shows up to 3 items by default, expandable via a toggle button.
 */
export default function ProgressByLevel({ byLevel }) {
  const [isExpanded, setIsExpanded] = useState(false);

  if (!byLevel?.length) {
    return (
      <p className="text-sm text-muted">
        Belum ada progress. Selesaikan materi pertama kamu untuk mulai
        menumpuk angka di sini.
      </p>
    );
  }

  const visibleLevels = isExpanded ? byLevel : byLevel.slice(0, 3);
  const hasMore = byLevel.length > 3;

  return (
    <div>
      <ul className="space-y-3">
        {visibleLevels.map((row) => (
          <li key={row.level_id} className="animate-fade-in">
            <div className="flex items-center justify-between gap-2 text-sm">
              <span className="truncate font-medium text-foreground min-w-0">
                {row.level_title}
              </span>
              <span className="shrink-0 font-mono text-xs text-muted tabular-nums">
                {formatNumber(row.completed_lessons)} / {formatNumber(row.total_lessons)}
              </span>
            </div>
            <div className="mt-1.5 h-1 w-full overflow-hidden rounded-full bg-black/40">
              <div
                className="h-full rounded-full bg-gradient-to-r from-accent to-accent-hover transition-all duration-700"
                style={{ width: `${Math.min(100, row.percentage)}%` }}
              />
            </div>
            <div className="mt-1 text-right text-[11px] font-mono text-muted">
              {row.percentage.toFixed(1)}%
            </div>
          </li>
        ))}
      </ul>
      
      {hasMore && (
        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="mt-4 flex w-full items-center justify-center gap-1.5 rounded-xl border border-white/5 bg-white/[0.02] py-2 text-xs font-medium text-muted transition-colors hover:bg-white/[0.05] hover:text-foreground"
        >
          {isExpanded ? (
            <>
              Tampilkan lebih sedikit <ChevronUp size={14} />
            </>
          ) : (
            <>
              Tampilkan lebih banyak ({byLevel.length - 3}) <ChevronDown size={14} />
            </>
          )}
        </button>
      )}
    </div>
  );
}
