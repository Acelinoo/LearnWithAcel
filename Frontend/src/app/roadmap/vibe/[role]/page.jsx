import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Bot,
  Clock,
  Compass,
  Layers,
  Sparkles,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import ViewTracker from "@/components/ui/ViewTracker";
import { JALUR_META } from "@/lib/jalur-data";

export const dynamic = "force-dynamic";

const ROLE_DETAILS = {
  "prompt-architect": {
    badge: "AI Prompt",
    title: "AI Prompt Architect",
    tagline: "Sutradara di balik layar AI.",
    intro:
      "Role ini fokus ke kemampuan menyusun prompt yang menghasilkan output konsisten dan relevan. Kamu bakal belajar cara mengarahkan AI untuk menyelesaikan task multi-step yang kompleks tanpa kehilangan konteks.",
    pitch: [
      "Kapan to-the-point, kapan ngasih konteks panjang",
      "Library prompt yang bisa kamu pakai ulang lintas project",
      "Cara debugging hasil AI yang ngarang",
      "Multi-step orchestration biar AI nggak bingung di tengah jalan",
    ],
    levels: [
      {
        number: 1,
        title: "Dasar Prompt yang Konsisten",
        summary:
          "Anatomi prompt, role-setting, dan teknik menjaga AI tetap on-track.",
      },
      {
        number: 2,
        title: "Multi-Step Orchestration",
        summary:
          "Memecah task besar jadi rangkaian prompt yang nyambung dan andal.",
      },
    ],
  },
  "product-curator": {
    badge: "Product & UX",
    title: "Product & UX Curator",
    tagline: "Jaga rasa & arah produk.",
    intro:
      "AI bisa generate puluhan opsi UI dalam menit. Role ini fokus ke kemampuan curating — milih mana yang masuk produk, mana yang dibuang, mana yang harus diiterasi.",
    pitch: [
      "Design taste & critique untuk output AI",
      "User journey mapping sederhana",
      "Polish UI biar nggak terasa AI-generated",
      "Komunikasi sama developer & stakeholder",
    ],
    levels: [
      {
        number: 1,
        title: "Design Taste untuk Builder",
        summary:
          "Spacing, hierarchy, typography — fondasi yang bikin output AI naik kelas.",
      },
      {
        number: 2,
        title: "Curating User Experience",
        summary:
          "Mapping perjalanan user dan ngecek mana flow yang ngebantu, mana yang ngeganggu.",
      },
    ],
  },
  "code-reviewer": {
    badge: "Code Review",
    title: "Code Reviewer & Debugger",
    tagline: "Mata kedua untuk kode AI.",
    intro:
      "Output AI sering kelihatan benar tapi ngarang. Role ini fokus jadi mata kedua yang ngecek hasil AI sebelum dipakai user — dari security, performance, sampai logic correctness.",
    pitch: [
      "Spot common AI bugs yang sering nyangkut di production",
      "Strategi testing untuk kode yang AI bikin",
      "Security review dasar (auth, input validation, secrets)",
      "Performance smell — kode yang jalan tapi pelan",
    ],
    levels: [
      {
        number: 1,
        title: "Spot Common AI Bugs",
        summary:
          "Pola error yang sering muncul di output AI dan cara nangkapnya cepet.",
      },
      {
        number: 2,
        title: "Testing & Security Dasar",
        summary:
          "Strategi nge-test cepet plus security review minimal yang wajib.",
      },
    ],
  },
  "solo-founder": {
    badge: "Indie Hacker",
    title: "Solo Founder / Indie Hacker",
    tagline: "Build, ship, monetize sendirian.",
    intro:
      "Akhir dari jalan vibe coder. Role ini gabungin semua skill plus elemen bisnis: bikin produk yang dipakai user, monetize, sampai jadi revenue stream. Bukan jalan tercepat ke kaya, tapi jalan paling realistis buat solo builder.",
    pitch: [
      "MVP dari ide ke launch dalam hitungan minggu",
      "Marketing dasar yang nggak butuh tim",
      "Stripe, analytics, support tools yang minimal",
      "Mindset operator: tau kapan ship, kapan stop, kapan pivot",
    ],
    levels: [
      {
        number: 1,
        title: "Ide ke MVP yang Live",
        summary:
          "Cara cepat dari konsep ke produk yang bisa dipakai 10 user pertama.",
      },
      {
        number: 2,
        title: "Monetize & Distribusi",
        summary:
          "Pasang Stripe, analytics, dan strategi sederhana buat dapet user pertama.",
      },
    ],
  },
};

