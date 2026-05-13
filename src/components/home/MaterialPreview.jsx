import Link from "next/link";
import { ArrowUpRight, Clock, PlayCircle } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";

const previews = [
  {
    tag: "HTML & CSS",
    title: "Mengenal HTML: Fondasi halaman web.",
    desc: "Pahami struktur dokumen, tag semantik, dan cara berpikir saat menulis markup.",
    href: "/materi/html-css/mengenal-html",
    time: "8 menit",
    featured: true,
  },
  {
    tag: "JavaScript",
    title: "Closure & Scope dijelaskan pelan.",
    desc: "Konsep yang sering membingungkan pemula, ditulis dengan analogi sehari-hari.",
    href: "/materi/javascript/function-dan-scope",
    time: "12 menit",
  },
  {
    tag: "React",
    title: "Cara berpikir komponen di React.",
    desc: "Mulai dari memecah UI menjadi bagian kecil yang mudah dikelola.",
    href: "/materi/react-tailwind/pengenalan-react",
    time: "18 menit",
  },
  {
    tag: "Project",
    title: "Struktur project modern dan scalable.",
    desc: "Pelajari folder, konvensi, dan pola yang dipakai developer profesional.",
    href: "/materi/real-project/struktur-project-modern",
    time: "10 menit",
  },
];

export default function MaterialPreview() {
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
            key={p.title}
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
