"use client";

import { Trophy, Target, ListChecks, Lightbulb, ChevronDown } from "lucide-react";
import { useState } from "react";
import CompleteLessonButton from "./CompleteLessonButton";
import { Markdown as MarkdownRenderer } from "@/lib/markdown";
import type { ApiLessonDetail } from "@/lib/api/content";
import { cn } from "@/lib/utils";

type Props = {
  lesson: ApiLessonDetail;
};

export default function PracticalLabRenderer({ lesson }: Props) {
  const [hintOpen, setHintOpen] = useState(false);

  // Extract the project name from the title
  // Example: "Mini Project: Aplikasi To-Do List" -> "Aplikasi To-Do List"
  const cleanTitle = lesson.title.replace(/^(Mini Project(\s*& Studi Kasus)?|Proyek Akhir|Praktik):?\s*/i, "");

  return (
    <div className="space-y-10 pb-16">
      {/* Header */}
      <div className="relative overflow-hidden rounded-2xl border border-accent/20 bg-gradient-to-br from-accent/10 via-card to-card p-6 sm:p-8">
        <div className="absolute -right-4 -top-4 opacity-10">
          <Trophy size={120} />
        </div>
        <div className="relative z-10">
          <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-accent/30 bg-accent/10 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-accent-hover">
            <Trophy size={14} />
            Practical Lab
          </div>
          <h1 className="font-display text-3xl font-bold tracking-tight sm:text-4xl">
            {cleanTitle}
          </h1>
          <p className="mt-4 max-w-2xl text-lg leading-relaxed text-muted">
            Saatnya menguji pemahamanmu! Terapkan semua yang telah kamu pelajari di level ini ke dalam proyek nyata.
          </p>
        </div>
      </div>

      {/* 🎯 Tujuan Project */}
      <section className="scroll-mt-24" id="tujuan">
        <div className="mb-4 flex items-center gap-2 border-b border-white/10 pb-2">
          <Target className="text-emerald-400" size={24} />
          <h2 className="font-display text-2xl font-semibold">Tujuan Project</h2>
        </div>
        <p className="text-[17px] leading-relaxed text-foreground/90">
          {lesson.summary}
        </p>
      </section>

      {/* 📋 Instruksi & Kriteria */}
      <section className="scroll-mt-24" id="instruksi">
        <div className="mb-4 flex items-center gap-2 border-b border-white/10 pb-2">
          <ListChecks className="text-amber-400" size={24} />
          <h2 className="font-display text-2xl font-semibold">Instruksi & Kriteria</h2>
        </div>
        <div className="prose prose-invert max-w-none prose-headings:font-display prose-a:text-accent-hover mb-6">
          <MarkdownRenderer source={lesson.content.replace(/^#\s+.*$/m, '')} />
        </div>

        {lesson.criteria && lesson.criteria.length > 0 && (
          <div className="mt-8 rounded-xl border border-white/10 bg-white/5 p-5 sm:p-6">
            <h3 className="mb-4 font-display text-lg font-semibold text-foreground">
              Checklist Kriteria Kelulusan:
            </h3>
            <div className="space-y-3">
              {(typeof lesson.criteria === "string" ? JSON.parse(lesson.criteria) : lesson.criteria).map((criterion: string, i: number) => (
                <label
                  key={i}
                  className="flex cursor-pointer items-start gap-3 rounded-lg border border-transparent p-2 transition-colors hover:bg-white/5"
                >
                  <div className="relative mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded border border-white/20 bg-black/20 text-emerald-400">
                    <input
                      type="checkbox"
                      className="peer absolute h-full w-full cursor-pointer opacity-0"
                    />
                    <div className="pointer-events-none absolute hidden peer-checked:block">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="3"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-3.5 w-3.5"
                      >
                        <polyline points="20 6 9 17 4 12"></polyline>
                      </svg>
                    </div>
                  </div>
                  <span className="text-sm leading-relaxed text-foreground/80 peer-checked:text-muted peer-checked:line-through">
                    <MarkdownRenderer source={criterion} />
                  </span>
                </label>
              ))}
            </div>
          </div>
        )}
      </section>

      {/* 💡 Interactive Hint */}
      {lesson.hints && (
        <section className="scroll-mt-24" id="hint">
          <button
            onClick={() => setHintOpen(!hintOpen)}
            className="group flex w-full items-center justify-between rounded-xl border border-white/10 bg-white/[0.02] p-4 text-left transition-colors hover:bg-white/[0.04]"
          >
            <div className="flex items-center gap-3">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-sky-500/20 text-sky-400">
                <Lightbulb size={20} />
              </div>
              <div>
                <div className="font-display text-lg font-semibold text-foreground">
                  Membutuhkan Bantuan?
                </div>
                <div className="text-sm text-muted">
                  Lihat panduan step-by-step 💡
                </div>
              </div>
            </div>
            <ChevronDown
              size={20}
              className={cn(
                "text-muted transition-transform duration-300",
                hintOpen ? "rotate-180" : ""
              )}
            />
          </button>
          
          {hintOpen && (
            <div className="mt-2 rounded-xl border border-white/5 bg-black/20 p-5 animate-in slide-in-from-top-2 fade-in duration-300">
              <p className="mb-4 text-sm text-muted">
                <strong>Tips Pengerjaan:</strong> Cobalah kerjakan sendiri terlebih dahulu. Jangan ragu untuk mencari referensi di Google atau dokumentasi resmi.
              </p>
              <div className="prose prose-invert max-w-none text-sm opacity-80">
                <MarkdownRenderer source={lesson.hints} />
              </div>
            </div>
          )}
        </section>
      )}

      {/* 🎁 Reward Completion */}
      <section className="mt-12 rounded-2xl border border-emerald-500/20 bg-gradient-to-br from-emerald-500/10 via-card to-card p-6 text-center sm:p-10">
        <div className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-emerald-500/20 text-emerald-400 shadow-[0_0_30px_rgba(16,185,129,0.3)]">
          <Trophy size={40} />
        </div>
        <h2 className="mb-2 font-display text-2xl font-bold">Project Selesai?</h2>
        <p className="mb-8 text-muted">
          Klaim <strong className="text-emerald-400">+150 XP</strong> dan simpan progress belajarmu ke profil.
        </p>
        
        <div className="flex justify-center">
          <CompleteLessonButton 
            lessonId={lesson.id} 
            levelId={lesson.level_id}
          />
        </div>
      </section>
    </div>
  );
}
