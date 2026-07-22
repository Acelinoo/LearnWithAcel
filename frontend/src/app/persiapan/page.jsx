import Link from "next/link";
import {
  ArrowRight,
  Brain,
  Clock,
  ExternalLink,
  FolderCheck,
  Laptop,
  MousePointerClick,
  Sparkles,
  Wifi,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import { getRoadmap } from "@/lib/api/content";
import { getServerUser } from "@/lib/api/server";
import { rolePreparationData, defaultPreparationData } from "@/data/rolePreparationData";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Persiapan — Siapkan alat sebelum mulai belajar",
  description:
    "Sebelum mulai belajar, ada beberapa alat yang perlu kamu siapkan dulu. Ringan, gratis, dan cepat dipasang.",
};

const mindset = [
  { icon: Clock, title: "Sisihkan waktu rutin", desc: "30 menit sehari setiap hari lebih ampuh daripada 5 jam seminggu sekali." },
  { icon: MousePointerClick, title: "Ketik ulang, jangan copy", desc: "Otak belajar dari gerakan jari. Copy-paste membuat ingatan tidak menempel." },
  { icon: Brain, title: "Ramah dengan error", desc: "Error bukan musuh. Baca pesannya pelan-pelan, biasanya sudah kasih petunjuk." },
  { icon: FolderCheck, title: "Simpan semua di satu folder", desc: "Buat folder khusus di komputermu, isi semua project latihan kamu di situ." },
];

async function getFirstLessonHref() {
  try {
    const roadmap = await getRoadmap("frontend"); // Fallback
    const firstLevel = roadmap.levels[0];
    const firstLesson = firstLevel?.lessons[0];
    if (firstLevel && firstLesson) {
      return `/materi/${firstLevel.slug}/${firstLesson.slug}`;
    }
  } catch {
    // backend down — fall back to roadmap page
  }
  return "/roadmap";
}

