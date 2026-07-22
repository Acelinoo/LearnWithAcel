"use client";

import { useEffect, useState } from "react";

export default function ReadingProgress({ lessonId }) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Scroll restore on mount
    if (lessonId) {
      const saved = localStorage.getItem(`lesson_scroll_${lessonId}`);
      if (saved) {
        window.scrollTo({ top: parseInt(saved, 10), behavior: "smooth" });
      }
    }

    const onScroll = () => {
      const scrollTop = window.scrollY;
      const docHeight =
        document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      setProgress(Math.min(100, Math.max(0, pct)));
      
      if (lessonId) {
        localStorage.setItem(`lesson_scroll_${lessonId}`, scrollTop.toString());
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [lessonId]);

  return (
    <div className="fixed inset-x-0 top-0 z-[60] h-0.5 bg-transparent">
      <div
        className="h-full bg-gradient-to-r from-accent to-accent-hover transition-all duration-150"
        style={{ width: `${progress}%` }}
      />
    </div>
  );
}
