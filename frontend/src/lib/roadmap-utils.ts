/**
 * Pure helpers used by roadmap UI to format and aggregate data returned
 * by the FastAPI backend. No data fetching here — keep these usable on
 * both server and client.
 */

import {
  normalizeTags,
  normalizeTechs,
  type ApiCategory,
  type ApiLessonSummary,
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

/** Total lessons/viewers across a list of levels. */
export function aggregateLevels(levels: ApiLevelSummary[]) {
  let totalLessons = 0;
  let totalViewers = 0;
  for (const lvl of levels) {
    totalLessons += lvl.lessons.length;
    totalViewers += lvl.base_viewers || 0;
  }
  return { totalLessons, totalViewers };
}

/** Top N most-viewed lessons across all levels. */
export type PopularLesson = ApiLessonSummary & {
  levelSlug: string;
  levelTitle: string;
  levelNumber: number;
};

export function getPopularLessons(
  levels: ApiLevelSummary[],
  limit = 5
): PopularLesson[] {
  const flat: PopularLesson[] = levels.flatMap((lvl) =>
    lvl.lessons.map((l) => ({
      ...l,
      levelSlug: lvl.slug,
      levelTitle: lvl.title,
      levelNumber: lvl.number,
    }))
  );
  return flat
    .sort((a, b) => b.base_viewers - a.base_viewers)
    .slice(0, limit);
}

/** The single most-viewed level (by base_viewers). */
export function getTopLevel(levels: ApiLevelSummary[]): ApiLevelSummary | null {
  if (!levels.length) return null;
  return [...levels].sort((a, b) => b.base_viewers - a.base_viewers)[0];
}

/** Get parsed tags for a level. Defensive against backends sending strings. */
export function levelTags(level: ApiLevelSummary): string[] {
  return normalizeTags(level.tags);
}
