/**
 * Backwards-compatible re-export. The renderer was split into
 * `./markdown/` to support custom section callouts and a sidebar TOC.
 * Existing imports of `@/lib/markdown` keep working.
 */

export { Markdown, extractHeadings } from "./markdown/index";
export type { HeadingItem } from "./markdown/index";
