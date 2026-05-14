"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, Map, Sparkles } from "lucide-react";
import ViewerBadge from "@/components/ui/ViewerBadge";

export default function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute left-1/2 top-0 h-[600px] w-[900px] -translate-x-1/2 rounded-full bg-accent/20 blur-[120px]" />
      </div>

      <div className="container-page relative pb-24 pt-20 sm:pt-28">
        <div className="mx-auto flex max-w-3xl flex-col items-center text-center">
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="flex flex-wrap items-center justify-center gap-2"
          >
            <span className="section-eyebrow">
              <Sparkles size={12} />
              Platform belajar Web Developer.
            </span>
            <ViewerBadge />
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.05 }}
            className="mt-6 font-display text-4xl font-semibold leading-[1.1] tracking-tight text-balance sm:text-6xl"
          >
            Belajar Web Development{" "}
            <span className="shimmer-text">Dari Nol GRATIS.</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.15 }}
            className="mt-5 max-w-xl text-[15px] leading-relaxed text-muted sm:text-base"
          >
            From Beginner to Real Developer. Roadmap terstruktur, materi mudah
            dipahami, dan praktek langsung di VS Code supaya kamu tidak hanya
            membaca, tapi juga mencoba.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.25 }}
            className="mt-9 flex flex-col items-center gap-3 sm:flex-row"
          >
            <Link href="/pilih-jalur" className="btn-primary">
              Mulai Belajar
              <ArrowRight size={16} />
            </Link>
            <Link href="/roadmap" className="btn-secondary">
              <Map size={16} />
              Lihat Roadmap
            </Link>
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.5 }}
            className="mt-14 flex flex-wrap items-center justify-center gap-x-8 gap-y-3 text-xs text-muted"
          >
            <div>
              <span className="font-mono text-foreground">100%</span> gratis
              untuk semua
            </div>
            <div className="hidden h-1 w-1 rounded-full bg-white/20 sm:block" />
            <div>
              <span className="font-mono text-foreground">70+</span> materi
              terkurasi
            </div>
            <div className="hidden h-1 w-1 rounded-full bg-white/20 sm:block" />
            <div>
              <span className="font-mono text-foreground">5</span> level
              progression
            </div>
          </motion.div>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.9, delay: 0.35 }}
          className="relative mx-auto mt-20 max-w-5xl"
        >
          <div className="rounded-2xl border border-white/10 bg-gradient-to-b from-white/[0.04] to-transparent p-1.5 shadow-glow-lg">
            <div className="overflow-hidden rounded-xl border border-white/5 bg-card">
              <div className="flex items-center gap-1.5 border-b border-white/5 px-4 py-2.5">
                <span className="h-2.5 w-2.5 rounded-full bg-white/10" />
                <span className="h-2.5 w-2.5 rounded-full bg-white/10" />
                <span className="h-2.5 w-2.5 rounded-full bg-white/10" />
                <span className="ml-3 font-mono text-[11px] text-muted">
                  learnwithacel.dev/roadmap
                </span>
              </div>
              <div className="grid grid-cols-1 divide-y divide-white/5 md:grid-cols-3 md:divide-x md:divide-y-0">
                {[
                  { n: "01", t: "HTML & CSS", d: "Fondasi halaman web" },
                  { n: "02", t: "JavaScript", d: "Menghidupkan halaman" },
                  { n: "03", t: "React & Tailwind", d: "UI modern scalable" },
                ].map((x) => (
                  <div key={x.n} className="p-6">
                    <div className="font-mono text-[11px] text-accent-hover">
                      LEVEL {x.n}
                    </div>
                    <div className="mt-2 font-display text-lg font-semibold">
                      {x.t}
                    </div>
                    <div className="mt-1 text-sm text-muted">{x.d}</div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