export default async function PersiapanPage() {
  const user = await getServerUser().catch(() => null);
  const roleSlug = user?.selected_role || "frontend-developer";
  
  const roleData = rolePreparationData[roleSlug] || defaultPreparationData;
  const essentials = roleData.essentials;
  const vscodeExtensions = roleData.extensions;

  const firstLessonHref = await getFirstLessonHref();

  return (
    <div>
      <section className="container-page pt-12">
        <Reveal>
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
          >
            ← Kembali ke beranda
          </Link>
        </Reveal>
        <Reveal delay={0.05}>
          <span className="section-eyebrow mt-8 inline-flex">
            <Sparkles size={12} />
            Jalur: {roleData.title}
          </span>
        </Reveal>
        <Reveal delay={0.1}>
          <h1 className="mt-5 max-w-3xl font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            Siapkan alatnya dulu, belajarnya sambil praktik ya.
          </h1>
        </Reveal>
        <Reveal delay={0.15}>
          <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
            {roleData.description} Tenang, semuanya gratis dan mudah. Sediakan waktu sekitar 15 menit
            untuk install semua, lalu kamu siap masuk ke materi pertama.
          </p>
        </Reveal>

        <Reveal delay={0.2}>
          <div className="mt-8 grid grid-cols-2 gap-3 sm:grid-cols-4">
            {[
              { icon: Laptop, label: "Perangkat", value: "Windows / Mac / Linux" },
              { icon: Wifi, label: "Koneksi internet", value: "Untuk download alat" },
              { icon: Clock, label: "Estimasi setup", value: "±15 menit" },
              { icon: FolderCheck, label: "Harga", value: "Semua gratis" },
            ].map((s) => (
              <div key={s.label} className="card-base flex items-center gap-3 p-4">
                <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-accent-hover">
                  <s.icon size={16} />
                </div>
                <div>
                  <div className="text-[11px] uppercase tracking-wider text-muted">{s.label}</div>
                  <div className="text-sm font-medium text-foreground">{s.value}</div>
                </div>
              </div>
            ))}
          </div>
        </Reveal>
      </section>

      <section className="container-page pt-20">
        <Reveal>
          <span className="section-eyebrow">Step 1</span>
          <h2 className="mt-4 font-display text-3xl font-semibold tracking-tight">
            Install aplikasi wajib.
          </h2>
        </Reveal>

        <div className="mt-10 grid gap-4 md:grid-cols-2">
          {essentials.map((item, i) => {
            const Icon = item.icon;
            return (
              <Reveal key={item.name} delay={i * 0.05}>
                <div className="card-base card-hover group relative h-full overflow-hidden p-6 sm:p-7">
                  <div className={`pointer-events-none absolute -right-12 -top-12 h-32 w-32 rounded-full bg-gradient-to-br ${item.tone} opacity-70 blur-3xl`} />
                  <div className="relative flex flex-col gap-5 h-full">
                    <div className="flex items-start justify-between gap-3">
                      <div className="flex items-center gap-3">
                        <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-white/10 bg-white/[0.03] text-accent-hover">
                          <Icon size={18} />
                        </div>
                        <div>
                          <div className="font-mono text-[10px] uppercase tracking-[0.14em] text-accent-hover">
                            {item.tag}
                          </div>
                          <h3 className="font-display text-lg font-semibold">{item.name}</h3>
                        </div>
                      </div>
                      <span className={"shrink-0 rounded-full border px-2.5 py-0.5 text-[10px] font-medium " + (item.must ? "border-accent/30 bg-accent/10 text-accent-hover" : "border-white/10 bg-white/[0.03] text-muted")}>
                        {item.must ? "Wajib" : "Opsional"}
                      </span>
                    </div>
                    <p className="text-sm leading-relaxed text-foreground/80">{item.desc}</p>
                    <div className="mt-auto flex flex-wrap items-center justify-between gap-3 border-t border-white/5 pt-4">
                      <span className="text-xs text-muted">Ukuran: {item.size}</span>
                      {item.link ? (
                        <a href={item.link} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm font-medium text-accent-hover transition-colors hover:text-foreground">
                          Download <ExternalLink size={14} />
                        </a>
                      ) : null}
                    </div>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>
      </section>

      <section className="container-page pt-20">
        <Reveal>
          <span className="section-eyebrow">Step 2</span>
          <h2 className="mt-4 font-display text-3xl font-semibold tracking-tight">
            Ekstensi / Tools tambahan.
          </h2>
        </Reveal>
        <div className="mt-10 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {vscodeExtensions.map((ext, i) => (
            <Reveal key={ext.name} delay={i * 0.04}>
              <div className="card-base h-full p-5">
                <div className="flex items-center gap-2">
                  <span className="flex h-7 w-7 items-center justify-center rounded-md border border-accent/25 bg-accent/10 text-[10px] font-mono text-accent-hover">
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <h3 className="font-display text-sm font-semibold">{ext.name}</h3>
                </div>
                <p className="mt-3 text-sm leading-relaxed text-muted">{ext.desc}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="container-page pt-20">
        <Reveal>
          <span className="section-eyebrow">Step 3</span>
          <h2 className="mt-4 font-display text-3xl font-semibold tracking-tight">
            Siapkan juga kepalanya.
          </h2>
        </Reveal>
        <div className="mt-10 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {mindset.map((m, i) => (
            <Reveal key={m.title} delay={i * 0.05}>
              <div className="card-base card-hover h-full p-5">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl border border-white/10 bg-white/[0.03] text-accent-hover">
                  <m.icon size={16} />
                </div>
                <h3 className="mt-4 font-display text-base font-semibold">{m.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted">{m.desc}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="container-page py-20">
        <Reveal>
          <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-gradient-to-br from-accent/15 via-card to-card p-8 sm:p-12">
            <div className="pointer-events-none absolute -right-24 -top-24 h-64 w-64 rounded-full bg-accent/30 blur-3xl" />
            <div className="pointer-events-none absolute -bottom-24 left-1/3 h-64 w-64 rounded-full bg-accent-hover/20 blur-3xl" />
            <div className="relative flex flex-col items-start gap-8 md:flex-row md:items-center md:justify-between">
              <div className="max-w-xl">
                <span className="section-eyebrow">
                  <Sparkles size={12} /> Alat sudah siap?
                </span>
                <h3 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
                  Waktunya masuk ke materi pertama.
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-muted">
                  Kamu udah milih jalur {roleData.title}. Mulai pelan-pelan dari materi pertama.
                </p>
              </div>
              <div className="flex flex-col gap-3 sm:flex-row md:flex-col">
                <Link href="/dashboard" className="btn-primary">
                  Saya Sudah Siap!
                  <ArrowRight size={16} />
                </Link>
                <Link href={firstLessonHref} className="btn-secondary">
                  Langsung Baca Materi
                </Link>
              </div>
            </div>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
