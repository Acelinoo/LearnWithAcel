import re

file_path = r"c:\Marchelino Kurniawan\Project-2026\LearnWIthAcel\LearnWithAcel\backend\scripts\content\dummy_content.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add line-by-line explanation to HTML
content = content.replace(
    '''             "HTML adalah kerangka utama web. Ingat selalu buka dan tutup tag (seperti `<h1>` dan `</h1>`)."),''',
    '''             "- `<!DOCTYPE html>`: Dokumen HTML5.\\n- `<html>`: Pembungkus utama.\\n- `<head>`: Info meta/judul.\\n- `<body>`: Tubuh konten.",\n             "HTML adalah kerangka utama web. Ingat selalu buka dan tutup tag (seperti `<h1>` dan `</h1>`)."),'''
)

content = content.replace(
    '''             "Gunakan tag yang bermakna seperti `<header>`, `<article>`, dan `<footer>` alih-alih cuma pakai `<div>`."),''',
    '''             "- `<article>`: Konten artikel mandiri.\\n- `<header>`: Judul dari artikel.\\n- `<p>`: Paragraf teks.\\n- `<footer>`: Catatan kaki.",\n             "Gunakan tag yang bermakna seperti `<header>`, `<article>`, dan `<footer>` alih-alih cuma pakai `<div>`."),'''
)

content = content.replace(
    '''             "CSS mengubah warna, letak, dan gaya elemen HTML. Setiap elemen adalah kotak (Box Model) yang punya margin, border, dan padding."),''',
    '''             "- `.kamar-tidur`: Memilih elemen class 'kamar-tidur'.\\n- `background-color`: Mengubah warna latar.\\n- `padding`: Jarak ke dalam.\\n- `margin`: Jarak ke luar.",\n             "CSS mengubah warna, letak, dan gaya elemen HTML. Setiap elemen adalah kotak (Box Model) yang punya margin, border, dan padding."),'''
)

content = content.replace(
    '''             "Gunakan `display: flex;` pada kontainer untuk menata isinya secara otomatis, baik ke samping maupun ke bawah.")''',
    '''             "- `display: flex;`: Mengaktifkan mode Flexbox.\\n- `justify-content`: Mengatur spasi horizontal.\\n- `align-items`: Menyelaraskan konten di tengah vertikal.",\n             "Gunakan `display: flex;` pada kontainer untuk menata isinya secara otomatis, baik ke samping maupun ke bawah.")'''
)

# JS
content = content.replace(
    '''             "Gunakan `const` untuk data yang tetap (seperti tanggal lahir) dan `let` untuk data yang bisa berubah (seperti umur)."),''',
    '''             "- `const`: Variabel permanen (konstanta).\\n- `let`: Variabel yang isinya bisa diubah nanti.",\n             "Gunakan `const` untuk data yang tetap (seperti tanggal lahir) dan `let` untuk data yang bisa berubah (seperti umur)."),'''
)

content = content.replace(
    '''             "Kita bisa menangkap elemen HTML menggunakan `document.getElementById` atau `querySelector`, lalu memberikannya aksi."),''',
    '''             "- `getElementById`: Mengambil elemen berdasarkan ID.\\n- `addEventListener`: Menunggu aksi (seperti klik).\\n- `alert`: Memunculkan pesan di layar.",\n             "Kita bisa menangkap elemen HTML menggunakan `document.getElementById` atau `querySelector`, lalu memberikannya aksi."),'''
)

content = content.replace(
    '''             "Kata kunci `async/await` membuat kode yang berjalan secara asinkron terlihat rapi dan mudah dibaca (seperti kode sinkron)."),''',
    '''             "- `async`: Menandai fungsi ini asinkron.\\n- `await fetch()`: Mengambil data dari URL.\\n- `await json()`: Mengubah respons menjadi objek JavaScript.",\n             "Kata kunci `async/await` membuat kode yang berjalan secara asinkron terlihat rapi dan mudah dibaca (seperti kode sinkron)."),'''
)

content = content.replace(
    '''             "Pecah masalah besar menjadi fungsi-fungsi kecil yang mudah dipahami. Misalnya fungsi untuk tambah, hapus, dan tampilkan.")''',
    '''             "- `[]`: Membuat array (daftar) kosong.\\n- `push(baru)`: Memasukkan item baru ke daftar.\\n- `tampilkanKeLayar()`: Memanggil fungsi lain.",\n             "Pecah masalah besar menjadi fungsi-fungsi kecil yang mudah dipahami. Misalnya fungsi untuk tambah, hapus, dan tampilkan.")'''
)

