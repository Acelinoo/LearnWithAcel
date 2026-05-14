"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import {
  ArrowRight,
  BookOpen,
  Compass,
  History,
  PlayCircle,
} from "lucide-react";
import type { ApiLevelStats } from "@/lib/api/progress";

// framer-motion 11.x typing workaround
const MDiv = motion.div as unknown as React.FC<
  React.HTMLAttributes<HTMLDivElement> & Record<string, unknown>
>;
const MLi = motion.li as unknown as React.FC<
  React.LiHTMLAttributes<HTMLLIElement> & Record<string, unknown>
>;

type Props = {
  /** Per-level progress stats from /api/v1/progress/stats. */
  byLevel: ApiLevelStats[];
};

/**
 * "Continue learning" derives its content from server-side progress stats:
 * the levels you've started (1 ≤ completed < total) come first, followed by
 * fresh levels you haven't started yet. Clicking a row sends you to the
 * roadmap anchor for that level.
 */
export default function ContinueLearning({ byLevel }: Props) {
  // In-progress first, then fresh levels.
  const started = byLevel.filter(
    (b) => b.completed_lessons > 0 && b.completed_lessons < b.total_lessons
  );
  const fresh = byLevel.filter((b) => b.completed_lessons === 0);
  const items = [...started, ...fresh].slice(0, 6);

  return (
    <section className="relative overflow-hidden rounded-2xl border border-white/10 bg-white/[0.02] p-6 backdrop-blur-xl sm:p-8">
      <div
        aria-hidden
        className="pointer-events-none absolute -right-24 -top-24 h-56 w-56 rounded-full bg-accent/15 blur-3xl"
      />

      <div className="relative flex items-start justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <History size={16} className="text-accent-hover" />
            <h2 className="font-display text-xl font-semibold tracking-tight">
              Continue learning
            </h2>
          </div>
          <p className="mt-1 text-sm text-muted">
            Berdasarkan progress kamu, ini level berikutnya untuk dilanjutin.
          </p>
        </div>
      </div>

      {items.length === 0 ? (
        <EmptyState />
      ) : (
        <ol className="relative mt-6 space-y-2">
          {items.map((row, i) => (
            <MLi
              key={row.level_id}
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{
                duration: 0.45,
                delay: 0.04 + i * 0.05,
                ease: [0.22, 1, 0.36, 1],
              }}
            >
              <Link
                href={`/roadmap#${row.level_slug}`}
                className="group flex items-center gap-4 rounded-xl border border-white/5 bg-white/[0.02] p-4 transition-all hover:-translate-y-0.5 hover:border-accent/30 hover:bg-white/[0.04]"
              >
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/[0.04] text-foreground transition-transform group-hover:scale-105">
                  <BookOpen size={15} />
                </span>

                <div className="min-w-0 flex-1">
                  <div className="text-[11px] uppercase tracking-[0.12em] text-muted">
                    {row.completed_lessons > 0 ? "In progress" : "Belum dimulai"}
                  </div>
                  <div className="mt-1 truncate text-sm font-medium text-foreground group-hover:text-accent-hover">
                    {row.level_title}
                  </div>
                  <div className="mt-1.5 h-1 w-full overflow-hidden rounded-full bg-white/[0.05]">
                    <div
                      className="h-full rounded-full bg-gradient-to-r from-accent to-accent-hover"
                      style={{ width: `${Math.min(100, row.percentage)}%` }}
                    />
                  </div>
                </div>

                <span className="hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/[0.03] px-3 py-1.5 text-[12px] font-medium text-foreground/85 transition-colors group-hover:border-accent/40 group-hover:bg-accent/10 group-hover:text-accent-hover sm:inline-flex">
                  <PlayCircle size={12} />
                  Lanjutkan
                  <ArrowRight
                    size={12}
                    className="transition-transform group-hover:translate-x-0.5"
                  />
                </span>
              </Link>
            </MLi>
          ))}
        </ol>
      )}
    </section>
  );
}

function EmptyState() {
  return (
    <MDiv
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
      className="relative mt-6 flex flex-col items-center rounded-2xl border border-dashed border-white/10 bg-white/[0.015] px-6 py-10 text-center"
    >
      <span className="flex h-14 w-14 items-center justify-center rounded-2xl border border-white/10 bg-gradient-to-br from-accent/30 to-accent/5 text-accent-hover">
        <Compass size={20} />
      </span>
      <h3 className="mt-5 font-display text-base font-semibold">
        Semua level sudah selesai!
      </h3>
      <p className="mt-1.5 max-w-sm text-[13.5px] leading-relaxed text-muted">
        Mantap. Kamu siap explore project nyata atau loncat ke jalur lain.
      </p>
      <Link href="/roadmap" className="mt-5 btn-primary">
        Jelajahi roadmap
        <ArrowRight size={14} />
      </Link>
    </MDiv>
  );
}
