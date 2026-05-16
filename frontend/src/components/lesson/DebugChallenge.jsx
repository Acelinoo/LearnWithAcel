"use client";

import { useState } from "react";
import {
  AlertTriangle,
  Bug,
  CheckCircle2,
  Eye,
  EyeOff,
  Lightbulb,
  RotateCcw,
  Sparkles,
} from "lucide-react";

/**
 * Tantangan "Temukan Errornya".
 * Shape:
 *  {
 *    description: string,
 *    errorCount: number,
 *    brokenCode: string,
 *    language?: "html" | "css" | "js" | "jsx",
 *    errors: [{ hint: string, fix: string }],
 *    fixedCode: string,
 *  }
 */
export default function DebugChallenge({ challenge }) {
  const [showHints, setShowHints] = useState(false);
  const [showFix, setShowFix] = useState(false);

  if (!challenge) return null;

  const langLabel =
    challenge.language === "html"
      ? "HTML"
      : challenge.language === "css"
      ? "CSS"
      : challenge.language === "jsx"
      ? "JSX"
      : challenge.language === "js"
      ? "JavaScript"
      : "Code";

  function reset() {
    setShowHints(false);
    setShowFix(false);
  }

  return (
    <div className="relative overflow-hidden rounded-2xl border border-amber-400/25 bg-gradient-to-br from-amber-400/10 via-card to-card p-6 sm:p-8">
      <div className="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-amber-400/10 blur-3xl" />

      <div className="relative">
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-amber-400/30 bg-amber-400/10 text-amber-300">
              <Bug size={14} />
            </span>
            <div>
              <div className="font-mono text-[11px] uppercase tracking-[0.14em] text-amber-300">
                Temukan errornya
              </div>
              <h3 className="font-display text-base font-semibold text-foreground">
                Debug challenge
              </h3>
            </div>
          </div>
          <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/[0.03] px-2.5 py-1 text-[11px] text-muted">
            <AlertTriangle size={11} className="text-amber-300" />
            <span className="font-mono text-foreground">
              {challenge.errorCount}
            </span>
            error
          </span>
        </div>

        {challenge.description && (
          <p className="mt-4 text-[15px] leading-relaxed text-foreground/85">
            {challenge.description}
          </p>
        )}

        {/* Broken code */}
        <div className="mt-5">
          <div className="flex items-center justify-between rounded-t-xl border border-b-0 border-white/10 bg-[#0a0a0a] px-4 py-2">
            <span className="font-mono text-[10px] uppercase tracking-wider text-rose-300">
              {langLabel} — rusak
            </span>
            <span className="inline-flex items-center gap-1 text-[11px] text-muted">
              <AlertTriangle size={10} className="text-rose-300" />
              ada yang salah di sini
            </span>
          </div>
          <pre className="overflow-x-auto rounded-b-xl border border-white/10 bg-[#0a0a0a] p-4 font-mono text-sm leading-relaxed text-foreground/85">
            <code>{challenge.brokenCode}</code>
          </pre>
        </div>

        {/* Controls */}
        <div className="mt-5 flex flex-wrap items-center gap-3">
          {!showHints ? (
            <button
              onClick={() => setShowHints(true)}
              className="btn-secondary"
            >
              <Lightbulb size={14} />
              Tunjukkan hint
            </button>
          ) : (
            !showFix && (
              <button onClick={() => setShowFix(true)} className="btn-primary">
                <Eye size={14} />
                Tunjukkan jawaban
              </button>
            )
          )}
          {(showHints || showFix) && (
            <button onClick={reset} className="btn-ghost">
              <RotateCcw size={14} />
              Mulai ulang
            </button>
          )}
          {!showHints && !showFix && (
            <span className="text-xs text-muted">
              Coba temukan sendiri dulu. Kalau buntu, klik tombol di atas.
            </span>
          )}
        </div>

        {/* Hints */}
        {showHints && (
          <div className="mt-5 rounded-xl border border-white/10 bg-white/[0.03] p-5">
            <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
              <Lightbulb size={14} className="text-amber-300" />
              Hint (tanpa spoiler)
            </div>
            <ol className="mt-3 space-y-2">
              {challenge.errors.map((e, i) => (
                <li
                  key={i}
                  className="flex gap-3 text-sm leading-relaxed text-foreground/85"
                >
                  <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-amber-400/30 bg-amber-400/10 font-mono text-[10px] text-amber-300">
                    {i + 1}
                  </span>
                  <span>{e.hint}</span>
                </li>
              ))}
            </ol>
          </div>
        )}

        {/* Full answer */}
        {showFix && (
          <div className="mt-5 space-y-4">
            <div>
              <div className="flex items-center justify-between rounded-t-xl border border-b-0 border-emerald-400/20 bg-[#0a0a0a] px-4 py-2">
                <span className="font-mono text-[10px] uppercase tracking-wider text-emerald-300">
                  {langLabel} — sudah diperbaiki
                </span>
                <span className="inline-flex items-center gap-1 text-[11px] text-muted">
                  <CheckCircle2 size={10} className="text-emerald-300" />
                  siap dijalankan
                </span>
              </div>
              <pre className="overflow-x-auto rounded-b-xl border border-emerald-400/20 bg-[#0a0a0a] p-4 font-mono text-sm leading-relaxed text-foreground/85">
                <code>{challenge.fixedCode}</code>
              </pre>
            </div>

            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-5">
              <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
                <Sparkles size={14} className="text-accent-hover" />
                Rincian perbaikan
              </div>
              <ol className="mt-3 space-y-2.5">
                {challenge.errors.map((e, i) => (
                  <li
                    key={i}
                    className="flex gap-3 text-sm leading-relaxed text-foreground/85"
                  >
                    <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-emerald-400/30 bg-emerald-400/10 font-mono text-[10px] text-emerald-300">
                      {i + 1}
                    </span>
                    <span>{e.fix}</span>
                  </li>
                ))}
              </ol>
            </div>
          </div>
        )}
      </div>

      {/* Collapse-all helper */}
      {(showHints || showFix) && !showFix && (
        <button
          onClick={() => setShowHints(false)}
          className="relative mt-4 inline-flex items-center gap-1.5 text-xs text-muted transition-colors hover:text-foreground"
        >
          <EyeOff size={12} />
          Sembunyikan hint
        </button>
      )}
    </div>
  );
}