# React
content = content.replace(
    '''             "Komponen memisahkan desain UI menjadi potongan independen. Props adalah cara mengirim pesan (data) ke komponen tersebut."),''',
    '''             "- `function TombolMerah`: Mendefinisikan komponen.\\n- `props.teks`: Mengambil data dari luar.\\n- `<TombolMerah ... />`: Memanggil dan menampilkan komponen.",\n             "Komponen memisahkan desain UI menjadi potongan independen. Props adalah cara mengirim pesan (data) ke komponen tersebut."),'''
)

content = content.replace(
    '''             "Gunakan hook `useState` untuk menyimpan data di komponen. Saat data (state) berubah, UI otomatis diperbarui (re-render)."),''',
    '''             "- `useState(0)`: Menginisialisasi state dengan angka 0.\\n- `skor`: Variabel pembaca nilai.\\n- `setSkor`: Fungsi untuk mengubah nilai.",\n             "Gunakan hook `useState` untuk menyimpan data di komponen. Saat data (state) berubah, UI otomatis diperbarui (re-render)."),'''
)

content = content.replace(
    '''             "File-based routing di Next.js mempercepat pengembangan web. Gunakan kurung siku `[id].jsx` untuk halaman yang isinya dinamis."),''',
    '''             "- `export default`: Mengekspor komponen untuk digunakan sistem.\\n- `app/tentang/page.jsx`: Path file menjadi rute '/tentang'.",\n             "File-based routing di Next.js mempercepat pengembangan web. Gunakan kurung siku `[id].jsx` untuk halaman yang isinya dinamis."),'''
)

content = content.replace(
    '''             "Dalam proyek besar, pisahkan dengan jelas komponen yang bertugas mengambil data (Logic) dan yang bertugas menampilkan data (UI).")''',
    '''             "- `<LayoutGedung>`: Komponen pembungkus.\\n- `<SidebarNavigasi />`: Navigasi samping.\\n- `<KontenUtama />`: Isi aplikasi.",\n             "Dalam proyek besar, pisahkan dengan jelas komponen yang bertugas mengambil data (Logic) dan yang bertugas menampilkan data (UI).")'''
)

# HTTP
content = content.replace(
    '''             "Request adalah permintaan data ke server. Response adalah jawaban dari server (berhasil atau gagal)."),''',
    '''             "- `GET`: Metode meminta data.\\n- `HTTP/1.1`: Versi protokol HTTP.\\n- `200 OK`: Kode sukses.",\n             "Request adalah permintaan data ke server. Response adalah jawaban dari server (berhasil atau gagal)."),'''
)

content = content.replace(
    '''             "Gunakan GET untuk membaca data, POST untuk menambah data baru, PUT/PATCH untuk mengedit, dan DELETE untuk menghapus."),''',
    '''             "- `fetch`: Melakukan request.\\n- `method: 'POST'`: Mode kirim data.\\n- `JSON.stringify`: Mengubah objek jadi string.",\n             "Gunakan GET untuk membaca data, POST untuk menambah data baru, PUT/PATCH untuk mengedit, dan DELETE untuk menghapus."),'''
)

content = content.replace(
    '''             "Kelompok 2xx berarti Sukses, 4xx berarti Klien (pengguna) salah, dan 5xx berarti Server (backend) yang bermasalah."),''',
    '''             "- `404`: Kode error untuk Not Found.\\n- `pesan_error`: Pesan yang bisa dibaca manusia.",\n             "Kelompok 2xx berarti Sukses, 4xx berarti Klien (pengguna) salah, dan 5xx berarti Server (backend) yang bermasalah."),'''
)

content = content.replace(
    '''             "Gunakan kata benda (Noun) dan jauhi kata kerja dalam merancang Endpoint. Metode HTTP-nya (GET/POST) sudah menjadi kata kerjanya!")''',
    '''             "- `GET /artikel`: Baik (Ambil semua).\\n- `POST /bikin...`: Buruk (Tidak RESTful).",\n             "Gunakan kata benda (Noun) dan jauhi kata kerja dalam merancang Endpoint. Metode HTTP-nya (GET/POST) sudah menjadi kata kerjanya!")'''
)

