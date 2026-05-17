import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowRight,
  BookOpen,
  Bot,
  Clock,
  Code2,
  Compass,
  Layers,
  PlayCircle,
  Sparkles,
  Wrench,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ViewTracker from "@/components/ui/ViewTracker";
import { JALUR_META, getJalurMeta } from "@/lib/jalur-data";

export const dynamic = "force-dynamic";

export function generateStaticParams() {
  return Object.keys(JALUR_META).map((path) => ({ path }));
}

export function generateMetadata({ params }) {
  const meta = getJalurMeta(params.path);
  if (!meta) return { title: "Jalur tidak ditemukan" };
  return {
    title: `${meta.eyebrow} · LearnWithAcel`,
    description: meta.subtitle,
  };
}

const TONE = {
  accent: {
    chip: "border-accent/25 bg-accent/[0.08] text-accent-hover",
    badge: "border-accent/30 bg-accent/10 text-accent-hover",
    softBorder: "hover:border-accent/40",
    iconWrap: "border-accent/20 bg-accent/[0.06] text-accent-hover",
    glow: "from-accent/30",
    barFrom: "from-accent",
    barTo: "to-accent-hover",
    btn: "bg-accent text-foreground hover:bg-accent-hover",
  },
  sky: {
    chip: "border-sky-400/25 bg-sky-500/[0.08] text-sky-300",
    badge: "border-sky-400/30 bg-sky-400/10 text-sky-300",
    softBorder: "hover:border-sky-400/40",
    iconWrap: "border-sky-400/20 bg-sky-500/[0.06] text-sky-300",
    glow: "from-sky-500/25",
    barFrom: "from-sky-400",
    barTo: "to-sky-300",
    btn: "bg-sky-500 text-foreground hover:bg-sky-400",
  },
};

