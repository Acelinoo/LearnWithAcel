import Link from "next/link";
import { redirect } from "next/navigation";
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
import LevelLeaderboard from "@/components/dashboard/LevelLeaderboard";
import ProgressByLevel from "@/components/dashboard/ProgressByLevel";
import ContinueLearning from "@/components/dashboard/ContinueLearning";
import LogoutButton from "@/components/auth/LogoutButton";
import { getServerUser, getServerStats } from "@/lib/api/server";
import { listCategories, getRoadmap } from "@/lib/api/content";
import {
  aggregateLevels,
  getPopularLessons,
  getTopLevel,
} from "@/lib/roadmap-utils";
import DashboardProgressCard from "@/components/dashboard/DashboardProgressCard";
import { formatCompact } from "@/lib/utils";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Dashboard — Aktivitas Platform",
  description:
    "Pantau aktivitas platform: progress kamu, materi terpopuler, level paling banyak dibuka.",
};


export default async function DashboardPage() {
  const user = await getServerUser();
  if (!user) redirect("/login?redirectTo=/dashboard");
  if (!user.selected_role) redirect("/onboarding");

  const [stats, categories] = await Promise.all([
    getServerStats().catch(() => null),
    listCategories().catch(() => []),
  ]);

  const roadmaps = await Promise.all(
    categories.map(async (c) => {
      try {
        const r = await getRoadmap(c.slug);
        return [c.slug, r.levels];
      } catch {
        return [c.slug, []];
      }
    })
  );
  const roadmapMap = Object.fromEntries(roadmaps);
  
  const frontend = { levels: roadmapMap[user.selected_role] || [] };

  const levels = frontend?.levels ?? [];
  const popularLessons = getPopularLessons(levels, 5);
  const topLevel = getTopLevel(levels);
  const { totalLessons, totalViewers } = aggregateLevels(levels);

  const displayName =
    user.full_name || user.email?.split("@")[0] || "Learner";

  return (
    <div className="w-full max-w-full overflow-x-hidden px-4 sm:px-6 lg:px-8 py-16">
      <Reveal>
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div>
            <span className="section-eyebrow">
              <Sparkles size={12} />
              Dashboard
            </span>
            <h1 className="mt-4 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
              Halo, {displayName}.
            </h1>
            <p className="mt-2 text-[15px] text-muted">
              Lihat progress kamu, lalu lanjut ke materi berikutnya.
            </p>
          </div>
          <div className="flex items-center gap-2">
            <LogoutButton variant="secondary" />
            <Link href="/roadmap" className="btn-primary">
              <PlayCircle size={16} />
              Mulai belajar
            </Link>
          </div>
        </div>
      </Reveal>

      {/* Bento grid stats */}
      <div className="mt-10 grid gap-4 grid-cols-1 lg:grid-cols-2 items-start">
        <Reveal>
          <DashboardProgressCard 
            stats={stats}
            categories={categories}
            roadmapMap={roadmapMap}
            defaultRole={user.selected_role}
          />
        </Reveal>

        <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-2 gap-4">
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
              sub: "frontend path",
            },
            {
              icon: Users,
              label: "Paling populer",
              value: topLevel ? `0${topLevel.number}` : "-",
              sub: topLevel?.title ?? "Belum ada level",
            },
          ].map((s, i) => (
            <Reveal key={s.label} delay={0.05 * (i + 1)}>
              <div className="card-base flex h-[160px] flex-col justify-between p-4 sm:p-5">
                <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-accent-hover">
                  <s.icon size={16} />
                </div>
                <div className="mt-6">
                  <div className="font-display text-2xl font-semibold">
                    {s.value}
                  </div>
                  <div className="mt-1 text-xs text-muted">{s.label}</div>
                  <div className="text-xs text-muted/70 line-clamp-1">{s.sub}</div>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>

      {stats && (
        <Reveal>
          <div className="mt-10">
            <ContinueLearning byLevel={stats.by_level} />
          </div>
        </Reveal>
      )}

      <div className="mt-10 grid gap-6 grid-cols-1 lg:grid-cols-3">
        {/* Popular lessons */}
        <Reveal className="lg:col-span-2">
          <section className="card-base p-4 sm:p-6 md:p-8">
            <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
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
                className="shrink-0 text-sm text-muted transition-colors hover:text-accent-hover"
              >
                Lihat semua
              </Link>
            </div>

            <ol className="mt-6 space-y-2">
              {popularLessons.length === 0 && (
                <p className="text-sm text-muted">
                  Belum ada materi. Tambahkan dari panel admin terlebih dulu.
                </p>
              )}
              {popularLessons.map((l, idx) => (
                <li key={`${l.levelSlug}/${l.slug}`}>
                  <Link
                    href={`/materi/${l.levelSlug}/${l.slug}`}
                    className="group flex items-center gap-3 sm:gap-4 rounded-xl border border-white/5 bg-white/[0.02] p-3 sm:p-4 transition-all hover:border-accent/30 hover:bg-white/[0.04]"
                  >
                    <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] font-mono text-xs text-accent-hover">
                      {String(idx + 1).padStart(2, "0")}
                    </span>
                    <div className="min-w-0 flex-1">
                      <div className="text-[11px] uppercase tracking-wider text-muted line-clamp-1">
                        Level 0{l.levelNumber} — {l.levelTitle}
                      </div>
                      <div className="mt-0.5 line-clamp-2 text-sm font-medium text-foreground group-hover:text-accent-hover">
                        {l.title}
                      </div>
                    </div>
                    <div className="hidden shrink-0 items-center gap-4 sm:flex">
                      <span className="flex items-center gap-1.5 text-xs text-muted">
                        <Clock size={12} />
                        {l.duration}
                      </span>
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
          <Reveal>
            <section className="card-base p-4 sm:p-6">
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

          <Reveal delay={0.05}>
            <section className="relative overflow-hidden rounded-2xl border border-accent/25 bg-gradient-to-br from-accent/10 via-card to-card p-4 sm:p-6">
              <div className="pointer-events-none absolute -right-12 -top-12 h-32 w-32 rounded-full bg-accent/20 blur-3xl" />
              <div className="relative">
                <div className="flex items-center gap-2">
                  <Sparkles size={14} className="text-accent-hover" />
                  <h3 className="font-display text-sm font-semibold">
                    Akun kamu aktif
                  </h3>
                </div>
                <p className="mt-3 text-sm leading-relaxed text-muted">
                  Masuk sebagai{" "}
                  <span className="text-foreground/90">{user.email}</span>.
                  Progress lesson tersinkron otomatis ke akun ini.
                </p>
                <div className="mt-4">
                  <LogoutButton variant="ghost" className="px-3" />
                </div>
              </div>
            </section>
          </Reveal>
        </div>
      </div>


    </div>
  );
}
