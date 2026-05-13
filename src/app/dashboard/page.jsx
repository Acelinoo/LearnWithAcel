import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Clock,
  Flame,
  Layers,
  PlayCircle,
  Sparkles,
  TrendingUp,
  Users,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import LessonViewerBadge from "@/components/ui/LessonViewerBadge";
import ViewerBadge from "@/components/ui/ViewerBadge";
import LevelLeaderboard from "@/components/dashboard/LevelLeaderboard";
import LiveGlobalCount from "@/components/dashboard/LiveGlobalCount";
import ViewerBarChart from "@/components/dashboard/ViewerBarChart";
import {
  levels,
  totalLessons,
  totalViewers,
  topLevel,
  getPopularLessons,
} from "@/lib/roadmap";

export const metadata = {
  title: "Dashboard — Aktivitas Platform",
  description:
    "Pantau aktivitas platform: materi terpopuler, level paling banyak dibuka, dan statistik viewer real-time.",
};

export default function DashboardPage() {
  const popularLessons = getPopularLessons(5);

  return (
    <div className="container-page py-16">
      <Reveal>
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div>
            <span className="section-eyebrow">
              <Sparkles size={12} />
              Dashboard
            </span>
            <h1 className="mt-4 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
              Aktivitas platform hari ini.
            </h1>
            <p className="mt-2 text-[15px] text-muted">
              Lihat apa yang paling banyak dibuka learner lain, lalu ikutan
              belajar bareng.
            </p>
          </div>
          <Link href="/persiapan" className="btn-primary">
            <PlayCircle size={16} />
            Mulai belajar sekarang
          </Link>
        </div>
      </Reveal>

      {/* Bento grid stats */}
      <div className="mt-10 grid gap-4 md:grid-cols-6">
        <Reveal className="md:col-span-3">
          <div className="card-base relative h-full overflow-hidden p-6 sm:p-8">
            <div className="pointer-events-none absolute -right-16 -top-16 h-48 w-48 rounded-full bg-accent/20 blur-3xl" />
            <div className="relative">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-xs uppercase tracking-[0.14em] text-muted">
                  <TrendingUp size={12} />
                  Total viewers
                </div>
                <ViewerBadge compact />
              </div>
              <div className="mt-5 flex items-end justify-between gap-6">
                <div>
                  <div className="font-display text-5xl font-semibold tabular-nums">
                    <LiveGlobalCount fallback={totalViewers} />
                  </div>
                  <div className="mt-2 text-sm text-muted">
                    pengunjung sudah menjelajah platform ini
                  </div>
                </div>
                <div className="flex items-center gap-1.5 rounded-full border border-emerald-400/30 bg-emerald-400/10 px-3 py-1 text-xs font-medium text-emerald-300">
                  <Flame size={12} />
                  Trending
                </div>
              </div>

              <div className="mt-8">
                <ViewerBarChart levels={levels} />
              </div>
            </div>
          </div>
        </Reveal>

        {[
          {
            icon: BookOpen,
            label: "Total materi",
            value: totalLessons,
            sub: "di seluruh level",
          },
          {
            icon: Layers,
            label: "Level tersedia",
            value: `${levels.length}`,
            sub: "dari basic ke karir",
          },
          {
            icon: Users,
            label: "Paling populer",
            value: `0${topLevel.number}`,
            sub: topLevel.title,
          },
        ].map((s, i) => (
          <Reveal key={s.label} delay={0.05 * (i + 1)} className="md:col-span-1">
            <div className="card-base flex h-full flex-col justify-between p-5">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-accent-hover">
                <s.icon size={16} />
              </div>
              <div className="mt-6">
                <div className="font-display text-2xl font-semibold">
                  {s.value}
                </div>
                <div className="mt-1 text-xs text-muted">{s.label}</div>
                <div className="text-xs text-muted/70">{s.sub}</div>
              </div>
            </div>
          </Reveal>
        ))}
      </div>

      <div className="mt-10 grid gap-6 lg:grid-cols-3">
        {/* Popular lessons */}
        <Reveal className="lg:col-span-2">
          <section className="card-base p-6 sm:p-8">
            <div className="flex items-center justify-between">
              <div>
                <div className="flex items-center gap-2">
                  <Flame size={16} className="text-accent-hover" />
                  <h2 className="font-display text-xl font-semibold">
                    Materi populer
                  </h2>
                </div>
                <p className="mt-1 text-sm text-muted">
                  Paling banyak dibuka oleh pengunjung minggu ini.
                </p>
              </div>
              <Link
                href="/roadmap"
                className="text-sm text-muted transition-colors hover:text-accent-hover"
              >
                Lihat semua
              </Link>
            </div>

            <ol className="mt-6 space-y-2">
              {popularLessons.map((l, idx) => (
                <li key={`${l.levelSlug}/${l.slug}`}>
                  <Link
                    href={`/materi/${l.levelSlug}/${l.slug}`}
                    className="group flex items-center gap-4 rounded-xl border border-white/5 bg-white/[0.02] p-4 transition-all hover:border-accent/30 hover:bg-white/[0.04]"
                  >
                    <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] font-mono text-xs text-accent-hover">
                      {String(idx + 1).padStart(2, "0")}
                    </span>
                    <div className="min-w-0 flex-1">
                      <div className="text-[11px] uppercase tracking-wider text-muted">
                        Level 0{l.levelNumber} — {l.levelTitle}
                      </div>
                      <div className="mt-0.5 truncate text-sm font-medium text-foreground group-hover:text-accent-hover">
                        {l.title}
                      </div>
                    </div>
                    <div className="hidden shrink-0 items-center gap-4 sm:flex">
                      <span className="flex items-center gap-1.5 text-xs text-muted">
                        <Clock size={12} />
                        {l.duration}
                      </span>
                      <LessonViewerBadge
                        lessonKey={`${l.levelSlug}/${l.slug}`}
                        seed={l.viewers}
                        showLabel={false}
                        bordered={false}
                        iconSize={12}
                      />
                    </div>
                    <ArrowRight
                      size={14}
                      className="shrink-0 text-muted transition-transform group-hover:translate-x-0.5 group-hover:text-accent-hover"
                    />
                  </Link>
                </li>
              ))}
            </ol>
          </section>
        </Reveal>

        <div className="space-y-6">
          {/* Level viewers leaderboard */}
          <Reveal>
            <section className="card-base p-6">
              <div className="flex items-center gap-2">
                <TrendingUp size={16} className="text-accent-hover" />
                <h2 className="font-display text-base font-semibold">
                  Level terpopuler
                </h2>
              </div>
              <div className="mt-4">
                <LevelLeaderboard levels={levels} />
              </div>
            </section>
          </Reveal>

          {/* Hint card */}
          <Reveal delay={0.05}>
            <section className="relative overflow-hidden rounded-2xl border border-accent/25 bg-gradient-to-br from-accent/10 via-card to-card p-6">
              <div className="pointer-events-none absolute -right-12 -top-12 h-32 w-32 rounded-full bg-accent/20 blur-3xl" />
              <div className="relative">
                <div className="flex items-center gap-2">
                  <Sparkles size={14} className="text-accent-hover" />
                  <h3 className="font-display text-sm font-semibold">
                    Belum ada sesi login
                  </h3>
                </div>
                <p className="mt-3 text-sm leading-relaxed text-muted">
                  Fitur progress personal, bookmark, dan history akan muncul
                  setelah sistem akun siap. Untuk sekarang, dashboard fokus pada
                  aktivitas komunitas.
                </p>
              </div>
            </section>
          </Reveal>
        </div>
      </div>
    </div>
  );
}
