"use client";

import { useStoredCount } from "@/hooks/useViewerCount";
import { formatNumber } from "@/lib/utils";

function Bar({ level, max }) {
  const { count, ready } = useStoredCount(
    `lwa_level_viewers_${level.slug}`,
    level.viewers
  );
  const value = ready ? count : level.viewers;
  const h = Math.max(20, (value / max) * 100);
  return (
    <div className="flex-1">
      <div
        className="rounded-md bg-gradient-to-t from-accent/60 to-accent-hover transition-all duration-700"
        style={{ height: `${h}px` }}
        title={`${level.title}: ${formatNumber(value)} viewers`}
      />
      <div className="mt-2 text-center font-mono text-[10px] text-muted">
        L{level.number}
      </div>
    </div>
  );
}

export default function ViewerBarChart({ levels }) {
  const max = Math.max(...levels.map((l) => l.viewers));
  return (
    <div className="flex items-end gap-2">
      {levels.map((l) => (
        <Bar key={l.id} level={l} max={max} />
      ))}
    </div>
  );
}
