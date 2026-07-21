/**
 * Auth API bindings against the FastAPI backend.
 *   POST /api/v1/auth/register
 *   POST /api/v1/auth/login
 *   GET  /api/v1/auth/me
 */

import { apiFetch } from "./client";

export type ApiUser = {
  id: string;
  email: string;
  full_name: string;
  avatar_url: string | null;
  is_admin: boolean;
  created_at: string;
  selected_category: string | null;
  selected_role: string | null;
};

export type LoginPayload = {
  email: string;
  password: string;
};

export type RegisterPayload = {
  email: string;
  password: string;
  full_name: string;
};

export type UpdateRolePayload = {
  selected_category: string;
  selected_role: string;
};

export type TokenResponse = {
  access_token: string;
  token_type: string;
};

export function login(payload: LoginPayload): Promise<TokenResponse> {
  return apiFetch<TokenResponse>("/api/v1/auth/login", {
    method: "POST",
    body: payload,
  });
}

export function register(payload: RegisterPayload): Promise<ApiUser> {
  return apiFetch<ApiUser>("/api/v1/auth/register", {
    method: "POST",
    body: payload,
  });
}

export function getMe(token: string): Promise<ApiUser> {
  return apiFetch<ApiUser>("/api/v1/auth/me", {
    method: "GET",
    token,
    cache: "no-store",
  });
}

export function updateRole(token: string, payload: UpdateRolePayload): Promise<ApiUser> {
  return apiFetch<ApiUser>("/api/v1/auth/role", {
    method: "PUT",
    token,
    body: payload,
  });
}
