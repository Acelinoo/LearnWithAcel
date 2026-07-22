/**
 * Section-level rendering.
 *
 * Lessons follow a canonical structure: Ringkasan Kilat → Pembuka →
 * Penjelasan inti → Contoh code → Mini Practice → Fix Error Challenge
 * → Quiz → Kesalahan umum. Every section renders as a plain heading
 * (eyebrow + H2) followed by content. Interactive sections (Fix Error
 * Challenge, Quiz) swap their body for a dedicated client component
 * but still use the same heading treatment for visual consistency.
 */

import { Blocks } from "./blocks";
import type { Section } from "./parse";
import { extractFixError, extractQuiz } from "./extract";
import Quiz from "@/components/lesson/Quiz";
import FixError from "@/components/lesson/FixError";

/* ------------------------------------------------------------------ */
/* Section type detection                                              */
/* ------------------------------------------------------------------ */

export type SectionKind =
  | "tldr"
  | "metadata-tools"
  | "metadata-outcomes"
  | "practice"
  | "fix-error"
  | "quiz"
  | "common-mistakes"
  | "default";

const TITLE_PATTERNS: Array<{ pattern: RegExp; kind: SectionKind }> = [
  { pattern: /^tl;?dr$/i, kind: "tldr" },
  { pattern: /^ringkasan kilat$/i, kind: "tldr" },
  { pattern: /^inti materi$/i, kind: "tldr" },
  { pattern: /^tools yang dipakai$/i, kind: "metadata-tools" },
  { pattern: /^yang akan kamu bisa setelah ini$/i, kind: "metadata-outcomes" },
  { pattern: /^yang akan kamu bisa$/i, kind: "metadata-outcomes" },
  { pattern: /^mini practice$/i, kind: "practice" },
  { pattern: /^fix error challenge$/i, kind: "fix-error" },
  { pattern: /^quiz$/i, kind: "quiz" },
  { pattern: /^kesalahan umum$/i, kind: "common-mistakes" },
];

export function detectSectionKind(title: string): SectionKind {
  for (const { pattern, kind } of TITLE_PATTERNS) {
    if (pattern.test(title.trim())) return kind;
  }
  return "default";
}

/* ------------------------------------------------------------------ */
/* Specific section renderers                                          */
/* ------------------------------------------------------------------ */

export function TldrSection({ section }: { section: Section }) {
  return (
    <PlainSection
      section={section}
      eyebrow="Inti Materi"
      title="Ringkasan Kilat"
    />
  );
}

export function PracticeSection({ section }: { section: Section }) {
  return (
    <PlainSection
      section={section}
      eyebrow="Coba langsung"
      title="Mini Practice"
    />
  );
}

export function FixErrorSection({ section }: { section: Section }) {
  const challenge = extractFixError(section);
  return (
    <section className="mt-16 scroll-mt-24" id={section.id}>
      <div className="text-[10px] font-semibold uppercase tracking-[0.18em] text-foreground/55">
        Latihan debug
      </div>
      <h2 className="mt-2 font-display text-2xl font-semibold tracking-tight text-foreground sm:text-[1.7rem]">
        Fix Error Challenge
      </h2>
      <div className="mt-5">
        {challenge ? (
          <FixError challenge={challenge} />
        ) : (
          <Blocks blocks={section.blocks} />
        )}
      </div>
    </section>
  );
}

export function CommonMistakesSection({ section }: { section: Section }) {
  return (
    <PlainSection
      section={section}
      eyebrow="Hindari ini"
      title="Kesalahan umum"
    />
  );
}

export function QuizSection({ section }: { section: Section }) {
  const questions = extractQuiz(section);
  return (
    <section className="mt-16 scroll-mt-24" id={section.id}>
      <div className="text-[10px] font-semibold uppercase tracking-[0.18em] text-foreground/55">
        Uji pemahaman
      </div>
      <h2 className="mt-2 font-display text-2xl font-semibold tracking-tight text-foreground sm:text-[1.7rem]">
        Quiz
      </h2>
      <div className="mt-5">
        {questions.length > 0 ? (
          <Quiz questions={questions} />
        ) : (
          <Blocks blocks={section.blocks} />
        )}
      </div>
    </section>
  );
}

export function MetadataSection({
  section,
  variant,
}: {
  section: Section;
  variant: "tools" | "outcomes";
}) {
  return (
    <PlainSection
      section={section}
      eyebrow={variant === "tools" ? "Persiapan" : "Setelah lesson ini"}
      title={
        variant === "tools" ? "Tools yang dipakai" : "Yang akan kamu bisa"
      }
    />
  );
}

export function DefaultSection({ section }: { section: Section }) {
  return <PlainSection section={section} />;
}

/**
 * Some legacy alias kept for backwards compat at the index re-export.
 * (Not currently used but harmless.)
 */
export { PlainSection };

/* ------------------------------------------------------------------ */
/* Plain section — used for any "informational" section that should
 * blend visually with Pembuka / Penjelasan inti instead of being
 * wrapped in a colored card.
 *
 * The eyebrow is rendered above the heading as a small uppercase tag.
 * Optional accent color comes through the heading itself, not a border.
 * ------------------------------------------------------------------ */

type PlainProps = {
  section: Section;
  /** Optional small label above the H2, e.g. "Inti Materi". */
  eyebrow?: string;
  /** Optional override for the visible H2 text. Defaults to the
   *  section title from the markdown. */
  title?: string;
};

function PlainSection({ section, eyebrow, title }: PlainProps) {
  const heading = title ?? section.title;
  return (
    <section className="mt-14 scroll-mt-24 border-t border-border/30 pt-10 first:mt-0 first:border-t-0 first:pt-0" id={section.id}>
      {eyebrow && (
        <div className="text-[11px] font-semibold uppercase tracking-[0.2em] text-accent-hover">
          {eyebrow}
        </div>
      )}
      {heading && (
        <h2 className="mt-2 font-display text-2xl font-bold tracking-tight text-foreground sm:text-[1.8rem]">
          {heading}
        </h2>
      )}
      <div className={heading ? "mt-6 space-y-6" : "space-y-6"}>
        <Blocks blocks={section.blocks} />
      </div>
    </section>
  );
}
