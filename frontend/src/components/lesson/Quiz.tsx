"use client";

/**
 * Interactive quiz block.
 *
 *   - User picks an answer → instant feedback (correct / wrong + explanation).
 *   - Wrong answers can be retried, the picked option is locked out so the
 *     user has to consider another one.
 *   - Next question unlocks once the current one is answered correctly.
 *   - A small progress bar at the top reflects how many have been cleared.
 *
 * The component is intentionally state-only (no API calls). Persistence
 * to the backend is part of a future task; the seed lesson markdown is
 * still the source of truth for question text and answers.
 */

import { useMemo, useState, useEffect } from "react";
import {
  Check,
  CircleHelp,
  RotateCcw,
  Sparkles,
  X,
} from "lucide-react";
import type { QuizQuestion } from "@/lib/markdown/extract";
import { renderInline } from "@/lib/markdown/inline";
import { emitQuizCompleted } from "@/lib/progress-events";
import { cn } from "@/lib/utils";

type Props = {
  questions: QuizQuestion[];
};

type AnswerState = {
  pickedIndex: number;
  correct: boolean;
};

export default function Quiz({ questions }: Props) {
  // Index of the currently-active question. We only render one at a time
  // for focus, but already-cleared ones stay rendered above (collapsed
  // to a compact summary).
  const [activeIdx, setActiveIdx] = useState(0);

  // Per-question history. Once a question is answered correctly, it's
  // marked done. Wrong attempts disable the picked option but keep the
  // question active.
  const [answers, setAnswers] = useState<Record<number, AnswerState[]>>({});

  const totalCleared = useMemo(() => {
    return Object.values(answers).filter((arr) =>
      arr.some((a) => a.correct),
    ).length;
  }, [answers]);

  function attempt(qIdx: number, optionIdx: number) {
    const q = questions[qIdx];
    const isCorrect = optionIdx === q.correctIndex;
    setAnswers((prev) => {
      const list = prev[qIdx] ?? [];
      // Don't double-record the same option if the user clicks it twice.
      if (list.some((a) => a.pickedIndex === optionIdx)) return prev;
      return {
        ...prev,
        [qIdx]: [...list, { pickedIndex: optionIdx, correct: isCorrect }],
      };
    });

    if (isCorrect) {
      // Auto-advance after a short pause so the explanation has time to
      // render and animate in.
      setTimeout(() => {
        setActiveIdx((curr) => Math.min(curr + 1, questions.length));
      }, 1200);
    }
  }

  function reset(qIdx: number) {
    setAnswers((prev) => {
      const next = { ...prev };
      delete next[qIdx];
      return next;
    });
  }

  const allDone = questions.length > 0 && totalCleared === questions.length;
  const progressPct = questions.length > 0 ? (totalCleared / questions.length) * 100 : 0;

  useEffect(() => {
    if (allDone) {
      emitQuizCompleted();
    }
  }, [allDone]);

  if (questions.length === 0) return null;

  return (
    <div className="space-y-5">
      {/* Progress strip */}
      <div className="flex items-center gap-3 text-[12px] text-muted">
        <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-black/50">
          <div
            className="h-full rounded-full bg-gradient-to-r from-sky-400 to-sky-300 transition-all duration-500 ease-out"
            style={{ width: `${progressPct}%` }}
          />
        </div>
        <span className="font-mono tabular-nums text-foreground/70">
          {totalCleared}/{questions.length}
        </span>
      </div>

      {/* Cleared questions summary */}
      {Object.keys(answers).map((key) => {
        const idx = Number(key);
        const list = answers[idx] ?? [];
        if (idx === activeIdx) return null;
        const isCleared = list.some((a) => a.correct);
        if (!isCleared) return null;
        const q = questions[idx];
        return (
          <div
            key={`done-${idx}`}
            className="rounded-2xl border border-emerald-400/20 bg-emerald-400/[0.04] px-4 py-3 text-sm"
          >
            <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.14em] text-emerald-300/80">
              <Check size={11} />
              Soal {q.number}
            </div>
            <p className="mt-1 line-clamp-1 text-foreground/80">
              {q.question}
            </p>
          </div>
        );
      })}

      {/* Active question or completed banner */}
      {!allDone ? (
        <ActiveQuestion
          question={questions[activeIdx]}
          attempts={answers[activeIdx] ?? []}
          onAttempt={(optIdx) => attempt(activeIdx, optIdx)}
          onReset={() => reset(activeIdx)}
        />
      ) : (
        <div className="rounded-2xl border border-emerald-400/30 bg-emerald-400/[0.06] p-6 text-center">
          <div className="inline-flex h-10 w-10 items-center justify-center rounded-full border border-emerald-400/30 bg-emerald-400/10 text-emerald-300">
            <Sparkles size={18} />
          </div>
          <h3 className="mt-3 font-display text-lg font-semibold text-foreground">
            Mantap. Semua soal kelar.
          </h3>
          <p className="mt-1.5 text-sm text-muted">
            Lanjut baca bagian berikutnya, atau gulir ke bawah untuk lanjut ke materi selanjutnya.
          </p>
        </div>
      )}
    </div>
  );
}

