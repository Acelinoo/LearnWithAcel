"use client";

/**
 * "Continue learning" card on the dashboard.
 *
 * The backend resolves the optimal next lesson at /progress/stats:
 *   1. The lesson the user last opened (if not yet completed).
 *   2. The next incomplete lesson within that same level.
 *   3. The first incomplete lesson of any level the user has progress in.
 *
 * The fallback grid below the headline shows the user's in-progress
 * levels for quick navigation.
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Compass,
  History,
  PlayCircle,
} from "lucide-react";
import type {
  ApiContinueLesson,
  ApiLevelStats,
} from "@/lib/api/progress";
import { onProgressUpdate } from "@/lib/progress-events";

type Props = {
  byLevel: ApiLevelStats[];
  continueLesson: ApiContinueLesson | null;
};

function lessonHref(item: ApiContinueLesson): string {
  if (item.category_slug === "vibe") {
    return `/materi/vibe/${item.level_slug}/${item.lesson_slug}`;
  }
  return `/materi/${item.level_slug}/${item.lesson_slug}`;
}

export default function ContinueLearning({ byLevel, continueLesson }: Props) {
  const [optimisticLevels, setOptimisticLevels] = useState(byLevel);
  const [target, setTarget] = useState(continueLesson);

  // Sync with server when stats refresh (router.refresh()).
  useEffect(() => {
    setOptimisticLevels(byLevel);
  }, [byLevel]);
  useEffect(() => {
    setTarget(continueLesson);
  }, [continueLesson]);

  // Apply optimistic per-level bump when a lesson is completed.
  useEffect(() => {
    return onProgressUpdate((u) => {
      if (!u.justCompleted || !u.levelId) return;
      setOptimisticLevels((prev) =>
        prev.map((b) =>
          b.level_id === u.levelId
            ? {
                ...b,
                completed_lessons: Math.min(
                  b.total_lessons,
                  b.completed_lessons + 1,
                ),
                percentage: Math.min(
                  100,
                  Math.round(
                    ((b.completed_lessons + 1) / b.total_lessons) * 100 * 10,
                  ) / 10,
                ),
              }
            : b,
        ),
      );
    });
  }, []);

  // Levels in progress (started but not finished) come first, then
  // fresh levels.
  const started = optimisticLevels.filter(
    (b) => b.completed_lessons > 0 && b.completed_lessons < b.total_lessons,
  );
  const fresh = optimisticLevels.filter((b) => b.completed_lessons === 0);
  const items = [...started, ...fresh].slice(0, 5);

  const showHeadline = target !== null;

  return (
    <section className="relative overflow-hidden rounded-2xl border border-border bg-black/30 p-6 backdrop-blur-xl sm:p-8">
      <div
        aria-hidden
        className="pointer-events-none absolute -right-24 -top-24 h-56 w-56 rounded-full bg-accent/15 blur-3xl"
      />

      <div className="relative flex items-start justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <History size={16} className="text-accent-hover" />
            <h2 className="font-display text-xl font-semibold tracking-tight">
              Lanjutkan belajar
            </h2>
          </div>
          <p className="mt-1 text-sm text-muted">
            {showHeadline
              ? "Sambung dari tempat kamu terakhir berhenti."
              : "Pilih jalur untuk mulai belajar."}
          </p>
        </div>
      </div>

      {/* Headline target — the resolved continue lesson */}
      {target && (
        <Link
          href={lessonHref(target)}
          className="group relative mt-6 flex items-center justify-between gap-4 rounded-xl border border-accent/25 bg-accent/[0.05] p-5 transition-all duration-300 hover:border-accent/45 hover:bg-accent/[0.08]"
        >
          <div className="min-w-0 flex-1">
            <div className="text-[11px] uppercase tracking-[0.14em] text-accent-hover/80">
              Lesson berikutnya · Level{" "}
              {String(target.level_number).padStart(2, "0")} —{" "}
              {target.level_title}
            </div>
            <div className="mt-1.5 truncate font-display text-base font-semibold text-foreground sm:text-lg">
              {target.lesson_title}
            </div>
          </div>
          <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border border-accent/30 bg-accent/10 text-accent-hover transition-all group-hover:translate-x-0.5 group-hover:bg-accent/20">
            <PlayCircle size={16} />
          </span>
        </Link>
      )}

      {items.length === 0 && !target ? (
        <EmptyState />
      ) : (
        <ol className="relative mt-5 space-y-2">
          {items.map((row) => (
            <li key={row.level_id}>
              <Link
                href={`/roadmap${row.category_slug && row.category_slug !== "frontend" ? `?path=${row.category_slug}` : ""}#${row.level_slug}`}
                className="group flex items-center gap-4 rounded-xl border border-border bg-black/30 p-4 transition-all hover:-translate-y-0.5 hover:border-accent/30"
              >
                <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-border bg-black/40 text-foreground transition-transform group-hover:scale-105">
                  <BookOpen size={15} />
                </span>

                <div className="min-w-0 flex-1">
                  <div className="text-[11px] uppercase tracking-[0.12em] text-muted">
                    {row.completed_lessons > 0 ? "In progress" : "Belum dimulai"}
                  </div>
                  <div className="mt-1 truncate text-sm font-medium text-foreground group-hover:text-accent-hover">
                    {row.level_title}
                  </div>
                  <div className="mt-1.5 h-1 w-full overflow-hidden rounded-full bg-black/40">
                    <div
                      className="h-full rounded-full bg-gradient-to-r from-accent to-accent-hover transition-all duration-500"
                      style={{ width: `${Math.min(100, row.percentage)}%` }}
                    />
                  </div>
                </div>

                <span className="hidden shrink-0 items-center gap-1.5 rounded-full border border-border bg-black/30 px-3 py-1.5 text-[12px] font-medium text-foreground/85 transition-colors group-hover:border-accent/40 group-hover:bg-accent/10 group-hover:text-accent-hover sm:inline-flex">
                  Lanjutkan
                  <ArrowRight
                    size={12}
                    className="transition-transform group-hover:translate-x-0.5"
                  />
                </span>
              </Link>
            </li>
          ))}
        </ol>
      )}
    </section>
  );
}

function EmptyState() {
  return (
    <div className="relative mt-6 flex flex-col items-center rounded-2xl border border-dashed border-border bg-black/30 px-6 py-10 text-center">
      <span className="flex h-14 w-14 items-center justify-center rounded-2xl border border-border bg-gradient-to-br from-accent/30 to-accent/5 text-accent-hover">
        <Compass size={20} />
      </span>
      <h3 className="mt-5 font-display text-base font-semibold">
        Belum ada lesson yang dimulai
      </h3>
      <p className="mt-1.5 max-w-sm text-[13.5px] leading-relaxed text-muted">
        Pilih jalur belajar dan mulai dari Level 01.
      </p>
      <Link href="/pilih-jalur" className="mt-5 btn-primary">
        Pilih jalur
        <ArrowRight size={14} />
      </Link>
    </div>
  );
}
