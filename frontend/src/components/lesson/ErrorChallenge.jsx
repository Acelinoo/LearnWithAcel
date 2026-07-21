"use client";

import { useState } from "react";
import {
  Bug,
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  Eye,
  Lightbulb,
  RotateCcw,
} from "lucide-react";

/**
 * Tantangan "Cari Error" — interactive find-the-bug challenge.
 * Shape:
 *  {
 *    title: string,
 *    instruction: string,
 *    buggyCode: string,
 *    hints: string[],
 *    fixedCode: string,
 *    explanation: string,
 *  }
 */
export default function ErrorChallenge({ data }) {
  const [revealedHints, setRevealedHints] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);

  if (!data) return null;

  function revealNextHint() {
    setRevealedHints((prev) => Math.min(prev + 1, data.hints.length));
  }

  function reset() {
    setRevealedHints(0);
    setShowAnswer(false);
  }

  return (
    <div className="relative overflow-hidden rounded-2xl border border-rose-400/25 bg-gradient-to-br from-rose-400/10 via-card to-card p-6 sm:p-8">
      <div className="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-rose-400/10 blur-3xl" />

      <div className="relative">
        {/* Header */}
        <div className="flex items-center gap-2">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-rose-400/30 bg-rose-400/10 text-rose-300">
            <Bug size={14} />
          </span>
          <div>
            <h3 className="font-display text-base font-semibold text-foreground">
              🐛 {data.title}
            </h3>
          </div>
        </div>

        {/* Instruction */}
        <p className="mt-4 text-[15px] leading-relaxed text-foreground/85">
          {data.instruction}
        </p>

        {/* Buggy code */}
        <div className="mt-5">
          <div className="flex items-center justify-between rounded-t-xl border border-b-0 border-white/10 bg-[#0a0a0a] px-4 py-2">
            <span className="font-mono text-[10px] uppercase tracking-wider text-rose-300">
              Kode bermasalah
            </span>
          </div>
          <pre className="overflow-x-auto rounded-b-xl border border-white/10 bg-[#0a0a0a] p-4 font-mono text-sm leading-relaxed text-foreground/85">
            <code>{data.buggyCode}</code>
          </pre>
        </div>

        {/* Hints section */}
        <div className="mt-5 space-y-2">
          {data.hints.map((hint, i) => (
            <div key={i}>
              {i < revealedHints ? (
                <div className="flex gap-3 rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-sm leading-relaxed text-foreground/85">
                  <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-amber-400/30 bg-amber-400/10 font-mono text-[10px] text-amber-300">
                    {i + 1}
                  </span>
                  <span>{hint}</span>
                </div>
              ) : i === revealedHints && !showAnswer ? (
                <button
                  onClick={revealNextHint}
                  className="flex w-full items-center gap-2 rounded-xl border border-dashed border-white/10 px-4 py-3 text-sm text-muted transition-colors hover:border-amber-400/30 hover:text-amber-300"
                >
                  <Lightbulb size={14} />
                  <span>Tampilkan hint {i + 1}</span>
                  <ChevronRight size={14} className="ml-auto" />
                </button>
              ) : null}
            </div>
          ))}
        </div>

        {/* Show answer button */}
        <div className="mt-5 flex flex-wrap items-center gap-3">
          {!showAnswer && (
            <button onClick={() => setShowAnswer(true)} className="btn-primary">
              <Eye size={14} />
              Lihat jawaban
            </button>
          )}
          {(revealedHints > 0 || showAnswer) && (
            <button onClick={reset} className="btn-ghost">
              <RotateCcw size={14} />
              Mulai ulang
            </button>
          )}
        </div>

        {/* Answer section */}
        {showAnswer && (
          <div className="mt-5 space-y-4">
            {/* Fixed code */}
            <div>
              <div className="flex items-center justify-between rounded-t-xl border border-b-0 border-emerald-400/20 bg-[#0a0a0a] px-4 py-2">
                <span className="font-mono text-[10px] uppercase tracking-wider text-emerald-300">
                  Kode yang benar
                </span>
                <span className="inline-flex items-center gap-1 text-[11px] text-muted">
                  <CheckCircle2 size={10} className="text-emerald-300" />
                  diperbaiki
                </span>
              </div>
              <pre className="overflow-x-auto rounded-b-xl border border-emerald-400/20 bg-[#0a0a0a] p-4 font-mono text-sm leading-relaxed text-foreground/85">
                <code>{data.fixedCode}</code>
              </pre>
            </div>

            {/* Explanation */}
            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-5">
              <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
                <CheckCircle2 size={14} className="text-emerald-300" />
                Penjelasan
              </div>
              <p className="mt-3 text-sm leading-relaxed text-foreground/85">
                {data.explanation}
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
