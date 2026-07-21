import Link from "next/link";
import { ArrowRight, Github, Globe } from "lucide-react";
import SectionHeading from "@/components/ui/SectionHeading";
import Reveal from "@/components/ui/Reveal";

export default function AboutCreator() {
  return (
    <section className="container-page py-24">
      <SectionHeading
        eyebrow="About creator"
        title="Halo, aku Acel."
        description="Aku membuat LearnWithAcel karena dulu aku juga bingung mau mulai dari mana. Sekarang aku ingin membuat jalan itu lebih jelas untuk kamu."
      />

      <Reveal>
        <div className="card-base overflow-hidden p-8 sm:p-10">
          <div className="grid gap-8 lg:grid-cols-[auto_1fr] lg:items-center">
            <div className="relative">
              <div className="relative h-32 w-32 overflow-hidden rounded-2xl border border-border bg-gradient-to-br from-accent/40 to-accent-hover/20">
                <div className="absolute inset-0 flex items-center justify-center font-display text-5xl font-semibold text-foreground/90">
                  A
                </div>
              </div>
              <div className="absolute -right-2 -top-2 h-3 w-3 rounded-full bg-emerald-400 shadow-[0_0_12px_rgba(52,211,153,0.8)]" />
            </div>

            <div>
              <p className="text-[15px] leading-relaxed text-foreground/85">
                Aku seorang frontend developer yang percaya belajar coding
                harusnya seperti main game, satu level selesai, level berikutnya
                terbuka. Di platform ini aku menuangkan pengalaman, kesalahan,
                dan cara sederhana yang dulu aku harap seseorang ajarkan ke aku.
              </p>

              <div className="mt-6 flex flex-wrap items-center gap-3">
                <Link href="/about" className="btn-primary">
                  Cerita lengkap
                  <ArrowRight size={16} />
                </Link>
                <a
                  href="https://github.com"
                  className="btn-secondary"
                >
                  <Github size={16} />
                  GitHub
                </a>
                <a
                  href="https://example.com"
                  className="btn-secondary"
                >
                  <Globe size={16} />
                  Portfolio
                </a>
              </div>
            </div>
          </div>
        </div>
      </Reveal>
    </section>
  );
}
