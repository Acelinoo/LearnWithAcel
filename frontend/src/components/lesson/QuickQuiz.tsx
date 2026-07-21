"use client";

import { useState } from "react";
import { CheckCircle2, HelpCircle, XCircle } from "lucide-react";
import { cn } from "@/lib/utils";

type Props = {
  children: React.ReactNode;
  initiallyCompleted: boolean;
};

// Pertanyaan kuis dummy sederhana. Idealnya diambil dari database.
const DUMMY_QUIZ = {
  question: "Apa fungsi utama dari materi yang baru saja dipelajari?",
  options: [
    { id: "a", text: "Untuk menghias tampilan agar cantik", correct: false },
    { id: "b", text: "Untuk memahami struktur dan logika yang tepat", correct: true },
    { id: "c", text: "Untuk menghapus isi database", correct: false },
  ]
};

export default function QuickQuiz({ children, initiallyCompleted }: Props) {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [isCorrect, setIsCorrect] = useState<boolean>(initiallyCompleted);

  if (initiallyCompleted) {
    return <>{children}</>;
  }

  if (isCorrect) {
    return (
      <div className="flex flex-col items-end gap-4">
        <div className="text-sm font-medium text-emerald-400 flex items-center gap-2">
          <CheckCircle2 size={16} />
          Jawaban Benar! Silakan lanjutkan.
        </div>
        {children}
      </div>
    );
  }

  const handleSelect = (id: string, correct: boolean) => {
    setSelectedId(id);
    if (correct) {
      setTimeout(() => setIsCorrect(true), 1000);
    }
  };

  return (
    <div className="rounded-xl border border-border bg-black/20 p-5 backdrop-blur-sm max-w-sm ml-auto">
      <div className="flex items-center gap-2 text-sm font-semibold text-accent-hover mb-3">
        <HelpCircle size={16} />
        Kuis Pemahaman Singkat
      </div>
      <p className="text-sm text-foreground mb-4">{DUMMY_QUIZ.question}</p>
      <div className="space-y-2 mb-4">
        {DUMMY_QUIZ.options.map((opt) => {
          const isSelected = selectedId === opt.id;
          let btnClass = "border-border bg-black/30 hover:border-accent/40 text-muted hover:text-foreground";
          let Icon = null;
          
          if (isSelected) {
            if (opt.correct) {
              btnClass = "border-emerald-400/40 bg-emerald-400/10 text-emerald-300";
              Icon = <CheckCircle2 size={14} className="text-emerald-400" />;
            } else {
              btnClass = "border-rose-400/40 bg-rose-400/10 text-rose-300";
              Icon = <XCircle size={14} className="text-rose-400" />;
            }
          }

          return (
            <button
              key={opt.id}
              disabled={selectedId === opt.id && opt.correct}
              onClick={() => handleSelect(opt.id, opt.correct)}
              className={cn(
                "w-full flex items-center justify-between text-left rounded-lg border p-3 text-xs transition-colors",
                btnClass
              )}
            >
              <span>{opt.text}</span>
              {Icon && <span className="ml-2 flex-shrink-0">{Icon}</span>}
            </button>
          );
        })}
      </div>
    </div>
  );
}
