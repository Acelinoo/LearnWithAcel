import { Sparkles } from "lucide-react";

export default function Loading() {
  return (
    <div className="flex min-h-[60vh] items-center justify-center">
      <div className="flex flex-col items-center gap-4">
        <div className="relative flex h-14 w-14 items-center justify-center rounded-2xl border border-border bg-card shadow-glow">
          <Sparkles size={20} className="text-accent-hover" />
          <span className="absolute inset-0 animate-ping rounded-2xl border border-accent/40" />
        </div>
        <div className="flex items-center gap-2 text-sm text-muted">
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-accent" />
          Menyiapkan materi...
        </div>
      </div>
    </div>
  );
}
