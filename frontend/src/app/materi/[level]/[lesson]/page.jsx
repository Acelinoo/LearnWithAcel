import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight, BookOpen, Clock, CheckCircle2, Sparkles, Trophy } from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import LessonShell from "@/components/lesson/LessonShell";
import LessonSidebar from "@/components/lesson/LessonSidebar";
import CompleteLessonButton from "@/components/lesson/CompleteLessonButton";
import LessonShortcuts from "@/components/lesson/LessonShortcuts";
import PracticalLabRenderer from "@/components/lesson/PracticalLabRenderer";
import { Markdown, extractHeadings } from "@/lib/markdown";
import { getLesson, getRoadmap } from "@/lib/api/content";
import { getServerStats } from "@/lib/api/server";
import { ApiError } from "@/lib/api/client";

export const dynamic = "force-dynamic";

async function loadLessonContext(levelSlug, lessonSlug) {
  try {
    const roleSlug = levelSlug.includes("-level-")
      ? levelSlug.split("-level-")[0]
      : levelSlug;

    const [lesson, roadmap, stats] = await Promise.all([
      getLesson(levelSlug, lessonSlug),
      getRoadmap(roleSlug).catch(() => null),
      getServerStats().catch(() => null),
    ]);

    const matchingLevel = roadmap?.levels.find((l) => l.slug === levelSlug);
    const category = roadmap?.category;
    const lessonsInLevel = matchingLevel?.lessons ?? [];
    const idx = lessonsInLevel.findIndex((l) => l.slug === lessonSlug);
    const next = idx >= 0 && idx + 1 < lessonsInLevel.length ? lessonsInLevel[idx + 1] : null;
    const prev = idx > 0 ? lessonsInLevel[idx - 1] : null;

    const completedLessonIds = stats?.completed_lesson_ids ?? [];
    const isCompleted = completedLessonIds.includes(lesson.id);

    return {
      lesson,
      level: matchingLevel,
      category,
      next,
      prev,
      lessonsInLevel,
      completedLessonIds,
      isCompleted,
      lessonIndex: idx >= 0 ? idx + 1 : 1,
    };
  } catch (e) {
    if (e instanceof ApiError && e.status === 404) {
      return { lesson: null, level: null, category: null, next: null, prev: null, lessonsInLevel: [], completedLessonIds: [], isCompleted: false, lessonIndex: 1 };
    }
    throw e;
  }
}

export async function generateMetadata({ params }) {
  try {
    const lesson = await getLesson(params.level, params.lesson);
    return {
      title: `${lesson.title} · LearnWithAcel`,
      description: lesson.summary,
    };
  } catch {
    return {
      title: "Materi Pembelajaran · LearnWithAcel",
      description: "Materi pembelajaran LearnWithAcel.",
    };
  }
}

export default async function LessonPage({ params }) {
  const {
    lesson,
    level,
    category,
    next,
    prev,
    lessonsInLevel,
    completedLessonIds,
    isCompleted,
    lessonIndex,
  } = await loadLessonContext(params.level, params.lesson);

  if (!lesson) notFound();

  const headings = extractHeadings(lesson.content);
  const hasQuiz = lesson.content.includes("## Quiz");
  const lessonHrefBase = `/materi/${params.level}`;

  const sidebarLessons = lessonsInLevel.map((l) => ({
    id: l.id,
    slug: l.slug,
    title: l.title,
    duration: l.duration,
    isCurrent: l.slug === params.lesson,
    isProject: l.is_project,
  }));

  const roleName = category?.name || category?.role || "LearnWithAcel";
  const xpReward = lesson.order_index === 4 ? 100 : 50;

  return (
    <>
      <ReadingProgress lessonId={lesson.id} />
      <LessonShortcuts 
        nextHref={next ? `/materi/${params.level}/${next.slug}` : undefined}
        prevHref={prev ? `/materi/${params.level}/${prev.slug}` : undefined}
        backHref="/roadmap"
      />

      <LessonShell
        sidebar={
          <LessonSidebar
            levelTitle={level ? level.title : "Level Progress"}
            levelNumber={level?.number}
            lessons={sidebarLessons}
            completedLessonIds={completedLessonIds}
            lessonHrefBase={lessonHrefBase}
            headings={headings}
            nextLesson={next ? { slug: next.slug, title: next.title } : null}
            tone="accent"
          />
        }
      >
        <Reveal>
          <Link
            href="/roadmap"
            className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
          >
            <ArrowLeft size={14} />
            Kembali ke roadmap
          </Link>
        </Reveal>

        {/* Meta Badge Header & Content */}
        {lesson.is_project ? (
          <div className="mt-8">
            <PracticalLabRenderer lesson={lesson} />
          </div>
        ) : (
          <>
            <Reveal delay={0.05}>
              <div className="mt-6 flex flex-wrap items-center gap-2">
                <span className="section-eyebrow uppercase tracking-wider">
                  {roleName} • {level ? `LEVEL 0${level.number}` : "LEVEL"}
                </span>
                <span className="chip">
                  <Clock size={12} />
                  {lesson.duration}
                </span>
                <span className="chip border-accent/30 bg-accent/10 text-accent-hover">
                  <Trophy size={12} />
                  +{xpReward} XP
                </span>
                {isCompleted && (
                  <span className="inline-flex items-center gap-1 rounded-full border border-emerald-400/30 bg-emerald-400/10 px-2.5 py-0.5 text-xs font-medium text-emerald-300">
                    <CheckCircle2 size={12} />
                    Selesai
                  </span>
                )}
              </div>
            </Reveal>

            <Reveal delay={0.1}>
              <h1 className="mt-4 font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl lg:text-5xl">
                {lesson.title}
              </h1>
            </Reveal>

            <Reveal delay={0.15}>
              <p className="mt-4 text-base leading-relaxed text-muted sm:text-lg">
                {lesson.summary}
              </p>
            </Reveal>

            {/* Content Body */}
            <div className="mt-10">
              <Markdown source={lesson.content} />
            </div>

            {/* Bottom Bar & Action */}
            <Reveal>
              <div className="mt-12 flex flex-wrap items-center justify-between gap-4 border-t border-border pt-8">
                <div className="flex items-center gap-2 text-sm text-muted">
                  <BookOpen size={14} className="text-accent-hover" />
                  <span>
                    Materi {lessonIndex} dari {lessonsInLevel.length || 4} di {level?.title || "Level ini"}
                  </span>
                </div>
                <CompleteLessonButton
                  lessonId={lesson.id}
                  levelId={level?.id}
                  initiallyCompleted={isCompleted}
                  nextHref={next ? `/materi/${params.level}/${next.slug}` : undefined}
                  hasQuiz={hasQuiz}
                />
              </div>
            </Reveal>
          </>
        )}

        {/* Next Lesson Card */}
        {next && (
          <Reveal delay={0.1}>
            <Link
              href={`/materi/${params.level}/${next.slug}`}
              className="group mt-8 flex items-center justify-between gap-4 rounded-2xl border border-white/10 bg-gradient-to-r from-card to-accent/10 p-6 transition-all hover:border-accent/40"
            >
              <div>
                <div className="text-xs text-muted">Materi berikutnya</div>
                <div className="mt-1 font-display text-lg font-semibold text-foreground">
                  {next.title}
                </div>
              </div>
              <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border border-white/10 bg-white/[0.04] text-muted transition-all group-hover:border-accent/40 group-hover:text-accent-hover">
                <ArrowRight size={16} />
              </span>
            </Link>
          </Reveal>
        )}
      </LessonShell>
    </>
  );
}
