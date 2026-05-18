/**
 * Pure helpers used by roadmap UI to format and aggregate data returned
 * by the FastAPI backend. No data fetching here — keep these usable on
 * both server and client.
 */

import {
  normalizeTags,
  normalizeTechs,
  type ApiCategory,
  type ApiLevelSummary,
} from "@/lib/api/content";

/** Lightweight category shape used by the tabs UI. */
export type CategoryTab = {
  id: string;
  label: string;
  available: boolean;
  role: string;
  side: string;
  description: string;
  tasks: string;
  techs: { label: string; items: string[] }[];
};

export function categoryToTab(c: ApiCategory): CategoryTab {
  return {
    id: c.slug,
    label: c.name,
    available: c.available,
    role: c.role,
    side: c.side,
    description: c.description,
    tasks: c.tasks,
    techs: normalizeTechs(c.techs),
  };
}

/** Total lessons across a list of levels. */
export function aggregateLevels(levels: ApiLevelSummary[]) {
  let totalLessons = 0;
  for (const lvl of levels) {
    totalLessons += lvl.lessons.length;
  }
  return { totalLessons };
}

/** Get parsed tags for a level. Defensive against backends sending strings. */
export function levelTags(level: ApiLevelSummary): string[] {
  return normalizeTags(level.tags);
}
