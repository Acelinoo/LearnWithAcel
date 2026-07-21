/**
 * Inline Markdown formatting (bold, italic, inline code, links).
 *
 * Inputs come from authored lesson content on our backend, so a small
 * regex-based pipeline is acceptable. We escape HTML before applying any
 * transformation to keep `dangerouslySetInnerHTML` safe.
 */

import type { ReactNode } from "react";

export function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

export function renderInline(text: string): ReactNode {
  let html = escapeHtml(text);

  // Inline code first to avoid mangling nested markers inside code.
  html = html.replace(
    /`([^`]+)`/g,
    (_, code) =>
      `<code class="rounded-md border border-[#1F1F1F] bg-black/40 px-1.5 py-0.5 font-mono text-[0.85em] text-accent-hover">${code}</code>`,
  );

  // Bold
  html = html.replace(
    /\*\*([^*]+)\*\*/g,
    '<strong class="font-semibold text-foreground">$1</strong>',
  );

  // Italic
  html = html.replace(/(^|\s)\*([^*\s][^*]*)\*/g, "$1<em>$2</em>");
  html = html.replace(/(^|\s)_([^_\s][^_]*)_/g, "$1<em>$2</em>");

  // Links
  html = html.replace(
    /\[([^\]]+)\]\(([^)]+)\)/g,
    (_, label, url) =>
      `<a href="${url}" class="font-medium text-accent-hover underline-offset-4 hover:text-accent hover:underline" target="_blank" rel="noopener noreferrer">${label}</a>`,
  );

  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}
