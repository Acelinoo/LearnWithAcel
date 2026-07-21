/**
 * Hero block at the top of a lesson page.
 *
 * Props are intentionally specific (not generic content) so the page
 * stays a thin orchestrator and this component handles all the layout
 * decisions in one place.
 */

import Link from "next/link";
import { ArrowLeft, Award, Clock, Layers, Sparkles } from "lucide-react";
import Reveal from "@/components/ui/Reveal";

export type LessonHeroProps = {
  /** Title of the lesson, rendered as the page H1. */
  title: string;
  /** Short blurb shown under the title. */
  summary: string;
  /** Estimated read time, e.g. "12 menit". */
  readTime: string;
  /** Track this lesson belongs to (Frontend / Backend / Vibe Coding…). */
  pathLabel: string;
  /** Tone for the path chip — keeps the visual language consistent
   *  between the manual and Vibe entry points. */
  pathTone?: "accent" | "sky";
  /** Optional level title shown alongside `Level NN`. */
  levelTitle?: string;
  /** Numeric level (e.g. 1, 2). When 0 we still display "Level 00"
   *  for the Vibe orientation level. */
  levelNumber?: number;
  /** Path-relative href to return to the roadmap (e.g. "/roadmap" or
   *  "/roadmap/vibe"). */
  roadmapHref: string;
  /** Used in the sub-header strip to indicate progress within a level
   *  (1-based). When `lessonsTotal` is 0 we hide this badge. */
  lessonIndex?: number;
  lessonsTotal?: number;
  /** Optional XP reward shown as a trophy chip. */
  xpReward?: number;
  /** Whether the user has already completed this lesson — flips the
   *  status chip from "Belum selesai" to "Sudah selesai". */
  completed?: boolean;
};

const PATH_TONE_CLASSES = {
  accent:
    "border-accent/20 bg-accent/[0.06] text-accent-hover [&_svg]:text-accent-hover",
  sky:
    "border-sky-400/20 bg-sky-500/[0.06] text-sky-300 [&_svg]:text-sky-300",
} as const;

export default function LessonHero({
  title,
  summary,
  readTime,
  pathLabel,
  pathTone = "accent",
  levelTitle,
  levelNumber,
  roadmapHref,
  lessonIndex,
  lessonsTotal,
  xpReward,
  completed,
}: LessonHeroProps) {
  const levelLabel =
    typeof levelNumber === "number"
      ? `Level ${String(levelNumber).padStart(2, "0")}`
      : null;

  return (
    <header className="relative">
      {/* Subtle radial glow behind the hero, scoped to this block. */}
      <div
        aria-hidden
        className="pointer-events-none absolute inset-x-0 -top-12 h-56 bg-radial-fade opacity-60"
      />

      <Reveal className="">
        <nav aria-label="Breadcrumb" className="flex items-center space-x-2 text-sm text-muted">
          <Link href={roadmapHref} className="transition-colors hover:text-foreground">
            Roadmap
          </Link>
          <span className="text-muted-foreground/40">/</span>
          <Link href={roadmapHref} className="transition-colors hover:text-foreground">
            {pathLabel}
          </Link>
          {levelLabel && (
            <>
              <span className="text-muted-foreground/40">/</span>
              <span className="text-foreground">{levelLabel}</span>
            </>
          )}
        </nav>
      </Reveal>

      <Reveal delay={0.05} className="">
        <div className="mt-6 flex flex-wrap items-center gap-2">
          <span
            className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-[0.14em] ${PATH_TONE_CLASSES[pathTone]}`}
          >
            <Sparkles size={10} />
            {pathLabel}
            {levelLabel && ` • ${levelLabel}`}
            {levelTitle && ` — ${levelTitle}`}
          </span>
        </div>
      </Reveal>

      <Reveal delay={0.1} className="">
        <h1 className="relative mt-6 font-display text-4xl font-semibold tracking-tight text-balance text-foreground sm:text-5xl">
          {title}
        </h1>
      </Reveal>

      {summary && (
        <Reveal delay={0.15} className="">
          <p className="mt-5 max-w-2xl text-lg leading-relaxed text-muted">
            {summary}
          </p>
        </Reveal>
      )}

      <Reveal delay={0.2} className="">
        <div className="mt-7 flex flex-wrap items-center gap-2">
          <span className="chip">
            <Clock size={12} />
            {readTime}
          </span>

          {typeof lessonIndex === "number" &&
            typeof lessonsTotal === "number" &&
            lessonsTotal > 0 && (
              <span className="chip">
                <Layers size={12} />
                Lesson {lessonIndex} / {lessonsTotal}
              </span>
            )}

          {typeof xpReward === "number" && xpReward > 0 && (
            <span className="inline-flex items-center gap-1.5 rounded-full border border-amber-300/20 bg-amber-300/[0.05] px-3 py-1 text-xs font-medium text-amber-200">
              <Award size={12} />
              {xpReward} XP
            </span>
          )}

          <span
            className={
              "inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-medium " +
              (completed
                ? "border-emerald-400/25 bg-emerald-400/[0.06] text-emerald-300"
                : "border-border bg-black/30 text-muted")
            }
          >
            <span
              aria-hidden
              className={
                "h-1.5 w-1.5 rounded-full " +
                (completed ? "bg-emerald-400" : "bg-muted/60")
              }
            />
            {completed ? "Sudah selesai" : "Belum selesai"}
          </span>
        </div>
      </Reveal>
    </header>
  );
}
