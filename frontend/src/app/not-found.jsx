import Link from "next/link";
import { ArrowLeft, Compass } from "lucide-react";

export default function NotFound() {
  return (
    <div className="container-page py-24">
      <div className="mx-auto flex max-w-md flex-col items-center text-center">
        <div className="flex h-16 w-16 items-center justify-center rounded-2xl border border-border bg-black/30 text-accent-hover">
          <Compass size={22} />
        </div>
        <div className="mt-6 font-mono text-xs uppercase tracking-[0.16em] text-accent-hover">
          404
        </div>
        <h1 className="mt-3 font-display text-4xl font-semibold tracking-tight text-balance">
          Halaman tidak ditemukan.
        </h1>
        <p className="mt-4 text-[15px] leading-relaxed text-muted">
          Mungkin kamu tersesat di lorong yang salah. Kembali ke roadmap saja,
          itu jalur teramannya.
        </p>
        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Link href="/" className="btn-primary">
            <ArrowLeft size={16} />
            Kembali ke beranda
          </Link>
          <Link href="/roadmap" className="btn-secondary">
            Lihat roadmap
          </Link>
        </div>
      </div>
    </div>
  );
}
