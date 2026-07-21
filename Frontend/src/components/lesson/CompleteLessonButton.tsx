"use client";

/**
 * Mark-as-complete CTA at the bottom of every lesson.
 *
 * Behaviour:
 *   - Hits POST /progress/complete/{lesson_id}.
 *   - On the first transition incomplete → complete, pops a small
 *     celebration banner (XP earned + streak) for ~5s.
 *   - Emits a global progress event so the lesson sidebar, dashboard
 *     widgets, and "continue learning" card can apply optimistic
 *     updates instantly.
 *   - On 401 (stale token / user gone), wipes the local session and
 *     redirects to /login. This was the source of the "User not found"
 *     error users saw after the database was rebuilt.
 *   - Calls router.refresh() at the end so server components re-fetch
 *     the canonical state.
 */

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Flame, Loader2, Sparkles } from "lucide-react";
import { completeLesson } from "@/lib/api/progress";
import { ApiError } from "@/lib/api/client";
import { useAuth } from "@/components/providers/AuthProvider";
import { friendlyAuthError } from "@/lib/auth/errors";
import { emitProgressUpdate } from "@/lib/progress-events";
import { cn } from "@/lib/utils";

type Props = {
  lessonId: string;
  levelId?: string;
  initiallyCompleted?: boolean;
  nextHref?: string;
};

type Celebration = {
  xp: number;
  streak: number;
};

export default function CompleteLessonButton({
  lessonId,
  levelId,
  initiallyCompleted = false,
  nextHref,
}: Props) {
  const router = useRouter();
  const { token, user, signOut } = useAuth();
  const [done, setDone] = useState(initiallyCompleted);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [celebration, setCelebration] = useState<Celebration | null>(null);

  async function handleClick() {
    if (loading || done) return;
    if (!token) {
      router.push("/login?redirectTo=" + encodeURIComponent(window.location.pathname));
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const result = await completeLesson(lessonId, token);
      setDone(true);

      // Broadcast so sidebars, dashboard, and continue-learning can
      // update instantly without waiting for router.refresh().
      emitProgressUpdate({
        lessonId,
        levelId,
        justCompleted: result.just_completed ?? false,
        xpEarned: result.xp_earned ?? 0,
        newTotalXp: result.new_total_xp ?? 0,
        streak: result.streak ?? 0,
      });

      if (result.just_completed && (result.xp_earned ?? 0) > 0) {
        setCelebration({
          xp: result.xp_earned ?? 0,
          streak: result.streak ?? 0,
        });
        window.setTimeout(() => setCelebration(null), 5000);
        
        if (nextHref) {
          window.setTimeout(() => {
            router.push(nextHref);
          }, 1500);
        } else {
          router.refresh();
        }
      } else {
        if (nextHref) {
          router.push(nextHref);
        } else {
          // Server components (lesson page, dashboard) re-fetch.
          router.refresh();
        }
      }
    } catch (e) {
      // 401 = token invalid OR user account no longer exists in the DB
      // (this happens after a wipe + reseed). Force a fresh session.
      if (e instanceof ApiError && e.status === 401) {
        await signOut();
        return;
      }

      const msg =
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal menyimpan progress.";
      setError(friendlyAuthError(msg));
    } finally {
      setLoading(false);
    }
  }

  if (!user) {
    return (
      <button
        type="button"
        onClick={() => router.push("/login")}
        className="btn-secondary"
      >
        Masuk untuk simpan progress
      </button>
    );
  }

  return (
    <div className="flex flex-col items-end gap-3">
      <button
        type="button"
        onClick={handleClick}
        disabled={loading || done}
        className={cn(
          "inline-flex items-center justify-center gap-2 rounded-full px-5 py-2.5 text-sm font-medium transition-all",
          done
            ? "border border-emerald-400/30 bg-emerald-400/[0.08] text-emerald-300"
            : "bg-accent text-white shadow-glow hover:bg-accent-hover hover:shadow-glow-lg active:scale-[0.98]",
          (loading || done) && "cursor-default",
        )}
      >
        {loading ? (
          <>
            <Loader2 size={15} className="animate-spin" />
            Menyimpan...
          </>
        ) : done ? (
          <>
            <CheckCircle2 size={15} />
            Sudah selesai
          </>
        ) : (
          <>
            <CheckCircle2 size={15} />
            Tandai selesai
          </>
        )}
      </button>

      {celebration && (
        <button
          type="button"
          onClick={() => setCelebration(null)}
          className="group flex animate-fade-up items-center gap-3 rounded-xl border border-emerald-400/25 bg-emerald-400/[0.08] px-4 py-2.5 text-left text-sm text-emerald-100 transition-all hover:border-emerald-400/40 hover:bg-emerald-400/[0.12]"
        >
          <Sparkles size={14} className="text-emerald-300" />
          <span>
            <span className="font-semibold tabular-nums">+{celebration.xp} XP</span>
            <span className="text-emerald-200/70"> diraih</span>
            {celebration.streak > 1 && (
              <span className="ml-2 inline-flex items-center gap-1 text-emerald-200/80">
                <Flame size={12} />
                {celebration.streak} hari beruntun
              </span>
            )}
          </span>
        </button>
      )}

      {error && <p className="text-xs text-rose-300">{error}</p>}
    </div>
  );
}
