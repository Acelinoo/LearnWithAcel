import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Clock,
  Hourglass,
  Target,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import Quiz from "@/components/lesson/Quiz";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import PracticeBlock from "@/components/lesson/PracticeBlock";
import DebugChallenge from "@/components/lesson/DebugChallenge";
import ErrorChallenge from "@/components/lesson/ErrorChallenge";
import LessonViewerBadge from "@/components/ui/LessonViewerBadge";
import { getLesson } from "@/lib/lessonContent";
import { getLevelBySlug } from "@/lib/roadmap";

export async function generateMetadata({ params }) {
  const lesson = getLesson(params.level, params.lesson);
  if (!lesson) {
    const level = getLevelBySlug(params.level);
    return {
      title: level ? `${level.title} — Coming soon` : "Materi",
      description: "Materi ini sedang disiapkan.",
    };
  }
  return {
    title: lesson.title,
    description: lesson.description,
  };
}

export default function LessonPage({ params }) {
  const level = getLevelBySlug(params.level);
  if (!level) notFound();

  const lesson = getLesson(params.level, params.lesson);
  const lessonMeta = level.lessons.find((l) => l.slug === params.lesson);
  const viewerKey = `${params.level}/${params.lesson}`;
  const viewerSeed = lessonMeta?.viewers ?? 500;

  // Elegant empty state when content is still being prepared
  if (!lesson) {
    return (
      <div className="container-page max-w-2xl py-24">
        <Reveal>
          <Link
            href="/roadmap"
            className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
          >
            <ArrowLeft size={14} />
            Kembali ke roadmap
          </Link>
        </Reveal>
        <Reveal delay={0.05}>
          <div className="mt-12 flex flex-col items-center text-center">
            <div className="flex h-16 w-16 items-center justify-center rounded-2xl border border-white/10 bg-white/[0.03] text-accent-hover">
              <Hourglass size={22} />
            </div>
            <span className="section-eyebrow mt-6">
              Materi sedang disiapkan
            </span>
            <h1 className="mt-4 font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl">
              {lessonMeta?.title || "Materi ini segera hadir"}
            </h1>
            <p className="mt-4 max-w-md text-[15px] leading-relaxed text-muted">
              Materi untuk {level.title} ini sedang diracik dengan seksama.
              Sambil menunggu, kamu bisa mulai dari materi lain yang sudah
              tersedia.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
              <Link href={`/roadmap#${level.slug}`} className="btn-primary">
                Lihat materi lain
                <ArrowRight size={16} />
              </Link>
              <Link href="/" className="btn-secondary">
                Kembali ke beranda
              </Link>
            </div>
          </div>
        </Reveal>
      </div>
    );
  }

  return (
    <>
      <ReadingProgress />

      <article className="container-page max-w-3xl py-16">
        <Reveal>
          <Link
            href="/roadmap"
            className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
          >
            <ArrowLeft size={14} />
            Kembali ke roadmap
          </Link>
        </Reveal>

        <Reveal delay={0.05}>
          <div className="mt-8 flex flex-wrap items-center gap-2">
            <span className="section-eyebrow">{lesson.level}</span>
            <span className="chip">
              <Clock size={12} />
              {lesson.readTime}
            </span>
            <LessonViewerBadge lessonKey={viewerKey} seed={viewerSeed} />
          </div>
        </Reveal>

        <Reveal delay={0.1}>
          <h1 className="mt-5 font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            {lesson.title}
          </h1>
        </Reveal>

        <Reveal delay={0.15}>
          <p className="mt-5 text-lg leading-relaxed text-muted">
            {lesson.description}
          </p>
        </Reveal>

        {lesson.hero && (
          <Reveal delay={0.2}>
            <div className="mt-10 flex items-center gap-4 rounded-2xl border border-white/5 bg-gradient-to-br from-accent/10 via-card to-card p-6">
              <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/[0.03] text-3xl">
                {lesson.hero.emoji}
              </div>
              <p className="text-[15px] italic text-foreground/80">
                {lesson.hero.caption}
              </p>
            </div>
          </Reveal>
        )}

        {/* Objectives */}
        <Reveal delay={0.2}>
          <section className="mt-10 card-base p-6">
            <div className="flex items-center gap-2">
              <Target size={16} className="text-accent-hover" />
              <h2 className="font-display text-sm font-semibold uppercase tracking-[0.12em] text-muted">
                Poin Pembelajaran
              </h2>
            </div>
            <ul className="mt-4 space-y-2.5">
              {lesson.objectives.map((o) => (
                <li
                  key={o}
                  className="flex gap-3 text-[15px] leading-relaxed text-foreground/90"
                >
                  <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-accent-hover" />
                  {o}
                </li>
              ))}
            </ul>
          </section>
        </Reveal>

        {/* Practice / VS Code CTA */}
        {lesson.practice && (
          <Reveal delay={0.25}>
            <div className="mt-6">
              <PracticeBlock practice={lesson.practice} />
            </div>
          </Reveal>
        )}

        {/* Sections */}
        <div className="prose-article mt-12">
          {lesson.sections.map((s, idx) => (
            <Reveal key={idx} delay={0.05}>
              <section>
                <h2>{s.heading}</h2>
                {s.body?.map((p, i) => (
                  <p key={i}>{p}</p>
                ))}
                {s.list && (
                  <ul>
                    {s.list.map((li, i) => (
                      <li key={i}>{li}</li>
                    ))}
                  </ul>
                )}
                {s.code && (
                  <pre>
                    <code>{s.code}</code>
                  </pre>
                )}
              </section>
            </Reveal>
          ))}
        </div>

        {/* Debug Challenge */}
        {lesson.debug && (
          <Reveal>
            <div className="mt-16">
              <DebugChallenge challenge={lesson.debug} />
            </div>
          </Reveal>
        )}

        {/* Quiz */}
        {lesson.quiz && (
          <Reveal>
            <div className="mt-16">
              <Quiz quiz={lesson.quiz} />
            </div>
          </Reveal>
        )}

        {/* Error Challenge */}
        {lesson.errorChallenge && (
          <Reveal>
            <div className="mt-16">
              <ErrorChallenge data={lesson.errorChallenge} />
            </div>
          </Reveal>
        )}

        {/* Next lesson */}
        {lesson.nextLesson && (
          <Reveal>
            <Link
              href={lesson.nextLesson.href}
              className="group mt-10 flex items-center justify-between gap-4 rounded-2xl border border-white/5 bg-gradient-to-r from-card to-accent/10 p-6 transition-all hover:border-accent/40"
            >
              <div>
                <div className="text-xs text-muted">Materi berikutnya</div>
                <div className="mt-1 font-display text-lg font-semibold">
                  {lesson.nextLesson.title}
                </div>
              </div>
              <span className="flex h-10 w-10 items-center justify-center rounded-full border border-white/10 bg-white/[0.04] text-muted transition-all group-hover:border-accent/40 group-hover:text-accent-hover">
                <ArrowRight size={16} />
              </span>
            </Link>
          </Reveal>
        )}

        {/* Back to level */}
        <Reveal>
          <div className="mt-8 flex items-center gap-2 text-sm text-muted">
            <BookOpen size={14} />
            Bagian dari{" "}
            <Link
              href={`/roadmap#${level.slug}`}
              className="text-foreground hover:text-accent-hover"
            >
              {level.title}
            </Link>
          </div>
        </Reveal>
      </article>
    </>
  );
}
