/**
 * Content API bindings against the FastAPI backend.
 *
 *   GET /api/v1/categories
 *   GET /api/v1/roadmap/{category_slug}
 *   GET /api/v1/lessons/{level_slug}/{lesson_slug}
 */

import { apiFetch } from "./client";

export type TechGroup = { label: string; items: string[] };

export type ApiCategory = {
  id: string;
  name: string;
  slug: string;
  available: boolean;
  role: string;
  side: string;
  description: string;
  tasks: string;
  /** Stored as JSON in the DB. The backend may hand it back as either an
   *  array of objects or a JSON-encoded string — both are normalized below. */
  techs: TechGroup[] | string;
};

export type ApiLessonSummary = {
  id: string;
  title: string;
  slug: string;
  summary: string;
  duration: string;
  base_viewers: number;
  order_index: number;
  xp_reward?: number;
  is_project?: boolean;
};

export type ApiLevelSummary = {
  id: string;
  number: number;
  title: string;
  slug: string;
  subtitle: string;
  description: string;
  duration: string;
  difficulty: string;
  accent_color: string;
  mini_project: string;
  quiz_count: number;
  base_viewers: number;
  /** JSON array of strings, may arrive as an array or string. */
  tags: string[] | string;
  coming_soon: boolean;
  lessons: ApiLessonSummary[];
};

export type ApiRoadmap = {
  category: ApiCategory;
  levels: ApiLevelSummary[];
};

export type ApiLessonDetail = {
  id: string;
  title: string;
  slug: string;
  summary: string;
  content: string;
  duration: string;
  base_viewers: number;
  order_index: number;
  level_id: string;
  xp_reward?: number;
  is_project?: boolean;
  criteria?: string[] | string | null;
  hints?: string | null;
};

/* ------------------------------------------------------------------ */
/* JSON normalization                                                  */
/* ------------------------------------------------------------------ */

function safeParseJson<T>(value: unknown, fallback: T): T {
  if (value == null) return fallback;
  if (Array.isArray(value) || typeof value === "object") return value as T;
  if (typeof value !== "string") return fallback;
  try {
    return JSON.parse(value) as T;
  } catch {
    return fallback;
  }
}

export function normalizeTechs(techs: ApiCategory["techs"]): TechGroup[] {
  return safeParseJson<TechGroup[]>(techs, []);
}

export function normalizeTags(tags: ApiLevelSummary["tags"]): string[] {
  return safeParseJson<string[]>(tags, []);
}

export function normalizeCriteria(criteria: ApiLessonDetail["criteria"]): string[] {
  return safeParseJson<string[]>(criteria, []);
}

/* ------------------------------------------------------------------ */
/* Calls                                                               */
/* ------------------------------------------------------------------ */

export function listCategories(): Promise<ApiCategory[]> {
  return apiFetch<ApiCategory[]>("/api/v1/categories", {
    method: "GET",
    cache: "no-store",
  });
}

export function getRoadmap(categorySlug: string): Promise<ApiRoadmap> {
  return apiFetch<ApiRoadmap>(`/api/v1/roadmap/${categorySlug}`, {
    method: "GET",
    cache: "no-store",
  });
}

export function getLesson(
  levelSlug: string,
  lessonSlug: string
): Promise<ApiLessonDetail> {
  return apiFetch<ApiLessonDetail>(
    `/api/v1/lessons/${levelSlug}/${lessonSlug}`,
    { method: "GET", cache: "no-store" }
  );
}
