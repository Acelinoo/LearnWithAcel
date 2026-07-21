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
        "Bisa bikin halaman HTML pertama dari nol",
        "Bisa pake tag heading, paragraf, link, dan gambar",
        "Bisa baca dan nulis tag HTML yang punya makna",
    ],
    tldr=(
        "HTML itu kerangka halaman web. Tiap tag punya makna sendiri — judul, "
        "paragraf, link, gambar. Browser baca tag-nya, terus nampilin jadi "
        "halaman."
    ),
    pembuka=dedent(
        """\
        Coba bayangin kamu lagi mau bikin rumah. Sebelum dicat, sebelum dikasih furniture, kamu harus pasang dindingnya dulu, pintunya, jendelanya, atapnya.

        HTML itu kerangka rumahnya. Dia yang nentuin "ini judul, ini paragraf, ini gambar".

        Tiap halaman web yang pernah kamu buka — Google, YouTube, TikTok — kerangkanya pake HTML. Beneran semua.
        """
    ),
    penjelasan=dedent(
        """\
        ### HTML itu sebenernya apa

        HTML kepanjangannya **HyperText Markup Language**. Kata "markup" artinya "menandai".

        Jadi HTML itu cara kita nandain isi halaman: ini judul, ini paragraf, ini link.

        Tanda yang dipake namanya **tag**. Tag selalu berpasangan: tag pembuka sama tag penutup. Misal `<p>...</p>` artinya "mulai paragraf di sini, selesai paragraf di sini".

        Beberapa tag gak butuh penutup karena gak punya isi, contohnya `<img>` (gambar) sama `<br>` (baris baru).

        ### Anatomi dokumen HTML

        Tiap file HTML punya kerangka standar. Kayak denah dasar rumah:

        - `<!DOCTYPE html>` — ngasih tau browser ini HTML versi modern
        - `<html>` — pembungkus semua isi halaman
        - `<head>` — info yang **gak keliatan user**, kayak judul tab dan link CSS
        - `<body>` — semua yang **keliatan user**

        ### Tag yang sering dipake

        - `<h1>` sampe `<h6>` — judul, dari paling gede ke paling kecil
        - `<p>` — paragraf
        - `<a>` — link, misal `<a href="https://example.com">Klik aku</a>`
        - `<img>` — gambar, misal `<img src="foto.jpg" alt="Foto saya">`
        - `<div>` — pembungkus block, ngambil baris penuh
        - `<span>` — pembungkus inline, ngikutin alur teks

        ### Atribut

        Atribut itu info tambahan di dalem tag. `src` nentuin sumber gambar. `alt` itu teks pengganti kalau gambar gagal muncul. `href` alamat tujuan buat link.

        Atribut `alt` itu wajib di `<img>`. Selain buat fallback kalau gambar gak load, teks ini juga bantu orang yang gak bisa lihat gambar (pake aplikasi pembaca layar) buat ngerti isi gambarnya.

        ### Tag yang punya makna khusus

        Daripada bungkus semua pake `<div>`, mendingan pilih tag yang sesuai isinya. Ada `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.

        Kenapa ini penting? Dua alasan:

        - Mesin pencari kayak Google jadi lebih ngerti bagian mana judul, mana navigasi, mana isi utama. Itu ngebantu halaman kamu muncul di hasil pencarian.
        - Aplikasi pembaca layar (yang dipake orang yang susah lihat) bisa lompat antar bagian dengan rapi.

        Banyak yang awal-awal mikir tag-tag ini ribet. Padahal cuma ngegantiin `<div>` dengan nama yang lebih jelas.
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
        "Bikin satu file `index.html` isinya nama kamu di `<h1>`, satu foto "
        "(boleh placeholder dari `https://placehold.co/200x200`), dan tiga "
        "hal yang kamu suka dalam list `<ul>` + `<li>`. Buka file di browser "
        "dengan klik dua kali."
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
            "sama satu atribut yang wajib ada di tag gambar."
        ),
        "answer_explanation": dedent(
            """\
            1. `<title>` belum ditutup. Harusnya `</title>`, bukan `<title>` lagi.
            2. `</h1` kurang `>` di akhir tag penutup.
            3. `<img>` wajib punya atribut `alt` biar gambarnya punya teks pengganti.
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
            "Tag `<head>` fungsinya buat apa?",
            [
                "Nampilin konten utama halaman",
                "Nyimpen info tentang halaman yang gak keliatan user",
                "Bikin heading paling gede",
                "Ngatur warna background",
            ],
            "B",
            "`<head>` isinya metadata kayak title, link CSS, sama script. Isinya gak ditampilin langsung ke user.",
        ),
        q(
            "Tag mana yang paling tepat buat judul utama halaman?",
            ["`<title>`", "`<header>`", "`<h1>`", "`<bold>`"],
            "C",
            "`<h1>` itu heading level 1, dipake buat judul paling penting di halaman. `<title>` cuma muncul di tab browser, bukan di halaman.",
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
            "`<strong>` bikin teks di dalemnya jadi tebel dan punya makna penekanan.",
        ),
        q(
            "Atribut apa yang WAJIB ada di tag `<img>`?",
            [
                "`src` sama `width`",
                "`src` sama `alt`",
                "`href` sama `src`",
                "`class` sama `id`",
            ],
            "B",
            "`src` nentuin lokasi gambar, `alt` ngasih teks pengganti kalau gambar gak muncul, dan dipake aplikasi pembaca layar buat jelasin gambar.",
        ),
        q(
            "Apa bedanya `<div>` sama `<span>`?",
            [
                "Gak ada bedanya",
                "`<div>` buat teks, `<span>` buat gambar",
                "`<div>` itu block element, `<span>` itu inline element",
                "`<span>` lebih modern dari `<div>`",
            ],
            "C",
            "Block element kayak `<div>` ngambil lebar penuh dan masuk baris baru. Inline element kayak `<span>` ngikutin alur teks tanpa pindah baris.",
        ),
    ],
    common_mistakes=[
        "Lupa nutup tag, terutama `<title>` sama `<a>`. Browser bisa salah nampilin sisa halaman.",
        "Nulis `<img>` tanpa `alt`. Kalau gambarnya gak load, gak ada teks pengganti, dan orang yang pake pembaca layar gak tau isi gambar.",
        "Pake `<br>` kebanyakan buat bikin jarak. Itu kerjaan CSS, bukan HTML.",
    ],
    checkpoint=[
        "Bisa bikin file HTML dari nol tanpa contekan",
        "Paham bedanya `<head>` sama `<body>`",
        "Bisa pasang heading, paragraf, link, dan gambar dengan atribut yang bener",
        "Tau kapan pake `<section>` vs `<div>`",
    ],
    xp_reward=50,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — CSS Fundamental
