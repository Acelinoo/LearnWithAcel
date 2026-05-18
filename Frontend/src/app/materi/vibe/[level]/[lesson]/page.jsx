import Link from "next/link";
import { notFound } from "next/navigation";
import { Sparkles } from "lucide-react";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import LessonHero from "@/components/lesson/LessonHero";
import LessonShell from "@/components/lesson/LessonShell";
import LessonSidebar from "@/components/lesson/LessonSidebar";
import LessonNextCard from "@/components/lesson/LessonNextCard";
import CompleteLessonButton from "@/components/lesson/CompleteLessonButton";
import { Markdown, extractHeadings } from "@/lib/markdown";
import { getLesson, getRoadmap } from "@/lib/api/content";
import { getServerStats } from "@/lib/api/server";
import { ApiError } from "@/lib/api/client";

export const dynamic = "force-dynamic";

async function loadLessonContext(level, lessonSlug) {
  try {
    const [lesson, roadmap] = await Promise.all([
      getLesson(level, lessonSlug),
      getRoadmap("vibe").catch(() => null),
    ]);
    const matchingLevel = roadmap?.levels.find((l) => l.slug === level);
    return { lesson, level: matchingLevel };
  } catch (e) {
    if (e instanceof ApiError && e.status === 404) {
      return { lesson: null, level: null };
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
  const { lesson, level } = await loadLessonContext(
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
  const lessonHrefBase = `/materi/vibe/${params.level}`;

  return (
    <>
      <ReadingProgress />

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
              tone="sky"
            />
          )
        }
      >
        <LessonHero
          title={lesson.title}
          summary={lesson.summary}
          readTime={lesson.duration}
          pathLabel="Vibe Coding"
          pathTone="sky"
          levelTitle={level?.title}
          levelNumber={level?.number}
          roadmapHref="/roadmap/vibe"
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
              <Sparkles size={14} className="text-sky-300" />
              {level ? (
                <>
                  Bagian dari{" "}
                  <Link
                    href={`/roadmap/vibe#${level.slug}`}
                    className="text-foreground transition-colors hover:text-sky-300"
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
                tone="sky"
              />
            </div>
          )}
        </footer>
      </LessonShell>
    </>
  );
}
