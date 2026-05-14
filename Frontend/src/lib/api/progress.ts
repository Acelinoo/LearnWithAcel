/**
 * Progress API bindings against the FastAPI backend.
 *
 *   POST /api/v1/progress/complete/{lesson_id}
 *   GET  /api/v1/progress/stats
 */

import { apiFetch } from "./client";

export type ApiProgress = {
  id: string;
  user_id: string;
  lesson_id: string;
  is_completed: boolean;
  completed_at: string | null;
};

export type ApiLevelStats = {
  level_id: string;
  level_title: string;
  level_slug: string;
  total_lessons: number;
  completed_lessons: number;
  percentage: number;
};

export type ApiStats = {
  total_lessons: number;
  completed_lessons: number;
  overall_percentage: number;
  by_level: ApiLevelStats[];
};

export function completeLesson(
  lessonId: string,
  token: string
): Promise<ApiProgress> {
  return apiFetch<ApiProgress>(`/api/v1/progress/complete/${lessonId}`, {
    method: "POST",
    token,
  });
}

export function getStats(token: string): Promise<ApiStats> {
  return apiFetch<ApiStats>("/api/v1/progress/stats", {
    method: "GET",
    token,
    cache: "no-store",
  });
}
