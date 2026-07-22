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
import CodeBlock from "@/components/ui/CodeBlock";



type Props = { block: Block; index: number };

export function BlockRenderer({ block, index: _index }: Props) {
  switch (block.type) {
    case "h1":
      return (
        <h1 id={block.id} className="mb-6 scroll-mt-24 font-display text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
          {renderInline(block.text)}
        </h1>
      );
    case "h2":
      return (
        <h2
          id={block.id}
          className="mt-12 mb-6 scroll-mt-24 font-display text-2xl font-bold tracking-tight text-foreground border-b border-border/40 pb-3.5 sm:text-3xl"
        >
          {renderInline(block.text)}
        </h2>
      );
    case "h3":
      return (
        <h3
          id={block.id}
          className="mt-10 mb-4 scroll-mt-24 font-display text-xl font-semibold text-foreground/95"
        >
          {renderInline(block.text)}
        </h3>
      );
    case "h4":
      return (
        <h4
          id={block.id}
          className="mt-8 mb-4 scroll-mt-24 font-display text-lg font-medium text-foreground/90"
        >
          {renderInline(block.text)}
        </h4>
      );
    case "p":
      return (
        <p className="mb-6 leading-relaxed text-foreground/90 font-normal text-base sm:text-[17px]">
          {renderInline(block.text)}
        </p>
      );
    case "ul":
      return (
        <ul className="mb-6 mt-4 list-disc space-y-4 pl-5 text-foreground/90 text-base sm:text-[17px] marker:text-accent-hover">
          {block.items.map((item, j) => (
            <li key={j} className="leading-relaxed pl-1">
              {renderInline(item)}
            </li>
          ))}
        </ul>
      );
    case "ol":
      return (
        <ol className="mb-6 mt-4 list-decimal space-y-4 pl-5 text-foreground/90 text-base sm:text-[17px] marker:font-mono marker:text-accent-hover marker:text-[0.9em]">
          {block.items.map((item, j) => (
            <li key={j} className="leading-relaxed pl-1">
              {renderInline(item)}
            </li>
          ))}
        </ol>
      );
    case "code":
      return <CodeBlock code={block.code} lang={block.lang} />;
    case "table":
      return (
        <div className="my-8 overflow-x-auto rounded-2xl border border-border/80 bg-black/40 p-1.5 shadow-md">
          <table className="w-full text-left text-sm sm:text-[15px] text-foreground/90 border-collapse">
            <thead>
              <tr className="border-b border-border/80 bg-white/[0.05]">
                {block.headers.map((h, j) => (
                  <th key={j} className="px-5 py-4 font-semibold text-foreground">
                    {renderInline(h)}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-border/30">
              {block.rows.map((row, rIdx) => (
                <tr key={rIdx} className="hover:bg-white/[0.03] transition-colors">
                  {row.map((cell, cIdx) => (
                    <td key={cIdx} className="px-5 py-4 leading-relaxed">
                      {renderInline(cell)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    case "blockquote":
      return (
        <blockquote className="my-6 rounded-2xl border-l-4 border-accent/80 bg-accent/[0.08] px-6 py-4.5 text-foreground/95 shadow-sm">
          {block.lines.map((ln, j) => (
            <p key={j} className="leading-relaxed my-1.5 text-base sm:text-[17px] font-medium italic">
              {renderInline(ln)}
            </p>
          ))}
        </blockquote>
      );
    case "hr":
      return <hr className="my-10 border-border/50" />;
    default:
      return null;
  }
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
