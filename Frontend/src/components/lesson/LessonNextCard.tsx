/**
 * Bottom-of-page card linking to the next lesson in the level.
 */

import Link from "next/link";
import { ArrowRight, Clock } from "lucide-react";

type Props = {
  href: string;
  title: string;
  duration?: string;
  tone?: "accent" | "sky";
};

const TONE_HOVER = {
  accent: "hover:border-accent/40",
  sky: "hover:border-sky-400/40",
} as const;

const TONE_TEXT = {
  accent: "group-hover:text-accent-hover",
  sky: "group-hover:text-sky-300",
} as const;

export default function LessonNextCard({
  href,
  title,
  duration,
  tone = "accent",
}: Props) {
  return (
    <Link
      href={href}
      className={`group flex items-center justify-between gap-4 rounded-xl border border-border bg-black/30 p-5 transition-all duration-300 ${TONE_HOVER[tone]}`}
    >
      <div>
        <div className="flex items-center gap-2 text-xs uppercase tracking-[0.18em] text-muted/80">
          <span>Materi berikutnya</span>
          {duration && (
            <span className="inline-flex items-center gap-1 text-[11px] normal-case tracking-normal">
              <Clock size={11} />
              {duration}
            </span>
          )}
        </div>
        <div className="mt-2 font-display text-base font-semibold text-foreground sm:text-lg">
          {title}
        </div>
      </div>
      <span
        className={`flex h-10 w-10 items-center justify-center rounded-full border border-border bg-black/40 text-muted transition-all duration-300 group-hover:translate-x-0.5 ${TONE_TEXT[tone]}`}
      >
        <ArrowRight size={16} />
      </span>
    </Link>
  );
}
