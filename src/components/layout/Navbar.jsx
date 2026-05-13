"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { Menu, X, Sparkles } from "lucide-react";
import { cn } from "@/lib/utils";

const navItems = [
  { href: "/", label: "Home" },
  { href: "/roadmap", label: "Roadmap" },
  { href: "/dashboard", label: "Dashboard" },
  { href: "/about", label: "About" },
  { href: "/donate", label: "Support" },
];

export default function Navbar() {
  const pathname = usePathname();
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    setOpen(false);
  }, [pathname]);

  return (
    <header
      className={cn(
        "fixed inset-x-0 top-0 z-50 transition-all duration-300",
        scrolled
          ? "border-b border-white/5 bg-background/70 backdrop-blur-xl"
          : "border-b border-transparent"
      )}
    >
      <div className="container-page flex h-16 items-center justify-between">
        <Link
          href="/"
          className="group flex items-center gap-2 font-display text-base font-semibold tracking-tight"
        >
          <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-white/10 bg-gradient-to-br from-accent/60 to-accent-hover/40 shadow-glow">
            <Sparkles className="h-4 w-4 text-white" />
          </span>
          <span className="text-foreground">
            Learn<span className="text-accent-hover">With</span>Acel
          </span>
        </Link>

        <nav className="hidden items-center gap-1 md:flex">
          {navItems.map((item) => {
            const active =
              item.href === "/"
                ? pathname === "/"
                : pathname.startsWith(item.href);
            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "rounded-full px-3.5 py-1.5 text-sm transition-colors",
                  active
                    ? "bg-white/[0.06] text-foreground"
                    : "text-muted hover:text-foreground"
                )}
              >
                {item.label}
              </Link>
            );
          })}
        </nav>

        <div className="hidden md:flex">
          <Link href="/persiapan" className="btn-primary">
            Mulai Belajar
          </Link>
        </div>

        <button
          className="flex h-10 w-10 items-center justify-center rounded-lg border border-white/10 text-muted md:hidden"
          onClick={() => setOpen((v) => !v)}
          aria-label="Toggle menu"
        >
          {open ? <X size={18} /> : <Menu size={18} />}
        </button>
      </div>

      {open && (
        <div className="md:hidden">
          <div className="container-page pb-4">
            <div className="glass-panel rounded-2xl p-2">
              {navItems.map((item) => {
                const active =
                  item.href === "/"
                    ? pathname === "/"
                    : pathname.startsWith(item.href);
                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    className={cn(
                      "block rounded-xl px-4 py-3 text-sm transition-colors",
                      active
                        ? "bg-white/[0.06] text-foreground"
                        : "text-muted hover:bg-white/[0.04] hover:text-foreground"
                    )}
                  >
                    {item.label}
                  </Link>
                );
              })}
              <Link
                href="/persiapan"
                className="btn-primary mt-2 w-full"
              >
                Mulai Belajar
              </Link>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
