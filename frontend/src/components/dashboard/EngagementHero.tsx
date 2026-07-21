"use client";

/**
 * Three-card strip on the dashboard showing Total XP, daily streak,
 * and longest streak.
 *
 * Initial values come from the server (so SSR is correct), but the
 * component listens to the global progress bus and applies optimistic
 * bumps the moment the user completes a lesson — no full reload.
 */

import { useEffect, useState } from "react";
import { Award, Flame, TrendingUp } from "lucide-react";
import { onProgressUpdate } from "@/lib/progress-events";
import { formatNumber } from "@/lib/utils";

type Props = {
  initialXp: number;
  initialStreak: number;
  initialLongestStreak: number;
};

export default function EngagementHero({
  initialXp,
  initialStreak,
  initialLongestStreak,
}: Props) {
  const [xp, setXp] = useState(initialXp);
  const [streak, setStreak] = useState(initialStreak);
  const [longest, setLongest] = useState(initialLongestStreak);

  // Sync with server-side updates when re-rendering (router.refresh).
  useEffect(() => {
    setXp(initialXp);
    setStreak(initialStreak);
    setLongest(initialLongestStreak);
  }, [initialXp, initialStreak, initialLongestStreak]);

  // Optimistic bumps from CompleteLessonButton.
  useEffect(() => {
    return onProgressUpdate((u) => {
      if (!u.justCompleted) return;
      if (u.newTotalXp > 0) setXp(u.newTotalXp);
      if (u.streak > 0) {
        setStreak(u.streak);
        setLongest((l) => Math.max(l, u.streak));
      }
    });
  }, []);

  return (
    <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
      <Card
        icon={<Award size={12} className="text-amber-300" />}
        label="Total XP"
        value={formatNumber(xp)}
        hint="Selesaikan lesson untuk dapat XP."
      />
      <Card
        icon={<Flame size={12} className="text-rose-300" />}
        label="Streak harian"
        value={
          <>
            {streak}
            <span className="ml-1.5 text-base font-normal text-muted">
              hari
            </span>
          </>
        }
        hint={
          streak > 0
            ? "Pertahankan momentum, lanjut hari ini."
            : "Belajar 1 lesson hari ini untuk mulai streak."
        }
      />
      <Card
        icon={<TrendingUp size={12} className="text-emerald-300" />}
        label="Streak terlama"
        value={
          <>
            {longest}
            <span className="ml-1.5 text-base font-normal text-muted">
              hari
            </span>
          </>
        }
        hint="Rekor pribadi kamu sejauh ini."
        wide
      />
    </div>
  );
}

function Card({
  icon,
  label,
  value,
  hint,
  wide = false,
}: {
  icon: React.ReactNode;
  label: string;
  value: React.ReactNode;
  hint: string;
  wide?: boolean;
}) {
  return (
    <div
      className={
        "rounded-2xl border border-border bg-black/30 p-5 transition-all duration-300 " +
        (wide ? "sm:col-span-2 lg:col-span-1" : "")
      }
    >
      <div className="flex items-center gap-2 text-[11px] font-semibold uppercase tracking-[0.18em] text-muted/70">
        {icon}
        {label}
      </div>
      <div className="mt-3 font-display text-3xl font-semibold tabular-nums text-foreground">
        {value}
      </div>
      <p className="mt-1 text-xs text-muted">{hint}</p>
    </div>
  );
}
