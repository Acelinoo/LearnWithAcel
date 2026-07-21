"use client";

/**
 * Interactive Fix Error challenge.
 *
 * Layout:
 *
 *   ┌─────────────────────────────────────────────────────┐
 *   │ Editor mock                                          │
 *   │  ┌─ tab bar ────────────────────────────────┐        │
 *   │  │ broken-code.<lang>            ⚠ 3 issues │        │
 *   │  └──────────────────────────────────────────┘        │
 *   │  line numbers + broken code                          │
 *   ├─────────────────────────────────────────────────────┤
 *   │ [ Lihat Hint ]    [ Lihat Jawaban ]                  │
 *   └─────────────────────────────────────────────────────┘
 *
 * Hint and Jawaban panels stay collapsed until the learner clicks the
 * matching button — keeping the puzzle a puzzle.
 */

import { useState } from "react";
import { ChevronDown, Lightbulb, Wrench } from "lucide-react";
import type { FixErrorChallenge } from "@/lib/markdown/extract";
import { renderInline } from "@/lib/markdown/inline";
import { cn } from "@/lib/utils";

const LANG_LABELS: Record<string, string> = {
  js: "javascript",
  javascript: "javascript",
  ts: "typescript",
  typescript: "typescript",
  tsx: "tsx",
  jsx: "jsx",
  py: "python",
  python: "python",
  html: "html",
  css: "css",
  json: "json",
  bash: "bash",
  shell: "shell",
  sh: "shell",
  sql: "sql",
  prisma: "prisma",
  http: "http",
  text: "text",
};

function fileExt(lang: string): string {
  const norm = lang.toLowerCase();
  switch (norm) {
    case "js":
    case "javascript":
      return "js";
    case "ts":
    case "typescript":
      return "ts";
    case "jsx":
      return "jsx";
    case "tsx":
      return "tsx";
    case "py":
    case "python":
      return "py";
    case "html":
      return "html";
    case "css":
      return "css";
    case "json":
      return "json";
    case "bash":
    case "shell":
    case "sh":
      return "sh";
    case "sql":
      return "sql";
    case "prisma":
      return "prisma";
    default:
      return "txt";
  }
}

type Props = {
  challenge: FixErrorChallenge;
};

