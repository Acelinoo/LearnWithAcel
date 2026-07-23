import Link from "next/link";
import { Github, Instagram, Twitter, Sparkles, Heart } from "lucide-react";

const columns = [
  {
    title: "Platform",
    links: [
      { label: "Roadmap", href: "/roadmap" },
      { label: "Materi", href: "/roadmap" },
      { label: "Dashboard", href: "/dashboard" },
    ],
  },
  {
    title: "Creator",
    links: [
      { label: "About", href: "/about" },
      { label: "Portfolio", href: "https://acelino.vercel.app" },
      { label: "Kontak", href: "mailto:marchelinokurniawan321@gmail.com" },
    ],
  },
  {
    title: "Dukungan",
    links: [
      { label: "Donasi", href: "/donate" },
      { label: "FAQ", href: "/about#faq" },
      { label: "Changelog", href: "/about#changelog" },
    ],
  },
];

export default function Footer() {
  return (
    <footer className="mt-32 border-t border-white/5 bg-surface/40">
      <div className="container-page grid gap-10 py-16 md:grid-cols-5">
        <div className="md:col-span-2">
          <div className="flex items-center gap-2 font-display text-lg font-semibold">
            <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-white/10 bg-gradient-to-br from-accent/60 to-accent-hover/40 shadow-glow">
              <Sparkles className="h-4 w-4 text-white" />
            </span>
            Learn<span className="text-accent-hover">With</span>Acel
          </div>
          <p className="mt-4 max-w-sm text-sm leading-relaxed text-muted">
            Platform belajar web development modern untuk pemula. Dari nol
            sampai siap membuat project nyata.
          </p>
          <div className="mt-6 flex items-center gap-2">
            <a
              href="https://github.com/acelinoo"
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 text-muted transition-colors hover:border-white/20 hover:text-foreground"
              aria-label="GitHub"
            >
              <Github size={16} />
            </a>
            <a
              href="https://instagram.com/acelino"
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-white/10 text-muted transition-colors hover:border-white/20 hover:text-foreground"
              aria-label="Instagram"
            >
              <Instagram size={16} />
            </a>
          </div>
        </div>

        {columns.map((col) => (
          <div key={col.title}>
            <h4 className="mb-4 text-xs font-semibold uppercase tracking-[0.14em] text-muted">
              {col.title}
            </h4>
            <ul className="space-y-2.5 text-sm">
              {col.links.map((link) => (
                <li key={link.label}>
                  <Link
                    href={link.href}
                    className="text-foreground/80 transition-colors hover:text-accent-hover"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="border-t border-white/5">
        <div className="container-page flex flex-col items-center justify-between gap-4 py-6 text-xs text-muted md:flex-row">
          <p>© {new Date().getFullYear()} Learn With Acel. All rights reserved.</p>
          <p className="flex items-center gap-1.5">
            Dibuat dengan <Heart size={12} className="text-accent-hover" /> untuk
            pemula di Indonesia.
          </p>
        </div>
      </div>
    </footer>
  );
}
