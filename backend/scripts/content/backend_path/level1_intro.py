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
    summary="Server, database, dan apa yang terjadi setelah klik tombol.",
    tools=["Browser DevTools (Network tab)", "Notes app"],
    outcomes=[
        "Membedakan frontend dan backend dengan analogi nyata",
        "Mengenali HTTP method dan status code dasar",
        "Membaca request/response di Network tab DevTools",
    ],
    tldr=(
        "Frontend = meja restoran (yang user lihat). Backend = dapur (yang "
        "kerja di belakang). Keduanya bicara via HTTP request/response. "
        "Method utama: GET, POST, PUT, DELETE."
    ),
    pembuka=dedent(
        """\
        Saat kamu klik 'Login' di Twitter, ada banyak yang terjadi dalam sepersekian detik.

        Tampilan yang kamu lihat itu frontend. Tapi yang verifikasi password, ambil data tweet, dan kirim balik — itu backend.

        Lesson ini bedah anatomi sederhana: apa yang terjadi di balik layar.
        """
    ),
    penjelasan=dedent(
        """\
        ### Analogi restoran

        Bayangkan website itu restoran:

        - **Meja, menu, pelayan** = frontend. Itu yang kamu sentuh.
        - **Dapur** = backend. Tempat masak data terjadi. Kamu tidak masuk ke dapur.
        - **Pelayan yang antar pesanan** = API. Jembatan antara meja dan dapur.
        - **Lemari bahan dan stok** = database. Tempat data tersimpan rapi.

        Saat kamu klik 'Login', frontend kirim "permintaan" ke backend. Backend cek di database, lalu kirim balik hasilnya: berhasil atau gagal.

        ### HTTP — bahasa percakapan

        Frontend dan backend bicara pakai HTTP. Setiap percakapan punya format yang sama:

        - **Request** dari frontend → backend.
        - **Response** dari backend → frontend.

        Request punya:

        - **Method.** Tipe aksi: `GET` (ambil), `POST` (buat baru), `PUT` (update), `DELETE` (hapus).
        - **URL.** Alamat tujuan, misal `/api/users/42`.
        - **Headers.** Info tambahan (token auth, content-type).
        - **Body.** Data yang dikirim (cuma untuk POST/PUT).

        Response punya:

        - **Status code.** Angka yang menjelaskan hasil.
        - **Body.** Data yang dikirim balik.

        ### Status code yang sering muncul

        - `200 OK` — sukses.
        - `201 Created` — sukses bikin data baru.
        - `400 Bad Request` — request kamu salah format.
        - `401 Unauthorized` — kamu belum login.
        - `403 Forbidden` — sudah login tapi tidak punya akses.
        - `404 Not Found` — data tidak ada.
        - `500 Internal Server Error` — backend yang error.

        Dua kelompok besar: 2xx = sukses, 4xx = salah dari sisi user, 5xx = salah dari sisi server.

        ### REST — gaya bicara yang umum

        REST adalah konvensi cara nyusun URL dan method.

        - `GET /users` — daftar semua user.
        - `GET /users/42` — detail user dengan id 42.
        - `POST /users` — bikin user baru.
        - `PUT /users/42` — update user 42.
        - `DELETE /users/42` — hapus user 42.

        Pola ini konsisten dan mudah ditebak. Hampir semua API publik mengikutinya.

        ### Coba lihat sendiri

        Buka satu situs apa saja, tekan F12 → tab Network. Refresh halaman. Kamu akan lihat puluhan request. Klik salah satu untuk lihat detail: method, status, headers, body.

        Itu yang sebenarnya terjadi setiap detik di internet.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh request HTTP saat user login (versi sederhana):

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
        "Buka [github.com](https://github.com) di browser. Tekan F12 → Network. "
        "Refresh halaman. Klik request paling atas (biasanya yang URL-nya "
        "github.com itu sendiri). Catat: method, status code, dan satu header "
        "menarik yang muncul."
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
        "hint": "Method dan tujuan tidak match. REST punya konvensi yang spesifik.",
        "answer_explanation": dedent(
            """\
            Kesalahan: untuk **mengambil** data, gunakan `GET`, bukan `POST`. POST itu untuk membuat data baru.

            REST convention untuk satu resource:

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
            "Apa yang dilakukan backend dalam analogi restoran?",
            [
                "Mengantar pesanan ke meja",
                "Menjadi tempat data diproses dan disimpan, seperti dapur",
                "Menjadi menu yang dilihat user",
                "Meja kasir saja",
            ],
            "B",
            "Backend = dapur. Tempat data dimasak, query database, dan logika bisnis dijalankan.",
        ),
        q(
            "Mana method HTTP yang BENAR untuk mengambil daftar user?",
            ["POST", "PUT", "GET", "DELETE"],
            "C",
            "GET dipakai untuk membaca data. POST untuk membuat baru, PUT untuk update, DELETE untuk hapus.",
        ),
        q(
            "Apa arti status code 401 Unauthorized?",
            [
                "Server error",
                "User belum login atau token tidak valid",
                "Halaman tidak ditemukan",
                "Sukses",
            ],
            "B",
            "401 artinya 'kamu belum membuktikan siapa kamu'. Beda dengan 403 yang artinya 'sudah login tapi tidak punya akses'.",
        ),
        q(
            "Apa fungsi tab Network di DevTools?",
            [
                "Mengubah CSS",
                "Melihat semua HTTP request/response yang terjadi di halaman",
                "Edit file lokal",
                "Compile kode",
            ],
            "B",
            "Network tab adalah jendela ke percakapan HTTP. Penting saat debug masalah API.",
        ),
        q(
            "Mana URL REST yang KONSISTEN untuk update user dengan id 42?",
            [
                "POST /update-user-42",
                "PUT /users/42",
                "GET /users/update/42",
                "DELETE /users/42",
            ],
            "B",
            "REST: PUT atau PATCH ke `/users/42` untuk update. Method dan struktur URL bersifat konvensional.",
        ),
    ],
    common_mistakes=[
        "Pakai POST untuk semua aksi. Padahal GET/PUT/DELETE punya makna sendiri.",
        "Pikir 401 dan 403 sama. Bedanya: 401 = belum login, 403 = login tapi tidak boleh.",
        "Lupa `Content-Type: application/json` di request POST. Server bingung parse body.",
    ],
    checkpoint=[
        "Bisa jelaskan beda frontend dan backend tanpa istilah teknis.",
        "Hafal 4 method utama HTTP dan kapan dipakai.",
        "Tahu beda status code 2xx/4xx/5xx.",
        "Bisa baca Network tab DevTools secara umum.",
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
    summary="REST API, JSON, dan cara konsumsi API publik dari browser.",
    tools=["Browser modern", "DevTools (Console + Network)"],
    outcomes=[
        "Memahami API sebagai kontrak antar aplikasi",
        "Membaca dan menulis JSON",
        "Memanggil API publik lewat fetch dari Console",
    ],
    tldr=(
        "API = kontrak. Frontend kirim request sesuai kontrak, backend balas "
        "data dalam format JSON. fetch() adalah cara JavaScript memanggil API."
    ),
    pembuka=dedent(
        """\
        Pernah download cuaca harian di app HP? App-nya tidak nyetak datanya sendiri.

        Dia minta ke API cuaca. API balas dengan data: suhu, kelembaban, prediksi tiga hari ke depan. App-mu cuma menampilkan.

        API itu jembatan antar aplikasi. Lesson ini membongkar cara kerjanya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Definisi sederhana

        API (Application Programming Interface) adalah **kontrak komunikasi** antar aplikasi.

        Backend bilang: "Kalau kamu mau data X, kirim request ke `/path` dengan method Y. Aku akan balas dengan format Z."

        Selama kontrak dipatuhi, frontend dan backend bisa develop terpisah. Tim backend bisa rewrite Python ke Go, frontend tidak perlu tahu — selama kontrak API tetap sama.

        ### REST API — gaya yang dominan

        REST API mengelola **resource**. Resource = "benda" yang punya identitas (user, post, produk).

        Untuk tiap resource, ada 5 endpoint umum:

        - `GET /products` — daftar produk.
        - `GET /products/42` — detail produk.
        - `POST /products` — bikin produk baru.
        - `PUT /products/42` — update produk.
        - `DELETE /products/42` — hapus.

        Jenis lain: GraphQL, gRPC, tRPC. Tapi untuk pemula, REST yang paling lazim ditemui.

        ### JSON — format data standar

        JSON (JavaScript Object Notation) adalah cara nulis data yang mudah dibaca manusia dan mesin.

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

        - Object: `{ key: value }`. Key wajib pakai kutip ganda.
        - Array: `[ item, item ]`.
        - Type: string, number, boolean, null, object, array. **Tidak ada `undefined` di JSON.**
        - Tidak boleh ada koma di akhir item terakhir (trailing comma).

        ### fetch — cara JavaScript panggil API

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

        `fetch` mengembalikan Promise. Kita pakai `await` untuk menunggu, lalu `res.json()` untuk parse body jadi JavaScript object.

        ### Coba sendiri di Console

        Buka tab Console di DevTools, paste kode ini:

        ```js
        const res = await fetch("https://jsonplaceholder.typicode.com/users/1");
        const data = await res.json();
        console.log(data);
        ```

        Kamu akan dapat object berisi data user dummy. JSONPlaceholder adalah API publik gratis untuk latihan.
        """
    ),
    contoh_code_md=dedent(
        """\
        Memanggil API publik dan menampilkan datanya:

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

        Pola umum: try/catch + cek `res.ok`. Karena `fetch` cuma reject saat network error — bukan saat status 404 atau 500.
        """
    ),
    practice=(
        "Buka Console di browser. Panggil API JSONPlaceholder ini:\n\n"
        "`fetch('https://jsonplaceholder.typicode.com/posts/1').then(r => r.json()).then(console.log)`\n\n"
        "Lalu ubah angka 1 ke 5 — lihat data berbeda. Lalu coba `/posts` (tanpa "
        "id) untuk dapat daftar semua post."
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
        "hint": "fetch dan json() keduanya asynchronous. Cek apa yang sebenarnya kamu dapat tanpa await.",
        "answer_explanation": dedent(
            """\
            Kesalahan: `fetch` mengembalikan **Promise**, bukan response langsung. Tanpa `await`, `res` adalah Promise — dan `Promise.json()` tidak ada.

            Solusi: tambah `await` di kedua langkah, atau pakai `.then()`. Function pembungkusnya juga harus `async`.
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

            // atau dengan .then():
            // fetch("https://api.example.com/users")
            //   .then((r) => r.json())
            //   .then((data) => console.log(data[0].name));
            """
        ),
    },
    quiz=[
        q(
            "Apa itu API dalam satu kalimat?",
            [
                "Bahasa pemrograman",
                "Kontrak komunikasi antar aplikasi",
                "Editor kode",
                "Library JavaScript",
            ],
            "B",
            "API adalah kontrak. Selama kontrak dipatuhi, dua aplikasi bisa berkomunikasi tanpa peduli implementasi internalnya.",
        ),
        q(
            "Format data yang paling umum di REST API modern?",
            ["XML", "CSV", "JSON", "YAML"],
            "C",
            "JSON dominan karena ringan, mudah dibaca, dan native dengan JavaScript. XML dipakai dulu, sekarang jarang.",
        ),
        q(
            "Apa yang dikembalikan `fetch(url)` di JavaScript?",
            [
                "Response data langsung",
                "Promise yang resolve menjadi Response object",
                "String JSON",
                "Boolean",
            ],
            "B",
            "fetch mengembalikan Promise. Kita perlu `await` atau `.then()` untuk dapat Response, lalu `res.json()` untuk parse body.",
        ),
        q(
            "Apa beda `res.ok` dan tidak adanya error fetch?",
            [
                "Tidak ada beda",
                "fetch tidak reject saat status 4xx/5xx — `res.ok` (true kalau 2xx) yang harus dicek manual",
                "`res.ok` cuma untuk POST",
                "fetch otomatis throw saat 404",
            ],
            "B",
            "fetch cuma reject saat network error (offline, DNS, dll). Status 404 atau 500 tetap dianggap berhasil sampai ke kita. Jadi cek `res.ok` di kode.",
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
            "JSON wajib: kutip ganda di key, tidak ada trailing comma, value sesuai tipe yang valid.",
        ),
    ],
    common_mistakes=[
        "Lupa `await` saat panggil `fetch`. Hasilnya bukan response, tapi Promise.",
        "Pakai kutip tunggal di key JSON. Bukan JSON valid.",
        "Tidak cek `res.ok`. Kode lanjut walau backend balas error.",
    ],
    checkpoint=[
        "Bisa jelaskan apa itu API dengan analogi pelayan restoran.",
        "Bisa baca dan tulis JSON sederhana.",
        "Bisa panggil API publik dengan `fetch` di Console.",
        "Tahu pentingnya cek `res.ok` dan handle error.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Intro Database
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DB = make_lesson(
    title="Intro Database & Prisma",
    slug="intro-database",
    order_index=3,
    read_time="13 menit",
    summary="SQL vs NoSQL, tabel, query dasar, dan Prisma sebagai ORM.",
    tools=["PostgreSQL (lokal atau Supabase)", "Node.js + Prisma", "VS Code"],
    outcomes=[
        "Memahami konsep tabel, kolom, baris dengan analogi spreadsheet",
        "Membaca query SQL dasar (SELECT, INSERT, UPDATE, DELETE)",
        "Memakai Prisma untuk operasi database dari JavaScript",
    ],
    tldr=(
        "Database = lemari arsip. PostgreSQL = pilihan default yang aman. "
        "SQL = bahasa untuk tanya-jawab dengan database. Prisma = penerjemah "
        "antara JavaScript dan database — kamu nulis JS, dia generate SQL."
    ),
    pembuka=dedent(
        """\
        Variable di JavaScript hilang saat halaman ditutup. localStorage hilang saat user ganti browser.

        Untuk data yang harus tetap ada untuk semua user — daftar produk, comment, profil — kamu butuh database.

        Bayangkan database itu lemari arsip raksasa yang terorganisir. Backend yang ngambilin file dari lemari ini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Dua kelompok besar

        - **SQL (Relational).** Data tersusun dalam tabel dengan baris dan kolom yang jelas. Contoh: PostgreSQL, MySQL, SQLite. **Pilihan default untuk pemula.**
        - **NoSQL (Document/Key-Value).** Data lebih fleksibel, mirip JSON. Contoh: MongoDB, Redis. Cocok untuk kasus tertentu, tapi belajar SQL dulu.

        Untuk jalur ini, kita pakai **PostgreSQL**. Solid, gratis, dipakai industri besar.

        ### Anatomi tabel

        Bayangkan tabel seperti spreadsheet:

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
        - **Primary key** — kolom unik yang menandai tiap baris (biasanya `id`).

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

        Cukup dengan empat verb ini, kamu bisa kerjain 80% pekerjaan database.

        ### Prisma — penerjemah JS ↔ Database

        Nulis SQL terus-terusan capek dan rawan typo. **ORM (Object-Relational Mapping)** menerjemahkan operasi database jadi method bahasa pemrograman.

        Prisma adalah ORM populer untuk Node.js. Alur kerjanya:

        1. Tulis schema di `schema.prisma`.
        2. Jalankan `prisma db push` — Prisma bikin tabel di DB.
        3. Jalankan `prisma generate` — Prisma bikin client TypeScript yang punya tipe lengkap.
        4. Pakai client di kode kamu.

        Schema example:

        ```prisma
        model User {
          id        String   @id @default(uuid())
          email     String   @unique
          full_name String
          created_at DateTime @default(now())
        }
        ```

        Pakai dari kode:

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

        Tidak nulis SQL satu pun. Prisma generate query yang efisien.

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
        "Prisma seperti contoh di atas dengan model `Book`. Push schema, lalu "
        "buka Supabase Studio — kamu harus lihat tabel `Book` muncul."
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
        "hint": "Tiga masalah: penamaan model, primary key, dan deklarasi relasi.",
        "answer_explanation": dedent(
            """\
            1. Nama model di Prisma **wajib PascalCase**. `book` jadi `Book`.
            2. Primary key butuh `@id`. `String @default(uuid())` saja tidak cukup.
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
            "Apa pilihan database default yang paling aman untuk pemula?",
            ["MongoDB", "Redis", "PostgreSQL", "Excel"],
            "C",
            "PostgreSQL solid, gratis, dipakai industri besar, dan sangat well-supported di ekosistem Node.js + Prisma.",
        ),
        q(
            "Apa fungsi Prisma?",
            [
                "Bahasa programming baru",
                "ORM yang menerjemahkan operasi database jadi method JavaScript",
                "Cloud hosting",
                "Frontend framework",
            ],
            "B",
            "Prisma menulis SQL untukmu. Kamu nulis `prisma.user.findMany()`, dia generate query SQL yang efisien.",
        ),
        q(
            "Mana SQL yang BENAR untuk ambil user dengan id 1?",
            [
                "`GET users WHERE id = 1`",
                "`SELECT * FROM users WHERE id = 1`",
                "`FETCH users WHERE id == 1`",
                "`READ users id 1`",
            ],
            "B",
            "SQL pakai `SELECT ... FROM ... WHERE`. Berbeda dengan HTTP method (GET) yang sering disamakan oleh pemula.",
        ),
        q(
            "Apa fungsi `@id` di Prisma schema?",
            [
                "Penanda kolom enkripsi",
                "Penanda primary key — kolom unik yang menandai tiap baris",
                "Untuk auto-increment",
                "Untuk format tanggal",
            ],
            "B",
            "Setiap model di Prisma wajib punya satu field dengan `@id`. Itu primary key-nya.",
        ),
        q(
            "Apa keuntungan ORM dibanding nulis SQL manual?",
            [
                "Lebih lambat",
                "Type safety (terutama dengan TypeScript), auto-completion, dan mengurangi typo SQL",
                "Tidak ada keuntungan",
                "Wajib oleh hukum",
            ],
            "B",
            "Prisma generate client dengan tipe TypeScript otomatis. Salah ketik field langsung error sebelum runtime.",
        ),
    ],
    common_mistakes=[
        "Nama model lowercase di Prisma. Generator complain: harus PascalCase.",
        "Lupa `prisma generate` setelah edit schema. Client tidak ter-update.",
        "Push ke production tanpa backup. Migration salah bisa hilangkan data.",
    ],
    checkpoint=[
        "Bisa jelaskan beda SQL vs NoSQL.",
        "Bisa baca SQL dasar (SELECT, INSERT, UPDATE, DELETE).",
        "Bisa setup Prisma dari nol di project Node.",
        "Tahu apa itu primary key dan relasi antar model.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_REST_API = make_lesson(
    title="Mini Project — REST API CRUD untuk Buku",
    slug="mini-project-rest-api-buku",
    order_index=4,
    read_time="120 menit",
    summary="Bangun API CRUD lengkap dengan Express, Prisma, dan PostgreSQL.",
    tools=["Node.js LTS", "Express", "Prisma", "PostgreSQL atau Supabase", "Postman atau Thunder Client"],
    outcomes=[
        "Membangun REST API end-to-end dari nol",
        "Menerapkan 5 endpoint CRUD",
        "Menggunakan Prisma untuk database operations",
        "Test API dengan Postman atau Thunder Client",
    ],
    tldr=(
        "Bangun API dengan 5 endpoint: list, detail, create, update, delete. "
        "Stack: Express + Prisma + PostgreSQL. Test dengan Postman."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungkan semua: HTTP, REST, JSON, database, ORM.

        Kamu akan bangun API yang bisa di-call dari frontend mana saja.

        Setelah selesai, kamu sudah punya backend pertama yang real — bukan tutorial dummy.
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

        Edit `prisma/schema.prisma` untuk model `Book`. Set `DATABASE_URL` di `.env`.

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

        - `POST /books` tanpa `title`: balas 400 dengan error message yang jelas.
        - `GET /books/:id` dengan ID yang tidak ada: balas 404.
        - Field `year` harus number, bukan string.

        ### Test dengan Postman atau Thunder Client

        Postman gratis. Thunder Client adalah extension VS Code yang lebih ringan.

        Test scenario minimal:

        - POST satu buku → status 201 + data buku yang baru.
        - GET list → status 200 + array berisi buku tadi.
        - PUT buku → status 200 + data ter-update.
        - DELETE buku → status 204 (no content).
        - GET buku yang sudah dihapus → status 404.

        ### Submit

        Push ke GitHub dengan README minimal yang isinya: cara setup (`.env`, install, db push), cara run, dan daftar endpoint dengan contoh request.
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
          if (!book) return res.status(404).json({ detail: "Buku tidak ditemukan" });
          res.json(book);
        });

        // POST /api/books
        router.post("/", async (req, res) => {
          const { title, author, year } = req.body;
          if (!title || !author) {
            return res.status(400).json({ detail: "Title dan author wajib diisi" });
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
            res.status(404).json({ detail: "Buku tidak ditemukan" });
          }
        });

        // DELETE /api/books/:id
        router.delete("/:id", async (req, res) => {
          try {
            await prisma.book.delete({ where: { id: req.params.id } });
            res.status(204).send();
          } catch {
            res.status(404).json({ detail: "Buku tidak ditemukan" });
          }
        });

        export default router;
        ```

        Tambahkan script di `package.json`:

        ```json
        "scripts": {
          "dev": "nodemon src/index.js",
          "start": "node src/index.js"
        }
        ```
        """
    ),
    practice=(
        "Selesaikan API sesuai spec. Test semua endpoint dengan Postman/Thunder "
        "Client. Pastikan response code-nya benar (201 untuk create, 204 untuk "
        "delete, 404 saat tidak ditemukan). Push ke GitHub dengan README "
        "lengkap."
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
        "hint": "Tiga masalah: status code, validasi input, dan tipe data field.",
        "answer_explanation": dedent(
            """\
            1. Untuk endpoint create, status sukses adalah `201 Created`, bukan default `200 OK`.
            2. Tidak ada validasi — kalau body kosong atau tidak punya `title`, Prisma akan throw error tanpa pesan jelas.
            3. `req.body.year` bisa berupa string. Wajib di-cast ke number sebelum disimpan supaya schema Prisma tidak reject.
            """
        ),
        "fixed_code": dedent(
            """\
            router.post("/", async (req, res) => {
              const { title, author, year } = req.body;

              if (!title || !author) {
                return res.status(400).json({
                  detail: "Title dan author wajib diisi",
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
            "Status code yang BENAR untuk POST /books yang sukses bikin buku baru?",
            ["200 OK", "201 Created", "204 No Content", "302 Redirect"],
            "B",
            "201 Created khusus untuk resource baru. 200 OK biasa dipakai untuk GET. Pisah supaya client paham hasilnya.",
        ),
        q(
            "Status code yang TEPAT untuk DELETE /books/:id yang sukses?",
            ["200 OK", "201 Created", "204 No Content", "400 Bad Request"],
            "C",
            "204 dipakai saat sukses tapi tidak ada body yang dikembalikan — pas untuk DELETE.",
        ),
        q(
            "Apa fungsi `app.use(express.json())`?",
            [
                "Untuk styling",
                "Middleware yang parse body request JSON jadi `req.body` object",
                "Otomatis bikin tabel",
                "Untuk login",
            ],
            "B",
            "Tanpa middleware ini, `req.body` undefined. Express harus diberitahu cara baca body JSON.",
        ),
        q(
            "Apa yang harus dilakukan saat `GET /books/:id` dan ID-nya tidak ada?",
            [
                "Balas 200 OK dengan body kosong",
                "Balas 404 Not Found dengan pesan yang jelas",
                "Crash server",
                "Balas 500 Internal Server Error",
            ],
            "B",
            "Resource tidak ada = 404. Itu standar REST yang harus di-handle eksplisit.",
        ),
        q(
            "Kenapa `cors()` middleware penting saat API mau dipanggil dari frontend?",
            [
                "Untuk performance",
                "Mengizinkan browser frontend memanggil API yang origin-nya berbeda. Tanpa ini, browser blokir request.",
                "Untuk styling",
                "Tidak penting",
            ],
            "B",
            "Default browser blokir cross-origin request demi keamanan. CORS middleware kasih izin eksplisit.",
        ),
    ],
    common_mistakes=[
        "Pakai 200 OK untuk semua sukses. Hilang nuance antara create (201) dan no-content (204).",
        "Tidak validasi input. Body kosong langsung lewat ke Prisma, error message-nya tidak ramah.",
        "Lupa CORS. Frontend tidak bisa panggil API meski API-nya benar.",
    ],
    checkpoint=[
        "API jalan di lokal dan bisa di-test dengan Postman.",
        "Lima endpoint CRUD bekerja dengan status code yang benar.",
        "Validasi minimal sudah ada (400 untuk input salah, 404 untuk tidak ditemukan).",
        "Repo GitHub punya README dengan cara setup dan contoh request.",
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
    subtitle="Dari klik tombol sampai data tersimpan",
    description=(
        "Pengantar dunia server-side. Kamu akan paham cara kerja HTTP, REST "
        "API, database, dan tutup level dengan REST API CRUD pertamamu pakai "
        "Express + Prisma + PostgreSQL."
    ),
    duration="~3 minggu",
    difficulty="Pemula",
    accent_color="from-sky-400/30 to-violet-500/10",
    mini_project="REST API CRUD untuk Buku",
    tags=["Node.js", "Express", "REST", "Prisma", "PostgreSQL"],
    lessons=[LESSON_APA_BACKEND, LESSON_API, LESSON_DB, PROJECT_REST_API],
)
