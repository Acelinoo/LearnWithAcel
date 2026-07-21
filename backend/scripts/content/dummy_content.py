def get_code_snippet(role_slug):
    snippets = {
        "frontend-developer": ("html", "<h1>Hello Frontend</h1>\n<script>\n  console.log('Welcome to Frontend Development!');\n</script>"),
        "backend-developer": ("javascript", "const express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => {\n  res.send('Hello from Backend!');\n});\napp.listen(3000);"),
        "full-stack-developer": ("javascript", "fetch('/api/data').then(res => res.json()).then(data => console.log(data));"),
        "penetration-tester": ("bash", "# Menjalankan port scanning dasar\nnmap -sV 192.168.1.100"),
        "soc-analyst": ("bash", "# Melihat log autentikasi di Linux\ntail -n 50 /var/log/auth.log | grep 'Failed password'"),
        "security-engineer": ("bash", "# Menambahkan rule firewall sederhana\niptables -A INPUT -p tcp --dport 22 -j ACCEPT"),
        "malware-analyst": ("c", "#include <stdio.h>\nint main() {\n    printf(\"Analyzing malware behavior...\\n\");\n    return 0;\n}"),
        "android-developer": ("kotlin", "fun main() {\n    println(\"Welcome to Android Development with Kotlin!\")\n}"),
        "ios-developer": ("swift", "import SwiftUI\n\nstruct ContentView: View {\n    var body: some View {\n        Text(\"Hello, iOS!\")\n    }\n}"),
        "cross-platform-developer": ("dart", "void main() {\n  print('Building Cross-Platform apps with Flutter!');\n}"),
        "network-engineer": ("text", "Router(config)# interface GigabitEthernet0/0\nRouter(config-if)# ip address 192.168.1.1 255.255.255.0\nRouter(config-if)# no shutdown"),
        "data-scientist": ("python", "import pandas as pd\n\n# Load dataset\ndf = pd.read_csv('data.csv')\nprint(df.head())"),
        "machine-learning-engineer": ("python", "from sklearn.ensemble import RandomForestClassifier\n\nmodel = RandomForestClassifier()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)"),
    }
    return snippets.get(role_slug, ("python", "print('Hello World')"))

