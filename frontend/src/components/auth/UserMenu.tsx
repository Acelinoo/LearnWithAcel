"use client";

import Link from "next/link";
import { AnimatePresence, motion } from "framer-motion";
import { useEffect, useRef, useState } from "react";
import { LayoutDashboard, LogOut, Loader2, User } from "lucide-react";
import { useAuth } from "@/components/providers/AuthProvider";
import { cn } from "@/lib/utils";

// framer-motion 11.x typing workaround
const MDiv = motion.div as unknown as React.FC<
  React.HTMLAttributes<HTMLDivElement> & Record<string, unknown>
>;

function initialsOf(nameOrEmail: string) {
  const base = nameOrEmail.split("@")[0] || nameOrEmail;
  const parts = base.replace(/[._-]+/g, " ").trim().split(/\s+/);
  return (parts[0]?.[0] ?? "") + (parts[1]?.[0] ?? "");
}

export default function UserMenu() {
  const { user, loading, signOut } = useAuth();
  const [open, setOpen] = useState(false);
  const [signingOut, setSigningOut] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onClick(e: MouseEvent) {
      if (!ref.current) return;
      if (!ref.current.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener("mousedown", onClick);
    return () => document.removeEventListener("mousedown", onClick);
  }, []);

  if (loading) {
    return (
      <div className="h-9 w-9 animate-pulse rounded-full border border-border bg-black/30" />
    );
  }

  if (!user) {
    return (
      <div className="hidden items-center gap-2 md:flex">
        <Link href="/login" className="btn-ghost">
          Masuk
        </Link>
        <Link href="/register" className="btn-primary">
          Daftar
        </Link>
      </div>
    );
  }

  const label = user.full_name || user.email || "Akun";
  const initials = initialsOf(label).toUpperCase().slice(0, 2) || "LW";

  return (
    <div ref={ref} className="relative">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className={cn(
          "flex h-9 items-center gap-2 rounded-full border border-border bg-black/30 pl-1 pr-3 text-sm transition-colors",
          "hover:border-border hover:bg-black/40",
          open && "border-accent/40 bg-black/40"
        )}
        aria-haspopup="menu"
        aria-expanded={open}
      >
        <span className="flex h-7 w-7 items-center justify-center rounded-full bg-gradient-to-br from-accent/80 to-accent-hover/60 text-[11px] font-semibold text-white shadow-glow">
          {initials}
        </span>
        <span className="hidden max-w-[140px] truncate text-[13px] text-foreground/90 sm:block">
          {label}
        </span>
      </button>

      <AnimatePresence>
        {open && (
          <MDiv
            initial={{ opacity: 0, y: -6, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -6, scale: 0.98 }}
            transition={{ duration: 0.18, ease: [0.22, 1, 0.36, 1] }}
            className="absolute right-0 top-[calc(100%+8px)] w-60 overflow-hidden rounded-xl border border-border bg-[#151515]/95 shadow-card backdrop-blur-xl"
            role="menu"
          >
            <div className="border-b border-border px-4 py-3">
              <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.14em] text-muted">
                <User size={11} />
                Signed in as
              </div>
              <div className="mt-1 truncate text-[13px] text-foreground">
                {user.email}
              </div>
            </div>

            <div className="p-1.5">
              <Link
                href="/dashboard"
                className="flex items-center gap-2.5 rounded-lg px-3 py-2 text-[13px] text-foreground/90 transition-colors hover:bg-black/40"
                role="menuitem"
                onClick={() => setOpen(false)}
              >
                <LayoutDashboard size={14} className="text-accent-hover" />
                Dashboard
              </Link>
              <button
                type="button"
                role="menuitem"
                onClick={async () => {
                  setSigningOut(true);
                  try {
                    await signOut();
                  } finally {
                    setSigningOut(false);
                    setOpen(false);
                  }
                }}
                className="flex w-full items-center gap-2.5 rounded-lg px-3 py-2 text-left text-[13px] text-foreground/90 transition-colors hover:bg-black/40"
              >
                {signingOut ? (
                  <Loader2 size={14} className="animate-spin text-accent-hover" />
                ) : (
                  <LogOut size={14} className="text-accent-hover" />
                )}
                {signingOut ? "Keluar..." : "Keluar"}
              </button>
            </div>
          </MDiv>
        )}
      </AnimatePresence>
    </div>
  );
}
