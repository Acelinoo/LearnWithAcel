import { NextResponse, type NextRequest } from "next/server";
import { TOKEN_COOKIE } from "@/lib/auth/token";

/**
 * Auth gate: protects /dashboard and /onboarding, and bounces logged-in
 * users away from /login + /register.
 *
 * We intentionally do NOT validate the JWT here — that costs a round-trip
 * to the backend on every navigation. Server components handle the actual
 * validation via getServerUser() and will send the user back to /login if
 * the token is stale.
 */
export function middleware(request: NextRequest) {
  const token = request.cookies.get(TOKEN_COOKIE)?.value ?? null;
  const { pathname } = request.nextUrl;

  const protectedPaths = ["/dashboard", "/onboarding"];
  const authPaths = ["/login", "/register"];

  const isProtected = protectedPaths.some((p) => pathname.startsWith(p));
  const isAuthPage = authPaths.some((p) => pathname.startsWith(p));

  if (!token && isProtected) {
    const redirectUrl = request.nextUrl.clone();
    redirectUrl.pathname = "/login";
    redirectUrl.searchParams.set("redirectTo", pathname);
    return NextResponse.redirect(redirectUrl);
  }

  if (token && isAuthPage) {
    if (request.nextUrl.searchParams.has("redirectTo")) {
      const response = NextResponse.next();
      response.cookies.delete(TOKEN_COOKIE);
      return response;
    }

    const redirectUrl = request.nextUrl.clone();
    redirectUrl.pathname = "/dashboard";
    redirectUrl.searchParams.delete("redirectTo");
    return NextResponse.redirect(redirectUrl);
  }

  const response = NextResponse.next();
  if (isAuthPage) {
    response.headers.set("Cache-Control", "no-store, max-age=0");
  }
  return response;
}

export const config = {
  matcher: [
    /*
     * Match all request paths except static files, images, and API
     * that doesn't need auth.
     */
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
