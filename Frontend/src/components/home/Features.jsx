import {
  BookOpen,
  Compass,
  Layers,
  LineChart,
  Rocket,
  Sparkles,
} from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";

const features = [
  {
    icon: Compass,
    title: "Roadmap terstruktur",
    desc: "Kamu tahu persis apa yang harus dipelajari berikutnya. Tidak ada lagi bingung mulai dari mana.",
  },
  {
    icon: Layers,
    title: "Level progression",
    desc: "Lima level dari dasar hingga siap kerja. Setiap level punya target dan mini project nyata.",
  },
  {
    icon: BookOpen,
    title: "Materi mudah dipahami",
    desc: "Ditulis dengan bahasa santai untuk pemula. Tanpa istilah membingungkan di awal perjalanan.",
  },
  {
    icon: LineChart,
    title: "Progress belajar",
    desc: "Lacak materi yang sudah kamu selesaikan dan tetap termotivasi lewat dashboard personal.",
  },
  {
    icon: Rocket,
    title: "Fokus project nyata",
    desc: "Belajar sambil membangun. Setiap level diakhiri dengan project yang bisa masuk portfolio.",
  },
  {
    icon: Sparkles,
    title: "Nyaman di mata",
    desc: "Dark mode first, typography bersih, dan animasi halus untuk sesi belajar panjang.",
  },
];

export default function Features() {
  return (
    <section className="container-page py-24">
      <SectionHeading
        eyebrow="Kenapa di sini"
        title="Dirancang untuk kamu yang serius belajar dari nol."
        description="Bukan sekadar kumpulan tutorial. Ini pengalaman belajar yang dikurasi, terarah, dan ramah pemula."
      />

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {features.map((f, i) => (
          <Reveal key={f.title} delay={i * 0.05}>
            <div className="card-base card-hover group relative overflow-hidden p-6">
              <div className="absolute -right-8 -top-8 h-24 w-24 rounded-full bg-accent/10 opacity-0 blur-2xl transition-opacity duration-500 group-hover:opacity-100" />
              <div className="relative">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl border border-border bg-black/30 text-accent-hover">
                  <f.icon size={18} />
                </div>
                <h3 className="mt-5 font-display text-lg font-semibold">
                  {f.title}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-muted">
                  {f.desc}
                </p>
              </div>
            </div>
          </Reveal>
        ))}
      </div>
    </section>
  );
}
