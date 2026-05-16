import Link from "next/link";
import { Coffee, Heart } from "lucide-react";
import Reveal from "@/components/ui/Reveal";

export default function DonationCTA() {
  return (
    <section className="container-page py-24">
      <Reveal>
        <div className="relative overflow-hidden rounded-3xl border border-border bg-gradient-to-br from-accent/15 via-card to-card p-10 sm:p-14">
          <div className="pointer-events-none absolute -right-24 -top-24 h-64 w-64 rounded-full bg-accent/30 blur-3xl" />
          <div className="pointer-events-none absolute -bottom-24 left-1/3 h-64 w-64 rounded-full bg-accent-hover/20 blur-3xl" />

          <div className="relative flex flex-col items-start gap-8 md:flex-row md:items-center md:justify-between">
            <div className="max-w-xl">
              <span className="section-eyebrow">
                <Heart size={12} />
                Support LearnWithAcel
              </span>
              <h3 className="mt-5 font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl">
                Platform ini gratis. Donasimu membuatnya terus hidup.
              </h3>
              <p className="mt-4 text-[15px] leading-relaxed text-muted">
                Semua materi di sini bisa kamu akses tanpa bayar sepeser pun.
                Kalau kamu merasa terbantu, satu cangkir kopi virtual sangat
                berarti untuk membuat materi baru terus lahir.
              </p>
            </div>

            <div className="flex flex-col gap-3 sm:flex-row md:flex-col">
              <Link href="/donate" className="btn-primary">
                <Coffee size={16} />
                Traktir Acel
              </Link>
              <Link href="/about" className="btn-secondary">
                Tentang platform
              </Link>
            </div>
          </div>
        </div>
      </Reveal>
    </section>
  );
}
