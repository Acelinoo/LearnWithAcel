/**
 * Auth token storage. The JWT lives in a cookie so it can be read on both
 * the server (via next/headers cookies()) and the client.
 *
 * The cookie is NOT HttpOnly because the browser-side fetch needs to attach
 * it to backend requests as a Bearer token. The cookie is `SameSite=Lax`,
 * `Secure` in production, and expires after 24h to mirror the backend JWT.
 */

export const TOKEN_COOKIE = "lwa_token";
export const TOKEN_MAX_AGE_SECONDS = 60 * 60 * 24; // 24h

/* ------------------------------------------------------------------ */
/* Client-side helpers                                                 */
/* ------------------------------------------------------------------ */

export function getClientToken(): string | null {
  if (typeof document === "undefined") return null;
  const match = document.cookie
    .split("; ")
    .find((c) => c.startsWith(`${TOKEN_COOKIE}=`));
  return match ? decodeURIComponent(match.split("=").slice(1).join("=")) : null;
}

export function setClientToken(token: string) {
  if (typeof document === "undefined") return;
  const secure = location.protocol === "https:" ? "; Secure" : "";
  document.cookie = `${TOKEN_COOKIE}=${encodeURIComponent(
    token
  )}; Path=/; Max-Age=${TOKEN_MAX_AGE_SECONDS}; SameSite=Lax${secure}`;
}

export function clearClientToken() {
  if (typeof document === "undefined") return;
  document.cookie = `${TOKEN_COOKIE}=; Path=/; Max-Age=0; SameSite=Lax`;
}