# SQL
content = content.replace(
    '''             "Tabel menyimpan kategori objek (misal tabel Pengguna, tabel Transaksi). 'Primary Key' adalah nomor KTP unik setiap baris data."),''',
    '''             "- `SERIAL PRIMARY KEY`: ID berurut otomatis.\\n- `VARCHAR(50)`: Teks panjang maksimal 50.\\n- `INT`: Tipe data angka.",\n             "Tabel menyimpan kategori objek (misal tabel Pengguna, tabel Transaksi). 'Primary Key' adalah nomor KTP unik setiap baris data."),'''
)

content = content.replace(
    '''             "Selalu perhatikan dan waspada saat pakai UPDATE dan DELETE! Kalau lupa menambahkan klausa 'WHERE', semua data di database bisa ikut terhapus."),''',
    '''             "- `INSERT INTO`: Menambah data.\\n- `VALUES`: Nilai kolomnya.\\n- `SELECT *`: Ambil semua kolom.\\n- `WHERE`: Filter data.",\n             "Selalu perhatikan dan waspada saat pakai UPDATE dan DELETE! Kalau lupa menambahkan klausa 'WHERE', semua data di database bisa ikut terhapus."),'''
)

content = content.replace(
    '''             "Gunakan 'Foreign Key' untuk merujuk tabel lain. INNER JOIN menggabungkan data yang sama-sama ada di kedua tabel."),''',
    '''             "- `JOIN`: Menggabungkan tabel.\\n- `ON`: Aturan/syarat gabung (ID sama).",\n             "Gunakan 'Foreign Key' untuk merujuk tabel lain. INNER JOIN menggabungkan data yang sama-sama ada di kedua tabel."),'''
)

content = content.replace(
    '''             "Konsep 'Normalisasi' memastikan tidak ada data yang mubazir. Desainlah tabel yang kecil dan spesifik lalu gabungkan saat perlu ditarik laporannya.")''',
    '''             "- `produk_id INT`: Foreign key merujuk ke tabel lain.",\n             "Konsep 'Normalisasi' memastikan tidak ada data yang mubazir. Desainlah tabel yang kecil dan spesifik lalu gabungkan saat perlu ditarik laporannya.")'''
)

# Auth
content = content.replace(
    '''             "Selalu ingat: Autentikasi = Buktikan Identitasmu. Otorisasi = Apa wewenangmu?"),''',
    '''             "- `user.isLogin`: Cek autentikasi.\\n- `user.role`: Cek otorisasi.",\n             "Selalu ingat: Autentikasi = Buktikan Identitasmu. Otorisasi = Apa wewenangmu?"),'''
)

content = content.replace(
    '''             "Gunakan pustaka seperti `bcrypt` untuk mengacak (hash) password. Jangan pakai metode kuno seperti MD5."),''',
    '''             "- `bcrypt.hash`: Mengenkripsi teks.\\n- `10`: Salting rounds (kekuatan enkripsi).",\n             "Gunakan pustaka seperti `bcrypt` untuk mengacak (hash) password. Jangan pakai metode kuno seperti MD5."),'''
)

content = content.replace(
    '''             "JWT ditaruh di header request. Jangan pernah menyimpan password mentah di dalam payload tiket gelang JWT!"),''',
    '''             "- `jwt.sign`: Membuat token.\\n- `{ idUser: 8 }`: Data yang disimpan di token.\\n- `expiresIn`: Batas waktu kadaluarsa.",\n             "JWT ditaruh di header request. Jangan pernah menyimpan password mentah di dalam payload tiket gelang JWT!"),'''
)

content = content.replace(
    '''             "Selain hash password, selalu batasi jumlah percobaan login menggunakan teknik Rate Limiting (batas kecepatan hitungan API).")''',
    '''             "- `rateLimiter`: Membatasi jumlah request.\\n- `limit`: Menerapkan batasan pada endpoint tertentu.",\n             "Selain hash password, selalu batasi jumlah percobaan login menggunakan teknik Rate Limiting (batas kecepatan hitungan API).")'''
)

# Linux
content = content.replace(
    '''             "Biasakan pakai tombol TAB di keyboard saat ngetik di terminal untuk memunculkan otomatis sisa katanya (Autocomplete)."),''',
    '''             "- `pwd`: Cetak lokasi saat ini.\\n- `ls`: List isi folder.\\n- `cd`: Ganti folder aktif.",\n             "Biasakan pakai tombol TAB di keyboard saat ngetik di terminal untuk memunculkan otomatis sisa katanya (Autocomplete)."),'''
)

