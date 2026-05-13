import Link from "next/link";
import { ArrowRight } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";
import LevelViewerBadge from "@/components/ui/LevelViewerBadge";
import CategoryTabs from "@/components/ui/CategoryTabs";
import { levels, backendLevels, fullstackLevels, categories } from "@/lib/roadmap";

function LevelCard({ level }) {
  const isComingSoon = level.comingSoon;

  return (
    <div
      className={`group card-base relative block h-full overflow-hidden p-6 ${
        isComingSoon ? "opacity-60" : "card-hover"
      }`}
    >
      <div
        className={`pointer-events-none absolute inset-0 bg-gradient-to-br ${level.accent} opacity-0 transition-opacity duration-500 ${
          !isComingSoon ? "group-hover:opacity-100" : ""
        }`}
      />
      <div className="relative">
        <div className="flex items-center justify-between">
          <span className="font-mono text-[11px] uppercase tracking-[0.16em] text-accent-hover">
            Level 0{level.number}
          </span>
          {isComingSoon ? (
            <span className="rounded-full border border-white/10 bg-white/[0.04] px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
              Coming Soon
            </span>
          ) : (
            <LevelViewerBadge
              levelSlug={level.slug}
              seed={level.viewers}
              size="xs"
            />
          )}
        </div>

        <h3 className="mt-4 font-display text-xl font-semibold tracking-tight">
          {level.title}
        </h3>
        <p className="mt-1.5 text-sm leading-relaxed text-muted">
          {level.subtitle}
        </p>

        <div className="mt-6 flex flex-wrap gap-1.5">
          {level.tags.slice(0, 3).map((t) => (
            <span
              key={t}
              className="rounded-full border border-white/10 bg-white/[0.02] px-2 py-0.5 text-[11px] text-muted"
            >
              {t}
            </span>
          ))}
        </div>

        <div className="mt-5 flex items-center gap-4 border-t border-white/5 pt-4 text-xs text-muted">
          <span>{level.lessonsCount} materi</span>
          <span className="h-1 w-1 rounded-full bg-white/20" />
          <span>{level.duration}</span>
        </div>
      </div>
    </div>
  );
}

export default function RoadmapPreview() {
  const frontendLevels = levels.filter((l) => l.category === "frontend");

  return (
    <section className="container-page py-24">
      <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-end">
        <SectionHeading
          eyebrow="Learning roadmap"
          title="Satu jalur belajar dari nol sampai siap kerja."
          description="Setiap level dibangun di atas level sebelumnya. Fokus, progresif, dan mudah diikuti."
          className="mb-0"
        />
        <Link href="/roadmap" className="btn-secondary shrink-0">
          Lihat Roadmap Lengkap
          <ArrowRight size={16} />
        </Link>
      </div>

      <div className="mt-10">
        <CategoryTabs
          categories={categories}
          panels={[
            {
              id: "frontend",
              content: (
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {frontendLevels.map((level, i) => (
                    <Reveal key={level.id} delay={i * 0.06}>
                      <Link
                        href={`/roadmap#${level.slug}`}
                        className="block h-full"
                      >
                        <LevelCard level={level} />
                      </Link>
                    </Reveal>
                  ))}
                </div>
              ),
            },
            {
              id: "backend",
              content: (
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {backendLevels.map((level, i) => (
                    <Reveal key={level.id} delay={i * 0.06}>
                      <LevelCard level={level} />
                    </Reveal>
                  ))}
                </div>
              ),
            },
            {
              id: "fullstack",
              content: (
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {fullstackLevels.map((level, i) => (
                    <Reveal key={level.id} delay={i * 0.06}>
                      <LevelCard level={level} />
                    </Reveal>
                  ))}
                </div>
              ),
            },
          ]}
        />
      </div>
    </section>
  );
}
