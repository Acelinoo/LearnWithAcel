"""
Frontend / Level 1 — HTML & CSS Dasar.

Lessons:
  1. mengenal-html
  2. css-fundamental
  3. flexbox-grid-modern
  4. mini-project-personal-landing-page  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Mengenal HTML
# ─────────────────────────────────────────────────────────────────────────────

LESSON_HTML = make_lesson(
    title="Mengenal HTML",
    slug="mengenal-html",
    order_index=1,
    read_time="8 menit",
    summary="Struktur dasar halaman web dan tag yang sering dipakai.",
    tools=["Browser modern (Chrome/Firefox/Edge)", "VS Code"],
    outcomes=[
        "Membuat halaman HTML pertama dari nol",
        "Memakai tag heading, paragraf, link, dan gambar",
        "Membaca dan menulis tag HTML semantik",
    ],
    tldr=(
        "HTML adalah kerangka halaman web. Setiap tag punya makna: judul, "
        "paragraf, link, gambar, atau pembungkus. Browser membaca tag dan "
        "menampilkannya jadi halaman."
    ),
    pembuka=dedent(
        """\
        Bayangkan kamu mau bangun rumah. Sebelum dicat atau dikasih furnitur, kamu butuh dulu dinding, pintu, jendela, dan atap.

        HTML itu adalah kerangka rumahmu. Dia yang menentukan ada heading di sini, paragraf di sini, gambar di sini.

        Setiap halaman web yang pernah kamu buka — Google, YouTube, TikTok — kerangkanya pakai HTML.
        """
    ),
    penjelasan=dedent(
        """\
        HTML kepanjangan dari **HyperText Markup Language**. Kata "markup" artinya "menandai". Jadi HTML adalah cara kita menandai isi halaman: ini judul, ini paragraf, ini link.

        Tanda yang dipakai disebut **tag**. Tag selalu berpasangan: tag pembuka dan tag penutup. Misal `<p>...</p>` artinya "mulai paragraf di sini, selesai paragraf di sini".

        Beberapa tag tidak butuh penutup karena tidak punya isi, contohnya `<img>` (gambar) dan `<br>` (baris baru).

        ### Struktur dasar dokumen HTML

        Setiap file HTML punya kerangka standar. Anggap ini "denah dasar rumah":

        - `<!DOCTYPE html>` memberitahu browser ini HTML versi modern.
        - `<html>` membungkus semua isi halaman.
        - `<head>` berisi info yang **tidak terlihat user**, seperti judul tab dan link CSS.
        - `<body>` berisi semua yang **terlihat user**.

        ### Tag yang sering dipakai

        - `<h1>` sampai `<h6>` untuk judul, dari paling besar ke paling kecil.
        - `<p>` untuk paragraf.
        - `<a>` untuk link, misal `<a href="https://example.com">Klik aku</a>`.
        - `<img>` untuk gambar, misal `<img src="foto.jpg" alt="Foto saya">`.
        - `<div>` pembungkus block, ambil baris penuh.
        - `<span>` pembungkus inline, mengikuti alur teks.

        ### Atribut

        Atribut adalah info tambahan di dalam tag. `src` menentukan sumber gambar. `alt` adalah teks pengganti kalau gambar gagal muncul. `href` adalah alamat tujuan untuk link.

        Atribut `alt` itu wajib di `<img>`. Kalau gambar gagal muncul, teks `alt` yang dipakai sebagai pengganti. Teks ini juga membantu orang yang tidak bisa melihat gambar memahami isi gambarnya.

        ### Tag yang punya makna khusus

        Daripada bungkus semua pakai `<div>`, pilih tag yang sesuai isinya. `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.

        Kenapa ini penting? Mesin pencari seperti Google jadi lebih paham bagian mana judul, mana navigasi, mana isi utama — itu membantu halamanmu muncul di hasil pencarian. Aplikasi pembaca layar (yang dipakai orang yang sulit melihat) juga bisa lompat antar bagian dengan rapi.
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman profil sederhana:

        ```html
        <!DOCTYPE html>
        <html lang="id">
          <head>
            <title>Profil Saya</title>
          </head>
          <body>
            <header>
              <h1>Halo, saya Acel</h1>
              <p>Belajar web dev dari nol.</p>
            </header>

            <main>
              <section>
                <h2>Tentang saya</h2>
                <p>Suka kopi, kode, dan film.</p>
              </section>

              <section>
                <h2>Kontak</h2>
                <a href="mailto:saya@email.com">Email saya</a>
              </section>
            </main>
          </body>
        </html>
        ```
        """
    ),
    practice=(
        "Buat satu file `index.html` berisi nama kamu di `<h1>`, satu foto "
        "(boleh placeholder dari `https://placehold.co/200x200`), dan tiga hal "
        "yang kamu suka dalam list `<ul>` + `<li>`. Buka file di browser dengan "
        "klik dua kali."
    ),
    fix_error={
        "language": "html",
        "broken_code": dedent(
            """\
            <!DOCTYPE html>
            <html>
              <head>
                <title>Halaman Saya<title>
              </head>
              <body>
                <h1>Halo, nama saya Budi!</h1
                <p>Saya suka belajar coding.</p>
                <img src="foto.jpg">
              </body>
            </html>
            """
        ),
        "hint": (
            "Ada tiga kesalahan. Cek penutup tag judul, penutup tag heading, "
            "dan satu atribut yang wajib ada di tag gambar."
        ),
        "answer_explanation": dedent(
            """\
            1. `<title>` belum ditutup. Harusnya `</title>`, bukan `<title>` lagi.
            2. `</h1` kurang `>` di akhir tag penutup.
            3. `<img>` wajib punya atribut `alt` supaya gambar punya teks pengganti.
            """
        ),
        "fixed_code": dedent(
            """\
            <!DOCTYPE html>
            <html lang="id">
              <head>
                <title>Halaman Saya</title>
              </head>
              <body>
                <h1>Halo, nama saya Budi!</h1>
                <p>Saya suka belajar coding.</p>
                <img src="foto.jpg" alt="Foto Budi">
              </body>
            </html>
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi tag `<head>` dalam HTML?",
            [
                "Menampilkan konten utama halaman",
                "Menyimpan informasi tentang halaman yang tidak terlihat user",
                "Membuat heading paling besar",
                "Mengatur warna background",
            ],
            "B",
            "`<head>` berisi metadata seperti title, link CSS, dan script. Isinya tidak ditampilkan langsung ke user.",
        ),
        q(
            "Tag mana yang paling tepat untuk judul utama halaman?",
            ["`<title>`", "`<header>`", "`<h1>`", "`<bold>`"],
            "C",
            "`<h1>` adalah heading level 1, dipakai untuk judul paling penting di halaman. `<title>` cuma muncul di tab browser, bukan di halaman.",
        ),
        q(
            "Apa output dari kode `<p>Halo <strong>Dunia</strong>!</p>`?",
            [
                "Halo Dunia! (semua huruf sama)",
                "Halo **Dunia**! (kata Dunia dicetak tebal)",
                "Error",
                "Halo (Dunia) !",
            ],
            "B",
            "`<strong>` membuat teks di dalamnya jadi tebal dan punya makna penekanan.",
        ),
        q(
            "Atribut apa yang WAJIB ada di tag `<img>`?",
            [
                "`src` dan `width`",
                "`src` dan `alt`",
                "`href` dan `src`",
                "`class` dan `id`",
            ],
            "B",
            "`src` menentukan lokasi gambar, `alt` memberikan teks pengganti kalau gambar tidak muncul, dan dipakai aplikasi pembaca layar untuk menjelaskan gambar.",
        ),
        q(
            "Apa perbedaan `<div>` dan `<span>`?",
            [
                "Tidak ada perbedaan",
                "`<div>` untuk teks, `<span>` untuk gambar",
                "`<div>` adalah block element, `<span>` adalah inline element",
                "`<span>` lebih modern dari `<div>`",
            ],
            "C",
            "Block element seperti `<div>` ambil lebar penuh dan masuk baris baru. Inline element seperti `<span>` mengikuti alur teks tanpa pindah baris.",
        ),
    ],
    common_mistakes=[
        "Lupa menutup tag, terutama `<title>` dan `<a>`. Browser bisa salah nampilin sisa halaman.",
        "Menulis `<img>` tanpa `alt`. Gambar yang gagal muncul tidak punya teks pengganti, dan orang yang pakai pembaca layar tidak tahu isi gambar.",
        "Pakai `<br>` berlebihan untuk bikin jarak. Itu tugas CSS, bukan HTML.",
    ],
    checkpoint=[
        "Bisa membuat file HTML dari nol tanpa contekan kerangka.",
        "Paham bedanya `<head>` dan `<body>`.",
        "Bisa pasang heading, paragraf, link, dan gambar dengan atribut yang benar.",
        "Tahu kapan pakai `<section>` vs `<div>`.",
    ],
    xp_reward=50,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — CSS Fundamental
# ─────────────────────────────────────────────────────────────────────────────

LESSON_CSS = make_lesson(
    title="CSS Fundamental",
    slug="css-fundamental",
    order_index=2,
    read_time="10 menit",
    summary="Selector, box model, dan cara menata tampilan modern.",
    tools=["Browser modern", "VS Code", "DevTools (F12)"],
    outcomes=[
        "Menghubungkan file CSS ke HTML",
        "Memilih elemen dengan selector dasar",
        "Mengatur ruang dengan box model (margin, padding, border)",
        "Memakai CSS variable untuk warna konsisten",
    ],
    tldr=(
        "CSS itu cat dan dekorasinya HTML. Kamu pilih elemen pakai selector, "
        "lalu kasih property + value. Ingat box model: content, padding, border, "
        "margin."
    ),
    pembuka=dedent(
        """\
        Kalau HTML adalah kerangka rumah, CSS itu cat, lampu, dan dekorasinya.

        Dengan CSS kamu atur warna, ukuran, jarak, font — semua hal yang bikin website kamu enak dilihat.

        CSS yang sama bisa dipakai banyak halaman sekaligus, jadi sekali ubah, semuanya ikut berubah.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga cara pakai CSS

        Ada tiga cara, tapi yang dipakai di project nyata cuma satu.

        - **Inline style** langsung di tag HTML. Cepat, tapi berantakan kalau banyak.
        - **Internal style** di dalam `<style>` di `<head>`. Cocok untuk halaman tunggal.
        - **External stylesheet** file `.css` terpisah, di-link dari HTML. Ini yang paling sering dipakai.

        Aturan praktis: untuk project nyata, selalu pakai external. Memisahkan struktur (HTML) dan tampilan (CSS) bikin kode lebih rapi.

        ### Anatomi aturan CSS

        Satu aturan CSS terdiri dari tiga bagian: selector, property, value. Selector menunjuk elemen mana yang mau di-style. Property nama hal yang mau diubah. Value nilainya.

        Tanda `:` memisahkan property dan value. Tanda `;` menutup tiap baris.

        ### Selector

        - `h1` memilih semua tag h1.
        - `.judul` memilih semua elemen dengan `class="judul"`.
        - `#hero` memilih elemen dengan `id="hero"` (id harus unik di satu halaman).
        - `nav a` memilih semua link di dalam nav.
        - `button:hover` aktif saat mouse di atas tombol.

        ### CSS Box Model

        Bayangkan setiap elemen HTML adalah sebuah kardus. Isinya = content. Bantalan dalam = padding. Dinding kardus = border. Jarak ke kardus lain = margin.

        Property yang sering dipakai: `color`, `background`, `font-size`, `font-family`, `width`, `height`, `padding`, `margin`, `border`, `border-radius`, `text-align`.

        ### Units

        - `px` ukuran tetap. Cocok untuk border tipis.
        - `%` persentase dari elemen pembungkus.
        - `rem` kelipatan dari font root (default 16px). **Direkomendasikan** untuk ukuran font dan spacing besar.
        - `em` kelipatan dari font elemen pembungkus.

        ### CSS Variables

        Mau warna utama dipakai di banyak tempat? Bikin sekali, panggil banyak. Definisikan dengan `--nama` di dalam `:root`, panggil dengan `var(--nama)`.

        Kalau mau ganti tema, kamu cuma ubah satu tempat.
        """
    ),
    contoh_code_md=dedent(
        """\
        File `index.html`:

        ```html
        <link rel="stylesheet" href="style.css">

        <header class="hero">
          <h1>Halo, saya Acel</h1>
          <p class="tagline">Belajar web dev dari nol.</p>
        </header>
        ```

        File `style.css`:

        ```css
        :root {
          --bg: #0D0D0D;
          --text: #F5F5F5;
          --accent: #4EBAEC;
        }

        body {
          background: var(--bg);
          color: var(--text);
          font-family: system-ui, sans-serif;
          margin: 0;
          padding: 32px;
        }

        .hero h1 {
          font-size: 2.5rem;
          color: var(--accent);
        }

        .tagline {
          color: #a1a1aa;
          font-size: 1rem;
        }
        ```
        """
    ),
    practice=(
        "Buat file `style.css` lalu sambungkan ke `index.html` dari lesson "
        "sebelumnya pakai `<link rel=\"stylesheet\">`. Ubah background jadi gelap "
        "(`#0D0D0D`), warna teks putih, padding `body` 32px, dan kasih warna aksen "
        "biru (`#4EBAEC`) ke nama kamu."
    ),
    fix_error={
        "language": "css",
        "broken_code": dedent(
            """\
            body {
              background-color #1a1a1a;
              font-family: Arial, sans-serif
              color: white;
            }

            h1 {
              font-size 24px;
              color: #4EBAEC
            }
            """
        ),
        "hint": (
            "Property dan value dipisahkan oleh titik dua. Tiap baris diakhiri "
            "titik koma. Cek baris yang kelihatan 'polos'."
        ),
        "answer_explanation": dedent(
            """\
            1. `background-color #1a1a1a;` kurang `:` setelah nama property.
            2. `font-family: Arial, sans-serif` kurang `;` di akhir baris.
            3. `font-size 24px;` kurang `:` setelah nama property.
            4. `color: #4EBAEC` kurang `;` di akhir baris.
            """
        ),
        "fixed_code": dedent(
            """\
            body {
              background-color: #1a1a1a;
              font-family: Arial, sans-serif;
              color: white;
            }

            h1 {
              font-size: 24px;
              color: #4EBAEC;
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa cara paling direkomendasikan untuk pakai CSS di project nyata?",
            [
                "Inline style di setiap tag",
                "Internal style di dalam `<style>` di `<head>`",
                "External stylesheet (.css terpisah) yang di-link",
                "Tidak pakai CSS sama sekali",
            ],
            "C",
            "External stylesheet memisahkan tampilan dari struktur, mudah di-maintain, dan bisa dipakai ulang di banyak halaman.",
        ),
        q(
            "Apa yang dipilih oleh selector `.judul`?",
            [
                "Semua tag dengan id `judul`",
                "Semua elemen dengan class `judul`",
                "Tag `<judul>`",
                "Error karena syntax salah",
            ],
            "B",
            "Tanda `.` di depan nama menandakan class selector. Untuk id, pakai `#`.",
        ),
        q(
            "Dalam CSS Box Model, apa fungsi `padding`?",
            [
                "Jarak antar elemen",
                "Garis tepi elemen",
                "Bantalan di dalam elemen, antara isi dan border",
                "Lebar maksimal elemen",
            ],
            "C",
            "`padding` adalah jarak antara isi dan border. `margin` adalah jarak ke elemen di luarnya.",
        ),
        q(
            "Mana unit yang paling direkomendasikan untuk ukuran font supaya scalable?",
            ["`px`", "`rem`", "`pt`", "`cm`"],
            "B",
            "`rem` mengikuti ukuran font root, jadi kalau user perbesar teks di browser, semua ikut menyesuaikan. `px` itu fixed.",
        ),
        q(
            "Apa fungsi `var(--primary)` di CSS?",
            [
                "Membuat variabel baru bernama `primary`",
                "Memanggil nilai dari custom property `--primary` yang sudah didefinisikan",
                "Menamai warna baru",
                "Error syntax",
            ],
            "B",
            "`--primary: ...` mendefinisikan variabel. `var(--primary)` cara memanggilnya.",
        ),
    ],
    common_mistakes=[
        "Lupa `;` di akhir baris CSS. Aturan setelahnya jadi tidak jalan.",
        "Mencampur ID dan class tanpa alasan. Default pakai class, ID untuk hal yang benar-benar unik.",
        "Spacing pakai `<br>` atau spasi, bukan `margin`/`padding`.",
    ],
    checkpoint=[
        "Bisa link external stylesheet ke HTML.",
        "Tahu beda margin dan padding.",
        "Bisa pakai CSS variable untuk warna utama.",
        "Bisa baca dan menulis selector class, id, dan kombinasi.",
    ],
    xp_reward=70,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Flexbox & Grid Modern
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FLEX_GRID = make_lesson(
    title="Flexbox & Grid Modern",
    slug="flexbox-grid-modern",
    order_index=3,
    read_time="12 menit",
    summary="Layout modern dengan Flexbox satu dimensi dan Grid dua dimensi.",
    tools=["Browser modern", "VS Code", "DevTools layout panel"],
    outcomes=[
        "Membuat navbar dengan Flexbox",
        "Centering elemen di tengah halaman",
        "Membuat gallery responsive dengan Grid",
        "Memilih Flexbox vs Grid untuk kasus tertentu",
    ],
    tldr=(
        "Flexbox untuk layout satu arah (rak panjang). Grid untuk layout dua "
        "arah (papan catur). `gap` jaga jarak. `justify-content` dan "
        "`align-items` untuk posisi."
    ),
    pembuka=dedent(
        """\
        Dulu mengatur tata letak website itu menyiksa. Orang pakai `<table>`, lalu pakai `float`, dan semua berantakan.

        Sekarang ada dua senjata utama: Flexbox dan Grid. Keduanya bagian dari CSS modern.

        Flexbox seperti mengatur barang dalam satu rak panjang. Grid seperti mengatur barang di papan catur.
        """
    ),
    penjelasan=dedent(
        """\
        ### Flexbox

        Untuk pakai Flexbox, kasih `display: flex` ke elemen pembungkus. Anak-anaknya otomatis tersusun horizontal.

        Property utama:

        - `flex-direction` arah: `row` (kiri ke kanan, default) atau `column` (atas ke bawah).
        - `justify-content` posisi sepanjang arah utama. Pilihan populer: `flex-start`, `center`, `space-between`, `space-around`.
        - `align-items` posisi tegak lurus arah utama. Pilihan populer: `flex-start`, `center`, `stretch`.
        - `gap` jarak antar item, lebih bersih daripada margin.
        - `flex-wrap: wrap` membuat item turun baris kalau tidak muat.

        Centering yang dulu butuh tiga jam, sekarang tiga baris: `display: flex`, `justify-content: center`, `align-items: center`.

        ### CSS Grid

        Untuk pakai Grid, kasih `display: grid` plus `grid-template-columns`.

        - `repeat(3, 1fr)` artinya tiga kolom sama lebar.
        - `1fr` artinya "satu pecahan dari ruang yang tersedia".
        - `gap` sama seperti di Flexbox.

        Untuk grid yang otomatis menyesuaikan layar, pakai `repeat(auto-fit, minmax(240px, 1fr))`. Hasilnya: setiap card minimal lebar 240px, sisanya dibagi rata. Layar lebar = banyak kolom, layar sempit = sedikit. Tidak butuh media query.

        Kalau ada satu card yang harus lebih lebar, pakai `grid-column: span 2` di card itu.

        ### Kapan pakai apa

        Pakai Flexbox untuk navbar, deretan tombol, list horizontal, centering, dan layout satu arah.

        Pakai Grid untuk gallery, dashboard, dan layout dua dimensi (sidebar + konten + footer).

        Sering kombinasi keduanya: Grid untuk layout besar, Flexbox di dalam tiap card untuk atur isinya.
        """
    ),
    contoh_code_md=dedent(
        """\
        Navbar dengan Flexbox:

        ```html
        <nav class="navbar">
          <span>Logo</span>
          <div class="menu">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
          </div>
        </nav>
        ```

        ```css
        .navbar {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 16px 32px;
        }

        .menu {
          display: flex;
          gap: 24px;
        }
        ```

        Gallery responsive dengan Grid:

        ```css
        .cards {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
          gap: 20px;
        }
        ```
        """
    ),
    practice=(
        "Buat satu section berisi tiga card sejajar pakai Flexbox. Tiap card "
        "punya judul dan deskripsi singkat. Tambah `gap: 16px` antar card dan "
        "`align-items: stretch` supaya tinggi card sama walau isinya beda."
    ),
    fix_error={
        "language": "css",
        "broken_code": dedent(
            """\
            .container {
              display: flex;
              justify-items: center;
              align-content: center;
            }

            .grid-layout {
              display: grid;
              grid-template-column: repeat(3, 1fr);
              gap: 16px;
            }
            """
        ),
        "hint": (
            "Untuk Flexbox, ada dua nama property yang salah dipasangkan. Untuk "
            "Grid, satu property kurang huruf 's' di akhir."
        ),
        "answer_explanation": dedent(
            """\
            1. `justify-items` valid di Grid, bukan Flexbox. Untuk Flexbox pakai `justify-content`.
            2. `align-content` valid di Flexbox tapi untuk multi-line. Untuk single line pakai `align-items`.
            3. `grid-template-column` salah eja. Yang benar `grid-template-columns` (plural).
            """
        ),
        "fixed_code": dedent(
            """\
            .container {
              display: flex;
              justify-content: center;
              align-items: center;
            }

            .grid-layout {
              display: grid;
              grid-template-columns: repeat(3, 1fr);
              gap: 16px;
            }
            """
        ),
    },
    quiz=[
        q(
            "Property apa yang menentukan jarak antar item di Flexbox dan Grid modern?",
            ["`margin`", "`space`", "`gap`", "`padding`"],
            "C",
            "`gap` adalah cara modern untuk atur jarak antar item, lebih bersih daripada `margin` di tiap anak.",
        ),
        q(
            "Apa output `justify-content: space-between` di flex container yang berisi 3 item?",
            [
                "Item pertama dan terakhir nempel ke pinggir, item kedua di tengah dengan jarak rata",
                "Semua item rapat ke kiri",
                "Semua item di tengah, tidak ada jarak",
                "Item membentuk grid",
            ],
            "A",
            "`space-between` menaruh item pertama di paling kiri, terakhir di paling kanan, sisanya jaraknya merata.",
        ),
        q(
            "Mana yang paling cocok pakai CSS Grid (bukan Flexbox)?",
            [
                "Navbar dengan logo kiri dan menu kanan",
                "Tombol-tombol horizontal di footer",
                "Gallery foto 4 kolom 3 baris",
                "Centering satu kotak di tengah halaman",
            ],
            "C",
            "Gallery butuh layout dua dimensi (baris + kolom). Itu wilayahnya Grid.",
        ),
        q(
            "Apa arti `1fr` di `grid-template-columns: 1fr 2fr`?",
            [
                "Lebar kolom dalam pixel",
                "Pecahan ruang tersedia. Kolom pertama 1 bagian, kolom kedua 2 bagian",
                "Frame per second",
                "Error syntax",
            ],
            "B",
            "`fr` (fraction) berarti pecahan dari sisa ruang. `1fr 2fr` berarti kolom pertama dapat 1/3, kolom kedua 2/3.",
        ),
        q(
            "Apa fungsi `repeat(auto-fit, minmax(240px, 1fr))`?",
            [
                "Bikin tepat 3 kolom selalu",
                "Otomatis bikin sebanyak mungkin kolom dengan minimal lebar 240px, sisanya dibagi rata",
                "Error",
                "Bikin baris, bukan kolom",
            ],
            "B",
            "Pola ini untuk grid responsive: layar lebar = banyak kolom, layar sempit = sedikit. Tanpa media query.",
        ),
    ],
    common_mistakes=[
        "Tertukar `justify-content` dengan `justify-items`. Yang pertama untuk Flexbox, yang kedua untuk Grid.",
        "Pakai Flexbox untuk gallery dua dimensi. Hasilnya repot. Pakai Grid.",
        "Lupa `gap`. Akhirnya kasih margin di setiap anak yang berakibat ada margin di pinggir yang tidak diinginkan.",
    ],
    checkpoint=[
        "Bisa bikin navbar dengan logo kiri dan menu kanan pakai Flexbox.",
        "Bisa centering satu elemen di tengah halaman.",
        "Bisa bikin gallery card responsive dengan Grid.",
        "Tahu kapan pilih Flexbox vs Grid.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_LANDING = make_lesson(
    title="Mini Project — Personal Landing Page",
    slug="mini-project-personal-landing-page",
    order_index=4,
    read_time="60 menit",
    summary="Bangun halaman pertamamu dan deploy ke internet.",
    tools=["VS Code", "GitHub", "Vercel atau Netlify"],
    outcomes=[
        "Membangun halaman tunggal end-to-end",
        "Memakai HTML semantik dan CSS modern di project nyata",
        "Deploy ke hosting gratis dan punya URL publik",
    ],
    tldr=(
        "Bangun halaman perkenalan diri pakai HTML + CSS murni. "
        "Pakai Flexbox untuk navbar, Grid untuk skill section, dan deploy "
        "gratis ke Vercel."
    ),
    pembuka=dedent(
        """\
        Saatnya bikin sesuatu yang nyata. Selesai project ini, kamu punya halaman pertama yang layak masuk portfolio.

        Ini bukan latihan biasa. Ini akan jadi proof bahwa kamu bisa pakai HTML + CSS dari nol sampai live di internet.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa yang kamu bangun

        Sebuah halaman tunggal (single-page) yang memperkenalkan dirimu ke dunia.

        Tech stack: HTML5 semantic + CSS3 dengan Flexbox dan/atau Grid. Tanpa framework. Fokus ke yang sudah dipelajari.

        ### Section minimal

        - **Hero** dengan nama besar, tagline satu kalimat, dan foto profil.
        - **Tentang Saya** dua sampai tiga kalimat, gaya santai.
        - **Skills atau Hobi** minimal empat item, ditata dalam grid (bukan list biasa).
        - **Kontak** dengan email atau social media sebagai link yang bisa diklik.

        ### Tips agar hasil bagus

        Mulai dari mock-up kasar di kertas atau Figma. Tahu mau ke mana sebelum nulis kode menghemat banyak waktu.

        Pakai `gap` untuk jarak antar item, bukan `margin` random di tiap anak. Hasilnya lebih bersih.

        Pilih satu warna utama, satu warna teks, satu warna muted. Itu sudah cukup untuk halaman pertama.

        Buka di mode HP via DevTools (F12 → Toggle device toolbar). Pastikan tidak ada teks yang keluar layar.

        ### Cara deploy ke Vercel

        Buat akun di vercel.com (gratis). Buat repo GitHub, push file project kamu. Klik **Add New Project** di Vercel, pilih repo. Klik Deploy. Selesai dalam tiga puluh detik. Kamu dapat URL `nama-project.vercel.app`.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sketsa kerangka untuk memulai. Boleh kamu modifikasi sesuai keinginan.

        ```html
        <!DOCTYPE html>
        <html lang="id">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Profil — Nama Kamu</title>
            <link rel="stylesheet" href="style.css">
          </head>
          <body>
            <nav class="navbar">
              <span class="brand">Nama Kamu</span>
              <a href="#kontak">Kontak</a>
            </nav>

            <main>
              <section class="hero">
                <h1>Halo, saya Nama Kamu</h1>
                <p>Web developer pemula yang lagi belajar.</p>
              </section>

              <section>
                <h2>Tentang saya</h2>
                <p>Tulis dua tiga kalimat tentang dirimu di sini.</p>
              </section>

              <section>
                <h2>Skills</h2>
                <div class="skills">
                  <div class="card">HTML</div>
                  <div class="card">CSS</div>
                  <div class="card">Flexbox</div>
                  <div class="card">Grid</div>
                </div>
              </section>

              <footer id="kontak">
                <a href="mailto:saya@email.com">saya@email.com</a>
              </footer>
            </main>
          </body>
        </html>
        ```
        """
    ),
    practice=(
        "Selesaikan proyek di atas sampai live di Vercel. Salin URL hasilnya "
        "ke catatan kamu. Itu jadi item pertama portfolio kamu."
    ),
    fix_error={
        "language": "css",
        "broken_code": dedent(
            """\
            .skills {
              display: grid;
              grid-template-columns: repeat(2, 1fr);
              gap 16px;
            }

            .card {
              padding: 16px;
              border 1px solid #333;
              border-radius: 8px;
            }
            """
        ),
        "hint": "Cek dua baris yang property dan value-nya tidak dipisah dengan benar.",
        "answer_explanation": dedent(
            """\
            1. `gap 16px;` kurang `:` setelah `gap`.
            2. `border 1px solid #333;` kurang `:` setelah `border`.
            """
        ),
        "fixed_code": dedent(
            """\
            .skills {
              display: grid;
              grid-template-columns: repeat(2, 1fr);
              gap: 16px;
            }

            .card {
              padding: 16px;
              border: 1px solid #333;
              border-radius: 8px;
            }
            """
        ),
    },
    quiz=[
        q(
            "Untuk hero section dengan satu judul besar dan satu tagline, layout-nya cocok pakai apa?",
            [
                "Grid 4 kolom",
                "Flexbox dengan `flex-direction: column` dan `align-items: center`",
                "Tabel HTML",
                "Tidak perlu layout, biar default",
            ],
            "B",
            "Hero biasanya susunan vertikal yang di-center. Flexbox dengan column + center cocok dan ringkas.",
        ),
        q(
            "Mana praktik yang paling baik untuk warna di project ini?",
            [
                "Hardcode warna di setiap selector",
                "Pakai CSS variable di `:root` lalu panggil dengan `var()`",
                "Pakai inline style supaya cepat",
                "Random tiap section",
            ],
            "B",
            "CSS variable membuat ganti tema cukup di satu tempat dan menjaga konsistensi.",
        ),
        q(
            "Apa langkah deploy yang BENAR ke Vercel?",
            [
                "Upload file ZIP ke email Vercel",
                "Push ke GitHub, lalu hubungkan repo ke Vercel dan klik Deploy",
                "Salin file ke server sendiri",
                "Tidak bisa deploy HTML statis di Vercel",
            ],
            "B",
            "Vercel deploy dari Git repo. Push ke GitHub lalu import repo di Vercel.",
        ),
        q(
            "Mana yang TIDAK perlu untuk landing page sederhana ini?",
            [
                "Tag `<meta viewport>` untuk responsive",
                "Tag `<title>` untuk tab browser",
                "Database PostgreSQL",
                "Tag `<link rel=\"stylesheet\">` untuk CSS",
            ],
            "C",
            "Halaman statis HTML/CSS tidak butuh database. Itu untuk app dinamis.",
        ),
        q(
            "Setelah deploy, bagaimana cara cek halaman tampil benar di HP?",
            [
                "Beli HP baru",
                "Buka URL di browser HP, atau pakai DevTools → Toggle device toolbar",
                "Tidak perlu cek, default sudah responsive",
                "Print halaman lalu lipat",
            ],
            "B",
            "DevTools punya simulator perangkat. Buka URL deploy di HP juga oke. Default tidak otomatis responsive — kamu yang bikin responsive.",
        ),
    ],
    common_mistakes=[
        "Foto terlalu besar tanpa `max-width`. Akhirnya halaman scroll horizontal di HP.",
        "Lupa `<meta viewport>`. Mobile rendering jadi seperti desktop kecil.",
        "Warna terlalu banyak. Tetap di tiga sampai empat warna utama.",
    ],
    checkpoint=[
        "Halaman live di internet dengan URL publik.",
        "Tampil rapi di desktop dan HP.",
        "Pakai HTML semantik dan CSS variable.",
        "Repo GitHub punya README minimal.",
    ],
    xp_reward=200,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=1,
    slug="html-css-dasar",
    title="HTML & CSS Dasar",
    subtitle="Fondasi setiap halaman web",
    description=(
        "Pahami struktur HTML semantik dan styling dengan CSS modern. "
        "Belajar layout dengan Flexbox dan Grid dari nol, lalu tutup dengan "
        "personal landing page yang live di internet."
    ),
    duration="~1 minggu",
    difficulty="Pemula",
    accent_color="from-violet-500/30 to-fuchsia-500/10",
    mini_project="Personal Landing Page",
    tags=["HTML5", "CSS3", "Flexbox", "Grid", "Responsive"],
    lessons=[LESSON_HTML, LESSON_CSS, LESSON_FLEX_GRID, PROJECT_LANDING],
)