def generate_rich_lessons(role_name, role_slug, level_num, module_title):
    SPECIFIC_CONTENT = {
        "HTML & CSS Dasar": [
            ("Pengenalan HTML & Struktur Dokumen Web", 
             "Bayangkan membuat halaman web itu seperti membangun rumah. HTML adalah pondasi dan kerangka betonnya. Tanpa HTML, rumah (web) tidak bisa berdiri karena tidak ada strukturnya.", 
             "Membangun struktur dasar sebuah halaman agar mesin pencari (Google) dan browser mengerti apa isi halaman tersebut.",
             "html", "<!DOCTYPE html>\n<html>\n<head>\n  <title>Rumah Pertamaku</title>\n</head>\n<body>\n  <h1>Selamat Datang!</h1>\n  <p>Ini ruang tamunya.</p>\n</body>\n</html>", 
             "- `<!DOCTYPE html>`: Dokumen HTML5.\n- `<html>`: Pembungkus utama.\n- `<head>`: Info meta/judul.\n- `<body>`: Tubuh konten.",
             "HTML adalah kerangka utama web. Ingat selalu buka dan tutup tag (seperti `<h1>` dan `</h1>`)."),
             
            ("Element, Tag, Attributes & Semantic HTML", 
             "Jika HTML adalah kerangka rumah, Semantic HTML ibarat memberikan label yang jelas pada setiap ruangan: 'Ini Dapur', 'Ini Kamar Tidur'. Jadi, orang buta atau mesin robot (seperti Google) tidak bingung saat berkunjung.", 
             "Meningkatkan SEO (agar mudah dicari di Google) dan membantu pengguna tunanetra membaca web kita dengan Screen Reader.",
             "html", "<article>\n  <header>Judul Cerita</header>\n  <p>Pada suatu hari...</p>\n  <footer>Ditulis oleh Acel</footer>\n</article>", 
             "- `<article>`: Konten artikel mandiri.\n- `<header>`: Judul dari artikel.\n- `<p>`: Paragraf teks.\n- `<footer>`: Catatan kaki.",
             "Gunakan tag yang bermakna seperti `<header>`, `<article>`, dan `<footer>` alih-alih cuma pakai `<div>`."),
             
            ("Dasar CSS (Selector, Properties, Box Model)", 
             "Sekarang bayangkan kamu sedang mengecat rumah dan memilih perabotan. CSS adalah cat dinding, tirai jendela, dan desain interiornya yang membuat rumah terlihat cantik!", 
             "Sebagus apapun sistemnya, pengguna internet sangat peduli dengan tampilan. CSS membuat web kamu enak dipandang.",
             "css", ".kamar-tidur {\n  background-color: lightblue;\n  padding: 20px; /* Jarak ke dalam */\n  margin: 10px; /* Jarak ke luar */\n  border: 1px solid black;\n}", 
             "- `.kamar-tidur`: Memilih elemen class 'kamar-tidur'.\n- `background-color`: Mengubah warna latar.\n- `padding`: Jarak ke dalam.\n- `margin`: Jarak ke luar.",
             "CSS mengubah warna, letak, dan gaya elemen HTML. Setiap elemen adalah kotak (Box Model) yang punya margin, border, dan padding."),
             
            ("Flexbox & Layouting Sederhana", 
             "Pernah mengatur buku-buku di dalam rak buku agar terlihat rapi dan tidak berjatuhan? Flexbox adalah fitur CSS yang mengatur elemen-elemen web (buku) ke dalam baris atau kolom yang rapi secara otomatis.", 
             "Mendesain halaman web untuk layar HP, tablet, dan laptop butuh sistem tata letak (layout) yang fleksibel. Flexbox menyelesaikannya dengan mudah.",
             "css", ".rak-buku {\n  display: flex;\n  justify-content: space-between; /* Bagikan sisa ruang kosong secara rata */\n  align-items: center; /* Sejajarkan di tengah vertikal */\n}", 
             "- `display: flex;`: Mengaktifkan mode Flexbox.\n- `justify-content`: Mengatur spasi horizontal.\n- `align-items`: Menyelaraskan konten di tengah vertikal.",
             "Gunakan `display: flex;` pada kontainer untuk menata isinya secara otomatis, baik ke samping maupun ke bawah.")
        ],
        "Modern JavaScript": [
            ("Variabel & Tipe Data", 
             "JavaScript itu ibarat otot dan sistem saraf yang membuat tubuh bisa bergerak dan merespon sentuhan. Nah, Variabel adalah 'kotak penyimpanan' di dalam otak kita untuk mengingat hal-hal penting seperti nama atau umur.", 
             "Variabel menyimpan data sementara agar program kita bisa memprosesnya nanti.",
             "javascript", "// Mengingat nama (teks) tidak boleh diubah\nconst nama = 'John';\n\n// Mengingat umur (angka) yang bisa berubah tiap tahun\nlet umur = 25;", 
             "- `const`: Variabel permanen (konstanta).\n- `let`: Variabel yang isinya bisa diubah nanti.",
             "Gunakan `const` untuk data yang tetap (seperti tanggal lahir) dan `let` untuk data yang bisa berubah (seperti umur)."),
             
            ("DOM Manipulation", 
             "Bayangkan kamu punya remote control TV ajaib yang bisa mengubah channel, warna TV, dan ukuran TV dari jarak jauh. DOM adalah remote control tersebut untuk memodifikasi halaman web (HTML) langsung pakai JavaScript.", 
             "Memberikan interaksi! Saat pengguna menekan tombol, kita bisa memunculkan popup atau mengubah warna latar.",
             "javascript", "// 1. Cari tombolnya (ambil remotenya)\nconst tombol = document.getElementById('btnSihir');\n\n// 2. Beri aksi saat ditekan\ntombol.addEventListener('click', () => {\n  alert('Abrakadabra!'); // Munculkan pesan\n});", 
             "- `getElementById`: Mengambil elemen berdasarkan ID.\n- `addEventListener`: Menunggu aksi (seperti klik).\n- `alert`: Memunculkan pesan di layar.",
             "Kita bisa menangkap elemen HTML menggunakan `document.getElementById` atau `querySelector`, lalu memberikannya aksi."),
             
            ("Asynchronous & Promises", 
             "Pernah pesan makanan di restoran cepat saji? Setelah pesan, kamu diberi nomor antrean lalu kamu bebas main HP sambil menunggu. Saat makanan siap, nomor antrean dipanggil. Itulah Asynchronous (Tidak menahan proses lainnya).", 
             "JavaScript sering harus mengambil data dari server jauh. Kalau sistemnya ditahan (synchronous), halaman web akan 'hang' atau membeku sampai datanya datang.",
             "javascript", "// Pakai 'await' untuk sabar menunggu data tiba\nasync function ambilData() {\n  const respon = await fetch('https://api.buku.com');\n  const dataBuku = await respon.json();\n  console.log(dataBuku);\n}", 
             "- `async`: Menandai fungsi ini asinkron.\n- `await fetch()`: Mengambil data dari URL.\n- `await json()`: Mengubah respons menjadi objek JavaScript.",
             "Kata kunci `async/await` membuat kode yang berjalan secara asinkron terlihat rapi dan mudah dibaca (seperti kode sinkron)."),
             
            ("Studi Kasus: To-Do List", 
             "Ini adalah ujian terakhir. Kita akan menyatukan kerangka (HTML), cat (CSS), dan otot (JavaScript) untuk membuat aplikasi Daftar Tugas.", 
             "Latihan langsung adalah cara terbaik menguji pemahaman. Aplikasi To-Do List adalah standar portofolio pertama bagi Web Developer.",
             "javascript", "const daftarTugas = []; // Kotak kosong\n\nfunction tambahTugas(tugasBaru) {\n  daftarTugas.push(tugasBaru); // Masukkan ke kotak\n  tampilkanKeLayar(); // Update tampilan (HTML)\n}", 
             "- `[]`: Membuat array (daftar) kosong.\n- `push(baru)`: Memasukkan item baru ke daftar.\n- `tampilkanKeLayar()`: Memanggil fungsi lain.",
             "Pecah masalah besar menjadi fungsi-fungsi kecil yang mudah dipahami. Misalnya fungsi untuk tambah, hapus, dan tampilkan.")
        ],
        "React.js / Next.js": [
            ("Komponen & Props", 
             "Pernah main balok Lego? Kamu punya balok standar, jendela, dan roda yang bisa dipakai berulang kali untuk membuat mobil atau rumah. React itu sama: kita membangun web menggunakan 'balok Lego' yang disebut Komponen.", 
             "Membuat web jadi sangat cepat karena kita tidak perlu menulis ulang kode. Kita cuma pakai ulang komponen yang sama di berbagai halaman.",
             "jsx", "// Ini cetakan Lego kita\nfunction TombolMerah(props) {\n  return <button style={{color: 'red'}}>{props.teks}</button>;\n}\n\n// Cara memakainya:\n<TombolMerah teks='Hapus Data' />\n<TombolMerah teks='Keluar' />", 
             "- `function TombolMerah`: Mendefinisikan komponen.\n- `props.teks`: Mengambil data dari luar.\n- `<TombolMerah ... />`: Memanggil dan menampilkan komponen.",
             "Komponen memisahkan desain UI menjadi potongan independen. Props adalah cara mengirim pesan (data) ke komponen tersebut."),
            ("State & Hooks", 
             "Bayangkan kamu punya papan skor bola basket di kepalamu. Setiap kali bola masuk, kamu mengingat skor baru. Di React, ingatan atau memori sementara komponen itu disebut State.", 
             "Aplikasi butuh mengingat sesuatu, misalnya apakah pengguna sudah login, atau sudah menekan tombol 'Like'. State memungkinkan UI bereaksi terhadap perubahan data.",
             "jsx", "import { useState } from 'react';\n\nfunction PapanSkor() {\n  // Memori skor, nilai awalnya 0\n  const [skor, setSkor] = useState(0);\n\n  // Tombol untuk menambah skor\n  return <button onClick={() => setSkor(skor + 1)}>Skor: {skor}</button>;\n}", 
             "- `useState(0)`: Menginisialisasi state dengan angka 0.\n- `skor`: Variabel pembaca nilai.\n- `setSkor`: Fungsi untuk mengubah nilai.",
             "Gunakan hook `useState` untuk menyimpan data di komponen. Saat data (state) berubah, UI otomatis diperbarui (re-render)."),
            ("Next.js Routing", 
             "Kalau React cuma ngurusin satu ruangan, Next.js ngurusin satu gedung apartemen. Next.js punya lift otomatis (Routing). Cukup bikin file baru di folder `app/`, otomatis jadi halaman baru webmu!", 
             "Routing bawaan Next.js membuat pembuatan multi-halaman super gampang dan otomatis Search Engine Optimized (SEO) tanpa konfigurasi rumit.",
             "jsx", "// Simpan di folder: app/tentang/page.jsx\n// Bakal otomatis jadi halaman web: domain.com/tentang\nexport default function TentangKami() {\n  return <h1>Halaman Tentang Kami</h1>;\n}", 
             "- `export default`: Mengekspor komponen untuk digunakan sistem.\n- `app/tentang/page.jsx`: Path file menjadi rute '/tentang'.",
             "File-based routing di Next.js mempercepat pengembangan web. Gunakan kurung siku `[id].jsx` untuk halaman yang isinya dinamis."),
            ("Studi Kasus: Dashboard", 
             "Sekarang kita rakit semua balok Lego-nya (Komponen, State, dan Halaman). Kita mau bikin ruang kontrol pesawat ruang angkasa (Dashboard Admin) yang interaktif.", 
             "Aplikasi sesungguhnya di industri butuh manajemen state kompleks dan tata letak berlapis (seperti Sidebar di samping, konten utama di kanan).",
             "jsx", "export default function DashboardAdmin() {\n  return (\n    <LayoutGedung>\n       <SidebarNavigasi />\n       <KontenUtama />\n    </LayoutGedung>\n  );\n}", 
             "- `<LayoutGedung>`: Komponen pembungkus.\n- `<SidebarNavigasi />`: Navigasi samping.\n- `<KontenUtama />`: Isi aplikasi.",
             "Dalam proyek besar, pisahkan dengan jelas komponen yang bertugas mengambil data (Logic) dan yang bertugas menampilkan data (UI).")
        ],
        "HTTP & REST API": [
            ("Konsep HTTP & Request/Response", 
             "HTTP itu persis seperti memesan makanan di restoran. Klien (kamu) memanggil pelayan dan memesan makanan (HTTP Request). Server (Dapur) menerima pesan, memasak, lalu pelayan membawa kembali makanan (HTTP Response).", 
             "Dunia internet beroperasi 100% menggunakan protokol HTTP ini. Jika kamu mengerti siklus ini, kamu paham cara kerja internet.",
             "text", "--- Klien (Browser) ---\nGET /api/menu HTTP/1.1\n\n--- Server (Backend) ---\nHTTP/1.1 200 OK\n{'menu': 'Nasi Goreng'}", 
             "- `GET`: Metode meminta data.\n- `HTTP/1.1`: Versi protokol HTTP.\n- `200 OK`: Kode sukses.",
             "Request adalah permintaan data ke server. Response adalah jawaban dari server (berhasil atau gagal)."),
            ("HTTP Methods", 
             "Di restoran, kamu bisa meminta Menu (GET), membuat Pesanan Baru (POST), meminta masakan Ditambah Bumbu (PUT/PATCH), atau Membatalkan Pesanan (DELETE). Inilah HTTP Methods!", 
             "Menggunakan metode standar ini bikin semua programmer dari berbagai bahasa pemrograman punya kesepakatan yang sama (RESTful).",
             "javascript", "fetch('/api/buku', {\n  method: 'POST', // 'Tolong catat data baru!'\n  body: JSON.stringify({ judul: 'Harry Potter' })\n});", 
             "- `fetch`: Melakukan request.\n- `method: 'POST'`: Mode kirim data.\n- `JSON.stringify`: Mengubah objek jadi string.",
             "Gunakan GET untuk membaca data, POST untuk menambah data baru, PUT/PATCH untuk mengedit, dan DELETE untuk menghapus."),
            ("Status Codes", 
             "Ketika pelayan kembali dari dapur, dia bisa bilang: 'Silakan dimakan (200 OK)', 'Maaf alamat meja tidak ketemu (404 Not Found)', atau 'Maaf koki sedang pingsan (500 Server Error)'. Ini adalah kode status.", 
             "Kode status mempermudah Frontend mengetahui apakah operasinya berhasil atau ada masalah, tanpa perlu membaca pesan teks panjang-lebar.",
             "json", "{\n  \"status\": 404,\n  \"pesan_error\": \"Barang tidak ditemukan di gudang\"\n}", 
             "- `404`: Kode error untuk Not Found.\n- `pesan_error`: Pesan yang bisa dibaca manusia.",
             "Kelompok 2xx berarti Sukses, 4xx berarti Klien (pengguna) salah, dan 5xx berarti Server (backend) yang bermasalah."),
            ("Studi Kasus: Desain API", 
             "Mari kita merancang menu restoran yang rapi. Jangan tulis menu seperti 'TolongAmbilSatuBuku', tapi tulis saja '/buku' (jika butuh banyak) atau '/buku/1' (jika butuh satu).", 
             "API yang kotor dan acak-acakan bikin bingung tim Frontend. REST API mewajibkan aturan penulisan tautan yang rapi dan konsisten.",
             "text", "Bagus (RESTful):\nGET /artikel -> Ambil semua artikel\nPOST /artikel -> Bikin artikel baru\n\nJelek:\nGET /ambil-semua-artikel\nPOST /bikin-artikel-baru", 
             "- `GET /artikel`: Baik (Ambil semua).\n- `POST /bikin...`: Buruk (Tidak RESTful).",
             "Gunakan kata benda (Noun) dan jauhi kata kerja dalam merancang Endpoint. Metode HTTP-nya (GET/POST) sudah menjadi kata kerjanya!")
        ],
        "SQL & PostgreSQL": [
            ("Pengenalan Database & Tabel", 
             "Bayangkan database relasional (SQL) itu seperti buku kas di Microsoft Excel yang sangat canggih dan anti-rusak. Data disimpan dalam bentuk baris dan kolom yang rapi pada 'Tabel'.", 
             "Menyimpan data di memori biasa akan hilang saat listrik mati. Database menyimpan data secara permanen, aman, dan bisa dicari dalam hitungan milidetik.",
             "sql", "CREATE TABLE Pengguna (\n  id SERIAL PRIMARY KEY, /* NIK Unik */\n  nama VARCHAR(50),      /* Kolom nama (maksimal 50 huruf) */\n  umur INT               /* Kolom umur (berupa angka) */\n);", 
             "- `SERIAL PRIMARY KEY`: ID berurut otomatis.\n- `VARCHAR(50)`: Teks panjang maksimal 50.\n- `INT`: Tipe data angka.",
             "Tabel menyimpan kategori objek (misal tabel Pengguna, tabel Transaksi). 'Primary Key' adalah nomor KTP unik setiap baris data."),
            ("CRUD dengan SQL", 
             "Bagaimana cara berinteraksi dengan tabel? Cukup perintahkan dengan bahasa inggris sederhana. SELECT (pilih/baca), INSERT (masukkan), UPDATE (perbarui), DELETE (hapus).", 
             "Ini adalah 4 operasi wajib yang dipakai di hampir seluruh aplikasi di dunia untuk memodifikasi datanya.",
             "sql", "-- 1. Masukkan pelanggan baru\nINSERT INTO Pengguna (nama, umur) VALUES ('Budi', 20);\n\n-- 2. Cari Budi\nSELECT * FROM Pengguna WHERE nama = 'Budi';", 
             "- `INSERT INTO`: Menambah data.\n- `VALUES`: Nilai kolomnya.\n- `SELECT *`: Ambil semua kolom.\n- `WHERE`: Filter data.",
             "Selalu perhatikan dan waspada saat pakai UPDATE dan DELETE! Kalau lupa menambahkan klausa 'WHERE', semua data di database bisa ikut terhapus."),
            ("Relasi Antar Tabel & JOIN", 
             "Gimana caranya menghubungkan buku absensi kelas dengan buku perpustakaan? Keduanya dihubungkan pakai 'Nomor Induk Siswa' (ID). Inilah gunanya JOIN, dia menarik info dari 2 buku tabel yang beda jadi satu.", 
             "Membantu memecah data agar tidak ada duplikasi mubazir, tapi kita tetap bisa melihat laporan datanya secara utuh bersamaan.",
             "sql", "-- Gabungkan informasi dari tabel Pelanggan dan Pesanan pakai kunci ID Pelanggan\nSELECT Pelanggan.nama, Pesanan.total_harga \nFROM Pelanggan\nJOIN Pesanan ON Pelanggan.id = Pesanan.pelanggan_id;", 
             "- `JOIN`: Menggabungkan tabel.\n- `ON`: Aturan/syarat gabung (ID sama).",
             "Gunakan 'Foreign Key' untuk merujuk tabel lain. INNER JOIN menggabungkan data yang sama-sama ada di kedua tabel."),
            ("Studi Kasus: Desain Skema Toko", 
             "Sekarang kita rancang pondasi toko online. Ada Tabel Barang, ada Tabel Pelanggan, dan Tabel Pesanan. Bagaimana 3 tabel ini saling bertautan tanpa membingungkan server?", 
             "Desain database yang salah dari awal akan membuat aplikasi jadi lambat parah atau sering error ketika penggunanya membeludak.",
             "sql", "-- Skema Dasar:\nCREATE TABLE Produk (id SERIAL PRIMARY KEY, harga INT);\nCREATE TABLE Keranjang (id SERIAL PRIMARY KEY, produk_id INT);", 
             "- `produk_id INT`: Foreign key merujuk ke tabel lain.",
             "Konsep 'Normalisasi' memastikan tidak ada data yang mubazir. Desainlah tabel yang kecil dan spesifik lalu gabungkan saat perlu ditarik laporannya.")
        ],
        "Authentication & Security": [
            ("Autentikasi vs Otorisasi", 
             "Bayangkan kamu naik pesawat. Waktu check-in, petugas minta KTP untuk cek 'Siapa kamu?' (Ini Autentikasi). Lalu kamu masuk kabin kelas bisnis, pramugari akan cegat dan bilang 'Tiketmu ekonomi, kamu tidak berhak duduk di sini' (Ini Otorisasi).", 
             "Tanpa Autentikasi, siapapun bisa masuk ke aplikasimu. Tanpa Otorisasi, pengguna biasa bisa seenaknya hapus data bos/admin.",
             "javascript", "function periksaAkses(user) {\n  if (!user.isLogin) return 'Stop! KTP mana? (Authn Gagal)';\n  if (user.role !== 'admin') return 'Stop! Kelas Ekonomi (Authz Gagal)';\n  return 'Silakan masuk, Pak Admin!';\n}", 
             "- `user.isLogin`: Cek autentikasi.\n- `user.role`: Cek otorisasi.",
             "Selalu ingat: Autentikasi = Buktikan Identitasmu. Otorisasi = Apa wewenangmu?"),
            ("Hashing Password", 
             "Jangan pernah menulis password 'rahasia123' di database seperti tulisan biasa! Kalau database dicuri hacker, tamatlah riwayat penggunamu. Kita gunakan mesin penggiling daging (Hashing) yang menghancurkan password jadi string acak, tapi masih bisa diverifikasi mesin.", 
             "Ini adalah hukum emas di industri keamanan siber (cybersecurity).",
             "javascript", "const bcrypt = require('bcrypt');\n\n// Password asli: 'katasandi123'\n// Hashing merusaknya jadi: '$2b$10$C8qH...'\nconst passwordAman = await bcrypt.hash('katasandi123', 10);", 
             "- `bcrypt.hash`: Mengenkripsi teks.\n- `10`: Salting rounds (kekuatan enkripsi).",
             "Gunakan pustaka seperti `bcrypt` untuk mengacak (hash) password. Jangan pakai metode kuno seperti MD5."),
            ("JSON Web Tokens (JWT)", 
             "JWT itu seperti tiket gelang konser vip VIP di pergelangan tanganmu. Sekali masuk gerbang, kamu dicap tiket gelang, dan setelah itu bebas hilir mudik antar panggung tanpa harus ngasih KTP lagi setiap detik.", 
             "JWT sangat cepat dan irit, karena server tidak perlu mengingat siapa kamu di memorinya (Stateless), server cukup melihat keaslian tanda tangan di tiket gelangmu.",
             "javascript", "const jwt = require('jsonwebtoken');\n\n// Bikin tiket gelang untuk 1 jam\nconst tiketGelang = jwt.sign({ idUser: 8 }, 'RAHASIA_NEGARA', { expiresIn: '1h' });", 
             "- `jwt.sign`: Membuat token.\n- `{ idUser: 8 }`: Data yang disimpan di token.\n- `expiresIn`: Batas waktu kadaluarsa.",
             "JWT ditaruh di header request. Jangan pernah menyimpan password mentah di dalam payload tiket gelang JWT!"),
            ("Studi Kasus: Sistem Login Aman", 
             "Ujian akhir di tahap ini adalah merakit kunci brankas perpaduan JWT dan Bcrypt. Gimana kita cegah robot hacker (Brute Force) yang mencoba tebak password jutaan kali per detik?", 
             "Membuat sistem login yang aman menjaga reputasi aplikasimu di mata klien.",
             "javascript", "// Limitasi agar cuma boleh login 5x salah\nconst limit = rateLimiter({ max: 5 });\napp.post('/login', limit, prosesLogin);", 
             "- `rateLimiter`: Membatasi jumlah request.\n- `limit`: Menerapkan batasan pada endpoint tertentu.",
             "Selain hash password, selalu batasi jumlah percobaan login menggunakan teknik Rate Limiting (batas kecepatan hitungan API).")
        ],
        "Linux Basics": [
            ("Pengenalan Terminal & Navigasi", 
             "Membuka Linux itu rasanya seperti masuk ke gudang gelap tanpa lampu; kamu butuh senter (perintah teks/Terminal). Perintah `pwd` ibarat nanya 'Saya lagi di mana?', dan `ls` itu 'Ada barang apa aja di sekitar sini?'.", 
             "Server raksasa di seluruh dunia jarang pakai tampilan Mouse dan Windows yang cantik. Semuanya dikendalikan pakai ketikan jari di layar hitam.",
             "bash", "pwd      # Print Working Directory: Di folder mana saya?\nls       # List: Cek isi folder\ncd /home # Change Directory: Pindah ke folder rumah", 
             "- `pwd`: Cetak lokasi saat ini.\n- `ls`: List isi folder.\n- `cd`: Ganti folder aktif.",
             "Biasakan pakai tombol TAB di keyboard saat ngetik di terminal untuk memunculkan otomatis sisa katanya (Autocomplete)."),
            ("Manajemen File", 
             "Memindahkan barang di Linux itu seperti bawa kotak paket. `mkdir` bikin dus kosong, `cp` fotokopi isi dus, dan `mv` memindahkan atau mengganti nama label dus.", 
             "Semua konfigurasi di Linux berbentuk file teks (bukan Registry). Bisa atur file = bisa atur nyawa sistem.",
             "bash", "mkdir ProyekBaru    # Bikin folder baru\ncp rahasia.txt salinan.txt # Fotokopi file\nrm -rf Virus/       # Hapus paksa folder Virus", 
             "- `mkdir`: Membuat folder.\n- `cp`: Kopi file.\n- `rm -rf`: Hapus folder paksa.",
             "Hati-hati dengan perintah `rm -rf`, ibarat bawa bom penghancur. Kalau ngetik salah sasaran, file penting lenyap tanpa ampun!"),
            ("Izin & Kepemilikan (Permissions)", 
             "Setiap file di Linux punya satpam masing-masing. Satpam ini mengatur siapa yang boleh Baca (Read), Tulis (Write), dan Menjalankan File (Execute). Hak akses tertinggi dipegang oleh Presiden (Root/Superuser).", 
             "Menjaga agar pengguna biasa tidak bisa secara tak sengaja menghapus konfigurasi sistem inti yang membahayakan nyawa server.",
             "bash", "sudo su             # Menyamar jadi superuser / Root\nchmod 777 skrip.sh  # Memberi izin semuanya ke siapa saja (HATI-HATI!)\nchmod 755 skrip.sh  # Izin aman (Read & Execute)", 
             "- `sudo su`: Masuk ke mode admin.\n- `chmod 777`: Buka semua hak akses (Bahaya).\n- `chmod 755`: Hak akses normal.",
             "Perintah `chmod` mengatur izin akses. Angka 4=Read, 2=Write, 1=Execute. Tambahkan angkanya kalau mau gabung!"),
            ("Bash Scripting Sederhana", 
             "Capek ngetik manual perintah terminal yang sama tiap pagi? Bash Scripting itu ibarat pakai tape recorder untuk merekam semua perintah lalu memutarnya ulang dengan satu tombol.", 
             "Sangat menghemat waktu untuk otomatisasi, mulai dari backup harian, bersih-bersih sampah, sampai update aplikasi massal.",
             "bash", "#!/bin/bash\n# Simpan ini jadi file backup.sh\necho \"Mulai beres-beres folder...\"\ntar -czvf arsip.tar.gz /data-penting\necho \"Selesai!\"", 
             "- `#!/bin/bash`: Shebang bash.\n- `tar -czvf`: Kompres file/folder.",
             "Selalu gunakan `#!/bin/bash` di baris pertama skrip agar Linux tahu jenis penerjemah yang tepat untuk mengeksekusinya.")
        ],
    }

    if module_title in SPECIFIC_CONTENT:
        lesson_data = SPECIFIC_CONTENT[module_title]
        lessons = []
        for i, (title, analogi, pentingnya, lang, code, penjelasan, summary) in enumerate(lesson_data):
            content = f"""# {title}

💡 **Analogi Sederhana**
{analogi}

🚀 **Kenapa Ini Penting?**
{pentingnya}

💻 **Contoh Nyata & Kode Sederhana**
```{lang}
{code}
```

🔍 **Penjelasan Baris per Baris**
{penjelasan}

📌 **Rangkuman Kilat**
- {summary}
"""
            lessons.append({
                "slug": f"{role_slug}-lesson-{level_num}-{i+1}",
                "title": title,
                "summary": analogi[:100] + "...",
                "content": content,
                "duration": f"{15 + (i * 5)} menit",
                "order_index": i + 1,
                "xp_reward": 50 if i < 3 else 100,
                "is_project": i == 3,
            })
        return lessons

    # Fallback Generic Content
    lesson_titles = [
        f"Konsep Mendasar: {module_title}",
        f"Komponen Utama {module_title}",
        f"Praktik Langsung {module_title}",
        f"Misi Akhir: {module_title}"
    ]
    lang, snippet = get_code_snippet(role_slug)
    
    contents = [
        f"""# Konsep Mendasar: {module_title}

💡 **Analogi Sederhana**
Mempelajari {module_title} itu ibarat belajar naik sepeda. Awalnya terasa kagok dan butuh roda bantuan, tapi saat kamu paham cara menjaga keseimbangan (konsep dasar), semuanya akan mengalir secara otomatis.

🚀 **Kenapa Ini Penting?**
Sebagai seorang **{role_name}**, {module_title} adalah roda penggerak utama. Industri teknologi selalu menggunakan fondasi ini untuk memecahkan persoalan dunia nyata. Memahami dasarnya akan mencegahmu dari kebingungan tingkat lanjut!

💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Contoh perkenalan singkat dengan sistem
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Baris kode di atas menginisialisasi atau menjalankan perintah mendasar dari ekosistem yang digunakan.
- Ini adalah titik masuk utama agar sistem mulai bekerja sesuai instruksi.

📌 **Rangkuman Kilat**
- Pahami keseimbangan intinya sebelum mencoba memodifikasi. Selalu merujuk pada dokumentasi resmi sebagai 'buku panduan manual' mu!
""",
        f"""# Komponen Utama {module_title}

💡 **Analogi Sederhana**
Pernah membongkar jam tangan? Di dalamnya ada banyak gir kecil yang saling berkaitan. Komponen di dalam {module_title} berfungsi sama: pecahan fungsi-fungsi kecil yang bekerja selaras menggerakkan satu sistem utuh.

🚀 **Kenapa Ini Penting?**
Jika satu gir rusak, jam akan mati. Jika kamu mencampur-adukkan kode tanpa membaginya ke komponen kecil (Separation of Concerns), kode aplikasi akan ruwet layaknya benang kusut yang susah diperbaiki orang lain.

💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Bagian ini adalah salah satu 'gir kecil' dalam arsitektur
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Setiap blok atau variabel yang didefinisikan mewakili satu komponen logis mandiri.
- Semua saling memanggil dan mengolah data dari hulu ke hilir.

📌 **Rangkuman Kilat**
- Pecah sistem besar jadi potongan-potongan terkecil yang bisa berdiri sendiri. Jangan tumpuk logika dan tampilan di satu tempat!
""",
        f"""# Praktik Langsung {module_title}

💡 **Analogi Sederhana**
Kamu nggak akan pernah bisa berenang kalau cuma baca teori dari buku. Kamu harus nyemplung ke air! Sama halnya, praktik coding (*hands-on*) diperlukan agar jari-jarimu memiliki *muscle memory*.

🚀 **Kenapa Ini Penting?**
Error dan typo adalah guru terbaik. Menerapkan teori secara lokal di komputermu akan memancing error yang bikin kamu mikir, mencari solusi (Googling), dan jadi developer sejati.

💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Ketik ulang kode ini di komputermu, dan lihat hasilnya!
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Menguji fungsi eksekusi secara langsung untuk memastikan logika berjalan tanpa hambatan.
- Jika terjadi error, baris tersebut akan memberikan pesan penunjuk spesifik.

📌 **Rangkuman Kilat**
- Lakukan *commit* kecil tiap kali kamu berhasil menambah satu fitur kecil, biar kalau aplikasi rusak, kamu gampang memutar waktu mundur (Ctrl+Z level dewa).
""",
        f"""# Misi Akhir: {module_title}

💡 **Analogi Sederhana**
Ini adalah simulasi ujian SIM mobilmu. Kita gabungkan gas, rem, kopling, dan setir menjadi satu manuver halus. Klien akan memintamu menyelesaikan studi kasus ini dengan rapi.

🚀 **Kenapa Ini Penting?**
Keahlian menyatukan komponen-komponen terpisah menjadi satu solusi (aplikasi jadi) yang tahan banting, tidak lemot, dan aman adalah skill mahal yang selalu dicari pewawancara teknis (*Technical Interview*).

💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Penggabungan arsitektur solusi tahap akhir
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Baris ini menghubungkan beberapa komponen yang sebelumnya telah dipelajari secara terpisah.
- Menghasilkan output atau fungsionalitas yang siap dipakai pengguna.

📌 **Rangkuman Kilat**
- Gunakan pendekatan paling simpel lebih dulu (jangan terlalu over-thinking/over-engineering). Baru evaluasi dan poles kode (Refactoring) ketika solusi kasarnya sudah jalan!
"""
    ]

    lessons = []
    for i in range(4):
        lessons.append({
            "slug": f"{role_slug}-lesson-{level_num}-{i+1}",
            "title": lesson_titles[i],
            "summary": "Membahas konsep dan perumpamaan sehari-hari dari materi ini.",
            "content": contents[i],
            "duration": f"{15 + (i * 5)} menit",
            "order_index": i + 1,
            "xp_reward": 50 if i < 3 else 100,
            "is_project": i == 3,
        })
    return lessons

