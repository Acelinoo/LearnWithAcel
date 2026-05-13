import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Bot,
  Clock,
  GraduationCap,
  Rocket,
  Trophy,
  Users,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import LevelViewerBadge from "@/components/ui/LevelViewerBadge";
import { vibeLevels, vibeTotalLessons, vibeTotalViewers } from "@/lib/vibeRoadmap";
import { formatCompact } from "@/lib/utils";

export const metadata = {
  title: "Roadmap Vibe Coding — AI-Assisted Learning Path",
  description:
    "9 level dari mindset hingga professional builder. Bangun app nyata dengan bantuan AI.",
};

export default function VibeRoadmapPage() {
  return (
    <div className="container-page py-16">
      <Reveal>
        <div className="flex items-center gap-2">
          <span className="section-eyebrow">
            <Bot size={12} />
            Vibe Coding Roadmap
          </span>
          <span className="rounded-full border border-violet-400/30 bg-violet-400/10 px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-[0.12em] text-violet-300">
            AI Assisted
          </span>
        </div>
      </Reveal>
      <Reveal delay={0.05}>
        <h1 className="mt-5 max-w-3xl font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
          Dari nol sampai bisa build app sendiri, dibantu AI.
        </h1>
      </Reveal>
      <Reveal delay={0.1}>
        <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
          9 level progresif. Setiap level diakhiri project nyata. Kamu tidak
          perlu hafal syntax — cukup pahami workflow dan biarkan AI membantu
          eksekusi.
        </p>
      </Reveal>

      {/* Stats */}
      <Reveal delay={0.15}>
        <div className="mt-10 grid grid-cols-2 gap-3 sm:grid-cols-4">
          {[
            { icon: Users, label: "Total viewers", value: formatCompact(vibeTotalViewers) },
            { icon: BookOpen, label: "Total materi", value: vibeTotalLessons },
            { icon: Trophy, label: "Mini project", value: vibeLevels.length },
            { icon: Clock, label: "Estimasi", value: "~4 bulan" },
          ].map((s) => (
            <div key={s.label} className="card-base flex items-center gap-3 p-4">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-accent-hover">
                <s.icon size={16} />
              </div>
              <div>
                <div className="text-xs text-muted">{s.label}</div>
                <div className="font-display text-lg font-semibold">{s.value}</div>
              </div>
            </div>
          ))}
        </div>
      </Reveal>

      {/* Persiapan banner */}
      <Reveal delay={0.18}>
        <Link
          href="/persiapan/vibe"
          className="group mt-8 flex items-center justify-between gap-4 rounded-2xl border border-violet-400/20 bg-gradient-to-r from-violet-400/10 via-card to-card p-5 transition-colors hover:border-violet-400/40"
        >
          <div className="flex items-center gap-3">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl border border-violet-400/30 bg-violet-400/10 text-violet-300">
              <Rocket size={15} />
            </span>
            <div>
              <div className="font-display text-sm font-semibold">Belum setup tools?</div>
              <div className="text-xs text-muted">Install Cursor, buat akun GitHub & Vercel dulu.</div>
            </div>
          </div>
          <span className="hidden items-center gap-1 text-sm text-violet-300 group-hover:text-foreground sm:inline-flex">
            Lihat persiapan <ArrowRight size={14} />
          </span>
        </Link>
      </Reveal>

      {/* Levels */}
      <div className="relative mt-16">
        <div className="absolute left-[26px] top-6 bottom-6 w-px bg-gradient-to-b from-violet-400/40 via-white/10 to-transparent md:left-[30px]" />

        <div className="space-y-5">
          {vibeLevels.map((level, i) => (
            <Reveal key={level.id} delay={i * 0.04}>
              <article id={level.slug} className="relative scroll-mt-24 pl-16 md:pl-20">
                <div className="absolute left-0 top-6 flex h-[52px] w-[52px] items-center justify-center rounded-2xl border border-white/10 bg-card shadow-card md:h-[60px] md:w-[60px]">
                  <div className={`flex h-full w-full items-center justify-center rounded-2xl bg-gradient-to-br ${level.accent}`}>
                    <span className="font-display text-lg font-semibold text-foreground md:text-xl">
                      0{level.number}
                    </span>
                  </div>
                </div>

                <div className="card-base card-hover group p-6 sm:p-8">
                  <div className="flex flex-wrap items-start justify-between gap-4">
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-[11px] uppercase tracking-[0.16em] text-violet-300">
                          Level 0{level.number}
                        </span>
                        <LevelViewerBadge levelSlug={level.slug} seed={level.viewers} size="xs" />
                      </div>
                      <h2 className="mt-2 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
                        {level.title}
                      </h2>
                      <p className="mt-1 text-[15px] text-muted">{level.subtitle}</p>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {level.tags.slice(0, 4).map((t) => (
                        <span key={t} className="chip">{t}</span>
                      ))}
                    </div>
                  </div>

                  <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-foreground/85">
                    {level.description}
                  </p>

                  <div className="mt-6 grid gap-4 sm:grid-cols-3">
                    {[
                      { label: "Durasi", value: level.duration },
                      { label: "Materi", value: `${level.lessonsCount} lesson` },
                      { label: "Level", value: level.difficulty },
                    ].map((m) => (
                      <div key={m.label} className="rounded-xl border border-white/5 bg-white/[0.02] px-4 py-3">
                        <div className="text-[11px] uppercase tracking-wider text-muted">{m.label}</div>
                        <div className="mt-1 text-sm font-medium text-foreground">{m.value}</div>
                      </div>
                    ))}
                  </div>

                  <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-white/5 pt-6">
                    <div className="flex items-center gap-2 text-sm text-muted">
                      <Trophy size={14} className="text-violet-300" />
                      Project: <span className="text-foreground">{level.miniProject}</span>
                    </div>
                  </div>

                  {/* Lesson list */}
                  {level.lessons.length > 0 && (
                    <div className="mt-6 grid gap-2 border-t border-white/5 pt-6 sm:grid-cols-2 lg:grid-cols-3">
                      {level.lessons.map((lesson) => (
                        <div
                          key={lesson.slug}
                          className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/[0.02] p-3"
                        >
                          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-violet-300">
                            <BookOpen size={14} />
                          </span>
                          <div className="min-w-0 flex-1">
                            <div className="truncate text-sm font-medium text-foreground">{lesson.title}</div>
                            <div className="mt-0.5 text-xs text-muted">
                              <Clock size={10} className="inline mr-1" />
                              {lesson.duration}
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </article>
            </Reveal>
          ))}
        </div>
      </div>

      {/* Switch path */}
      <Reveal>
        <div className="mt-16 text-center">
          <p className="text-sm text-muted">
            Ingin jalur yang lebih fokus ke fundamental?
          </p>
          <Link href="/roadmap" className="mt-2 inline-flex items-center gap-2 text-sm font-medium text-accent-hover hover:text-foreground">
            Lihat Roadmap Manual Coding <ArrowRight size={14} />
          </Link>
        </div>
      </Reveal>
    </div>
  );
}
