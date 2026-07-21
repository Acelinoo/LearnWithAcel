"use client";

/**
 * Table of contents with scroll-spy.
 *
 * Mounts an IntersectionObserver against every heading whose id we
 * received via `headings`. Whichever heading is closest to the top of
 * the viewport becomes the active item.
 *
 * The component intentionally has no Suspense boundary or loading
 * state — headings are computed during server render and passed in as
 * a prop, so the first paint is correct.
 */

import { useEffect, useState } from "react";
import { List } from "lucide-react";
import type { HeadingItem } from "@/lib/markdown";
import { cn } from "@/lib/utils";

type Props = {
  headings: HeadingItem[];
};

export default function LessonTOC({ headings }: Props) {
  const [activeId, setActiveId] = useState<string | null>(
    headings[0]?.id ?? null,
  );

  useEffect(() => {
    if (typeof window === "undefined" || headings.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        // Find the entry that is currently most "in view" near the top.
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort(
            (a, b) =>
              a.boundingClientRect.top - b.boundingClientRect.top,
          );
        if (visible.length > 0) {
          setActiveId(visible[0].target.id);
        }
      },
      {
        // Anchor the spy zone to the top quarter of the viewport.
        rootMargin: "-15% 0px -65% 0px",
        threshold: [0, 1],
      },
    );

    headings.forEach((h) => {
      const el = document.getElementById(h.id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, [headings]);

  if (headings.length === 0) return null;

  return (
    <nav aria-label="Daftar bagian" className="text-sm">
      <div className="flex items-center gap-2 px-2 text-[11px] font-semibold uppercase tracking-[0.18em] text-muted/70">
        <List size={12} />
        Daftar isi
      </div>
      <ul className="mt-3 space-y-0.5">
        {headings.map((h) => (
          <li key={h.id}>
            <a
              href={`#${h.id}`}
              className={cn(
                "group block rounded-lg border-l-2 px-3 py-1.5 text-[13px] leading-snug transition-all duration-200",
                h.level === 3 && "ml-3 text-[12.5px]",
                activeId === h.id
                  ? "border-accent bg-accent/[0.06] text-foreground"
                  : "border-transparent text-muted hover:border-border hover:bg-black/40 hover:text-foreground",
              )}
            >
              {h.text}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
