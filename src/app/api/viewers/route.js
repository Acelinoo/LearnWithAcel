import { NextResponse } from "next/server";
import fs from "node:fs/promises";
import path from "node:path";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

// Satu counter bersama untuk seluruh platform.
// Disimpan di file .data/viewers.json di server (bekerja di dev / VPS).
// Saat di-deploy ke Vercel (serverless readonly), fallback ke memory:
// counter tetap naik selama instance aktif, bisa reset saat cold start.
// Untuk persistence yang benar-benar permanen di produksi, pakai
// Vercel KV / Upstash Redis / database kecil.

const DATA_DIR = path.join(process.cwd(), ".data");
const DATA_FILE = path.join(DATA_DIR, "viewers.json");

let memoryCount = 0;
let loaded = false;

async function ensureLoaded() {
  if (loaded) return;
  try {
    const raw = await fs.readFile(DATA_FILE, "utf8");
    const parsed = JSON.parse(raw);
    if (typeof parsed.count === "number" && parsed.count >= 0) {
      memoryCount = parsed.count;
    }
  } catch {
    // file belum ada atau tidak bisa dibaca → mulai dari 0
    memoryCount = 0;
  }
  loaded = true;
}

async function persist() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true });
    await fs.writeFile(
      DATA_FILE,
      JSON.stringify({ count: memoryCount }, null, 2),
      "utf8"
    );
  } catch {
    // readonly fs (mis. serverless) — lanjutkan dengan in-memory saja
  }
}

export async function GET() {
  await ensureLoaded();
  return NextResponse.json({ count: memoryCount });
}

export async function POST() {
  await ensureLoaded();
  memoryCount += 1;
  await persist();
  return NextResponse.json({ count: memoryCount });
}
