"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import { useRouter } from "next/navigation";
import { getMe, type ApiUser } from "@/lib/api/auth";
import {
  clearClientToken,
  getClientToken,
  setClientToken,
} from "@/lib/auth/token";

type AuthContextValue = {
  user: ApiUser | null;
  token: string | null;
  loading: boolean;
  setSession: (token: string, user?: ApiUser | null) => Promise<void>;
  refresh: () => Promise<void>;
  signOut: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({
  children,
  initialUser = null,
}: {
  children: ReactNode;
  initialUser?: ApiUser | null;
}) {
  const router = useRouter();
  const [user, setUser] = useState<ApiUser | null>(initialUser);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(!initialUser);

  // Hydrate token + verify on mount.
  useEffect(() => {
    let cancelled = false;
    const t = getClientToken();
    if (!t) {
      setLoading(false);
      return;
    }
    setToken(t);

    if (initialUser) {
      // SSR already validated the user, no extra round-trip needed.
      setLoading(false);
      return;
    }

    (async () => {
      try {
        const me = await getMe(t);
        if (!cancelled) {
          setUser(me);
        }
      } catch {
        if (!cancelled) {
          clearClientToken();
          setToken(null);
          setUser(null);
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [initialUser]);

  const setSession = useCallback(
    async (nextToken: string, nextUser: ApiUser | null = null) => {
      setClientToken(nextToken);
      setToken(nextToken);
      try {
        const me = nextUser ?? (await getMe(nextToken));
        setUser(me);
      } catch {
        setUser(nextUser);
      }
      setLoading(false);
      router.refresh();
    },
    [router]
  );

  const refresh = useCallback(async () => {
    const t = getClientToken();
    if (!t) {
      setUser(null);
      setToken(null);
      return;
    }
    try {
      const me = await getMe(t);
      setToken(t);
      setUser(me);
    } catch {
      clearClientToken();
      setToken(null);
      setUser(null);
    }
  }, []);

  const signOut = useCallback(async () => {
    clearClientToken();
    setToken(null);
    setUser(null);
    router.replace("/login");
    router.refresh();
  }, [router]);

  const value = useMemo<AuthContextValue>(
    () => ({ user, token, loading, setSession, refresh, signOut }),
    [user, token, loading, setSession, refresh, signOut]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within <AuthProvider>");
  return ctx;
}
