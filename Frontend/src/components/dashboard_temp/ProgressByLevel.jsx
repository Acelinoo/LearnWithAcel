import { formatNumber } from "@/lib/utils";

/**
 * Visualises per-level completion percentage from /api/v1/progress/stats.
 * Pure presentational — receives the `by_level` array as a prop.
 */
export default function ProgressByLevel({ byLevel }) {
  if (!byLevel?.length) {
    return (
      <p className="text-sm text-muted">
        Belum ada progress. Selesaikan materi pertama kamu untuk mulai
        menumpuk angka di sini.
      </p>
    );
  }

  return (
    <ul className="space-y-3">
      {byLevel.map((row) => (
        <li key={row.level_id}>
          <div className="flex items-center justify-between gap-2 text-sm">
            <span className="truncate font-medium text-foreground">
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
  );
}