def generate_dummy_levels(role_name: str, role_slug: str):
    """Generate 4 levels for a given role slug, using specific curricula if available, otherwise generic."""

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
        "full-stack-developer": [
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
        "cross-platform-developer": [
            ("Dart Programming", "Modul 1: Bahasa di balik Flutter."),
            ("Flutter UI Basics", "Modul 2: Widget dan layout dasar."),
            ("State Management", "Modul 3: Mengelola state aplikasi (Provider/Riverpod)."),
            ("Firebase Mobile", "Modul 4: Integrasi backend Firebase.")
        ],
        "network-engineer": [
            ("Network Fundamentals", "Modul 1: Dasar-dasar jaringan komputer."),
            ("Routing & Switching", "Modul 2: Konfigurasi perangkat jaringan."),
            ("Network Security Basics", "Modul 3: Keamanan jaringan dasar."),
            ("Network Troubleshooting", "Modul 4: Analisis dan penyelesaian masalah jaringan.")
        ],
        "data-scientist": [
            ("Python for Data", "Modul 1: Pemrograman Python untuk data."),
            ("Data Wrangling", "Modul 2: Pembersihan dan manipulasi data."),
            ("Data Visualization", "Modul 3: Membuat visualisasi data yang informatif."),
            ("Machine Learning Basics", "Modul 4: Pengantar machine learning.")
        ],
        "machine-learning-engineer": [
            ("ML Fundamentals", "Modul 1: Konsep dasar machine learning."),
            ("Supervised Learning", "Modul 2: Algoritma pembelajaran dengan pengawasan."),
            ("Deep Learning Basics", "Modul 3: Pengantar jaringan saraf tiruan."),
            ("Model Deployment", "Modul 4: Menyebarkan model ke production.")
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
            "accent_color": "blue-500",
            "mini_project": f"Proyek Mini {level_num}: {title}",
            "tags": [role_name, "Dasar", f"Modul {level_num}"],
            "lessons": generate_rich_lessons(role_name, role_slug, level_num, title),
        })

    return levels
