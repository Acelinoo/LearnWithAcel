"use client";

import { Eye } from "lucide-react";
import { useLessonViewerCount } from "@/hooks/useViewerCount";
import { formatNumber } from "@/lib/utils";

/**
 * Badge "viewers" per materi.
 * - increment=true (dipasang di halaman materi saat dibuka): auto-bump
 * - increment=false (di daftar / card): hanya membaca, ikut update kalau counter lain bump
 * - showLabel=false untuk tampilan compact (ikon + angka saja)
 */
export default function LessonViewerBadge({
  lessonKey,
  seed,
  increment = false,
  showLabel = true,
  bordered = true,
  iconSize = 12,
  className = "",
}) {
  const { count, ready } = useLessonViewerCount(lessonKey, seed, { increment });

  const base = bordered
    ? "inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/[0.03] px-2.5 py-1 text-xs text-muted"
    : "inline-flex items-center gap-1.5 text-xs text-muted";

  return (
    <span className={base + " " + className}>
      <Eye size={iconSize} />
      <span className="font-mono tabular-nums text-foreground">
        {ready ? formatNumber(count) : formatNumber(seed)}
      </span>
      {showLabel && <span>viewers</span>}
    </span>
  );
}
