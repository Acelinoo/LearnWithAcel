import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Bot,
  Clock,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import LessonViewerBadge from "@/components/ui/LessonViewerBadge";
import CompleteLessonButton from "@/components/lesson/CompleteLessonButton";
import { Markdown } from "@/lib/markdown";
import { getLesson, getRoadmap } from "@/lib/api/content";
import { ApiError } from "@/lib/api/client";

export const dynamic = "force-dynamic";

async function loadLessonContext(level, lessonSlug) {
  try {
    const [lesson, roadmap] = await Promise.all([
      getLesson(level, lessonSlug),
      getRoadmap("vibe").catch(() => null),
    ]);
    const matchingLevel = roadmap?.levels.find((l) => l.slug === level);
    const lessonsInLevel = matchingLevel?.lessons ?? [];
    const idx = lessonsInLevel.findIndex((l) => l.slug === lessonSlug);
    const next = idx >= 0 ? lessonsInLevel[idx + 1] : null;
    return { lesson, level: matchingLevel, next };
  } catch (e) {
    if (e instanceof ApiError && e.status === 404) {
      return { lesson: null, level: null, next: null };
    }
    throw e;
  }
}

export async function generateMetadata({ params }) {
  try {
    const lesson = await getLesson(params.level, params.lesson);
    return {
      title: `${lesson.title} — Vibe Coding`,
      description: lesson.summary,
    };
  } catch {
    return { title: "Vibe Coding", description: "Materi Vibe Coding." };
  }
}

export default async function VibeLessonPage({ params }) {
  const { lesson, level, next } = await loadLessonContext(
    params.level,
    params.lesson
  );

  if (!lesson) notFound();

  return (
    <>
      <ReadingProgress />

      <article className="container-page max-w-3xl py-16">
        <Reveal>
          <Link
            href="/roadmap/vibe"
            className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
          >
            <ArrowLeft size={14} />
            Kembali ke roadmap
          </Link>
        </Reveal>

        <Reveal delay={0.05}>
          <div className="mt-8 flex flex-wrap items-center gap-2">
            <span className="rounded-full border border-sky-400/30 bg-sky-400/10 px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-[0.12em] text-sky-300">
              <Bot size={10} className="mr-1 inline" />
              Vibe Coding
            </span>
            {level && (
              <span className="section-eyebrow">
                Level 0{level.number} — {level.title}
              </span>
            )}
            <span className="chip">
              <Clock size={12} />
              {lesson.duration}
            </span>
            <LessonViewerBadge count={lesson.base_viewers} />
          </div>
        </Reveal>

        <Reveal delay={0.1}>
          <h1 className="mt-5 font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            {lesson.title}
          </h1>
        </Reveal>

        <Reveal delay={0.15}>
          <p className="mt-5 text-lg leading-relaxed text-muted">
            {lesson.summary}
          </p>
        </Reveal>

        <div className="mt-12">
          <Markdown source={lesson.content} />
        </div>

        <Reveal>
          <div className="mt-12 flex flex-wrap items-center justify-between gap-4 border-t border-white/5 pt-8">
            <div className="flex items-center gap-2 text-sm text-muted">
              <BookOpen size={14} />
              Bagian dari{" "}
              {level && (
                <Link
                  href={`/roadmap/vibe#${level.slug}`}
                  className="text-foreground hover:text-sky-300"
                >
                  {level.title}
                </Link>
              )}
            </div>
            <CompleteLessonButton lessonId={lesson.id} />
          </div>
        </Reveal>

        {next && (
          <Reveal>
            <Link
              href={`/materi/vibe/${params.level}/${next.slug}`}
              className="group mt-10 flex items-center justify-between gap-4 rounded-2xl border border-sky-400/10 bg-gradient-to-r from-card to-sky-500/10 p-6 transition-all hover:border-sky-400/40"
            >
              <div>
                <div className="text-xs text-muted">Materi berikutnya</div>
                <div className="mt-1 font-display text-lg font-semibold">
                  {next.title}
                </div>
              </div>
              <span className="flex h-10 w-10 items-center justify-center rounded-full border border-sky-400/20 bg-sky-400/[0.06] text-muted transition-all group-hover:border-sky-400/40 group-hover:text-sky-300">
                <ArrowRight size={16} />
              </span>
            </Link>
          </Reveal>
        )}
      </article>
    </>
  );
}
