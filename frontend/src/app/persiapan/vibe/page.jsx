import Link from "next/link";
import {
  ArrowRight,
  Bot,
  Brain,
  Clock,
  ExternalLink,
  FolderCheck,
  Laptop,
  Sparkles,
  Wifi,
  Zap,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ReadingProgress from "@/components/lesson/ReadingProgress";
import { getRoadmap } from "@/lib/api/content";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Persiapan Vibe Coding — Siapkan tools AI-mu",
  description:
    "Sebelum mulai vibe coding, install tools AI yang dibutuhkan. Cursor, akun GitHub, Vercel, dan akun AI.",
};

const tools = [
  { name: "Cursor", tag: "AI Code Editor", desc: "VS Code versi AI. Bisa generate, edit, dan debug kode lewat chat. Ini senjata utamamu.", link: "https://cursor.sh", size: "~120 MB", must: true },
  { name: "Google Chrome", tag: "Browser + DevTools", desc: "Untuk melihat hasil app-mu dan debugging. Tekan F12 untuk buka DevTools.", link: "https://www.google.com/chrome", size: "~100 MB", must: true },
  { name: "GitHub Account", tag: "Code hosting", desc: "Tempat menyimpan kode dan deploy otomatis. Gratis. Buat akun di github.com.", link: "https://github.com", size: "Gratis", must: true },
  { name: "Vercel Account", tag: "Deployment", desc: "Publish app ke internet dalam 1 klik. Hubungkan ke GitHub, deploy otomatis tiap push.", link: "https://vercel.com", size: "Gratis", must: true },
  { name: "ChatGPT / Claude", tag: "AI Assistant", desc: "Untuk brainstorm, debugging, dan menulis prompt kompleks. Bisa pakai versi gratis.", link: "https://chat.openai.com", size: "Gratis", must: false },
  { name: "Node.js (LTS)", tag: "Runtime", desc: "Dibutuhkan untuk menjalankan project React/Next.js di lokal. Install versi LTS.", link: "https://nodejs.org", size: "~30 MB", must: true },
];

const mindset = [
  { icon: Zap, title: "Fokus pada hasil", desc: "Kamu belajar untuk membangun, bukan untuk menghafal syntax." },
  { icon: Bot, title: "AI adalah partner", desc: "Bukan cheat. Kamu tetap perlu memahami apa yang AI hasilkan." },
  { icon: Brain, title: "Iterasi cepat", desc: "Generate → review → perbaiki → deploy. Ulangi." },
  { icon: FolderCheck, title: "Satu project per level", desc: "Setiap level diakhiri dengan project nyata yang bisa kamu tunjukkan." },
];

async function getFirstVibeLesson() {
  try {
    const roadmap = await getRoadmap("vibe");
    const firstLevel = roadmap.levels[0];
    const firstLesson = firstLevel?.lessons[0];
    if (firstLevel && firstLesson) {
      return `/materi/vibe/${firstLevel.slug}/${firstLesson.slug}`;
    }
  } catch {
    // backend offline
  }
  return "/roadmap/vibe";
}

