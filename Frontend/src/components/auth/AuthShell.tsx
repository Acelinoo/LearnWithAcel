"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import { cn } from "@/lib/utils";
import type { ReactNode } from "react";

// framer-motion 11.x typing workaround
const MDiv = motion.div as unknown as React.FC<
  React.HTMLAttributes<HTMLDivElement> & Record<string, unknown>
>;

type Props = {
  title: string;
  subtitle?: string;
  eyebrow?: string;
  footer?: ReactNode;
  children: ReactNode;
  className?: string;
};

export default function AuthShell({
  title,
  subtitle,
  eyebrow = "Authentication",
  footer,
  children,
  className,
}: Props) {
  return (
    <div className="relative flex min-h-[calc(100vh-5rem)] items-center justify-center px-5 py-12 sm:px-8">
      {/* Ambient glow */}
      <div
        aria-hidden
        className="pointer-events-none absolute inset-0 -z-10 overflow-hidden"
      >
        <div className="absolute left-1/2 top-0 h-[420px] w-[820px] -translate-x-1/2 rounded-full bg-accent/15 blur-[120px]" />
        <div className="absolute bottom-0 right-1/4 h-[260px] w-[320px] rounded-full bg-accent/10 blur-[100px]" />
      </div>

      <MDiv
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
        className={cn("w-full max-w-md", className)}
      >
        <div className="mb-6 flex items-center justify-center">
          <Link
            href="/"
            className="group flex items-center gap-2 font-display text-sm font-semibold tracking-tight"
          >
            <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-white/10 bg-gradient-to-br from-accent/60 to-accent-hover/40 shadow-glow">
              <Sparkles className="h-4 w-4 text-white" />
            </span>
            <span className="text-foreground">
              Learn<span className="text-accent-hover">With</span>Acel
            </span>
          </Link>
        </div>

        <div className="glass-panel relative rounded-2xl p-6 shadow-card sm:p-8">
          {/* Subtle top highlight */}
          <div
            aria-hidden
            className="pointer-events-none absolute inset-x-6 top-0 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"
          />

          {eyebrow && (
            <span className="section-eyebrow">
              <Sparkles size={12} />
              {eyebrow}
            </span>
          )}
          <h1 className="mt-4 font-display text-2xl font-semibold tracking-tight sm:text-[26px]">
            {title}
          </h1>
          {subtitle && (
            <p className="mt-2 text-[14.5px] leading-relaxed text-muted">
              {subtitle}
            </p>
          )}

          <div className="mt-7">{children}</div>
        </div>

        {footer && (
          <div className="mt-6 text-center text-sm text-muted">{footer}</div>
        )}
      </MDiv>
    </div>
  );
}
