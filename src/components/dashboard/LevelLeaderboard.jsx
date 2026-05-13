"use client";

import Link from "next/link";
import { useLevelViewerCount } from "@/hooks/useViewerCount";
import { formatNumber } from "@/lib/utils";

function Row({ level, max }) {
  const { count, ready } = useLevelViewerCount(level.slug, level.viewers);
  const value = ready ? count : level.viewers;
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
  const max = Math.max(...levels.map((l) => l.viewers));
  const sorted = [...levels].sort((a, b) => b.viewers - a.viewers);
  return (
    <ul className="space-y-3">
      {sorted.map((l) => (
        <Row key={l.id} level={l} max={max} />
      ))}
    </ul>
  );
}
