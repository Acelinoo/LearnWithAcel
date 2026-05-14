/**
 * Server-only helpers for talking to the backend from React Server Components.
 *
 *   getServerToken()    — read the JWT cookie set by the auth flow
 *   getServerUser()     — fetch the current user via /auth/me
 *   getServerStats()    — fetch the current user's progress stats
 */

import { cookies } from "next/headers";
import { TOKEN_COOKIE } from "@/lib/auth/token";
import { getMe, type ApiUser } from "./auth";
import { getStats, type ApiStats } from "./progress";

export function getServerToken(): string | null {
  const store = cookies();
  return store.get(TOKEN_COOKIE)?.value ?? null;
}

export async function getServerUser(): Promise<ApiUser | null> {
  const token = getServerToken();
  if (!token) return null;
  try {
    return await getMe(token);
  } catch {
    return null;
  }
}

export async function getServerStats(): Promise<ApiStats | null> {
  const token = getServerToken();
  if (!token) return null;
  try {
    return await getStats(token);
  } catch {
    return null;
  }
}
