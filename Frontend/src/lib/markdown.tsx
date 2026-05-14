/**
 * Minimal Markdown renderer for lesson content delivered by the FastAPI
 * backend. We intentionally avoid pulling in a heavyweight MD library —
 * lessons are written in a constrained subset (headings, paragraphs,
 * inline code, fenced code blocks, lists, bold/italic) and that's enough
 * to keep the typography premium without extra deps.
 */

import type { ReactNode } from "react";

type Block =
  | { type: "h1" | "h2" | "h3" | "h4"; text: string }
  | { type: "p"; text: string }
  | { type: "ul" | "ol"; items: string[] }
  | { type: "code"; lang: string; code: string }
  | { type: "blockquote"; text: string }
  | { type: "hr" };

function parse(markdown: string): Block[] {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const blocks: Block[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block
    if (/^```/.test(line)) {
      const lang = line.replace(/^```/, "").trim();
      const buf: string[] = [];
      i += 1;
      while (i < lines.length && !/^```/.test(lines[i])) {
        buf.push(lines[i]);
        i += 1;
      }
      i += 1; // consume closing ```
      blocks.push({ type: "code", lang, code: buf.join("\n") });
      continue;
    }

    // Headings
    const heading = /^(#{1,4})\s+(.*)$/.exec(line);
    if (heading) {
      const level = heading[1].length as 1 | 2 | 3 | 4;
      blocks.push({
        type: (`h${level}` as "h1" | "h2" | "h3" | "h4"),
        text: heading[2].trim(),
      });
      i += 1;
      continue;
    }

    // Horizontal rule
    if (/^---+\s*$/.test(line)) {
      blocks.push({ type: "hr" });
      i += 1;
      continue;
    }

    // Blockquote
    if (/^>\s?/.test(line)) {
      const buf: string[] = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        buf.push(lines[i].replace(/^>\s?/, ""));
        i += 1;
      }
      blocks.push({ type: "blockquote", text: buf.join(" ") });
      continue;
    }

    // Unordered list
    if (/^\s*[-*+]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*+]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*+]\s+/, ""));
        i += 1;
      }
      blocks.push({ type: "ul", items });
      continue;
    }

    // Ordered list
    if (/^\s*\d+\.\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*\d+\.\s+/, ""));
        i += 1;
      }
      blocks.push({ type: "ol", items });
      continue;
    }

    // Blank line
    if (line.trim() === "") {
      i += 1;
      continue;
    }

    // Paragraph (collect until blank/structural line)
    const buf: string[] = [];
    while (
      i < lines.length &&
      lines[i].trim() !== "" &&
      !/^(#{1,4}\s|```|>\s|---+\s*$|\s*[-*+]\s|\s*\d+\.\s)/.test(lines[i])
    ) {
      buf.push(lines[i]);
      i += 1;
    }
    blocks.push({ type: "p", text: buf.join(" ") });
  }

  return blocks;
}

/* ------------------------------------------------------------------ */
/* Inline formatting (bold, italic, inline code, links)                 */
/* ------------------------------------------------------------------ */

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderInline(text: string): ReactNode {
  // Tokenize the safest way: replace MD markers with HTML, then dangerouslySetInnerHTML.
  // The text is sourced from our backend (admin authored), so this is acceptable.
  let html = escapeHtml(text);

  // Inline code first to avoid mangling code samples.
  html = html.replace(/`([^`]+)`/g, (_, code) => `<code>${code}</code>`);

  // Bold (**text**)
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  // Italic (*text* or _text_)
  html = html.replace(/(^|\s)\*([^*\s][^*]*)\*/g, "$1<em>$2</em>");
  html = html.replace(/(^|\s)_([^_\s][^_]*)_/g, "$1<em>$2</em>");

  // Links [label](url)
  html = html.replace(
    /\[([^\]]+)\]\(([^)]+)\)/g,
    (_, label, url) =>
      `<a href="${url}" class="text-accent-hover hover:text-foreground" target="_blank" rel="noopener noreferrer">${label}</a>`
  );

  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}

/* ------------------------------------------------------------------ */
/* Public renderer                                                      */
/* ------------------------------------------------------------------ */

export function Markdown({ source }: { source: string }) {
  if (!source) return null;
  const blocks = parse(source);

  return (
    <div className="prose-article">
      {blocks.map((block, i) => {
        switch (block.type) {
          case "h1":
            return (
              <h2 key={i} className="text-3xl">
                {renderInline(block.text)}
              </h2>
            );
          case "h2":
            return <h2 key={i}>{renderInline(block.text)}</h2>;
          case "h3":
            return <h3 key={i}>{renderInline(block.text)}</h3>;
          case "h4":
            return (
              <h4
                key={i}
                className="mt-6 mb-2 font-display text-base font-semibold"
              >
                {renderInline(block.text)}
              </h4>
            );
          case "p":
            return <p key={i}>{renderInline(block.text)}</p>;
          case "ul":
            return (
              <ul key={i}>
                {block.items.map((item, j) => (
                  <li key={j}>{renderInline(item)}</li>
                ))}
              </ul>
            );
          case "ol":
            return (
              <ol key={i}>
                {block.items.map((item, j) => (
                  <li key={j}>{renderInline(item)}</li>
                ))}
              </ol>
            );
          case "code":
            return (
              <pre key={i}>
                <code>{block.code}</code>
              </pre>
            );
          case "blockquote":
            return (
              <blockquote key={i}>{renderInline(block.text)}</blockquote>
            );
          case "hr":
            return <hr key={i} className="my-8 border-white/5" />;
          default:
            return null;
        }
      })}
    </div>
  );
}