export default async function PersiapanVibePage() {
  const firstHref = await getFirstVibeLesson();

  return (
    <>
      <ReadingProgress />
      <section className="container-page pt-12">
        <Reveal>
          <Link href="/onboarding" className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground">
            ← Kembali ke pilih jalur
          </Link>
        </Reveal>
        <Reveal delay={0.05}>
          <div className="mt-8 flex items-center gap-2">
            <span className="section-eyebrow">
              <Bot size={12} /> Vibe Coding — Persiapan
            </span>
            <span className="rounded-full border border-sky-400/30 bg-sky-400/10 px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-[0.12em] text-sky-300">
              AI Assisted
            </span>
          </div>
        </Reveal>
        <Reveal delay={0.1}>
          <h1 className="mt-5 max-w-3xl font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            Siapkan tools AI-mu, lalu kita build bareng.
          </h1>
        </Reveal>
        <Reveal delay={0.15}>
          <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
            Vibe coding butuh tools yang berbeda dari coding tradisional. Semua
            gratis, setup sekitar 15 menit.
          </p>
        </Reveal>

        <Reveal delay={0.2}>
          <div className="mt-8 grid grid-cols-2 gap-3 sm:grid-cols-4">
            {[
              { icon: Laptop, label: "Device", value: "Laptop / PC" },
              { icon: Wifi, label: "Internet", value: "Wajib ada" },
              { icon: Clock, label: "Setup", value: "±15 menit" },
              { icon: Sparkles, label: "Harga", value: "Semua gratis" },
            ].map((s) => (
              <div key={s.label} className="card-base flex items-center gap-3 p-4">
                <div className="flex h-9 w-9 items-center justify-center rounded-lg border border-border bg-black/30 text-accent-hover">
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

      <section className="container-page pt-16">
        <Reveal>
          <span className="section-eyebrow">Step 1</span>
          <h2 className="mt-4 font-display text-3xl font-semibold tracking-tight">Install & buat akun.</h2>
        </Reveal>
        <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {tools.map((t, i) => (
            <Reveal key={t.name} delay={i * 0.04}>
              <div className="card-base card-hover h-full p-5">
                <div className="flex items-center justify-between">
                  <div className="font-mono text-[10px] uppercase tracking-[0.14em] text-accent-hover">{t.tag}</div>
                  <span className={`rounded-full border px-2 py-0.5 text-[10px] font-medium ${t.must ? "border-accent/30 bg-accent/10 text-accent-hover" : "border-border bg-black/30 text-muted"}`}>
                    {t.must ? "Wajib" : "Opsional"}
                  </span>
                </div>
                <h3 className="mt-3 font-display text-base font-semibold">{t.name}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted">{t.desc}</p>
                <div className="mt-4 flex items-center justify-between border-t border-border pt-3">
                  <span className="text-xs text-muted">{t.size}</span>
                  <a href={t.link} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-sm font-medium text-accent-hover hover:text-foreground">
                    Buka <ExternalLink size={12} />
                  </a>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="container-page pt-16">
        <Reveal>
          <span className="section-eyebrow">Step 2</span>
          <h2 className="mt-4 font-display text-3xl font-semibold tracking-tight">Mindset vibe coder.</h2>
        </Reveal>
        <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {mindset.map((m, i) => (
            <Reveal key={m.title} delay={i * 0.05}>
              <div className="card-base card-hover h-full p-5">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl border border-border bg-black/30 text-accent-hover">
                  <m.icon size={16} />
                </div>
                <h3 className="mt-4 font-display text-base font-semibold">{m.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted">{m.desc}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="container-page py-16">
        <Reveal>
          <div className="relative overflow-hidden rounded-3xl border border-border bg-gradient-to-br from-sky-500/15 via-card to-card p-8 sm:p-12">
            <div className="pointer-events-none absolute -right-24 -top-24 h-64 w-64 rounded-full bg-sky-500/30 blur-3xl" />
            <div className="relative flex flex-col items-start gap-8 md:flex-row md:items-center md:justify-between">
              <div className="max-w-xl">
                <span className="section-eyebrow"><Sparkles size={12} />Siap?</span>
                <h3 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
                  Mulai dari level pertama.
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-muted">
                  Kita pahami landscape AI coding dulu, lalu langsung build.
                </p>
              </div>
              <div className="flex flex-col gap-3 sm:flex-row md:flex-col">
                <Link href={firstHref} className="btn-primary">
                  Mulai materi pertama
                  <ArrowRight size={16} />
                </Link>
                <Link href="/roadmap/vibe" className="btn-secondary">
                  Lihat roadmap dulu
                </Link>
              </div>
            </div>
          </div>
        </Reveal>
      </section>
    </>
  );
}
