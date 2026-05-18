import Link from "next/link";
import { redirect } from "next/navigation";
import {
  ArrowRight,
  BookOpen,
  Flame,
  Layers,
  PlayCircle,
  Sparkles,
  TrendingUp,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ProgressByLevel from "@/components/dashboard/ProgressByLevel";
import ContinueLearning from "@/components/dashboard/ContinueLearning";
import EngagementHero from "@/components/dashboard/EngagementHero";
import LogoutButton from "@/components/auth/LogoutButton";
import { getServerUser, getServerStats } from "@/lib/api/server";
import { getRoadmap } from "@/lib/api/content";
import { aggregateLevels } from "@/lib/roadmap-utils";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Dashboard — Aktivitas Platform",
  description:
    "Pantau progress kamu, lanjut ke materi berikutnya, dan jaga streak harian.",
};

async function loadFrontendRoadmap() {
  try {
    return await getRoadmap("frontend");
  } catch {
    return null;
  }
}

export default async function DashboardPage() {
  const user = await getServerUser();
  if (!user) redirect("/login?redirectTo=/dashboard");

  const [stats, frontend] = await Promise.all([
    getServerStats(),
    loadFrontendRoadmap(),
  ]);

  const levels = frontend?.levels ?? [];
  const { totalLessons } = aggregateLevels(levels);

  const displayName =
    user.full_name || user.email?.split("@")[0] || "Learner";

  const xp = stats?.xp_total ?? 0;
  const streak = stats?.current_streak ?? 0;
  const longestStreak = stats?.longest_streak ?? 0;

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
              Halo, {displayName}.
            </h1>
            <p className="mt-2 text-[15px] text-muted">
              Lihat progress kamu, lalu lanjut ke materi berikutnya.
            </p>
          </div>
          <div className="flex items-center gap-2">
            <LogoutButton variant="secondary" />
            <Link href="/pilih-jalur" className="btn-primary">
              <PlayCircle size={16} />
              Mulai belajar
            </Link>
          </div>
        </div>
      </Reveal>

      {/* XP + streak strip (live, listens to progress events) */}
      <Reveal delay={0.05}>
        <div className="mt-8">
          <EngagementHero
            initialXp={xp}
            initialStreak={streak}
            initialLongestStreak={longestStreak}
          />
        </div>
      </Reveal>

      {/* Progress overview */}
      <div className="mt-10 grid gap-4 md:grid-cols-6">
        <Reveal className="md:col-span-4">
          <div className="card-base relative h-full overflow-hidden p-6 sm:p-8">
            <div className="pointer-events-none absolute -right-16 -top-16 h-48 w-48 rounded-full bg-accent/20 blur-3xl" />
            <div className="relative">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-xs uppercase tracking-[0.14em] text-muted">
                  <TrendingUp size={12} />
                  Progress kamu
                </div>
              </div>
              <div className="mt-5 flex items-end justify-between gap-6">
                <div>
                  <div className="font-display text-5xl font-semibold tabular-nums">
                    {stats
                      ? `${stats.completed_lessons} / ${stats.total_lessons}`
                      : "-"}
                  </div>
                  <div className="mt-2 text-sm text-muted">
                    materi sudah kamu selesaikan
                  </div>
                </div>
                <div className="flex items-center gap-1.5 rounded-full border border-emerald-400/30 bg-emerald-400/10 px-3 py-1 text-xs font-medium text-emerald-300">
                  <Flame size={12} />
                  {stats ? `${stats.overall_percentage.toFixed(0)}%` : "0%"}
                </div>
              </div>

              {stats && (
                <div className="mt-8">
                  <ProgressByLevel byLevel={stats.by_level} />
                </div>
              )}
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
            sub: "frontend path",
          },
        ].map((s, i) => (
          <Reveal
            key={s.label}
            delay={0.05 * (i + 1)}
            className="md:col-span-1"
          >
            <div className="card-base flex h-full flex-col justify-between p-5">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-black/30 text-accent-hover">
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

      {stats && (
        <Reveal>
          <div className="mt-10">
            <ContinueLearning
              byLevel={stats.by_level}
              continueLesson={stats.continue_lesson ?? null}
            />
          </div>
        </Reveal>
      )}

      {/* Account card */}
      <div className="mt-10">
        <Reveal>
          <section className="relative overflow-hidden rounded-2xl border border-accent/25 bg-gradient-to-br from-accent/10 via-card to-card p-6 sm:p-8">
            <div className="pointer-events-none absolute -right-12 -top-12 h-32 w-32 rounded-full bg-accent/20 blur-3xl" />
            <div className="relative flex flex-wrap items-start justify-between gap-4">
              <div>
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
              </div>
              <Link
                href="/roadmap"
                className="inline-flex items-center gap-1.5 text-sm text-accent-hover transition-colors hover:text-foreground"
              >
                Buka roadmap
                <ArrowRight size={14} />
              </Link>
            </div>
          </section>
        </Reveal>
      </div>
    </div>
  );
}
