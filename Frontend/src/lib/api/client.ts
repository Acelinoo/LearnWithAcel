/**
 * Thin fetch wrapper around the LearnWithAcel FastAPI backend.
 *
 * - Reads `NEXT_PUBLIC_API_URL` (defaults to http://localhost:8000)
 * - Adds `Authorization: Bearer <token>` when a token is provided
 * - Throws `ApiError` on non-2xx responses with a friendly message
 */

export const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export class ApiError extends Error {
  status: number;
  detail: unknown;

  constructor(message: string, status: number, detail?: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

type FetchOptions = Omit<RequestInit, "body"> & {
  body?: unknown;
  token?: string | null;
};

async function parseError(res: Response): Promise<{ message: string; detail: unknown }> {
  const text = await res.text();
  if (!text) return { message: res.statusText || `HTTP ${res.status}`, detail: null };
  try {
    const json = JSON.parse(text);
    const message =
      (typeof json?.detail === "string" && json.detail) ||
      (Array.isArray(json?.detail) && json.detail[0]?.msg) ||
      json?.message ||
      res.statusText ||
      `HTTP ${res.status}`;
    return { message, detail: json };
  } catch {
    return { message: text || `HTTP ${res.status}`, detail: text };
  }
}

export async function apiFetch<T>(
  path: string,
  options: FetchOptions = {}
): Promise<T> {
  const { body, token, headers, ...rest } = options;

  const finalHeaders: Record<string, string> = {
    Accept: "application/json",
    ...((headers as Record<string, string>) || {}),
  };

  if (body !== undefined && !(body instanceof FormData)) {
    finalHeaders["Content-Type"] = "application/json";
  }
  if (token) {
    finalHeaders["Authorization"] = `Bearer ${token}`;
  }

  const url = path.startsWith("http")
    ? path
    : `${API_URL}${path.startsWith("/") ? path : `/${path}`}`;

  const res = await fetch(url, {
    ...rest,
    headers: finalHeaders,
    body:
      body === undefined
        ? undefined
        : body instanceof FormData
          ? body
          : JSON.stringify(body),
  });

  if (!res.ok) {
    const { message, detail } = await parseError(res);
    throw new ApiError(message, res.status, detail);
  }

  if (res.status === 204) return undefined as T;
  const text = await res.text();
  if (!text) return undefined as T;
  try {
    return JSON.parse(text) as T;
  } catch {
    return text as unknown as T;
  }
}
