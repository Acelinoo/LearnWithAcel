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
    title="Database buat Vibe Coder",
    slug="database-untuk-vibe-coder",
    order_index=1,
    read_time="11 menit",
    summary="Konsep database tanpa istilah ribet, plus cara prompt schema ke AI.",
    tools=["Notes app", "Browser"],
    outcomes=[
        "Paham konsep tabel, kolom, baris pake analogi sehari-hari",
        "Tau kapan app butuh database",
        "Bisa prompt AI buat generate Prisma schema",
    ],
    tldr=(
        "Database = lemari arsip digital. Tabel = laci buat tiap kategori. "
        "Kolom = atribut tiap berkas. Baris = satu record. Kasih AI deskripsi "
        "model data, dia generate Prisma schema."
    ),
    pembuka=dedent(
        """\
        Sampe sini app kamu masih ilang datanya pas refresh. Catetan ditulis, langsung ilang pas tab ditutup.

        Buat app beneran, kamu butuh database — tempat data tersimpen permanen sama bisa di-query siapa aja yang punya akses.

        Lesson ini ngebedah konsep database tanpa istilah teknis.
        """
    ),
    penjelasan=dedent(
        """\
        ### Analogi: lemari arsip kantor

        Mikir kantor zaman dulu yang punya banyak lemari arsip:

        - **Lemari "Karyawan"** isinya map buat tiap karyawan. Tiap map ada: foto, nama, jabatan, tanggal masuk.
        - **Lemari "Proyek"** isinya map buat tiap proyek. Tiap map ada: nama proyek, status, deadline, karyawan yang terlibat.
        - **Lemari "Gaji"** isinya map buat tiap pembayaran. Tiap map ada: tanggal, nominal, karyawan penerima.

        Database modern kerjanya persis kayak gini:

        - **Lemari** = **tabel**.
        - **Map dalam lemari** = **baris** (record).
        - **Atribut di tiap map** = **kolom**.

        Tiap record bisa terhubung ke record di lemari lain (proyek terhubung ke karyawan lewat "diisi sama").

        ### Kapan app butuh database

        Gak semua app butuh database. Kamu butuh kalau salah satu kondisi ini muncul:

        - Data harus tetep ada walau tab/HP/komputer ditutup.
        - Data harus dishare antar user (komentar, pesan, post).
        - Data harus bisa dicari/di-filter pake kriteria tertentu.
        - Data tumbuh gede dari waktu ke waktu (ribuan/jutaan record).

        Kalau cuma tampilan statis kayak landing page atau portfolio, **gak butuh database**. Hardcode data di file udah cukup.

        ### Anatomi tabel

        Bayangin tabel `users`:

        ```text
        ┌──────┬──────────────────┬──────────────┬─────────────────────┐
        │  id  │      email       │  full_name   │     created_at      │
        ├──────┼──────────────────┼──────────────┼─────────────────────┤
        │   1  │ acel@email.com   │  Acel        │  2026-01-15 10:00   │
        │   2  │ budi@email.com   │  Budi        │  2026-01-16 14:30   │
        │   3  │ citra@email.com  │  Citra       │  2026-01-17 09:00   │
        └──────┴──────────────────┴──────────────┴─────────────────────┘
        ```

        - **id** — kolom unik buat identifikasi (kayak nomor map). Disebut primary key.
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

        Hasilnya: post 100 sama 101 dimiliki user 1 (Acel). Post 102 milik user 2 (Budi). Ini namanya **foreign key relationship**.

        ### SQL vs NoSQL

        Dua kelompok gede database:

        - **SQL (relational)** — data terstruktur dalam tabel-tabel yang saling terhubung. PostgreSQL, MySQL, SQLite.
        - **NoSQL (document)** — data lebih fleksibel, mirip JSON. MongoDB, Firebase Firestore.

        Buat vibe coder, **PostgreSQL via Supabase** itu pilihan default. Alesannya:

        - Skill SQL berlaku di banyak tempat.
        - Free tier Supabase gede.
        - Auth + storage + realtime udah built-in.

        ### Cara prompt schema ke AI

        Daripada nulis Prisma schema dari nol, deskripsiin model data ke AI:

        > Saya mau bikin app habit tracker. Model data:
        >
        > - User: punya banyak habit sama banyak check-in.
        > - Habit: dimiliki user, punya nama, deskripsi, target frekuensi (harian/mingguan).
        > - CheckIn: dimiliki user sama habit, dengan tanggal sama catatan opsional.
        >
        > Generate Prisma schema sama PostgreSQL provider, primary key UUID, sama timestamp buat created_at.

        AI bakal kasih schema lengkap dengan relasi yang bener. Kamu tinggal review.

        ### Aturan emas

        - **Mulai sederhana.** 3-5 model cukup buat MVP.
        - **Pake UUID buat primary key.** Lebih aman daripada integer auto-increment.
        - **Snake_case buat nama kolom.** Contoh: `created_at`, `user_id`. Kebiasaan yang umum.
        - **Tambah `created_at` sama `updated_at` ke semua model.** Berguna buat debugging sama analytics.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh Prisma schema buat app habit tracker:

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

        Tiga model, semua punya UUID, ada cascade delete (kalau user dihapus, habit sama checkin ikut kehapus), sama index buat query cepet.
        """
    ),
    practice=(
        "Mikirin satu app yang pengen kamu bangun. Tulis di catetan: berapa "
        "model data yang dibutuhin, apa kolom-kolomnya, gimana mereka saling "
        "terhubung. Terus prompt AI buat generate Prisma schema-nya."
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
            "Empat masalah: penamaan model, primary key, kolom unique, sama "
            "deklarasi relasi."
        ),
        "answer_explanation": dedent(
            """\
            1. Nama model **wajib PascalCase** — `User` bukan `user`.
            2. Primary key butuh `@id`. Saran modern pake `String @default(uuid())`.
            3. Email harus `@unique` biar gak ada duplikat.
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
            "Mana analogi yang paling pas buat database?",
            [
                "Aplikasi WhatsApp",
                "Lemari arsip yang terorganisir sama banyak laci, tiap laci buat kategori beda",
                "Spreadsheet di komputer",
                "Browser bookmark",
            ],
            "B",
            "Lemari arsip = tabel-tabel yang terhubung. Tiap map = record. Atribut map = kolom. Ini analogi yang paling akurat.",
        ),
        q(
            "Kapan app TIDAK butuh database?",
            [
                "Gak ada — app selalu butuh database",
                "Pas data statis (landing page, portfolio) sama gak perlu disimpen buat user",
                "Pas ada login",
                "Pas ada chat",
            ],
            "B",
            "Landing page, portfolio, dokumentasi statis gak butuh database. Hardcode data di file lebih simpel.",
        ),
        q(
            "Fungsi `@unique` di Prisma itu apa?",
            [
                "Mempercepat query",
                "Mastiin gak ada duplikat di kolom itu (misal: email gak boleh sama antar user)",
                "Auto-encrypt",
                "Gak ada fungsi",
            ],
            "B",
            "Aturan database biar data konsisten. Tanpa unique di email, dua user bisa daftar pake email sama — kacau.",
        ),
        q(
            "Mana primary key yang DIREKOMENDASIKAN?",
            [
                "Integer auto-increment (1, 2, 3, ...)",
                "UUID (`String @id @default(uuid())`)",
                "Email user",
                "Nama lengkap",
            ],
            "B",
            "UUID acak panjang jadi gak bisa ditebak, aman dipake di URL publik, sama gak konflik pas data di-merge dari sumber beda.",
        ),
        q(
            "Apa yang dilakuin `onDelete: Cascade` di relasi Prisma?",
            [
                "Backup otomatis sebelum delete",
                "Pas parent dihapus, semua child yang terhubung ikut kehapus",
                "Mencegah delete",
                "Gak ada efek",
            ],
            "B",
            "Cascade delete jaga konsistensi. Kalau User dihapus, Post-nya juga harus kehapus — gak boleh ada Post tanpa author.",
        ),
    ],
    common_mistakes=[
        "Lowercase nama model di Prisma. Generator-nya bakal complain.",
        "Lupa `@unique` di kolom email. Bisa duplikat, masalah pas login.",
        "Pake integer auto-increment di production. Bocor info jumlah user, gak aman di URL.",
    ],
    checkpoint=[
        "Bisa jelasin database pake analogi lemari arsip.",
        "Bisa baca dan nulis Prisma schema sederhana.",
        "Tau kapan app butuh database.",
        "Bisa prompt AI buat generate schema dari deskripsi model data.",
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
        "Bisa bikin project Supabase sama database PostgreSQL",
        "Bisa setup Prisma di Next.js",
        "Bisa push schema sama jalanin query pertama",
    ],
    tldr=(
        "Supabase kasih PostgreSQL gratis dalam < 5 menit. Konek ke Next.js "
        "lewat Prisma. Habis `prisma db push`, tabel siap dipake."
    ),
    pembuka=dedent(
        """\
        Bikin database dari nol biasanya ribet: install PostgreSQL, set password, manage versi. Makan waktu sebelum nulis satu baris kode pun.

        Supabase ngehapus semua hambatan itu. Sign up, klik new project, tunggu 2 menit. Selesai. Kamu punya PostgreSQL siap pake.

        Lesson ini step by step setup-nya plus integrasi ke project Next.js.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu Supabase

        Supabase itu platform "alternatif Firebase" yang dibangun di atas PostgreSQL. Free tier-nya gede banget buat hobi/MVP.

        Yang kamu dapet:

        - **PostgreSQL database** sama dashboard SQL editor.
        - **Auth** built-in (email + OAuth Google/GitHub/dll).
        - **Storage** buat upload file.
        - **Realtime** buat dengerin perubahan database.
        - **Auto-generated REST + GraphQL API** kalau mau pake langsung tanpa backend custom.

        Buat vibe coder, kombinasi yang paling sering: Supabase buat database + auth, Prisma sebagai ORM.

        ### Step 1 — Bikin project Supabase

        - Buka [supabase.com](https://supabase.com), Sign up pake GitHub.
        - **New Project** → kasih nama, password DB yang kuat (simpen di password manager), pilih region terdekat (Singapore buat Asia).
        - Tunggu sekitar 2 menit buat provisioning.

        Habis selesai, kamu masuk ke dashboard project. Di sini ada SQL editor, Auth panel, Storage, sama Logs.

        ### Step 2 — Salin connection string

        - Buka **Project Settings → Database**.
        - Cari section **Connection string**. Ada beberapa format:
          - **Direct connection (port 5432)** — buat migration sama dev.
          - **Connection pooling - Transaction (port 6543)** — buat runtime, **paling sering dipake**.
          - **Connection pooling - Session (port 5432)** — buat session-based.

        Buat Prisma + Next.js, paling aman pake **Direct (5432)** buat migration sama **Pooler Transaction (6543)** buat runtime.

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
        # Buat runtime (pooler)
        DATABASE_URL="postgresql://postgres.xxx:password@aws-0-region.pooler.supabase.com:6543/postgres?pgbouncer=true"

        # Buat migration (direct)
        DIRECT_URL="postgresql://postgres.xxx:password@aws-0-region.pooler.supabase.com:5432/postgres"
        ```

        Salin URL dari dashboard Supabase. Pastiin password udah di-replace.

        ### Step 4 — Push schema

        ```bash
        npx prisma db push
        ```

        Prisma bikin tabel di Supabase. Buka dashboard Supabase → Table Editor → kamu harusnya ngeliat tabel `User` muncul.

        ```bash
        npx prisma generate
        ```

        Generate Prisma Client TypeScript. Sekarang kamu bisa import sama pake dari kode.

        ### Step 5 — Singleton Prisma di Next.js

        Next.js dev mode hot-reload sering bikin Prisma Client multiple instance → memory leak warning. Solusinya: bikin singleton.

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

        Pake dari mana aja:

        ```ts
        import { db } from "@/lib/db";

        const users = await db.user.findMany();
        ```

        ### Test cepet

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

        Buka `http://localhost:3000/api/test`. Kamu harusnya dapet `{ count: 0, users: [] }`.

        Coba bikin user dari Supabase Table Editor (klik "Insert row"). Refresh API → user-nya muncul.

        ### Aturan keamanan

        - **JANGAN commit `.env.local`**. Tambahin ke `.gitignore`.
        - **JANGAN expose `DATABASE_URL` ke client.** Variabel TANPA prefix `NEXT_PUBLIC_` aman di server, gak ke-bundle ke browser.
        - **Pake password manager** buat simpen password DB.
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
              { error: "Email sama full_name wajib" },
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
        "Setup Supabase project baru, Prisma di project Next.js kamu, sama "
        "push schema model `User` sederhana. Bikin endpoint `/api/users` "
        "dengan GET sama POST. Test create user dari Postman, terus list "
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
            "Pas dev mode hot-reload, kamu bakal dapet warning multiple "
            "PrismaClient instance. Apa yang salah?"
        ),
        "answer_explanation": dedent(
            """\
            Salahnya: `new PrismaClient()` dipanggil tiap render. Hot-reload bikin instance baru terus, akhirnya warning "too many connections".

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
            "Apa yang ditawarin Supabase free tier?",
            [
                "Cuma database",
                "PostgreSQL + Auth + Storage + Realtime + auto-generated API",
                "Cuma hosting",
                "Gak ada",
            ],
            "B",
            "Supabase = backend-as-a-service. Buat MVP, sering gak butuh backend custom — Supabase aja udah cukup.",
        ),
        q(
            "Beda DATABASE_URL sama DIRECT_URL di Prisma + Supabase?",
            [
                "Gak ada bedanya",
                "DATABASE_URL buat runtime (pooler), DIRECT_URL buat migration",
                "Salah satu cuma buat testing",
                "DIRECT_URL buat frontend",
            ],
            "B",
            "Pooler aman buat runtime karena handle banyak connection. Migration butuh direct karena pooler gak support DDL.",
        ),
        q(
            "Kenapa kita butuh singleton PrismaClient di Next.js dev mode?",
            [
                "Buat gaya",
                "Hot-reload bikin instance PrismaClient baru terus → warning 'too many connections'",
                "Lebih cepet",
                "Gak butuh",
            ],
            "B",
            "Pola singleton lewat globalThis itu workaround standar di komunitas Next.js + Prisma.",
        ),
        q(
            "Apa yang HARUS dilakuin sama `.env.local`?",
            [
                "Commit ke GitHub biar temen bisa pake",
                "Tambahin ke `.gitignore` sama jangan pernah commit",
                "Upload ke cloud",
                "Email ke supabase",
            ],
            "B",
            "DATABASE_URL isinya password database. Bocor sekali, akses penuh ke data. .gitignore wajib.",
        ),
        q(
            "Apa yang terjadi habis `npx prisma db push`?",
            [
                "Gak ada",
                "Prisma sinkronin tabel di database sesuai schema.prisma",
                "Schema dihapus",
                "Database di-format",
            ],
            "B",
            "`db push` cocok buat dev. Buat production sebaiknya pake `prisma migrate` biar history schema kesimpen rapi.",
        ),
    ],
    common_mistakes=[
        "Commit `.env.local` ke GitHub. Password database bocor.",
        "Pake DATABASE_URL pooler buat migration. Migration gagal karena pooler gak support DDL.",
        "`new PrismaClient()` di tiap file. Memory leak di dev mode.",
    ],
    checkpoint=[
        "Project Supabase aktif sama PostgreSQL siap pake.",
        "Prisma terhubung sama schema ke-push.",
        "Bisa CRUD lewat API route Next.js.",
        "Singleton db.ts udah dibikin sama dipake konsisten.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Auth dengan NextAuth (Auth.js)
# ─────────────────────────────────────────────────────────────────────────────

LESSON_AUTH_NEXT = make_lesson(
    title="Auth Pake NextAuth",
    slug="auth-dengan-nextauth",
    order_index=3,
    read_time="14 menit",
    summary="Login/register pake NextAuth + Prisma adapter, plus protected routes.",
    tools=["Project Next.js + Prisma + Supabase", "Akun Google (buat OAuth)", "Cursor"],
    outcomes=[
        "Bisa setup NextAuth (Auth.js v5) di project Next.js",
        "Bisa auth pake email/password + Google OAuth",
        "Bisa proteksi halaman lewat session check",
    ],
    tldr=(
        "NextAuth (Auth.js) handle alur auth lengkap. Setup provider (email/"
        "Google), pake Prisma adapter buat simpen session/user di DB. "
        "Proteksi halaman pake `auth()` di server component."
    ),
    pembuka=dedent(
        """\
        Auth itu fitur yang hampir tiap app butuh. Tapi kalau nulis dari nol, kamu harus handle: hash password, generate token, manage session, OAuth flow, password reset.

        NextAuth (sekarang Auth.js) abstrakin semua itu. Kamu kasih config, dia urusin sisanya.

        Buat vibe coder, ini stack default — sebagian besar SaaS production di komunitas Next.js pake pola kayak gini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu NextAuth (Auth.js)

        NextAuth itu library authentication buat Next.js. Versi terbarunya namanya **Auth.js v5** (masih sering disebut NextAuth).

        Yang kamu dapet:

        - Login pake **provider** (email/password, Google, GitHub, Discord, dll).
        - Session management (cookie httpOnly, otomatis).
        - Database adapter (Prisma, Drizzle, dll) buat simpen user.
        - Helper buat protected route.
        - CSRF protection udah built-in.

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
        middleware.ts                ← opsional: protect lewat middleware
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

        ### Schema yang dibutuhin Prisma adapter

        Prisma adapter butuh model `User`, `Account`, `Session`, sama `VerificationToken`. Generate pake:

        ```bash
        # Di docs Auth.js, ada SQL schema yang siap pake
        # Atau prompt AI: "Bikin Prisma schema buat Auth.js v5 adapter"
        ```

        Saran: copy schema standar dari [authjs.dev/getting-started/adapters/prisma](https://authjs.dev/getting-started/adapters/prisma).

        ### Setup Google OAuth credentials

        - Buka [console.cloud.google.com](https://console.cloud.google.com).
        - Bikin project baru.
        - **APIs & Services → Credentials → Create Credentials → OAuth Client ID**.
        - Application type: Web Application.
        - Authorized redirect URI: `http://localhost:3000/api/auth/callback/google` (buat dev) sama domain Vercel (buat production).
        - Salin Client ID sama Client Secret ke `.env.local`.

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
              <button type="submit">Login pake Google</button>
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

        Gak butuh `useState`, gak butuh fetch token manual. NextAuth handle semua di balik layar.

        ### Proteksi lewat middleware (alternatif)

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

        Middleware jalan di edge sebelum request masuk ke route. Lebih efisien buat redirect blanket.

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

        AUTH_SECRET="generate pake: openssl rand -base64 32"
        AUTH_URL="http://localhost:3000"

        GOOGLE_CLIENT_ID="xxx.apps.googleusercontent.com"
        GOOGLE_CLIENT_SECRET="xxx"
        ```

        Pas deploy ke Vercel, salin semua ke env Vercel (kecuali AUTH_URL — Vercel set otomatis).
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
                <h2 className="font-semibold">Selamat datang di dashboard</h2>
                <p className="mt-2 text-sm text-gray-600">
                  Halaman ini cuma bisa diakses kalau kamu udah login.
                </p>
              </div>
            </main>
          );
        }
        ```
        """
    ),
    practice=(
        "Setup NextAuth pake Google OAuth di project Next.js kamu. Bikin "
        "halaman `/login` sama tombol Google, sama halaman `/dashboard` yang "
        "protected (redirect ke login kalau belum auth). Test login sama "
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
            "Cara ini jalan, tapi rentan sama ribet buat Next.js modern. Apa "
            "cara yang lebih elegan pake NextAuth?"
        ),
        "answer_explanation": dedent(
            """\
            Masalah:

            1. Pake `localStorage` buat token = rentan XSS.
            2. Loading state manual = flickering UX.
            3. Client-side redirect = halaman sempet muncul sebelum redirect.

            Solusi: pake server component sama `auth()`. Cek session di server, redirect sebelum HTML dikirim. NextAuth pake cookie httpOnly otomatis — aman dari XSS.
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
            "Fungsi Prisma adapter di NextAuth?",
            [
                "Generate UI",
                "Nyimpen user, account, session, sama verification token ke database lewat Prisma",
                "Buat styling",
                "Gak ada",
            ],
            "B",
            "Adapter itu jembatan antara NextAuth sama database kamu. Tanpa adapter, session disimpen di memori.",
        ),
        q(
            "Mana cara protect halaman yang LEBIH BAGUS di Next.js App Router?",
            [
                "Cek `localStorage` di useEffect",
                "Pake `auth()` di server component, redirect kalau gak ada session",
                "Gak perlu protect",
                "Hide tombol aja",
            ],
            "B",
            "Server-side protection lebih aman sama UX lebih bagus (gak flicker). Server tau session sebelum HTML dikirim.",
        ),
        q(
            "Apa yang HARUS ada di `.env.local` buat NextAuth + Google?",
            [
                "Cuma DATABASE_URL",
                "AUTH_SECRET, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, DATABASE_URL",
                "Cuma password",
                "Gak ada env",
            ],
            "B",
            "AUTH_SECRET buat sign cookie, Google credentials buat OAuth, DATABASE_URL buat simpen session. Semua wajib.",
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
            "httpOnly cookie gak bisa diakses JavaScript = aman dari XSS. NextAuth pake ini secara default.",
        ),
        q(
            "Apa yang dimaksud `redirect URI` pas setup Google OAuth?",
            [
                "URL buat login",
                "URL callback yang Google panggil habis user login (misal `/api/auth/callback/google`)",
                "URL homepage",
                "URL dashboard",
            ],
            "B",
            "Habis user login di Google, Google redirect balik ke aplikasi kamu di URL ini. Wajib di-whitelist di Google Console.",
        ),
    ],
    common_mistakes=[
        "Pake localStorage buat token. Rentan XSS.",
        "Lupa whitelist redirect URI di Google Console. OAuth gagal sama error 'redirect_uri_mismatch'.",
        "Cek session di client component padahal bisa di server component. Hasilnya UX flickering.",
    ],
    checkpoint=[
        "NextAuth setup sama Google OAuth aktif.",
        "Halaman protected redirect ke /login kalau gak ada session.",
        "Logout jalan.",
        "Schema Prisma adapter (User, Account, Session, VerificationToken) ke-push.",
    ],
    xp_reward=200,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_TODO_AUTH = make_lesson(
    title="Mini Project — Todo App sama Auth",
    slug="mini-project-todo-with-auth",
    order_index=4,
    read_time="180 menit",
    summary="Fullstack todo: login Google, data per user, deploy live.",
    tools=["Next.js + Prisma + Supabase + NextAuth", "Cursor", "Vercel"],
    outcomes=[
        "Bisa bikin fullstack app sama auth dan database",
        "Bisa pake owner-based authorization",
        "Bisa deploy ke production sama environment variables yang bener",
    ],
    tldr=(
        "Bangun todo app sama login Google. Tiap user cuma lihat sama edit "
        "todo miliknya. Deploy ke Vercel. Stack: Next.js + Prisma + "
        "Supabase + NextAuth + shadcn."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungin semua di Level 4: database, schema, auth, owner-based access, deploy.

        Hasilnya: todo app yang real, bisa dipake banyak user secara aman.

        Selesai project ini, kamu udah bisa bilang dengan jujur: 'Saya bisa bikin SaaS dasar dari nol.'
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind + shadcn/ui + Prisma + Supabase + NextAuth.

        Halaman:

        - `/` — landing page singkat sama tombol login.
        - `/login` — tombol "Login pake Google".
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

        ### Server actions buat mutate

        Pake server actions buat CRUD — lebih simpel daripada API route + fetch.

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

          // Pastiin owner
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

        Kunci di sini: `where: { id, user_id: session.user.id }` — query ini otomatis cuma cocok kalau todo bener-bener milik user yang lagi login.

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

        Gak ada `useState`, gak ada `useEffect`, gak ada fetch manual. Semua server-side.

        ### Test owner-based authorization

        Bikin dua akun Google. Login akun A, bikin todo. Logout. Login akun B. Halaman `/todos` harus kosong (todo milik A gak keliatan).

        Coba "trick" lebih lanjut: dapetin ID todo milik A, terus coba toggle/delete sebagai user B. Server harus reject.

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

        Update Google Console: tambahin `https://your-app.vercel.app/api/auth/callback/google` ke Authorized redirect URIs.

        Deploy. Test login + bikin todo + logout di production URL.

        ### Submit

        Share URL ke temen. Pastiin dua orang beda bisa pake tanpa lihat data satu sama lain.
        """
    ),
    contoh_code_md=dedent(
        """\
        Server action buat create todo sama validasi:

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
          if (!title) return { error: "Title gak boleh kosong" };
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

        Pake dari form di halaman:

        ```tsx
        <form action={createTodo} className="flex gap-2">
          <input name="title" required maxLength={200} className="flex-1 rounded border p-2" />
          <button type="submit" className="rounded bg-blue-500 px-4 text-white">
            Tambah
          </button>
        </form>
        ```

        Form action server-side = gak perlu fetch manual, gak perlu state management.
        """
    ),
    practice=(
        "Bangun todo app sesuai spec di atas. Test owner-based authorization "
        "pake dua akun Google. Deploy ke Vercel. Catet URL — share ke "
        "minimal satu temen sama pastiin data kalian terpisah."
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
        "hint": "Endpoint ini punya celah keamanan gede. User bisa delete todo milik orang lain.",
        "answer_explanation": dedent(
            """\
            Salahnya: cuma cek user login (`session` ada), tapi gak cek apakah todo itu milik user.

            Skenario: user A login, dapet list todo-nya. User A tau format ID. User A coba delete pake ID todo milik user B → kehapus. Itu vulnerability.

            Solusi: query sama filter `user_id: session.user.id`. Kalau gak match (gak ditemukan), berarti bukan miliknya — return 404 atau 403.
            """
        ),
        "fixed_code": dedent(
            """\
            export async function deleteTodo(id: string) {
              const session = await auth();
              if (!session?.user?.id) throw new Error("Unauthorized");

              // Pastiin todo milik user yang login
              const todo = await db.todo.findFirst({
                where: { id, user_id: session.user.id },
              });
              if (!todo) throw new Error("Gak ditemukan");

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
                "Lebih ringkes: gak butuh API route, gak butuh fetch manual, gak butuh state management buat form",
                "Gak ada keuntungan",
                "Wajib pake",
            ],
            "B",
            "Server Actions ngurangin boilerplate. Form langsung connect ke server function. Cocok buat mutation simpel.",
        ),
        q(
            "Kenapa cek `where: { id, user_id: session.user.id }` lebih aman daripada cek session aja?",
            [
                "Gak ada bedanya",
                "Pastiin operasi cuma jalan kalau todo bener-bener milik user — mencegah user lain manipulasi lewat ID",
                "Lebih cepet",
                "Buat styling",
            ],
            "B",
            "Authorization beda dari authentication. Session cek 'siapa kamu', tapi belum tentu kamu boleh akses resource itu. Filter berdasarkan owner = lapisan kedua.",
        ),
        q(
            "Apa yang dilakuin `revalidatePath('/todos')` habis mutation?",
            [
                "Reload halaman",
                "Ngasih tau Next.js buat fetch ulang data di halaman /todos pas user balik",
                "Refresh database",
                "Gak ada efek",
            ],
            "B",
            "Tanpa revalidatePath, halaman tetep nampilin data lama (cached). Habis revalidate, data fresh pas di-render lagi.",
        ),
        q(
            "Apa yang HARUS di-update di Google Console habis deploy ke Vercel?",
            [
                "Gak ada",
                "Tambahin URL production ke Authorized redirect URIs (`https://your-app.vercel.app/api/auth/callback/google`)",
                "Hapus akun Google",
                "Restart Cloud Console",
            ],
            "B",
            "Google butuh tau URL production secara eksplisit. Tanpa ini, OAuth callback gagal sama error 'redirect_uri_mismatch'.",
        ),
        q(
            "Mana cara test owner-based authorization yang TEPAT?",
            [
                "Cuma test sebagai satu user",
                "Login pake dua akun beda, pastiin masing-masing gak bisa lihat/edit data milik yang lain",
                "Gak perlu test",
                "Test pake production",
            ],
            "B",
            "Multi-account testing itu satu-satunya cara konfirm authorization bener-bener jalan. Single account test = blind spot.",
        ),
    ],
    common_mistakes=[
        "Cek session tapi lupa filter berdasarkan owner. Vulnerability authorization.",
        "Lupa update Google Console redirect URIs habis deploy. Login gagal di production.",
        "Gak revalidatePath habis mutate. Data tampilannya basi.",
    ],
    checkpoint=[
        "Todo app live di Vercel.",
        "Login pake Google bisa, logout bisa.",
        "Multi-account test pass: user A gak bisa lihat todo user B.",
        "Server action pake pola filter owner, bukan cuma cek session.",
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
        "Konsep database, setup Supabase + Prisma, auth pake NextAuth + "
        "Google OAuth. Tutup sama todo app fullstack yang punya owner-based "
        "authorization sama deployed ke production."
    ),
    duration="~3 minggu",
    difficulty="Menengah",
    accent_color="from-emerald-400/30 to-violet-500/10",
    mini_project="Todo App dengan Auth",
    tags=["Supabase", "Prisma", "NextAuth", "Server Actions"],
    lessons=[LESSON_DB_VIBE, LESSON_SUPABASE, LESSON_AUTH_NEXT, PROJECT_TODO_AUTH],
)
