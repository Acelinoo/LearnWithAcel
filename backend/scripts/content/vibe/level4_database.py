"""
Vibe / Level 4 — Database & Backend Basics.

Lessons:
  1. database-untuk-vibe-coder
  2. supabase-setup
  3. auth-dengan-nextauth
  4. mini-project-todo-with-auth  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Database untuk Vibe Coder
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DB_VIBE = make_lesson(
    title="Database untuk Vibe Coder",
    slug="database-untuk-vibe-coder",
    order_index=1,
    read_time="11 menit",
    summary="Konsep database tanpa istilah ribet, plus cara prompt schema ke AI.",
    tools=["Notes app", "Browser"],
    outcomes=[
        "Memahami konsep tabel, kolom, baris dengan analogi sehari-hari",
        "Mengenali kapan app butuh database",
        "Prompt AI untuk generate Prisma schema",
    ],
    tldr=(
        "Database = lemari arsip digital. Tabel = kategori berkas. Kolom = "
        "atribut tiap berkas. Baris = satu record. Prompt AI dengan model "
        "data yang kamu mau, dia generate Prisma schema."
    ),
    pembuka=dedent(
        """\
        Sampai sini app kamu masih hilang datanya saat refresh. Catatan ditulis, lalu hilang saat tab ditutup.

        Untuk app real, kamu butuh database — tempat data tersimpan permanen dan bisa di-query siapa saja yang punya akses.

        Lesson ini bedah konsep database dengan analogi yang tidak pakai istilah teknis.
        """
    ),
    penjelasan=dedent(
        """\
        ### Analogi: lemari arsip kantor

        Bayangkan kantor zaman dulu yang punya banyak lemari arsip:

        - **Lemari "Karyawan"** berisi map untuk setiap karyawan. Tiap map punya: foto, nama, jabatan, tanggal masuk.
        - **Lemari "Proyek"** berisi map untuk setiap proyek. Tiap map punya: nama proyek, status, deadline, karyawan yang terlibat.
        - **Lemari "Gaji"** berisi map untuk setiap pembayaran. Tiap map punya: tanggal, nominal, karyawan penerima.

        Database modern bekerja persis seperti ini:

        - **Lemari** = **tabel**.
        - **Map dalam lemari** = **baris** (record).
        - **Atribut di tiap map** = **kolom**.

        Setiap record bisa terhubung ke record di lemari lain (proyek terhubung ke karyawan via "diisi oleh").

        ### Kapan app butuh database

        Tidak semua app butuh database. Kamu butuh kalau salah satu kondisi ini muncul:

        - Data harus tetap ada walau tab/HP/komputer ditutup.
        - Data harus dishare antar user (komentar, pesan, post).
        - Data harus dicari/di-filter berdasarkan kriteria tertentu.
        - Data tumbuh besar dari waktu ke waktu (ribuan/jutaan record).

        Kalau cuma tampilan statis seperti landing page atau portfolio, **tidak butuh database**. Hardcode data di file sudah cukup.

        ### Anatomi tabel

        Bayangkan tabel `users`:

        ```text
        ┌──────┬──────────────────┬──────────────┬─────────────────────┐
        │  id  │      email       │  full_name   │     created_at      │
        ├──────┼──────────────────┼──────────────┼─────────────────────┤
        │   1  │ acel@email.com   │  Acel        │  2026-01-15 10:00   │
        │   2  │ budi@email.com   │  Budi        │  2026-01-16 14:30   │
        │   3  │ citra@email.com  │  Citra       │  2026-01-17 09:00   │
        └──────┴──────────────────┴──────────────┴─────────────────────┘
        ```

        - **id** — kolom unik untuk identifikasi (seperti nomor map). Disebut primary key.
        - **email**, **full_name** — kolom data.
        - **created_at** — kolom timestamp otomatis.
        - Tiap baris = satu record.

        ### Relasi antar tabel

        Tabel bisa saling terhubung. Contoh: tabel `posts` punya kolom `user_id` yang merujuk ke tabel `users`.

        ```text
        Tabel: posts
        ┌─────┬─────────────────┬─────────────┐
        │ id  │     title       │  user_id    │  ← merujuk ke users.id
        ├─────┼─────────────────┼─────────────┤
        │ 100 │ Belajar coding  │      1      │
        │ 101 │ Tips deploy     │      1      │
        │ 102 │ Cara prompt AI  │      2      │
        └─────┴─────────────────┴─────────────┘
        ```

        Hasilnya: post 100 dan 101 dimiliki user 1 (Acel). Post 102 milik user 2 (Budi). Ini namanya **foreign key relationship**.

        ### SQL vs NoSQL

        Dua kelompok besar database:

        - **SQL (relational)** — data terstruktur dalam tabel-tabel yang saling terhubung. PostgreSQL, MySQL, SQLite.
        - **NoSQL (document)** — data lebih fleksibel, mirip JSON. MongoDB, Firebase Firestore.

        Untuk vibe coder, **PostgreSQL via Supabase** adalah pilihan default. Alasannya:

        - SQL skill berlaku di banyak tempat.
        - Supabase free tier generous.
        - Auth + storage + realtime built-in.

        ### Cara prompt schema ke AI

        Daripada nulis Prisma schema dari nol, deskripsikan model data ke AI:

        > Saya mau bikin app habit tracker. Model data:
        >
        > - User: punya banyak habit dan banyak check-in.
        > - Habit: dimiliki user, punya nama, deskripsi, target frekuensi (harian/mingguan).
        > - CheckIn: dimiliki user dan habit, dengan tanggal dan catatan opsional.
        >
        > Generate Prisma schema dengan PostgreSQL provider, primary key UUID, dan timestamp untuk created_at.

        AI akan kasih schema lengkap dengan relasi yang benar. Kamu tinggal review.

        ### Aturan emas

        - **Mulai sederhana.** 3-5 model cukup untuk MVP.
        - **Pakai UUID untuk primary key.** Lebih aman daripada integer auto-increment.
        - **Snake_case untuk nama kolom.** Contoh: `created_at`, `user_id`. Konvensi yang umum.
        - **Tambah `created_at` dan `updated_at` ke semua model.** Berguna untuk debugging dan analytics.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh Prisma schema untuk app habit tracker:

        ```prisma
        generator client {
          provider = "prisma-client-js"
        }

        datasource db {
          provider = "postgresql"
          url      = env("DATABASE_URL")
        }

        model User {
          id         String    @id @default(uuid())
          email      String    @unique
          full_name  String
          created_at DateTime  @default(now())

          habits     Habit[]
          checkins   CheckIn[]
        }

        model Habit {
          id          String   @id @default(uuid())
          name        String
          description String?
          frequency   String   // "daily" | "weekly"
          user_id     String
          created_at  DateTime @default(now())

          owner       User     @relation(fields: [user_id], references: [id], onDelete: Cascade)
          checkins    CheckIn[]

          @@index([user_id])
        }

        model CheckIn {
          id          String   @id @default(uuid())
          habit_id    String
          user_id     String
          checked_at  DateTime @default(now())
          note        String?

          habit       Habit    @relation(fields: [habit_id], references: [id], onDelete: Cascade)
          user        User     @relation(fields: [user_id], references: [id], onDelete: Cascade)

          @@index([habit_id])
          @@index([user_id])
        }
        ```

        Tiga model, semua punya UUID, ada cascade delete (kalau user dihapus, habit dan checkin ikut terhapus), dan index untuk query cepat.
        """
    ),
    practice=(
        "Pikirkan satu app yang ingin kamu bangun. Tulis di catatan: berapa "
        "model data yang dibutuhkan, apa kolom-kolomnya, bagaimana mereka "
        "saling terhubung. Lalu prompt AI untuk generate Prisma schema-nya."
    ),
    fix_error={
        "language": "prisma",
        "broken_code": dedent(
            """\
            model user {
              id    Int
              email String
              posts Post
            }

            model Post {
              id      Int
              title   String
              user    user
            }
            """
        ),
        "hint": (
            "Empat masalah: penamaan model, primary key, kolom unique, dan "
            "deklarasi relasi."
        ),
        "answer_explanation": dedent(
            """\
            1. Nama model **wajib PascalCase** — `User` bukan `user`.
            2. Primary key butuh `@id`. Saran modern pakai `String @default(uuid())`.
            3. Email harus `@unique` supaya tidak ada duplikat.
            4. Relasi butuh foreign key field (`user_id`) + `@relation` mapping. `Post` dari `User` itu array (`Post[]`), bukan single.
            """
        ),
        "fixed_code": dedent(
            """\
            model User {
              id         String   @id @default(uuid())
              email      String   @unique
              created_at DateTime @default(now())
              posts      Post[]
            }

            model Post {
              id         String   @id @default(uuid())
              title      String
              user_id    String
              created_at DateTime @default(now())
              user       User     @relation(fields: [user_id], references: [id], onDelete: Cascade)

              @@index([user_id])
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa analogi paling tepat untuk database?",
            [
                "Aplikasi WhatsApp",
                "Lemari arsip yang terorganisir dengan banyak laci, tiap laci untuk kategori berbeda",
                "Spreadsheet di komputer",
                "Browser bookmark",
            ],
            "B",
            "Lemari arsip = tabel-tabel yang terhubung. Tiap map = record. Atribut map = kolom. Ini analogi yang paling akurat.",
        ),
        q(
            "Kapan app TIDAK butuh database?",
            [
                "Tidak ada — app selalu butuh database",
                "Saat data statis (landing page, portfolio) dan tidak perlu disimpan untuk user",
                "Saat ada login",
                "Saat ada chat",
            ],
            "B",
            "Landing page, portfolio, dokumentasi statis tidak butuh database. Hardcode data di file lebih sederhana.",
        ),
        q(
            "Apa fungsi `@unique` di Prisma?",
            [
                "Mempercepat query",
                "Memastikan tidak ada duplikat di kolom itu (misal: email tidak boleh sama antar user)",
                "Auto-encrypt",
                "Tidak ada fungsi",
            ],
            "B",
            "Constraint database untuk integrity. Tanpa unique pada email, dua user bisa daftar dengan email sama — kekacauan.",
        ),
        q(
            "Mana praktik primary key yang DIREKOMENDASIKAN?",
            [
                "Integer auto-increment (1, 2, 3, ...)",
                "UUID (`String @id @default(uuid())`)",
                "Email user",
                "Nama lengkap",
            ],
            "B",
            "UUID acak panjang sehingga tidak bisa ditebak, aman dipakai di URL publik, dan tidak konflik saat data di-merge dari sumber berbeda.",
        ),
        q(
            "Apa yang dilakukan `onDelete: Cascade` di relasi Prisma?",
            [
                "Backup otomatis sebelum delete",
                "Saat parent dihapus, semua child yang terhubung ikut terhapus",
                "Mencegah delete",
                "Tidak ada efek",
            ],
            "B",
            "Cascade delete menjaga konsistensi. Kalau User dihapus, Post-nya juga harus terhapus — tidak boleh ada Post tanpa author.",
        ),
    ],
    common_mistakes=[
        "Lowercase model name di Prisma. Generator complain.",
        "Lupa `@unique` di kolom email. Bisa duplikat, masalah saat login.",
        "Pakai integer auto-increment di production. Bocor info jumlah user, tidak aman di URL.",
    ],
    checkpoint=[
        "Bisa jelaskan database dengan analogi lemari arsip.",
        "Bisa membaca dan menulis Prisma schema sederhana.",
        "Tahu kapan app butuh database.",
        "Bisa prompt AI untuk generate schema dari deskripsi model data.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Supabase Setup
# ─────────────────────────────────────────────────────────────────────────────

LESSON_SUPABASE = make_lesson(
    title="Setup Supabase + Prisma",
    slug="supabase-setup",
    order_index=2,
    read_time="12 menit",
    summary="Database hosted dalam 5 menit, terhubung ke project Next.js.",
    tools=["Akun Supabase", "Project Next.js", "Cursor", "Terminal"],
    outcomes=[
        "Membuat project Supabase dan database PostgreSQL",
        "Setup Prisma di Next.js",
        "Push schema dan eksekusi query pertama",
    ],
    tldr=(
        "Supabase kasih PostgreSQL gratis dalam < 5 menit. Connect ke Next.js "
        "via Prisma. Setelah `prisma db push`, tabel siap dipakai."
    ),
    pembuka=dedent(
        """\
        Bikin database dari nol biasanya ribet: install PostgreSQL, set password, manage versi. Memakan waktu sebelum nulis satu baris kode pun.

        Supabase hapus semua hambatan itu. Sign up, klik new project, tunggu 2 menit. Selesai. Kamu punya PostgreSQL siap pakai.

        Lesson ini step by step setup-nya plus integrasi ke project Next.js.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu Supabase

        Supabase adalah platform "Firebase alternative" yang built on PostgreSQL. Free tier-nya generous untuk hobi/MVP.

        Yang kamu dapat:

        - **PostgreSQL database** dengan dashboard SQL editor.
        - **Auth** built-in (email + OAuth Google/GitHub/dll).
        - **Storage** untuk upload file.
        - **Realtime** subscriptions ke perubahan database.
        - **Auto-generated REST + GraphQL API** kalau mau pakai langsung tanpa backend custom.

        Untuk vibe coder, kombinasi yang paling sering: Supabase untuk database + auth, Prisma sebagai ORM.

        ### Step 1 — Bikin project Supabase

        - Buka [supabase.com](https://supabase.com), Sign up dengan GitHub.
        - **New Project** → kasih nama, password DB yang kuat (simpan di password manager), pilih region terdekat (Singapore untuk Asia).
        - Tunggu sekitar 2 menit untuk provisioning.

        Setelah selesai, kamu masuk ke dashboard project. Di sini ada SQL editor, Auth panel, Storage, dan Logs.

        ### Step 2 — Salin connection string

        - Buka **Project Settings → Database**.
        - Cari section **Connection string**. Ada beberapa format:
          - **Direct connection (port 5432)** — untuk migration dan dev.
          - **Connection pooling - Transaction (port 6543)** — untuk runtime, **paling sering dipakai**.
          - **Connection pooling - Session (port 5432)** — untuk session-based.

        Untuk Prisma + Next.js, paling aman pakai **Direct (5432)** untuk migration dan **Pooler Transaction (6543)** untuk runtime.

        Format URL:

        ```text
        postgresql://postgres.[ref]:[password]@[host]:[port]/postgres
        ```

        ### Step 3 — Setup Prisma di Next.js

        Di project Next.js kamu:

        ```bash
        npm install prisma @prisma/client
        npx prisma init
        ```

        Edit `prisma/schema.prisma`:

        ```prisma
        generator client {
          provider = "prisma-client-js"
        }

        datasource db {
          provider  = "postgresql"
          url       = env("DATABASE_URL")
          directUrl = env("DIRECT_URL")
        }

        model User {
          id         String   @id @default(uuid())
          email      String   @unique
          full_name  String
          created_at DateTime @default(now())
        }
        ```

        Edit `.env.local`:

        ```bash
        # Untuk runtime (pooler)
        DATABASE_URL="postgresql://postgres.xxx:password@aws-0-region.pooler.supabase.com:6543/postgres?pgbouncer=true"

        # Untuk migration (direct)
        DIRECT_URL="postgresql://postgres.xxx:password@aws-0-region.pooler.supabase.com:5432/postgres"
        ```

        Salin URL dari Supabase dashboard. Pastikan password sudah di-replace.

        ### Step 4 — Push schema

        ```bash
        npx prisma db push
        ```

        Prisma bikin tabel di Supabase. Buka dashboard Supabase → Table Editor → kamu harusnya lihat tabel `User` muncul.

        ```bash
        npx prisma generate
        ```

        Generate Prisma Client TypeScript. Sekarang kamu bisa import dan pakai dari kode.

        ### Step 5 — Singleton Prisma di Next.js

        Next.js dev mode hot-reload sering bikin Prisma Client multiple instance → memory leak warning. Solusi: bikin singleton.

        ```ts
        // lib/db.ts
        import { PrismaClient } from "@prisma/client";

        const globalForPrisma = globalThis as unknown as {
          prisma: PrismaClient | undefined;
        };

        export const db = globalForPrisma.prisma ?? new PrismaClient();

        if (process.env.NODE_ENV !== "production") {
          globalForPrisma.prisma = db;
        }
        ```

        Pakai dari mana saja:

        ```ts
        import { db } from "@/lib/db";

        const users = await db.user.findMany();
        ```

        ### Test cepat

        Bikin endpoint API route Next.js:

        ```ts
        // app/api/test/route.ts
        import { db } from "@/lib/db";
        import { NextResponse } from "next/server";

        export async function GET() {
          const users = await db.user.findMany();
          return NextResponse.json({ count: users.length, users });
        }
        ```

        Buka `http://localhost:3000/api/test`. Kamu harusnya dapat `{ count: 0, users: [] }`.

        Coba bikin user dari Supabase Table Editor (klik "Insert row"). Refresh API → user-nya muncul.

        ### Aturan keamanan

        - **JANGAN commit `.env.local`**. Tambahkan ke `.gitignore`.
        - **JANGAN expose `DATABASE_URL` ke client.** Variabel TANPA prefix `NEXT_PUBLIC_` aman di server, tidak ter-bundle ke browser.
        - **Pakai password manager** untuk simpan password DB.
        """
    ),
    contoh_code_md=dedent(
        """\
        Singleton + endpoint test lengkap:

        ```ts
        // lib/db.ts
        import { PrismaClient } from "@prisma/client";

        const globalForPrisma = globalThis as unknown as {
          prisma: PrismaClient | undefined;
        };

        export const db = globalForPrisma.prisma ?? new PrismaClient({
          log: process.env.NODE_ENV === "development" ? ["query", "error"] : ["error"],
        });

        if (process.env.NODE_ENV !== "production") {
          globalForPrisma.prisma = db;
        }
        ```

        ```ts
        // app/api/users/route.ts
        import { db } from "@/lib/db";
        import { NextResponse } from "next/server";

        export async function GET() {
          const users = await db.user.findMany({
            orderBy: { created_at: "desc" },
          });
          return NextResponse.json(users);
        }

        export async function POST(req: Request) {
          const { email, full_name } = await req.json();

          if (!email || !full_name) {
            return NextResponse.json(
              { error: "Email dan full_name wajib" },
              { status: 400 },
            );
          }

          const user = await db.user.create({
            data: { email, full_name },
          });

          return NextResponse.json(user, { status: 201 });
        }
        ```
        """
    ),
    practice=(
        "Setup Supabase project baru, Prisma di project Next.js kamu, dan "
        "push schema model `User` sederhana. Bikin endpoint `/api/users` "
        "dengan GET dan POST. Test create user dari Postman, lalu list "
        "user-nya."
    ),
    fix_error={
        "language": "ts",
        "broken_code": dedent(
            """\
            // app/page.tsx
            import { PrismaClient } from "@prisma/client";

            const prisma = new PrismaClient();

            export default async function HomePage() {
              const users = await prisma.user.findMany();
              return <div>{users.length} users</div>;
            }
            """
        ),
        "hint": (
            "Saat dev mode hot-reload, kamu akan dapat warning multiple "
            "PrismaClient instance. Apa yang salah?"
        ),
        "answer_explanation": dedent(
            """\
            Kesalahan: `new PrismaClient()` dipanggil di setiap render. Hot-reload bikin instance baru terus, akhirnya warning "too many connections".

            Solusi: bikin singleton di `lib/db.ts` yang reuse instance lewat globalThis (selama bukan di production).
            """
        ),
        "fixed_code": dedent(
            """\
            // lib/db.ts
            import { PrismaClient } from "@prisma/client";

            const globalForPrisma = globalThis as unknown as {
              prisma: PrismaClient | undefined;
            };

            export const db = globalForPrisma.prisma ?? new PrismaClient();
            if (process.env.NODE_ENV !== "production") {
              globalForPrisma.prisma = db;
            }

            // app/page.tsx
            import { db } from "@/lib/db";

            export default async function HomePage() {
              const users = await db.user.findMany();
              return <div>{users.length} users</div>;
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa yang ditawarkan Supabase free tier?",
            [
                "Hanya database",
                "PostgreSQL + Auth + Storage + Realtime + auto-generated API",
                "Cuma hosting",
                "Tidak ada",
            ],
            "B",
            "Supabase = backend-as-a-service. Untuk MVP, sering tidak butuh backend custom — Supabase saja cukup.",
        ),
        q(
            "Apa beda DATABASE_URL dan DIRECT_URL di Prisma + Supabase?",
            [
                "Tidak ada beda",
                "DATABASE_URL untuk runtime (pooler), DIRECT_URL untuk migration",
                "Salah satu cuma untuk testing",
                "DIRECT_URL untuk frontend",
            ],
            "B",
            "Pooler aman untuk runtime karena handle banyak connection. Migration butuh direct connection karena pooler tidak support DDL.",
        ),
        q(
            "Mengapa kita butuh singleton PrismaClient di Next.js dev mode?",
            [
                "Untuk gaya",
                "Hot-reload bikin instance PrismaClient baru terus → warning 'too many connections'",
                "Lebih cepat",
                "Tidak butuh",
            ],
            "B",
            "Pola singleton via globalThis adalah workaround standar di komunitas Next.js + Prisma.",
        ),
        q(
            "Apa yang HARUS dilakukan dengan `.env.local`?",
            [
                "Commit ke GitHub supaya teman bisa pakai",
                "Tambahkan ke `.gitignore` dan jangan pernah commit",
                "Upload ke cloud",
                "Email ke supabase",
            ],
            "B",
            "DATABASE_URL berisi password database. Bocor sekali, akses penuh ke data. .gitignore wajib.",
        ),
        q(
            "Apa yang terjadi setelah `npx prisma db push`?",
            [
                "Tidak ada",
                "Prisma sinkronkan tabel di database sesuai schema.prisma",
                "Schema dihapus",
                "Database di-format",
            ],
            "B",
            "`db push` cocok untuk dev. Untuk production sebaiknya pakai `prisma migrate` agar history schema tersimpan rapi.",
        ),
    ],
    common_mistakes=[
        "Commit `.env.local` ke GitHub. Database password bocor.",
        "Pakai DATABASE_URL pooler untuk migration. Migration gagal karena pooler tidak support DDL.",
        "`new PrismaClient()` di setiap file. Memory leak di dev mode.",
    ],
    checkpoint=[
        "Project Supabase aktif dengan PostgreSQL siap pakai.",
        "Prisma terhubung dan schema ter-push.",
        "Bisa CRUD lewat API route Next.js.",
        "Singleton db.ts terbentuk dan dipakai konsisten.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Auth dengan NextAuth (Auth.js)
# ─────────────────────────────────────────────────────────────────────────────

LESSON_AUTH_NEXT = make_lesson(
    title="Auth dengan NextAuth",
    slug="auth-dengan-nextauth",
    order_index=3,
    read_time="14 menit",
    summary="Login/register dengan NextAuth + Prisma adapter, plus protected routes.",
    tools=["Project Next.js + Prisma + Supabase", "Akun Google (untuk OAuth)", "Cursor"],
    outcomes=[
        "Setup NextAuth (Auth.js v5) di project Next.js",
        "Auth dengan email/password + Google OAuth",
        "Protect halaman dengan session check",
    ],
    tldr=(
        "NextAuth (Auth.js) handle auth flow lengkap. Setup provider (email/"
        "Google), pakai Prisma adapter untuk simpan session/user di DB. "
        "Protect halaman dengan `auth()` di server component."
    ),
    pembuka=dedent(
        """\
        Auth itu fitur yang hampir setiap app butuh. Tapi nulis dari nol berarti kamu harus handle: hash password, generate token, manage session, OAuth flow, password reset.

        NextAuth (sekarang Auth.js) abstrak semua itu. Kamu kasih config, dia urusin sisanya.

        Untuk vibe coder, ini stack default — sebagian besar SaaS production di komunitas Next.js pakai pattern ini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu NextAuth (Auth.js)

        NextAuth adalah authentication library untuk Next.js. Versi terbaru namanya **Auth.js v5** (masih sering disebut NextAuth).

        Yang kamu dapat:

        - Login dengan **provider** (email/password, Google, GitHub, Discord, dll).
        - Session management (cookie httpOnly, otomatis).
        - Database adapter (Prisma, Drizzle, dll) untuk simpan user.
        - Protected route helper.
        - Built-in CSRF protection.

        ### Setup di Next.js 14 (App Router)

        ```bash
        npm install next-auth@beta @auth/prisma-adapter
        ```

        ### Struktur file

        ```text
        app/
          ├── api/
          │   └── auth/
          │       └── [...nextauth]/
          │           └── route.ts   ← handler NextAuth
          ├── login/page.tsx
          └── dashboard/page.tsx     ← protected
        auth.ts                      ← config utama
        middleware.ts                ← optional: protect via middleware
        ```

        ### Config dasar (Google OAuth)

        ```ts
        // auth.ts
        import NextAuth from "next-auth";
        import Google from "next-auth/providers/google";
        import { PrismaAdapter } from "@auth/prisma-adapter";
        import { db } from "@/lib/db";

        export const { handlers, auth, signIn, signOut } = NextAuth({
          adapter: PrismaAdapter(db),
          providers: [
            Google({
              clientId: process.env.GOOGLE_CLIENT_ID!,
              clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
            }),
          ],
          session: { strategy: "jwt" },
          pages: {
            signIn: "/login",
          },
        });
        ```

        ```ts
        // app/api/auth/[...nextauth]/route.ts
        import { handlers } from "@/auth";
        export const { GET, POST } = handlers;
        ```

        ### Schema yang dibutuhkan Prisma adapter

        Prisma adapter butuh model `User`, `Account`, `Session`, dan `VerificationToken`. Generate dengan:

        ```bash
        # Di docs Auth.js, ada SQL schema yang siap pakai
        # Atau prompt AI: "Bikin Prisma schema untuk Auth.js v5 adapter"
        ```

        Saran: copy schema standar dari [authjs.dev/getting-started/adapters/prisma](https://authjs.dev/getting-started/adapters/prisma).

        ### Setup Google OAuth credentials

        - Buka [console.cloud.google.com](https://console.cloud.google.com).
        - Bikin project baru.
        - **APIs & Services → Credentials → Create Credentials → OAuth Client ID**.
        - Application type: Web Application.
        - Authorized redirect URI: `http://localhost:3000/api/auth/callback/google` (untuk dev) dan domain Vercel (untuk production).
        - Salin Client ID dan Client Secret ke `.env.local`.

        ### Login button

        ```tsx
        // components/SignInButton.tsx
        import { signIn } from "@/auth";

        export default function SignInButton() {
          return (
            <form action={async () => {
              "use server";
              await signIn("google", { redirectTo: "/dashboard" });
            }}>
              <button type="submit">Login dengan Google</button>
            </form>
          );
        }
        ```

        ### Cek session di server component

        ```tsx
        // app/dashboard/page.tsx
        import { auth } from "@/auth";
        import { redirect } from "next/navigation";

        export default async function Dashboard() {
          const session = await auth();
          if (!session) redirect("/login");

          return (
            <div>
              <h1>Halo, {session.user.name}!</h1>
              <p>Email: {session.user.email}</p>
            </div>
          );
        }
        ```

        Tidak butuh `useState`, tidak butuh fetch token manual. NextAuth handle semua di balik layar.

        ### Protect via middleware (alternatif)

        ```ts
        // middleware.ts
        import { auth } from "@/auth";

        export default auth((req) => {
          if (!req.auth && req.nextUrl.pathname.startsWith("/dashboard")) {
            const url = new URL("/login", req.url);
            return Response.redirect(url);
          }
        });

        export const config = {
          matcher: ["/((?!api|_next|.*\\..*).*)"],
        };
        ```

        Middleware jalan di edge sebelum request masuk ke route. Lebih efisien untuk redirect blanket.

        ### Logout

        ```tsx
        import { signOut } from "@/auth";

        <form action={async () => {
          "use server";
          await signOut({ redirectTo: "/" });
        }}>
          <button type="submit">Logout</button>
        </form>
        ```

        ### .env.local lengkap

        ```bash
        DATABASE_URL="..."
        DIRECT_URL="..."

        AUTH_SECRET="generate dengan: openssl rand -base64 32"
        AUTH_URL="http://localhost:3000"

        GOOGLE_CLIENT_ID="xxx.apps.googleusercontent.com"
        GOOGLE_CLIENT_SECRET="xxx"
        ```

        Saat deploy ke Vercel, salin semua ke Vercel env (kecuali AUTH_URL — Vercel set otomatis).
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman dashboard yang aman:

        ```tsx
        // app/dashboard/page.tsx
        import { auth, signOut } from "@/auth";
        import { redirect } from "next/navigation";
        import { db } from "@/lib/db";

        export default async function Dashboard() {
          const session = await auth();
          if (!session?.user?.id) redirect("/login");

          const user = await db.user.findUnique({
            where: { id: session.user.id },
          });

          return (
            <main className="mx-auto max-w-2xl p-8">
              <header className="mb-8 flex items-center justify-between">
                <div>
                  <h1 className="text-2xl font-semibold">
                    Halo, {user?.name ?? "Teman"}!
                  </h1>
                  <p className="text-gray-400">{user?.email}</p>
                </div>
                <form action={async () => {
                  "use server";
                  await signOut({ redirectTo: "/" });
                }}>
                  <button className="rounded-lg border px-3 py-1 hover:bg-gray-100">
                    Logout
                  </button>
                </form>
              </header>

              <div className="rounded-2xl border p-6">
                <h2 className="font-semibold">Welcome ke dashboard</h2>
                <p className="mt-2 text-sm text-gray-600">
                  Halaman ini cuma bisa diakses kalau kamu sudah login.
                </p>
              </div>
            </main>
          );
        }
        ```
        """
    ),
    practice=(
        "Setup NextAuth dengan Google OAuth di project Next.js kamu. Bikin "
        "halaman `/login` dengan tombol Google, dan halaman `/dashboard` yang "
        "protected (redirect ke login kalau belum auth). Test login dan "
        "logout."
    ),
    fix_error={
        "language": "tsx",
        "broken_code": dedent(
            """\
            // app/dashboard/page.tsx
            "use client";
            import { useState, useEffect } from "react";

            export default function Dashboard() {
              const [user, setUser] = useState(null);

              useEffect(() => {
                const token = localStorage.getItem("token");
                if (!token) {
                  window.location.href = "/login";
                }
                // ... fetch user with token
              }, []);

              if (!user) return <p>Loading...</p>;
              return <h1>Halo {user.name}</h1>;
            }
            """
        ),
        "hint": (
            "Pendekatan ini bekerja, tapi rentan dan rumit untuk Next.js modern. "
            "Apa cara yang lebih elegan dengan NextAuth?"
        ),
        "answer_explanation": dedent(
            """\
            Masalah:

            1. Pakai `localStorage` untuk token = rentan XSS.
            2. Loading state manual = flickering UX.
            3. Client-side redirect = halaman sempat muncul sebelum redirect.

            Solusi: pakai server component dengan `auth()`. Cek session di server, redirect sebelum HTML dikirim. NextAuth pakai cookie httpOnly otomatis — aman dari XSS.
            """
        ),
        "fixed_code": dedent(
            """\
            // app/dashboard/page.tsx (Server Component, default)
            import { auth } from "@/auth";
            import { redirect } from "next/navigation";

            export default async function Dashboard() {
              const session = await auth();
              if (!session) redirect("/login");

              return <h1>Halo {session.user.name}</h1>;
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi Prisma adapter di NextAuth?",
            [
                "Generate UI",
                "Menyimpan user, account, session, dan verification token ke database via Prisma",
                "Untuk styling",
                "Tidak ada",
            ],
            "B",
            "Adapter adalah jembatan antara NextAuth dan database kamu. Tanpa adapter, session disimpan in-memory.",
        ),
        q(
            "Mana cara protect halaman yang LEBIH BAIK di Next.js App Router?",
            [
                "Cek `localStorage` di useEffect",
                "Pakai `auth()` di server component, redirect kalau tidak ada session",
                "Tidak perlu protect",
                "Hide tombol saja",
            ],
            "B",
            "Server-side protection lebih aman dan UX lebih baik (no flicker). Server tahu session sebelum HTML dikirim.",
        ),
        q(
            "Apa yang HARUS ada di `.env.local` untuk NextAuth + Google?",
            [
                "Cuma DATABASE_URL",
                "AUTH_SECRET, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, DATABASE_URL",
                "Cuma password",
                "Tidak ada env",
            ],
            "B",
            "AUTH_SECRET untuk sign cookie, Google credentials untuk OAuth, DATABASE_URL untuk simpan session. Semua wajib.",
        ),
        q(
            "Mana token storage yang LEBIH AMAN dari XSS?",
            [
                "localStorage",
                "Cookie httpOnly",
                "Variable JavaScript",
                "URL parameter",
            ],
            "B",
            "httpOnly cookie tidak bisa diakses JavaScript = aman dari XSS. NextAuth pakai ini secara default.",
        ),
        q(
            "Apa yang dimaksud `redirect URI` saat setup Google OAuth?",
            [
                "URL untuk login",
                "URL callback yang Google panggil setelah user login (misal `/api/auth/callback/google`)",
                "URL homepage",
                "URL dashboard",
            ],
            "B",
            "Setelah user login di Google, Google redirect balik ke aplikasi kamu di URL ini. Wajib di-whitelist di Google Console.",
        ),
    ],
    common_mistakes=[
        "Pakai localStorage untuk token. Rentan XSS.",
        "Lupa whitelist redirect URI di Google Console. OAuth gagal dengan error 'redirect_uri_mismatch'.",
        "Cek session di client component padahal bisa di server component. Hasilnya flickering UX.",
    ],
    checkpoint=[
        "NextAuth setup dengan Google OAuth aktif.",
        "Halaman protected redirect ke /login kalau tidak ada session.",
        "Logout berfungsi.",
        "Schema Prisma adapter (User, Account, Session, VerificationToken) ter-push.",
    ],
    xp_reward=200,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_TODO_AUTH = make_lesson(
    title="Mini Project — Todo App dengan Auth",
    slug="mini-project-todo-with-auth",
    order_index=4,
    read_time="180 menit",
    summary="Fullstack todo: login Google, data per user, deploy live.",
    tools=["Next.js + Prisma + Supabase + NextAuth", "Cursor", "Vercel"],
    outcomes=[
        "Membangun fullstack app dengan auth dan database",
        "Memakai owner-based authorization",
        "Deploy ke production dengan environment variables yang benar",
    ],
    tldr=(
        "Bangun todo app dengan login Google. Setiap user cuma lihat dan "
        "edit todo miliknya. Deploy ke Vercel. Stack: Next.js + Prisma + "
        "Supabase + NextAuth + shadcn."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungkan semua di Level 4: database, schema, auth, owner-based access, deploy.

        Hasilnya: todo app yang real, bisa dipakai banyak user secara aman.

        Selesai project ini, kamu sudah bisa bilang dengan jujur: 'Saya bisa bikin SaaS dasar dari nol.'
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind + shadcn/ui + Prisma + Supabase + NextAuth.

        Halaman:

        - `/` — landing page singkat dengan tombol login.
        - `/login` — tombol "Login dengan Google".
        - `/todos` — protected. List + form bikin todo + toggle selesai + hapus. Cuma todo milik user yang login.

        ### Schema Prisma

        ```prisma
        // Auth.js adapter models
        model User {
          id            String    @id @default(cuid())
          name          String?
          email         String    @unique
          emailVerified DateTime?
          image         String?
          accounts      Account[]
          sessions      Session[]

          // App-specific
          todos         Todo[]
        }

        model Account {
          id                String  @id @default(cuid())
          userId            String
          type              String
          provider          String
          providerAccountId String
          refresh_token     String?
          access_token      String?
          expires_at        Int?
          token_type        String?
          scope             String?
          id_token          String?
          session_state     String?
          user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)
          @@unique([provider, providerAccountId])
        }

        model Session {
          id           String   @id @default(cuid())
          sessionToken String   @unique
          userId       String
          expires      DateTime
          user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
        }

        model VerificationToken {
          identifier String
          token      String   @unique
          expires    DateTime
          @@unique([identifier, token])
        }

        // App data
        model Todo {
          id          String   @id @default(uuid())
          title       String
          completed   Boolean  @default(false)
          user_id     String
          created_at  DateTime @default(now())

          owner       User     @relation(fields: [user_id], references: [id], onDelete: Cascade)

          @@index([user_id])
        }
        ```

        ### Server actions untuk mutate

        Pakai server actions untuk CRUD — lebih simpel daripada API route + fetch.

        ```ts
        // app/todos/actions.ts
        "use server";

        import { auth } from "@/auth";
        import { db } from "@/lib/db";
        import { revalidatePath } from "next/cache";

        export async function createTodo(formData: FormData) {
          const session = await auth();
          if (!session?.user?.id) throw new Error("Unauthorized");

          const title = String(formData.get("title") ?? "").trim();
          if (!title) return;

          await db.todo.create({
            data: { title, user_id: session.user.id },
          });

          revalidatePath("/todos");
        }

        export async function toggleTodo(id: string) {
          const session = await auth();
          if (!session?.user?.id) throw new Error("Unauthorized");

          // Pastikan owner
          const todo = await db.todo.findFirst({
            where: { id, user_id: session.user.id },
          });
          if (!todo) throw new Error("Not found");

          await db.todo.update({
            where: { id },
            data: { completed: !todo.completed },
          });

          revalidatePath("/todos");
        }

        export async function deleteTodo(id: string) {
          const session = await auth();
          if (!session?.user?.id) throw new Error("Unauthorized");

          const todo = await db.todo.findFirst({
            where: { id, user_id: session.user.id },
          });
          if (!todo) throw new Error("Not found");

          await db.todo.delete({ where: { id } });
          revalidatePath("/todos");
        }
        ```

        Kunci di sini: `where: { id, user_id: session.user.id }` — query ini secara otomatis cuma cocok kalau todo benar-benar milik user yang sedang login.

        ### Halaman /todos

        ```tsx
        // app/todos/page.tsx
        import { auth } from "@/auth";
        import { db } from "@/lib/db";
        import { redirect } from "next/navigation";
        import { createTodo, toggleTodo, deleteTodo } from "./actions";

        export default async function TodosPage() {
          const session = await auth();
          if (!session?.user?.id) redirect("/login");

          const todos = await db.todo.findMany({
            where: { user_id: session.user.id },
            orderBy: { created_at: "desc" },
          });

          return (
            <main className="mx-auto max-w-2xl p-8">
              <h1 className="text-3xl font-semibold">Todo saya</h1>

              <form action={createTodo} className="mt-6 flex gap-2">
                <input
                  name="title"
                  placeholder="Tugas baru..."
                  className="flex-1 rounded border p-2"
                  required
                />
                <button className="rounded bg-blue-500 px-4 text-white">
                  Tambah
                </button>
              </form>

              <ul className="mt-8 space-y-2">
                {todos.map((t) => (
                  <li key={t.id} className="flex items-center gap-3 rounded border p-3">
                    <form action={toggleTodo.bind(null, t.id)}>
                      <button className={t.completed ? "line-through" : ""}>
                        {t.completed ? "✓" : "○"}
                      </button>
                    </form>

                    <span className={`flex-1 ${t.completed ? "line-through text-gray-400" : ""}`}>
                      {t.title}
                    </span>

                    <form action={deleteTodo.bind(null, t.id)}>
                      <button className="text-sm text-red-500">Hapus</button>
                    </form>
                  </li>
                ))}
              </ul>
            </main>
          );
        }
        ```

        Tidak ada `useState`, tidak ada `useEffect`, tidak ada fetch manual. Semua server-side.

        ### Test owner-based authorization

        Bikin dua akun Google. Login akun A, bikin todo. Logout. Login akun B. Halaman `/todos` harus kosong (todo milik A tidak terlihat).

        Coba "trick" lebih jauh: dapatkan ID todo milik A, lalu coba toggle/delete sebagai user B. Server harus reject.

        ### Deploy ke Vercel

        Push ke GitHub, import di Vercel. Set semua env variable di Vercel:

        ```bash
        DATABASE_URL=...
        DIRECT_URL=...
        AUTH_SECRET=...
        AUTH_URL=https://your-app.vercel.app
        GOOGLE_CLIENT_ID=...
        GOOGLE_CLIENT_SECRET=...
        ```

        Update Google Console: tambah `https://your-app.vercel.app/api/auth/callback/google` ke Authorized redirect URIs.

        Deploy. Test login + bikin todo + logout di production URL.

        ### Submit

        Bagikan URL ke teman. Pastikan dua orang berbeda bisa pakai tanpa lihat data satu sama lain.
        """
    ),
    contoh_code_md=dedent(
        """\
        Server action untuk create todo dengan validasi:

        ```ts
        // app/todos/actions.ts
        "use server";

        import { auth } from "@/auth";
        import { db } from "@/lib/db";
        import { revalidatePath } from "next/cache";

        export async function createTodo(formData: FormData) {
          const session = await auth();
          if (!session?.user?.id) {
            throw new Error("Harus login dulu");
          }

          const title = String(formData.get("title") ?? "").trim();
          if (!title) return { error: "Title tidak boleh kosong" };
          if (title.length > 200) return { error: "Title terlalu panjang" };

          await db.todo.create({
            data: {
              title,
              user_id: session.user.id,
            },
          });

          revalidatePath("/todos");
        }
        ```

        Pakai dari form di halaman:

        ```tsx
        <form action={createTodo} className="flex gap-2">
          <input name="title" required maxLength={200} className="flex-1 rounded border p-2" />
          <button type="submit" className="rounded bg-blue-500 px-4 text-white">
            Tambah
          </button>
        </form>
        ```

        Form action server-side = tidak perlu fetch manual, tidak perlu state management.
        """
    ),
    practice=(
        "Bangun todo app sesuai spec di atas. Test owner-based authorization "
        "dengan dua akun Google. Deploy ke Vercel. Catat URL — share ke "
        "minimal satu teman dan pastikan data kalian terpisah."
    ),
    fix_error={
        "language": "ts",
        "broken_code": dedent(
            """\
            export async function deleteTodo(id: string) {
              const session = await auth();
              if (!session) throw new Error("Unauthorized");

              await db.todo.delete({ where: { id } });
              revalidatePath("/todos");
            }
            """
        ),
        "hint": "Endpoint ini punya celah keamanan besar. User bisa delete todo milik orang lain.",
        "answer_explanation": dedent(
            """\
            Kesalahan: cuma cek user login (`session` ada), tapi tidak cek apakah todo itu milik user.

            Skenario: user A login, dapat list todo-nya. User A tahu format ID. User A coba delete dengan ID todo milik user B → terhapus. Itu vulnerability.

            Solusi: query dengan filter `user_id: session.user.id`. Kalau tidak match (tidak ditemukan), berarti bukan milik user — return 404 atau 403.
            """
        ),
        "fixed_code": dedent(
            """\
            export async function deleteTodo(id: string) {
              const session = await auth();
              if (!session?.user?.id) throw new Error("Unauthorized");

              // Pastikan todo milik user yang login
              const todo = await db.todo.findFirst({
                where: { id, user_id: session.user.id },
              });
              if (!todo) throw new Error("Tidak ditemukan");

              await db.todo.delete({ where: { id: todo.id } });
              revalidatePath("/todos");
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa keuntungan Server Actions dibanding API route + fetch di project ini?",
            [
                "Lebih lambat",
                "Lebih ringkas: tidak butuh API route, tidak butuh fetch manual, tidak butuh state management untuk form",
                "Tidak ada keuntungan",
                "Wajib pakai",
            ],
            "B",
            "Server Actions kurangi boilerplate. Form langsung connect ke server function. Cocok untuk mutation simpel.",
        ),
        q(
            "Mengapa cek `where: { id, user_id: session.user.id }` lebih aman daripada cek session saja?",
            [
                "Tidak ada bedanya",
                "Pastikan operasi cuma jalan kalau todo benar-benar milik user — mencegah user lain manipulasi via ID",
                "Lebih cepat",
                "Untuk styling",
            ],
            "B",
            "Authorization beda dari authentication. Session cek 'siapa kamu', tapi belum tentu kamu boleh akses resource itu. Filter berdasarkan owner = layer kedua.",
        ),
        q(
            "Apa yang dilakukan `revalidatePath('/todos')` setelah mutation?",
            [
                "Reload halaman",
                "Memberitahu Next.js untuk fetch ulang data di halaman /todos saat user kembali",
                "Refresh database",
                "Tidak ada efek",
            ],
            "B",
            "Tanpa revalidatePath, halaman tetap menampilkan data lama (cached). Setelah revalidate, data fresh saat di-render lagi.",
        ),
        q(
            "Apa yang HARUS di-update di Google Console setelah deploy ke Vercel?",
            [
                "Tidak ada",
                "Tambahkan production URL ke Authorized redirect URIs (`https://your-app.vercel.app/api/auth/callback/google`)",
                "Hapus akun Google",
                "Restart Cloud Console",
            ],
            "B",
            "Google butuh tahu production URL eksplisit. Tanpa ini, OAuth callback gagal dengan error 'redirect_uri_mismatch'.",
        ),
        q(
            "Mana cara test owner-based authorization yang TEPAT?",
            [
                "Cuma test sebagai satu user",
                "Login dengan dua akun berbeda, pastikan masing-masing tidak bisa lihat/edit data milik yang lain",
                "Tidak perlu test",
                "Test dengan production",
            ],
            "B",
            "Multi-account testing adalah satu-satunya cara konfirm authorization bener-bener jalan. Single account test = blind spot.",
        ),
    ],
    common_mistakes=[
        "Cek session tapi lupa filter berdasarkan owner. Vulnerability authorization.",
        "Lupa update Google Console redirect URIs setelah deploy. Login gagal di production.",
        "Tidak revalidatePath setelah mutate. Data tampil basi.",
    ],
    checkpoint=[
        "Todo app live di Vercel.",
        "Login dengan Google bisa, logout bisa.",
        "Multi-account test pass: user A tidak bisa lihat todo user B.",
        "Server action pakai pola filter owner, bukan cuma cek session.",
    ],
    xp_reward=600,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=4,
    slug="database-backend-basics",
    title="Database & Backend Basics",
    subtitle="Data yang beneran tersimpan",
    description=(
        "Konsep database, setup Supabase + Prisma, auth dengan NextAuth + "
        "Google OAuth. Tutup dengan todo app fullstack yang punya owner-based "
        "authorization dan deployed ke production."
    ),
    duration="~3 minggu",
    difficulty="Menengah",
    accent_color="from-emerald-400/30 to-violet-500/10",
    mini_project="Todo App dengan Auth",
    tags=["Supabase", "Prisma", "NextAuth", "Server Actions"],
    lessons=[LESSON_DB_VIBE, LESSON_SUPABASE, LESSON_AUTH_NEXT, PROJECT_TODO_AUTH],
)