content = content.replace(
    '''             "Hati-hati dengan perintah `rm -rf`, ibarat bawa bom penghancur. Kalau ngetik salah sasaran, file penting lenyap tanpa ampun!"),''',
    '''             "- `mkdir`: Membuat folder.\\n- `cp`: Kopi file.\\n- `rm -rf`: Hapus folder paksa.",\n             "Hati-hati dengan perintah `rm -rf`, ibarat bawa bom penghancur. Kalau ngetik salah sasaran, file penting lenyap tanpa ampun!"),'''
)

content = content.replace(
    '''             "Perintah `chmod` mengatur izin akses. Angka 4=Read, 2=Write, 1=Execute. Tambahkan angkanya kalau mau gabung!"),''',
    '''             "- `sudo su`: Masuk ke mode admin.\\n- `chmod 777`: Buka semua hak akses (Bahaya).\\n- `chmod 755`: Hak akses normal.",\n             "Perintah `chmod` mengatur izin akses. Angka 4=Read, 2=Write, 1=Execute. Tambahkan angkanya kalau mau gabung!"),'''
)

content = content.replace(
    '''             "Selalu gunakan `#!/bin/bash` di baris pertama skrip agar Linux tahu jenis penerjemah yang tepat untuk mengeksekusinya.")''',
    '''             "- `#!/bin/bash`: Shebang bash.\\n- `tar -czvf`: Kompres file/folder.",\n             "Selalu gunakan `#!/bin/bash` di baris pertama skrip agar Linux tahu jenis penerjemah yang tepat untuk mengeksekusinya.")'''
)


# Now update the unpacking loop
content = content.replace(
    "        for i, (title, analogi, pentingnya, lang, code, summary) in enumerate(lesson_data):",
    "        for i, (title, analogi, pentingnya, lang, code, penjelasan, summary) in enumerate(lesson_data):"
)

old_format = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
{code}
```

📌 **Rangkuman Kilat**"""

new_format = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
{code}
```

🔍 **Penjelasan Baris per Baris**
{penjelasan}

📌 **Rangkuman Kilat**"""

content = content.replace(old_format, new_format)

# Update fallback content
fallback_old_format = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Contoh perkenalan singkat dengan sistem
{snippet}
```

📌 **Rangkuman Kilat**"""

fallback_new_format = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Contoh perkenalan singkat dengan sistem
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Baris kode di atas menginisialisasi atau menjalankan perintah mendasar dari ekosistem yang digunakan.
- Ini adalah titik masuk utama agar sistem mulai bekerja sesuai instruksi.

📌 **Rangkuman Kilat**"""

content = content.replace(fallback_old_format, fallback_new_format)

fallback_old_format2 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Bagian ini adalah salah satu 'gir kecil' dalam arsitektur
{snippet}
```

📌 **Rangkuman Kilat**"""

fallback_new_format2 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Bagian ini adalah salah satu 'gir kecil' dalam arsitektur
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Setiap blok atau variabel yang didefinisikan mewakili satu komponen logis mandiri.
- Semua saling memanggil dan mengolah data dari hulu ke hilir.

📌 **Rangkuman Kilat**"""
content = content.replace(fallback_old_format2, fallback_new_format2)

fallback_old_format3 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Ketik ulang kode ini di komputermu, dan lihat hasilnya!
{snippet}
```

📌 **Rangkuman Kilat**"""

fallback_new_format3 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Ketik ulang kode ini di komputermu, dan lihat hasilnya!
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Menguji fungsi eksekusi secara langsung untuk memastikan logika berjalan tanpa hambatan.
- Jika terjadi error, baris tersebut akan memberikan pesan penunjuk spesifik.

📌 **Rangkuman Kilat**"""
content = content.replace(fallback_old_format3, fallback_new_format3)


fallback_old_format4 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Penggabungan arsitektur solusi tahap akhir
{snippet}
```

📌 **Rangkuman Kilat**"""

fallback_new_format4 = """💻 **Contoh Nyata & Kode Sederhana**
```{lang}
// Penggabungan arsitektur solusi tahap akhir
{snippet}
```

🔍 **Penjelasan Baris per Baris**
- Baris ini menghubungkan beberapa komponen yang sebelumnya telah dipelajari secara terpisah.
- Menghasilkan output atau fungsionalitas yang siap dipakai pengguna.

📌 **Rangkuman Kilat**"""
content = content.replace(fallback_old_format4, fallback_new_format4)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully!")
