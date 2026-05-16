import Link from "next/link";
import { notFound } from "next/navigation";
import { Sparkles } from "lucide-react";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import LessonHero from "@/components/lesson/LessonHero";
import LessonShell from "@/components/lesson/LessonShell";
import LessonSidebar from "@/components/lesson/LessonSidebar";
import LessonNextCard from "@/components/lesson/LessonNextCard";
import LessonViewTracker from "@/components/lesson/LessonViewTracker";
import CompleteLessonButton from "@/components/lesson/CompleteLessonButton";
import { Markdown, extractHeadings } from "@/lib/markdown";
import { getLesson, getRoadmap } from "@/lib/api/content";
import { getServerStats } from "@/lib/api/server";
import { ApiError } from "@/lib/api/client";

export const dynamic = "force-dynamic";

/**
 * Try /roadmap/<slug> for the supported manual paths until one yields a
 * level matching `levelSlug`. We don't know up-front whether a lesson
 * belongs to frontend, backend, or fullstack, and the lesson endpoint
 * itself only returns level_id (not category slug).
 */
async function resolveContext(levelSlug, lessonSlug) {
  let lesson;
  try {
    lesson = await getLesson(levelSlug, lessonSlug);
  } catch (e) {
    if (e instanceof ApiError && e.status === 404) {
      return { lesson: null };
    }
    throw e;
  }

  const candidates = ["frontend", "backend", "fullstack"];
  for (const slug of candidates) {
    try {
      const roadmap = await getRoadmap(slug);
      const level = roadmap?.levels?.find((l) => l.slug === levelSlug);
      if (level) {
        return { lesson, roadmap, level, categorySlug: slug };
      }
    } catch {
      /* swallow — try the next category */
    }
  }
  return { lesson, level: null };
}

export async function generateMetadata({ params }) {
  try {
    const lesson = await getLesson(params.level, params.lesson);
    return {
      title: lesson.title,
      description: lesson.summary,
    };
  } catch {
    return {
      title: "Materi",
      description: "Materi pembelajaran LearnWithAcel.",
    };
  }
}

export default async function LessonPage({ params }) {
  const { lesson, level, categorySlug } = await resolveContext(
    params.level,
    params.lesson,
  );

  if (!lesson) notFound();

  const stats = await getServerStats().catch(() => null);
  const completedIds = stats?.completed_lesson_ids ?? [];
  const initiallyCompleted = completedIds.includes(lesson.id);

  const lessonsInLevel = level?.lessons ?? [];
  const idx = lessonsInLevel.findIndex((l) => l.slug === params.lesson);
  const next = idx >= 0 ? lessonsInLevel[idx + 1] : null;

  const headings = extractHeadings(lesson.content);

  const lessonHrefBase = `/materi/${params.level}`;
  const roadmapHref = categorySlug
    ? `/roadmap${categorySlug === "frontend" ? "" : `?path=${categorySlug}`}`
    : "/roadmap";

  const PATH_LABELS = {
    frontend: "Frontend",
    backend: "Backend",
    fullstack: "Fullstack",
  };
  const pathLabel = categorySlug ? PATH_LABELS[categorySlug] : "Manual Coding";

  return (
    <>
      <ReadingProgress />
      <LessonViewTracker lessonId={lesson.id} />

      <LessonShell
        sidebar={
          level && (
            <LessonSidebar
              levelTitle={level.title}
              levelNumber={level.number}
              lessons={lessonsInLevel.map((l) => ({
                id: l.id,
                slug: l.slug,
                title: l.title,
                duration: l.duration,
                isCurrent: l.slug === params.lesson,
              }))}
              completedLessonIds={completedIds}
              lessonHrefBase={lessonHrefBase}
              headings={headings}
              nextLesson={next ? { slug: next.slug, title: next.title } : null}
              tone="accent"
            />
          )
        }
      >
        <LessonHero
          title={lesson.title}
          summary={lesson.summary}
          readTime={lesson.duration}
          pathLabel={pathLabel}
          pathTone="accent"
          levelTitle={level?.title}
          levelNumber={level?.number}
          roadmapHref={roadmapHref}
          lessonIndex={idx >= 0 ? idx + 1 : undefined}
          lessonsTotal={lessonsInLevel.length}
          xpReward={lesson.xp_reward}
          completed={initiallyCompleted}
        />

        <article className="mt-14 max-w-[68ch]">
          <Markdown source={lesson.content} />
        </article>

        <footer className="mt-16 max-w-[68ch] border-t border-border pt-10">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-sm text-muted">
              <Sparkles size={14} className="text-accent-hover" />
              {level ? (
                <>
                  Bagian dari{" "}
                  <Link
                    href={`/roadmap#${level.slug}`}
                    className="text-foreground transition-colors hover:text-accent-hover"
                  >
                    {level.title}
                  </Link>
                </>
              ) : (
                <span>Selamat belajar</span>
              )}
            </div>
            <CompleteLessonButton
              lessonId={lesson.id}
              levelId={level?.id}
              initiallyCompleted={initiallyCompleted}
            />
          </div>

          {next && (
            <div className="mt-10">
              <LessonNextCard
                href={`${lessonHrefBase}/${next.slug}`}
                title={next.title}
                duration={next.duration}
                tone="accent"
              />
            </div>
          )}
        </footer>
      </LessonShell>
    </>
  );
}
