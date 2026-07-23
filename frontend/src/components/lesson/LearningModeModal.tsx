"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Video, BookOpen, Check } from "lucide-react";

const MDiv = motion.div as unknown as React.FC<
  React.HTMLAttributes<HTMLDivElement> & Record<string, unknown>
>;

interface LearningModeModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectMode: (mode: string, remember: boolean) => void;
}

export default function LearningModeModal({ isOpen, onClose, onSelectMode }: LearningModeModalProps) {
  const [remember, setRemember] = useState(true);

  // Prevent scrolling when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "unset";
    }
    return () => {
      document.body.style.overflow = "unset";
    };
  }, [isOpen]);

  const handleSelect = (mode: string) => {
    onSelectMode(mode, remember);
    onClose();
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 px-4 sm:px-6">
          <MDiv
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 bg-background/80 backdrop-blur-sm"
            onClick={onClose}
          />
          
          <MDiv
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            className="relative w-full max-w-2xl overflow-hidden rounded-3xl border border-white/10 bg-card p-6 shadow-2xl sm:p-8"
          >
            <div className="mb-8 text-center">
              <h2 className="font-display text-2xl font-bold tracking-tight text-foreground sm:text-3xl">
                Pilih Mode Belajar Kamu 🚀
              </h2>
              <p className="mt-2 text-muted-foreground">
                Kamu bisa merubah preferensi ini kapan saja di kemudian hari.
              </p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              <button
                onClick={() => handleSelect("video")}
                className="group relative flex flex-col items-center gap-4 rounded-2xl border border-white/5 bg-white/[0.02] p-6 text-center transition-all hover:border-accent/50 hover:bg-accent/5"
              >
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-accent/10 text-accent transition-transform group-hover:scale-110 group-hover:bg-accent/20">
                  <Video size={32} />
                </div>
                <div>
                  <h3 className="font-semibold text-foreground">Mode Video (Interactive Watch)</h3>
                  <p className="mt-2 text-sm text-muted-foreground">
                    Belajar santai lewat penjelasan video visual & audio secara menyeluruh.
                  </p>
                </div>
                <div className="absolute right-4 top-4 opacity-0 transition-opacity group-hover:opacity-100">
                  <span className="flex h-6 w-6 items-center justify-center rounded-full bg-accent/20 text-accent">
                    <Check size={14} />
                  </span>
                </div>
              </button>

              <button
                onClick={() => handleSelect("text")}
                className="group relative flex flex-col items-center gap-4 rounded-2xl border border-white/5 bg-white/[0.02] p-6 text-center transition-all hover:border-emerald-500/50 hover:bg-emerald-500/5"
              >
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-emerald-500/10 text-emerald-400 transition-transform group-hover:scale-110 group-hover:bg-emerald-500/20">
                  <BookOpen size={32} />
                </div>
                <div>
                  <h3 className="font-semibold text-foreground">Mode Modul Teks & Baca</h3>
                  <p className="mt-2 text-sm text-muted-foreground">
                    Belajar mandiri lewat dokumentasi teks, analogi, dan contoh kode yang terstruktur.
                  </p>
                </div>
                <div className="absolute right-4 top-4 opacity-0 transition-opacity group-hover:opacity-100">
                  <span className="flex h-6 w-6 items-center justify-center rounded-full bg-emerald-500/20 text-emerald-400">
                    <Check size={14} />
                  </span>
                </div>
              </button>
            </div>

            <div className="mt-8 flex items-center justify-center gap-2">
              <input
                type="checkbox"
                id="remember"
                checked={remember}
                onChange={(e) => setRemember(e.target.checked)}
                className="h-4 w-4 rounded border-white/10 bg-white/5 text-accent focus:ring-accent focus:ring-offset-background"
              />
              <label htmlFor="remember" className="text-sm text-muted-foreground cursor-pointer select-none">
                Ingat pilihan saya
              </label>
            </div>
          </MDiv>
        </div>
      )}
    </AnimatePresence>
  );
}
