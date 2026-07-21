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
    title="Nyambungin Frontend sama Backend",
    slug="frontend-backend-connection",
    order_index=1,
    read_time="14 menit",
    summary="CORS, fetch dari Next.js, environment variable, sama error handling.",
    tools=["Next.js project", "Backend API dari Backend Level 1", "Browser DevTools"],
    outcomes=[
        "Paham CORS sama cara ngebukanya di backend",
        "Bisa manggil API dari Next.js pake environment variable",
        "Bisa nampilin loading state sama error state",
    ],
    tldr=(
        "Frontend sama backend jalan di port beda → browser blokir (CORS). "
        "Buka pake middleware `cors()` di backend. Simpen URL API di "
        "`.env.local` lewat `NEXT_PUBLIC_API_URL`. Selalu handle loading & "
        "error state."
    ),
    pembuka=dedent(
        """\
        Sekarang kamu udah punya frontend (Next.js) sama backend (Express + Prisma). Saatnya nyambungin keduanya.

        Kerjaan ini keliatan simpel: manggil API dari frontend. Tapi ada beberapa jebakan yang sering bikin pemula nyerah di langkah ini.

        Kita ngebedah satu-satu: CORS, environment variable, sama UX state yang ramah.
        """
    ),
    penjelasan=dedent(
        """\
        ### Kenapa ada masalah CORS

        Browser punya aturan keamanan: **same-origin policy**. Default-nya, JavaScript di domain A gak boleh manggil API di domain B.

        Pas kamu develop:

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

        Wildcard `*` gampang, tapi gak aman buat production. Selalu sebut origin yang spesifik.

        ### Environment variable di Next.js

        Jangan hardcode URL API. Ganti URL antar dev / staging / production lewat `.env.local`.

        ```bash
        # Frontend/.env.local
        NEXT_PUBLIC_API_URL=http://localhost:3001/api
        ```

        Aturan penting di Next.js:

        - Variabel yang aman dipake di browser HARUS punya prefix `NEXT_PUBLIC_`.
        - Variabel TANPA prefix cuma boleh diakses dari server component / API route. Jangan buat SECRET KEY.

        ### Pola fetch yang ramah

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

        Pola ini muncul berulang-ulang. Banyak orang milih library kayak TanStack Query atau SWR biar gak ngulang boilerplate ini di project gede.

        ### Server vs Client component (Next.js App Router)

        Default component di App Router itu **Server Component**. Gak bisa pake `useState`/`useEffect`.

        Buat component yang butuh state atau event handler, kasih `"use client"` di baris pertama file.

        Pola umum:

        - Page (server) fetch data → render Client component sama data sebagai prop.
        - Client component handle interaksi (form, button, animasi).

        Untungnya: data fetch bisa di server (lebih cepet, gak perlu loading state di browser), interaksi tetep di client.
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
        "Sambungin Next.js project kamu ke API books dari Backend Level 1. "
        "Bikin halaman `/books` yang nampilin daftar buku dari API. Tampilin "
        "loading state pas fetch sama error message kalau API mati."
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
        "hint": "Variable env gak kebaca di browser. Cek aturan Next.js buat env yang dipake di client.",
        "answer_explanation": dedent(
            """\
            Salahnya: `process.env.API_URL` di Next.js client gak bakal kebaca. Aturan Next.js:

            - Env tanpa prefix `NEXT_PUBLIC_` cuma tersedia di server component / API route.
            - Buat dipake di browser/client component, prefix WAJIB `NEXT_PUBLIC_`.

            Habis rename, restart `npm run dev` biar env-nya di-reload.
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
            "Apa penyebab error CORS pas develop frontend sama backend lokal?",
            [
                "Internet mati",
                "Frontend sama backend di port beda → beda origin → browser blokir",
                "Code typo",
                "Database error",
            ],
            "B",
            "Browser blokir cross-origin request demi keamanan. Backend harus kasih izin eksplisit lewat CORS.",
        ),
        q(
            "Mana cara yang BAGUS buat URL API di Next.js?",
            [
                "Hardcode `http://localhost:3001` di komponen",
                "Simpen di `.env.local` sama prefix `NEXT_PUBLIC_API_URL`",
                "Simpen di `localStorage`",
                "Simpen di global window object",
            ],
            "B",
            "Env variable bikin URL bisa diganti antar dev/staging/prod tanpa edit kode. Prefix `NEXT_PUBLIC_` biar bisa diakses di browser.",
        ),
        q(
            "Kapan kamu butuh `\"use client\"` di Next.js App Router?",
            [
                "Selalu di tiap component",
                "Pas component butuh `useState`, `useEffect`, atau event handler",
                "Pas component isinya gambar",
                "Pas component pake Tailwind",
            ],
            "B",
            "Server Component default gak bisa pake hooks atau event handler. Tambah `\"use client\"` pas component perlu interaktivitas.",
        ),
        q(
            "Mana yang HARUS di-handle pas fetch data?",
            [
                "Cuma success state",
                "Loading, success, sama error state",
                "Cuma error state",
                "Gak perlu state",
            ],
            "B",
            "User experience yang bagus: kasih tau data lagi dimuat, atau kalau ada error. Tampilan kosong tanpa konteks bikin user bingung.",
        ),
        q(
            "Beda `cache: \"no-store\"` di fetch Next.js?",
            [
                "Performance lebih jelek selalu",
                "Mastiin data selalu fresh, gak di-cache. Cocok buat data yang sering berubah.",
                "Aktifin offline mode",
                "Gak ada bedanya",
            ],
            "B",
            "Default Next.js nge-cache hasil fetch di server. `no-store` matiin cache — data selalu fresh tiap request.",
        ),
    ],
    common_mistakes=[
        "Lupa prefix `NEXT_PUBLIC_` buat env yang dipake di browser. `process.env.X` jadi `undefined`.",
        "Wildcard CORS `*` di production. Bahaya — sebut origin spesifik.",
        "Gak restart `npm run dev` habis edit `.env.local`. Env-nya gak ke-reload.",
    ],
    checkpoint=[
        "Bisa jelasin kenapa CORS error muncul.",
        "Bisa setup env variable di Next.js sama prefix yang bener.",
        "Bisa fetch data dari API di server component sama client component.",
        "Selalu handle loading sama error state.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Auth dengan JWT
# ─────────────────────────────────────────────────────────────────────────────

LESSON_AUTH = make_lesson(
    title="Auth Dasar Pake JWT",
    slug="auth-dengan-jwt",
    order_index=2,
    read_time="16 menit",
    summary="Authentication, authorization, JWT, sama protected routes.",
    tools=["Backend Express + Prisma", "Library jsonwebtoken + bcryptjs", "Next.js"],
    outcomes=[
        "Bisa bedain authentication vs authorization",
        "Paham cara kerja JWT lewat analogi nyata",
        "Bisa bangun endpoint register/login sama protected route",
    ],
    tldr=(
        "Authentication = ngecek siapa kamu. Authorization = ngecek apa yang "
        "boleh kamu lakuin. JWT = kartu akses yang server keluarin habis "
        "login. Selalu hash password sebelum simpen."
    ),
    pembuka=dedent(
        """\
        App tanpa auth itu kayak pintu rumah tanpa kunci. Siapa aja bisa masuk sama ngacak-ngacak.

        Auth itu fitur yang hampir tiap app butuhin. Untungnya, polanya seragam banget.

        Lesson ini ngebahas pake analogi konkrit, terus langsung implementasi.
        """
    ),
    penjelasan=dedent(
        """\
        ### Authentication vs Authorization

        Sering dianggep sama, padahal beda:

        - **Authentication (AuthN)** — "Siapa kamu?". Verifikasi identitas lewat email + password.
        - **Authorization (AuthZ)** — "Apa yang boleh kamu lakuin?". Cek role/permission.

        Login = AuthN. Cek `is_admin` sebelum hapus user = AuthZ.

        ### JWT — kartu akses gedung

        Bayangin kamu masuk gedung kantor:

        - **Hari pertama:** kasih KTP ke resepsionis. Resepsionis bikin **kartu akses** sama foto kamu, nomor lantai yang boleh dibuka, sama tanggal kadaluarsa. Kasih ke kamu.
        - **Hari berikutnya:** tap kartu, sensor cek apakah kartu ini valid (tanda tangan resepsionis ada). Kalau iya, pintu buka. Gak perlu nunjukin KTP lagi.

        JWT (JSON Web Token) jalannya kayak kartu akses itu:

        1. User login pake email + password.
        2. Server verifikasi.
        3. Server bikin token yang isinya user id + tanda tangan rahasia.
        4. Frontend simpen token, kirim di header tiap request berikutnya.
        5. Server cek tanda tangan token. Kalau valid, request lanjut.

        ### Anatomi JWT

        Token JWT keliatan kayak string tiga bagian dipisah titik:

        ```text
        eyJhbGciOiJIUzI1NiIsI...   . eyJzdWIiOiJ1MTIiLCJpYXQiOj...   . dBjftJeZ4CVPmB92K27uhbUJU1...
        ─────  HEADER  ─────       ─────  PAYLOAD  ─────              ────  SIGNATURE  ────
        ```

        - **Header.** Algoritma + tipe token.
        - **Payload.** Data user (id, role, expire). Bisa di-decode siapa pun, **jangan simpen password atau secret di sini.**
        - **Signature.** Hasil tanda tangan pake secret server. Ini yang verifikasi keasliannya.

        Kalau payload diubah orang, signature jadi gak match. Server tolak.

        ### Hash password — wajib

        **Jangan PERNAH simpen password plain text di database.** Pake `bcryptjs`:

        ```js
        import bcrypt from "bcryptjs";

        // Pas register
        const hash = await bcrypt.hash(password, 10);
        await prisma.user.create({ data: { email, hashed_password: hash } });

        // Pas login
        const user = await prisma.user.findUnique({ where: { email } });
        const ok = await bcrypt.compare(password, user.hashed_password);
        if (!ok) return res.status(401).json({ detail: "Email atau password salah" });
        ```

        Bcrypt itu satu arah: kamu bisa hash password jadi string acak, tapi gak bisa balik dari string acak ke password asli. Pas login, kamu bandingin hash baru vs hash di database.

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
          if (!auth) return res.status(401).json({ detail: "Token gak ada" });

          const token = auth.split(" ")[1];
          try {
            const payload = jwt.verify(token, process.env.JWT_SECRET);
            req.userId = payload.sub;                       // simpen buat handler
            next();
          } catch {
            return res.status(401).json({ detail: "Token gak valid" });
          }
        }

        app.get("/api/auth/me", authRequired, async (req, res) => {
          const user = await prisma.user.findUnique({ where: { id: req.userId } });
          res.json(user);
        });
        ```

        ### Frontend — simpen token di mana?

        Dua pilihan utama:

        - **httpOnly cookie.** Aman dari XSS, browser otomatis kirim. Butuh setup CORS sama `credentials: true`.
        - **localStorage.** Gampang, tapi bisa dibaca script jahat (XSS). Cuma buat app personal/belajar.

        Buat production, **selalu pilih httpOnly cookie**.
        """
    ),
    contoh_code_md=dedent(
        """\
        Endpoint register sama login lengkap:

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
            return res.status(400).json({ detail: "Email sama password wajib" });
          }

          const exists = await prisma.user.findUnique({ where: { email } });
          if (exists) {
            return res.status(409).json({ detail: "Email udah terdaftar" });
          }

          const hashed = await bcrypt.hash(password, 10);
          const user = await prisma.user.create({
            data: { email, hashed_password: hashed, full_name },
          });

          // Kembaliin profil tanpa password
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
        "Tambahin model `User` di Prisma schema (id, email, hashed_password, "
        "full_name). Push schema. Bikin endpoint `/auth/register` sama "
        "`/auth/login`. Test pake Postman: register user baru, terus login "
        "pake password yang bener sama yang salah."
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
    "hint": "Tiga masalah keamanan serius. Cek penyimpanan password, isi token, sama secret yang dipake.",
        "answer_explanation": dedent(
            """\
            1. Password disimpen plain text. WAJIB di-hash dulu pake bcrypt sebelum masuk database.
            2. JWT payload isinya password. Payload bisa di-decode siapa pun — jangan pernah taruh secret di JWT.
            3. Secret `"rahasia"` hardcoded sama lemah. Pake env variable yang panjang sama random (`JWT_SECRET`).
            """
        ),
        "fixed_code": dedent(
            """\
            router.post("/register", async (req, res) => {
              const { email, password, full_name } = req.body;
              if (!email || !password) {
                return res.status(400).json({ detail: "Email sama password wajib" });
              }

              const hashed = await bcrypt.hash(password, 10);
              const user = await prisma.user.create({
                data: { email, hashed_password: hashed, full_name },
              });

              // Token cuma isinya user id, bukan password
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
            "Beda authentication sama authorization?",
            [
                "Sama aja",
                "Authentication = siapa kamu, Authorization = apa yang boleh kamu lakuin",
                "Authentication lebih cepet",
                "Authorization buat admin aja",
            ],
            "B",
            "Login = AuthN. Cek role / permission = AuthZ. Dua hal beda yang sering dianggep sama.",
        ),
        q(
            "Apa yang HARUS dilakuin sebelum simpen password ke database?",
            [
                "Encode pake base64",
                "Hash pake bcrypt (atau argon2/scrypt)",
                "Encrypt pake AES",
                "Gak perlu, simpen langsung",
            ],
            "B",
            "Bcrypt one-way hash. Database gak bakal pernah tau password aslinya — bahkan kalau bocor pun.",
        ),
        q(
            "Apa yang AMAN disimpen di payload JWT?",
            [
                "Password user",
                "User id, role, expiration",
                "Credit card",
                "Database password",
            ],
            "B",
            "Payload JWT bisa di-decode siapa pun. Cuma simpen info yang gak rahasia. Password atau secret jangan pernah masuk JWT.",
        ),
        q(
            "Fungsi signature di JWT?",
            [
                "Buat encryption payload",
                "Mastiin payload gak diubah — kalau diubah, signature gak match sama token ditolak",
                "Buat performance",
                "Gak ada fungsi",
            ],
            "B",
            "Signature dihasilin pake secret server. Server pegang secret, jadi cuma server yang bisa bikin token valid.",
        ),
        q(
            "Mana cara nyimpen token yang LEBIH AMAN di production?",
            [
                "localStorage",
                "Variable JavaScript biasa",
                "httpOnly cookie",
                "URL parameter",
            ],
            "C",
            "httpOnly cookie gak bisa diakses JavaScript, jadi aman dari XSS. localStorage rentan kalau ada script jahat.",
        ),
    ],
    common_mistakes=[
        "Simpen password plain text. Bocor sekali, semua user kena.",
        "Hardcode JWT_SECRET di kode. Gampang bocor pas repo public.",
        "Pesan error spesifik 'email gak terdaftar'. Lebih aman 'email atau password salah' biar attacker gak bisa nebak user mana yang ada.",
    ],
    checkpoint=[
        "Bisa jelasin beda AuthN vs AuthZ.",
        "Bisa hash password pake bcrypt.",
        "Bisa generate sama verifikasi JWT.",
        "Bisa bikin protected route pake middleware.",
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
        "Bisa setup PostgreSQL di Supabase",
        "Bisa deploy backend Express ke Railway",
        "Bisa deploy frontend Next.js ke Vercel",
        "Bisa nyambungin ketiganya pake environment variable",
    ],
    tldr=(
        "Database di Supabase (gratis). Backend di Railway/Render (gratis "
        "sama limit). Frontend di Vercel (gratis buat hobi). Sambungin "
        "lewat env variable. Total waktu setup: ~1 jam."
    ),
    pembuka=dedent(
        """\
        Bikin app di lokal itu gampang. Bikin app yang bisa diakses orang lain dari HP mereka, itu cerita lain.

        Untungnya 2026 punya banyak free tier. Kumpulan tools Vercel + Railway + Supabase bikin deploy fullstack hampir tanpa hambatan.

        Lesson ini langkah konkrit: dari nol sampe URL publik yang bisa kamu bagiin.
        """
    ),
    penjelasan=dedent(
        """\
        ### Arsitektur deploy

        Tiga layanan yang bakal kita pake:

        - **Supabase** — PostgreSQL hosted. Free tier-nya gede banget buat hobi.
        - **Railway** atau **Render** — hosting buat backend Node.js. Free tier 500 jam/bulan.
        - **Vercel** — hosting buat frontend Next.js. Free tier-nya enak banget.

        Alurnya: frontend (Vercel) → API request → backend (Railway) → query → database (Supabase).

        ### Step 1 — Database di Supabase

        - Buka [supabase.com](https://supabase.com), Sign up pake GitHub.
        - **New Project** → kasih nama, password kuat buat database, pilih region terdekat.
        - Tunggu sekitar 2 menit buat provisioning.
        - Buka **Project Settings → Database → Connection string**. Salin URL connection.

        Ada dua format URL:
        - **Direct** (port 5432) — buat migrations sama dev.
        - **Pooler** (port 6543) — buat production runtime.

        Buat Prisma + Railway, pake **Pooler** (lebih scalable).

        ### Step 2 — Backend ke Railway

        - Push backend ke GitHub repo terpisah.
        - Buka [railway.app](https://railway.app) → Sign up pake GitHub.
        - **New Project → Deploy from GitHub repo** → pilih repo backend.
        - Buka tab **Variables**, tambahin:
          - `DATABASE_URL` = URL Supabase Pooler.
          - `JWT_SECRET` = string random panjang (`openssl rand -hex 32`).
          - `PORT` = `3001` (Railway override otomatis, tapi aman).
        - Tab **Settings → Networking → Generate Domain**. Kamu dapet URL `xxx.up.railway.app`.

        Build command: `npm install && npx prisma generate && npx prisma db push`.
        Start command: `node src/index.js` atau `npm start`.

        ### Step 3 — Frontend ke Vercel

        - Push frontend ke GitHub repo terpisah.
        - Buka [vercel.com/new](https://vercel.com/new) → import repo.
        - Tambahin env variable:
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

        - **Monorepo vs multi-repo.** Buat pemula, lebih gampang multi-repo (frontend sama backend repo terpisah). Lebih jelas mana yang deploy ke mana.
        - **Logs.** Railway sama Vercel dua-duanya punya tab Logs. Selalu cek di sini pas deploy gagal.
        - **Free tier limit.** Railway free tier bakal tidur kalau idle terlalu lama. Buat demo OK, buat produksi mungkin perlu paid plan.
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup script di `package.json` backend buat Railway:

        ```json
        {
          "scripts": {
            "build": "prisma generate && prisma db push",
            "start": "node src/index.js",
            "dev": "nodemon src/index.js"
          }
        }
        ```

        Listen ke port yang Railway sediain (env `PORT`):

        ```js
        // src/index.js
        const port = process.env.PORT || 3001;

        app.listen(port, () => {
          console.log(`API running on port ${port}`);
        });
        ```

        Frontend `.env.production` buat override URL API pas di Vercel:

        ```bash
        NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app/api
        ```
        """
    ),
    practice=(
        "Deploy stack lengkap: backend dari Backend Level 1 ke Railway, "
        "frontend Next.js minimal ke Vercel, database di Supabase. Test "
        "fetch dari URL Vercel — pastiin CORS oke sama datanya muncul. "
        "Catet tiga URL ini di catetan kamu."
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
        "hint": "Dua masalah pas dideploy ke Railway: port hardcoded sama CORS terlalu sempit.",
        "answer_explanation": dedent(
            """\
            1. Railway override port lewat env `PORT`. Hardcode 3001 bikin Railway gak bisa expose service kamu. Pake `process.env.PORT || 3001`.
            2. CORS cuma ngebolehin `localhost:3000`. Pas frontend di Vercel, request bakal diblokir. Tambah domain Vercel (atau pake array origin).
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
            "Mana kombinasi free tier yang umum buat fullstack pemula?",
            [
                "AWS + DigitalOcean + Heroku",
                "Vercel + Railway + Supabase",
                "Netlify + Replit + MongoDB Atlas Enterprise",
                "Gak ada yang gratis",
            ],
            "B",
            "Tiga ini punya free tier yang generous, kumpulan tools-nya matang, sama deploy-nya gampang.",
        ),
        q(
            "Fungsi `process.env.PORT` pas deploy ke Railway?",
            [
                "Gak ada",
                "Railway dynamically assign port lewat env. Harus di-respect, bukan hardcode.",
                "Cuma buat dev",
                "Wajib 8080",
            ],
            "B",
            "Platform PaaS biasanya assign port dinamis. Kalau hardcode 3001, app kamu gak bisa di-expose.",
        ),
        q(
            "Apa yang HARUS di-update di backend habis deploy frontend ke Vercel?",
            [
                "Database schema",
                "CORS — tambahin domain Vercel ke allowed origins",
                "Hash password",
                "Gak perlu update",
            ],
            "B",
            "Frontend di Vercel itu origin baru. Backend harus eksplisit ngebolehin, atau request bakal diblokir browser.",
        ),
        q(
            "Mana cara JWT_SECRET di production?",
            [
                "Hardcode di kode biar konsisten",
                "Generate string random panjang (`openssl rand -hex 32`) sama simpen sebagai env variable di platform deploy",
                "Pake 'rahasia'",
                "Gak perlu",
            ],
            "B",
            "Secret panjang sama unik ngelindungin token dari brute-force. Simpen di env, jangan commit ke repo.",
        ),
        q(
            "Apa yang biasanya bikin deploy gagal?",
            [
                "Salah font",
                "Env variable kurang atau salah, build script salah, CORS belum di-update",
                "Logo terlalu gede",
                "Browser lambat",
            ],
            "B",
            "Tiga masalah klasik. Selalu cek logs di platform deploy buat pesan error spesifik.",
        ),
    ],
    common_mistakes=[
        "Hardcode `localhost:3001` di frontend production. Gak ada di production.",
        "Lupa tambah domain Vercel ke CORS origin. Browser blokir.",
        "Generate Supabase URL versi 'Direct' buat app jangka panjang. Kadang lebih boros connection — pake Pooler.",
    ],
    checkpoint=[
        "Database Supabase live sama bisa diakses dari Prisma.",
        "Backend deployed di Railway sama env variable lengkap.",
        "Frontend deployed di Vercel sama `NEXT_PUBLIC_API_URL` bener.",
        "End-to-end: bisa login dari URL Vercel, data tersimpen di Supabase.",
    ],
    xp_reward=180,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_NOTES = make_lesson(
    title="Mini Project — Note-Taking App Pake Auth",
    slug="mini-project-note-taking-app",
    order_index=4,
    read_time="180 menit",
    summary="Fullstack app: register/login + CRUD note + deploy ke production.",
    tools=["Next.js", "Express + Prisma", "Supabase", "Railway", "Vercel"],
    outcomes=[
        "Bisa bangun fullstack app dari ujung ke ujung",
        "Bisa pake JWT buat session management",
        "Bisa nerapin owner-based authorization (note cuma bisa dilihat owner-nya)",
        "Bisa deploy ke production sama stack modern",
    ],
    tldr=(
        "Bangun note-taking app: auth + CRUD note per user + deploy. Tiap "
        "note milik user. User cuma bisa CRUD note miliknya sendiri. Deploy "
        "stack lengkap: Vercel + Railway + Supabase."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungin semua yang dipelajarin di level ini.

        Note-taking app sederhana, tapi isinya pola produksi: auth, owner-based access, deploy ke tiga layanan.

        Selesai project ini, kamu udah bisa bilang: "Saya bisa bikin fullstack app dari nol sampe live."
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
        - `/login` — form login. Pas sukses, simpen token, redirect ke `/notes`.
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

        Aturannya: user A gak boleh CRUD note milik user B. Tapi karena URL pake ID, kalau cuma cek "user login = OK", user A bisa hapus note B sama tau ID-nya.

        Solusi: di tiap endpoint note, cek `note.user_id === req.userId`. Kalau gak match, balas 403 Forbidden.

        ```js
        router.delete("/:id", authRequired, async (req, res) => {
          const note = await prisma.note.findUnique({ where: { id: req.params.id } });
          if (!note) return res.status(404).json({ detail: "Note gak ditemukan" });
          if (note.user_id !== req.userId) {
            return res.status(403).json({ detail: "Bukan note kamu" });
          }
          await prisma.note.delete({ where: { id: note.id } });
          res.status(204).send();
        });
        ```

        Atau lebih ringkes — query langsung sama filter user_id:

        ```js
        const note = await prisma.note.findFirst({
          where: { id: req.params.id, user_id: req.userId },
        });
        if (!note) return res.status(404).json({ detail: "Note gak ditemukan" });
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

        Catetan: localStorage dipake di sini biar simpel. Buat production beneran, ganti ke httpOnly cookie.

        ### Submit

        Live di Vercel (frontend) + Railway (backend) + Supabase (DB). Bagiin URL. Ajak temen bikin akun. Pastiin note-nya gak saling keliatan.
        """
    ),
    contoh_code_md=dedent(
        """\
        Endpoint create note sama auth dan ownership:

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
          if (!note) return res.status(404).json({ detail: "Note gak ditemukan" });

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
          if (!note) return res.status(404).json({ detail: "Note gak ditemukan" });

          await prisma.note.delete({ where: { id: note.id } });
          res.status(204).send();
        });

        export default router;
        ```
        """
    ),
    practice=(
        "Bangun stack lengkap sesuai spec. Test owner authorization: bikin "
        "dua akun, login akun A, coba akses note milik akun B sama ID-nya "
        "secara langsung — harus dapet 404. Selesai itu, deploy semua sama "
        "bagiin URL ke temen."
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
        "hint": "Endpoint ini punya celah keamanan gede. User bisa hapus note milik orang lain.",
        "answer_explanation": dedent(
            """\
            Salahnya: cuma cek user login, tapi gak cek ownership note.

            User A login → tau ID note milik user B → DELETE → kehapus. Itu vulnerability.

            Solusi: filter berdasarkan owner. Pake `findFirst` sama `user_id: req.userId` buat verifikasi ownership sebelum delete.
            """
        ),
        "fixed_code": dedent(
            """\
            router.delete("/:id", authRequired, async (req, res) => {
              const note = await prisma.note.findFirst({
                where: { id: req.params.id, user_id: req.userId },
              });
              if (!note) {
                return res.status(404).json({ detail: "Note gak ditemukan" });
              }
              await prisma.note.delete({ where: { id: note.id } });
              res.status(204).send();
            });
            """
        ),
    },
    quiz=[
        q(
            "Kenapa endpoint delete note WAJIB cek ownership, bukan cuma auth?",
            [
                "Buat performance",
                "Auth cuma cek user login. Tanpa cek owner, user bisa delete note milik orang lain sama tau ID-nya.",
                "Gak perlu",
                "Buat gaya",
            ],
            "B",
            "Authorization (cek hak akses ke resource spesifik) wajib selain authentication. Ini vulnerability nyata yang sering luput pemula.",
        ),
        q(
            "Status code yang TEPAT pas user A coba akses note milik user B?",
            [
                "200 OK",
                "401 Unauthorized",
                "404 Not Found atau 403 Forbidden",
                "500 Internal Server Error",
            ],
            "C",
            "Banyak yang pake 404 biar gak bocorin apakah ID itu valid atau enggak. 403 juga bener kalau mau eksplisit.",
        ),
        q(
            "Fungsi `onDelete: Cascade` di Prisma schema?",
            [
                "Backup otomatis",
                "Pas parent (User) dihapus, semua child (Note) ikut kehapus",
                "Performance",
                "Gak ada fungsi",
            ],
            "B",
            "Cascade penting buat konsistensi. Note tanpa owner = data nyasar.",
        ),
        q(
            "Mana cara filter note milik user yang lagi login di Prisma?",
            [
                "`findMany()` terus filter di JavaScript",
                "`findMany({ where: { user_id: req.userId } })`",
                "`findUnique({ id: req.userId })`",
                "Gak bisa filter",
            ],
            "B",
            "Filter di database lebih efisien daripada filter di kode. Bikin query selalu ngecualiin data milik user lain.",
        ),
        q(
            "Apa yang HARUS di-handle pas token expired di frontend?",
            [
                "Crash app",
                "Hapus token, redirect ke /login",
                "Loop request terus-menerus",
                "Gak perlu di-handle",
            ],
            "B",
            "401 dari API berarti token udah gak valid lagi. UX yang bagus: bersihin token lokal sama kirim user ke login.",
        ),
    ],
    common_mistakes=[
        "Cek auth tapi lupa cek ownership. Vulnerability.",
        "Gak handle 401 di frontend. User stuck di halaman yang gagal load.",
        "Pesan error beda buat 'note gak ada' vs 'bukan milik kamu'. Bisa dipake buat ngintipin ID. Pake 404 sama buat keduanya.",
    ],
    checkpoint=[
        "Stack lengkap deployed ke Vercel + Railway + Supabase.",
        "Auth flow lengkap: register, login, logout, protected page.",
        "Owner-based authorization: user A gak bisa lihat note user B.",
        "URL publik bisa diakses sama dipake dua akun beda secara terpisah.",
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
        "Belajar nyambungin frontend sama backend jadi satu aplikasi utuh. "
        "Auth, owner-based authorization, environment variable, sama deploy "
        "production stack: Vercel + Railway + Supabase."
    ),
    duration="~4 minggu",
    difficulty="Menengah",
    accent_color="from-indigo-400/30 to-violet-500/10",
    mini_project="Note-Taking App dengan Auth",
    tags=["Next.js", "Express", "Prisma", "JWT", "Deployment"],
    lessons=[LESSON_CONNECTION, LESSON_AUTH, LESSON_DEPLOY, PROJECT_NOTES],
)
