"use client";

import { useEffect } from "react";
import { usePathname } from "next/navigation";
import { bumpSharedAccess } from "@/hooks/useViewerCount";

/**
 * Bump shared viewer counter (server-side) sekali per pathname per session.
 * Dipasang di root layout sehingga semua halaman memicu kenaikan counter yang sama.
 */
export default function AccessBumper() {
  const pathname = usePathname();

  useEffect(() => {
    if (!pathname) return;
    const sessionKey = `lwa_seen_${pathname}`;
    try {
      if (sessionStorage.getItem(sessionKey)) return;
      sessionStorage.setItem(sessionKey, "1");
    } catch {
      // sessionStorage tidak tersedia (mis. privacy mode) — lanjutkan saja
    }
    bumpSharedAccess();
  }, [pathname]);

  return null;
}
