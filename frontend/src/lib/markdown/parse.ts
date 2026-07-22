/**
 * Lightweight Markdown parser that emits a flat list of typed blocks.
 *
 * Lessons authored on the backend follow a constrained Markdown subset
 * (see Frontend/src/lib/markdown/index.tsx for the full list of supported
 * block types). This module is the only place that touches strings — once
 * we have `Block[]`, the renderer focuses on JSX.
 *
 * Notable additions on top of the previous parser:
 *   • Heading IDs are derived via `slugify()` so the lesson sidebar can
 *     anchor jump links and run a scroll spy.
 *   • Fenced code blocks track their language so we can render a header
 *     pill above the snippet.
 */

export type Block =
  | { type: "h1" | "h2" | "h3" | "h4"; id: string; text: string }
  | { type: "p"; text: string }
  | { type: "ul" | "ol"; items: string[] }
  | { type: "code"; lang: string; code: string }
  | { type: "blockquote"; lines: string[] }
  | { type: "table"; headers: string[]; rows: string[][] }
  | { type: "hr" };

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

export function parseMarkdown(markdown: string): Block[] {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const blocks: Block[] = [];
  const seen = new Map<string, number>();

  function uniqueSlug(raw: string): string {
    const base = slugify(raw) || "section";
    const count = seen.get(base) ?? 0;
    seen.set(base, count + 1);
    return count === 0 ? base : `${base}-${count + 1}`;
  }

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
      i += 1; // consume closing fence
      blocks.push({ type: "code", lang, code: buf.join("\n") });
      continue;
    }

    // Headings
    const heading = /^(#{1,4})\s+(.*)$/.exec(line);
    if (heading) {
      const level = heading[1].length as 1 | 2 | 3 | 4;
      const text = heading[2].trim();
      blocks.push({
        type: (`h${level}` as "h1" | "h2" | "h3" | "h4"),
        id: uniqueSlug(text),
        text,
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
      blocks.push({ type: "blockquote", lines: buf });
      continue;
    }

    // Table
    if (/^\s*\|/.test(line)) {
      const tableLines: string[] = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) {
        tableLines.push(lines[i]);
        i += 1;
      }
      if (tableLines.length >= 2) {
        const parseRow = (rowStr: string) =>
          rowStr
            .trim()
            .replace(/^\|/, "")
            .replace(/\|$/, "")
            .split("|")
            .map((cell) => cell.trim());

        const headers = parseRow(tableLines[0]);
        const contentRows = tableLines
          .slice(1)
          .filter((l) => !/^\s*\|?\s*:?-+:?\s*(\||\s*$)/.test(l));
        const rows = contentRows.map(parseRow);

        blocks.push({ type: "table", headers, rows });
        continue;
      }
    }

    // Unordered list
    if (/^\s*[-*+]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*+]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*+]\s+/.test(lines[i]) ? lines[i].match(/^\s*[-*+]\s+/)?.[0] || "" : "", ""));
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
      !/^(#{1,4}\s|```|>\s|---+\s*$|\s*\||\s*[-*+]\s|\s*\d+\.\s)/.test(lines[i])
    ) {
      buf.push(lines[i]);
      i += 1;
    }
    blocks.push({ type: "p", text: buf.join(" ") });
  }

  return blocks;
}

/* ------------------------------------------------------------------ */
/* Section grouping — wrap H2 + following blocks into a Section unit.  */
/* ------------------------------------------------------------------ */

export type Section = {
  /** Slug heading, used as anchor id. May be empty for the leading
   *  intro block (everything before the first H2, e.g. the H1 title). */
  id: string;
  /** Visible title of the section. Empty string for the intro block. */
  title: string;
  /** Inner blocks in source order. */
  blocks: Block[];
};

/**
 * Split flat blocks into sections delimited by H2 headings. Anything
 * before the first H2 is bundled in the leading "intro" section.
 */
export function groupSections(blocks: Block[]): Section[] {
  const sections: Section[] = [];
  let current: Section = { id: "", title: "", blocks: [] };

  for (const block of blocks) {
    if (block.type === "h2") {
      if (current.title || current.blocks.length) sections.push(current);
      current = { id: block.id, title: block.text, blocks: [] };
      continue;
    }
    current.blocks.push(block);
  }

  if (current.title || current.blocks.length) sections.push(current);
  return sections;
}

/* ------------------------------------------------------------------ */
/* Heading extraction for the sidebar TOC.                             */
/* ------------------------------------------------------------------ */

export type HeadingItem = { id: string; text: string; level: 2 | 3 };

export function extractHeadings(markdown: string): HeadingItem[] {
  const blocks = parseMarkdown(markdown);
  const items: HeadingItem[] = [];
  for (const b of blocks) {
    if (b.type === "h2" || b.type === "h3") {
      items.push({ id: b.id, text: b.text, level: b.type === "h2" ? 2 : 3 });
    }
  }
  return items;
}
