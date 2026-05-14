"use client";

import { type ComponentType, type ButtonHTMLAttributes } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import {
  ArrowRight,
  Bot,
  CheckCircle2,
  Code2,
  Sparkles,
} from "lucide-react";
import { cn } from "@/lib/utils";

// framer-motion 11.x typing workaround
const MButton = motion.button as unknown as React.FC<
  ButtonHTMLAttributes<HTMLButtonElement> & Record<string, unknown>
>;

type PathOption = {
  id: "vibe" | "manual";
  href: string;
  icon: ComponentType<{ size?: number; className?: string }>;
  badge: string;
  badgeClass: string;
  title: string;
  tagline: string;
  description: string;
  benefits: string[];
};

const options: PathOption[] = [
  {
    id: "vibe",
    href: "/roadmap/vibe",
    icon: Bot,
    badge: "AI Assisted",
    badgeClass: "border-sky-400/30 bg-sky-400/10 text-sky-300",
    title: "Vibe Coding",
    tagline: "Build faster with AI.",
    description:
      "Belajar membangun aplikasi modern menggunakan AI workflow seperti Cursor, ChatGPT, Claude, Lovable, Bolt, dan V0.",
    benefits: [
      "Lebih cepat dapat hasil nyata",
      "Cocok untuk pemula & non-teknis",
      "Fokus prompt, ship, & iterasi",
    ],
  },
  {
    id: "manual",
    href: "/roadmap",
    icon: Code2,
    badge: "Fundamental",
    badgeClass: "border-cyan-400/30 bg-cyan-400/10 text-cyan-300",
    title: "Manual Coding",
    tagline: "Master the fundamentals.",
    description:
      "Belajar web development dari dasar secara tradisional menggunakan HTML, CSS, JavaScript, React, dan Next.js.",
    benefits: [
      "Fundamental kuat & long-term",
      "Logic programming & debugging",
      "Fleksibel untuk stack apa pun",
    ],
  },
];

export default function PathSelection() {
  const router = useRouter();

  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2">
        {options.map((opt, i) => {
          const Icon = opt.icon;

          return (
            <MButton
              key={opt.id}
              type="button"
              initial={{ opacity: 0, y: 18 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{
                duration: 0.55,
                delay: 0.08 + i * 0.1,
                ease: [0.22, 1, 0.36, 1],
              }}
              whileHover={{ y: -4 }}
              whileTap={{ scale: 0.99 }}
              onClick={() => router.push(opt.href)}
              className={cn(
                "group relative flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-white/[0.025] p-6 text-left backdrop-blur-xl transition-colors",
                "hover:border-accent/40 hover:bg-white/[0.04]"
              )}
            >
              <div
                aria-hidden
                className="pointer-events-none absolute -right-20 -top-20 h-44 w-44 rounded-full bg-accent/20 blur-3xl opacity-0 transition-opacity duration-500 group-hover:opacity-100"
              />
              <div
                aria-hidden
                className="pointer-events-none absolute inset-x-6 top-0 h-px bg-gradient-to-r from-transparent via-white/15 to-transparent"
              />

              <div className="relative flex items-center justify-between">
                <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-white/10 bg-white/[0.04] text-foreground transition-colors group-hover:border-accent/40 group-hover:text-accent-hover">
                  <Icon size={19} />
                </div>
                <span
                  className={cn(
                    "rounded-full border px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.12em]",
                    opt.badgeClass
                  )}
                >
                  {opt.badge}
                </span>
              </div>

              <h3 className="relative mt-5 font-display text-xl font-semibold tracking-tight">
                {opt.title}
              </h3>
              <p className="relative mt-1 font-mono text-[11px] text-accent-hover">
                {opt.tagline}
              </p>
              <p className="relative mt-3 text-[13.5px] leading-relaxed text-muted">
                {opt.description}
              </p>

              <ul className="relative mt-5 flex-1 space-y-2">
                {opt.benefits.map((b) => (
                  <li
                    key={b}
                    className="flex items-start gap-2 text-[13px] text-foreground/85"
                  >
                    <CheckCircle2
                      size={13}
                      className="mt-0.5 shrink-0 text-accent-hover"
                    />
                    {b}
                  </li>
                ))}
              </ul>

              <div className="relative mt-6 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.03] px-4 py-2 text-[13px] font-medium transition-colors group-hover:border-accent/40 group-hover:bg-accent/10 group-hover:text-accent-hover">
                Lihat roadmap
                <ArrowRight
                  size={13}
                  className="transition-transform group-hover:translate-x-0.5"
                />
              </div>
            </MButton>
          );
        })}
      </div>

      <p className="flex items-center justify-center gap-1.5 pt-2 text-center text-[12px] text-muted/80">
        <Sparkles size={11} className="text-accent-hover" />
        Tenang, kamu bisa eksplorasi keduanya kapan saja.
      </p>
    </div>
  );
}
