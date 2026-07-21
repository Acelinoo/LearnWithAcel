"use client";

/**
 * Sidebar shown alongside lesson content on lg+ screens.
 *
 * Layout:
 *   - Level progress bar (live: listens to progress events)
 *   - Lesson list within the current level (with completed dot)
 *   - Daftar isi (TOC) with scroll-spy
 *   - Next lesson CTA
 *
 * The sidebar receives initial completion data from the server (via
 * `completedLessonIds`) and then listens to the global progress event
 * bus so it can flip a row to "done" the moment the user marks it
 * complete — no full reload needed.
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  CheckCircle2,
} from "lucide-react";
import LessonTOC from "./LessonTOC";
import type { HeadingItem } from "@/lib/markdown";
import { onProgressUpdate } from "@/lib/progress-events";
import { cn } from "@/lib/utils";

export type LessonSidebarLesson = {
  id: string;
  slug: string;
  title: string;
  duration?: string;
  /** True when this is the lesson the user is currently reading. */
  isCurrent?: boolean;
};

type Props = {
  /** Heading text shown above the lesson list (e.g. level title). */
  levelTitle: string;
  /** Used to label "Lesson 02 / 04" style strings. */
  levelNumber?: number;
  /** Lessons within the level, in order. */
  lessons: LessonSidebarLesson[];
  /** Lesson IDs the current user has already completed (server-side
   *  initial state). The sidebar applies optimistic updates on top. */
  completedLessonIds: string[];
  /** Path-relative prefix used to build lesson links. */
  lessonHrefBase: string;
  /** TOC headings extracted from the current lesson markdown. */
  headings: HeadingItem[];
  /** Optional next-lesson link rendered at the bottom. */
  nextLesson?: { slug: string; title: string } | null;
  /** Visual tone, mirrors the hero. */
  tone?: "accent" | "sky";
};

const TONE_BAR_FROM = {
  accent: "from-accent",
  sky: "from-sky-400",
} as const;

const TONE_BAR_TO = {
  accent: "to-accent-hover",
  sky: "to-sky-300",
} as const;

const TONE_TEXT = {
  accent: "text-accent-hover",
  sky: "text-sky-300",
} as const;

