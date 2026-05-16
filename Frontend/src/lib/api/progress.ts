/**
 * Progress API bindings against the FastAPI backend.
 *
 *   POST /api/v1/progress/complete/{lesson_id}
 *   POST /api/v1/progress/view/{lesson_id}
 *   GET  /api/v1/progress/stats
 */

import { apiFetch } from "./client";

export type ApiProgress = {
  id: string;
  user_id: string;
  lesson_id: string;
  is_completed: boolean;
  completed_at: string | null;

  // Engagement payload returned by the backend on each complete call.
  // `just_completed` is true only when this request flipped the lesson
  // from incomplete to complete — frontend uses it to trigger the
  // celebration toast / xp burst exactly once.
  xp_earned?: number;
  new_total_xp?: number;
  streak?: number;
  just_completed?: boolean;
};

export type ApiLevelStats = {
  level_id: string;
  level_title: string;
  level_slug: string;
  /** Slug of the parent category (e.g. "frontend", "vibe"). Helps
   *  compose lesson links from the dashboard without an extra fetch. */
  category_slug?: string | null;
  total_lessons: number;
  completed_lessons: number;
  percentage: number;
};

export type ApiContinueLesson = {
  lesson_id: string;
  lesson_slug: string;
  lesson_title: string;
  level_id: string;
  level_slug: string;
  level_title: string;
  level_number: number;
  category_slug: string | null;
};

export type ApiStats = {
  total_lessons: number;
  completed_lessons: number;
  overall_percentage: number;
  by_level: ApiLevelStats[];

  /** Flat list of lesson IDs the user has completed. */
  completed_lesson_ids?: string[];

  // Engagement metrics — populated by the backend even for new users
  // (zero defaults). Frontend renders them in the dashboard hero.
  xp_total?: number;
  current_streak?: number;
  longest_streak?: number;
  last_activity_at?: string | null;

  /** Resolved next lesson the user should continue with. Null if
   *  there's no obvious continuation. */
  continue_lesson?: ApiContinueLesson | null;
};

export type ApiLessonView = {
  lesson_id: string;
  views: number;
  last_opened_at: string;
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

export function trackLessonView(
  lessonId: string,
  token: string
): Promise<ApiLessonView> {
  return apiFetch<ApiLessonView>(`/api/v1/progress/view/${lessonId}`, {
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