export default function FixError({ challenge }: Props) {
  const [hintOpen, setHintOpen] = useState(false);
  const [answerOpen, setAnswerOpen] = useState(false);

  const lines = challenge.brokenCode.split("\n");
  const langLabel = LANG_LABELS[challenge.language.toLowerCase()] ?? challenge.language;

  return (
    <div className="space-y-4">
      {challenge.intro && (
        <p className="text-[14px] leading-relaxed text-muted">
          {renderInline(challenge.intro)}
        </p>
      )}

      {/* Editor mock for the broken code */}
      <div className="overflow-hidden rounded-xl border border-border bg-[#09090b]">
        <div className="flex items-center justify-between border-b border-border bg-black/40 px-4 py-2.5">
          <div className="flex items-center gap-2 text-[12px] text-muted">
            <span className="flex gap-1.5">
              <span aria-hidden className="h-2.5 w-2.5 rounded-full bg-rose-400/60" />
              <span aria-hidden className="h-2.5 w-2.5 rounded-full bg-amber-400/60" />
              <span aria-hidden className="h-2.5 w-2.5 rounded-full bg-emerald-400/60" />
            </span>
            <span className="font-mono text-[11.5px] text-muted/80">
              broken.{fileExt(challenge.language)}
            </span>
          </div>
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-muted/70">
            {langLabel}
          </span>
        </div>

        <pre className="overflow-x-auto px-4 py-4 font-mono text-[13px] leading-[1.65] text-foreground/90">
          <code>
            {lines.map((line, i) => (
              <div key={i} className="flex gap-4">
                <span
                  aria-hidden
                  className="select-none text-right font-mono text-[11px] text-muted/40"
                  style={{ minWidth: "1.6rem" }}
                >
                  {i + 1}
                </span>
                <span className="flex-1 whitespace-pre">{line || " "}</span>
              </div>
            ))}
          </code>
        </pre>
      </div>

      {/* Action row */}
      <div className="flex flex-wrap gap-2">
        <RevealButton
          label={hintOpen ? "Sembunyikan hint" : "Lihat Hint"}
          icon={<Lightbulb size={13} />}
          tone="amber"
          open={hintOpen}
          onClick={() => setHintOpen((v) => !v)}
        />
        <RevealButton
          label={answerOpen ? "Sembunyikan jawaban" : "Lihat Jawaban"}
          icon={<Wrench size={13} />}
          tone="emerald"
          open={answerOpen}
          onClick={() => setAnswerOpen((v) => !v)}
        />
      </div>

      {/* Hint */}
      <Collapsible
        open={hintOpen}
        title="Hint"
        tone="amber"
        body={renderInline(challenge.hint)}
      />

      {/* Answer */}
      <Collapsible
        open={answerOpen}
        title="Jawaban"
        tone="emerald"
        body={
          <div className="space-y-4">
            {challenge.answerExplanation && (
              <div className="space-y-2 text-[14px] leading-relaxed text-foreground/85">
                {challenge.answerExplanation
                  .split("\n")
                  .filter((l) => l.trim())
                  .map((line, idx) => (
                    <p key={idx}>{renderInline(line)}</p>
                  ))}
              </div>
            )}
            {challenge.fixedCode && (
              <div className="overflow-hidden rounded-xl border border-emerald-400/20 bg-[#0a0a0a]">
                <div className="flex items-center justify-between border-b border-emerald-400/10 bg-emerald-400/[0.04] px-4 py-2 text-[11px] text-emerald-200/80">
                  <span className="font-mono">fixed.{fileExt(challenge.language)}</span>
                  <span className="font-mono uppercase tracking-[0.18em]">
                    {langLabel}
                  </span>
                </div>
                <pre className="overflow-x-auto px-4 py-4 font-mono text-[13px] leading-[1.65] text-foreground/90">
                  <code>{challenge.fixedCode}</code>
                </pre>
              </div>
            )}
          </div>
        }
      />
    </div>
  );
}

/* ------------------------------------------------------------------ */
/* Reveal button + collapsible primitives                               */
/* ------------------------------------------------------------------ */

const TONE_BUTTON: Record<"amber" | "emerald", string> = {
  amber:
    "border-amber-300/20 bg-amber-300/[0.04] text-amber-100 hover:border-amber-300/40 hover:bg-amber-300/[0.08]",
  emerald:
    "border-emerald-300/20 bg-emerald-400/[0.04] text-emerald-100 hover:border-emerald-300/40 hover:bg-emerald-400/[0.08]",
};

function RevealButton({
  label,
  icon,
  tone,
  open,
  onClick,
}: {
  label: string;
  icon: React.ReactNode;
  tone: "amber" | "emerald";
  open: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-expanded={open}
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-[12.5px] font-medium transition-all",
        TONE_BUTTON[tone],
      )}
    >
      {icon}
      {label}
      <ChevronDown
        size={12}
        className={cn(
          "transition-transform duration-200",
          open && "rotate-180",
        )}
      />
    </button>
  );
}

const TONE_PANEL: Record<"amber" | "emerald", string> = {
  amber: "border-amber-300/20 bg-amber-300/[0.03]",
  emerald: "border-emerald-300/20 bg-emerald-400/[0.03]",
};

function Collapsible({
  open,
  title,
  tone,
  body,
}: {
  open: boolean;
  title: string;
  tone: "amber" | "emerald";
  body: React.ReactNode;
}) {
  if (!open) return null;
  return (
    <div
      className={cn(
        "animate-fade-up overflow-hidden rounded-2xl border px-5 py-4",
        TONE_PANEL[tone],
      )}
    >
      <div
        className={cn(
          "text-[10px] font-semibold uppercase tracking-[0.18em]",
          tone === "amber" ? "text-amber-200/80" : "text-emerald-200/80",
        )}
      >
        {title}
      </div>
      <div className="mt-2 text-[14px] leading-relaxed text-foreground/85">
        {body}
      </div>
    </div>
  );
}
