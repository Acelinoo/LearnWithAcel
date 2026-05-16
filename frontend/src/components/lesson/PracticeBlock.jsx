import { FileCode2, Lightbulb, Terminal } from "lucide-react";

export default function PracticeBlock({ practice }) {
  if (!practice) return null;
  return (
    <div className="relative overflow-hidden rounded-2xl border border-accent/25 bg-gradient-to-br from-accent/10 via-card to-card p-6 sm:p-7">
      <div className="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-accent/20 blur-3xl" />

      <div className="relative">
        <div className="flex items-center gap-2">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg border border-accent/30 bg-accent/10 text-accent-hover">
            <Terminal size={14} />
          </span>
          <div>
            <div className="font-mono text-[11px] uppercase tracking-[0.14em] text-accent-hover">
              Praktek sambil baca
            </div>
            <h3 className="font-display text-base font-semibold text-foreground">
              Buka VS Code, kita coding bareng.
            </h3>
          </div>
        </div>

        {practice.fileName && (
          <div className="mt-5 inline-flex items-center gap-2 rounded-lg border border-white/10 bg-black/40 px-3 py-1.5 font-mono text-xs text-muted">
            <FileCode2 size={12} className="text-accent-hover" />
            {practice.fileName}
          </div>
        )}

        <ol className="mt-5 space-y-2.5">
          {practice.steps.map((step, i) => (
            <li
              key={i}
              className="flex gap-3 text-[15px] leading-relaxed text-foreground/85"
            >
              <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full border border-accent/30 bg-accent/10 font-mono text-[11px] text-accent-hover">
                {i + 1}
              </span>
              <span className="whitespace-pre-line">{step}</span>
            </li>
          ))}
        </ol>

        {practice.tip && (
          <div className="mt-5 flex items-start gap-2.5 rounded-xl border border-white/5 bg-white/[0.03] p-4 text-sm leading-relaxed text-foreground/80">
            <Lightbulb size={14} className="mt-0.5 shrink-0 text-amber-300" />
            <span>
              <span className="font-medium text-foreground">Tip. </span>
              {practice.tip}
            </span>
          </div>
        )}
      </div>
    </div>
  );
}
