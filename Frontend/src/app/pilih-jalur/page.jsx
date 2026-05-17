"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import {
  ArrowRight,
  Bot,
  Brain,
  CheckCircle2,
  Code2,
  Cpu,
  Layers,
  Rocket,
  Sparkles,
  Zap,
} from "lucide-react";
import ViewTracker from "@/components/ui/ViewTracker";

const paths = [
  {
    id: "vibe",
    href: "/jalur/vibe",
    icon: Bot,
    badge: "AI Assisted",
    badgeColor: "border-sky-400/30 bg-sky-400/10 text-sky-300",
    title: "Vibe Coding",
    tagline: "Build faster with AI.",
    subtitle:
      "Belajar membuat aplikasi modern menggunakan AI workflow tanpa harus menjadi computer scientist.",
    benefits: [
      "Lebih cepat membuat project",
      "Cocok untuk orang awam",
      "Fokus praktik nyata",
      "Belajar AI workflow modern",
      "Bisa launch app lebih cepat",
      "Tetap memahami dasar engineering",
    ],
    accent: "from-sky-500/20 via-sky-300/10 to-transparent",
    border: "hover:border-sky-400/40",
    glow: "group-hover:shadow-[0_0_60px_-15px_rgba(139,92,246,0.4)]",
    cta: "Mulai Vibe Coding",
  },
  {
    id: "manual",
    href: "/jalur/manual",
    icon: Code2,
    badge: "Fundamental Path",
    badgeColor: "border-cyan-400/30 bg-cyan-400/10 text-cyan-300",
    title: "Manual Coding",
    tagline: "Understand the fundamentals deeply.",
    subtitle:
      "Belajar coding dari dasar dengan memahami bagaimana web bekerja secara nyata.",
    benefits: [
      "Fundamental lebih kuat",
      "Memahami logic programming",
      "Lebih fleksibel",
      "Cocok untuk karir engineer jangka panjang",
      "Memahami debugging lebih dalam",
      "Memahami struktur aplikasi modern",
    ],
    accent: "from-cyan-400/20 via-blue-500/10 to-transparent",
    border: "hover:border-cyan-400/40",
    glow: "group-hover:shadow-[0_0_60px_-15px_rgba(34,211,238,0.3)]",
    cta: "Mulai Manual Coding",
  },
];

const comparison = [
  { aspect: "Kecepatan build", vibe: "Sangat cepat", manual: "Bertahap" },
  { aspect: "Bantuan AI", vibe: "Utama", manual: "Pelengkap" },
  { aspect: "Pemahaman fundamental", vibe: "Cukup", manual: "Sangat dalam" },
  { aspect: "Cocok untuk", vibe: "Builder & non-teknis", manual: "Calon engineer" },
  { aspect: "Fokus utama", vibe: "Workflow modern", manual: "Logic & syntax" },
  { aspect: "Karir jangka panjang", vibe: "Startup / freelance", manual: "Engineer / senior dev" },
];

