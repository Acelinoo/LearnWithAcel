import Link from "next/link";
import { ArrowRight } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";
import CategoryTabs from "@/components/ui/CategoryTabs";
import { listCategories, getRoadmap } from "@/lib/api/content";
import { categoryToTab, levelTags } from "@/lib/roadmap-utils";

function LevelCard({ level }) {
  const isComingSoon = level.coming_soon;
  const tags = levelTags(level);

  return (
    <div
      className={`group card-base relative block h-full overflow-hidden p-6 ${
        isComingSoon ? "opacity-60" : "card-hover"
      }`}
    >
      <div
        className={`pointer-events-none absolute inset-0 bg-gradient-to-br ${level.accent_color} opacity-0 transition-opacity duration-500 ${
          !isComingSoon ? "group-hover:opacity-100" : ""
        }`}
      />
      <div className="relative">
        <div className="flex items-center justify-between">
          <span className="font-mono text-[11px] uppercase tracking-[0.16em] text-accent-hover">
            Level 0{level.number}
          </span>
          {isComingSoon && (
            <span className="rounded-full border border-border bg-black/30 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
              Coming Soon
            </span>
          )}
        </div>

        <h3 className="mt-4 font-display text-xl font-semibold tracking-tight">
          {level.title}
        </h3>
        <p className="mt-1.5 text-sm leading-relaxed text-muted">
          {level.subtitle}
        </p>

        <div className="mt-6 flex flex-wrap gap-1.5">
          {tags.slice(0, 3).map((t) => (
            <span
              key={t}
              className="rounded-full border border-border bg-black/30 px-2 py-0.5 text-[11px] text-muted"
            >
              {t}
            </span>
          ))}
        </div>

        <div className="mt-5 flex items-center gap-4 border-t border-border pt-4 text-xs text-muted">
          <span>{level.lessons.length} materi</span>
          <span className="h-1 w-1 rounded-full bg-white/20" />
          <span>{level.duration}</span>
        </div>
      </div>
    </div>
  );
}

function buildHref(categorySlug, level) {
  if (categorySlug === "vibe") return `/roadmap/vibe#${level.slug}`;
  return `/roadmap#${level.slug}`;
}

async function loadRoadmaps() {
  const categories = await listCategories();
  const slugs = categories.map((c) => c.slug);

  const roadmaps = await Promise.all(
    slugs.map(async (slug) => {
      try {
        const r = await getRoadmap(slug);
        return { slug, levels: r.levels };
      } catch {
        return { slug, levels: [] };
      }
    })
  );

  const map = new Map(roadmaps.map((r) => [r.slug, r.levels]));
  return { categories, roadmaps: map };
}

export default async function RoadmapPreview() {
  let categories;
  let roadmaps;
  try {
    ({ categories, roadmaps } = await loadRoadmaps());
  } catch {
    return (
      <section className="container-page py-24">
        <SectionHeading
          eyebrow="Learning roadmap"
          title="Satu jalur belajar dari nol sampai siap kerja."
          description="Setiap level dibangun di atas level sebelumnya. Fokus, progresif, dan mudah diikuti."
          className="mb-0"
        />
        <p className="mt-6 text-sm text-muted">
          Roadmap belum bisa dimuat. Pastikan backend FastAPI berjalan.
        </p>
      </section>
    );
  }

  const tabs = categories.map(categoryToTab);

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
          categories={tabs}
          panels={tabs.map((tab) => ({
            id: tab.id,
            content: (
              <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                {(roadmaps.get(tab.id) || []).map((level, i) => (
                  <Reveal key={level.id} delay={i * 0.06}>
                    {tab.available && !level.coming_soon ? (
                      <Link
                        href={buildHref(tab.id, level)}
                        className="block h-full"
                      >
                        <LevelCard level={level} />
                      </Link>
                    ) : (
                      <LevelCard level={level} />
                    )}
                  </Reveal>
                ))}
                {(roadmaps.get(tab.id) || []).length === 0 && (
                  <p className="col-span-full text-sm text-muted">
                    Belum ada level di kategori ini.
                  </p>
                )}
              </div>
            ),
          }))}
        />
      </div>
    </section>
  );
}
