import Image from "next/image";
import {
  Coffee,
  Heart,
  QrCode,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";

export const metadata = {
  title: "Support — Traktir Acel secangkir kopi",
  description:
    "Platform ini gratis. Donasimu membuatnya terus hidup dan melahirkan materi baru.",
};

export default function DonatePage() {
  return (
    <div className="container-page py-16">
      <div className="mx-auto max-w-2xl text-center">
        <Reveal>
          <span className="section-eyebrow">
            <Heart size={12} />
            Support LearnWithAcel
          </span>
        </Reveal>
        <Reveal delay={0.05}>
          <h1 className="mt-5 font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            Platform ini gratis.
            <br />
            <span className="text-muted">Tapi kalo mau ngasih secangkir kopi virtual.</span>
          </h1>
        </Reveal>
        <Reveal delay={0.1}>
          <p className="mt-5 text-[15px] leading-relaxed text-muted">
            Sangat membantu aku meluangkan waktu untuk menulis
            materi baru dan merawat platform ini.
          </p>
        </Reveal>
      </div>

      <div className="mx-auto mt-14 grid max-w-4xl gap-6 lg:grid-cols-[1.05fr_1fr]">
        {/* QRIS Card */}
        <Reveal>
          <div className="card-base relative overflow-hidden p-8">
            <div className="pointer-events-none absolute -right-20 -top-20 h-60 w-60 rounded-full bg-accent/20 blur-3xl" />
            <div className="relative flex flex-col items-center text-center">
              <div className="flex items-center gap-2">
                <span className="section-eyebrow">
                  <QrCode size={12} />
                  QRIS
                </span>
              </div>
              <h3 className="mt-4 font-display text-xl font-semibold">
                Scan untuk donasi
              </h3>
              <p className="mt-2 max-w-sm text-sm text-muted">
                Buka aplikasi bank atau e-wallet apa pun, lalu scan kode di
                bawah. Nominalnya bebas.
              </p>

              {/* QRIS Image */}
              <div className="mt-6 flex flex-col items-center rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                <div className="relative h-60 w-60 overflow-hidden rounded-xl bg-white p-2 shadow-card">
                  <Image
                    src="/images/qris.png"
                    alt="QRIS Donasi LearnWithAcel"
                    width={240}
                    height={240}
                    className="h-full w-full object-contain"
                  />
                </div>
                <div className="mt-3 text-center font-mono text-[11px] uppercase tracking-widest text-muted">
                  QRIS • LearnWithAcel
                </div>
              </div>

              <div className="mt-6 text-xs text-muted">
                Merchant: <span className="text-foreground">LearnWithAcel</span>
              </div>
            </div>
          </div>
        </Reveal>

        {/* Alternatives */}
        <Reveal delay={0.1}>
          <div className="flex h-full flex-col gap-6">
            <div className="card-base p-6">
              <div className="flex items-center gap-2">
                <Coffee size={16} className="text-accent-hover" />
                <h3 className="font-display text-base font-semibold">
                  Traktir secangkir kopi
                </h3>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-muted">
                Cara paling santai mendukung platform ini. Nominal tidak harus
                besar, konsistensi lebih berarti.
              </p>
              <div className="mt-5 flex flex-wrap gap-2">
                {["Saweria"].map((v) => (
                  <button
                    key={v}
                    className="rounded-full border border-white/10 bg-white/[0.03] px-4 py-1.5 text-sm text-foreground transition-colors hover:border-accent/40 hover:bg-accent/10"
                  >
                    {v}
                  </button>
                ))}
              </div>
              <a
                href="https://saweria.co/LearnWithAcel"
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary mt-6 w-full"
              >
                <Heart size={16} />
                Donasi sekarang
              </a>
            </div>

            <div className="rounded-2xl border border-accent/20 bg-accent/5 p-5 text-sm leading-relaxed text-foreground/85">
              Semua materi di LearnWithAcel akan tetap gratis. Donasi bukan
              syarat akses, hanya apresiasi.
            </div>
          </div>
        </Reveal>
      </div>
    </div>
  );
}