/* ------------------------------------------------------------------ */
/* Active question                                                      */
/* ------------------------------------------------------------------ */

const LETTERS = ["A", "B", "C", "D"];

function ActiveQuestion({
  question,
  attempts,
  onAttempt,
  onReset,
}: {
  question: QuizQuestion;
  attempts: AnswerState[];
  onAttempt: (idx: number) => void;
  onReset: () => void;
}) {
  const lastAttempt = attempts[attempts.length - 1];
  const cleared = attempts.some((a) => a.correct);
  const wrongIndices = attempts
    .filter((a) => !a.correct)
    .map((a) => a.pickedIndex);

  return (
    <div
      key={question.number}
      className="animate-fade-up rounded-xl border border-border bg-black/30 p-5 sm:p-6"
    >
      <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.14em] text-muted/80">
        <CircleHelp size={11} />
        Soal {question.number}
      </div>

      <p className="mt-3 text-base leading-relaxed text-foreground">
        {renderInline(question.question)}
      </p>

      <ul className="mt-5 space-y-2">
        {question.options.map((opt, optIdx) => {
          const isPicked = lastAttempt?.pickedIndex === optIdx;
          const isCorrectAndPicked = isPicked && lastAttempt?.correct;
          const isWrongAndPicked = isPicked && !lastAttempt?.correct;
          const wasWrongBefore = wrongIndices.includes(optIdx);
          const disabled = cleared || wasWrongBefore;

          return (
            <li key={optIdx}>
              <button
                type="button"
                onClick={() => onAttempt(optIdx)}
                disabled={disabled}
                aria-pressed={isPicked}
                className={cn(
                  "group flex w-full items-center gap-3 rounded-xl border px-4 py-3 text-left transition-all duration-200",
                  // baseline
                  "border-border bg-black/30 text-foreground/90",
                  // hover only when interactive
                  !disabled && "hover:border-border-strong hover:bg-black/40",
                  // wrong attempt history (locked out)
                  wasWrongBefore &&
                    !isCorrectAndPicked &&
                    "border-rose-400/20 bg-rose-500/[0.04] text-foreground/40 line-through",
                  // active wrong (just clicked)
                  isWrongAndPicked &&
                    "animate-shake border-rose-400/40 bg-rose-500/[0.08] text-foreground",
                  // correct
                  isCorrectAndPicked &&
                    "border-emerald-400/40 bg-emerald-400/[0.08] text-foreground",
                )}
              >
                <span
                  aria-hidden
                  className={cn(
                    "flex h-7 w-7 shrink-0 items-center justify-center rounded-lg border font-mono text-[11px] font-semibold transition-colors",
                    "border-border bg-black/40 text-muted",
                    !disabled && "group-hover:border-border-strong group-hover:text-foreground",
                    wasWrongBefore && "border-rose-400/30 bg-rose-500/[0.08] text-rose-200",
                    isCorrectAndPicked &&
                      "border-emerald-400/40 bg-emerald-400/[0.12] text-emerald-300",
                  )}
                >
                  {isCorrectAndPicked ? (
                    <Check size={13} />
                  ) : wasWrongBefore ? (
                    <X size={13} />
                  ) : (
                    LETTERS[optIdx]
                  )}
                </span>

                <span className="flex-1 text-[14px] leading-relaxed">
                  {renderInline(opt)}
                </span>
              </button>
            </li>
          );
        })}
      </ul>

      {/* Feedback panel */}
      {lastAttempt && (
        <div
          className={cn(
            "mt-5 animate-fade-up rounded-xl border px-4 py-3 text-sm",
            lastAttempt.correct
              ? "border-emerald-400/25 bg-emerald-400/[0.06] text-emerald-100/90"
              : "border-rose-400/25 bg-rose-500/[0.05] text-rose-100/90",
          )}
        >
          <div className="flex items-center gap-2 font-medium">
            {lastAttempt.correct ? (
              <>
                <Check size={14} className="text-emerald-300" />
                Benar — lanjut ke soal berikutnya.
              </>
            ) : (
              <>
                <X size={14} className="text-rose-300" />
                Belum tepat. Coba lagi.
              </>
            )}
          </div>
          <p className="mt-1.5 leading-relaxed text-foreground/80">
            {renderInline(question.explanation)}
          </p>
        </div>
      )}

      {!cleared && attempts.length > 0 && (
        <div className="mt-4 flex justify-end">
          <button
            type="button"
            onClick={onReset}
            className="inline-flex items-center gap-1.5 rounded-full border border-border bg-black/30 px-3 py-1.5 text-xs font-medium text-muted transition-colors hover:border-border-strong hover:text-foreground"
          >
            <RotateCcw size={11} />
            Reset jawaban
          </button>
        </div>
      )}
    </div>
  );
}