export default function LessonSidebar({
  levelTitle,
  levelNumber,
  lessons,
  completedLessonIds,
  lessonHrefBase,
  headings,
  nextLesson,
  tone = "accent",
}: Props) {
  const [completed, setCompleted] = useState<Set<string>>(
    () => new Set(completedLessonIds),
  );

  // Re-sync when the server sends fresh completion data (e.g. when
  // returning to a previously-completed lesson).
  useEffect(() => {
    setCompleted(new Set(completedLessonIds));
  }, [completedLessonIds]);

  // Optimistic updates from CompleteLessonButton.
  useEffect(() => {
    return onProgressUpdate((u) => {
      if (!u.justCompleted) return;
      setCompleted((prev) => {
        if (prev.has(u.lessonId)) return prev;
        const next = new Set(prev);
        next.add(u.lessonId);
        return next;
      });
    });
  }, []);

  const totalLessons = lessons.length;
  const completedLessons = lessons.filter((l) => completed.has(l.id)).length;
  const percentage =
    totalLessons > 0
      ? Math.round((completedLessons / totalLessons) * 100)
      : 0;

  return (
    <aside>
      <div className="sticky top-24 space-y-4">
        {/* Level progress */}
        <section className="rounded-xl border border-border bg-black/30 p-4 backdrop-blur-md">
          <div className="flex items-center justify-between gap-2">
            <div>
              <div className="text-[10px] font-semibold uppercase tracking-[0.18em] text-muted/70">
                Level
                {typeof levelNumber === "number" &&
                  ` ${String(levelNumber).padStart(2, "0")}`}
              </div>
              <div className="mt-1 line-clamp-1 font-display text-sm font-semibold text-foreground">
                {levelTitle}
              </div>
            </div>
            <span className={cn("font-mono text-sm tabular-nums", TONE_TEXT[tone])}>
              {percentage}%
            </span>
          </div>

          <div className="mt-4 h-1.5 overflow-hidden rounded-full bg-black/50">
            <div
              className={cn(
                "h-full rounded-full bg-gradient-to-r transition-all duration-700 ease-out",
                TONE_BAR_FROM[tone],
                TONE_BAR_TO[tone],
              )}
              style={{ width: `${percentage}%` }}
            />
          </div>

          <div className="mt-3 flex items-center justify-between text-[11px] text-muted">
            <span>
              {completedLessons} dari {totalLessons} lesson
            </span>
            {percentage === 100 && (
              <span className="inline-flex items-center gap-1 text-emerald-300">
                <CheckCircle2 size={11} />
                Tuntas
              </span>
            )}
          </div>
        </section>

        {/* Lesson list */}
        {lessons.length > 0 && (
          <section className="rounded-xl border border-border bg-black/30 p-3 backdrop-blur-md">
            <div className="flex items-center gap-2 px-2 text-[11px] font-semibold uppercase tracking-[0.18em] text-muted/70">
              <BookOpen size={12} />
              Lesson di level ini
            </div>
            <ul className="mt-3 space-y-0.5">
              {lessons.map((l, i) => {
                const isDone = completed.has(l.id);
                return (
                  <li key={l.id}>
                    <Link
                      href={`${lessonHrefBase}/${l.slug}`}
                      className={cn(
                        "group flex items-start gap-3 rounded-lg px-3 py-2 transition-colors duration-200",
                        l.isCurrent
                          ? "bg-black/40 text-foreground"
                          : "text-muted hover:bg-black/30 hover:text-foreground",
                      )}
                    >
                      <span
                        aria-hidden
                        className={cn(
                          "mt-1 inline-flex h-4 w-4 shrink-0 items-center justify-center rounded-full border text-[9px] font-semibold transition-colors",
                          isDone
                            ? "border-emerald-400/30 bg-emerald-400/[0.1] text-emerald-300"
                            : l.isCurrent
                              ? cn("border-current", TONE_TEXT[tone])
                              : "border-border bg-black/40 text-muted",
                        )}
                      >
                        {isDone ? (
                          <CheckCircle2 size={10} />
                        ) : (
                          String(i + 1).padStart(2, "0")
                        )}
                      </span>
                      <span className="flex-1 text-[13px] leading-snug">
                        {l.title}
                        {l.duration && (
                          <span className="block text-[11px] text-muted/70">
                            {l.duration}
                          </span>
                        )}
                      </span>
                    </Link>
                  </li>
                );
              })}
            </ul>
          </section>
        )}

        {/* TOC */}
        {headings.length > 0 && (
          <section className="rounded-xl border border-border bg-black/30 p-3 backdrop-blur-md">
            <LessonTOC headings={headings} />
          </section>
        )}

        {/* Next lesson */}
        {nextLesson && (
          <Link
            href={`${lessonHrefBase}/${nextLesson.slug}`}
            className={cn(
              "group flex items-center justify-between rounded-xl border border-border bg-black/30 p-4 transition-all duration-300",
              tone === "sky"
                ? "hover:border-sky-400/40"
                : "hover:border-accent/40",
            )}
          >
            <div>
              <div className="text-[10px] font-semibold uppercase tracking-[0.18em] text-muted/70">
                Berikutnya
              </div>
              <div className="mt-1 line-clamp-2 text-sm font-medium text-foreground">
                {nextLesson.title}
              </div>
            </div>
            <span className="ml-3 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-border bg-black/40 text-muted transition-all duration-300 group-hover:translate-x-0.5 group-hover:text-foreground">
              <ArrowRight size={14} />
            </span>
          </Link>
        )}
      </div>
    </aside>
  );
}