export default function PilihJalurPage() {
  return (
    <div className="container-page py-16">
      <ViewTracker entityType="page" entityId="pilih-jalur" />
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="mx-auto max-w-2xl text-center"
      >
        <span className="section-eyebrow">
          <Sparkles size={12} />
          Pilih jalur belajarmu
        </span>
        <h1 className="mt-5 font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
          Mau belajar dengan cara apa?
        </h1>
        <p className="mt-4 text-[15px] leading-relaxed text-muted">
          Dua jalur, satu tujuan: bisa membangun aplikasi nyata. Pilih yang
          paling cocok dengan gaya belajarmu. Kamu bisa pindah jalur kapan saja.
        </p>
      </motion.div>

      {/* Cards */}
      <div className="mx-auto mt-14 grid max-w-5xl gap-6 lg:grid-cols-2">
        {paths.map((p, i) => (
          <motion.div
            key={p.id}
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.1 + i * 0.1 }}
          >
            <Link
              href={p.href}
              className={`group relative flex h-full flex-col overflow-hidden rounded-3xl border border-border bg-card p-8 transition-all duration-500 sm:p-10 ${p.border} ${p.glow}`}
            >
              {/* Gradient bg */}
              <div
                className={`pointer-events-none absolute inset-0 bg-gradient-to-br ${p.accent} opacity-0 transition-opacity duration-500 group-hover:opacity-100`}
              />
              {/* Glow orb */}
              <div className="pointer-events-none absolute -right-20 -top-20 h-48 w-48 rounded-full bg-gradient-to-br from-white/[0.03] to-transparent blur-3xl transition-opacity duration-500 group-hover:opacity-100 opacity-0" />

              <div className="relative flex flex-1 flex-col">
                {/* Icon + badge */}
                <div className="flex items-center justify-between">
                  <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-border bg-black/30">
                    <p.icon size={22} className="text-foreground" />
                  </div>
                  <span
                    className={`rounded-full border px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.12em] ${p.badgeColor}`}
                  >
                    {p.badge}
                  </span>
                </div>

                {/* Title */}
                <h2 className="mt-6 font-display text-3xl font-semibold tracking-tight">
                  {p.title}
                </h2>
                <p className="mt-1 font-mono text-xs text-accent-hover">
                  {p.tagline}
                </p>
                <p className="mt-4 text-[15px] leading-relaxed text-muted">
                  {p.subtitle}
                </p>

                {/* Benefits */}
                <ul className="mt-6 flex-1 space-y-2.5">
                  {p.benefits.map((b) => (
                    <li
                      key={b}
                      className="flex items-start gap-2.5 text-sm text-foreground/85"
                    >
                      <CheckCircle2
                        size={14}
                        className="mt-0.5 shrink-0 text-accent-hover"
                      />
                      {b}
                    </li>
                  ))}
                </ul>

                {/* CTA */}
                <div className="mt-8">
                  <span className="btn-primary">
                    {p.cta}
                    <ArrowRight size={16} />
                  </span>
                </div>
              </div>
            </Link>
          </motion.div>
        ))}
      </div>

      {/* Comparison */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
        className="mx-auto mt-24 max-w-4xl"
      >
        <div className="text-center">
          <span className="section-eyebrow">
            <Layers size={12} />
            Masih bingung memilih?
          </span>
          <h2 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-3xl">
            Perbandingan kedua jalur.
          </h2>
        </div>

        <div className="mt-10 overflow-hidden rounded-2xl border border-border">
          {/* Header */}
          <div className="grid grid-cols-3 border-b border-border bg-black/30">
            <div className="px-5 py-4 text-xs font-semibold uppercase tracking-[0.12em] text-muted">
              Aspek
            </div>
            <div className="flex items-center gap-2 border-l border-border px-5 py-4 text-xs font-semibold uppercase tracking-[0.12em] text-sky-300">
              <Bot size={12} />
              Vibe Coding
            </div>
            <div className="flex items-center gap-2 border-l border-border px-5 py-4 text-xs font-semibold uppercase tracking-[0.12em] text-cyan-300">
              <Code2 size={12} />
              Manual Coding
            </div>
          </div>
          {/* Rows */}
          {comparison.map((row, i) => (
            <div
              key={row.aspect}
              className={`grid grid-cols-3 ${
                i < comparison.length - 1 ? "border-b border-border" : ""
              }`}
            >
              <div className="px-5 py-4 text-sm font-medium text-foreground">
                {row.aspect}
              </div>
              <div className="border-l border-border px-5 py-4 text-sm text-muted">
                {row.vibe}
              </div>
              <div className="border-l border-border px-5 py-4 text-sm text-muted">
                {row.manual}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-8 text-center text-sm text-muted">
          Kedua jalur bisa saling melengkapi. Banyak developer profesional
          menggunakan keduanya.
        </div>
      </motion.div>
    </div>
  );
}
