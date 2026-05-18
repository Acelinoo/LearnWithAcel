/**
 * Admin / CMS API bindings against the FastAPI backend.
 *
 * All endpoints require a JWT belonging to a user with `is_admin = true`.
 *
 *   POST   /api/v1/admin/categories
 *   PUT    /api/v1/admin/categories/{id}
 *   DELETE /api/v1/admin/categories/{id}
 *
 *   POST   /api/v1/admin/levels
 *   PUT    /api/v1/admin/levels/{id}
 *   DELETE /api/v1/admin/levels/{id}
 *
 *   POST   /api/v1/admin/lessons
 *   PUT    /api/v1/admin/lessons/{id}
 *   DELETE /api/v1/admin/lessons/{id}
 */

import { apiFetch } from "./client";
import type {
  ApiCategory,
  ApiLessonDetail,
  ApiLevelSummary,
  TechGroup,
} from "./content";

export type DeleteResponse = { message: string; id: string };

/* ── Categories ─────────────────────────────────────────────────── */

export type CategoryCreate = {
  name: string;
  slug: string;
  available: boolean;
  role: string;
  side: string;
  description: string;
  tasks: string;
  techs: TechGroup[];
};

export type CategoryUpdate = Partial<CategoryCreate>;

export function createCategory(
  payload: CategoryCreate,
  token: string
): Promise<ApiCategory> {
  return apiFetch<ApiCategory>("/api/v1/admin/categories", {
    method: "POST",
    body: payload,
    token,
  });
}

export function updateCategory(
  id: string,
  payload: CategoryUpdate,
  token: string
): Promise<ApiCategory> {
  return apiFetch<ApiCategory>(`/api/v1/admin/categories/${id}`, {
    method: "PUT",
    body: payload,
    token,
  });
}

export function deleteCategory(
  id: string,
  token: string
): Promise<DeleteResponse> {
  return apiFetch<DeleteResponse>(`/api/v1/admin/categories/${id}`, {
    method: "DELETE",
    token,
  });
}

/* ── Levels ─────────────────────────────────────────────────────── */

export type LevelCreate = {
  category_id: string;
  number: number;
  title: string;
  slug: string;
  subtitle: string;
  description: string;
  duration: string;
  difficulty: string;
  accent_color: string;
  mini_project: string;
  quiz_count?: number;
  tags: string[];
  coming_soon?: boolean;
};

export type LevelUpdate = Partial<LevelCreate>;

export function createLevel(
  payload: LevelCreate,
  token: string
): Promise<ApiLevelSummary> {
  return apiFetch<ApiLevelSummary>("/api/v1/admin/levels", {
    method: "POST",
    body: payload,
    token,
  });
}

export function updateLevel(
  id: string,
  payload: LevelUpdate,
  token: string
): Promise<ApiLevelSummary> {
  return apiFetch<ApiLevelSummary>(`/api/v1/admin/levels/${id}`, {
    method: "PUT",
    body: payload,
    token,
  });
}

export function deleteLevel(id: string, token: string): Promise<DeleteResponse> {
  return apiFetch<DeleteResponse>(`/api/v1/admin/levels/${id}`, {
    method: "DELETE",
    token,
  });
}

/* ── Lessons ────────────────────────────────────────────────────── */

export type LessonCreate = {
  level_id: string;
  title: string;
  slug: string;
  summary: string;
  content: string;
  duration: string;
  order_index: number;
};

export type LessonUpdate = Partial<LessonCreate>;

export function createLesson(
  payload: LessonCreate,
  token: string
): Promise<ApiLessonDetail> {
  return apiFetch<ApiLessonDetail>("/api/v1/admin/lessons", {
    method: "POST",
    body: payload,
    token,
  });
}

export function updateLesson(
  id: string,
  payload: LessonUpdate,
  token: string
): Promise<ApiLessonDetail> {
  return apiFetch<ApiLessonDetail>(`/api/v1/admin/lessons/${id}`, {
    method: "PUT",
    body: payload,
    token,
  });
}

export function deleteLesson(
  id: string,
  token: string
): Promise<DeleteResponse> {
  return apiFetch<DeleteResponse>(`/api/v1/admin/lessons/${id}`, {
    method: "DELETE",
    token,
  });
}
