/**
 * Public Markdown renderer.
 *
 * Pipeline:
 *   parseMarkdown(string) → Block[]
 *   groupSections(Block[]) → Section[]
 *   each Section → custom callout (TL;DR, Practice, Fix Error, Quiz,
 *                                  Checkpoint, Common Mistakes, …)
 *                  or default heading + body
 *
 * The frontend Markdown subset supported is intentionally small —
 * see `parse.ts` for the supported block types.
 */

import { parseMarkdown, groupSections, extractHeadings, type HeadingItem } from "./parse";
import { Blocks } from "./blocks";
import {
  detectSectionKind,
  TldrSection,
  PracticeSection,
  FixErrorSection,
  QuizSection,
  CommonMistakesSection,
  MetadataSection,
  DefaultSection,
} from "./sections";

export type { HeadingItem };
export { extractHeadings };

export function Markdown({ source }: { source: string }) {
  if (!source) return null;
  const sections = groupSections(parseMarkdown(source));

  return (
    <div className="prose-article">
      {sections.map((section, i) => {
        // Lead-in fragment (everything before the first H2). Render
        // its blocks straight without a section wrapper.
        if (!section.title) {
          return <Blocks key={`intro-${i}`} blocks={section.blocks} />;
        }

        const kind = detectSectionKind(section.title);
        switch (kind) {
          case "tldr":
            return <TldrSection key={section.id} section={section} />;
          case "metadata-tools":
            return (
              <MetadataSection
                key={section.id}
                section={section}
                variant="tools"
              />
            );
          case "metadata-outcomes":
            return (
              <MetadataSection
                key={section.id}
                section={section}
                variant="outcomes"
              />
            );
          case "practice":
            return <PracticeSection key={section.id} section={section} />;
          case "fix-error":
            return <FixErrorSection key={section.id} section={section} />;
          case "quiz":
            return <QuizSection key={section.id} section={section} />;
          case "common-mistakes":
            return <CommonMistakesSection key={section.id} section={section} />;
          default:
            return <DefaultSection key={section.id} section={section} />;
        }
      })}
    </div>
  );
}
