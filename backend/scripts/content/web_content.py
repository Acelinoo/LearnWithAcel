WEB_CONTENT = {
    "frontend-developer": [
        {
            "title": "Level 1: HTML & CSS Dasar",
            "subtitle": "Pondasi utama untuk membuat struktur dan tampilan web.",
            "description": "Pelajari elemen dasar pembentuk website, dari struktur tag hingga styling sederhana.",
            "lessons": [
                {
                    "title": "Struktur Dokumen HTML5",
                    "content": "# Struktur HTML5\nHTML (HyperText Markup Language) adalah kerangka tulang dari setiap halaman web. Setiap file HTML5 memiliki struktur dasar yang standar.\n\n## Struktur Dasar\nBerikut adalah contoh kerangka minimum HTML5:\n```html\n<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Website Pertamaku</title>\n</head>\n<body>\n  <h1>Halo Dunia!</h1>\n  <p>Selamat datang di kelas Frontend.</p>\n</body>\n</html>\n```\n\n## Penjelasan Tag Utama\n- `<!DOCTYPE html>`: Memberitahu browser bahwa ini dokumen HTML5.\n- `<html>`: Elemen root dari halaman.\n- `<head>`: Berisi metadata (title, link CSS, dll).\n- `<body>`: Berisi semua konten yang akan ditampilkan ke user.\n\n> **Best Practice**: Selalu gunakan atribut `lang` pada tag `<html>` untuk membantu SEO dan aksesibilitas screen reader."
                },
                {
                    "title": "Semantic HTML",
                    "content": "# Semantic HTML\nTag semantic adalah tag HTML yang namanya menjelaskan secara persis maknanya, bukan cuma sekadar kontainer seperti `<div>` atau `<span>`.\n\n## Keuntungan Semantic HTML\n1. **SEO**: Membantu mesin pencari mengindeks struktur web.\n2. **Aksesibilitas**: Membantu tunanetra (dengan screen reader) membaca navigasi web.\n\n## Contoh Penggunaan\n```html\n<header>\n  <nav>\n    <ul>\n      <li><a href=\"#\">Home</a></li>\n    </ul>\n  </nav>\n</header>\n\n<main>\n  <article>\n    <h2>Belajar Frontend</h2>\n    <p>Ini adalah artikel pertama.</p>\n  </article>\n</main>\n\n<footer>\n  <p>Copyright 2026</p>\n</footer>\n```\n\n> **Best Practice**: Hindari *div soup* (terlalu banyak div bertumpuk). Gunakan `<header>`, `<main>`, `<section>`, `<article>`, dan `<footer>` semaksimal mungkin."
                },
                {
                    "title": "Dasar CSS & Box Model",
                    "content": "# Dasar CSS & Box Model\nCSS (Cascading Style Sheets) digunakan untuk mengatur gaya dan layout dari HTML.\n\n## CSS Box Model\nSetiap elemen di web pada dasarnya adalah kotak persegi. Box Model terdiri dari:\n- **Content**: Isi elemen (teks/gambar).\n- **Padding**: Jarak ke dalam (antara border dan content).\n- **Border**: Garis tepi kotak.\n- **Margin**: Jarak ke luar (jarak dengan kotak lain).\n\n```css\n.kartu {\n  background-color: #f4f4f4;\n  padding: 20px;   /* Jarak ke dalam */\n  border: 1px solid #ccc;\n  margin: 15px;    /* Jarak ke luar */\n}\n```\n\n## CSS Reset\nBrowser punya default margin/padding. Selalu reset ini di awal:\n```css\n* {\n  margin: 0;\n  padding: 0;\n  box-sizing: border-box;\n}\n```\n> **Best Practice**: `box-sizing: border-box` mencegah ukuran elemen bertambah saat kamu menambahkan padding atau border."
                }
            ]
        },
        {
            "title": "Level 2: Modern JavaScript",
            "subtitle": "Menghidupkan halaman dengan logika interaktif.",
            "description": "Kuasai ES6+, manipulasi DOM, dan asynchronous programming.",
            "lessons": [
                {
                    "title": "Variabel & Tipe Data ES6",
                    "content": "# Variabel ES6+\nSebelum ES6, JavaScript menggunakan `var`. Sekarang kita menggunakan `let` dan `const` karena scoping-nya lebih terprediksi.\n\n## Let vs Const\n```javascript\n// const: Nilai tidak bisa di-assign ulang\nconst phi = 3.14;\n// phi = 3.15; // Akan error!\n\n// let: Nilai bisa diubah\nlet umur = 20;\numur = 21; // Valid\n```\n\n## Tipe Data\nJavaScript memiliki beberapa tipe data dasar:\n- `String`: Teks (`\"Halo\"`)\n- `Number`: Angka (`10`, `3.14`)\n- `Boolean`: Benar/Salah (`true`/`false`)\n- `Object`: Pasangan key-value\n- `Array`: Kumpulan data bertipe list\n\n> **Best Practice**: Selalu gunakan `const` secara default. Gunakan `let` hanya jika kamu yakin nilai variabel itu akan berubah."
                },
                {
                    "title": "Manipulasi DOM",
                    "content": "# DOM Manipulation\nDOM (Document Object Model) adalah representasi HTML yang bisa dimanipulasi dengan JavaScript.\n\n## Memilih Elemen\n```javascript\nconst judul = document.querySelector('.judul');\nconst semuaTombol = document.querySelectorAll('button');\n```\n\n## Mengubah Konten & Event Listener\n```javascript\nconst tombol = document.getElementById('btn-login');\n\ntombol.addEventListener('click', () => {\n  judul.textContent = 'Login Berhasil!';\n  judul.style.color = 'green';\n});\n```\n\n> **Best Practice**: Simpan elemen DOM dalam variabel agar tidak dipanggil berulang kali di memory."
                },
                {
                    "title": "Asynchronous & Fetch API",
                    "content": "# Asynchronous JavaScript\nWeb modern perlu mengambil data dari server tanpa me-refresh halaman.\n\n## Promises dan Async/Await\n```javascript\nasync function getData() {\n  try {\n    // fetch() mengembalikan Promise\n    const response = await fetch('https://jsonplaceholder.typicode.com/users');\n    \n    // Ubah hasil ke JSON\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error('Terjadi error:', error);\n  }\n}\n\ngetData();\n```\n\n> **Best Practice**: Selalu bungkus `await` di dalam blok `try...catch` agar error koneksi (misal jaringan putus) bisa ditangani dengan rapi tanpa membuat web crash."
                }
            ]
        },
        {
            "title": "Level 3: Responsive Design & Git",
            "subtitle": "Membangun layout fleksibel dan bekerja dengan version control.",
            "description": "Menggunakan Flexbox, Grid, Media Queries, dan Git untuk kolaborasi tim.",
            "lessons": [
                {
                    "title": "Flexbox Layout",
                    "content": "# Flexbox\nFlexbox adalah sistem layout satu dimensi (baris atau kolom) untuk mendistribusikan ruang antar elemen.\n\n## Konsep Utama\n```css\n.container {\n  display: flex;\n  /* Mengatur arah: row atau column */\n  flex-direction: row;\n  /* Mengatur spasi horizontal */\n  justify-content: space-between;\n  /* Mengatur perataan vertikal */\n  align-items: center;\n}\n```\n\n> **Best Practice**: Gunakan Flexbox untuk komponen UI yang sejajar (seperti navbar, form, atau list tombol). Untuk layout dua dimensi, gunakan CSS Grid."
                },
                {
                    "title": "Media Queries (Responsive)",
                    "content": "# Media Queries\nResponsive web design membuat web tampil bagus di HP maupun desktop. Media Queries adalah kuncinya.\n\n## Breakpoints\n```css\n/* Default: Style untuk Mobile (Mobile-First) */\n.konten {\n  width: 100%;\n}\n\n/* Saat layar lebih dari 768px (Tablet/Desktop) */\n@media (min-width: 768px) {\n  .konten {\n    width: 50%;\n  }\n}\n```\n\n> **Best Practice**: Gunakan pendekatan **Mobile-First**. Tulis CSS untuk layar kecil terlebih dahulu, lalu tambahkan `@media (min-width: ...)` untuk modifikasi di layar yang lebih besar."
                },
                {
                    "title": "Dasar Git & GitHub",
                    "content": "# Git & Version Control\nGit adalah mesin waktu untuk kodemu. Jika salah, kamu bisa mundur ke versi sebelumnya.\n\n## Alur Kerja Git\n1. `git init` - Inisialisasi repo.\n2. `git add .` - Masukkan file ke staging area.\n3. `git commit -m \"Pesan\"` - Simpan snapshot kode.\n4. `git push origin main` - Kirim kode ke GitHub.\n\n> **Best Practice**: Tulis commit message yang deskriptif. Contoh buruk: `\"update file\"`. Contoh baik: `\"feat: tambah form login dan validasi\"`."
                }
            ]
        },
        {
            "title": "Level 4: React.js / Next.js",
            "subtitle": "Framework UI paling populer di dunia.",
            "description": "Membangun aplikasi single-page (SPA) dan server-side rendering (SSR) dengan ekosistem React.",
            "lessons": [
                {
                    "title": "Komponen & JSX",
                    "content": "# Pengenalan React\nReact menggunakan komponen (potongan UI kecil) yang digabung menjadi satu halaman. JSX adalah syntax mirip HTML di dalam JavaScript.\n\n## Contoh Komponen\n```jsx\nfunction Tombol({ teks }) {\n  return (\n    <button className=\"btn-merah\">\n      {teks}\n    </button>\n  );\n}\n\nexport default function App() {\n  return (\n    <div>\n      <h1>Halo React</h1>\n      <Tombol teks=\"Klik Saya\" />\n    </div>\n  );\n}\n```\n\n> **Best Practice**: Pecah kodemu menjadi komponen kecil-kecil agar mudah digunakan ulang (reusable) dan tidak berantakan."
                },
                {
                    "title": "State & Props",
                    "content": "# State & Props\n- **Props**: Data yang dikirim dari luar (Parent ke Child).\n- **State**: Data internal komponen yang bisa berubah-ubah.\n\n## Menggunakan useState\n```jsx\nimport { useState } from 'react';\n\nexport default function Counter() {\n  const [hitung, setHitung] = useState(0);\n\n  return (\n    <div>\n      <p>Angka saat ini: {hitung}</p>\n      <button onClick={() => setHitung(hitung + 1)}>\n        Tambah 1\n      </button>\n    </div>\n  );\n}\n```\n\n> **Best Practice**: Jangan pernah mengubah state secara langsung (misal: `hitung = 10`). Selalu gunakan fungsi setter (`setHitung(10)`)."
                },
                {
                    "title": "Hooks (useEffect)",
                    "content": "# useEffect\n`useEffect` digunakan untuk menjalankan efek samping (side effects) seperti fetching data dari API saat komponen pertama kali dimuat.\n\n## Fetching Data\n```jsx\nimport { useState, useEffect } from 'react';\n\nfunction DaftarUser() {\n  const [users, setUsers] = useState([]);\n\n  useEffect(() => {\n    fetch('https://api.example.com/users')\n      .then(res => res.json())\n      .then(data => setUsers(data));\n  }, []); // Array kosong = hanya jalan sekali saat awal muat\n\n  return (\n    <ul>\n      {users.map(u => <li key={u.id}>{u.nama}</li>)}\n    </ul>\n  );\n}\n```\n\n> **Best Practice**: Pastikan kamu mengisi *dependency array* `[]` dengan benar. Jika lupa menaruhnya, API akan dipanggil terus-menerus tanpa henti (infinite loop)!"
                }
            ]
        }
    ],
    "backend-developer": [
        {
            "title": "Level 1: HTTP & REST API",
            "subtitle": "Bahasa komunikasi di internet.",
            "description": "Pahami bagaimana client dan server bertukar data menggunakan protokol HTTP dan standar REST.",
            "lessons": [
                {
                    "title": "Konsep Protokol HTTP",
                    "content": "# Protokol HTTP\nHTTP adalah fondasi dari komunikasi web. Ada dua hal utama: **Request** (permintaan dari client) dan **Response** (jawaban dari server).\n\n## HTTP Methods\n- `GET`: Mengambil data (misal: lihat profil).\n- `POST`: Mengirim data baru (misal: submit form).\n- `PUT`/`PATCH`: Mengubah data.\n- `DELETE`: Menghapus data.\n\n## Status Codes\n- **2xx**: Berhasil (200 OK, 201 Created).\n- **4xx**: Error di sisi client (400 Bad Request, 404 Not Found).\n- **5xx**: Error di sisi server (500 Internal Server Error).\n\n> **Best Practice**: Jangan pernah gunakan metode `GET` untuk mengubah atau menghapus data. Gunakan sesuai fungsinya."
                },
                {
                    "title": "Desain REST API",
                    "content": "# REST API\nREST (Representational State Transfer) adalah gaya arsitektur untuk merancang API.\n\n## Aturan Penamaan Endpoint (URI)\nGunakan kata benda jamak (plural nouns) dan jangan gunakan kata kerja.\n\n- **BENAR**: `GET /users` (Ambil semua user)\n- **BENAR**: `POST /users` (Buat user baru)\n- **BENAR**: `GET /users/123` (Ambil user ID 123)\n- **SALAH**: `GET /getUsers` atau `POST /createUser`\n\n> **Best Practice**: Konsisten. Jika menggunakan huruf kecil dan jamak (`/products`), terapkan pola itu ke seluruh API kamu."
                },
                {
                    "title": "JSON (JavaScript Object Notation)",
                    "content": "# JSON\nJSON adalah format standar untuk mengirim data lewat API. Sintaksnya ringan dan mudah dibaca manusia.\n\n## Contoh JSON\n```json\n{\n  \"status\": \"success\",\n  \"data\": {\n    \"id\": 123,\n    \"nama\": \"Budi\",\n    \"is_active\": true,\n    \"roles\": [\"admin\", \"user\"]\n  }\n}\n```\n\n> **Best Practice**: Pastikan format kembalian (response) API kamu selalu konsisten, misalnya selalu ada key `status` dan `data`, walau error sekalipun (misal kembalikan `message` error)."
                }
            ]
        },
        {
            "title": "Level 2: Node.js & Express / Python FastAPI",
            "subtitle": "Membangun server backend pertamamu.",
            "description": "Menggunakan bahasa pemrograman untuk membuat routing, controller, dan middleware.",
            "lessons": [
                {
                    "title": "Inisialisasi Server",
                    "content": "# Server Express (Node.js)\nExpress.js adalah framework paling populer di Node.js untuk membuat web server.\n\n## Hello World\n```javascript\nconst express = require('express');\nconst app = express();\n\n// Middleware membaca body JSON\napp.use(express.json());\n\napp.get('/', (req, res) => {\n  res.json({ message: \"Hello Backend!\" });\n});\n\napp.listen(8000, () => {\n  console.log('Server jalan di port 8000');\n});\n```\n\n> **Best Practice**: Selalu tambahkan middleware `express.json()` jika ingin menerima payload JSON, kalau tidak body request akan bernilai `undefined`."
                },
                {
                    "title": "Routing & Controller",
                    "content": "# Memisahkan Logika (Controller)\nJangan satukan semua kode di file utama (`index.js`). Pisahkan berdasarkan *resource*.\n\n## Contoh Pemisahan\nDi file `user.controller.js`:\n```javascript\nexports.getUsers = (req, res) => {\n  const users = [{id: 1, name: 'Budi'}];\n  res.status(200).json(users);\n};\n```\nDi file `routes.js`:\n```javascript\nconst userCtrl = require('./user.controller');\nconst express = require('express');\nconst router = express.Router();\n\nrouter.get('/users', userCtrl.getUsers);\nmodule.exports = router;\n```\n\n> **Best Practice**: Gunakan arsitektur MVC (Model-View-Controller) atau pola Layered agar proyek mudah di-maintenance saat membesar."
                },
                {
                    "title": "Middleware",
                    "content": "# Konsep Middleware\nMiddleware adalah fungsi yang dipanggil **sebelum** request mencapai controller. Berguna untuk logging, auth, atau manipulasi data.\n\n## Contoh Middleware Logging\n```javascript\nfunction logger(req, res, next) {\n  console.log(`${req.method} request ke ${req.url}`);\n  next(); // Wajib dipanggil agar lanjut ke fungsi berikutnya!\n}\n\n// Mendaftarkan middleware global\napp.use(logger);\n```\n\n> **Best Practice**: Selalu panggil fungsi `next()` di dalam middleware. Jika lupa, request akan menggantung (hang) dan timeout."
                }
            ]
        },
        {
            "title": "Level 3: SQL & PostgreSQL",
            "subtitle": "Menyimpan data secara permanen dan terstruktur.",
            "description": "Mendesain skema database relasional dan menggunakan SQL atau ORM.",
            "lessons": [
                {
                    "title": "Dasar SQL Query",
                    "content": "# SQL (Structured Query Language)\nCara berinteraksi dengan database relasional (PostgreSQL, MySQL).\n\n## CRUD Dasar\n```sql\n-- Create (INSERT)\nINSERT INTO users (nama, umur) VALUES ('Acel', 25);\n\n-- Read (SELECT)\nSELECT id, nama FROM users WHERE umur > 20;\n\n-- Update\nUPDATE users SET nama = 'Acel Baru' WHERE id = 1;\n\n-- Delete\nDELETE FROM users WHERE id = 1;\n```\n\n> **Best Practice**: **JANGAN PERNAH** menjalankan query `UPDATE` atau `DELETE` tanpa kondisi `WHERE`. Jika kamu melakukannya, kamu akan menghapus seluruh isi database!"
                },
                {
                    "title": "Relasi & JOIN",
                    "content": "# Relasi Data\nKekuatan database relasional adalah kemampuannya menghubungkan data dari tabel berbeda.\n\n## INNER JOIN\n```sql\nSELECT users.nama, orders.total_harga \nFROM users\nINNER JOIN orders ON users.id = orders.user_id;\n```\n*Query di atas mengambil nama user dan harga barang yang ia beli dengan mencocokkan `user_id`.*\n\n> **Best Practice**: Selalu berikan index (pengindeksan) pada kolom yang sering dijadikan kondisi JOIN atau pencarian (seperti `user_id`) untuk mempercepat query secara drastis."
                },
                {
                    "title": "Menggunakan ORM (Prisma)",
                    "content": "# Object-Relational Mapping (ORM)\nORM memampukan kita menulis query ke database menggunakan kode JavaScript/Python, tanpa harus menulis raw SQL secara manual.\n\n## Contoh dengan Prisma\n```javascript\n// Prisma akan meng-generate query SQL secara otomatis di balik layar\nconst user = await prisma.user.create({\n  data: {\n    nama: \"Budi\",\n    email: \"budi@example.com\"\n  }\n});\n\nconst allUsers = await prisma.user.findMany({\n  where: { isActive: true }\n});\n```\n\n> **Best Practice**: Gunakan ORM untuk tugas-tugas standar (CRUD) karena lebih aman dari *SQL Injection*, tapi kuasai raw SQL untuk optimasi query kompleks."
                }
            ]
        },
        {
            "title": "Level 4: Authentication & Security",
            "subtitle": "Mengamankan API dari akses ilegal.",
            "description": "Implementasi hashing password, JWT, dan pengamanan dasar backend.",
            "lessons": [
                {
                    "title": "Hashing Password (Bcrypt)",
                    "content": "# Hashing Password\n**Jangan pernah menyimpan password pengguna dalam bentuk plain text!** Jika database bocor, habislah sudah.\n\n## Menggunakan Bcrypt\nBcrypt akan mengenkripsi satu arah (hash).\n```javascript\nconst bcrypt = require('bcrypt');\n\n// Mendaftar (Hash)\nconst passwordAsli = \"rahasia123\";\nconst hashedPassword = await bcrypt.hash(passwordAsli, 10);\n\n// Login (Compare)\nconst isMatch = await bcrypt.compare(\"rahasia123\", hashedPassword);\n// isMatch = true\n```\n\n> **Best Practice**: Tambahkan \"Salt\" (angka `10` di atas) agar password yang sama (misal \"12345\") akan menghasilkan hash yang acak dan unik per user."
                },
                {
                    "title": "JSON Web Tokens (JWT)",
                    "content": "# JWT (JSON Web Token)\nJWT adalah metode untuk memberikan kartu identitas (token) kepada user setelah login berhasil.\n\n## Cara Kerja\n1. User login dengan email & password.\n2. Server verifikasi, lalu membuat JWT rahasia dan dikembalikan ke user.\n3. Di request berikutnya, user menyisipkan JWT di header `Authorization: Bearer <token>`.\n\n```javascript\nconst jwt = require('jsonwebtoken');\n\n// Membuat token (Berlaku 1 jam)\nconst token = jwt.sign({ userId: 1 }, \"KUNCI_RAHASIA\", { expiresIn: \"1h\" });\n\n// Verifikasi token (biasanya di Middleware)\nconst decoded = jwt.verify(token, \"KUNCI_RAHASIA\");\n```\n\n> **Best Practice**: Gunakan waktu kedaluwarsa (`expiresIn`) yang pendek. Jangan simpan data sensitif seperti password di dalam isi/payload JWT."
                },
                {
                    "title": "CORS & Security Headers",
                    "content": "# CORS (Cross-Origin Resource Sharing)\nSecara default, browser memblokir request API jika frontend dan backend berbeda domain (misal web di `vercel.app` tapi API di `onrender.com`).\n\n## Setup CORS\n```javascript\nconst cors = require('cors');\n\n// Mengizinkan frontend tertentu\napp.use(cors({\n  origin: 'https://nama-frontend-kamu.vercel.app',\n  methods: ['GET', 'POST']\n}));\n```\n\n> **Best Practice**: Di server production, JANGAN gunakan `cors()` tanpa konfigurasi (allow origin `*`). Selalu whitelist domain spesifik demi alasan keamanan."
                }
            ]
        }
    ],
    "fullstack-developer": [
        {
            "title": "Level 1: Tinjauan Frontend & Backend",
            "subtitle": "Koneksi antara dua dunia.",
            "description": "Memahami arsitektur Client-Server secara utuh sebelum masuk ke pengkodean.",
            "lessons": [
                {
                    "title": "Arsitektur Client-Server",
                    "content": "# Arsitektur Client-Server\nSebagai fullstack, kamu berdiri di dua dunia: Frontend (Client) dan Backend (Server).\n\n## Peran Masing-masing\n- **Client (Frontend)**: Berjalan di browser user. Bertanggung jawab atas UI, UX, animasi, dan merender data.\n- **Server (Backend)**: Berjalan di mesin remote. Bertanggung jawab atas validasi data rahasia, pengolahan database, dan security.\n\n> **Best Practice**: Validasi data harus selalu dilakukan di KEDUA sisi. Validasi frontend untuk kenyamanan UX, validasi backend wajib untuk keamanan sejati."
                },
                {
                    "title": "Data Flow (Aliran Data)",
                    "content": "# Aliran Data (Flow)\nBagaimana sebuah tweet dikirim?\n\n1. User klik tombol kirim (Frontend React).\n2. React menjalankan fungsi `fetch()` mengirim payload JSON.\n3. Backend (Node.js) menerima JSON, mengecek token auth dari Header.\n4. Jika valid, Backend menyimpan tweet via SQL ke Database (PostgreSQL).\n5. Backend membalas JSON `status: 201 Created`.\n6. React mengubah state dan menampilkan tweet tersebut tanpa refresh layar.\n\n> **Best Practice**: Gunakan loading state (spinner/skeleton) di Frontend selama menunggu proses nomor 3 hingga 5 selesai."
                },
                {
                    "title": "Environment Variables",
                    "content": "# Konfigurasi Environment\nBaik frontend maupun backend butuh konfigurasi URL rahasia.\n\n## File `.env`\n```bash\n# Di Backend\nDATABASE_URL=\"postgres://user:pass@host/db\"\nJWT_SECRET=\"rahasia\"\n\n# Di Frontend (Contoh Next.js)\nNEXT_PUBLIC_API_URL=\"https://api.backend.com\"\n```\n\n> **Best Practice**: Jangan PERNAH commit file `.env` ke GitHub (masukkan ke `.gitignore`). Di Frontend, awalan `NEXT_PUBLIC_` atau `VITE_` membuatnya bisa dilihat user, JANGAN taruh secret key di sana!"
                }
            ]
        },
        {
            "title": "Level 2: Membangun API (Backend)",
            "subtitle": "Menyediakan data untuk frontend.",
            "description": "Membuat RESTful API lengkap menggunakan framework modern dan database.",
            "lessons": [
                {
                    "title": "Setup Express & Prisma ORM",
                    "content": "# Stack Backend Populer\nKita gabungkan Express (routing) dan Prisma (ORM).\n\n## Init Prisma\n```bash\nnpm install prisma --save-dev\nnpx prisma init\n```\nIsi file `schema.prisma`:\n```prisma\nmodel Post {\n  id        Int     @id @default(autoincrement())\n  title     String\n  content   String\n}\n```\n\n> **Best Practice**: Setiap ada perubahan di file `schema.prisma`, jangan lupa jalankan `npx prisma db push` atau `prisma migrate` agar struktur tabel sinkron dengan database sungguhan."
                },
                {
                    "title": "CRUD Endpoints",
                    "content": "# Menyelesaikan CRUD\nMari buat Endpoint lengkap.\n\n```javascript\n// CREATE\napp.post('/posts', async (req, res) => {\n  const post = await prisma.post.create({ data: req.body });\n  res.status(201).json(post);\n});\n\n// READ\napp.get('/posts', async (req, res) => {\n  const posts = await prisma.post.findMany();\n  res.json(posts);\n});\n```\n\n> **Best Practice**: Gunakan `try...catch` dan kembalikan response 500 error secara konsisten jika Prisma gagal mengambil data."
                },
                {
                    "title": "Validasi Payload (Zod)",
                    "content": "# Validasi Input\nJangan asal terima data dari user!\n\n## Contoh dengan Zod\n```javascript\nconst { z } = require('zod');\n\nconst postSchema = z.object({\n  title: z.string().min(3),\n  content: z.string()\n});\n\napp.post('/posts', (req, res) => {\n  const parseResult = postSchema.safeParse(req.body);\n  if (!parseResult.success) {\n    return res.status(400).json({ error: parseResult.error });\n  }\n  // lanjut simpan database...\n});\n```\n\n> **Best Practice**: Validasi tipe data (string/int) dan logika bisnis (panjang karakter minimum) sedini mungkin sebelum menyentuh database."
                }
            ]
        },
        {
            "title": "Level 3: Integrasi dengan React (Frontend)",
            "subtitle": "Menyambungkan UI dengan API.",
            "description": "Mengambil dan mengirim data menggunakan useEffect atau library seperti React Query.",
            "lessons": [
                {
                    "title": "Fetch API di React Component",
                    "content": "# Fetch Data di React\nCara manual menggunakan standard `useEffect`.\n\n```jsx\nimport { useEffect, useState } from 'react';\n\nfunction PostList() {\n  const [posts, setPosts] = useState([]);\n  \n  useEffect(() => {\n    fetch('http://localhost:8000/posts')\n      .then(r => r.json())\n      .then(data => setPosts(data));\n  }, []);\n\n  return posts.map(p => <div key={p.id}>{p.title}</div>);\n}\n```\n\n> **Best Practice**: Jangan lupa key pada method `.map()`. Ini penting agar React tahu mana elemen yang diubah atau dihapus (menjaga optimasi render)."
                },
                {
                    "title": "Menggunakan SWR / React Query",
                    "content": "# Data Fetching Modern\nMenulis useEffect untuk fetch data punya banyak kekurangan (tidak ada cache, ribet menangani error).\n\n## Gunakan SWR (atau React Query)\n```jsx\nimport useSWR from 'swr';\n\nconst fetcher = url => fetch(url).then(r => r.json());\n\nfunction PostList() {\n  const { data, error, isLoading } = useSWR('/api/posts', fetcher);\n\n  if (isLoading) return <p>Loading...</p>;\n  if (error) return <p>Gagal memuat!</p>;\n  \n  return data.map(p => <div key={p.id}>{p.title}</div>);\n}\n```\n\n> **Best Practice**: Library fetching akan mengatur caching, deduping, dan retrying secara otomatis. Sangat disarankan untuk aplikasi kelas production!"
                },
                {
                    "title": "Handle Form & POST Data",
                    "content": "# Mengirim Data (POST)\nContoh form sederhana di React yang menembak endpoint backend.\n\n```jsx\nfunction CreatePost() {\n  const handleSubmit = async (e) => {\n    e.preventDefault();\n    const formData = new FormData(e.target);\n    \n    await fetch('http://localhost:8000/posts', {\n      method: 'POST',\n      headers: { 'Content-Type': 'application/json' },\n      body: JSON.stringify(Object.fromEntries(formData))\n    });\n    alert(\"Tersimpan!\");\n  };\n\n  return (\n    <form onSubmit={handleSubmit}>\n      <input name=\"title\" placeholder=\"Judul\" required />\n      <button type=\"submit\">Kirim</button>\n    </form>\n  );\n}\n```\n\n> **Best Practice**: Cegah refresh halaman default HTML dengan `e.preventDefault()` di awal fungsi handleSubmit."
                }
            ]
        },
        {
            "title": "Level 4: Autentikasi Fullstack & Deploy",
            "subtitle": "Mengamankan sesi user dan mengunggah aplikasi ke publik.",
            "description": "Menggabungkan JWT ke dalam workflow React dan deployment terpisah (Vercel & Render).",
            "lessons": [
                {
                    "title": "Alur Login JWT (Frontend)",
                    "content": "# Menyimpan Token\nSetelah backend mengembalikan token JWT, frontend harus menyimpannya.\n\n## LocalStorage vs Cookies\n- **LocalStorage**: Paling gampang diakses lewat Javascript (`localStorage.setItem()`). Namun rentan serangan XSS.\n- **HttpOnly Cookies**: Paling aman. Token dikirim dan disimpan oleh browser secara otomatis, tidak bisa diakses lewat JS.\n\n> **Best Practice**: Jika memungkinkan, atur backend untuk mengembalikan JWT dalam `Set-Cookie: HttpOnly`. Jika memakai LocalStorage, berhati-hatilah terhadap package NPM yang mencurigakan."
                },
                {
                    "title": "Private Routes di React",
                    "content": "# Melindungi Halaman (Private Route)\nJika user belum login, lemparkan dia kembali ke `/login`.\n\n```jsx\nfunction ProtectedRoute({ children }) {\n  const token = localStorage.getItem('token');\n  \n  if (!token) {\n    return <Navigate to=\"/login\" />;\n  }\n  \n  return children;\n}\n\n// Penggunaan di Router\n<Route path=\"/dashboard\" element={\n  <ProtectedRoute>\n    <Dashboard />\n  </ProtectedRoute>\n} />\n```\n\n> **Best Practice**: Ingat, mengecek `token` di frontend BUKAN jaminan keamanan, ini hanya UX (User Experience). Keamanan absolut hanya ada di sisi backend!"
                },
                {
                    "title": "Deployment Strategi",
                    "content": "# Cara Deploy Fullstack\nUmumnya, aplikasi dipisah. Frontend di provider CDN/Edge, Backend di Server biasa.\n\n## Skema Umum\n1. **Frontend**: Deploy kode Next.js/React ke Vercel atau Netlify. Masukkan env `NEXT_PUBLIC_API_URL=https://api.kamu.com`.\n2. **Backend**: Deploy Node.js ke Render atau Railway. Atur CORS agar hanya domain Vercel yang bisa akses.\n3. **Database**: Gunakan Supabase Postgres atau Railway DB, salin `DATABASE_URL` ke env Backend.\n\n> **Best Practice**: Selalu pastikan branch *main/master* di Github adalah branch yang langsung terhubung ke layanan auto-deploy. Jaga kebersihan kode sebelum *push*."
                }
            ]
        }
    ]
}