export default function JalurPathPage({ params }) {
  const meta = getJalurMeta(params.path);
  if (!meta) notFound();

  const tone = TONE[meta.badgeTone];
  const PathIcon = meta.path === "vibe" ? Bot : Code2;
  const totalLessons = meta.lessons.length;

  return (
    <div className="container-page py-16">
      <ViewTracker entityType="page" entityId={`jalur-${meta.path}`} />

      <Reveal>
        <Link
          href="/pilih-jalur"
          className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
        >
          ← Kembali ke pilih jalur
        </Link>
      </Reveal>

      {/* Hero */}
      <section className="relative mt-8 overflow-hidden rounded-3xl border border-border bg-card p-8 sm:p-12">
        <div
          aria-hidden
          className={`pointer-events-none absolute -right-24 -top-24 h-72 w-72 rounded-full bg-gradient-to-br ${tone.glow} to-transparent blur-3xl opacity-70`}
        />
        <div
          aria-hidden
          className="pointer-events-none absolute -bottom-24 left-1/3 h-64 w-64 rounded-full bg-accent-hover/15 blur-3xl"
        />

        <div className="relative">
          <Reveal delay={0.05}>
            <div className="flex flex-wrap items-center gap-2">
              <span className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.16em] ${tone.badge}`}>
                <PathIcon size={12} />
                {meta.badge}
              </span>
              <span className="font-mono text-[10px] uppercase tracking-[0.16em] text-muted">
                {meta.tagline}
              </span>
            </div>
          </Reveal>

          <Reveal delay={0.1}>
            <h1 className="mt-6 max-w-3xl font-display text-4xl font-semibold leading-[1.1] tracking-tight text-balance sm:text-5xl">
              {meta.title}
            </h1>
          </Reveal>

          <Reveal delay={0.15}>
            <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
              {meta.subtitle}
            </p>
          </Reveal>

          <Reveal delay={0.2}>
            <div className="mt-8 flex flex-wrap items-center gap-3">
              <Link
                href={`/jalur/${meta.path}/${meta.lessons[0].slug}`}
                className={`inline-flex items-center gap-2 rounded-xl px-5 py-2.5 text-sm font-medium transition-colors ${tone.btn}`}
              >
                <PlayCircle size={16} />
                Mulai dari lesson pertama
              </Link>

              <Link
                href={meta.setupHref}
                className="btn-secondary"
              >
                <Wrench size={14} />
                {meta.setupCtaLabel}
              </Link>
            </div>
          </Reveal>

          <Reveal delay={0.25}>
            <div className="mt-10 grid grid-cols-2 gap-3 sm:grid-cols-4">
              {[
                { icon: BookOpen, label: "Total lesson", value: `${totalLessons} lesson` },
                { icon: Clock, label: "Estimasi total", value: "~1 jam" },
                { icon: Layers, label: "Setelah ini", value: `Pilih ${meta.path === "vibe" ? "role" : "spesialisasi"}` },
                { icon: Sparkles, label: "Format", value: "Baca + praktik" },
              ].map((s) => (
                <div key={s.label} className="card-base flex items-center gap-3 p-4">
                  <div className={`flex h-9 w-9 items-center justify-center rounded-lg border ${tone.iconWrap}`}>
                    <s.icon size={16} />
                  </div>
                  <div className="min-w-0">
                    <div className="text-[11px] uppercase tracking-wider text-muted">
                      {s.label}
                    </div>
                    <div className="truncate text-sm font-medium text-foreground">
                      {s.value}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      {/* Intro line */}
      <Reveal delay={0.3}>
        <p className="mt-12 max-w-2xl text-[15px] leading-relaxed text-foreground/80">
          {meta.intro}
        </p>
      </Reveal>

      {/* Lessons list */}
      <section className="mt-10">
        <Reveal>
          <div className="flex items-baseline justify-between gap-3">
            <h2 className="font-display text-2xl font-semibold tracking-tight sm:text-3xl">
              {meta.eyebrow}
            </h2>
            <span className="hidden font-mono text-xs text-muted sm:inline">
              {totalLessons} lesson
            </span>
          </div>
        </Reveal>

        <div className="mt-6 space-y-3">
          {meta.lessons.map((lesson, i) => (
            <Reveal key={lesson.slug} delay={i * 0.04}>
              <Link
                href={`/jalur/${meta.path}/${lesson.slug}`}
                className={`group flex items-start gap-4 rounded-2xl border border-border bg-card p-5 transition-all duration-300 ${tone.softBorder} hover:-translate-y-0.5`}
              >
                <span className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border ${tone.iconWrap} font-mono text-sm`}>
                  {String(i + 1).padStart(2, "0")}
                </span>

                <div className="min-w-0 flex-1">
                  <h3 className="font-display text-base font-semibold tracking-tight text-foreground sm:text-lg">
                    {lesson.title}
                  </h3>
                  <p className="mt-1.5 line-clamp-2 text-sm leading-relaxed text-muted">
                    {lesson.summary}
                  </p>
                  <div className="mt-3 flex items-center gap-2 text-[11px] text-muted">
                    <Clock size={11} />
                    {lesson.duration}
                  </div>
                </div>

                <span className="hidden h-9 w-9 shrink-0 items-center justify-center rounded-full border border-border bg-black/30 text-muted transition-all group-hover:translate-x-0.5 group-hover:text-foreground sm:inline-flex">
                  <ArrowRight size={14} />
                </span>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* Role chooser */}
      <section id="pilih-role" className="mt-20 scroll-mt-24">
        <Reveal>
          <div className="flex items-center gap-2">
            <span className={`section-eyebrow`}>
              <Compass size={12} />
              {meta.path === "vibe" ? "Pilih role" : "Pilih spesialisasi"}
            </span>
          </div>
        </Reveal>

        <Reveal delay={0.05}>
          <h2 className="mt-4 max-w-3xl font-display text-2xl font-semibold tracking-tight sm:text-3xl">
            {meta.roleSectionTitle}
          </h2>
        </Reveal>

        <Reveal delay={0.1}>
          <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted">
            {meta.roleSectionSubtitle}
          </p>
        </Reveal>

        <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {meta.roles.map((role, i) => {
            const isAvailable = role.available;

            return (
              <Reveal key={role.slug} delay={0.1 + i * 0.04}>
                {isAvailable ? (
                  <Link
                    href={role.href}
                    className={`group block h-full overflow-hidden rounded-2xl border border-border bg-card p-6 transition-all duration-300 ${tone.softBorder} hover:-translate-y-0.5`}
                  >
                    <RoleCardBody role={role} tone={tone} available />
                  </Link>
                ) : (
                  <div className="relative h-full overflow-hidden rounded-2xl border border-border bg-card p-6 opacity-90">
                    <RoleCardBody role={role} tone={tone} available={false} />
                  </div>
                )}
              </Reveal>
            );
          })}
        </div>
      </section>

      {/* Full roadmap link (vibe only) */}
      {meta.fullRoadmapHref && meta.path === "vibe" && (
        <section className="mt-16">
          <Reveal>
            <Link
              href={meta.fullRoadmapHref}
              className={`group flex items-center justify-between gap-4 rounded-2xl border border-sky-400/20 bg-gradient-to-r from-sky-400/10 via-card to-card p-5 transition-colors hover:border-sky-400/40`}
            >
              <div className="flex items-center gap-3">
                <span className="flex h-10 w-10 items-center justify-center rounded-xl border border-sky-400/30 bg-sky-400/10 text-sky-300">
                  <Layers size={16} />
                </span>
                <div>
                  <div className="font-display text-sm font-semibold">
                    {meta.fullRoadmapLabel}
                  </div>
                  <div className="text-xs text-muted">
                    Lihat semua level lengkap dari mindset sampai database & auth.
                  </div>
                </div>
              </div>
              <span className="hidden items-center gap-1 text-sm text-sky-300 group-hover:text-foreground sm:inline-flex">
                Buka roadmap <ArrowRight size={14} />
              </span>
            </Link>
          </Reveal>
        </section>
      )}
    </div>
  );
}

function RoleCardBody({ role, tone, available }) {
  return (
    <>
      <div className="flex items-start justify-between gap-3">
        <span className={`rounded-full border px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-[0.12em] ${tone.badge}`}>
          {role.badge}
        </span>
        {!available && (
          <span className="rounded-full border border-border bg-black/30 px-2.5 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
            Coming soon
          </span>
        )}
      </div>

      <h3 className="mt-5 font-display text-lg font-semibold tracking-tight">
        {role.title}
      </h3>
      <p className="mt-1 font-mono text-[11px] text-muted">{role.tagline}</p>

      <p className="mt-3 text-[13.5px] leading-relaxed text-muted">
        {role.description}
      </p>

      <ul className="mt-4 space-y-1.5 text-sm text-foreground/85">
        {role.bullets.map((b) => (
          <li key={b} className="flex items-start gap-2">
            <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-current opacity-50" />
            {b}
          </li>
        ))}
      </ul>

      <div className="mt-5 inline-flex items-center gap-1.5 text-sm font-medium text-foreground/80">
        {available ? "Buka roadmap" : "Materi sedang disiapkan"}
        {available && <ArrowRight size={13} className="transition-transform group-hover:translate-x-0.5" />}
      </div>
    </>
  );
}
