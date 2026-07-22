"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

type Props = {
  nextHref?: string;
  prevHref?: string;
  backHref: string;
};

export default function LessonShortcuts({ nextHref, prevHref, backHref }: Props) {
  const router = useRouter();

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignore if typing in an input
      if (
        document.activeElement?.tagName === "INPUT" ||
        document.activeElement?.tagName === "TEXTAREA"
      ) {
        return;
      }

      if (e.key === "Escape") {
        e.preventDefault();
        router.push(backHref);
      } else if (e.altKey && e.key === "ArrowRight") {
        if (nextHref) {
          e.preventDefault();
          router.push(nextHref);
        }
      } else if (e.altKey && e.key === "ArrowLeft") {
        if (prevHref) {
          e.preventDefault();
          router.push(prevHref);
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [nextHref, prevHref, backHref, router]);

  return null;
}
