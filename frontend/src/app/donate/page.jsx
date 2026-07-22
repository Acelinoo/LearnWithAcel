import {
  Coffee,
  Copy,
  CreditCard,
  Heart,
  QrCode,
  Sparkles,
} from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import SectionHeading from "@/components/ui/SectionHeading";

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

              {/* QR placeholder */}
              <div className="mt-6 rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                <div className="relative h-56 w-56 rounded-xl bg-[#f5f5f5] p-3">
                  <div className="grid h-full w-full grid-cols-10 grid-rows-10 gap-[2px]">
                    {Array.from({ length: 100 }).map((_, i) => (
                      <div
                        key={i}
                        className="rounded-[1px]"
                        style={{
                          background:
                            (i * 37) % 7 < 3 ? "#0d0d0d" : "transparent",
                        }}
                      />
                    ))}
                  </div>
                  {/* corner markers */}
                  <div className="absolute left-3 top-3 h-10 w-10 rounded-lg border-[6px] border-[#0d0d0d]" />
                  <div className="absolute right-3 top-3 h-10 w-10 rounded-lg border-[6px] border-[#0d0d0d]" />
                  <div className="absolute bottom-3 left-3 h-10 w-10 rounded-lg border-[6px] border-[#0d0d0d]" />
                  {/* center logo */}
                  <div className="absolute left-1/2 top-1/2 flex h-10 w-10 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-lg bg-accent text-white">
                    <Sparkles size={16} />
                  </div>
                </div>
                <div className="mt-3 text-center text-[11px] font-mono uppercase tracking-widest text-black/60">
                  QRIS · Placeholder
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
                className="btn-primary mt-6 w-full"
              >
                <Heart size={16} />
                Donasi sekarang
              </a>
            </div>

      
              {/* <div className="flex items-center gap-2">
                <CreditCard size={16} className="text-accent-hover" />
                <h3 className="font-display text-base font-semibold">
                  Transfer manual
                </h3>
              </div> */}
              {/* <div className="mt-4 divide-y divide-white/5 rounded-xl border border-white/5 bg-white/[0.02]">
                {[
                  { bank: "BCA", no: "1234567890", name: "Acel" },
                  { bank: "DANA", no: "0812-3456-7890", name: "Acel" },
                ].map((b) => (
                  <div
                    key={b.bank}
                    className="flex items-center justify-between gap-3 px-4 py-3"
                  >
                    <div>
                      <div className="text-xs uppercase tracking-wider text-muted">
                        {b.bank}
                      </div>
                      <div className="mt-0.5 font-mono text-sm text-foreground">
                        {b.no}
                      </div>
                      <div className="text-xs text-muted">a/n {b.name}</div>
                    </div>
                    <button
                      className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 text-muted transition-colors hover:border-white/20 hover:text-foreground"
                      aria-label="Copy"
                    >
                      <Copy size={14} />
                    </button>
                  </div>
                ))}
              </div> */}
        

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
