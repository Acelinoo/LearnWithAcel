"use client";

import { useMemo, useState } from "react";
import {
  ArrowRight,
  CheckCircle2,
  RotateCcw,
  Sparkles,
  Trophy,
  XCircle,
} from "lucide-react";
import { cn } from "@/lib/utils";

export default function Quiz({ quiz }) {
  // Normalize: accept either a single quiz object or { questions: [...] }
  const questions = useMemo(() => {
    if (!quiz) return [];
    if (Array.isArray(quiz.questions)) return quiz.questions;
    if (Array.isArray(quiz)) return quiz;
    return [quiz];
  }, [quiz]);

  const total = questions.length;
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);
  const [finished, setFinished] = useState(false);

  if (total === 0) return null;

  const current = questions[index];
  const isCorrect = submitted && selected === current.answer;
  const isLast = index === total - 1;

  function handleSubmit() {
    if (!selected || submitted) return;
    const correct = selected === current.answer;
    if (correct) setScore((s) => s + 1);
    setSubmitted(true);
  }

  function handleNext() {
    if (isLast) {
      setFinished(true);
      return;
    }
    setIndex((i) => i + 1);
    setSelected(null);
    setSubmitted(false);
  }

  function handleRestart() {
    setIndex(0);
    setSelected(null);
    setSubmitted(false);
    setScore(0);
    setFinished(false);
  }

  if (finished) {
    const percent = Math.round((score / total) * 100);
    const passed = percent >= 67;
    return (
      <div className="card-base relative overflow-hidden p-6 sm:p-8">
        <div className="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-accent/20 blur-3xl" />
        <div className="relative flex flex-col items-center text-center">
          <div
            className={cn(
              "flex h-14 w-14 items-center justify-center rounded-2xl border",
              passed
                ? "border-emerald-400/30 bg-emerald-400/10 text-emerald-300"
                : "border-accent/30 bg-accent/10 text-accent-hover"
            )}
          >
            <Trophy size={22} />
          </div>
          <div className="mt-5 font-mono text-[11px] uppercase tracking-[0.14em] text-accent-hover">
            Hasil quiz
          </div>
          <div className="mt-2 font-display text-3xl font-semibold">
            {score} dari {total} benar
          </div>
          <div className="mt-2 text-sm text-muted">
            {passed
              ? "Kerja bagus. Kamu siap lanjut ke materi berikutnya."
              : "Jangan patah semangat. Baca ulang materi lalu coba lagi."}
          </div>
          <div className="mt-6">
            <button onClick={handleRestart} className="btn-secondary">
              <RotateCcw size={14} />
              Ulangi quiz
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="card-base p-6 sm:p-8">
      <div className="flex items-center justify-between gap-3">
        <span className="section-eyebrow">
          <Sparkles size={12} />
          Quiz ringan
        </span>
        <span className="font-mono text-xs text-muted">
          Soal{" "}
          <span className="text-foreground">
            {String(index + 1).padStart(2, "0")}
          </span>{" "}
          / {String(total).padStart(2, "0")}
        </span>
      </div>

      {/* Progress */}
      <div className="mt-4 flex gap-1.5">
        {questions.map((_, i) => (
          <div
            key={i}
            className={cn(
              "h-1 flex-1 rounded-full transition-colors",
              i < index
                ? "bg-accent-hover"
                : i === index
                ? "bg-accent"
                : "bg-white/[0.06]"
            )}
          />
        ))}
      </div>

      <h3 className="mt-6 font-display text-xl font-semibold">
        {current.question}
      </h3>

      <div className="mt-5 space-y-2.5">
        {current.options.map((opt) => {
          const active = selected === opt.id;
          const correct = submitted && opt.id === current.answer;
          const wrong = submitted && active && opt.id !== current.answer;
          return (
            <button
              key={opt.id}
              onClick={() => !submitted && setSelected(opt.id)}
              className={cn(
                "flex w-full items-start gap-3 rounded-xl border p-4 text-left text-sm transition-all",
                active && !submitted && "border-accent/50 bg-accent/10",
                !active &&
                  !submitted &&
                  "border-white/5 bg-white/[0.02] hover:border-white/15 hover:bg-white/[0.04]",
                correct && "border-emerald-400/40 bg-emerald-400/10",
                wrong && "border-rose-400/40 bg-rose-400/10"
              )}
            >
              <span
                className={cn(
                  "mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border font-mono text-[10px] uppercase",
                  active && !submitted && "border-accent text-accent-hover",
                  !active && !submitted && "border-white/15 text-muted",
                  correct && "border-emerald-400 text-emerald-300",
                  wrong && "border-rose-400 text-rose-300"
                )}
              >
                {opt.id}
              </span>
              <span className="flex-1 leading-relaxed text-foreground/90">
                {opt.text}
              </span>
              {correct && (
                <CheckCircle2 size={16} className="text-emerald-400" />
              )}
              {wrong && <XCircle size={16} className="text-rose-400" />}
            </button>
          );
        })}
      </div>

      <div className="mt-6 flex flex-wrap items-center gap-3">
        {!submitted ? (
          <button
            onClick={handleSubmit}
            disabled={!selected}
            className="btn-primary disabled:cursor-not-allowed disabled:opacity-50"
          >
            Cek jawaban
          </button>
        ) : (
          <button onClick={handleNext} className="btn-primary">
            {isLast ? "Lihat hasil" : "Soal berikutnya"}
            <ArrowRight size={16} />
          </button>
        )}
        {submitted && (
          <span
            className={cn(
              "text-sm",
              isCorrect ? "text-emerald-300" : "text-rose-300"
            )}
          >
            {isCorrect ? "Tepat sekali." : "Belum tepat."}
          </span>
        )}
      </div>

      {submitted && (
        <div className="mt-4 rounded-xl border border-white/5 bg-white/[0.02] p-4 text-sm leading-relaxed text-foreground/80">
          <span className="font-medium text-foreground">Penjelasan. </span>
          {current.explanation}
        </div>
      )}
    </div>
  );
}
