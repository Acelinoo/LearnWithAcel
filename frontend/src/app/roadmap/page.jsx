import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Clock,
  GraduationCap,
  Rocket,
  Trophy,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import RoadmapFilter from "./RoadmapFilter";
import { listCategories, getRoadmap } from "@/lib/api/content";
import { getServerUser } from "@/lib/api/server";
import { levelTags } from "@/lib/roadmap-utils";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Roadmap — Jalur Belajar Developer",
  description:
    "Jalur belajar terstruktur untuk Web Development, Cybersecurity, dan Mobile Development.",
};

function LevelArticle({ level, i, basePath }) {
  const isComingSoon = level.coming_soon;
  const tags = levelTags(level);
  const lessonHref = (slug) => `${basePath}/${level.slug}/${slug}`;

  return (
    <Reveal delay={i * 0.05}>
      <article
        id={level.slug}
        className={`relative scroll-mt-24 pl-16 md:pl-20 ${
          isComingSoon ? "opacity-60" : ""
        }`}
      >
        <div className="absolute left-0 top-6 flex h-[52px] w-[52px] items-center justify-center rounded-2xl border border-white/10 bg-card shadow-card md:h-[60px] md:w-[60px]">
          <div
            className={`flex h-full w-full items-center justify-center rounded-2xl bg-gradient-to-br ${level.accent_color || "from-blue-500/20 to-purple-500/20"}`}
          >
            <span className="font-display text-lg font-semibold text-foreground md:text-xl">
              0{level.number}
            </span>
          </div>
        </div>

        <div className={`card-base group p-6 sm:p-8 ${!isComingSoon ? "card-hover" : ""}`}>
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div className="flex items-center gap-2">
                <span className="font-mono text-[11px] uppercase tracking-[0.16em] text-accent-hover">
                  Level 0{level.number}
                </span>
                {isComingSoon && (
                  <span className="rounded-full border border-white/10 bg-white/[0.04] px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
                    Coming Soon
                  </span>
                )}
              </div>
              <h2 className="mt-2 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
                {level.title}
              </h2>
              <p className="mt-1 text-[15px] text-muted">{level.subtitle}</p>
            </div>
            <div className="flex flex-wrap gap-2">
              {tags.slice(0, 4).map((t) => (
                <span key={t} className="chip">
                  {t}
                </span>
              ))}
            </div>
          </div>

          <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-foreground/85">
            {level.description}
          </p>

          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            {[
              { label: "Durasi", value: level.duration },
              { label: "Level", value: level.difficulty },
              { label: "Materi", value: `${level.lessons?.length || 0} lesson` },
            ].map((m) => (
              <div
                key={m.label}
                className="rounded-xl border border-white/5 bg-white/[0.02] px-4 py-3"
              >
                <div className="text-[11px] uppercase tracking-wider text-muted">
                  {m.label}
                </div>
                <div className="mt-1 text-sm font-medium text-foreground">
                  {m.value}
                </div>
              </div>
            ))}
          </div>

          <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-white/5 pt-6">
            <div className="flex items-center gap-2 text-sm text-muted">
              <Trophy size={14} className="text-accent-hover" />
              Mini project:{" "}
              <span className="text-foreground">{level.mini_project}</span>
            </div>
            {!isComingSoon && level.lessons?.[0] && (
              <div className="ml-auto flex gap-2">
                <Link
                  href={lessonHref(level.lessons[0].slug)}
                  className="btn-primary"
                >
                  Mulai level
                  <ArrowRight size={16} />
                </Link>
              </div>
            )}
          </div>

          {!isComingSoon && level.lessons?.length > 0 && (
            <div className="mt-6 grid gap-2 border-t border-white/5 pt-6 sm:grid-cols-2 lg:grid-cols-3">
              {level.lessons.map((lesson) => (
                <Link
                  key={lesson.slug}
                  href={lessonHref(lesson.slug)}
                  className="group/lesson flex items-center gap-3 rounded-xl border border-white/5 bg-white/[0.02] p-3 transition-colors hover:border-accent/30 hover:bg-white/[0.04]"
                >
                  <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-accent-hover">
                    <BookOpen size={14} />
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="truncate text-sm font-medium text-foreground">
                      {lesson.title}
                    </div>
                    <div className="mt-1 flex items-center gap-2 text-xs text-muted">
                      <Clock size={10} />
                      {lesson.duration}
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}

          {isComingSoon && (
            <div className="mt-6 border-t border-white/5 pt-6">
              <p className="text-sm italic text-muted">
                Materi sedang dalam pengembangan. Stay tuned!
              </p>
            </div>
          )}
        </div>
      </article>
    </Reveal>
  );
}

async function loadAll() {
  const categories = await listCategories();
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
  return { categories, roadmapMap: new Map(roadmaps) };
}

export default async function RoadmapPage() {
  const user = await getServerUser().catch(() => null);
  let categories = [];
  let roadmapMap = new Map();
  try {
    const loaded = await loadAll();
    categories = loaded.categories;
    roadmapMap = loaded.roadmapMap;
  } catch {
    return (
      <div className="container-page py-24">
        <h1 className="font-display text-3xl font-semibold">Roadmap</h1>
        <p className="mt-4 text-sm text-muted">
          Gagal mengambil data dari server.
        </p>
      </div>
    );
  }

  const defaultMainCategory = user?.selected_category || "web";
  const defaultRole = user?.selected_role || "frontend-developer";

  const panels = categories.map((cat) => ({
    id: cat.slug,
    content: (
      <div className="relative">
        <div className="absolute left-[26px] top-6 bottom-6 w-px bg-gradient-to-b from-accent/40 via-white/10 to-transparent md:left-[30px]" />
        <div className="space-y-5">
          {(roadmapMap.get(cat.slug) || [])
            .filter((l) => !l.coming_soon)
            .map((level, i) => (
            <LevelArticle
              key={level.id}
              level={level}
              i={i}
              basePath="/materi"
            />
          ))}
          {(roadmapMap.get(cat.slug) || []).filter((l) => !l.coming_soon).length === 0 && (
            <p className="text-sm text-muted">
              Belum ada level untuk kategori ini.
            </p>
          )}
        </div>
      </div>
    ),
  }));

  return (
    <div className="container-page py-24">
      <Reveal>
        <span className="section-eyebrow">
          <GraduationCap size={12} />
          Learning Roadmap
        </span>
      </Reveal>
      <Reveal delay={0.05}>
        <h1 className="mt-5 max-w-3xl font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
          Jalur belajar terstruktur dari nol menjadi developer nyata.
        </h1>
      </Reveal>
      <Reveal delay={0.1}>
        <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
          Setiap level dibangun di atas level sebelumnya. Baca materi, praktek
          langsung di VS Code, dan lanjut ke level berikutnya saat sudah nyaman.
        </p>
      </Reveal>


      <div className="mt-12">
        <RoadmapFilter
          categories={categories}
          panels={panels}
          defaultMainCategory={defaultMainCategory}
          defaultRole={defaultRole}
        />
      </div>
    </div>
  );
}
