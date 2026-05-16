import Link from "next/link";
import { ArrowUpRight, Clock, PlayCircle } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";
import { getRoadmap } from "@/lib/api/content";
import { getPopularLessons } from "@/lib/roadmap-utils";

async function loadPreviews() {
  const out = [];
  for (const slug of ["frontend", "vibe"]) {
    try {
      const r = await getRoadmap(slug);
      const popular = getPopularLessons(r.levels, 4);
      for (const lesson of popular) {
        out.push({
          tag: r.category.name,
          title: lesson.title,
          desc: lesson.summary,
          href:
            slug === "vibe"
              ? `/materi/vibe/${lesson.levelSlug}/${lesson.slug}`
              : `/materi/${lesson.levelSlug}/${lesson.slug}`,
          time: lesson.duration,
          views: lesson.base_viewers,
        });
      }
    } catch {
      // skip
    }
  }
  return out
    .sort((a, b) => b.views - a.views)
    .slice(0, 4)
    .map((p, i) => ({ ...p, featured: i === 0 }));
}

export default async function MaterialPreview() {
  const previews = await loadPreviews();

  if (previews.length === 0) return null;

  return (
    <section className="container-page py-24">
      <SectionHeading
        eyebrow="Preview materi"
        title="Materi yang ditulis seperti dokumentasi premium."
        description="Typography bersih, contoh konkret, dan ajakan langsung praktek di VS Code setiap materi."
      />

      <div className="grid grid-cols-1 gap-4 md:grid-cols-6">
        {previews.map((p, i) => (
          <Reveal
            key={p.href}
            delay={i * 0.05}
            className={p.featured ? "md:col-span-3 md:row-span-2" : "md:col-span-3"}
          >
            <Link
              href={p.href}
              className="group card-base card-hover relative flex h-full flex-col justify-between overflow-hidden p-6"
            >
              <div>
                <div className="flex items-center justify-between">
                  <span className="chip">
                    <PlayCircle size={12} />
                    {p.tag}
                  </span>
                  <ArrowUpRight
                    size={16}
                    className="text-muted transition-all duration-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5 group-hover:text-accent-hover"
                  />
                </div>
                <h3
                  className={`mt-5 font-display font-semibold tracking-tight text-balance ${
                    p.featured ? "text-2xl sm:text-3xl" : "text-lg"
                  }`}
                >
                  {p.title}
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-muted">
                  {p.desc}
                </p>
              </div>
              <div className="mt-6 flex items-center gap-2 text-xs text-muted">
                <Clock size={12} />
                {p.time} baca
              </div>
            </Link>
          </Reveal>
        ))}
      </div>
    </section>
  );
}
