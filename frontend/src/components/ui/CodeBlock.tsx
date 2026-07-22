"use client";

import { useState } from "react";
import { Check, Copy, Code2 } from "lucide-react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/cjs/styles/prism";

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

export default function CodeBlock({ code, lang }: { code: string; lang: string }) {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="my-7 overflow-hidden rounded-2xl border border-border bg-[#0a0a0a]">
      <div className="flex items-center justify-between border-b border-border bg-black/40 px-4 py-2">
        <div className="flex items-center gap-2">
          <Code2 size={12} className="text-muted/70" />
          <span className="font-mono text-[10.5px] uppercase tracking-[0.18em] text-muted/70">
            {langLabel(lang)}
          </span>
        </div>
        <button
          onClick={copyToClipboard}
          className="flex items-center gap-1.5 rounded-md px-2 py-1 text-xs text-muted/70 hover:bg-white/10 hover:text-foreground transition-colors"
          aria-label="Copy code"
        >
          {copied ? <Check size={14} className="text-emerald-400" /> : <Copy size={14} />}
          <span>{copied ? "Copied" : "Copy"}</span>
        </button>
      </div>
      <div className="text-[13px] leading-[1.7]">
        <SyntaxHighlighter
          language={lang || "text"}
          style={vscDarkPlus}
          customStyle={{
            margin: 0,
            padding: "1.25rem 1.25rem",
            background: "transparent",
            fontSize: "13px",
          }}
          codeTagProps={{
            style: {
              fontFamily: "var(--font-geist-mono)",
            },
          }}
        >
          {code}
        </SyntaxHighlighter>
      </div>
    </div>
  );
}
