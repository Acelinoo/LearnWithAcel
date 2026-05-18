/**
 * Block renderers for the Markdown pipeline.
 *
 * Each function maps one parsed block type to JSX. They're consumed by
 * both the regular content area and the section callouts, so they must
 * be context-free — no side effects, no fetching.
 */

import { Code2 } from "lucide-react";
import type { Block } from "./parse";
import { renderInline } from "./inline";

/** Map of fenced-code language tokens to a friendly label shown in the
 *  pill above the snippet. The list is intentionally short — anything
 *  unknown falls back to the raw token (or "code" if empty). */
const LANG_LABELS: Record<string, string> = {
  js: "JavaScript",
  javascript: "JavaScript",
  ts: "TypeScript",
  typescript: "TypeScript",
  tsx: "TSX",
  jsx: "JSX",
  py: "Python",
  python: "Python",
  html: "HTML",
  css: "CSS",
  json: "JSON",
  bash: "Bash",
  shell: "Shell",
  sh: "Shell",
  sql: "SQL",
  prisma: "Prisma",
  http: "HTTP",
  md: "Markdown",
  markdown: "Markdown",
  text: "Text",
};

function langLabel(raw: string): string {
  if (!raw) return "Code";
  const norm = raw.toLowerCase();
  return LANG_LABELS[norm] ?? raw;
}

type Props = { block: Block; index: number };

export function BlockRenderer({ block, index: _index }: Props) {
  switch (block.type) {
    case "h1":
      // Lesson page renders the title separately, but still keep h1
      // available for nested fragments.
      return (
        <h2 id={block.id} className="scroll-mt-24 font-display text-3xl font-semibold text-foreground">
          {renderInline(block.text)}
        </h2>
      );
    case "h2":
      // H2 is normally absorbed by section grouping, but we keep this
      // path for completeness.
      return (
        <h2
          id={block.id}
          className="mt-16 mb-5 scroll-mt-24 font-display text-2xl font-semibold tracking-tight text-foreground"
        >
          {renderInline(block.text)}
        </h2>
      );
    case "h3":
      return (
        <h3
          id={block.id}
          className="mt-10 mb-3 scroll-mt-24 font-display text-lg font-semibold text-foreground"
        >
          {renderInline(block.text)}
        </h3>
      );
    case "h4":
      return (
        <h4
          id={block.id}
          className="mt-8 mb-3 scroll-mt-24 font-display text-base font-semibold text-foreground"
        >
          {renderInline(block.text)}
        </h4>
      );
    case "p":
      return (
        <p className="my-5 leading-[1.85] text-foreground/85">
          {renderInline(block.text)}
        </p>
      );
    case "ul":
      return (
        <ul className="my-5 list-none space-y-2.5 pl-1 text-foreground/85">
          {block.items.map((item, j) => (
            <li key={j} className="relative pl-6 leading-[1.75]">
              <span
                aria-hidden
                className="absolute left-0 top-[0.7em] h-1.5 w-1.5 rounded-full bg-accent/45"
              />
              {renderInline(item)}
            </li>
          ))}
        </ul>
      );
    case "ol":
      return (
        <ol className="my-5 list-none space-y-2.5 pl-1 text-foreground/85">
          {block.items.map((item, j) => (
            <li key={j} className="relative pl-9 leading-[1.75]">
              <span
                aria-hidden
                className="absolute left-0 top-[0.15em] inline-flex h-5 min-w-5 items-center justify-center rounded-md border border-border bg-black/40 px-1 font-mono text-[10px] text-accent-hover"
              >
                {j + 1}
              </span>
              {renderInline(item)}
            </li>
          ))}
        </ol>
      );
    case "code":
      return <CodeBlock code={block.code} lang={block.lang} />;
    case "blockquote":
      return (
        <blockquote className="my-7 rounded-2xl border border-border bg-black/30 px-6 py-5 text-foreground/85">
          {block.lines.map((ln, j) => (
            <p key={j} className="leading-relaxed">
              {renderInline(ln)}
            </p>
          ))}
        </blockquote>
      );
    case "table":
      return <TableBlock headers={block.headers} rows={block.rows} />;
    case "hr":
      return <hr className="my-12 border-border" />;
    default:
      return null;
  }
}

/** Code block with a header pill (language tag) for visual hierarchy. */
function CodeBlock({ code, lang }: { code: string; lang: string }) {
  return (
    <div className="my-7 overflow-hidden rounded-2xl border border-border bg-[#0a0a0a]">
      <div className="flex items-center gap-2 border-b border-border bg-black/40 px-4 py-2">
        <Code2 size={12} className="text-muted/70" />
        <span className="font-mono text-[10.5px] uppercase tracking-[0.18em] text-muted/70">
          {langLabel(lang)}
        </span>
      </div>
      <pre className="overflow-x-auto px-5 py-5 font-mono text-[13px] leading-[1.7] text-foreground/90">
        <code>{code}</code>
      </pre>
    </div>
  );
}

/** Table block — used for compact comparison and reference rows.
 *  Keeps the same card-style border + dark surface as the rest of the
 *  lesson UI so it doesn't visually jump. */
function TableBlock({
  headers,
  rows,
}: {
  headers: string[];
  rows: string[][];
}) {
  if (headers.length === 0) return null;
  return (
    <div className="my-7 overflow-hidden rounded-2xl border border-border bg-black/30">
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-left text-[13.5px]">
          <thead>
            <tr className="bg-black/40">
              {headers.map((h, j) => (
                <th
                  key={j}
                  className="border-b border-border px-4 py-3 font-mono text-[10.5px] font-semibold uppercase tracking-[0.16em] text-muted/80"
                >
                  {renderInline(h)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, i) => (
              <tr key={i} className={i < rows.length - 1 ? "border-b border-border" : ""}>
                {headers.map((_, j) => (
                  <td
                    key={j}
                    className={
                      "px-4 py-3 align-top text-foreground/85 leading-[1.65]" +
                      (j === 0 ? " font-medium text-foreground" : "")
                    }
                  >
                    {renderInline(row[j] ?? "")}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

/** Render a list of blocks in source order. */
export function Blocks({ blocks }: { blocks: Block[] }) {
  return (
    <>
      {blocks.map((block, i) => (
        <BlockRenderer key={i} block={block} index={i} />
      ))}
    </>
  );
}
