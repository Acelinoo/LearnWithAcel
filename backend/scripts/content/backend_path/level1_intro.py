"""
Backend / Level 1 — Backend Beginner.

Lessons:
  1. apa-itu-backend
  2. apa-itu-api
  3. intro-database
  4. mini-project-rest-api-buku  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Apa itu Backend
# ─────────────────────────────────────────────────────────────────────────────

LESSON_APA_BACKEND = make_lesson(
    title="Apa itu Backend",
    slug="apa-itu-backend",
    order_index=1,
    read_time="10 menit",
    summary="Server, database, sama apa yang terjadi habis kamu klik tombol.",
    tools=["Browser DevTools (tab Network)", "Notes app"],
    outcomes=[
        "Bisa bedain frontend sama backend pake analogi nyata",
        "Bisa kenalin HTTP method sama status code dasar",
        "Bisa baca request/response di tab Network DevTools",
    ],
    tldr=(
        "Frontend = meja restoran (yang user lihat). Backend = dapur (yang "
        "kerja di belakang). Keduanya ngobrol lewat HTTP request/response. "
        "Method utama: GET, POST, PUT, DELETE."
    ),
    pembuka=dedent(
        """\
        Pas kamu klik 'Login' di Twitter, ada banyak hal yang kejadian dalam sepersekian detik.

        Tampilan yang kamu lihat itu frontend. Tapi yang verifikasi password, ambil data tweet, sama kirim balik — itu backend.

        Lesson ini ngebedah anatomi sederhananya: apa yang sebenernya kejadian di balik layar.
        """
    ),
    penjelasan=dedent(
        """\
        ### Analogi restoran

        Mikir website itu kayak restoran:

        - **Meja, menu, pelayan** = frontend. Itu yang kamu sentuh.
        - **Dapur** = backend. Tempat data dimasak. Kamu gak masuk ke dapur.
        - **Pelayan yang nganterin pesenan** = API. Jembatan antara meja sama dapur.
        - **Lemari bahan sama stok** = database. Tempat data tersimpan rapi.

        Pas kamu klik 'Login', frontend ngirim "permintaan" ke backend. Backend cek di database, terus kirim balik hasilnya: berhasil atau gagal.

        ### HTTP — bahasa percakapan

        Frontend sama backend ngobrol pake HTTP. Tiap percakapan punya format yang sama:

        - **Request** dari frontend → backend.
        - **Response** dari backend → frontend.

        Request isinya:

        - **Method.** Jenis aksi: `GET` (ambil), `POST` (bikin baru), `PUT` (update), `DELETE` (hapus).
        - **URL.** Alamat tujuan, misal `/api/users/42`.
        - **Headers.** Info tambahan (token auth, content-type).
        - **Body.** Data yang dikirim (cuma buat POST/PUT).

        Response isinya:

        - **Status code.** Angka yang njelasin hasilnya gimana.
        - **Body.** Data yang dikirim balik.

        ### Status code yang sering muncul

        - `200 OK` — sukses.
        - `201 Created` — sukses bikin data baru.
        - `400 Bad Request` — request kamu salah format.
        - `401 Unauthorized` — kamu belum login.
        - `403 Forbidden` — udah login tapi gak punya akses.
        - `404 Not Found` — datanya gak ada.
        - `500 Internal Server Error` — backend yang error.

        Dua kelompok gede: 2xx = sukses, 4xx = salah dari sisi user, 5xx = salah dari sisi server.

        ### REST — gaya ngomong yang umum

        REST itu kebiasaan cara nyusun URL sama method.

        - `GET /users` — daftar semua user.
        - `GET /users/42` — detail user dengan id 42.
        - `POST /users` — bikin user baru.
        - `PUT /users/42` — update user 42.
        - `DELETE /users/42` — hapus user 42.

        Pola ini konsisten sama gampang ditebak. Hampir semua API publik ngikutin pola ini.

        ### Coba lihat sendiri

        Buka satu situs apa aja, pencet F12 → tab Network. Refresh halaman. Kamu bakal lihat puluhan request. Klik salah satu buat lihat detail: method, status, headers, body.

        Itu yang sebenernya kejadian tiap detik di internet.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh request HTTP pas user login (versi sederhana):

        ```http
        POST /api/auth/login HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
          "email": "saya@email.com",
          "password": "rahasia123"
        }
        ```

        Response sukses:

        ```http
        HTTP/1.1 200 OK
        Content-Type: application/json

        {
          "access_token": "eyJhbGciOi...",
          "user": {
            "id": "abc-123",
            "email": "saya@email.com",
            "full_name": "Acel"
          }
        }
        ```

        Response gagal (password salah):

        ```http
        HTTP/1.1 401 Unauthorized
        Content-Type: application/json

        {
          "detail": "Email atau password salah"
        }
        ```
        """
    ),
    practice=(
        "Buka [github.com](https://github.com) di browser. Pencet F12 → "
        "Network. Refresh halaman. Klik request paling atas (biasanya yang "
        "URL-nya github.com itu sendiri). Catet: method, status code, sama "
        "satu header menarik yang muncul."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Frontend kirim:
              POST /api/users/42

            Tujuan: ambil detail user dengan id 42.

            Backend balas: 400 Bad Request "Method not allowed".
            """
        ),
        "hint": "Method sama tujuannya gak match. REST punya kebiasaan yang spesifik.",
        "answer_explanation": dedent(
            """\
            Salahnya: buat **ambil** data, pake `GET`, bukan `POST`. POST itu buat bikin data baru.

            Pola REST buat satu resource:

            - GET /users/42 → ambil
            - PUT /users/42 → update
            - DELETE /users/42 → hapus
            - POST /users → bikin user baru (tanpa id, server yang generate)
            """
        ),
        "fixed_code": dedent(
            """\
            Frontend kirim:
              GET /api/users/42

            Tujuan: ambil detail user dengan id 42.

            Backend balas: 200 OK { "id": "42", "email": "...", ... }
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dilakuin backend dalam analogi restoran?",
            [
                "Nganter pesenan ke meja",
                "Jadi tempat data diproses sama disimpen, kayak dapur",
                "Jadi menu yang dilihat user",
                "Cuma meja kasir",
            ],
            "B",
            "Backend = dapur. Tempat data dimasak, query database, sama logika bisnis dijalanin.",
        ),
        q(
            "Mana method HTTP yang BENER buat ngambil daftar user?",
            ["POST", "PUT", "GET", "DELETE"],
            "C",
            "GET dipake buat baca data. POST buat bikin baru, PUT buat update, DELETE buat hapus.",
        ),
        q(
            "Status code 401 Unauthorized artinya apa?",
            [
                "Server error",
                "User belum login atau token-nya gak valid",
                "Halaman gak ditemukan",
                "Sukses",
            ],
            "B",
            "401 artinya 'kamu belum buktiin siapa kamu'. Beda sama 403 yang artinya 'udah login tapi gak punya akses'.",
        ),
        q(
            "Fungsi tab Network di DevTools?",
            [
                "Ngubah CSS",
                "Liat semua HTTP request/response yang kejadian di halaman",
                "Edit file lokal",
                "Compile kode",
            ],
            "B",
            "Tab Network itu jendela ke percakapan HTTP. Penting banget pas debug masalah API.",
        ),
        q(
            "Mana URL REST yang KONSISTEN buat update user dengan id 42?",
            [
                "POST /update-user-42",
                "PUT /users/42",
                "GET /users/update/42",
                "DELETE /users/42",
            ],
            "B",
            "REST: PUT atau PATCH ke `/users/42` buat update. Method sama struktur URL itu kebiasaan.",
        ),
    ],
    common_mistakes=[
        "Pake POST buat semua aksi. Padahal GET/PUT/DELETE punya makna sendiri.",
        "Ngira 401 sama 403 itu sama. Bedanya: 401 = belum login, 403 = login tapi gak boleh.",
        "Lupa `Content-Type: application/json` di request POST. Server bingung parse body-nya.",
    ],
    checkpoint=[
        "Bisa jelasin beda frontend sama backend tanpa istilah teknis.",
        "Hafal 4 method utama HTTP sama kapan dipake.",
        "Tau beda status code 2xx/4xx/5xx.",
        "Bisa baca tab Network DevTools secara umum.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Apa itu API
# ─────────────────────────────────────────────────────────────────────────────

LESSON_API = make_lesson(
    title="Apa itu API",
    slug="apa-itu-api",
    order_index=2,
    read_time="11 menit",
    summary="REST API, JSON, sama cara manggil API publik dari browser.",
    tools=["Browser modern", "DevTools (Console + Network)"],
    outcomes=[
        "Paham API itu kontrak antar aplikasi",
        "Bisa baca sama nulis JSON",
        "Bisa manggil API publik lewat fetch dari Console",
    ],
    tldr=(
        "API = kontrak. Frontend kirim request sesuai kontrak, backend balas "
        "data dalam format JSON. fetch() itu cara JavaScript manggil API."
    ),
    pembuka=dedent(
        """\
        Pernah download cuaca harian di app HP? App-nya gak nyetak datanya sendiri.

        Dia minta ke API cuaca. API balas sama data: suhu, kelembaban, prediksi tiga hari ke depan. App kamu cuma nampilin.

        API itu jembatan antar aplikasi. Lesson ini ngebongkar cara kerjanya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Definisi sederhana

        API (Application Programming Interface) itu **kontrak komunikasi** antar aplikasi.

        Backend bilang: "Kalau kamu mau data X, kirim request ke `/path` pake method Y. Aku bakal balas pake format Z."

        Selama kontrak dipatuhi, frontend sama backend bisa develop terpisah. Tim backend bisa rewrite Python ke Go, frontend gak perlu tau — selama kontrak API-nya tetep sama.

        ### REST API — gaya yang dominan

        REST API ngelola **resource**. Resource = "benda" yang punya identitas (user, post, produk).

        Buat tiap resource, ada 5 endpoint umum:

        - `GET /products` — daftar produk.
        - `GET /products/42` — detail produk.
        - `POST /products` — bikin produk baru.
        - `PUT /products/42` — update produk.
        - `DELETE /products/42` — hapus.

        Jenis lain: GraphQL, gRPC, tRPC. Tapi buat pemula, REST yang paling sering ditemui.

        ### JSON — format data standar

        JSON (JavaScript Object Notation) itu cara nulis data yang gampang dibaca manusia sama mesin.

        ```json
        {
          "id": 42,
          "name": "Kopi Susu Gula Aren",
          "price": 18000,
          "tags": ["kopi", "manis", "lokal"],
          "available": true,
          "creator": {
            "id": 7,
            "name": "Pak Budi"
          }
        }
        ```

        Aturan JSON:

        - Object: `{ key: value }`. Key wajib pake kutip ganda.
        - Array: `[ item, item ]`.
        - Type: string, number, boolean, null, object, array. **Gak ada `undefined` di JSON.**
        - Gak boleh ada koma di akhir item terakhir (trailing comma).

        ### fetch — cara JavaScript manggil API

        ```js
        // GET request
        const res = await fetch("https://api.example.com/users");
        const data = await res.json();
        console.log(data);

        // POST request
        const res2 = await fetch("https://api.example.com/users", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name: "Acel", email: "saya@email.com" }),
        });
        const created = await res2.json();
        ```

        `fetch` ngembaliin Promise. Kita pake `await` buat nunggu, terus `res.json()` buat parse body jadi JavaScript object.

        ### Coba sendiri di Console

        Buka tab Console di DevTools, paste kode ini:

        ```js
        const res = await fetch("https://jsonplaceholder.typicode.com/users/1");
        const data = await res.json();
        console.log(data);
        ```

        Kamu bakal dapet object isinya data user dummy. JSONPlaceholder itu API publik gratis buat latihan.
        """
    ),
    contoh_code_md=dedent(
        """\
        Manggil API publik sama nampilin datanya:

        ```js
        async function ambilCuaca(kota) {
          try {
            const url = `https://api.example.com/weather?city=${kota}`;
            const res = await fetch(url);

            if (!res.ok) {
              throw new Error(`API error: ${res.status}`);
            }

            const data = await res.json();

            console.log(`Cuaca ${kota}:`);
            console.log(`Suhu: ${data.temperature}°C`);
            console.log(`Status: ${data.condition}`);

            return data;
          } catch (err) {
            console.error("Gagal ambil cuaca:", err.message);
          }
        }

        ambilCuaca("Jakarta");
        ```

        Pola umum: try/catch + cek `res.ok`. Karena `fetch` cuma reject pas network error — bukan pas status 404 atau 500.
        """
    ),
    practice=(
        "Buka Console di browser. Manggil API JSONPlaceholder ini:\n\n"
        "`fetch('https://jsonplaceholder.typicode.com/posts/1').then(r => r.json()).then(console.log)`\n\n"
        "Terus ubah angka 1 ke 5 — lihat datanya beda. Terus coba `/posts` "
        "(tanpa id) buat dapet daftar semua post."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            const res = fetch("https://api.example.com/users");
            const data = res.json();
            console.log(data.name);
            """
        ),
        "hint": "fetch sama json() dua-duanya asynchronous. Cek apa yang sebenernya kamu dapet tanpa await.",
        "answer_explanation": dedent(
            """\
            Salahnya: `fetch` ngembaliin **Promise**, bukan response langsung. Tanpa `await`, `res` itu Promise — dan `Promise.json()` gak ada.

            Solusinya: tambah `await` di kedua langkah, atau pake `.then()`. Function pembungkusnya juga harus `async`.
            """
        ),
        "fixed_code": dedent(
            """\
            async function ambilUsers() {
              const res = await fetch("https://api.example.com/users");
              const data = await res.json();
              console.log(data[0].name);
            }

            ambilUsers();

            // atau pake .then():
            // fetch("https://api.example.com/users")
            //   .then((r) => r.json())
            //   .then((data) => console.log(data[0].name));
            """
        ),
    },
    quiz=[
        q(
            "API dalam satu kalimat?",
            [
                "Bahasa pemrograman",
                "Kontrak komunikasi antar aplikasi",
                "Editor kode",
                "Library JavaScript",
            ],
            "B",
            "API itu kontrak. Selama kontrak dipatuhi, dua aplikasi bisa ngobrol tanpa peduli implementasi internalnya.",
        ),
        q(
            "Format data yang paling umum di REST API modern?",
            ["XML", "CSV", "JSON", "YAML"],
            "C",
            "JSON dominan karena ringan, gampang dibaca, sama nyatu sama JavaScript. XML dipake dulu, sekarang jarang.",
        ),
        q(
            "Apa yang dikembaliin `fetch(url)` di JavaScript?",
            [
                "Response data langsung",
                "Promise yang resolve jadi Response object",
                "String JSON",
                "Boolean",
            ],
            "B",
            "fetch ngembaliin Promise. Kita perlu `await` atau `.then()` buat dapet Response, terus `res.json()` buat parse body-nya.",
        ),
        q(
            "Beda `res.ok` sama gak adanya error fetch?",
            [
                "Gak ada beda",
                "fetch gak reject pas status 4xx/5xx — `res.ok` (true kalau 2xx) yang harus dicek manual",
                "`res.ok` cuma buat POST",
                "fetch otomatis throw pas 404",
            ],
            "B",
            "fetch cuma reject pas network error (offline, DNS, dll). Status 404 atau 500 tetep dianggep berhasil sampe ke kita. Jadi cek `res.ok` di kode.",
        ),
        q(
            "Mana JSON yang VALID?",
            [
                "{ name: 'Acel' }",
                '{ "name": "Acel", }',
                '{ "name": "Acel" }',
                "{ name = 'Acel' }",
            ],
            "C",
            "JSON wajib: kutip ganda di key, gak ada trailing comma, value sesuai tipe yang valid.",
        ),
    ],
    common_mistakes=[
        "Lupa `await` pas manggil `fetch`. Hasilnya bukan response, tapi Promise.",
        "Pake kutip tunggal di key JSON. Bukan JSON valid.",
        "Gak cek `res.ok`. Kode lanjut walau backend balas error.",
    ],
    checkpoint=[
        "Bisa jelasin apa itu API pake analogi pelayan restoran.",
        "Bisa baca sama nulis JSON sederhana.",
        "Bisa manggil API publik pake `fetch` di Console.",
        "Tau pentingnya cek `res.ok` sama handle error.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Intro Database
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DB = make_lesson(
    title="Kenalan sama Database & Prisma",
    slug="intro-database",
    order_index=3,
    read_time="13 menit",
    summary="SQL vs NoSQL, tabel, query dasar, sama Prisma sebagai ORM.",
    tools=["PostgreSQL (lokal atau Supabase)", "Node.js + Prisma", "VS Code"],
    outcomes=[
        "Paham konsep tabel, kolom, baris pake analogi spreadsheet",
        "Bisa baca query SQL dasar (SELECT, INSERT, UPDATE, DELETE)",
        "Bisa pake Prisma buat operasi database dari JavaScript",
    ],
    tldr=(
        "Database = lemari arsip. PostgreSQL = pilihan default yang aman. "
        "SQL = bahasa buat tanya-jawab sama database. Prisma = penerjemah "
        "antara JavaScript sama database — kamu nulis JS, dia generate SQL."
    ),
    pembuka=dedent(
        """\
        Variable di JavaScript ilang pas halaman ditutup. localStorage ilang pas user ganti browser.

        Buat data yang harus tetep ada buat semua user — daftar produk, comment, profil — kamu butuh database.

        Mikir database itu kayak lemari arsip raksasa yang terorganisir. Backend yang ngambilin file dari lemari ini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Dua kelompok gede

        - **SQL (Relational).** Data tersusun dalam tabel sama baris dan kolom yang jelas. Contoh: PostgreSQL, MySQL, SQLite. **Pilihan default buat pemula.**
        - **NoSQL (Document/Key-Value).** Data lebih fleksibel, mirip JSON. Contoh: MongoDB, Redis. Cocok buat kasus tertentu, tapi belajar SQL dulu.

        Buat jalur ini, kita pake **PostgreSQL**. Solid, gratis, dipake industri gede.

        ### Anatomi tabel

        Bayangin tabel kayak spreadsheet:

        ```text
        Tabel: users
        ┌──────┬────────────┬──────────────────┐
        │  id  │   email    │     full_name    │
        ├──────┼────────────┼──────────────────┤
        │   1  │ a@mail.com │  Acel            │
        │   2  │ b@mail.com │  Budi            │
        │   3  │ c@mail.com │  Citra           │
        └──────┴────────────┴──────────────────┘
        ```

        - **Tabel** — kelompok data (users, products).
        - **Kolom** — atribut (id, email, full_name).
        - **Baris** — satu record (satu user).
        - **Primary key** — kolom unik yang nandain tiap baris (biasanya `id`).

        ### Query dasar SQL

        ```sql
        -- Ambil semua user
        SELECT * FROM users;

        -- Ambil user tertentu
        SELECT email, full_name FROM users WHERE id = 1;

        -- Tambah user baru
        INSERT INTO users (email, full_name) VALUES ('d@mail.com', 'Dina');

        -- Update
        UPDATE users SET full_name = 'Acel Baru' WHERE id = 1;

        -- Hapus
        DELETE FROM users WHERE id = 3;
        ```

        Cukup pake empat kata kerja ini, kamu udah bisa kerjain 80% pekerjaan database.

        ### Prisma — penerjemah JS ↔ Database

        Nulis SQL terus-terusan capek sama rawan typo. **ORM (Object-Relational Mapping)** nerjemahin operasi database jadi method bahasa pemrograman.

        Prisma itu ORM populer buat Node.js. Alur kerjanya:

        1. Tulis schema di `schema.prisma`.
        2. Jalanin `prisma db push` — Prisma bikin tabel di DB.
        3. Jalanin `prisma generate` — Prisma bikin client TypeScript yang punya tipe lengkap.
        4. Pake client di kode kamu.

        Contoh schema:

        ```prisma
        model User {
          id        String   @id @default(uuid())
          email     String   @unique
          full_name String
          created_at DateTime @default(now())
        }
        ```

        Pake dari kode:

        ```js
        import { PrismaClient } from "@prisma/client";
        const prisma = new PrismaClient();

        // Baca semua
        const users = await prisma.user.findMany();

        // Tambah
        const acel = await prisma.user.create({
          data: { email: "saya@mail.com", full_name: "Acel" },
        });

        // Update
        await prisma.user.update({
          where: { id: acel.id },
          data: { full_name: "Acel Baru" },
        });

        // Hapus
        await prisma.user.delete({ where: { id: acel.id } });
        ```

        Gak nulis SQL satu pun. Prisma generate query yang efisien.

        ### Relationship — antar tabel saling terhubung

        Tabel di SQL bisa saling terhubung. Contoh: tiap post punya satu author (user).

        ```prisma
        model User {
          id    String @id @default(uuid())
          email String @unique
          posts Post[]
        }

        model Post {
          id       String @id @default(uuid())
          title    String
          content  String
          user_id  String
          author   User   @relation(fields: [user_id], references: [id])
        }
        ```

        Sekarang kamu bisa baca user beserta semua post-nya dalam satu query:

        ```js
        const userWithPosts = await prisma.user.findUnique({
          where: { id: "abc-123" },
          include: { posts: true },
        });
        ```
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup minimum Prisma di project Node:

        ```bash
        # Inisialisasi project
        npm init -y
        npm install prisma @prisma/client
        npx prisma init
        ```

        ```prisma
        // prisma/schema.prisma
        generator client {
          provider = "prisma-client-js"
        }

        datasource db {
          provider = "postgresql"
          url      = env("DATABASE_URL")
        }

        model Book {
          id     String   @id @default(uuid())
          title  String
          author String
          year   Int
        }
        ```

        ```bash
        # Set DATABASE_URL di .env
        echo 'DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"' > .env

        # Push schema ke database
        npx prisma db push

        # Generate client
        npx prisma generate
        ```

        ```js
        // index.js
        import { PrismaClient } from "@prisma/client";
        const prisma = new PrismaClient();

        async function main() {
          await prisma.book.create({
            data: { title: "Atomic Habits", author: "James Clear", year: 2018 },
          });

          const all = await prisma.book.findMany();
          console.log(all);
        }

        main();
        ```
        """
    ),
    practice=(
        "Bikin akun gratis di [supabase.com](https://supabase.com), bikin "
        "project baru. Salin DATABASE_URL ke `.env` project Node kamu. Setup "
        "Prisma kayak contoh di atas pake model `Book`. Push schema, terus "
        "buka Supabase Studio — kamu harus liat tabel `Book` muncul."
    ),
    fix_error={
        "language": "prisma",
        "broken_code": dedent(
            """\
            model book {
              id    String  @default(uuid())
              title String
              year  Int
              user  User
            }

            model User {
              id   String @id @default(uuid())
              name String
            }
            """
        ),
        "hint": "Tiga masalah: penamaan model, primary key, sama deklarasi relasi.",
        "answer_explanation": dedent(
            """\
            1. Nama model di Prisma **wajib PascalCase**. `book` jadi `Book`.
            2. Primary key butuh `@id`. Cuma `String @default(uuid())` aja gak cukup.
            3. Relasi butuh foreign key field + `@relation` mapping.
            """
        ),
        "fixed_code": dedent(
            """\
            model Book {
              id      String @id @default(uuid())
              title   String
              year    Int
              user_id String
              user    User   @relation(fields: [user_id], references: [id])
            }

            model User {
              id    String @id @default(uuid())
              name  String
              books Book[]
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa pilihan database default yang paling aman buat pemula?",
            ["MongoDB", "Redis", "PostgreSQL", "Excel"],
            "C",
            "PostgreSQL solid, gratis, dipake industri gede, sama support-nya bagus banget di kumpulan tools Node.js + Prisma.",
        ),
        q(
            "Fungsi Prisma?",
            [
                "Bahasa programming baru",
                "ORM yang nerjemahin operasi database jadi method JavaScript",
                "Cloud hosting",
                "Frontend framework",
            ],
            "B",
            "Prisma nulis SQL buat kamu. Kamu nulis `prisma.user.findMany()`, dia generate query SQL yang efisien.",
        ),
        q(
            "Mana SQL yang BENER buat ambil user dengan id 1?",
            [
                "`GET users WHERE id = 1`",
                "`SELECT * FROM users WHERE id = 1`",
                "`FETCH users WHERE id == 1`",
                "`READ users id 1`",
            ],
            "B",
            "SQL pake `SELECT ... FROM ... WHERE`. Beda sama HTTP method (GET) yang sering disamain pemula.",
        ),
        q(
            "Fungsi `@id` di Prisma schema?",
            [
                "Penanda kolom enkripsi",
                "Penanda primary key — kolom unik yang nandain tiap baris",
                "Buat auto-increment",
                "Buat format tanggal",
            ],
            "B",
            "Tiap model di Prisma wajib punya satu field sama `@id`. Itu primary key-nya.",
        ),
        q(
            "Apa keuntungan ORM dibanding nulis SQL manual?",
            [
                "Lebih lambat",
                "Type safety (apalagi sama TypeScript), auto-completion, sama ngurangin typo SQL",
                "Gak ada keuntungan",
                "Wajib menurut hukum",
            ],
            "B",
            "Prisma generate client sama tipe TypeScript otomatis. Salah ketik field langsung error sebelum runtime.",
        ),
    ],
    common_mistakes=[
        "Nama model lowercase di Prisma. Generator-nya complain: harus PascalCase.",
        "Lupa `prisma generate` habis edit schema. Client gak ke-update.",
        "Push ke production tanpa backup. Migration salah bisa ngilangin data.",
    ],
    checkpoint=[
        "Bisa jelasin beda SQL vs NoSQL.",
        "Bisa baca SQL dasar (SELECT, INSERT, UPDATE, DELETE).",
        "Bisa setup Prisma dari nol di project Node.",
        "Tau apa itu primary key sama relasi antar model.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_REST_API = make_lesson(
    title="Mini Project — REST API CRUD buat Buku",
    slug="mini-project-rest-api-buku",
    order_index=4,
    read_time="120 menit",
    summary="Bangun API CRUD lengkap pake Express, Prisma, sama PostgreSQL.",
    tools=["Node.js LTS", "Express", "Prisma", "PostgreSQL atau Supabase", "Postman atau Thunder Client"],
    outcomes=[
        "Bisa bangun REST API dari ujung ke ujung dari nol",
        "Bisa nerapin 5 endpoint CRUD",
        "Bisa pake Prisma buat operasi database",
        "Bisa test API pake Postman atau Thunder Client",
    ],
    tldr=(
        "Bangun API sama 5 endpoint: list, detail, create, update, delete. "
        "Stack: Express + Prisma + PostgreSQL. Test pake Postman."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungin semua: HTTP, REST, JSON, database, ORM.

        Kamu bakal bangun API yang bisa di-call dari frontend mana aja.

        Habis selesai, kamu udah punya backend pertama yang real — bukan tutorial dummy.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Node.js + Express + Prisma + PostgreSQL.

        Endpoint yang harus ada:

        - `GET /api/books` — daftar semua buku.
        - `GET /api/books/:id` — detail satu buku.
        - `POST /api/books` — bikin buku baru.
        - `PUT /api/books/:id` — update buku.
        - `DELETE /api/books/:id` — hapus buku.

        Tiap buku punya: `id`, `title`, `author`, `year`, `created_at`.

        ### Setup

        ```bash
        mkdir books-api
        cd books-api
        npm init -y
        npm install express prisma @prisma/client cors
        npm install -D nodemon
        npx prisma init
        ```

        Edit `prisma/schema.prisma` buat model `Book`. Set `DATABASE_URL` di `.env`.

        ```bash
        npx prisma db push
        npx prisma generate
        ```

        ### Struktur file

        ```text
        books-api/
          ├── prisma/schema.prisma
          ├── src/
          │   ├── index.js          (Express setup)
          │   └── routes/
          │       └── books.js      (5 endpoint)
          ├── .env
          └── package.json
        ```

        ### Validasi minimal

        - `POST /books` tanpa `title`: balas 400 sama error message yang jelas.
        - `GET /books/:id` sama ID yang gak ada: balas 404.
        - Field `year` harus number, bukan string.

        ### Test pake Postman atau Thunder Client

        Postman gratis. Thunder Client itu extension VS Code yang lebih ringan.

        Test scenario minimal:

        - POST satu buku → status 201 + data buku yang baru.
        - GET list → status 200 + array isinya buku tadi.
        - PUT buku → status 200 + data ter-update.
        - DELETE buku → status 204 (no content).
        - GET buku yang udah dihapus → status 404.

        ### Submit

        Push ke GitHub sama README minimal yang isinya: cara setup (`.env`, install, db push), cara run, sama daftar endpoint sama contoh request.
        """
    ),
    contoh_code_md=dedent(
        """\
        Skeleton Express + Prisma:

        ```js
        // src/index.js
        import express from "express";
        import cors from "cors";
        import booksRouter from "./routes/books.js";

        const app = express();
        app.use(cors());
        app.use(express.json());

        app.use("/api/books", booksRouter);

        app.listen(3001, () => {
          console.log("API jalan di http://localhost:3001");
        });
        ```

        ```js
        // src/routes/books.js
        import { Router } from "express";
        import { PrismaClient } from "@prisma/client";

        const prisma = new PrismaClient();
        const router = Router();

        // GET /api/books
        router.get("/", async (req, res) => {
          const books = await prisma.book.findMany({
            orderBy: { created_at: "desc" },
          });
          res.json(books);
        });

        // GET /api/books/:id
        router.get("/:id", async (req, res) => {
          const book = await prisma.book.findUnique({
            where: { id: req.params.id },
          });
          if (!book) return res.status(404).json({ detail: "Buku gak ditemukan" });
          res.json(book);
        });

        // POST /api/books
        router.post("/", async (req, res) => {
          const { title, author, year } = req.body;
          if (!title || !author) {
            return res.status(400).json({ detail: "Title sama author wajib diisi" });
          }
          const book = await prisma.book.create({
            data: { title, author, year: Number(year) || null },
          });
          res.status(201).json(book);
        });

        // PUT /api/books/:id
        router.put("/:id", async (req, res) => {
          try {
            const updated = await prisma.book.update({
              where: { id: req.params.id },
              data: req.body,
            });
            res.json(updated);
          } catch {
            res.status(404).json({ detail: "Buku gak ditemukan" });
          }
        });

        // DELETE /api/books/:id
        router.delete("/:id", async (req, res) => {
          try {
            await prisma.book.delete({ where: { id: req.params.id } });
            res.status(204).send();
          } catch {
            res.status(404).json({ detail: "Buku gak ditemukan" });
          }
        });

        export default router;
        ```

        Tambahin script di `package.json`:

        ```json
        "scripts": {
          "dev": "nodemon src/index.js",
          "start": "node src/index.js"
        }
        ```
        """
    ),
    practice=(
        "Selesain API sesuai spec. Test semua endpoint pake Postman/Thunder "
        "Client. Pastiin response code-nya bener (201 buat create, 204 buat "
        "delete, 404 pas gak ditemukan). Push ke GitHub sama README lengkap."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            router.post("/", async (req, res) => {
              const book = await prisma.book.create({
                data: req.body,
              });
              res.json(book);
            });
            """
        ),
        "hint": "Tiga masalah: status code, validasi input, sama tipe data field.",
        "answer_explanation": dedent(
            """\
            1. Buat endpoint create, status sukses-nya `201 Created`, bukan default `200 OK`.
            2. Gak ada validasi — kalau body kosong atau gak punya `title`, Prisma bakal throw error tanpa pesan jelas.
            3. `req.body.year` bisa berupa string. Wajib di-cast ke number sebelum disimpen biar schema Prisma gak reject.
            """
        ),
        "fixed_code": dedent(
            """\
            router.post("/", async (req, res) => {
              const { title, author, year } = req.body;

              if (!title || !author) {
                return res.status(400).json({
                  detail: "Title sama author wajib diisi",
                });
              }

              const book = await prisma.book.create({
                data: {
                  title,
                  author,
                  year: year ? Number(year) : null,
                },
              });

              res.status(201).json(book);
            });
            """
        ),
    },
    quiz=[
        q(
            "Status code yang BENER buat POST /books yang sukses bikin buku baru?",
            ["200 OK", "201 Created", "204 No Content", "302 Redirect"],
            "B",
            "201 Created khusus buat resource baru. 200 OK biasa dipake buat GET. Pisah biar client paham hasilnya.",
        ),
        q(
            "Status code yang TEPAT buat DELETE /books/:id yang sukses?",
            ["200 OK", "201 Created", "204 No Content", "400 Bad Request"],
            "C",
            "204 dipake pas sukses tapi gak ada body yang dikembaliin — pas banget buat DELETE.",
        ),
        q(
            "Fungsi `app.use(express.json())`?",
            [
                "Buat styling",
                "Middleware yang parse body request JSON jadi `req.body` object",
                "Otomatis bikin tabel",
                "Buat login",
            ],
            "B",
            "Tanpa middleware ini, `req.body` undefined. Express harus dikasih tau cara baca body JSON.",
        ),
        q(
            "Apa yang harus dilakuin pas `GET /books/:id` dan ID-nya gak ada?",
            [
                "Balas 200 OK sama body kosong",
                "Balas 404 Not Found sama pesan yang jelas",
                "Crash server",
                "Balas 500 Internal Server Error",
            ],
            "B",
            "Resource gak ada = 404. Itu standar REST yang harus di-handle eksplisit.",
        ),
        q(
            "Kenapa `cors()` middleware penting pas API mau dipanggil dari frontend?",
            [
                "Buat performance",
                "Ngebolehin browser frontend manggil API yang origin-nya beda. Tanpa ini, browser blokir request.",
                "Buat styling",
                "Gak penting",
            ],
            "B",
            "Default browser blokir cross-origin request demi keamanan. Middleware CORS kasih izin eksplisit.",
        ),
    ],
    common_mistakes=[
        "Pake 200 OK buat semua sukses. Hilang nuance antara create (201) sama no-content (204).",
        "Gak validasi input. Body kosong langsung lewat ke Prisma, error message-nya gak ramah.",
        "Lupa CORS. Frontend gak bisa manggil API meski API-nya bener.",
    ],
    checkpoint=[
        "API jalan di lokal sama bisa di-test pake Postman.",
        "Lima endpoint CRUD jalan sama status code yang bener.",
        "Validasi minimal udah ada (400 buat input salah, 404 buat gak ditemukan).",
        "Repo GitHub punya README sama cara setup dan contoh request.",
    ],
    xp_reward=400,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=1,
    slug="backend-beginner",
    title="Backend Beginner",
    subtitle="Dari klik tombol sampe data tersimpan",
    description=(
        "Pengantar dunia server-side. Kamu bakal paham cara kerja HTTP, "
        "REST API, database, sama nutup level sama REST API CRUD pertamamu "
        "pake Express + Prisma + PostgreSQL."
    ),
    duration="~3 minggu",
    difficulty="Pemula",
    accent_color="from-sky-400/30 to-violet-500/10",
    mini_project="REST API CRUD untuk Buku",
    tags=["Node.js", "Express", "REST", "Prisma", "PostgreSQL"],
    lessons=[LESSON_APA_BACKEND, LESSON_API, LESSON_DB, PROJECT_REST_API],
)
