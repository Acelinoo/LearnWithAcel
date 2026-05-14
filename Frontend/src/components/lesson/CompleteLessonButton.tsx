"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Loader2 } from "lucide-react";
import { completeLesson } from "@/lib/api/progress";
import { ApiError } from "@/lib/api/client";
import { useAuth } from "@/components/providers/AuthProvider";
import { friendlyAuthError } from "@/lib/auth/errors";
import { cn } from "@/lib/utils";

type Props = {
  lessonId: string;
  initiallyCompleted?: boolean;
};

export default function CompleteLessonButton({
  lessonId,
  initiallyCompleted = false,
}: Props) {
  const router = useRouter();
  const { token, user } = useAuth();
  const [done, setDone] = useState(initiallyCompleted);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleClick() {
    if (loading || done) return;
    if (!token) {
      router.push("/login");
      return;
    }
    setLoading(true);
    setError(null);
    try {
      await completeLesson(lessonId, token);
      setDone(true);
      router.refresh();
    } catch (e) {
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
    <div className="flex flex-col gap-2">
      <button
        type="button"
        onClick={handleClick}
        disabled={loading || done}
        className={cn(
          "inline-flex items-center justify-center gap-2 rounded-full px-5 py-2.5 text-sm font-medium transition-all",
          done
            ? "border border-emerald-400/40 bg-emerald-400/10 text-emerald-300"
            : "bg-accent text-white shadow-glow hover:bg-accent-hover hover:shadow-glow-lg active:scale-[0.98]",
          (loading || done) && "cursor-default"
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
      {error && <p className="text-xs text-rose-300">{error}</p>}
    </div>
  );
}
