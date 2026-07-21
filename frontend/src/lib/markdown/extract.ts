/**
 * Structured extractors for the special lesson sections.
 *
 * The seed renders Quiz and Fix Error blocks in a fixed Markdown shape.
 * To make those sections feel alive (not a static article), the lesson
 * page parses them into typed data and hands the data off to client
 * components that handle interactions like reveal/hint/answer/retry.
 *
 * Format reference (taken from `backend/scripts/content/_template.py`):
 *
 *   ## Quiz
 *
 *   ### Soal 1
 *
 *   <question>
 *
 *   - A. <opt>
 *   - B. <opt>
 *   - C. <opt>
 *   - D. <opt>
 *
 *   Jawaban benar: B
 *
 *   Penjelasan: <text>
 *
 *
 *   ## Fix Error Challenge
 *
 *   Coba perbaiki dulu sebelum scroll ke hint.
 *
 *   ```<lang>
 *   <broken>
 *   ```
 *
 *   ### Hint
 *
 *   <hint>
 *
 *   ### Jawaban
 *
 *   <explanation>
 *
 *   ```<lang>
 *   <fixed>
 *   ```
 */

import type { Block, Section } from "./parse";

export type QuizQuestion = {
  number: number;
  question: string;
  options: string[];
  correctIndex: number; // 0..3
  explanation: string;
};

export type FixErrorChallenge = {
  intro: string;
  language: string;
  brokenCode: string;
  hint: string;
  answerExplanation: string;
  fixedCode: string;
};

/* ------------------------------------------------------------------ */
/* Quiz                                                                */
/* ------------------------------------------------------------------ */

const LETTER_TO_INDEX: Record<string, number> = { A: 0, B: 1, C: 2, D: 3 };

/**
 * Walk the section blocks and pick out every "### Soal N" sub-heading
 * with its options, correct letter, and explanation. Anything that
 * doesn't fit the schema is silently dropped — the renderer falls back
 * to plain text rendering when extraction fails.
 */
export function extractQuiz(section: Section): QuizQuestion[] {
  const out: QuizQuestion[] = [];
  const blocks = section.blocks;

  let i = 0;
  while (i < blocks.length) {
    const b = blocks[i];
    if (b.type === "h3" && /^Soal\s+\d+/i.test(b.text)) {
      const numMatch = /^Soal\s+(\d+)/i.exec(b.text);
      const number = numMatch ? parseInt(numMatch[1], 10) : out.length + 1;

      // Question paragraph
      let question = "";
      i += 1;
      if (i < blocks.length && blocks[i].type === "p") {
        question = (blocks[i] as { text: string }).text;
        i += 1;
      }

      // Options (UL with 4 items)
      let options: string[] = [];
      if (i < blocks.length && blocks[i].type === "ul") {
        options = (blocks[i] as { items: string[] }).items.map((item) =>
          // Strip leading "A. " / "B. " etc. so renderer controls labeling.
          item.replace(/^[A-D]\.\s*/, ""),
        );
        i += 1;
      }

      // "Jawaban benar: X" paragraph
      let correctIndex = -1;
      while (i < blocks.length && blocks[i].type === "p") {
        const text = (blocks[i] as { text: string }).text;
        const m = /Jawaban benar:\s*([A-D])/i.exec(text);
        if (m) {
          correctIndex = LETTER_TO_INDEX[m[1].toUpperCase()] ?? -1;
          i += 1;
          break;
        }
        i += 1;
      }

      // "Penjelasan: ..." paragraph
      let explanation = "";
      if (i < blocks.length && blocks[i].type === "p") {
        const text = (blocks[i] as { text: string }).text;
        explanation = text.replace(/^Penjelasan:\s*/i, "");
        i += 1;
      }

      if (
        question &&
        options.length === 4 &&
        correctIndex >= 0 &&
        explanation
      ) {
        out.push({ number, question, options, correctIndex, explanation });
      }
      continue;
    }
    i += 1;
  }

  return out;
}

/* ------------------------------------------------------------------ */
/* Fix Error                                                           */
/* ------------------------------------------------------------------ */

type SubSection = "intro" | "broken" | "hint" | "answer" | "fixed";

export function extractFixError(section: Section): FixErrorChallenge | null {
  const blocks = section.blocks;
  let phase: SubSection = "intro";
  let language = "text";
  let brokenCode = "";
  let fixedCode = "";
  let intro = "";
  let hintBuf: string[] = [];
  let answerBuf: string[] = [];

  for (const b of blocks) {
    if (b.type === "h3") {
      const head = b.text.toLowerCase();
      if (head === "hint") {
        phase = "hint";
        continue;
      }
      if (head === "jawaban") {
        phase = "answer";
        continue;
      }
    }

    if (b.type === "code") {
      if (!brokenCode) {
        brokenCode = b.code;
        language = b.lang || language;
      } else if (!fixedCode) {
        fixedCode = b.code;
      }
      // After we see the broken code, the next text we collect belongs
      // to the answer section if the second code block follows it.
      if (phase === "answer" && fixedCode) {
        // nothing more to do here
      }
      continue;
    }

    if (b.type === "p") {
      if (phase === "intro") {
        intro = b.text;
      } else if (phase === "hint") {
        hintBuf.push(b.text);
      } else if (phase === "answer") {
        // Lines like "1. xxx" come through as ol; paragraphs in this
        // phase are intro lines or summary text we keep.
        answerBuf.push(b.text);
      }
    }

    if (b.type === "ul" || b.type === "ol") {
      const items = (b as { items: string[] }).items;
      const joined = items.map((it, idx) => `${idx + 1}. ${it}`).join("\n");
      if (phase === "hint") hintBuf.push(joined);
      if (phase === "answer") answerBuf.push(joined);
    }
  }

  if (!brokenCode) return null;

  return {
    intro,
    language,
    brokenCode,
    hint: hintBuf.join("\n\n").trim(),
    answerExplanation: answerBuf.join("\n\n").trim(),
    fixedCode,
  };
}
