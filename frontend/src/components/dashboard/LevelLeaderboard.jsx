import Link from "next/link";
import { formatNumber } from "@/lib/utils";

function Row({ level, max }) {
  const value = level.base_viewers || 0;
  const pct = Math.max(4, (value / max) * 100);
  return (
    <li>
      <Link href={`/roadmap#${level.slug}`} className="group block">
        <div className="flex items-center justify-between gap-2 text-sm">
          <span className="truncate font-medium text-foreground group-hover:text-accent-hover">
            {level.title}
          </span>
          <span className="shrink-0 font-mono text-xs text-muted tabular-nums">
            {formatNumber(value)}
          </span>
        </div>
        <div className="mt-1.5 h-1 w-full overflow-hidden rounded-full bg-white/[0.05]">
          <div
            className="h-full rounded-full bg-gradient-to-r from-accent to-accent-hover transition-all duration-700"
            style={{ width: `${pct}%` }}
          />
        </div>
      </Link>
    </li>
  );
}

export default function LevelLeaderboard({ levels }) {
  if (!levels.length) {
    return <p className="text-sm text-muted">Belum ada level.</p>;
  }
  const max = Math.max(...levels.map((l) => l.base_viewers || 0), 1);
  const sorted = [...levels].sort(
    (a, b) => (b.base_viewers || 0) - (a.base_viewers || 0)
  );
  return (
    <ul className="space-y-3">
      {sorted.map((l) => (
        <Row key={l.id} level={l} max={max} />
      ))}
    </ul>
  );
}
