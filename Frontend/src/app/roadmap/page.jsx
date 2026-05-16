import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Clock,
  GraduationCap,
  Rocket,
  Trophy,
  Users,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import LevelViewerBadge from "@/components/ui/LevelViewerBadge";
import LessonViewerBadge from "@/components/ui/LessonViewerBadge";
import CategoryTabs from "@/components/ui/CategoryTabs";
import { listCategories, getRoadmap } from "@/lib/api/content";
import {
  aggregateLevels,
  categoryToTab,
  levelTags,
} from "@/lib/roadmap-utils";
import { formatCompact } from "@/lib/utils";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Roadmap — Jalur Belajar Developer",
  description:
    "Jalur belajar terstruktur untuk Frontend, Backend, dan Vibe Coding. Setiap level memiliki materi, quiz, dan mini project.",
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
        <div className="absolute left-0 top-6 flex h-[52px] w-[52px] items-center justify-center rounded-2xl border border-border bg-card shadow-card md:h-[60px] md:w-[60px]">
          <div
            className={`flex h-full w-full items-center justify-center rounded-2xl bg-gradient-to-br ${level.accent_color}`}
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
                {isComingSoon ? (
                  <span className="rounded-full border border-border bg-black/30 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
                    Coming Soon
                  </span>
                ) : (
                  <LevelViewerBadge count={level.base_viewers} size="xs" />
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

          <div className="mt-6 grid gap-4 sm:grid-cols-4">
            {[
              { label: "Durasi", value: level.duration },
              { label: "Level", value: level.difficulty },
              { label: "Materi", value: `${level.lessons.length} lesson` },
              { label: "Quiz", value: `${level.quiz_count || 3} soal` },
            ].map((m) => (
              <div
                key={m.label}
                className="rounded-xl border border-border bg-black/30 px-4 py-3"
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

          <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-border pt-6">
            <div className="flex items-center gap-2 text-sm text-muted">
              <Trophy size={14} className="text-accent-hover" />
              Mini project:{" "}
              <span className="text-foreground">{level.mini_project}</span>
            </div>
            {!isComingSoon && level.lessons[0] && (
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

          {!isComingSoon && level.lessons.length > 0 && (
            <div className="mt-6 grid gap-2 border-t border-border pt-6 sm:grid-cols-2 lg:grid-cols-3">
              {level.lessons.map((lesson) => (
                <Link
                  key={lesson.slug}
                  href={lessonHref(lesson.slug)}
                  className="group/lesson flex items-center gap-3 rounded-xl border border-border bg-black/30 p-3 transition-colors hover:border-accent/30 hover:bg-black/30"
                >
                  <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border border-border bg-black/30 text-accent-hover">
                    <BookOpen size={14} />
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="truncate text-sm font-medium text-foreground">
                      {lesson.title}
                    </div>
                    <div className="mt-1 flex items-center gap-2 text-xs text-muted">
                      <Clock size={10} />
                      {lesson.duration}
                      <span className="text-white/10">·</span>
                      <LessonViewerBadge
                        count={lesson.base_viewers}
                        showLabel={false}
                        bordered={false}
                        iconSize={10}
                      />
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}

          {isComingSoon && (
            <div className="mt-6 border-t border-border pt-6">
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
  const tabs = categories.map(categoryToTab);
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
  return { tabs, roadmapMap: new Map(roadmaps) };
}

export default async function RoadmapPage() {
  let tabs;
  let roadmapMap;
  try {
    ({ tabs, roadmapMap } = await loadAll());
  } catch {
    return (
      <div className="container-page py-16">
        <h1 className="font-display text-3xl font-semibold">Roadmap</h1>
        <p className="mt-4 text-sm text-muted">
          Backend belum bisa dijangkau. Jalankan FastAPI di port 8000 dan
          coba lagi.
        </p>
      </div>
    );
  }

  // Manual path = "frontend" by default. Vibe has its own dedicated page.
  const visibleTabs = tabs.filter((t) => t.id !== "vibe");
  const allLevels = visibleTabs.flatMap(
    (t) => roadmapMap.get(t.id) || []
  );
  const { totalLessons, totalViewers } = aggregateLevels(allLevels);

  return (
    <div className="container-page py-16">
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

      <Reveal delay={0.12}>
        <Link
          href="/persiapan"
          className="group mt-8 flex items-center justify-between gap-4 rounded-2xl border border-accent/20 bg-gradient-to-r from-accent/10 via-card to-card p-5 transition-colors hover:border-accent/40"
        >
          <div className="flex items-center gap-3">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl border border-accent/30 bg-accent/10 text-accent-hover">
              <Rocket size={15} />
            </span>
            <div>
              <div className="font-display text-sm font-semibold">
                Pertama kali di sini? Siapkan alatnya dulu.
              </div>
              <div className="text-xs text-muted">
                Install VS Code, browser, dan kenalan dengan ekstensi wajib.
              </div>
            </div>
          </div>
          <span className="hidden items-center gap-1 text-sm text-accent-hover group-hover:text-foreground sm:inline-flex">
            Lihat persiapan
            <ArrowRight size={14} />
          </span>
        </Link>
      </Reveal>

      <Reveal delay={0.15}>
        <div className="mt-8 grid grid-cols-2 gap-3 sm:grid-cols-4">
          {[
            {
              icon: Users,
              label: "Total viewers",
              value: formatCompact(totalViewers),
            },
            { icon: BookOpen, label: "Total materi", value: totalLessons },
            { icon: Trophy, label: "Mini project", value: allLevels.length },
            { icon: Clock, label: "Estimasi", value: "15 minggu" },
          ].map((s) => (
            <div
              key={s.label}
              className="card-base flex items-center gap-3 p-4"
            >
              <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-black/30 text-accent-hover">
                <s.icon size={16} />
              </div>
              <div>
                <div className="text-xs text-muted">{s.label}</div>
                <div className="font-display text-lg font-semibold">
                  {s.value}
                </div>
              </div>
            </div>
          ))}
        </div>
      </Reveal>

      <div className="mt-12">
        <CategoryTabs
          categories={visibleTabs}
          panels={visibleTabs.map((tab) => ({
            id: tab.id,
            content: (
              <div className="relative">
                <div className="absolute left-[26px] top-6 bottom-6 w-px bg-gradient-to-b from-accent/40 via-white/10 to-transparent md:left-[30px]" />
                <div className="space-y-5">
                  {(roadmapMap.get(tab.id) || []).map((level, i) => (
                    <LevelArticle
                      key={level.id}
                      level={level}
                      i={i}
                      basePath="/materi"
                    />
                  ))}
                  {(roadmapMap.get(tab.id) || []).length === 0 && (
                    <p className="text-sm text-muted">
                      Belum ada level untuk kategori ini.
                    </p>
                  )}
                </div>
              </div>
            ),
          }))}
        />
      </div>
    </div>
  );
}
