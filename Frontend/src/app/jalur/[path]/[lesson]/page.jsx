import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowRight, Sparkles } from "lucide-react";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import LessonHero from "@/components/lesson/LessonHero";
import LessonShell from "@/components/lesson/LessonShell";
import LessonSidebar from "@/components/lesson/LessonSidebar";
import LessonNextCard from "@/components/lesson/LessonNextCard";
import { Markdown, extractHeadings } from "@/lib/markdown";
import {
  JALUR_META,
  getJalurMeta,
  getJalurLesson,
  getAllJalurPaths,
} from "@/lib/jalur-data";

export const dynamic = "force-static";

export function generateStaticParams() {
  return getAllJalurPaths().map((p) => ({ path: p.path, lesson: p.slug }));
}

export function generateMetadata({ params }) {
  const lesson = getJalurLesson(params.path, params.lesson);
  if (!lesson) return { title: "Lesson tidak ditemukan" };
  return {
    title: `${lesson.title} · LearnWithAcel`,
    description: lesson.summary,
  };
}

export default function JalurLessonPage({ params }) {
  const meta = getJalurMeta(params.path);
  if (!meta) notFound();

  const lesson = getJalurLesson(meta.path, params.lesson);
  if (!lesson) notFound();

  const idx = meta.lessons.findIndex((l) => l.slug === params.lesson);
  const next = idx >= 0 ? meta.lessons[idx + 1] : null;

  const headings = extractHeadings(lesson.content);
  const lessonHrefBase = `/jalur/${meta.path}`;

  // Sidebar lesson rows — these aren't real DB lessons so we synthesize
  // stable IDs from the slug. completedLessonIds stays empty in Phase 1
  // (fundamentals don't track progress yet).
  const sidebarLessons = meta.lessons.map((l) => ({
    id: `jalur-${meta.path}-${l.slug}`,
    slug: l.slug,
    title: l.title,
    duration: l.duration,
    isCurrent: l.slug === params.lesson,
  }));

  return (
    <>
      <ReadingProgress />

      <LessonShell
        sidebar={
          <LessonSidebar
            levelTitle={meta.eyebrow}
            levelNumber={undefined}
            lessons={sidebarLessons}
            completedLessonIds={[]}
            lessonHrefBase={lessonHrefBase}
            headings={headings}
            nextLesson={
              next ? { slug: next.slug, title: next.title } : null
            }
            tone={meta.badgeTone}
          />
        }
      >
        <LessonHero
          title={lesson.title}
          summary={lesson.summary}
          readTime={lesson.duration}
          pathLabel={meta.eyebrow}
          pathTone={meta.badgeTone}
          roadmapHref={`/jalur/${meta.path}`}
          lessonIndex={idx >= 0 ? idx + 1 : undefined}
          lessonsTotal={meta.lessons.length}
        />

        <article className="mt-14 max-w-[68ch]">
          <Markdown source={lesson.content} />
        </article>

        <footer className="mt-16 max-w-[68ch] border-t border-border pt-10">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-sm text-muted">
              <Sparkles size={14} className="text-accent-hover" />
              Bagian dari{" "}
              <Link
                href={`/jalur/${meta.path}`}
                className="text-foreground transition-colors hover:text-accent-hover"
              >
                {meta.eyebrow}
              </Link>
            </div>

            {next ? (
              <Link
                href={`${lessonHrefBase}/${next.slug}`}
                className="inline-flex items-center gap-1.5 text-sm font-medium text-foreground/80 transition-colors hover:text-foreground"
              >
                Lanjut ke lesson berikutnya
                <ArrowRight size={14} />
              </Link>
            ) : (
              <Link
                href={`/jalur/${meta.path}#pilih-role`}
                className="inline-flex items-center gap-1.5 text-sm font-medium text-foreground/80 transition-colors hover:text-foreground"
              >
                Lanjut ke pilih{" "}
                {meta.path === "vibe" ? "role" : "spesialisasi"}
                <ArrowRight size={14} />
              </Link>
            )}
          </div>

          {next && (
            <div className="mt-10">
              <LessonNextCard
                href={`${lessonHrefBase}/${next.slug}`}
                title={next.title}
                duration={next.duration}
                tone={meta.badgeTone}
              />
            </div>
          )}
        </footer>
      </LessonShell>
    </>
  );
}
