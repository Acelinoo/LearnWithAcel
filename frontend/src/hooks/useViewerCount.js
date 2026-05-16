"use client";

import { useEffect, useState } from "react";

// Satu counter bersama yang disimpan di server lewat /api/viewers.
// Semua badge viewer menampilkan: seed + sharedCount.
// Karena datanya dari server, Chrome, Edge, Firefox, dan device lain
// akan melihat angka yang sama.

const GLOBAL_BASE = 1000;
const REFRESH_INTERVAL_MS = 15000; // poll ringan supaya update dari browser lain ikut terlihat

let currentCount = 0;
let fetched = false;
let inflight = null;
const listeners = new Set();

function notify() {
  for (const l of listeners) l(currentCount);
}

function setCount(next) {
  if (typeof next !== "number" || next < 0) return;
  currentCount = next;
  fetched = true;
  notify();
}

async function fetchCount() {
  if (inflight) return inflight;
  inflight = (async () => {
    try {
      const res = await fetch("/api/viewers", { cache: "no-store" });
      if (res.ok) {
        const json = await res.json();
        if (typeof json.count === "number") setCount(json.count);
      }
    } catch {
      // abaikan error jaringan, angka kembali ke seed
    } finally {
      inflight = null;
    }
  })();
  return inflight;
}

export async function bumpSharedAccess() {
  try {
    const res = await fetch("/api/viewers", { method: "POST" });
    if (res.ok) {
      const json = await res.json();
      if (typeof json.count === "number") setCount(json.count);
    }
  } catch {
    // offline? abaikan
  }
}

/**
 * Hook utama untuk semua badge viewer.
 * Nilai yang ditampilkan = seed + sharedCount dari server.
 */
export function useSharedAccessCount(seed = 0) {
  const [value, setValue] = useState(seed);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const onChange = (v) => {
      setValue(seed + v);
      setReady(true);
    };
    listeners.add(onChange);

    // Reflect nilai saat ini jika sudah pernah difetch
    if (fetched) {
      setValue(seed + currentCount);
      setReady(true);
    } else {
      fetchCount();
    }

    // Re-fetch saat tab kembali aktif supaya update dari browser lain terlihat
    const onVisible = () => {
      if (document.visibilityState === "visible") fetchCount();
    };
    document.addEventListener("visibilitychange", onVisible);
    window.addEventListener("focus", fetchCount);

    // Polling ringan supaya angka tetap segar saat tab dibiarkan terbuka
    const id = setInterval(fetchCount, REFRESH_INTERVAL_MS);

    return () => {
      listeners.delete(onChange);
      document.removeEventListener("visibilitychange", onVisible);
      window.removeEventListener("focus", fetchCount);
      clearInterval(id);
    };
  }, [seed]);

  return { count: value, ready };
}

// Wrappers — nama tetap supaya komponen lama tidak perlu berubah.
export const useViewerCount = () => useSharedAccessCount(GLOBAL_BASE);
export const useViewerCountReadOnly = () => useSharedAccessCount(GLOBAL_BASE);
export const useLessonViewerCount = (_key, seed) =>
  useSharedAccessCount(seed);
export const useLevelViewerCount = (_slug, seed) => useSharedAccessCount(seed);
export const useStoredCount = (_key, seed) => useSharedAccessCount(seed);