export function generateStaticParams() {
  return Object.keys(ROLE_DETAILS).map((role) => ({ role }));
}

export function generateMetadata({ params }) {
  const role = ROLE_DETAILS[params.role];
  if (!role) return { title: "Role tidak ditemukan" };
  return {
    title: `${role.title} · Vibe Coding · LearnWithAcel`,
    description: role.intro,
  };
}

export default function VibeRolePage({ params }) {
  const role = ROLE_DETAILS[params.role];
  if (!role) notFound();

  const otherRoles = JALUR_META.vibe.roles.filter(
    (r) => r.slug !== params.role,
  );

  return (
    <div className="container-page py-16">
      <ViewTracker
        entityType="page"
        entityId={`vibe-role-${params.role}`}
      />

      <Reveal>
        <Link
          href="/jalur/vibe#pilih-role"
          className="inline-flex items-center gap-2 text-sm text-muted transition-colors hover:text-foreground"
        >
          <ArrowLeft size={14} />
          Kembali ke Vibe Fundamentals
        </Link>
      </Reveal>

      {/* Hero */}
      <section className="relative mt-8 overflow-hidden rounded-3xl border border-border bg-card p-8 sm:p-12">
        <div
          aria-hidden
          className="pointer-events-none absolute -right-24 -top-24 h-72 w-72 rounded-full bg-gradient-to-br from-sky-500/25 to-transparent blur-3xl"
        />

        <div className="relative">
          <Reveal delay={0.05}>
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 rounded-full border border-sky-400/30 bg-sky-400/10 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.16em] text-sky-300">
                <Bot size={12} />
                Vibe Coding · {role.badge}
              </span>
              <span className="rounded-full border border-border bg-black/30 px-2.5 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
                Coming soon
              </span>
            </div>
          </Reveal>

          <Reveal delay={0.1}>
            <h1 className="mt-6 max-w-3xl font-display text-4xl font-semibold leading-[1.1] tracking-tight text-balance sm:text-5xl">
              {role.title}
            </h1>
          </Reveal>

          <Reveal delay={0.15}>
            <p className="mt-3 font-mono text-xs text-muted">{role.tagline}</p>
          </Reveal>

          <Reveal delay={0.2}>
            <p className="mt-5 max-w-2xl text-[15px] leading-relaxed text-muted">
              {role.intro}
            </p>
          </Reveal>
        </div>
      </section>

      {/* What you'll learn */}
      <section className="mt-12">
        <Reveal>
          <span className="section-eyebrow">
            <Compass size={12} />
            Yang akan kamu pelajari
          </span>
        </Reveal>

        <Reveal delay={0.05}>
          <h2 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
            Empat fokus utama role ini.
          </h2>
        </Reveal>

        <ul className="mt-6 grid gap-3 md:grid-cols-2">
          {role.pitch.map((p, i) => (
            <Reveal key={p} delay={0.05 + i * 0.04}>
              <li className="card-base flex items-start gap-3 p-4">
                <span className="mt-1 flex h-7 w-7 shrink-0 items-center justify-center rounded-lg border border-sky-400/20 bg-sky-500/[0.06] text-[11px] font-mono text-sky-300">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <span className="text-sm leading-relaxed text-foreground/85">
                  {p}
                </span>
              </li>
            </Reveal>
          ))}
        </ul>
      </section>

      {/* Roadmap preview */}
      <section className="mt-16">
        <Reveal>
          <span className="section-eyebrow">
            <Layers size={12} />
            Roadmap (preview)
          </span>
        </Reveal>

        <Reveal delay={0.05}>
          <h2 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
            Level yang sedang disiapkan.
          </h2>
        </Reveal>

        <Reveal delay={0.1}>
          <p className="mt-3 max-w-2xl text-sm text-muted">
            Konten penuhnya masih dalam proses penulisan. Yang ditampilkan di sini adalah outline awal — judul dan ringkasan tiap level. Kabari kalau ada level yang ingin diprioritaskan.
          </p>
        </Reveal>

        <div className="mt-8 space-y-3">
          {role.levels.map((lvl, i) => (
            <Reveal key={lvl.number} delay={0.1 + i * 0.05}>
              <div className="flex items-start gap-4 rounded-2xl border border-border bg-card p-5 opacity-90">
                <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl border border-sky-400/20 bg-sky-500/[0.06] font-display text-lg font-semibold text-sky-300">
                  0{lvl.number}
                </span>

                <div className="min-w-0 flex-1">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-sky-300">
                      Level 0{lvl.number}
                    </span>
                    <span className="rounded-full border border-border bg-black/30 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-muted">
                      Coming soon
                    </span>
                  </div>
                  <h3 className="mt-2 font-display text-lg font-semibold tracking-tight">
                    {lvl.title}
                  </h3>
                  <p className="mt-1.5 text-sm leading-relaxed text-muted">
                    {lvl.summary}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* What to do meanwhile */}
      <section className="mt-16">
        <Reveal>
          <div className="rounded-3xl border border-border bg-gradient-to-br from-sky-500/10 via-card to-card p-6 sm:p-10">
            <div className="flex items-center gap-2">
              <span className="section-eyebrow">
                <Sparkles size={12} />
                Sambil menunggu
              </span>
            </div>

            <h3 className="mt-4 font-display text-xl font-semibold tracking-tight sm:text-2xl">
              Mulai dari Vibe Coding Fundamentals & roadmap utama.
            </h3>
            <p className="mt-3 max-w-2xl text-sm leading-relaxed text-muted">
              Sebagian besar materi role ini dibangun di atas fondasi vibe coding umum. Selesaikan dulu fundamentals dan roadmap utama biar pas role ini rilis, kamu langsung siap.
            </p>

            <div className="mt-6 flex flex-wrap gap-3">
              <Link href="/jalur/vibe" className="btn-primary">
                <BookOpen size={14} />
                Mulai Vibe Fundamentals
              </Link>
              <Link href="/roadmap/vibe" className="btn-secondary">
                <Clock size={14} />
                Lihat roadmap utama
              </Link>
            </div>
          </div>
        </Reveal>
      </section>

      {/* Other roles */}
      <section className="mt-16">
        <Reveal>
          <h2 className="font-display text-xl font-semibold tracking-tight">
            Atau lihat role lainnya
          </h2>
        </Reveal>

        <div className="mt-5 grid gap-3 md:grid-cols-3">
          {otherRoles.map((r, i) => (
            <Reveal key={r.slug} delay={i * 0.04}>
              <Link
                href={r.href}
                className="group block h-full rounded-xl border border-border bg-card p-4 transition-colors hover:border-sky-400/40"
              >
                <div className="font-mono text-[10px] uppercase tracking-[0.14em] text-sky-300">
                  {r.badge}
                </div>
                <div className="mt-2 font-display text-sm font-semibold text-foreground">
                  {r.title}
                </div>
                <div className="mt-1 line-clamp-2 text-xs text-muted">
                  {r.tagline}
                </div>
                <div className="mt-3 inline-flex items-center gap-1 text-xs text-muted group-hover:text-foreground">
                  Buka <ArrowRight size={11} />
                </div>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
