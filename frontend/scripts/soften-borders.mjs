/**
 * One-shot codemod: replace bright "white" borders/backgrounds with dark
 * variants powered by the shared design tokens (`border`, `border-strong`).
 *
 * The previous theme leaned on `border-white/[0.05]` style helpers, which
 * shimmer too brightly against the very dark background. This script
 * normalizes the entire frontend so every component picks up the same
 * subtle, dark-grey treatment.
 *
 * Run from the Frontend/ folder:
 *   node scripts/soften-borders.mjs
 *
 * Idempotent: running it twice is safe.
 */

import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve(process.cwd(), "src");

const EXTS = new Set([".tsx", ".ts", ".jsx", ".js", ".css"]);

// Ordered most-specific → least-specific. Anchors with a leading "border"
// are replaced first so we don't double-translate things like
// "border border-white/10".
const REPLACEMENTS = [
  // Border colour helpers
  [/border-white\/(?:\[0\.0\d+\]|\d+)/g, "border-border"],
  [/border-b-white\/(?:\[0\.0\d+\]|\d+)/g, "border-b-border"],
  [/border-t-white\/(?:\[0\.0\d+\]|\d+)/g, "border-t-border"],
  [/hover:border-white\/(?:\[0\.0?\d+\]|\d+)/g, "hover:border-border-strong"],
  [
    /focus-within:border-white\/(?:\[0\.0?\d+\]|\d+)/g,
    "focus-within:border-border-strong",
  ],

  // Subtle white background panels → near-black, ambient
  [/bg-white\/\[0\.0(?:1|15|2|25|3|35|4)\]/g, "bg-black/30"],
  [/bg-white\/\[0\.0?(?:5|6)\]/g, "bg-black/40"],
  [/bg-white\/\[0\.0?(?:8|9)\]/g, "bg-black/50"],
  [/bg-white\/(?:5|10)\b/g, "bg-black/40"],
  [/hover:bg-white\/\[0\.0?\d+\]/g, "hover:bg-black/40"],
];

let touched = 0;
let scanned = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "node_modules" || entry.name.startsWith(".next")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
    } else if (EXTS.has(path.extname(entry.name))) {
      scanned += 1;
      const before = fs.readFileSync(full, "utf8");
      let after = before;
      for (const [pattern, replacement] of REPLACEMENTS) {
        after = after.replace(pattern, replacement);
      }
      if (after !== before) {
        fs.writeFileSync(full, after);
        touched += 1;
        console.log("  •", path.relative(process.cwd(), full));
      }
    }
  }
}

console.log(`Scanning ${ROOT} ...`);
walk(ROOT);
console.log(`\n${touched} file(s) updated, ${scanned} scanned.`);