# ─────────────────────────────────────────────────────────────────────────────

LESSON_CSS = make_lesson(
    title="CSS Dasar — Bikin Halaman Jadi Rapi",
    slug="css-fundamental",
    order_index=2,
    read_time="10 menit",
    summary="Selector, box model, sama cara bikin tampilan modern.",
    tools=["Browser modern", "VS Code", "DevTools (F12)"],
    outcomes=[
        "Bisa nyambungin file CSS ke HTML",
        "Bisa milih elemen pake selector dasar",
        "Bisa ngatur jarak pake box model (margin, padding, border)",
        "Bisa pake CSS variable biar warna konsisten",
    ],
    tldr=(
        "CSS itu cat sama dekorasinya HTML. Kamu pilih elemen pake selector, "
        "terus kasih property + value. Inget box model: content, padding, "
        "border, margin."
    ),
    pembuka=dedent(
        """\
        Kalau HTML itu kerangka rumah, CSS itu cat, lampu, sama dekorasinya.

        Sama CSS kamu ngatur warna, ukuran, jarak, font — semua hal yang bikin website kamu enak diliat.

        CSS yang sama bisa dipake banyak halaman sekaligus. Sekali ubah, semuanya ikut berubah.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga cara pake CSS

        Ada tiga cara, tapi yang dipake di project nyata cuma satu.

        - **Inline style** — langsung di tag HTML. Cepet, tapi berantakan kalau banyak.
        - **Internal style** — di dalem `<style>` di `<head>`. Cocok buat halaman tunggal.
        - **External stylesheet** — file `.css` terpisah, di-link dari HTML. Ini yang paling sering dipake.

        Aturan praktisnya: buat project nyata, selalu pake external. Misahin struktur (HTML) sama tampilan (CSS) bikin kode lebih rapi.

        ### Anatomi aturan CSS

        Satu aturan CSS terdiri dari tiga bagian: selector, property, value. Selector nunjuk elemen mana yang mau di-style. Property itu nama hal yang mau diubah. Value itu nilainya.

        Tanda `:` misahin property sama value. Tanda `;` nutup tiap baris.

        ### Selector

        - `h1` — milih semua tag h1
        - `.judul` — milih semua elemen dengan `class="judul"`
        - `#hero` — milih elemen dengan `id="hero"` (id harus unik di satu halaman)
        - `nav a` — milih semua link di dalem nav
        - `button:hover` — aktif pas mouse di atas tombol

        ### Box Model — anggep aja kardus

        Tiap elemen HTML itu kayak kardus. Isinya = content. Bantalan dalemnya = padding. Dinding kardusnya = border. Jarak ke kardus lain = margin.

        Property yang sering dipake: `color`, `background`, `font-size`, `font-family`, `width`, `height`, `padding`, `margin`, `border`, `border-radius`, `text-align`.

        ### Units

        - `px` — ukuran tetep. Cocok buat border tipis.
        - `%` — persentase dari elemen pembungkus.
        - `rem` — kelipatan dari font root (default 16px). **Direkomendasiin** buat ukuran font sama spacing gede.
        - `em` — kelipatan dari font elemen pembungkus.

        ### CSS Variables

        Mau warna utama dipake di banyak tempat? Bikin sekali, panggil banyak. Definisiin pake `--nama` di dalem `:root`, panggil pake `var(--nama)`.

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
        "Bikin file `style.css` terus sambungin ke `index.html` dari lesson "
        "sebelumnya pake `<link rel=\"stylesheet\">`. Ubah background jadi "
        "gelap (`#0D0D0D`), warna teks putih, padding `body` 32px, dan kasih "
        "warna aksen biru (`#4EBAEC`) ke nama kamu."
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
            "Property sama value dipisahin pake titik dua. Tiap baris diakhirin "
            "titik koma. Cek baris yang keliatan 'polos'."
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
            "Cara paling direkomendasiin buat pake CSS di project nyata?",
            [
                "Inline style di tiap tag",
                "Internal style di dalem `<style>` di `<head>`",
                "External stylesheet (.css terpisah) yang di-link",
                "Gak pake CSS sama sekali",
            ],
            "C",
            "External stylesheet misahin tampilan dari struktur, gampang di-maintain, dan bisa dipake ulang di banyak halaman.",
        ),
        q(
            "Apa yang dipilih sama selector `.judul`?",
            [
                "Semua tag dengan id `judul`",
                "Semua elemen dengan class `judul`",
                "Tag `<judul>`",
                "Error karena syntax salah",
            ],
            "B",
            "Tanda `.` di depan nama berarti class selector. Buat id, pake `#`.",
        ),
        q(
            "Di Box Model, fungsi `padding` apa?",
            [
                "Jarak antar elemen",
                "Garis tepi elemen",
                "Bantalan di dalem elemen, antara isi sama border",
                "Lebar maksimal elemen",
            ],
            "C",
            "`padding` itu jarak antara isi sama border. `margin` itu jarak ke elemen di luarnya.",
        ),
        q(
            "Mana unit yang paling direkomendasiin buat ukuran font biar scalable?",
            ["`px`", "`rem`", "`pt`", "`cm`"],
            "B",
            "`rem` ngikutin ukuran font root, jadi kalau user ngegedein teks di browser, semua ikut nyesuaiin. `px` itu fixed.",
        ),
        q(
            "Apa fungsi `var(--primary)` di CSS?",
            [
                "Bikin variable baru bernama `primary`",
                "Manggil nilai dari custom property `--primary` yang udah didefinisiin",
                "Namain warna baru",
                "Error syntax",
            ],
            "B",
            "`--primary: ...` mendefinisiin variable. `var(--primary)` cara manggilnya.",
        ),
    ],
    common_mistakes=[
        "Lupa `;` di akhir baris CSS. Aturan setelahnya jadi gak jalan.",
        "Nyampurin ID sama class tanpa alasan. Default pake class, ID buat hal yang bener-bener unik.",
        "Spacing pake `<br>` atau spasi, bukan `margin`/`padding`.",
    ],
    checkpoint=[
        "Bisa link external stylesheet ke HTML",
        "Tau bedanya margin sama padding",
        "Bisa pake CSS variable buat warna utama",
        "Bisa baca dan nulis selector class, id, dan kombinasi",
    ],
    xp_reward=70,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Flexbox & Grid Modern
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FLEX_GRID = make_lesson(
    title="Flexbox & Grid — Layout Modern",
    slug="flexbox-grid-modern",
    order_index=3,
    read_time="12 menit",
    summary="Layout modern: Flexbox satu arah, Grid dua arah.",
    tools=["Browser modern", "VS Code", "DevTools layout panel"],
    outcomes=[
        "Bisa bikin navbar pake Flexbox",
        "Bisa centering elemen di tengah halaman",
        "Bisa bikin gallery responsive pake Grid",
        "Bisa milih Flexbox vs Grid buat kasus tertentu",
    ],
    tldr=(
        "Flexbox buat layout satu arah (rak panjang). Grid buat layout dua "
        "arah (papan catur). `gap` buat jaga jarak. `justify-content` sama "
        "`align-items` buat posisi."
    ),
    pembuka=dedent(
        """\
        Dulu ngatur tata letak website itu nyiksa banget. Orang pake `<table>`, terus pake `float`, semua berantakan.

        Sekarang ada dua senjata utama: Flexbox sama Grid. Dua-duanya bagian dari CSS modern.

        Flexbox kayak ngatur barang di satu rak panjang. Grid kayak ngatur barang di papan catur.
        """
    ),
    penjelasan=dedent(
        """\
        ### Flexbox

        Buat pake Flexbox, kasih `display: flex` ke elemen pembungkus. Anak-anaknya otomatis tersusun horizontal.

        Property utamanya:

        - `flex-direction` — arah: `row` (kiri ke kanan, default) atau `column` (atas ke bawah)
        - `justify-content` — posisi sepanjang arah utama. Pilihan populer: `flex-start`, `center`, `space-between`, `space-around`
        - `align-items` — posisi tegak lurus arah utama. Pilihan populer: `flex-start`, `center`, `stretch`
        - `gap` — jarak antar item, lebih bersih daripada margin
        - `flex-wrap: wrap` — bikin item turun baris kalau gak muat

        Centering yang dulu butuh tiga jam, sekarang tiga baris doang: `display: flex`, `justify-content: center`, `align-items: center`.

        ### CSS Grid

        Buat pake Grid, kasih `display: grid` plus `grid-template-columns`.

        - `repeat(3, 1fr)` artinya tiga kolom sama lebar
        - `1fr` artinya "satu pecahan dari ruang yang tersedia"
        - `gap` sama kayak di Flexbox

        Buat grid yang otomatis nyesuaiin layar, pake `repeat(auto-fit, minmax(240px, 1fr))`. Hasilnya: tiap card minimal lebar 240px, sisanya dibagi rata. Layar lebar = banyak kolom, layar sempit = sedikit. Gak butuh media query.

        Kalau ada satu card yang harus lebih lebar, pake `grid-column: span 2` di card itu.

        ### Kapan pake apa

        Pake Flexbox buat navbar, deretan tombol, list horizontal, centering, dan layout satu arah.

        Pake Grid buat gallery, dashboard, dan layout dua dimensi (sidebar + konten + footer).

        Sering dikombinasiin: Grid buat layout gede, Flexbox di dalem tiap card buat ngatur isinya.
        """
    ),
    contoh_code_md=dedent(
        """\
        Navbar pake Flexbox:

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

        Gallery responsive pake Grid:

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
        "Bikin satu section isinya tiga card sejajar pake Flexbox. Tiap card "
        "punya judul sama deskripsi singkat. Tambahin `gap: 16px` antar card "
        "sama `align-items: stretch` biar tinggi card sama walau isinya beda."
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
            "Buat Flexbox, ada dua nama property yang salah dipasangkan. Buat "
            "Grid, satu property kurang huruf 's' di akhir."
        ),
        "answer_explanation": dedent(
            """\
            1. `justify-items` itu valid di Grid, bukan Flexbox. Buat Flexbox pake `justify-content`.
            2. `align-content` itu valid di Flexbox tapi buat multi-line. Buat single line pake `align-items`.
            3. `grid-template-column` salah ketik. Yang bener `grid-template-columns` (plural).
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
            "Property apa yang nentuin jarak antar item di Flexbox sama Grid modern?",
            ["`margin`", "`space`", "`gap`", "`padding`"],
            "C",
            "`gap` itu cara modern buat ngatur jarak antar item, lebih bersih daripada `margin` di tiap anak.",
        ),
        q(
            "Apa output `justify-content: space-between` di flex container yang isinya 3 item?",
            [
                "Item pertama sama terakhir nempel ke pinggir, item kedua di tengah dengan jarak rata",
                "Semua item rapat ke kiri",
                "Semua item di tengah, gak ada jarak",
                "Item membentuk grid",
            ],
            "A",
            "`space-between` naro item pertama di paling kiri, terakhir di paling kanan, sisanya jaraknya merata.",
        ),
        q(
            "Mana yang paling cocok pake CSS Grid (bukan Flexbox)?",
            [
                "Navbar dengan logo kiri sama menu kanan",
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
            "`fr` (fraction) berarti pecahan dari sisa ruang. `1fr 2fr` berarti kolom pertama dapet 1/3, kolom kedua 2/3.",
        ),
        q(
            "Apa fungsi `repeat(auto-fit, minmax(240px, 1fr))`?",
            [
                "Bikin tepat 3 kolom selalu",
                "Otomatis bikin kolom sebanyak mungkin dengan minimal lebar 240px, sisanya dibagi rata",
                "Error",
                "Bikin baris, bukan kolom",
            ],
            "B",
            "Pola ini buat grid responsive: layar lebar = banyak kolom, layar sempit = sedikit. Tanpa media query.",
        ),
    ],
    common_mistakes=[
        "Ketuker `justify-content` sama `justify-items`. Yang pertama buat Flexbox, yang kedua buat Grid.",
        "Pake Flexbox buat gallery dua dimensi. Ribet hasilnya. Pake Grid.",
        "Lupa `gap`. Akhirnya kasih margin di tiap anak yang berakibat ada margin di pinggir yang gak diinginkan.",
    ],
    checkpoint=[
        "Bisa bikin navbar dengan logo kiri sama menu kanan pake Flexbox",
        "Bisa centering satu elemen di tengah halaman",
        "Bisa bikin gallery card responsive pake Grid",
        "Tau kapan pilih Flexbox vs Grid",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_LANDING = make_lesson(
    title="Mini Project — Personal Landing Page",
    slug="mini-project-personal-landing-page",
    order_index=4,
    read_time="60 menit",
    summary="Bikin halaman pertamamu dan deploy ke internet.",
    tools=["VS Code", "GitHub", "Vercel atau Netlify"],
    outcomes=[
        "Bisa bangun halaman tunggal end-to-end",
        "Bisa pake HTML semantik sama CSS modern di project nyata",
        "Bisa deploy ke hosting gratis dan punya URL publik",
    ],
    tldr=(
        "Bangun halaman perkenalan diri pake HTML + CSS murni. Pake Flexbox "
        "buat navbar, Grid buat skill section, dan deploy gratis ke Vercel."
    ),
    pembuka=dedent(
        """\
        Saatnya bikin sesuatu yang nyata. Selesai project ini, kamu punya halaman pertama yang layak masuk portfolio.

        Ini bukan latihan biasa. Ini bakal jadi bukti kalau kamu bisa pake HTML + CSS dari nol sampe live di internet.
        """
    ),
    penjelasan=dedent(
        """\
        ### Yang kamu bangun

        Halaman tunggal (single-page) yang ngenalin diri kamu ke dunia.

        Tech stack: HTML5 semantic + CSS3 dengan Flexbox dan/atau Grid. Tanpa framework. Fokus ke yang udah dipelajari.

        ### Section minimal

        - **Hero** — nama gede, tagline kuat satu kalimat, foto profil
        - **Tentang Saya** — dua sampe tiga kalimat, gaya santai
        - **Skills atau Hobi** — minimal empat item, ditata dalam grid (bukan list biasa)
        - **Kontak** — email atau social media sebagai link yang bisa diklik

        ### Tips biar hasilnya bagus

        Mulai dari mock-up kasar di kertas atau Figma. Tau mau ke mana sebelum nulis kode itu ngehemat banyak waktu.

        Pake `gap` buat jarak antar item, bukan `margin` random di tiap anak. Hasilnya lebih bersih.

        Pilih satu warna utama, satu warna teks, satu warna muted. Itu udah cukup buat halaman pertama.

        Buka di mode HP via DevTools (F12 → Toggle device toolbar). Pastiin gak ada teks yang keluar layar.

        ### Cara deploy ke Vercel

        Bikin akun di vercel.com (gratis). Bikin repo GitHub, push file project kamu. Klik **Add New Project** di Vercel, pilih repo. Klik Deploy. Selesai dalam tiga puluh detik. Kamu dapet URL `nama-project.vercel.app`.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sketsa kerangka buat mulai. Boleh kamu modif sesuai keinginan.

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
        "Selesain proyek di atas sampe live di Vercel. Salin URL hasilnya "
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
        "hint": "Cek dua baris yang property sama value-nya gak dipisah dengan bener.",
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
            "Buat hero section dengan satu judul gede sama satu tagline, layout-nya cocok pake apa?",
            [
                "Grid 4 kolom",
                "Flexbox dengan `flex-direction: column` sama `align-items: center`",
                "Tabel HTML",
                "Gak perlu layout, biar default",
            ],
            "B",
            "Hero biasanya susunan vertikal yang di-center. Flexbox dengan column + center cocok dan ringkas.",
        ),
        q(
            "Mana praktik yang paling baik buat warna di project ini?",
            [
                "Hardcode warna di tiap selector",
                "Pake CSS variable di `:root` terus panggil pake `var()`",
                "Pake inline style biar cepet",
                "Random tiap section",
            ],
            "B",
            "CSS variable bikin ganti tema cuma di satu tempat dan jaga konsistensi.",
        ),
        q(
            "Apa langkah deploy yang BENER ke Vercel?",
            [
                "Upload file ZIP ke email Vercel",
                "Push ke GitHub, terus konekin repo ke Vercel dan klik Deploy",
                "Salin file ke server sendiri",
                "Gak bisa deploy HTML statis di Vercel",
            ],
            "B",
            "Vercel deploy dari Git repo. Push ke GitHub terus import repo di Vercel.",
        ),
        q(
            "Mana yang GAK perlu buat landing page sederhana ini?",
            [
                "Tag `<meta viewport>` buat responsive",
                "Tag `<title>` buat tab browser",
                "Database PostgreSQL",
                "Tag `<link rel=\"stylesheet\">` buat CSS",
            ],
            "C",
            "Halaman statis HTML/CSS gak butuh database. Itu buat app dinamis.",
        ),
        q(
            "Habis deploy, gimana cara cek halaman tampil bener di HP?",
            [
                "Beli HP baru",
                "Buka URL di browser HP, atau pake DevTools → Toggle device toolbar",
                "Gak perlu cek, default udah responsive",
                "Print halaman terus dilipet",
            ],
            "B",
            "DevTools punya simulator perangkat. Buka URL deploy di HP juga oke. Default gak otomatis responsive — kamu yang bikin responsive.",
        ),
    ],
    common_mistakes=[
        "Foto kegedean tanpa `max-width`. Akhirnya halaman scroll horizontal di HP.",
        "Lupa `<meta viewport>`. Mobile rendering jadi kayak desktop kecil.",
        "Warna kebanyakan. Tetep di tiga sampe empat warna utama.",
    ],
    checkpoint=[
        "Halaman live di internet dengan URL publik",
        "Tampil rapi di desktop dan HP",
        "Pake HTML semantik sama CSS variable",
        "Repo GitHub punya README minimal",
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
    subtitle="Dasar yang harus kamu kuasain dulu",
    description=(
        "Pahami struktur HTML semantik dan styling pake CSS modern. Belajar "
        "layout dengan Flexbox dan Grid dari nol, terus tutup dengan personal "
        "landing page yang live di internet."
    ),
    duration="~1 minggu",
    difficulty="Pemula",
    accent_color="from-violet-500/30 to-fuchsia-500/10",
    mini_project="Personal Landing Page",
    tags=["HTML5", "CSS3", "Flexbox", "Grid", "Responsive"],
    lessons=[LESSON_HTML, LESSON_CSS, LESSON_FLEX_GRID, PROJECT_LANDING],
)
