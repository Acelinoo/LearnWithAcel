"""
Fullstack / Level 1 — Fullstack Beginner.

Lessons:
  1. frontend-backend-connection
  2. auth-dengan-jwt
  3. deploy-fullstack-app
  4. mini-project-note-taking-app  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Frontend + Backend Connection
# ─────────────────────────────────────────────────────────────────────────────

LESSON_CONNECTION = make_lesson(
    title="Frontend + Backend Connection",
    slug="frontend-backend-connection",
    order_index=1,
    read_time="14 menit",
    summary="CORS, fetch dari Next.js, environment variable, dan error handling.",
    tools=["Next.js project", "Backend API dari Backend Level 1", "Browser DevTools"],
    outcomes=[
        "Memahami CORS dan cara membukanya di backend",
        "Memanggil API dari Next.js dengan environment variable",
        "Menampilkan loading state dan error state",
    ],
    tldr=(
        "Frontend dan backend lari di port berbeda → browser blokir (CORS). "
        "Buka dengan middleware `cors()` di backend. Simpan URL API di "
        "`.env.local` lewat `NEXT_PUBLIC_API_URL`. Selalu handle loading & "
        "error state."
    ),
    pembuka=dedent(
        """\
        Sekarang kamu sudah punya frontend (Next.js) dan backend (Express + Prisma). Saatnya menyambungkan keduanya.

        Pekerjaan ini terlihat sederhana: panggil API dari frontend. Tapi ada beberapa jebakan yang sering bikin pemula menyerah di langkah ini.

        Kita bedah satu per satu: CORS, environment variable, dan UX state yang sopan.
        """
    ),
    penjelasan=dedent(
        """\
        ### Kenapa ada masalah CORS

        Browser punya aturan keamanan: **same-origin policy**. Default-nya, JavaScript di domain A tidak boleh panggil API di domain B.

        Saat kamu develop:

        - Frontend Next.js: `http://localhost:3000`.
        - Backend Express: `http://localhost:3001`.

        Beda port = beda origin. Browser blokir.

        Solusinya: backend kasih izin eksplisit lewat **CORS** (Cross-Origin Resource Sharing).

        ### Buka CORS di backend

        Di Express:

        ```js
        import cors from "cors";
        app.use(cors({
          origin: "http://localhost:3000", // atau ["http://localhost:3000", "https://app.com"]
          credentials: true,
        }));
        ```

        Di FastAPI:

        ```py
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        ```

        Wildcard `*` mudah, tapi tidak aman untuk production. Selalu sebut origin yang spesifik.

        ### Environment variable di Next.js

        Jangan hardcode URL API. Ganti URL antar dev / staging / production lewat `.env.local`.

        ```bash
        # Frontend/.env.local
        NEXT_PUBLIC_API_URL=http://localhost:3001/api
        ```

        Aturan penting di Next.js:

        - Variabel yang aman dipakai di browser HARUS punya prefix `NEXT_PUBLIC_`.
        - Variabel TANPA prefix cuma boleh diakses dari server component / API route. Jangan untuk SECRET KEY.

        ### Pola fetch yang sopan

        Tampilan harus paham tiga keadaan: loading, sukses, error.

        ```jsx
        "use client";

        import { useEffect, useState } from "react";

        export default function BookList() {
          const [books, setBooks] = useState([]);
          const [loading, setLoading] = useState(true);
          const [error, setError] = useState(null);

          useEffect(() => {
            async function load() {
              try {
                const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books`);
                if (!res.ok) throw new Error("Gagal ambil data");
                const data = await res.json();
                setBooks(data);
              } catch (err) {
                setError(err.message);
              } finally {
                setLoading(false);
              }
            }
            load();
          }, []);

          if (loading) return <p>Memuat…</p>;
          if (error) return <p className="text-red-500">{error}</p>;
          return (
            <ul>
              {books.map((b) => <li key={b.id}>{b.title}</li>)}
            </ul>
          );
        }
        ```

        Pola ini muncul berulang. Banyak orang memilih library seperti TanStack Query atau SWR untuk menghindari boilerplate ini di project besar.

        ### Server vs Client component (Next.js App Router)

        Default component di App Router adalah **Server Component**. Tidak bisa pakai `useState`/`useEffect`.

        Untuk component yang butuh state atau event handler, kasih `"use client"` di baris pertama file.

        Praktik umum:

        - Page (server) fetch data → render Client component dengan data sebagai prop.
        - Client component handle interaksi (form, button, animasi).

        Kelebihannya: data fetch bisa di server (lebih cepat, tidak perlu loading state di browser), interaksi tetap di client.
        """
    ),
    contoh_code_md=dedent(
        """\
        Hybrid: page server-side fetch + client component buat interaksi.

        ```jsx
        // app/books/page.jsx (Server Component, default)
        import BookList from "./BookList";

        async function getBooks() {
          const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books`, {
            cache: "no-store",
          });
          if (!res.ok) throw new Error("Gagal ambil data");
          return res.json();
        }

        export default async function BooksPage() {
          const books = await getBooks();
          return (
            <main>
              <h1>Daftar Buku</h1>
              <BookList initialBooks={books} />
            </main>
          );
        }
        ```

        ```jsx
        // app/books/BookList.jsx (Client Component)
        "use client";

        import { useState } from "react";

        export default function BookList({ initialBooks }) {
          const [books] = useState(initialBooks);

          return (
            <ul>
              {books.map((b) => (
                <li key={b.id}>
                  <strong>{b.title}</strong> — {b.author}
                </li>
              ))}
            </ul>
          );
        }
        ```
        """
    ),
    practice=(
        "Hubungkan Next.js project kamu ke API books dari Backend Level 1. "
        "Buat halaman `/books` yang menampilkan daftar buku dari API. "
        "Tampilkan loading state saat fetch dan error message kalau API mati."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            // .env.local
            API_URL=http://localhost:3001/api

            // Frontend code
            const res = await fetch(`${process.env.API_URL}/books`);
            const books = await res.json();
            console.log(books);
            """
        ),
        "hint": "Variable env tidak terbaca di browser. Cek konvensi Next.js untuk env yang dipakai di client.",
        "answer_explanation": dedent(
            """\
            Kesalahan: `process.env.API_URL` di Next.js client tidak akan terbaca. Aturan Next.js:

            - Env tanpa prefix `NEXT_PUBLIC_` cuma tersedia di server component / API route.
            - Untuk dipakai di browser/client component, prefix WAJIB `NEXT_PUBLIC_`.

            Setelah rename, restart `npm run dev` supaya env di-reload.
            """
        ),
        "fixed_code": dedent(
            """\
            // .env.local
            NEXT_PUBLIC_API_URL=http://localhost:3001/api

            // Frontend code
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books`);
            const books = await res.json();
            console.log(books);
            """
        ),
    },
    quiz=[
        q(
            "Apa penyebab error CORS saat develop frontend dan backend lokal?",
            [
                "Internet mati",
                "Frontend dan backend di port berbeda → beda origin → browser blokir",
                "Code typo",
                "Database error",
            ],
            "B",
            "Browser blokir cross-origin request demi keamanan. Backend harus kasih izin eksplisit lewat CORS.",
        ),
        q(
            "Mana praktik yang BAIK untuk URL API di Next.js?",
            [
                "Hardcode `http://localhost:3001` di komponen",
                "Simpan di `.env.local` dengan prefix `NEXT_PUBLIC_API_URL`",
                "Simpan di `localStorage`",
                "Simpan di global window object",
            ],
            "B",
            "Env variable membuat URL bisa diganti antar dev/staging/prod tanpa edit kode. Prefix `NEXT_PUBLIC_` agar bisa diakses di browser.",
        ),
        q(
            "Kapan kamu butuh `\"use client\"` di Next.js App Router?",
            [
                "Selalu di setiap component",
                "Saat component butuh `useState`, `useEffect`, atau event handler",
                "Saat component berisi gambar",
                "Saat component pakai Tailwind",
            ],
            "B",
            "Server Component default tidak bisa pakai hooks atau event handler. Tambah `\"use client\"` saat component perlu interaktivitas.",
        ),
        q(
            "Mana yang HARUS di-handle saat fetch data?",
            [
                "Cuma success state",
                "Loading, success, dan error state",
                "Cuma error state",
                "Tidak perlu state",
            ],
            "B",
            "User experience yang baik: kasih tahu data sedang dimuat, atau kalau ada error. Tampilan kosong tanpa context bikin user bingung.",
        ),
        q(
            "Apa beda `cache: \"no-store\"` di fetch Next.js?",
            [
                "Performance lebih buruk selalu",
                "Memastikan data selalu fresh, tidak di-cache. Cocok untuk data yang sering berubah.",
                "Mengaktifkan offline mode",
                "Tidak ada bedanya",
            ],
            "B",
            "Default Next.js men-cache hasil fetch di server. `no-store` matikan cache — data selalu fresh tiap request.",
        ),
    ],
    common_mistakes=[
        "Lupa prefix `NEXT_PUBLIC_` untuk env yang dipakai di browser. `process.env.X` jadi `undefined`.",
        "Wildcard CORS `*` di production. Berbahaya — sebut origin spesifik.",
        "Tidak restart `npm run dev` setelah edit `.env.local`. Env tidak ter-reload.",
    ],
    checkpoint=[
        "Bisa jelaskan kenapa CORS error muncul.",
        "Bisa setup env variable di Next.js dengan prefix yang benar.",
        "Bisa fetch data dari API di server component dan client component.",
        "Selalu handle loading dan error state.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Auth dengan JWT
# ─────────────────────────────────────────────────────────────────────────────

LESSON_AUTH = make_lesson(
    title="Auth Dasar dengan JWT",
    slug="auth-dengan-jwt",
    order_index=2,
    read_time="16 menit",
    summary="Authentication, authorization, JWT, dan protected routes.",
    tools=["Backend Express + Prisma", "Library jsonwebtoken + bcryptjs", "Next.js"],
    outcomes=[
        "Membedakan authentication vs authorization",
        "Memahami cara kerja JWT dengan analogi nyata",
        "Membangun endpoint register/login dan protected route",
    ],
    tldr=(
        "Authentication = ngecek siapa kamu. Authorization = ngecek apa yang "
        "boleh kamu lakukan. JWT = kartu akses yang server keluarkan setelah "
        "login. Selalu hash password sebelum simpan."
    ),
    pembuka=dedent(
        """\
        App tanpa auth = pintu rumah tanpa kunci. Siapa saja bisa masuk dan ngacak-acak.

        Auth itu fitur yang hampir setiap app butuhkan. Untungnya, polanya sangat seragam.

        Lesson ini bahas dengan analogi konkrit, lalu langsung implementasi.
        """
    ),
    penjelasan=dedent(
        """\
        ### Authentication vs Authorization

        Sering dianggap sama, padahal beda:

        - **Authentication (AuthN)** — "Siapa kamu?". Verifikasi identitas via email + password.
        - **Authorization (AuthZ)** — "Apa yang boleh kamu lakukan?". Cek role/permission.

        Login = AuthN. Cek `is_admin` sebelum hapus user = AuthZ.

        ### JWT — kartu akses gedung

        Bayangkan kamu masuk gedung kantor:

        - **Hari pertama:** kasih KTP ke resepsionis. Resepsionis bikin **kartu akses** dengan foto kamu, nomor lantai yang boleh dibuka, dan tanggal kadaluarsa. Kasih ke kamu.
        - **Hari berikutnya:** tap kartu, sensor cek apakah kartu ini valid (tanda tangan resepsionis ada). Kalau ya, pintu buka. Tidak perlu nunjukin KTP lagi.

        JWT (JSON Web Token) bekerja seperti kartu akses itu:

        1. User login dengan email + password.
        2. Server verifikasi.
        3. Server bikin token yang berisi user id + tanda tangan rahasia.
        4. Frontend simpan token, kirim di header tiap request berikutnya.
        5. Server cek tanda tangan token. Kalau valid, request lanjut.

        ### Anatomi JWT

        Token JWT terlihat seperti string tiga bagian dipisah titik:

        ```text
        eyJhbGciOiJIUzI1NiIsI...   . eyJzdWIiOiJ1MTIiLCJpYXQiOj...   . dBjftJeZ4CVPmB92K27uhbUJU1...
        ─────  HEADER  ─────       ─────  PAYLOAD  ─────              ────  SIGNATURE  ────
        ```

        - **Header.** Algoritma + tipe token.
        - **Payload.** Data user (id, role, expire). Bisa di-decode oleh siapa pun, **jangan simpan password atau secret di sini.**
        - **Signature.** Hasil tanda tangan dengan secret server. Ini yang verifikasi keaslian.

        Kalau payload diubah orang, signature jadi tidak match. Server tolak.

        ### Hash password — wajib

        **Jangan PERNAH simpan password plain text di database.** Pakai `bcryptjs`:

        ```js
        import bcrypt from "bcryptjs";

        // Saat register
        const hash = await bcrypt.hash(password, 10);
        await prisma.user.create({ data: { email, hashed_password: hash } });

        // Saat login
        const user = await prisma.user.findUnique({ where: { email } });
        const ok = await bcrypt.compare(password, user.hashed_password);
        if (!ok) return res.status(401).json({ detail: "Email atau password salah" });
        ```

        Bcrypt itu satu arah: kamu bisa hash password jadi string acak, tapi tidak bisa balik dari string acak ke password asli. Saat login, kamu bandingkan hash baru vs hash di database.

        ### Endpoint auth standar

        ```text
        POST /api/auth/register   → bikin user baru
        POST /api/auth/login      → balas { access_token, user }
        GET  /api/auth/me         → ambil profil user yang lagi login (butuh token)
        ```

        ### Protected route — middleware

        Endpoint yang butuh login dilindungi middleware:

        ```js
        function authRequired(req, res, next) {
          const auth = req.headers.authorization;          // "Bearer <token>"
          if (!auth) return res.status(401).json({ detail: "Token tidak ada" });

          const token = auth.split(" ")[1];
          try {
            const payload = jwt.verify(token, process.env.JWT_SECRET);
            req.userId = payload.sub;                       // simpan untuk handler
            next();
          } catch {
            return res.status(401).json({ detail: "Token tidak valid" });
          }
        }

        app.get("/api/auth/me", authRequired, async (req, res) => {
          const user = await prisma.user.findUnique({ where: { id: req.userId } });
          res.json(user);
        });
        ```

        ### Frontend — simpan token di mana?

        Dua pilihan utama:

        - **httpOnly cookie.** Aman dari XSS, browser otomatis kirim. Butuh setup CORS dengan `credentials: true`.
        - **localStorage.** Mudah, tapi bisa dibaca script jahat (XSS). Hanya untuk app personal/belajar.

        Untuk production, **selalu pilih httpOnly cookie**.
        """
    ),
    contoh_code_md=dedent(
        """\
        Endpoint register dan login lengkap:

        ```js
        // src/routes/auth.js
        import { Router } from "express";
        import bcrypt from "bcryptjs";
        import jwt from "jsonwebtoken";
        import { PrismaClient } from "@prisma/client";

        const prisma = new PrismaClient();
        const router = Router();

        router.post("/register", async (req, res) => {
          const { email, password, full_name } = req.body;
          if (!email || !password) {
            return res.status(400).json({ detail: "Email dan password wajib" });
          }

          const exists = await prisma.user.findUnique({ where: { email } });
          if (exists) {
            return res.status(409).json({ detail: "Email sudah terdaftar" });
          }

          const hashed = await bcrypt.hash(password, 10);
          const user = await prisma.user.create({
            data: { email, hashed_password: hashed, full_name },
          });

          // Kembalikan profil tanpa password
          const { hashed_password, ...safe } = user;
          res.status(201).json(safe);
        });

        router.post("/login", async (req, res) => {
          const { email, password } = req.body;

          const user = await prisma.user.findUnique({ where: { email } });
          if (!user) {
            return res.status(401).json({ detail: "Email atau password salah" });
          }

          const ok = await bcrypt.compare(password, user.hashed_password);
          if (!ok) {
            return res.status(401).json({ detail: "Email atau password salah" });
          }

          const token = jwt.sign(
            { sub: user.id },
            process.env.JWT_SECRET,
            { expiresIn: "24h" },
          );

          res.json({ access_token: token, token_type: "Bearer" });
        });

        export default router;
        ```
        """
    ),
    practice=(
        "Tambahkan `User` model di Prisma schema (id, email, hashed_password, "
        "full_name). Push schema. Bikin endpoint `/auth/register` dan "
        "`/auth/login`. Test dengan Postman: register user baru, lalu login "
        "dengan password yang benar dan salah."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            router.post("/register", async (req, res) => {
              const { email, password } = req.body;

              const user = await prisma.user.create({
                data: { email, password },
              });

              const token = jwt.sign({ user, password }, "rahasia");

              res.json({ token });
            });
            """
        ),
        "hint": "Tiga masalah keamanan serius. Cek penyimpanan password, isi token, dan secret yang dipakai.",
        "answer_explanation": dedent(
            """\
            1. Password disimpan plain text. WAJIB di-hash dulu pakai bcrypt sebelum masuk database.
            2. JWT payload berisi password. Payload bisa di-decode siapa pun — never put secrets in JWT.
            3. Secret `"rahasia"` hardcoded dan lemah. Pakai env variable yang panjang dan random (`JWT_SECRET`).
            """
        ),
        "fixed_code": dedent(
            """\
            router.post("/register", async (req, res) => {
              const { email, password, full_name } = req.body;
              if (!email || !password) {
                return res.status(400).json({ detail: "Email dan password wajib" });
              }

              const hashed = await bcrypt.hash(password, 10);
              const user = await prisma.user.create({
                data: { email, hashed_password: hashed, full_name },
              });

              // Token cuma berisi user id, bukan password
              const token = jwt.sign(
                { sub: user.id },
                process.env.JWT_SECRET,
                { expiresIn: "24h" },
              );

              res.status(201).json({ access_token: token });
            });
            """
        ),
    },
    quiz=[
        q(
            "Apa beda authentication dengan authorization?",
            [
                "Sama saja",
                "Authentication = siapa kamu, Authorization = apa yang boleh kamu lakukan",
                "Authentication lebih cepat",
                "Authorization untuk admin saja",
            ],
            "B",
            "Login = AuthN. Cek role / permission = AuthZ. Dua hal berbeda yang sering dianggap sama.",
        ),
        q(
            "Apa yang HARUS dilakukan sebelum simpan password ke database?",
            [
                "Encode dengan base64",
                "Hash dengan bcrypt (atau argon2/scrypt)",
                "Encrypt dengan AES",
                "Tidak perlu, simpan langsung",
            ],
            "B",
            "Bcrypt one-way hash. Database tidak akan pernah tahu password aslinya — bahkan kalau bocor pun.",
        ),
        q(
            "Apa yang AMAN disimpan di payload JWT?",
            [
                "Password user",
                "User id, role, expiration",
                "Credit card",
                "Database password",
            ],
            "B",
            "Payload JWT bisa di-decode siapa pun. Cuma simpan info yang tidak rahasia. Password atau secret jangan pernah masuk JWT.",
        ),
        q(
            "Apa fungsi signature di JWT?",
            [
                "Untuk encryption payload",
                "Memastikan payload tidak diubah — kalau diubah, signature tidak match dan token ditolak",
                "Untuk performance",
                "Tidak ada fungsi",
            ],
            "B",
            "Signature dihasilkan dengan secret server. Server pegang secret, jadi cuma server yang bisa bikin token valid.",
        ),
        q(
            "Mana cara penyimpanan token yang LEBIH AMAN di production?",
            [
                "localStorage",
                "Variable JavaScript biasa",
                "httpOnly cookie",
                "URL parameter",
            ],
            "C",
            "httpOnly cookie tidak bisa diakses JavaScript, jadi aman dari XSS. localStorage rentan kalau ada script jahat.",
        ),
    ],
    common_mistakes=[
        "Simpan password plain text. Bocor sekali, semua user kena.",
        "Hardcode JWT_SECRET di kode. Gampang bocor saat repo public.",
        "Pesan error spesifik 'email tidak terdaftar'. Lebih aman 'email atau password salah' supaya attacker tidak bisa enumerate user.",
    ],
    checkpoint=[
        "Bisa jelaskan beda AuthN vs AuthZ.",
        "Bisa hash password dengan bcrypt.",
        "Bisa generate dan verifikasi JWT.",
        "Bisa bikin protected route dengan middleware.",
    ],
    xp_reward=200,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Deploy Fullstack App
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DEPLOY = make_lesson(
    title="Deploy Fullstack App",
    slug="deploy-fullstack-app",
    order_index=3,
    read_time="13 menit",
    summary="Database di Supabase, backend di Railway, frontend di Vercel.",
    tools=["Supabase", "Railway atau Render", "Vercel", "GitHub"],
    outcomes=[
        "Setup PostgreSQL di Supabase",
        "Deploy backend Express ke Railway",
        "Deploy frontend Next.js ke Vercel",
        "Hubungkan ketiganya dengan environment variable",
    ],
    tldr=(
        "Database di Supabase (gratis). Backend di Railway/Render (gratis "
        "dengan limit). Frontend di Vercel (gratis untuk hobi). Hubungkan "
        "lewat env variable. Total waktu setup: ~1 jam."
    ),
    pembuka=dedent(
        """\
        Bikin app di lokal itu gampang. Bikin app yang bisa diakses orang lain dari HP mereka, itu beda cerita.

        Untungnya 2026 punya banyak free tier. Ekosistem Vercel + Railway + Supabase membuat deploy fullstack hampir tanpa hambatan.

        Lesson ini langkah-langkah konkrit: dari nol sampai URL publik yang bisa dibagikan.
        """
    ),
    penjelasan=dedent(
        """\
        ### Arsitektur deploy

        Tiga layanan yang akan kita pakai:

        - **Supabase** — PostgreSQL hosted. Free tier cukup besar untuk hobi.
        - **Railway** atau **Render** — hosting untuk backend Node.js. Free tier 500 jam/bulan.
        - **Vercel** — hosting untuk frontend Next.js. Free tier sangat generous.

        Alurnya: frontend (Vercel) → API request → backend (Railway) → query → database (Supabase).

        ### Step 1 — Database di Supabase

        - Buka [supabase.com](https://supabase.com), Sign up dengan GitHub.
        - **New Project** → kasih nama, password kuat untuk database, pilih region terdekat.
        - Tunggu sekitar 2 menit untuk provisioning.
        - Buka **Project Settings → Database → Connection string**. Salin URL connection.

        Ada dua format URL:
        - **Direct** (port 5432) — untuk migrations dan dev.
        - **Pooler** (port 6543) — untuk production runtime.

        Untuk Prisma + Railway, pakai **Pooler** (lebih scalable).

        ### Step 2 — Backend ke Railway

        - Push backend ke GitHub repo terpisah.
        - Buka [railway.app](https://railway.app) → Sign up dengan GitHub.
        - **New Project → Deploy from GitHub repo** → pilih repo backend.
        - Buka tab **Variables**, tambahkan:
          - `DATABASE_URL` = URL Supabase Pooler.
          - `JWT_SECRET` = string random panjang (`openssl rand -hex 32`).
          - `PORT` = `3001` (Railway override otomatis, tapi aman).
        - Tab **Settings → Networking → Generate Domain**. Kamu dapat URL `xxx.up.railway.app`.

        Build command: `npm install && npx prisma generate && npx prisma db push`.
        Start command: `node src/index.js` atau `npm start`.

        ### Step 3 — Frontend ke Vercel

        - Push frontend ke GitHub repo terpisah.
        - Buka [vercel.com/new](https://vercel.com/new) → import repo.
        - Tambahkan env variable:
          - `NEXT_PUBLIC_API_URL` = URL Railway dari step 2 (misal `https://xxx.up.railway.app/api`).
        - Klik **Deploy**.

        ### Step 4 — Update CORS di backend

        Di backend, CORS harus include domain Vercel:

        ```js
        app.use(cors({
          origin: [
            "http://localhost:3000",
            "https://your-app.vercel.app",
          ],
          credentials: true,
        }));
        ```

        Push lagi ke GitHub. Railway auto-redeploy.

        ### Custom domain (opsional)

        Vercel: Project → Settings → Domains → tambah domain kamu. Gratis SSL.

        Railway: serupa, di tab Networking.

        ### Tips

        - **Monorepo vs multi-repo.** Untuk pemula, lebih mudah multi-repo (frontend dan backend repo terpisah). Lebih jelas mana yang deploy ke mana.
        - **Logs.** Railway dan Vercel keduanya punya tab Logs. Selalu cek di sini saat deploy gagal.
        - **Free tier limit.** Railway free tier akan tidur kalau idle terlalu lama. Untuk demo OK, untuk produksi mungkin perlu paid plan.
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup script di `package.json` backend untuk Railway:

        ```json
        {
          "scripts": {
            "build": "prisma generate && prisma db push",
            "start": "node src/index.js",
            "dev": "nodemon src/index.js"
          }
        }
        ```

        Listen pada port yang Railway sediakan (env `PORT`):

        ```js
        // src/index.js
        const port = process.env.PORT || 3001;

        app.listen(port, () => {
          console.log(`API running on port ${port}`);
        });
        ```

        Frontend `.env.production` untuk override URL API saat di Vercel:

        ```bash
        NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app/api
        ```
        """
    ),
    practice=(
        "Deploy stack lengkap: backend dari Backend Level 1 ke Railway, "
        "frontend Next.js minimal ke Vercel, database di Supabase. Test "
        "fetch dari Vercel URL — pastikan CORS oke dan data muncul. Catat "
        "tiga URL ini di catatan kamu."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            // Backend src/index.js
            app.listen(3001, () => {
              console.log("API running on port 3001");
            });

            // Backend CORS
            app.use(cors({ origin: "http://localhost:3000" }));
            """
        ),
        "hint": "Dua masalah saat dideploy ke Railway: port hardcoded dan CORS terlalu sempit.",
        "answer_explanation": dedent(
            """\
            1. Railway override port via env `PORT`. Hardcode 3001 bikin Railway tidak bisa expose service-mu. Pakai `process.env.PORT || 3001`.
            2. CORS cuma izinkan `localhost:3000`. Saat frontend di Vercel, request akan diblokir. Tambah domain Vercel (atau pakai array origin).
            """
        ),
        "fixed_code": dedent(
            """\
            const port = process.env.PORT || 3001;
            app.listen(port, () => {
              console.log(`API running on port ${port}`);
            });

            const allowedOrigins = [
              "http://localhost:3000",
              "https://your-app.vercel.app",
            ];

            app.use(cors({
              origin: allowedOrigins,
              credentials: true,
            }));
            """
        ),
    },
    quiz=[
        q(
            "Mana kombinasi free tier yang umum untuk fullstack pemula?",
            [
                "AWS + DigitalOcean + Heroku",
                "Vercel + Railway + Supabase",
                "Netlify + Replit + MongoDB Atlas Enterprise",
                "Tidak ada yang gratis",
            ],
            "B",
            "Tiga ini punya free tier yang generous, ekosistem matang, dan deploy-nya gampang.",
        ),
        q(
            "Apa fungsi `process.env.PORT` saat deploy ke Railway?",
            [
                "Tidak ada",
                "Railway dynamically assign port lewat env. Harus di-respect, bukan hardcode.",
                "Cuma untuk dev",
                "Wajib 8080",
            ],
            "B",
            "Platform PaaS biasanya assign port dinamis. Kalau hardcode 3001, app kamu tidak bisa di-expose.",
        ),
        q(
            "Apa yang HARUS di-update di backend setelah deploy frontend ke Vercel?",
            [
                "Database schema",
                "CORS — tambahkan domain Vercel ke allowed origins",
                "Hash password",
                "Tidak perlu update",
            ],
            "B",
            "Frontend di Vercel adalah origin baru. Backend harus eksplisit izinkan, atau request akan diblokir browser.",
        ),
        q(
            "Mana praktik untuk JWT_SECRET di production?",
            [
                "Hardcode di kode supaya konsisten",
                "Generate string random panjang (`openssl rand -hex 32`) dan simpan sebagai env variable di platform deploy",
                "Pakai 'rahasia'",
                "Tidak perlu",
            ],
            "B",
            "Secret panjang dan unik melindungi token dari brute-force. Simpan di env, jangan commit ke repo.",
        ),
        q(
            "Apa yang biasanya menyebabkan deploy gagal?",
            [
                "Salah font",
                "Env variable kurang atau salah, build script salah, CORS belum update",
                "Logo terlalu besar",
                "Browser lambat",
            ],
            "B",
            "Tiga masalah klasik. Selalu cek logs di platform deploy untuk pesan error spesifik.",
        ),
    ],
    common_mistakes=[
        "Hardcode `localhost:3001` di frontend production. Tidak ada di production.",
        "Lupa tambah domain Vercel ke CORS origin. Browser blokir.",
        "Generate Supabase URL versi 'Direct' untuk app jangka panjang. Kadang lebih boros connection — pakai Pooler.",
    ],
    checkpoint=[
        "Database Supabase live dan bisa diakses dari Prisma.",
        "Backend deployed di Railway dengan env variable lengkap.",
        "Frontend deployed di Vercel dengan `NEXT_PUBLIC_API_URL` benar.",
        "End-to-end: bisa login dari URL Vercel, data tersimpan di Supabase.",
    ],
    xp_reward=180,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_NOTES = make_lesson(
    title="Mini Project — Note-Taking App dengan Auth",
    slug="mini-project-note-taking-app",
    order_index=4,
    read_time="180 menit",
    summary="Fullstack app: register/login + CRUD note + deploy ke production.",
    tools=["Next.js", "Express + Prisma", "Supabase", "Railway", "Vercel"],
    outcomes=[
        "Membangun fullstack app end-to-end",
        "Memakai JWT untuk session management",
        "Menerapkan owner-based authorization (note hanya bisa dilihat owner-nya)",
        "Deploy ke production dengan stack modern",
    ],
    tldr=(
        "Bangun note-taking app: auth + CRUD note per user + deploy. "
        "Setiap note milik user. User cuma bisa CRUD note miliknya sendiri. "
        "Deploy stack lengkap: Vercel + Railway + Supabase."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungkan semua yang dipelajari di level ini.

        Note-taking app sederhana, tapi mengandung pola produksi: auth, owner-based access, deploy ke tiga layanan.

        Selesai project ini, kamu sudah bisa bilang: "Saya bisa bikin fullstack app dari nol sampai live."
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        **Backend (Express + Prisma):**

        - `POST /auth/register` — bikin user baru.
        - `POST /auth/login` — balas access_token.
        - `GET /auth/me` — profil user (butuh token).
        - `GET /notes` — daftar note milik user yang login.
        - `POST /notes` — bikin note (owner = user yang login).
        - `PUT /notes/:id` — update note. Tolak kalau bukan owner.
        - `DELETE /notes/:id` — hapus note. Tolak kalau bukan owner.

        **Frontend (Next.js):**

        - `/register` — form register.
        - `/login` — form login. Saat sukses, simpan token, redirect ke `/notes`.
        - `/notes` — list note + form bikin baru. Protected (redirect ke login kalau belum auth).
        - `/notes/[id]` — detail + edit + delete note.

        **Database (Prisma schema):**

        ```prisma
        model User {
          id              String @id @default(uuid())
          email           String @unique
          full_name       String
          hashed_password String
          notes           Note[]
        }

        model Note {
          id        String   @id @default(uuid())
          title     String
          content   String
          user_id   String
          owner     User     @relation(fields: [user_id], references: [id], onDelete: Cascade)
          created_at DateTime @default(now())
        }
        ```

        ### Owner-based authorization

        Aturan: user A tidak boleh CRUD note milik user B. Tapi karena URL pakai ID, kalau cuma cek "user login = OK", user A bisa hapus note B dengan tahu ID-nya.

        Solusi: di tiap endpoint note, cek `note.user_id === req.userId`. Kalau tidak match, balas 403 Forbidden.

        ```js
        router.delete("/:id", authRequired, async (req, res) => {
          const note = await prisma.note.findUnique({ where: { id: req.params.id } });
          if (!note) return res.status(404).json({ detail: "Note tidak ditemukan" });
          if (note.user_id !== req.userId) {
            return res.status(403).json({ detail: "Bukan note kamu" });
          }
          await prisma.note.delete({ where: { id: note.id } });
          res.status(204).send();
        });
        ```

        Atau lebih ringkas — query langsung dengan filter user_id:

        ```js
        const note = await prisma.note.findFirst({
          where: { id: req.params.id, user_id: req.userId },
        });
        if (!note) return res.status(404).json({ detail: "Note tidak ditemukan" });
        ```

        ### Frontend protected page

        ```jsx
        // app/notes/page.jsx
        "use client";

        import { useEffect, useState } from "react";
        import { useRouter } from "next/navigation";

        export default function NotesPage() {
          const router = useRouter();
          const [notes, setNotes] = useState([]);

          useEffect(() => {
            const token = localStorage.getItem("token");
            if (!token) {
              router.push("/login");
              return;
            }

            fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes`, {
              headers: { Authorization: `Bearer ${token}` },
            })
              .then((r) => {
                if (r.status === 401) {
                  localStorage.removeItem("token");
                  router.push("/login");
                  return [];
                }
                return r.json();
              })
              .then(setNotes);
          }, [router]);

          return (
            <main>
              <h1>Notes saya</h1>
              <ul>
                {notes.map((n) => (
                  <li key={n.id}>{n.title}</li>
                ))}
              </ul>
            </main>
          );
        }
        ```

        Catatan: localStorage dipakai di sini untuk kesederhanaan. Untuk production sungguhan, ganti ke httpOnly cookie.

        ### Submit

        Live di Vercel (frontend) + Railway (backend) + Supabase (DB). Bagikan URL. Ajak teman bikin akun. Pastikan note-nya tidak saling terlihat.
        """
    ),
    contoh_code_md=dedent(
        """\
        Endpoint create note dengan auth dan ownership:

        ```js
        // src/routes/notes.js
        import { Router } from "express";
        import { PrismaClient } from "@prisma/client";
        import authRequired from "../middleware/authRequired.js";

        const prisma = new PrismaClient();
        const router = Router();

        router.use(authRequired);

        // GET /notes — list note milik user yang login
        router.get("/", async (req, res) => {
          const notes = await prisma.note.findMany({
            where: { user_id: req.userId },
            orderBy: { created_at: "desc" },
          });
          res.json(notes);
        });

        // POST /notes
        router.post("/", async (req, res) => {
          const { title, content } = req.body;
          if (!title) return res.status(400).json({ detail: "Title wajib" });

          const note = await prisma.note.create({
            data: { title, content: content || "", user_id: req.userId },
          });
          res.status(201).json(note);
        });

        // PUT /notes/:id
        router.put("/:id", async (req, res) => {
          const note = await prisma.note.findFirst({
            where: { id: req.params.id, user_id: req.userId },
          });
          if (!note) return res.status(404).json({ detail: "Note tidak ditemukan" });

          const updated = await prisma.note.update({
            where: { id: note.id },
            data: req.body,
          });
          res.json(updated);
        });

        // DELETE /notes/:id
        router.delete("/:id", async (req, res) => {
          const note = await prisma.note.findFirst({
            where: { id: req.params.id, user_id: req.userId },
          });
          if (!note) return res.status(404).json({ detail: "Note tidak ditemukan" });

          await prisma.note.delete({ where: { id: note.id } });
          res.status(204).send();
        });

        export default router;
        ```
        """
    ),
    practice=(
        "Bangun stack lengkap sesuai spec. Test owner authorization: bikin "
        "dua akun, login akun A, coba akses note milik akun B dengan ID-nya "
        "secara langsung — harus dapat 404. Selesai itu, deploy semua dan "
        "bagikan URL ke teman."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            router.delete("/:id", authRequired, async (req, res) => {
              await prisma.note.delete({
                where: { id: req.params.id },
              });
              res.status(204).send();
            });
            """
        ),
        "hint": "Endpoint ini punya celah keamanan besar. User bisa hapus note milik orang lain.",
        "answer_explanation": dedent(
            """\
            Kesalahan: cuma cek user login, tapi tidak cek ownership note.

            User A login → tahu ID note milik user B → DELETE → terhapus. Itu vulnerability.

            Solusi: filter berdasarkan owner. Pakai `findFirst` dengan `user_id: req.userId` untuk verifikasi ownership sebelum delete.
            """
        ),
        "fixed_code": dedent(
            """\
            router.delete("/:id", authRequired, async (req, res) => {
              const note = await prisma.note.findFirst({
                where: { id: req.params.id, user_id: req.userId },
              });
              if (!note) {
                return res.status(404).json({ detail: "Note tidak ditemukan" });
              }
              await prisma.note.delete({ where: { id: note.id } });
              res.status(204).send();
            });
            """
        ),
    },
    quiz=[
        q(
            "Mengapa endpoint delete note WAJIB cek ownership, bukan cuma auth?",
            [
                "Untuk performance",
                "Auth cuma cek user login. Tanpa cek owner, user bisa delete note milik orang lain dengan tahu ID-nya.",
                "Tidak perlu",
                "Untuk gaya",
            ],
            "B",
            "Authorization (cek hak akses ke resource spesifik) wajib selain authentication. Ini vulnerability nyata yang sering luput pemula.",
        ),
        q(
            "Status code yang TEPAT saat user A coba akses note milik user B?",
            [
                "200 OK",
                "401 Unauthorized",
                "404 Not Found atau 403 Forbidden",
                "500 Internal Server Error",
            ],
            "C",
            "Banyak yang pakai 404 supaya tidak bocorkan apakah ID itu valid atau tidak. 403 juga benar kalau ingin eksplisit.",
        ),
        q(
            "Apa fungsi `onDelete: Cascade` di Prisma schema?",
            [
                "Backup otomatis",
                "Saat parent (User) dihapus, semua child (Note) ikut terhapus",
                "Performance",
                "Tidak ada fungsi",
            ],
            "B",
            "Cascade penting untuk konsistensi. Note tanpa owner = orphan data.",
        ),
        q(
            "Mana cara filter note milik user yang sedang login di Prisma?",
            [
                "`findMany()` lalu filter di JavaScript",
                "`findMany({ where: { user_id: req.userId } })`",
                "`findUnique({ id: req.userId })`",
                "Tidak bisa filter",
            ],
            "B",
            "Filter di database lebih efisien daripada filter di kode. Bikin query selalu mengecualikan data milik user lain.",
        ),
        q(
            "Apa yang HARUS di-handle saat token expired di frontend?",
            [
                "Crash app",
                "Hapus token, redirect ke /login",
                "Loop request terus-menerus",
                "Tidak perlu di-handle",
            ],
            "B",
            "401 dari API berarti token tidak valid lagi. UX yang baik: bersihkan token lokal dan kirim user ke login.",
        ),
    ],
    common_mistakes=[
        "Cek auth tapi lupa cek ownership. Vulnerability.",
        "Tidak handle 401 di frontend. User stuck di halaman yang gagal load.",
        "Pesan error berbeda untuk 'note tidak ada' vs 'bukan milik kamu'. Bisa dipakai untuk ID enumeration. Pakai 404 sama untuk keduanya.",
    ],
    checkpoint=[
        "Stack lengkap deployed ke Vercel + Railway + Supabase.",
        "Auth flow lengkap: register, login, logout, protected page.",
        "Owner-based authorization: user A tidak bisa lihat note user B.",
        "URL publik bisa diakses dan dipakai dua akun berbeda secara terpisah.",
    ],
    xp_reward=600,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=1,
    slug="fullstack-beginner",
    title="Fullstack Beginner",
    subtitle="Dua sisi, satu aplikasi",
    description=(
        "Belajar menjahit frontend dan backend jadi satu aplikasi utuh. "
        "Auth, owner-based authorization, environment variable, dan deploy "
        "production stack: Vercel + Railway + Supabase."
    ),
    duration="~4 minggu",
    difficulty="Menengah",
    accent_color="from-indigo-400/30 to-violet-500/10",
    mini_project="Note-Taking App dengan Auth",
    tags=["Next.js", "Express", "Prisma", "JWT", "Deployment"],
    lessons=[LESSON_CONNECTION, LESSON_AUTH, LESSON_DEPLOY, PROJECT_NOTES],
)
