// Article-like content for individual lessons. Kept as simple data so the
// rendering layer can stay purely presentational.
//
// Style notes:
// - Bahasa santai, langsung ke inti. Hindari jargon tanpa penjelasan.
// - Setiap poin penting ditutup dengan kata "contoh:" diikuti code nyata.
// - Setiap lesson punya 3 pertanyaan quiz dalam quiz.questions[].

export const lessonContent = {
  // ============================================================
  // LEVEL 1 — HTML & CSS
  // ============================================================
  "html-css/mengenal-html": {
    title: "Mengenal HTML: Fondasi Halaman Web",
    description:
      "HTML adalah bahasa yang memberi tahu browser bagaimana sebuah halaman disusun. Di pelajaran ini kamu belajar dasar-dasarnya dengan contoh langsung.",
    readTime: "8 menit",
    level: "Level 1 — HTML & CSS",
    hero: {
      emoji: "🧱",
      caption: "Setiap web hebat dimulai dari struktur yang baik.",
    },
    objectives: [
      "Paham apa itu HTML dan untuk apa",
      "Kenal tag-tag yang paling sering dipakai",
      "Bisa menulis halaman HTML pertamamu sendiri",
    ],
    practice: {
      fileName: "index.html",
      steps: [
        "Buka VS Code. Klik menu File → Open Folder. Di jendela yang muncul, klik kanan di tempat kosong → New folder → beri nama latihan-html, lalu klik Select Folder",
        "Di panel kiri VS Code (Explorer), arahkan kursor ke nama folder → klik ikon lembar (New File) yang muncul di sebelahnya → ketik index.html lalu Enter",
        "Ketik ulang contoh kode di bawah. Jangan copy-paste, supaya jari dan otak sama-sama belajar",
        "Untuk melihat hasilnya: klik kanan file index.html → Open with Live Server. Halaman akan otomatis terbuka di browser. Kalau menu Live Server belum ada, install ekstensinya dulu (lihat tip di bawah)",
      ],
      tip: "Install ekstensi Live Server: di VS Code tekan Ctrl + Shift + X untuk buka Extensions, ketik 'Live Server' (yang dibuat Ritwick Dey), klik Install. Setelah aktif, tiap kamu Save (Ctrl + S) halaman otomatis refresh.",
    },
    sections: [
      {
        heading: "Apa Itu HTML?",
        body: [
          "HTML adalah singkatan dari HyperText Markup Language. Gampangnya: HTML itu kerangka halaman web. Semua teks, gambar, link yang kamu lihat di website dibungkus pakai HTML.",
          "Analogi: HTML itu tulang dan daging rumah. CSS adalah cat dan dekorasinya. JavaScript adalah listrik yang bikin lampu nyala dan pintu bisa buka sendiri.",
        ],
      },
      {
        heading: "Tag: Potongan Kecil Pembentuk Halaman",
        body: [
          "Tag adalah perintah HTML yang ditulis dalam kurung siku. Sebagian besar tag punya pembuka dan penutup.",
        ],
        list: [
          "<h1> sampai <h6>: judul, dari paling besar ke paling kecil. contoh: <h1>Halo</h1>",
          "<p>: paragraf. contoh: <p>Ini kalimatku.</p>",
          "<a>: link ke halaman lain. contoh: <a href='https://google.com'>Ke Google</a>",
          "<img>: gambar, tidak perlu tag penutup. contoh: <img src='foto.jpg' alt='Foto aku'>",
          "<ul> dan <li>: daftar berurutan. contoh: <ul><li>Apel</li><li>Jeruk</li></ul>",
          "<div>: kotak kosong untuk mengelompokkan. contoh: <div>isi kelompok</div>",
        ],
      },
      {
        heading: "Halaman HTML Pertamamu",
        body: [
          "Struktur minimal halaman HTML seperti ini. Ketik ulang di VS Code, jangan copy.",
        ],
        code: `<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <title>Halo Dunia</title>
  </head>
  <body>
    <h1>Halo, aku sedang belajar HTML</h1>
    <p>Ini paragraf pertamaku.</p>
  </body>
</html>`,
        list: [
          "<!DOCTYPE html>: kasih tahu browser ini HTML modern",
          "<head>: info halaman (judul, bahasa, link ke CSS). Tidak muncul di layar",
          "<body>: isi yang benar-benar muncul di layar",
        ],
      },
      {
        heading: "Tips Belajar",
        body: [
          "Jangan hanya baca. Ketik ulang setiap contoh. Lalu sengaja rusak sedikit (hapus tag penutup, ganti huruf) supaya kamu paham apa yang pecah.",
        ],
      },
    ],
    debug: {
      description:
        "Coba buka file kode di bawah. Ada beberapa kesalahan kecil yang bikin halaman rusak. Baca baris demi baris dulu sebelum klik hint.",
      language: "html",
      errorCount: 2,
      brokenCode: `<!DOCTYPE html>
<html lang="id>
  <head>
    <meta charset="UTF-8" />
    <titleHalo Dunia</title>
  </head>
  <body>
    <h1>Halo, aku sedang belajar HTML</h1>
    <p>Ini paragraf pertamaku.</p>
  </body>
</html>`,
      errors: [
        {
          hint: "Cek atribut lang di tag <html>. Ada kutip yang tidak lengkap.",
          fix: "<html lang=\"id> seharusnya <html lang=\"id\">. Kutip penutup pada nilai atribut lang hilang, jadi browser menganggap atribut itu tidak pernah ditutup dan isi file jadi kacau.",
        },
        {
          hint: "Cek tag pembuka <title>. Ada yang kurang di situ.",
          fix: "<titleHalo Dunia</title> seharusnya <title>Halo Dunia</title>. Kurung siku penutup '>' pada tag pembuka <title> hilang, jadi seluruh teks 'Halo Dunia' dianggap bagian dari nama tag, bukan isi.",
        },
      ],
      fixedCode: `<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <title>Halo Dunia</title>
  </head>
  <body>
    <h1>Halo, aku sedang belajar HTML</h1>
    <p>Ini paragraf pertamaku.</p>
  </body>
</html>`,
    },
    quiz: {
      questions: [
        {
          question: "Apa fungsi utama HTML dalam sebuah halaman web?",
          options: [
            { id: "a", text: "Menambahkan logika interaktif" },
            { id: "b", text: "Menentukan struktur dan isi halaman" },
            { id: "c", text: "Mengatur warna dan font" },
            { id: "d", text: "Menghubungkan dengan database" },
          ],
          answer: "b",
          explanation:
            "HTML menyusun struktur dan isi halaman. Warna diatur CSS, logika diatur JavaScript.",
        },
        {
          question: "Tag mana yang cocok dipakai untuk membuat link ke halaman lain?",
          options: [
            { id: "a", text: "<p>" },
            { id: "b", text: "<img>" },
            { id: "c", text: "<a>" },
            { id: "d", text: "<div>" },
          ],
          answer: "c",
          explanation:
            "Tag <a> dengan atribut href dipakai untuk membuat hyperlink.",
        },
        {
          question:
            "Di antara bagian berikut, mana yang isinya tidak muncul langsung di layar?",
          options: [
            { id: "a", text: "<body>" },
            { id: "b", text: "<head>" },
            { id: "c", text: "<h1>" },
            { id: "d", text: "<p>" },
          ],
          answer: "b",
          explanation:
            "<head> berisi informasi halaman seperti title dan link CSS. Isi yang terlihat ditaruh di <body>.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `<!DOCTYPE html>
<html lang="id>
  <head>
    <meta charset="UTF-8" />
    <titleHalo Dunia</title>
  </head>
  <body>
    <h1>Halo, aku sedang belajar HTML</h1>
    <p>Ini paragraf pertamaku.</p>
  </body>
</html>`,
      hints: ["Perhatikan baris 2, ada tanda kutip yang belum ditutup", "Perhatikan baris 5, tag <title> pembukaannya tidak benar"],
      fixedCode: `<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <title>Halo Dunia</title>
  </head>
  <body>
    <h1>Halo, aku sedang belajar HTML</h1>
    <p>Ini paragraf pertamaku.</p>
  </body>
</html>`,
      explanation: "Ada dua error: (1) atribut lang=\"id\" kurang tanda kutip penutup, harusnya lang=\"id\" bukan lang=\"id. (2) tag <title> tidak punya tanda > penutup di pembukanya, harusnya <title> bukan <titleHalo."
    },
    nextLesson: {
      href: "/materi/html-css/css-fundamental",
      title: "CSS Fundamental",
    },
  },

  "html-css/css-fundamental": {
    title: "CSS Fundamental: Menata Tampilan Halaman",
    description:
      "Kalau HTML adalah kerangka, CSS adalah cat dan dekorasinya. Di sini kamu akan belajar cara memilih elemen dan mengubah tampilannya.",
    readTime: "12 menit",
    level: "Level 1 — HTML & CSS",
    hero: {
      emoji: "🎨",
      caption: "CSS bukan tentang menghafal, tapi memahami pola.",
    },
    objectives: [
      "Tahu tiga cara menyisipkan CSS ke HTML",
      "Bisa memilih elemen dengan selector",
      "Paham box model dan cara elemen mengambil ruang",
      "Tahu cara menangani konflik antar aturan CSS",
    ],
    practice: {
      fileName: "styles.css",
      steps: [
        "Pastikan kamu masih di folder latihan-html dari materi sebelumnya",
        "Di panel Explorer VS Code, klik ikon New File di sebelah nama folder → ketik styles.css lalu Enter",
        "Buka index.html, lalu tambahkan baris ini di dalam <head> sebelum </head>: <link rel='stylesheet' href='styles.css'>",
        "Coba contoh kode CSS di bawah. Setelah save (Ctrl + S), halaman di browser otomatis berubah warna",
        "Untuk melihat style apa saja yang aktif di suatu elemen: buka browser, tekan F12 (atau klik kanan di halaman → Inspect). Panel DevTools akan muncul. Pilih tab Elements → klik elemen apapun → panel Styles di sebelah kanan menampilkan semua CSS yang aktif",
      ],
      tip: "Di VS Code, buka file HTML kosong lalu ketik tanda seru '!' lalu tekan Tab. VS Code akan otomatis generate kerangka HTML lengkap (disebut Emmet).",
    },
    sections: [
      {
        heading: "Tiga Cara Menulis CSS",
        body: [
          "CSS bisa ditulis di tiga tempat. Yang paling direkomendasikan adalah cara ketiga (file terpisah) karena HTML dan CSS-nya jadi rapi.",
        ],
        list: [
          "Inline: langsung di atribut style. contoh: <p style=\"color: red\">Halo</p>",
          "Internal: di tag <style> di dalam <head>. contoh: <style>p { color: red; }</style>",
          "External: file .css terpisah, paling rapi. contoh: <link rel='stylesheet' href='styles.css'>",
        ],
      },
      {
        heading: "Selector: Cara Memilih Elemen",
        body: [
          "Sebelum mengubah tampilan elemen, kamu harus bisa memilihnya dulu. Ada tiga selector paling sering dipakai.",
        ],
        list: [
          "Tag selector: menarget semua tag tertentu. contoh: p { color: blue; } akan mewarnai SEMUA paragraf",
          "Class selector: pakai titik (.), dipakai ke class HTML. contoh: .judul { font-size: 32px; }",
          "Id selector: pakai pagar (#), untuk id unik di halaman. contoh: #intro { opacity: 0.8; }",
        ],
        code: `/* styles.css */
body {
  font-family: system-ui, sans-serif;
  background: #0d0d0d;
  color: #f5f5f5;
}

.judul {
  font-size: 32px;
  color: #38bdf8;
}

#intro {
  line-height: 1.6;
}`,
      },
      {
        heading: "Box Model: Setiap Elemen Adalah Kotak",
        body: [
          "Setiap elemen HTML sebenarnya adalah sebuah kotak. Dari dalam ke luar urutannya: content, padding, border, margin. Ingat urutan ini, banyak masalah layout selesai saat kamu paham.",
        ],
        list: [
          "Content: isi kotak (teks atau gambar). contoh: tulisan di dalam <p>",
          "Padding: jarak antara isi dan garis pembatas. contoh: padding: 16px bikin ada nafas 16px di dalam kotak",
          "Border: garis pembatas kotak. contoh: border: 1px solid #262626",
          "Margin: jarak kotak ini dengan kotak di sebelahnya. contoh: margin-bottom: 20px",
        ],
        code: `.card {
  padding: 24px;
  border: 1px solid #262626;
  border-radius: 12px;
  margin-bottom: 16px;
  background: #1c1c1c;
}`,
      },
      {
        heading: "Kalau Ada Aturan yang Bentrok",
        body: [
          "Kadang kamu menulis dua aturan yang menyentuh elemen yang sama. CSS memilih berdasarkan specificity. Urutan dari paling kuat ke paling lemah: inline > id > class > tag.",
          "Kalau style-mu tidak jalan, jangan buru-buru pakai !important. Biasanya ada aturan lain yang lebih spesifik mengalahkannya. Cara cek: tekan F12 di browser (atau klik kanan elemen → Inspect), klik elemen di tab Elements. Di panel Styles sebelah kanan, aturan yang dicoret berarti kalah. Yang tidak dicoret itulah aturan yang menang.",
        ],
      },
      {
        heading: "Unit yang Sering Dipakai",
        list: [
          "px: ukuran tetap dalam pixel. contoh: font-size: 16px",
          "rem: ukuran relatif ke root (1rem biasanya = 16px). contoh: padding: 1.5rem",
          "%: relatif terhadap elemen parent. contoh: width: 50%",
          "vh / vw: relatif terhadap layar. contoh: height: 100vh berarti setinggi layar",
        ],
      },
    ],
    debug: {
      description:
        "Kode CSS di bawah kelihatan rapi, tapi ada beberapa kesalahan kecil yang bikin stylenya tidak nempel ke HTML. Coba cari dulu sebelum lihat hint.",
      language: "css",
      errorCount: 3,
      brokenCode: `body {
  font-family: system-ui, sans-serif
  background: #0d0d0d;
  color: #f5f5f5;
}

judul {
  font-size: 32px;
  color: #38bdf8;
}

.card {
  padding 24px;
  border: 1px solid #262626;
  border-radius: 12px;
}`,
      errors: [
        {
          hint: "Di selector body, baris pertama terasa 'menyambung' ke baris bawahnya. Apa yang biasanya mengakhiri satu aturan CSS?",
          fix: "Setelah 'font-family: system-ui, sans-serif' kurang titik koma (;). Tanpa itu, browser nyambungin aturan ini ke aturan berikutnya dan jadi rusak.",
        },
        {
          hint: "Selector 'judul' kelihatan aneh. Kalau di HTML kamu pakai class='judul', tanda apa yang harus ada di depannya?",
          fix: "'judul { ... }' seharusnya '.judul { ... }'. Class selector wajib diawali titik (.). Tanpa titik, CSS menganggap itu tag HTML bernama 'judul' (yang tidak ada).",
        },
        {
          hint: "Di dalam .card, ada satu baris yang kehilangan tanda yang memisahkan nama property dengan nilainya.",
          fix: "'padding 24px;' seharusnya 'padding: 24px;'. Property dan value di CSS wajib dipisahkan dengan tanda titik dua (:).",
        },
      ],
      fixedCode: `body {
  font-family: system-ui, sans-serif;
  background: #0d0d0d;
  color: #f5f5f5;
}

.judul {
  font-size: 32px;
  color: #38bdf8;
}

.card {
  padding: 24px;
  border: 1px solid #262626;
  border-radius: 12px;
}`,
    },
    quiz: {
      questions: [
        {
          question: "Apa urutan box model dari dalam ke luar?",
          options: [
            { id: "a", text: "margin → border → padding → content" },
            { id: "b", text: "content → margin → padding → border" },
            { id: "c", text: "content → padding → border → margin" },
            { id: "d", text: "padding → content → border → margin" },
          ],
          answer: "c",
          explanation:
            "Dari dalam ke luar: content, padding (ruang dalam), border (pembatas), margin (jarak keluar).",
        },
        {
          question:
            "Selector mana yang paling tepat untuk menarget satu elemen unik dengan id='intro'?",
          options: [
            { id: "a", text: ".intro" },
            { id: "b", text: "#intro" },
            { id: "c", text: "intro" },
            { id: "d", text: "*intro" },
          ],
          answer: "b",
          explanation:
            "Id selector pakai tanda pagar (#). Class selector pakai titik (.), tag selector tanpa prefiks.",
        },
        {
          question: "Kamu ingin memberi jarak kotak dengan kotak di sebelahnya. Pakai apa?",
          options: [
            { id: "a", text: "padding" },
            { id: "b", text: "border" },
            { id: "c", text: "margin" },
            { id: "d", text: "content" },
          ],
          answer: "c",
          explanation:
            "Margin mengatur jarak kotak dengan kotak lain. Padding mengatur ruang di dalam kotak.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `body {
  font-family system-ui, sans-serif;
  background: #0d0d0d
  color: #f5f5f5;
}

.judul {
  font-size: 32px
  color: #38bdf8;
}`,
      hints: ["Setiap property CSS butuh tanda titik dua (:) antara nama dan nilai", "Setiap baris deklarasi CSS harus diakhiri titik koma (;)"],
      fixedCode: `body {
  font-family: system-ui, sans-serif;
  background: #0d0d0d;
  color: #f5f5f5;
}

.judul {
  font-size: 32px;
  color: #38bdf8;
}`,
      explanation: "Tiga error: (1) font-family kurang titik dua (:). (2) background: #0d0d0d kurang titik koma (;) di akhir. (3) font-size: 32px juga kurang titik koma. Di CSS, setiap deklarasi wajib format: property: value;"
    },
    nextLesson: {
      href: "/materi/html-css/flexbox-grid",
      title: "Flexbox & Grid Modern",
    },
  },

  "html-css/flexbox-grid": {
    title: "Flexbox & Grid Modern",
    description:
      "Dua sistem layout paling penting di CSS hari ini. Flexbox untuk satu arah, Grid untuk dua arah. Paham keduanya, kamu bisa bikin hampir semua layout.",
    readTime: "15 menit",
    level: "Level 1 — HTML & CSS",
    hero: {
      emoji: "📐",
      caption: "Layout bukan sihir, hanya soal mengatur ruang.",
    },
    objectives: [
      "Tahu kapan pakai Flexbox dan kapan pakai Grid",
      "Bisa membuat navbar dan card list dengan Flexbox",
      "Bisa membuat grid responsif dengan CSS Grid",
      "Paham rumus ajaib untuk layout responsif tanpa media query",
    ],
    practice: {
      fileName: "layout.html",
      steps: [
        "Di VS Code, buka folder latihan-html. Buat file baru bernama layout.html (klik ikon New File di Explorer, ketik nama, Enter)",
        "Copy struktur di bawah ke file itu, lalu buka pakai Live Server (klik kanan file → Open with Live Server)",
        "Coba ubah-ubah nilainya di VS Code: ganti gap: 20px jadi gap: 40px, ganti justify-content: space-between jadi center. Save, lihat efeknya langsung",
        "Untuk melihat tampilan di ukuran HP: tekan F12 atau klik kanan di halaman → Inspect. Di panel DevTools yang muncul, cari ikon kecil bergambar ponsel & tablet di pojok kiri atas panel (Toggle device toolbar, shortcut Ctrl + Shift + M). Klik itu, pilih ukuran iPhone / Galaxy di atas, lihat layout berubah",
        "Bonus: di tab Elements, cari elemen yang punya display: flex atau display: grid. Akan muncul label kecil 'flex' atau 'grid' di samping. Klik label itu → DevTools menampilkan panduan visual garis-garis flexbox / grid langsung di atas halaman",
      ],
      tip: "Kalau F12 tidak bekerja (biasanya di laptop dengan tombol Fn), coba Ctrl + Shift + I atau klik kanan halaman pilih Inspect. Inspect dan F12 membuka hal yang sama.",
    },
    sections: [
      {
        heading: "Flexbox: Untuk Layout Satu Arah",
        body: [
          "Flexbox bekerja dalam satu sumbu. Horizontal (baris) atau vertikal (kolom). Pas banget untuk navbar, daftar tombol, atau menengahkan isi.",
          "Caranya: parent diberi display: flex, lalu semua anak otomatis jadi flex item yang bisa diatur letaknya.",
        ],
        code: `<nav class="navbar">
  <div class="logo">Acel</div>
  <ul class="menu">
    <li>Home</li>
    <li>Roadmap</li>
    <li>About</li>
  </ul>
</nav>

<style>
  .navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
  }
  .menu {
    display: flex;
    gap: 20px;
    list-style: none;
  }
</style>`,
      },
      {
        heading: "Property Flexbox yang Sering Dipakai",
        list: [
          "flex-direction: arah sumbu. contoh: flex-direction: row (default) atau column",
          "justify-content: posisi di sumbu utama. contoh: justify-content: center untuk di tengah",
          "align-items: posisi di sumbu silang. contoh: align-items: center untuk tengah vertikal",
          "gap: jarak antar item, pengganti margin yang bersih. contoh: gap: 16px",
          "flex-wrap: pindah baris saat ruang kurang. contoh: flex-wrap: wrap",
        ],
      },
      {
        heading: "Grid: Untuk Layout Dua Arah",
        body: [
          "Grid membagi ruang dalam baris dan kolom sekaligus. Pas untuk galeri, kartu-kartu sejajar, atau kerangka halaman. Kamu merancang kisi-kisi dulu, lalu isi selnya.",
        ],
        code: `<section class="cards">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
  <div class="card">Card 4</div>
</section>

<style>
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
  }
  .card {
    padding: 24px;
    background: #1c1c1c;
    border-radius: 12px;
  }
</style>`,
      },
      {
        heading: "Rumus Ajaib Grid Responsif",
        body: [
          "Satu baris: repeat(auto-fit, minmax(240px, 1fr)). Ini bikin grid otomatis menyesuaikan jumlah kolom berdasarkan lebar layar. Tidak perlu media query.",
        ],
        list: [
          "auto-fit: isi ruang kosong dengan kolom sebanyak mungkin",
          "minmax(240px, 1fr): tiap kolom minimal 240px, kalau muat lebih, bagi sama rata",
          "gap: 16px: jarak antar kolom dan baris",
        ],
      },
      {
        heading: "Kapan Pakai yang Mana?",
        list: [
          "Satu arah (deret horizontal atau kolom vertikal): pakai Flexbox. contoh: navbar, toolbar",
          "Dua arah (baris dan kolom bersamaan): pakai Grid. contoh: galeri, dashboard",
          "Kombinasi: Grid untuk kerangka halaman, Flexbox untuk isi di dalam tiap sel",
        ],
      },
    ],
    debug: {
      description:
        "Kode di bawah seharusnya bikin navbar dengan logo di kiri dan menu di kanan, plus grid kartu 3 kolom di bawahnya. Tapi tampilannya rusak. Cari yang salah.",
      language: "css",
      errorCount: 3,
      brokenCode: `.navbar {
  display: flex;
  align-item: center;
  justify-content: space-between;
}

.menu {
  display: flex;
  gap 20px;
  list-style: none;
}

.cards {
  display: grid;
  grid-template-column: repeat(3, 1fr);
  gap: 16px;
}`,
      errors: [
        {
          hint: "Di .navbar, logo dan menu tidak rata vertikal. Coba periksa nama property yang mengatur posisi di sumbu silang.",
          fix: "'align-item: center;' seharusnya 'align-items: center;'. Perhatikan huruf 's' di akhir. Banyak CSS property pakai bentuk jamak karena mengatur banyak item sekaligus.",
        },
        {
          hint: "Di .menu, 'gap' tidak memberi jarak sama sekali. Sesuatu yang penting hilang antara nama property dan nilainya.",
          fix: "'gap 20px;' seharusnya 'gap: 20px;'. Property CSS selalu butuh titik dua (:) untuk memisahkan nama property dengan nilainya.",
        },
        {
          hint: "Di .cards, grid tidak membagi jadi 3 kolom. Periksa nama property untuk mendefinisikan kolom grid.",
          fix: "'grid-template-column' seharusnya 'grid-template-columns' (ada 's'). Sama seperti align-items, ini bentuk jamak karena mengatur banyak kolom.",
        },
      ],
      fixedCode: `.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.menu {
  display: flex;
  gap: 20px;
  list-style: none;
}

.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}`,
    },
    quiz: {
      questions: [
        {
          question:
            "Kamu ingin bikin galeri yang otomatis jadi 1 kolom di HP dan 3 kolom di laptop, tanpa media query. Paling cocok pakai apa?",
          options: [
            { id: "a", text: "Flexbox dengan flex-wrap" },
            { id: "b", text: "Grid dengan repeat(auto-fit, minmax(...))" },
            { id: "c", text: "Float dengan clearfix" },
            { id: "d", text: "Position absolute" },
          ],
          answer: "b",
          explanation:
            "CSS Grid dengan auto-fit dan minmax adalah cara paling singkat untuk galeri responsif tanpa media query.",
        },
        {
          question:
            "Pada Flexbox, property apa yang mengatur posisi item di sumbu utama (misal di tengah horizontal)?",
          options: [
            { id: "a", text: "align-items" },
            { id: "b", text: "justify-content" },
            { id: "c", text: "flex-wrap" },
            { id: "d", text: "flex-direction" },
          ],
          answer: "b",
          explanation:
            "justify-content mengatur posisi di sumbu utama. align-items mengatur sumbu silang.",
        },
        {
          question:
            "Kamu ingin memberi jarak rapi antar item tanpa banyak margin. Property apa yang paling bersih?",
          options: [
            { id: "a", text: "margin-right" },
            { id: "b", text: "padding" },
            { id: "c", text: "gap" },
            { id: "d", text: "space" },
          ],
          answer: "c",
          explanation:
            "gap memberi jarak antar item di Flexbox maupun Grid, lebih bersih daripada mengandalkan margin.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `.cards {
  display: gird;
  grid-template-column: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.navbar {
  display: flex;
  justify-contents: space-between;
  align-item: center;
}`,
      hints: ["Cek ejaan 'gird' dan 'column'", "Cek ejaan 'justify-contents' dan 'align-item'"],
      fixedCode: `.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}`,
      explanation: "Empat typo: (1) gird → grid. (2) grid-template-column → grid-template-columns (pakai s). (3) justify-contents → justify-content (tanpa s). (4) align-item → align-items (pakai s). CSS tidak kasih error merah, tapi property yang salah eja diam-diam diabaikan."
    },
    nextLesson: {
      href: "/materi/javascript/dasar-javascript",
      title: "Dasar JavaScript",
    },
  },

  // ============================================================
  // LEVEL 2 — JAVASCRIPT
  // ============================================================
  "javascript/dasar-javascript": {
    title: "Dasar JavaScript: Variable, Type, dan Logika",
    description:
      "JavaScript adalah bahasa yang bikin halaman web hidup. Di sini kamu belajar cara menyimpan data, mengenali tipenya, dan membuat kode bisa mengambil keputusan.",
    readTime: "14 menit",
    level: "Level 2 — JavaScript",
    hero: {
      emoji: "⚡",
      caption: "Di balik setiap web interaktif ada JavaScript.",
    },
    objectives: [
      "Paham beda const, let, dan var",
      "Kenal tipe data dasar JavaScript",
      "Bisa membandingkan nilai dengan operator",
      "Bisa bikin kode yang mengambil keputusan dengan if",
    ],
    practice: {
      fileName: "app.js",
      steps: [
        "Di VS Code, buat folder baru bernama belajar-js (File → Open Folder → klik kanan → New Folder)",
        "Di panel Explorer, buat dua file: index.html dan app.js (klik ikon New File, ketik nama, Enter)",
        "Isi index.html dengan kerangka HTML (ketik '!' lalu Tab). Tambahkan baris ini di dalam <head>: <script src='app.js' defer></script>",
        "Buka index.html pakai Live Server (klik kanan file → Open with Live Server)",
        "Di browser, tekan F12 atau klik kanan halaman → Inspect. Pilih tab Console di panel yang muncul. Di sinilah hasil console.log akan tampil",
        "Ketik console.log('halo dari app.js') di app.js → Save. Lihat tulisan 'halo dari app.js' muncul di tab Console. Selamat, kamu baru saja menjalankan JavaScript",
      ],
      tip: "Tab Console bukan cuma untuk melihat hasil, tapi juga tempat eksperimen. Ketik 1 + 1 lalu Enter, lalu ketik 'halo'.toUpperCase() lalu Enter. Hasilnya langsung muncul. Ini cara paling cepat menguji ide.",
    },
    sections: [
      {
        heading: "Variable: Wadah Menyimpan Data",
        body: [
          "Variable itu kotak untuk menyimpan nilai. JavaScript punya tiga keyword: const, let, dan var. Aturan sederhana: default pakai const, pakai let kalau nilainya perlu berubah, hindari var.",
        ],
        code: `const nama = "Acel";        // tidak bisa diganti, kalau dipaksa akan error
let umur = 20;              // bisa diganti
umur = 21;                  // valid

console.log(nama, umur);    // "Acel" 21

// Kalau kamu coba:
// nama = "Budi";           // ERROR: Assignment to constant variable`,
      },
      {
        heading: "Tipe Data Dasar",
        body: [
          "JavaScript bisa menyimpan berbagai macam data. Ini yang wajib kamu kenal:",
        ],
        list: [
          "String: teks, ditulis dalam kutip. contoh: 'ini' atau \"ini\"",
          "Number: angka, tidak perlu kutip. contoh: 23, 3.14, -7",
          "Boolean: kondisi benar atau salah. contoh: true, false",
          "null: sengaja dikosongkan. contoh: let hasil = null",
          "undefined: belum diisi. contoh: let x; lalu console.log(x) hasilnya undefined",
          "Array: daftar, ditulis dalam [ ]. contoh: ['apel', 'jeruk', 'mangga']",
          "Object: pasangan key-value, ditulis dalam { }. contoh: { nama: 'Acel', umur: 20 }",
        ],
        code: `const kata = "halo";
const angka = 42;
const aktif = true;
const kosong = null;
let belumDiisi;                                   // undefined
const menu = ["home", "roadmap", "about"];
const user = { nama: "Acel", level: 3 };

console.log(menu[0]);     // "home" (index mulai dari 0)
console.log(user.nama);   // "Acel"`,
      },
      {
        heading: "Operator: Alat untuk Menghitung dan Membandingkan",
        list: [
          "Aritmatika: +, -, *, /, %. contoh: 10 % 3 hasilnya 1 (sisa bagi)",
          "Perbandingan: === (sama persis), !== (tidak sama), >, <, >=, <=",
          "Logika: && (dan), || (atau), ! (kebalikan)",
        ],
        body: [
          "Selalu pakai === bukan ==. Sebab === mengecek nilai DAN tipe datanya. Ini mencegah bug menyebalkan.",
        ],
        code: `const a = 5;
const b = "5";

console.log(a == b);    // true (cuma cek nilai, tidak aman)
console.log(a === b);   // false (cek nilai dan tipe, lebih aman)

console.log(10 > 5 && 20 > 15);   // true (dua-duanya benar)
console.log(10 > 5 || 20 < 15);   // true (salah satu benar)`,
      },
      {
        heading: "Mengambil Keputusan dengan if",
        body: [
          "Kode yang bisa berkata 'kalau begini, lakukan itu' ditulis pakai if dan else.",
        ],
        code: `const nilai = 78;

if (nilai >= 80) {
  console.log("Nilai A");
} else if (nilai >= 70) {
  console.log("Nilai B");
} else {
  console.log("Nilai C");
}`,
      },
      {
        heading: "Versi Ringkas: Ternary Operator",
        body: [
          "Untuk kondisi sederhana, bisa ditulis satu baris dengan pola: kondisi ? jikaBenar : jikaSalah.",
        ],
        code: `const login = true;
const pesan = login ? "Selamat datang" : "Silakan masuk";

console.log(pesan);  // "Selamat datang"`,
      },
    ],
    debug: {
      description:
        "Kode di bawah seharusnya mencetak nilai dan tingkatan seorang pengguna. Tapi saat dijalankan, muncul error atau hasil yang aneh. Cari yang salah.",
      language: "js",
      errorCount: 3,
      brokenCode: `const nama = "Acel";
const umur = 20;

nama = "Budi";

const nilai = "85";

if (nilai >= 80) {
  console.log("Nilai A")
} else {
  console.log("Nilai B");
}

const user = { nama: "Acel", umur 20 };
console.log(user.umur);`,
      errors: [
        {
          hint: "Baris pertama deklarasi nama pakai keyword tertentu. Baris ketiga mencoba menggantinya. Apa yang akan terjadi?",
          fix: "'nama = \"Budi\";' akan menghasilkan error karena nama dideklarasi dengan const. Solusinya: ubah 'const nama' jadi 'let nama' di awal, ATAU hapus baris 'nama = \"Budi\";' kalau memang tidak perlu diganti.",
        },
        {
          hint: "Di dalam if yang pertama, lihat baris console.log. Ada yang hilang di akhir baris.",
          fix: "'console.log(\"Nilai A\")' kurang titik koma (;) di akhir. JavaScript kadang masih jalan, tapi biasakan menutup setiap statement dengan ';' supaya tidak bermasalah di case tertentu.",
        },
        {
          hint: "Di pembuatan object user, di antara 'umur' dan '20' ada yang hilang. Perhatikan baik-baik.",
          fix: "'{ nama: \"Acel\", umur 20 }' seharusnya '{ nama: \"Acel\", umur: 20 }'. Di object literal, key dan value dipisahkan dengan titik dua (:). Tanpa itu, JavaScript tidak tahu 20 itu nilai dari key mana.",
        },
      ],
      fixedCode: `let nama = "Acel";
const umur = 20;

nama = "Budi";

const nilai = 85;

if (nilai >= 80) {
  console.log("Nilai A");
} else {
  console.log("Nilai B");
}

const user = { nama: "Acel", umur: 20 };
console.log(user.umur);`,
    },
    quiz: {
      questions: [
        {
          question:
            "Kalau kamu menulis const nama = 'Acel', lalu mencoba nama = 'Budi', apa yang terjadi?",
          options: [
            { id: "a", text: "Berhasil, nama menjadi 'Budi'" },
            { id: "b", text: "Error, karena const tidak bisa diganti" },
            { id: "c", text: "Diam-diam diabaikan, tetap 'Acel'" },
            { id: "d", text: "Menjadi undefined" },
          ],
          answer: "b",
          explanation:
            "const berarti nilainya konstan. Coba diganti akan melempar error: Assignment to constant variable.",
        },
        {
          question: "Perbandingan mana yang lebih aman dan direkomendasikan?",
          options: [
            { id: "a", text: "== karena lebih fleksibel" },
            { id: "b", text: "=== karena mengecek nilai dan tipe data" },
            { id: "c", text: "= karena paling sederhana" },
            { id: "d", text: "!= karena kebalikannya" },
          ],
          answer: "b",
          explanation:
            "=== mengecek nilai sekaligus tipe data. == bisa bikin bug karena melakukan konversi otomatis.",
        },
        {
          question:
            "Tipe data apa yang paling tepat untuk menyimpan pasangan key-value seperti { nama: 'Acel', umur: 20 }?",
          options: [
            { id: "a", text: "String" },
            { id: "b", text: "Array" },
            { id: "c", text: "Object" },
            { id: "d", text: "Boolean" },
          ],
          answer: "c",
          explanation:
            "Object menyimpan data dalam bentuk key-value. Array untuk daftar berurutan, string untuk teks.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `const nama = "Acel";
nama = "Budi";

let umur = 20
console.log(umur)

if (umur = 25) {
  console.log("Umur 25");
}

const menu = ["home", "roadmap", "about"];
console.log(menu[3]);`,
      hints: ["const tidak bisa di-assign ulang", "Perhatikan beda = (assign) dan === (perbandingan) di dalam if", "Array index mulai dari 0, jadi index 3 di array berisi 3 item itu apa?"],
      fixedCode: `const nama = "Acel";
// nama = "Budi";  // ERROR: Assignment to constant variable

let umur = 20;
console.log(umur);

if (umur === 25) {
  console.log("Umur 25");
}

const menu = ["home", "roadmap", "about"];
console.log(menu[2]);  // "about" (index terakhir = panjang - 1)`,
      explanation: "Tiga error: (1) const tidak bisa diganti nilainya. (2) if (umur = 25) itu assignment, bukan perbandingan. Harusnya === untuk membandingkan. (3) menu[3] mengakses index ke-4 yang tidak ada (undefined). Index terakhir array 3 item adalah 2."
    },
    nextLesson: {
      href: "/materi/javascript/function-dan-scope",
      title: "Function & Scope",
    },
  },

  "javascript/function-dan-scope": {
    title: "Function & Scope",
    description:
      "Function itu resep kode yang bisa dipakai berulang-ulang. Scope itu aturan siapa boleh akses siapa. Dua hal fundamental yang perlu kamu kuasai.",
    readTime: "12 menit",
    level: "Level 2 — JavaScript",
    hero: {
      emoji: "🧩",
      caption: "Function yang baik mengerjakan satu hal dengan benar.",
    },
    objectives: [
      "Bisa bikin function dalam 3 gaya",
      "Paham beda parameter, argumen, dan return",
      "Tahu bedanya scope global, function, dan block",
      "Kenal konsep closure dan kenapa ia berguna",
    ],
    practice: {
      fileName: "functions.js",
      steps: [
        "Pastikan masih di folder belajar-js dari materi sebelumnya",
        "Di Explorer, klik ikon New File → ketik functions.js → Enter",
        "Buka index.html, cari baris <script src='app.js' defer></script>, ganti jadi <script src='functions.js' defer></script>",
        "Save semua (Ctrl + K Ctrl + S untuk save all, atau Ctrl + S di setiap file)",
        "Buka halaman pakai Live Server, tekan F12, pilih tab Console",
        "Coba tulis contoh function di bawah, save, lalu di tab Console ketik nama function-nya, contoh: sapa('Acel') lalu Enter. Hasilnya langsung muncul",
        "Bonus: sengaja ketik variable yang tidak ada, contoh console.log(lokal) di luar function. Lihat error merah yang muncul — itu pelajaran penting soal scope",
      ],
      tip: "Kalau function bisa ditulis singkat dan tidak pakai this, pilih arrow function. Kalau butuh this atau hoisting (panggil sebelum dideklarasi), pakai function declaration biasa.",
    },
    sections: [
      {
        heading: "Tiga Cara Menulis Function",
        body: [
          "Hasilnya sama, tapi sintaksnya beda. Di React modern, arrow function paling sering dipakai.",
        ],
        code: `// 1. Function declaration
function sapa(nama) {
  return "Halo, " + nama;
}

// 2. Function expression (disimpan ke variable)
const sapa2 = function (nama) {
  return "Halo, " + nama;
};

// 3. Arrow function (paling singkat)
const sapa3 = (nama) => "Halo, " + nama;

console.log(sapa("Acel"));   // "Halo, Acel"
console.log(sapa3("Budi"));  // "Halo, Budi"`,
      },
      {
        heading: "Parameter, Argumen, dan Return",
        list: [
          "Parameter: nama yang ditulis saat mendeklarasikan function. contoh: function tambah(a, b) → a dan b adalah parameter",
          "Argumen: nilai asli yang dikirim saat memanggil. contoh: tambah(3, 4) → 3 dan 4 adalah argumen",
          "Return: nilai yang dikirim balik oleh function. Kalau tidak ada return, hasilnya undefined",
        ],
        code: `function tambah(a, b) {       // a, b = parameter
  return a + b;
}

const hasil = tambah(3, 4);   // 3 dan 4 = argumen
console.log(hasil);           // 7

// Tanpa return
function sapa(nama) {
  console.log("Halo " + nama);
}
const x = sapa("Acel");       // tercetak "Halo Acel"
console.log(x);               // undefined (karena sapa tidak return)`,
      },
      {
        heading: "Scope: Siapa Bisa Akses Siapa",
        body: [
          "Variable yang dibuat di dalam function hanya bisa dibaca di dalam function itu. Ini disebut function scope. let dan const juga punya block scope, artinya mereka hanya hidup di dalam kurung kurawal { } terdekat.",
        ],
        code: `const pesan = "aku global";       // bisa diakses dimanapun

function contoh() {
  const lokal = "aku lokal";      // hanya hidup di dalam function
  console.log(pesan);             // valid, naik ke atas
  console.log(lokal);             // valid
}

contoh();
console.log(pesan);               // valid
console.log(lokal);               // ERROR: lokal is not defined`,
      },
      {
        heading: "Closure: Function yang Ingat Tempat Lahirnya",
        body: [
          "Closure terjadi saat sebuah function 'mengingat' variable dari tempat ia dibuat, bahkan setelah function parent-nya selesai. Konsep ini awal-awal terasa aneh, tapi penting banget dan dipakai di banyak tempat, termasuk React hooks.",
        ],
        code: `function buatCounter() {
  let hitung = 0;                   // variable lokal

  return function () {
    hitung++;                       // masih 'ingat' hitung
    return hitung;
  };
}

const counter = buatCounter();
console.log(counter());   // 1
console.log(counter());   // 2
console.log(counter());   // 3

// counter masih bisa akses 'hitung' walau buatCounter sudah selesai.
// Itulah closure.`,
      },
    ],
    debug: {
      description:
        "Kode di bawah seharusnya menghitung harga total belanja, lalu mencetaknya. Tapi ada yang salah — hasilnya bukan angka. Cari yang keliru.",
      language: "js",
      errorCount: 3,
      brokenCode: `function hitungTotal(harga, jumlah) {
  harga * jumlah;
}

const total = hitungTotal(10000, 3);
console.log("Total:", total);

const diskon = (persen) = {
  return persen / 100;
};

function tampilkan() {
  const pesan = "Halo dari dalam";
}

tampilkan();
console.log(pesan);`,
      errors: [
        {
          hint: "hitungTotal menghasilkan 'undefined'. Apa yang hilang di dalam function supaya nilainya dikirim keluar?",
          fix: "Di dalam hitungTotal kurang keyword 'return'. Harus jadi 'return harga * jumlah;'. Tanpa return, function menghitung tapi tidak mengirim hasilnya balik, jadi total menjadi undefined.",
        },
        {
          hint: "Perhatikan baris 'const diskon = (persen) = { ... }'. Ada tanda yang salah sebelum kurung kurawal.",
          fix: "'(persen) = {' seharusnya '(persen) => {'. Itu arrow function, butuh tanda panah '=>' bukan tanda sama dengan '='. Tanpa panah, JavaScript kira kamu mau assign value ke parameter.",
        },
        {
          hint: "Baris terakhir coba cetak 'pesan'. Tapi pesan didefinisikan di dalam tampilkan(). Apa masalahnya?",
          fix: "'console.log(pesan)' di luar function akan error: 'pesan is not defined'. Ini karena pesan adalah variable lokal di dalam tampilkan(), tidak bisa diakses dari luar. Ini adalah aturan scope.",
        },
      ],
      fixedCode: `function hitungTotal(harga, jumlah) {
  return harga * jumlah;
}

const total = hitungTotal(10000, 3);
console.log("Total:", total);

const diskon = (persen) => {
  return persen / 100;
};

function tampilkan() {
  const pesan = "Halo dari dalam";
  console.log(pesan);   // cetak di dalam function
}

tampilkan();`,
    },
    quiz: {
      questions: [
        {
          question:
            "Kenapa arrow function lebih sering dipilih di React modern?",
          options: [
            { id: "a", text: "Lebih cepat performanya" },
            { id: "b", text: "Sintaks lebih ringkas dan tidak punya this sendiri" },
            { id: "c", text: "Tidak bisa dijadikan callback" },
            { id: "d", text: "Dukungan browser lebih luas" },
          ],
          answer: "b",
          explanation:
            "Arrow function lebih ringkas dan menghindari masalah 'this' yang sering bikin bingung.",
        },
        {
          question:
            "Kalau sebuah function tidak menulis return sama sekali, nilai apa yang dihasilkan saat dipanggil?",
          options: [
            { id: "a", text: "null" },
            { id: "b", text: "0" },
            { id: "c", text: "undefined" },
            { id: "d", text: "Error langsung" },
          ],
          answer: "c",
          explanation:
            "Function tanpa return mengembalikan undefined secara otomatis.",
        },
        {
          question:
            "Dalam contoh buatCounter() di atas, kenapa variable 'hitung' tidak di-reset jadi 0 tiap kali counter() dipanggil?",
          options: [
            { id: "a", text: "Karena 'hitung' sebenarnya global" },
            { id: "b", text: "Karena function dalam 'mengingat' scope tempat ia dibuat (closure)" },
            { id: "c", text: "Karena let otomatis persistent" },
            { id: "d", text: "Karena JavaScript menyimpan semua variable di memori browser" },
          ],
          answer: "b",
          explanation:
            "Itulah closure. Function dalam tetap memegang akses ke scope parent-nya meskipun parent sudah selesai dijalankan.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `const sapa = (nama) => {
  return "Halo, " + nama
}

console.log(sapa);

function tambah(a, b) {
  a + b;
}

const hasil = tambah(3, 4);
console.log(hasil);

if (true) {
  let pesan = "halo";
}
console.log(pesan);`,
      hints: ["sapa itu function, untuk menjalankannya butuh tanda kurung ()", "Function tambah tidak mengembalikan apa-apa, cek keyword return", "Variable let di dalam { } tidak bisa diakses di luar { }"],
      fixedCode: `const sapa = (nama) => {
  return "Halo, " + nama;
};

console.log(sapa("Acel"));  // panggil dengan ()

function tambah(a, b) {
  return a + b;  // tambahkan return
}

const hasil = tambah(3, 4);
console.log(hasil);  // 7

if (true) {
  let pesan = "halo";
  console.log(pesan);  // akses di dalam scope-nya
}
// console.log(pesan);  // ERROR: pesan is not defined`,
      explanation: "Tiga error: (1) console.log(sapa) hanya mencetak definisi function, bukan hasilnya. Harus dipanggil: sapa('Acel'). (2) Function tambah tidak punya return, jadi hasilnya undefined. (3) let pesan hanya hidup di dalam { }, akses di luar akan error."
    },
    nextLesson: {
      href: "/materi/javascript/dom-manipulation",
      title: "DOM Manipulation",
    },
  },

  "javascript/dom-manipulation": {
    title: "DOM Manipulation: Membuat Halaman Bereaksi",
    description:
      "DOM adalah halaman web versi JavaScript. Dengan mengubahnya, kamu bisa bikin halaman bereaksi saat user klik, ketik, atau scroll.",
    readTime: "16 menit",
    level: "Level 2 — JavaScript",
    hero: {
      emoji: "🖱️",
      caption: "Halaman diam adalah halaman yang belum disentuh JavaScript.",
    },
    objectives: [
      "Bisa memilih elemen HTML dari JavaScript",
      "Bisa mengubah teks, atribut, dan class",
      "Bisa menanggapi aksi user dengan event listener",
      "Bisa bikin elemen baru dan menambahkannya ke halaman",
    ],
    practice: {
      fileName: "index.html + dom.js",
      steps: [
        "Masih di folder belajar-js. Buat file baru dom.js (klik ikon New File di Explorer)",
        "Di index.html, ganti <script src='functions.js' defer></script> jadi <script src='dom.js' defer></script>",
        "Ganti isi <body> di index.html dengan kode ini supaya ada elemen untuk dimainkan:\n<h1 id='judul'>Halo</h1>\n<button id='tombolku'>Klik aku</button>\n<p id='output'></p>",
        "Save semua, buka Live Server",
        "Di dom.js tulis contoh kode di bawah. Klik tombol di halaman, paragraf di bawahnya akan berubah. Itulah DOM manipulation",
        "Bonus: buka F12 → tab Elements. Klik tulisan <h1 id='judul'>Halo</h1> di sana (jadi ter-highlight biru). Lalu di tab Console ketik $0.textContent = 'Aku diubah dari Console' lalu Enter. Halaman ikut berubah. $0 adalah singkatan untuk elemen yang terakhir kamu klik di tab Elements",
      ],
      tip: "Kalau kamu lihat error 'Cannot read property ... of null' di Console, biasanya scriptnya jalan sebelum HTML selesai loading. Pastikan kamu pakai defer di tag <script>, seperti: <script src='dom.js' defer></script>.",
    },
    sections: [
      {
        heading: "Memilih Elemen",
        body: [
          "Sebelum mengubah, kamu harus memilih dulu. Dua method modern yang paling berguna: querySelector (satu elemen) dan querySelectorAll (semua yang cocok).",
        ],
        code: `// HTML:
// <h1 id="judul">Halo</h1>
// <p class="teks">Paragraf 1</p>
// <p class="teks">Paragraf 2</p>

// Ambil satu elemen dengan id 'judul'
const judul = document.querySelector("#judul");

// Ambil semua elemen dengan class 'teks'
const semuaTeks = document.querySelectorAll(".teks");

console.log(judul.textContent);   // "Halo"
console.log(semuaTeks.length);    // 2`,
      },
      {
        heading: "Mengubah Isi dan Tampilan",
        list: [
          "Ubah teks: element.textContent = 'baru'. contoh: judul.textContent = 'Halo Dunia'",
          "Ubah style langsung: element.style.color = 'red' (hanya untuk kebutuhan cepat)",
          "Tambah class: element.classList.add('aktif')",
          "Hapus class: element.classList.remove('nonaktif')",
          "Toggle class (tambah kalau belum ada, hapus kalau sudah ada): element.classList.toggle('terbuka')",
        ],
        code: `const judul = document.querySelector("#judul");

judul.textContent = "Halo Dunia";
judul.style.color = "#38bdf8";
judul.classList.add("aktif");`,
        body: [
          "Mengubah class lebih bersih daripada mengubah style langsung. Sebab stylingnya tetap di file CSS.",
        ],
      },
      {
        heading: "Event Listener: Menanggapi Aksi User",
        body: [
          "Event adalah cara browser memberitahu kode tentang aksi user: click, submit, input, scroll. Pasang reaksi lewat addEventListener.",
        ],
        code: `const tombol = document.querySelector("#tombolku");
const output = document.querySelector("#output");

let hitung = 0;

tombol.addEventListener("click", () => {
  hitung++;
  output.textContent = "Tombol diklik " + hitung + " kali";
});`,
      },
      {
        heading: "Contoh Kecil: Toggle Dark/Light Mode",
        body: [
          "Dengan beberapa baris JavaScript saja, kamu sudah bisa bikin fitur yang terlihat canggih.",
        ],
        code: `const toggle = document.querySelector("#toggle");

toggle.addEventListener("click", () => {
  document.body.classList.toggle("light");
});

/* CSS:
body.light {
  background: #f5f5f5;
  color: #0d0d0d;
}
*/`,
      },
      {
        heading: "Membuat Elemen Baru",
        body: [
          "Kadang kamu perlu menambah elemen ke halaman lewat JavaScript. Contohnya saat user menekan tombol 'Tambah Item'.",
        ],
        code: `const list = document.querySelector("#list");

function tambahItem(teks) {
  const li = document.createElement("li");
  li.textContent = teks;
  list.appendChild(li);
}

tambahItem("Belajar DOM");
tambahItem("Bikin todo list");`,
      },
    ],
    debug: {
      description:
        "Kode di bawah seharusnya: saat tombol diklik, teks di paragraf berubah dan class aktif di-toggle. Tapi ada beberapa error yang bikin kode gagal jalan.",
      language: "js",
      errorCount: 3,
      brokenCode: `const tombol = document.querySelector("tombolku");
const output = document.querySelector("#output");

tombol.addEventListener(click, () => {
  output.textContent = "Tombol diklik";
  output.classList.toggle.aktif;
});`,
      errors: [
        {
          hint: "querySelector menggunakan sintaks yang sama seperti CSS selector. Tombol kamu punya id='tombolku'. Apa yang kurang di selector pertama?",
          fix: "'querySelector(\"tombolku\")' seharusnya 'querySelector(\"#tombolku\")'. Untuk memilih by id, harus pakai tanda pagar (#) sama seperti di CSS.",
        },
        {
          hint: "Di addEventListener, parameter pertama adalah nama event. Format penulisannya perlu diperhatikan.",
          fix: "'addEventListener(click, ...)' seharusnya 'addEventListener(\"click\", ...)'. Nama event adalah string, jadi wajib dibungkus kutip. Tanpa kutip, JavaScript mengira 'click' adalah variable, dan bakal error karena tidak didefinisikan.",
        },
        {
          hint: "Di 'classList.toggle.aktif', cara memanggil method toggle kurang tepat. Method adalah function, jadi harus dipanggil bagaimana?",
          fix: "'classList.toggle.aktif' seharusnya 'classList.toggle(\"aktif\")'. toggle adalah method (function), harus dipanggil dengan tanda kurung dan nama class dibungkus kutip sebagai argumen.",
        },
      ],
      fixedCode: `const tombol = document.querySelector("#tombolku");
const output = document.querySelector("#output");

tombol.addEventListener("click", () => {
  output.textContent = "Tombol diklik";
  output.classList.toggle("aktif");
});`,
    },
    quiz: {
      questions: [
        {
          question:
            "Method yang paling rapi untuk menambah atau menghapus class 'aktif' saat tombol diklik?",
          options: [
            { id: "a", text: "element.style.class = 'aktif'" },
            { id: "b", text: "element.setAttribute('class', 'aktif')" },
            { id: "c", text: "element.classList.toggle('aktif')" },
            { id: "d", text: "element.innerHTML = 'aktif'" },
          ],
          answer: "c",
          explanation:
            "classList.toggle menambah class kalau belum ada dan menghapusnya kalau sudah ada. Ringkas dan aman.",
        },
        {
          question:
            "Kamu ingin memilih SEMUA elemen <p> yang punya class 'teks'. Pakai apa?",
          options: [
            { id: "a", text: "document.querySelector('.teks')" },
            { id: "b", text: "document.getElementById('teks')" },
            { id: "c", text: "document.querySelectorAll('.teks')" },
            { id: "d", text: "document.getTag('teks')" },
          ],
          answer: "c",
          explanation:
            "querySelector hanya ambil satu (yang pertama). querySelectorAll ambil semuanya dalam bentuk NodeList.",
        },
        {
          question: "Apa fungsi addEventListener?",
          options: [
            { id: "a", text: "Menambah elemen HTML baru ke halaman" },
            { id: "b", text: "Menanggapi aksi user seperti klik atau ketik" },
            { id: "c", text: "Menghapus elemen dari halaman" },
            { id: "d", text: "Mengganti isi teks elemen" },
          ],
          answer: "b",
          explanation:
            "addEventListener memasang reaksi yang dijalankan saat event (misal 'click') terjadi.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `const judul = document.querySelector("judul");
const tombol = document.querySelector("#tombolku");

tombol.addEventListener("click", function() {
  judul.textcontent = "Berubah!";
  judul.classlist.add("aktif");
});

document.querySelector("#list").innerHTML("<li>Item baru</li>");`,
      hints: ["querySelector butuh selector CSS yang valid (# untuk id, . untuk class)", "JavaScript itu case-sensitive: textContent bukan textcontent", "innerHTML bukan function, tapi property (pakai = bukan ())"],
      fixedCode: `const judul = document.querySelector("#judul");
const tombol = document.querySelector("#tombolku");

tombol.addEventListener("click", function() {
  judul.textContent = "Berubah!";
  judul.classList.add("aktif");
});

document.querySelector("#list").innerHTML = "<li>Item baru</li>";`,
      explanation: "Tiga error: (1) querySelector('judul') tanpa # tidak akan menemukan elemen dengan id judul. Harus '#judul'. (2) textcontent dan classlist salah huruf besar-kecilnya. Yang benar: textContent dan classList (huruf C dan L kapital). (3) innerHTML adalah property, bukan method. Pakai = untuk assign, bukan ()."
    },
    nextLesson: {
      href: "/materi/react-tailwind/pengenalan-react",
      title: "Pengenalan React",
    },
  },

  // ============================================================
  // LEVEL 3 — REACT & TAILWIND
  // ============================================================
  "react-tailwind/pengenalan-react": {
    title: "Pengenalan React: Cara Berpikir Komponen",
    description:
      "React mengubah cara bikin UI dari 'satu halaman penuh HTML' jadi 'susunan komponen yang bisa dipakai ulang'. Pas kamu paham pola pikirnya, semuanya lebih mudah.",
    readTime: "18 menit",
    level: "Level 3 — React & Tailwind",
    hero: {
      emoji: "⚛️",
      caption: "Bayangkan UI sebagai LEGO yang bisa disusun ulang.",
    },
    objectives: [
      "Tahu kenapa React populer",
      "Bisa bikin komponen pertamamu",
      "Bisa mengirim data antar komponen lewat props",
      "Paham dasar JSX dan aturan penulisannya",
    ],
    practice: {
      fileName: "App.jsx",
      steps: [
        "Pastikan Node.js sudah terinstall (cek dengan membuka terminal dan ketik: node -v. Kalau muncul versi seperti v20.x, berarti aman. Kalau belum, install dari nodejs.org dulu)",
        "Buka VS Code. Tekan Ctrl + ` (tanda backtick, di bawah tombol Esc) untuk buka Terminal terintegrasi",
        "Di terminal itu ketik: npm create vite@latest belajar-react -- --template react lalu Enter. Kalau ditanya install package, ketik y lalu Enter",
        "Setelah selesai, ketik berurutan: cd belajar-react lalu Enter, npm install lalu Enter (tunggu), lalu npm run dev lalu Enter",
        "Terminal akan menunjukkan alamat seperti http://localhost:5173. Klik link-nya sambil tahan Ctrl, atau buka di browser manual",
        "Di VS Code buka file src/App.jsx. Hapus isinya, ganti dengan contoh di bawah. Save (Ctrl + S). Halaman di browser otomatis berubah",
      ],
      tip: "Install ekstensi 'ES7+ React/Redux/React-Native snippets' di VS Code (Ctrl + Shift + X, cari nama itu). Setelah aktif, di file .jsx ketik rafce lalu tekan Tab — VS Code langsung generate komponen React lengkap.",
    },
    sections: [
      {
        heading: "Kenapa React?",
        body: [
          "Sebelum React, kamu nulis HTML, lalu manipulasi lewat JavaScript pakai DOM. Pas aplikasi membesar, kodenya ruwet.",
          "React menawarkan pola: pecah UI jadi komponen kecil. Tiap komponen cukup mendeskripsikan 'kalau data begini, tampilannya begini'. Kamu cukup ubah data, React yang urus update tampilannya.",
        ],
      },
      {
        heading: "Komponen Pertama",
        body: [
          "Komponen adalah function JavaScript yang mengembalikan JSX. Aturannya: nama komponen WAJIB diawali huruf kapital.",
        ],
        code: `// App.jsx
function App() {
  return (
    <div>
      <h1>Halo React</h1>
      <p>Aku belajar komponen pertamaku.</p>
    </div>
  );
}

export default App;`,
      },
      {
        heading: "JSX: HTML di dalam JavaScript",
        body: [
          "JSX kelihatan seperti HTML, tapi sebenarnya JavaScript. Ada beberapa aturan yang beda dari HTML biasa.",
        ],
        list: [
          "class menjadi className. contoh: <div className='kotak'>",
          "for di label menjadi htmlFor. contoh: <label htmlFor='email'>",
          "Semua tag harus ditutup. contoh: <img /> dan <br />",
          "Kamu bisa menyelipkan JavaScript dengan { }. contoh: <p>{nama}</p>",
        ],
        code: `function Sapaan() {
  const nama = "Acel";
  const jam = new Date().getHours();

  return (
    <div className="kotak">
      <h2>Halo, {nama}</h2>
      <p>{jam < 12 ? "Selamat pagi" : "Selamat siang"}</p>
    </div>
  );
}`,
      },
      {
        heading: "Props: Kirim Data ke Komponen Anak",
        body: [
          "Props itu cara parent ngasih data ke child. Mirip parameter function. Komponen yang sama bisa dipakai berkali-kali dengan isi beda.",
        ],
        code: `function Kartu({ judul, deskripsi }) {
  return (
    <div className="card">
      <h3>{judul}</h3>
      <p>{deskripsi}</p>
    </div>
  );
}

function App() {
  return (
    <div>
      <Kartu judul="HTML" deskripsi="Fondasi web." />
      <Kartu judul="CSS" deskripsi="Gaya halaman." />
      <Kartu judul="JS" deskripsi="Logika halaman." />
    </div>
  );
}`,
      },
      {
        heading: "Menampilkan List dengan .map()",
        body: [
          "Pola paling umum di React: punya array data, lalu diubah jadi array komponen pakai .map(). Jangan lupa kasih prop key yang unik untuk tiap item, supaya React bisa melacaknya.",
        ],
        code: `const materi = [
  { id: 1, judul: "HTML" },
  { id: 2, judul: "CSS" },
  { id: 3, judul: "JS" },
];

function Daftar() {
  return (
    <ul>
      {materi.map((m) => (
        <li key={m.id}>{m.judul}</li>
      ))}
    </ul>
  );
}`,
      },
    ],
    debug: {
      description:
        "Komponen React di bawah seharusnya menampilkan daftar 3 kartu. Tapi ada beberapa kesalahan umum yang bikin error. Cari yang salah.",
      language: "jsx",
      errorCount: 3,
      brokenCode: `const materi = [
  { id: 1, judul: "HTML" },
  { id: 2, judul: "CSS" },
  { id: 3, judul: "JS" },
];

function kartu({ judul }) {
  return (
    <div class="card">
      <h3>{judul}</h3>
    </div>
  );
}

function App() {
  return (
    <div>
      {materi.map((m) => (
        <kartu judul={m.judul} />
      ))}
    </div>
  );
}`,
      errors: [
        {
          hint: "Di JSX, atribut untuk memberi class CSS tidak ditulis seperti HTML biasa. Ada kata reserved di JavaScript.",
          fix: "'class=\"card\"' seharusnya 'className=\"card\"'. Di JSX, gunakan className karena 'class' sudah jadi keyword JavaScript (untuk bikin class).",
        },
        {
          hint: "Nama komponen React punya aturan huruf khusus. Perhatikan 'function kartu' dan '<kartu />'.",
          fix: "'function kartu' dan '<kartu />' seharusnya 'function Kartu' dan '<Kartu />'. Nama komponen React WAJIB diawali huruf kapital, supaya React bisa membedakan dari tag HTML biasa seperti <div>.",
        },
        {
          hint: "Di dalam .map(), setiap komponen yang dihasilkan membutuhkan sebuah prop khusus yang nilainya unik.",
          fix: "<Kartu judul={m.judul} /> kurang prop 'key'. Harus jadi <Kartu key={m.id} judul={m.judul} />. key membantu React melacak setiap item saat list berubah, dan menghasilkan warning kalau tidak ada.",
        },
      ],
      fixedCode: `const materi = [
  { id: 1, judul: "HTML" },
  { id: 2, judul: "CSS" },
  { id: 3, judul: "JS" },
];

function Kartu({ judul }) {
  return (
    <div className="card">
      <h3>{judul}</h3>
    </div>
  );
}

function App() {
  return (
    <div>
      {materi.map((m) => (
        <Kartu key={m.id} judul={m.judul} />
      ))}
    </div>
  );
}`,
    },
    quiz: {
      questions: [
        {
          question: "Kenapa tiap item di .map() butuh prop `key`?",
          options: [
            { id: "a", text: "Supaya tampilan lebih rapi" },
            {
              id: "b",
              text: "Supaya React bisa identifikasi item saat list berubah",
            },
            { id: "c", text: "Supaya JSX bisa jadi HTML" },
            { id: "d", text: "Tidak wajib, hanya rekomendasi gaya" },
          ],
          answer: "b",
          explanation:
            "key membantu React tahu item mana yang baru, berubah, atau dihapus, supaya update efisien dan konsisten.",
        },
        {
          question: "Di JSX, atribut class HTML ditulis jadi apa?",
          options: [
            { id: "a", text: "class" },
            { id: "b", text: "styleClass" },
            { id: "c", text: "className" },
            { id: "d", text: "cssClass" },
          ],
          answer: "c",
          explanation:
            "Di JSX, class ditulis sebagai className karena 'class' sudah jadi keyword di JavaScript.",
        },
        {
          question: "Nama komponen React yang benar?",
          options: [
            { id: "a", text: "function kartu() {}" },
            { id: "b", text: "function Kartu() {}" },
            { id: "c", text: "function KARTU() {}" },
            { id: "d", text: "function _Kartu() {}" },
          ],
          answer: "b",
          explanation:
            "Nama komponen React wajib PascalCase (huruf pertama kapital), supaya dibedakan dengan tag HTML biasa.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `function kartu({ judul, deskripsi }) {
  return (
    <div class="card">
      <h3>{judul}</h3>
      <p>{deskripsi}</p>
    </div>
  );
}

function App() {
  const items = ["HTML", "CSS", "JS"];
  return (
    <div>
      {items.map((item) => (
        <li>{item}</li>
      ))}
    </div>
  );
}`,
      hints: ["Nama komponen React wajib huruf kapital di awal", "Di JSX, class ditulis sebagai className", "Setiap item di .map() butuh prop key yang unik"],
      fixedCode: `function Kartu({ judul, deskripsi }) {
  return (
    <div className="card">
      <h3>{judul}</h3>
      <p>{deskripsi}</p>
    </div>
  );
}

function App() {
  const items = ["HTML", "CSS", "JS"];
  return (
    <div>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </div>
  );
}`,
      explanation: "Tiga error: (1) function kartu harus Kartu (PascalCase), kalau lowercase React menganggapnya tag HTML biasa. (2) class di JSX harus ditulis className karena class sudah jadi keyword JavaScript. (3) .map() tanpa key bikin React warning dan bisa bug saat list berubah."
    },
    nextLesson: {
      href: "/materi/react-tailwind/state-dan-hooks",
      title: "State & Hooks",
    },
  },

  "react-tailwind/state-dan-hooks": {
    title: "State & Hooks: Menghidupkan Komponen",
    description:
      "State adalah ingatan komponen. Hooks adalah cara modern memakainya. Pelajaran ini buka pintu ke fitur-fitur React yang paling ekspresif.",
    readTime: "20 menit",
    level: "Level 3 — React & Tailwind",
    hero: {
      emoji: "🔁",
      caption: "State bikin komponen berubah tanpa reload halaman.",
    },
    objectives: [
      "Paham apa itu state dan kapan dibutuhkan",
      "Bisa pakai useState untuk data yang berubah",
      "Bisa pakai useEffect untuk side-effect (misal fetch data)",
      "Kenal pola umum dan jebakan saat update state",
    ],
    practice: {
      fileName: "Counter.jsx",
      steps: [
        "Pastikan project Vite React dari materi sebelumnya masih ada. Kalau iya, cukup jalankan npm run dev lagi di terminal VS Code. Kalau belum ada, ulang langkah pembuatan project di materi sebelumnya",
        "Di VS Code, buka folder src. Klik ikon New File di sebelah folder src → ketik Counter.jsx → Enter",
        "Copy contoh di bawah ke Counter.jsx, save",
        "Buka src/App.jsx. Di atas, tambahkan: import Counter from './Counter'. Lalu di dalam return, taruh <Counter /> di mana saja. Save",
        "Lihat browser — muncul tombol dan angka. Klik tombol beberapa kali, angkanya naik. Itulah state",
        "Bonus: install 'React Developer Tools' di browser (cari di Chrome Web Store atau Edge Add-ons). Setelah install, buka F12, akan muncul tab baru bernama Components. Di situ kamu bisa lihat state setiap komponen secara live",
      ],
      tip: "Kalau angkanya tidak naik, kemungkinan besar kamu lupa panggil setter (setHitung). Ingat aturan: state cuma berubah lewat setternya, tidak bisa diubah dengan assignment biasa seperti hitung = hitung + 1.",
    },
    sections: [
      {
        heading: "Kenapa Butuh State?",
        body: [
          "Variable biasa di dalam komponen akan hilang tiap kali komponen dirender ulang. State itu ingatan yang bertahan antar render, sekaligus otomatis memicu render ulang saat isinya berubah.",
        ],
      },
      {
        heading: "useState: Hook Paling Penting",
        body: [
          "useState mengembalikan pasangan: [nilai, fungsi-untuk-ubah-nilai]. Jangan pernah langsung ubah state pakai assignment biasa. Selalu pakai setter-nya.",
        ],
        code: `import { useState } from "react";

function Counter() {
  const [hitung, setHitung] = useState(0);
  //       |              |
  //       |              setter (fungsi untuk ubah)
  //       nilai sekarang

  return (
    <div>
      <p>Kamu sudah klik {hitung} kali</p>
      <button onClick={() => setHitung(hitung + 1)}>
        Tambah
      </button>
    </div>
  );
}`,
      },
      {
        heading: "Aturan Hooks",
        list: [
          "Panggil hook hanya di top level komponen. Jangan di dalam if, loop, atau function lain",
          "Panggil hook hanya dari komponen React atau custom hook",
          "Custom hook wajib diawali 'use'. contoh: useForm, useWindowSize",
        ],
      },
      {
        heading: "useEffect: Menanggapi Perubahan",
        body: [
          "useEffect jalan setelah komponen dirender. Pas untuk fetch data, update document title, atau subscribe ke sesuatu. Kamu tentukan kapan effect jalan lewat dependency array.",
        ],
        code: `import { useEffect, useState } from "react";

function JudulHalaman() {
  const [nama, setNama] = useState("Acel");

  useEffect(() => {
    document.title = "Hai, " + nama;
  }, [nama]);   // effect jalan tiap kali 'nama' berubah

  return (
    <input
      value={nama}
      onChange={(e) => setNama(e.target.value)}
    />
  );
}`,
        list: [
          "Dependency array [] kosong: effect jalan sekali saat komponen muncul",
          "Dependency array [nama]: effect jalan saat nama berubah",
          "Tanpa dependency array: effect jalan tiap render (jarang dibutuhkan)",
        ],
      },
      {
        heading: "Update State yang Benar",
        body: [
          "Kalau state baru bergantung pada state lama, gunakan bentuk callback. Ini lebih aman saat ada beberapa update berurutan.",
        ],
        code: `// Kurang aman (bisa bug di beberapa kasus)
setHitung(hitung + 1);
setHitung(hitung + 1);   // ini hasil akhirnya cuma +1, bukan +2

// Lebih aman
setHitung((prev) => prev + 1);
setHitung((prev) => prev + 1);   // hasil akhirnya +2`,
      },
      {
        heading: "Lifting State Up",
        body: [
          "Kalau dua komponen saudara butuh data yang sama, taruh state di parent mereka, lalu kirim ke bawah lewat props. Ini pola standar di React: lifting state up.",
        ],
      },
    ],
    debug: {
      description:
        "Counter di bawah seharusnya menambah angka setiap tombol diklik, dan mengubah judul halaman sesuai angka saat ini. Tapi ada error. Coba cari.",
      language: "jsx",
      errorCount: 3,
      brokenCode: `import { useState, useEffect } from "react";

function Counter() {
  let hitung = useState(0);

  useEffect(() => {
    document.title = "Counter: " + hitung;
  });

  return (
    <div>
      <p>Angka: {hitung}</p>
      <button onClick={hitung = hitung + 1}>
        Tambah
      </button>
    </div>
  );
}`,
      errors: [
        {
          hint: "useState mengembalikan sesuatu yang berpasangan. Bentuk penyimpanannya tidak boleh hanya sebuah variable.",
          fix: "'let hitung = useState(0)' seharusnya 'const [hitung, setHitung] = useState(0)'. useState mengembalikan array dengan 2 elemen: [nilai, setter]. Kita pakai destructuring untuk memisahnya.",
        },
        {
          hint: "useEffect yang tidak punya dependency array akan jalan SETIAP render. Saat ia update title, komponen re-render lagi, dan seterusnya. Apa yang bisa kamu tambahkan untuk membatasi?",
          fix: "useEffect kurang dependency array. Harusnya: useEffect(() => { ... }, [hitung]). Tanpa array [hitung], effect jalan setiap render dan bisa bikin infinite loop.",
        },
        {
          hint: "Di onClick tombol, state dicoba diubah dengan assignment biasa. React tidak akan tahu bahwa state berubah kecuali kamu pakai cara yang benar.",
          fix: "'onClick={hitung = hitung + 1}' seharusnya 'onClick={() => setHitung(hitung + 1)}'. State HANYA boleh diubah lewat setter (setHitung), tidak bisa dengan assignment biasa. Dan onClick butuh function, bukan ekspresi langsung.",
        },
      ],
      fixedCode: `import { useState, useEffect } from "react";

function Counter() {
  const [hitung, setHitung] = useState(0);

  useEffect(() => {
    document.title = "Counter: " + hitung;
  }, [hitung]);

  return (
    <div>
      <p>Angka: {hitung}</p>
      <button onClick={() => setHitung(hitung + 1)}>
        Tambah
      </button>
    </div>
  );
}`,
    },
    quiz: {
      questions: [
        {
          question:
            "Kamu panggil setCount(count + 1) dua kali berturut-turut. Ternyata count cuma bertambah 1, bukan 2. Kenapa?",
          options: [
            { id: "a", text: "React menyamakan semua update jadi satu" },
            {
              id: "b",
              text: "Karena count masih membaca nilai lama. Pakai callback (prev) => prev + 1",
            },
            { id: "c", text: "Harus pakai useEffect dulu" },
            { id: "d", text: "React membatasi setState sekali per render" },
          ],
          answer: "b",
          explanation:
            "Kedua panggilan membaca nilai count yang sama di render itu. Pakai callback form supaya update berurutan akurat.",
        },
        {
          question:
            "Apa arti dependency array [] kosong pada useEffect?",
          options: [
            { id: "a", text: "Effect jalan setiap render" },
            { id: "b", text: "Effect jalan sekali saat komponen muncul" },
            { id: "c", text: "Effect tidak pernah jalan" },
            { id: "d", text: "Effect jalan saat komponen unmount saja" },
          ],
          answer: "b",
          explanation:
            "Dependency array [] kosong artinya tidak ada yang diawasi, jadi effect hanya jalan sekali saat komponen mount.",
        },
        {
          question:
            "Kenapa sebuah function tidak boleh langsung mengubah state dengan assignment biasa (misal count = count + 1)?",
          options: [
            { id: "a", text: "Karena itu merubah tipe data" },
            { id: "b", text: "Karena React hanya re-render kalau state diubah lewat setter" },
            { id: "c", text: "Karena JavaScript tidak mengizinkan" },
            { id: "d", text: "Tidak apa-apa, boleh saja" },
          ],
          answer: "b",
          explanation:
            "Hanya setter dari useState yang memberi tahu React untuk render ulang komponen. Assignment biasa tidak memicu render.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `import { useState } from "react";

function Counter() {
  let [hitung, setHitung] = useState(0);

  function tambah() {
    hitung = hitung + 1;
    setHitung(hitung + 1);
    setHitung(hitung + 1);
  }

  useEffect(() => {
    document.title = "Count: " + hitung;
  });

  return (
    <div>
      <p>{hitung}</p>
      <button onClick={tambah()}>Tambah</button>
    </div>
  );
}`,
      hints: ["Jangan ubah state langsung dengan assignment, selalu lewat setter", "setHitung dipanggil dua kali tapi pakai nilai yang sama, gunakan callback form", "useEffect tanpa import akan error", "onClick={tambah()} langsung memanggil function saat render, harusnya onClick={tambah}"],
      fixedCode: `import { useState, useEffect } from "react";

function Counter() {
  const [hitung, setHitung] = useState(0);

  function tambah() {
    setHitung((prev) => prev + 1);
  }

  useEffect(() => {
    document.title = "Count: " + hitung;
  }, [hitung]);

  return (
    <div>
      <p>{hitung}</p>
      <button onClick={tambah}>Tambah</button>
    </div>
  );
}`,
      explanation: "Empat error: (1) hitung = hitung + 1 mengubah state langsung, ini dilarang. Selalu lewat setter. (2) useEffect tidak di-import. (3) onClick={tambah()} langsung menjalankan function saat render, bukan saat diklik. Hapus (). (4) useEffect tanpa dependency array jalan setiap render, tambahkan [hitung]."
    },
    nextLesson: {
      href: "/materi/real-project/struktur-project-modern",
      title: "Struktur Project Modern",
    },
  },

  // ============================================================
  // LEVEL 4 — REAL PROJECT
  // ============================================================
  "real-project/struktur-project-modern": {
    title: "Struktur Project Modern",
    description:
      "Project nyata bukan soal banyak file, tapi file yang tahu tempatnya: jelas fungsinya, mudah dicari, dan tidak saling menyeret saat diganti.",
    readTime: "10 menit",
    level: "Level 4 — Real Project",
    hero: {
      emoji: "🗂️",
      caption: "Struktur yang baik bikin project tumbuh tanpa berantakan.",
    },
    objectives: [
      "Bisa menyusun folder project yang scalable",
      "Paham prinsip colocation (file terkait berdekatan)",
      "Tahu bedanya folder komponen, fitur, dan utility",
      "Biasa pakai alias import supaya path tidak panjang",
    ],
    practice: {
      fileName: "struktur folder",
      steps: [
        "Buka project React / Next.js yang sudah kamu buat di materi sebelumnya (misal belajar-react). Kalau belum ada, buat dulu dengan: npm create vite@latest belajar-struktur -- --template react di terminal VS Code",
        "Di Explorer VS Code, lihat folder src. Perhatikan bagaimana file disusun di sana",
        "Coba terapkan pola di bawah: klik kanan folder src → New Folder, buat folder components, hooks, lib. Pindahkan file lama ke tempat yang sesuai",
        "Buat alias import: di root project buat file jsconfig.json (klik kanan di area kosong Explorer → New File → ketik nama). Copy config dari contoh di bawah ke file itu. Save, lalu restart server dev (Ctrl + C di terminal, lalu npm run dev lagi)",
        "Sekarang di file kamu bisa pakai: import Card from '@/components/ui/Card' tanpa jalan panjang seperti '../../../components/ui/Card'",
      ],
      tip: "Nyalakan fitur 'File Nesting' di VS Code: File → Preferences → Settings → ketik 'file nesting' → centang Explorer: File Nesting Enabled. File yang terkait (misal Card.jsx + Card.module.css) akan dikelompokkan rapi di Explorer.",
    },
    sections: [
      {
        heading: "Prinsip Umum",
        list: [
          "Colocation: file yang sering diubah bersama, simpan berdekatan. contoh: Component.jsx dan Component.module.css di folder yang sama",
          "Separation of concerns: UI, data, dan logika di layer masing-masing. contoh: komponen di components/, data di lib/",
          "Scalability: struktur sama untuk 10 file dan 1000 file",
          "Readability: orang baru harus paham dalam 5 menit",
        ],
      },
      {
        heading: "Contoh Struktur yang Aman Buat Tumbuh",
        code: `src/
├── app/                # Route (Next.js App Router)
├── components/
│   ├── ui/             # Komponen dasar: Button, Card, Input
│   ├── layout/         # Navbar, Footer, Sidebar
│   └── [fitur]/        # Komponen spesifik fitur tertentu
├── hooks/              # Custom hooks (useSomething)
├── lib/                # Data, utility, helper murni JS
├── styles/             # CSS global (kalau ada)
└── public/             # Asset statis (gambar, favicon)`,
      },
      {
        heading: "Konvensi Penamaan",
        list: [
          "Komponen React: PascalCase. contoh: Card.jsx, UserAvatar.jsx",
          "Hook: camelCase diawali 'use'. contoh: useForm.js, useWindowSize.js",
          "Utility: camelCase. contoh: formatDate.js, parseQuery.js",
          "Folder: lowercase atau kebab-case. contoh: user-profile/",
        ],
      },
      {
        heading: "Alias Import",
        body: [
          "Daripada import '../../../components/ui/Card', pakai alias supaya path bersih dan tidak pusing saat memindahkan file.",
        ],
        code: `// jsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}

// Pemakaian
import Card from "@/components/ui/Card";
import { formatDate } from "@/lib/utils";`,
      },
      {
        heading: "Aturan Emas",
        body: [
          "Jangan terjebak mencari 'struktur sempurna' di hari pertama. Mulai sederhana, refactor saat terasa sakit. Yang penting konsisten.",
        ],
      },
    ],
    debug: {
      description:
        "File di bawah punya beberapa masalah organisasi. Kamu diminta me-review kode junior yang baru gabung. Temukan kebiasaan buruknya.",
      language: "jsx",
      errorCount: 3,
      brokenCode: `// src/components/usercard.jsx
import Button from "../../../components/ui/Button";
import { formatDate } from "../../../../lib/utils";

export default function userCard({ nama, tanggal }) {
  return (
    <div>
      <h3>{nama}</h3>
      <p>{formatDate(tanggal)}</p>
      <Button>Detail</Button>
    </div>
  );
}`,
      errors: [
        {
          hint: "Penamaan file dan komponen React punya konvensi yang jelas. Perhatikan nama file dan nama function yang di-export.",
          fix: "'usercard.jsx' dan 'function userCard' seharusnya 'UserCard.jsx' dan 'function UserCard'. Konvensi React: nama komponen dan file-nya memakai PascalCase (huruf pertama tiap kata kapital).",
        },
        {
          hint: "Path import '../../../' dan '../../../../' tergolong panjang dan rapuh. Kalau file-nya dipindah, semua path ini harus diperbaiki manual. Apa solusinya?",
          fix: "Gunakan alias import. Setup '@/*' di jsconfig.json lalu tulis: import Button from '@/components/ui/Button' dan import { formatDate } from '@/lib/utils'. Lebih pendek, lebih aman saat refactor.",
        },
        {
          hint: "Komponen ini punya import yang tidak dipakai. Apa saja yang kamu lihat tidak terpakai di JSX?",
          fix: "Dalam kasus ini sebenarnya semua import dipakai. Tapi yang perlu diperhatikan: kebiasaan nulis komponen UserCard TANPA memanfaatkan struktur folder components/ sesuai jenisnya. Idealnya komponen ini tinggal di 'src/components/ui/UserCard.jsx' atau 'src/components/user/UserCard.jsx' agar kolega mudah mencarinya.",
        },
      ],
      fixedCode: `// src/components/user/UserCard.jsx
import Button from "@/components/ui/Button";
import { formatDate } from "@/lib/utils";

export default function UserCard({ nama, tanggal }) {
  return (
    <div>
      <h3>{nama}</h3>
      <p>{formatDate(tanggal)}</p>
      <Button>Detail</Button>
    </div>
  );
}`,
    },
    quiz: {
      questions: [
        {
          question:
            "Prinsip mana yang paling dekat dengan kata 'colocation'?",
          options: [
            { id: "a", text: "Letakkan semua file di src/ agar pendek" },
            {
              id: "b",
              text: "Simpan file yang sering berubah bersama dalam satu tempat",
            },
            { id: "c", text: "Pisahkan ketat file CSS dari file JS" },
            { id: "d", text: "Buat folder sebanyak mungkin supaya rapi" },
          ],
          answer: "b",
          explanation:
            "Colocation menyarankan menyimpan file yang berubah bersama supaya navigasi dan refactor lebih mudah.",
        },
        {
          question:
            "Konvensi penamaan yang benar untuk komponen React?",
          options: [
            { id: "a", text: "user-card.jsx" },
            { id: "b", text: "userCard.jsx" },
            { id: "c", text: "UserCard.jsx" },
            { id: "d", text: "USERCARD.jsx" },
          ],
          answer: "c",
          explanation:
            "Komponen React pakai PascalCase (huruf pertama tiap kata kapital). Sesuai dengan aturan nama komponen itu sendiri.",
        },
        {
          question:
            "Manfaat utama setup alias import '@/*' di jsconfig.json?",
          options: [
            { id: "a", text: "Mempercepat build project" },
            { id: "b", text: "Menghindari path relatif yang panjang dan memudahkan refactor" },
            { id: "c", text: "Wajib untuk Next.js" },
            { id: "d", text: "Mengamankan file dari import luar" },
          ],
          answer: "b",
          explanation:
            "Alias bikin path import bersih. Saat memindahkan file, kamu tidak perlu memperbaiki banyak '../../../'.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `// File: src/components/ui/card.jsx
export default function card() {
  return <div className="card">...</div>;
}

// File: src/App.jsx
import card from "../../../components/ui/card";
import { formatdate } from "../../../lib/utils";

function App() {
  return <card />;
}`,
      hints: ["Nama file dan komponen React harusnya PascalCase", "Import path yang panjang bisa diganti alias @/", "Nama function komponen harus PascalCase supaya React mengenalinya"],
      fixedCode: `// File: src/components/ui/Card.jsx
export default function Card() {
  return <div className="card">...</div>;
}

// File: src/App.jsx
import Card from "@/components/ui/Card";
import { formatDate } from "@/lib/utils";

function App() {
  return <Card />;
}`,
      explanation: "Tiga masalah: (1) Nama file card.jsx dan function card() harusnya Card.jsx dan Card() (PascalCase). React menganggap <card /> sebagai tag HTML biasa, bukan komponen. (2) Path '../../../' panjang dan rapuh, pakai alias @/ lebih bersih. (3) formatdate harusnya formatDate (camelCase)."
    },
    nextLesson: {
      href: "/materi/career-freelance/membangun-portfolio",
      title: "Membangun Portfolio",
    },
  },

  // ============================================================
  // LEVEL 5 — CAREER & FREELANCE
  // ============================================================
  "career-freelance/membangun-portfolio": {
    title: "Membangun Portfolio yang Menarik Klien",
    description:
      "Portfolio bukan cuma showcase. Ia cerita singkat tentang kemampuan, proses, dan keputusanmu. Pelajaran ini bantu kamu menyusunnya.",
    readTime: "12 menit",
    level: "Level 5 — Career & Freelance",
    hero: {
      emoji: "🎯",
      caption: "Portfolio bagus menjawab pertanyaan klien sebelum ditanyakan.",
    },
    objectives: [
      "Paham apa yang dicari klien dan perekrut",
      "Bisa memilih project yang layak tampil",
      "Bisa menulis studi kasus yang hidup",
      "Siap dengan domain, hosting, dan deployment",
    ],
    practice: {
      fileName: "portfolio/",
      steps: [
        "Pilih 3 project terbaikmu dari folder latihanmu. Masing-masing buka di VS Code",
        "Di setiap project, buat file README.md di root (klik ikon New File di Explorer). Isi dengan 4 bagian singkat: Problem, Process, Result, Learning. Lihat contoh di bawah",
        "Upload setiap project ke GitHub. Cara paling cepat: install GitHub Desktop dari desktop.github.com, login, klik 'Add Local Repository' pilih folder project, lalu 'Publish repository'",
        "Deploy salah satu project sebagai portfolio utama ke Vercel: buka vercel.com, login pakai GitHub, klik 'Add New Project' → pilih repo → klik Deploy. Selesai dalam 1-2 menit",
        "Opsional — beli domain sendiri: buka namecheap.com atau domainesia.com, cari 'nama-kamu.dev' atau '.me' (biasanya Rp 150-200rb setahun). Di Vercel, tab Settings → Domains → tambahkan domainmu",
      ],
      tip: "Vercel otomatis redeploy setiap kamu push update ke GitHub. Ini workflow yang dipakai developer profesional, dan kamu sudah punya ini di project pertama.",
    },
    sections: [
      {
        heading: "Apa yang Dicari Klien dan Perekrut?",
        list: [
          "Bukti bahwa kamu bisa menyelesaikan sesuatu yang utuh. contoh: link project live, bukan sekadar kode di GitHub",
          "Cara berpikir dan pengambilan keputusan. contoh: cerita 'kenapa pilih React, bukan plain JS'",
          "Kualitas kode dan struktur yang rapi. contoh: README yang jelas, commit yang bermakna",
          "Kemampuan komunikasi lewat tulisan. contoh: studi kasus yang mudah dibaca",
        ],
      },
      {
        heading: "Tiga Jenis Project yang Layak Tampil",
        list: [
          "Project pribadi: menunjukkan minat dan inisiatif. contoh: dashboard keuangan pribadi, blog pribadi",
          "Clone atau rebuild: bukti kamu bisa membaca UI dan mereplikasinya dengan rapi. contoh: clone landing page startup favorit",
          "Project kolaborasi atau klien: bukti kamu bisa kerja dalam konteks nyata. contoh: landing page UMKM, event page kampus",
        ],
      },
      {
        heading: "Formula Studi Kasus: PPRL",
        list: [
          "Problem: masalah apa yang ingin dipecahkan. contoh: 'UMKM teman butuh landing page untuk promosi'",
          "Process: bagaimana kamu menyelesaikannya, tools, trade-off. contoh: 'pilih Next.js karena butuh SEO bagus'",
          "Result: hasilnya, metrik kalau ada, link live. contoh: '300 pengunjung di minggu pertama'",
          "Learning: apa yang kamu pelajari. contoh: 'pertama kali menangani form dengan validasi real-time'",
        ],
      },
      {
        heading: "Hal Teknis yang Perlu Disiapkan",
        list: [
          "Website portfolio yang cepat dan responsif",
          "Domain custom kalau memungkinkan (opsional tapi profesional)",
          "Link GitHub aktif dengan README project yang rapi",
          "Foto profil profesional, tidak perlu formal tapi jelas wajah",
          "Kontak mudah: email profesional dan LinkedIn",
        ],
      },
      {
        heading: "Kesalahan yang Sering Terjadi",
        list: [
          "Terlalu banyak project tanpa fokus. 3 project bagus > 10 project setengah jadi",
          "Cuma pajang screenshot tanpa cerita",
          "Lupa cantumkan link live dan link repo",
          "Tidak cek tampilan di mobile sebelum dibagikan",
          "Bio membosankan. Tulis yang jujur dan spesifik",
        ],
      },
    ],
    debug: {
      description:
        "Seorang junior kirim README project portfolio untuk di-review. Sebagai reviewer, cari bagian yang perlu diperbaiki supaya lebih menarik bagi klien.",
      language: "html",
      errorCount: 3,
      brokenCode: `# project saya

Ini adalah project yang saya buat pakai React.
Saya buat ini sekitar 2 bulan.

## Teknologi

- React
- Tailwind

## Cara run

npm install
npm run dev`,
      errors: [
        {
          hint: "Judul 'project saya' terlalu generik. Nama klien atau topik project-nya sebaiknya jelas terlihat.",
          fix: "'project saya' seharusnya nama spesifik, misal '# Warung Digital — Landing page UMKM'. Judul yang jelas langsung kasih konteks. 'project saya' bikin reviewer harus menebak.",
        },
        {
          hint: "Deskripsi 'Ini adalah project yang saya buat pakai React' menjawab 'apa', tapi bukan 'kenapa'. Klien ingin tahu masalah apa yang dipecahkan.",
          fix: "Tambahkan formula PPRL singkat: Problem (masalah yang dipecahkan), Process (tools dan alasannya), Result (hasil, metrik, link live), Learning (apa yang dipelajari). Ini yang membedakan portfolio yang 'hidup' dengan yang sekadar gallery.",
        },
        {
          hint: "Ada dua hal penting yang hilang, yang seharusnya ada di bagian awal README portfolio. Coba pikir: kalau reviewer cuma punya 10 detik, apa yang paling ingin dia lihat?",
          fix: "Hilang link live demo dan screenshot. Minimal taruh 'Live demo: https://...' dan 1 gambar hero di bagian atas. Tanpa link live, reviewer harus clone repo dan jalankan sendiri — 90% dari mereka tidak akan repot-repot.",
        },
      ],
      fixedCode: `# Warung Digital — Landing page UMKM

Landing page untuk membantu UMKM promosi online.
Live demo: https://warung-digital.vercel.app

![screenshot](./docs/hero.png)

## Problem
Banyak UMKM kesulitan promosi online karena tidak punya website.
Pemilik ingin satu halaman untuk promosi dan daftar kontak.

## Process
- React + Vite untuk kecepatan development
- Tailwind untuk styling konsisten
- Deploy ke Vercel karena gratis dan auto-CD dari GitHub

## Result
- Halaman live dalam 1 minggu
- Load time 1.2 detik di jaringan 4G
- 300+ pengunjung di minggu pertama

## Learning
Pertama kali menangani form kontak yang kirim email real
pakai Resend API. Belajar juga tentang SEO dasar.

## Teknologi
React · Tailwind · Vite · Vercel · Resend

## Cara run lokal
\`\`\`
npm install
npm run dev
\`\`\``,
    },
    quiz: {
      questions: [
        {
          question:
            "Mana yang paling penting dalam sebuah studi kasus portfolio?",
          options: [
            { id: "a", text: "Jumlah screenshot sebanyak mungkin" },
            { id: "b", text: "Cerita tentang proses dan keputusan" },
            { id: "c", text: "Ditulis dalam bahasa Inggris" },
            { id: "d", text: "Menampilkan semua project yang pernah dibuat" },
          ],
          answer: "b",
          explanation:
            "Studi kasus yang kuat berfokus pada proses berpikir dan keputusan, bukan sekadar galeri hasil akhir.",
        },
        {
          question:
            "Dalam formula PPRL, apa arti huruf 'L'?",
          options: [
            { id: "a", text: "Link (link ke live demo)" },
            { id: "b", text: "Logo (logo project)" },
            { id: "c", text: "Learning (apa yang dipelajari)" },
            { id: "d", text: "Layout (desain layout)" },
          ],
          answer: "c",
          explanation:
            "L = Learning. Ceritakan apa yang kamu pelajari atau akan kamu ubah kalau mengulang project-nya.",
        },
        {
          question:
            "Kamu punya 3 project bagus dan 7 project setengah jadi. Mana yang lebih baik ditampilkan di portfolio?",
          options: [
            { id: "a", text: "Semua 10 project agar terlihat produktif" },
            { id: "b", text: "3 project bagus yang sudah jadi dan punya cerita" },
            { id: "c", text: "7 project setengah jadi karena lebih banyak" },
            { id: "d", text: "Tidak ditampilkan sampai punya 10 project jadi" },
          ],
          answer: "b",
          explanation:
            "Klien menilai kualitas, bukan kuantitas. 3 project yang matang dan berceritakan jauh lebih meyakinkan.",
        },
      ],
    },
    errorChallenge: {
      title: "Cari Error",
      instruction: "Kode di bawah ada yang salah. Coba temukan dan perbaiki errornya sebelum lihat jawaban.",
      buggyCode: `# Portfolio Saya

saya bisa html css javascript react

## Project
- project 1
- project 2

## Kontak
email: acel@gmail.com`,
      hints: ["README yang baik punya struktur jelas: deskripsi, screenshot, tech stack, link live", "Jangan hanya list nama project tanpa penjelasan", "Tunjukkan proses dan keputusan, bukan hanya hasil"],
      fixedCode: `# Portfolio — Acel

Frontend developer yang fokus membangun UI modern dan responsif.

## 🚀 Project Unggulan

### 1. LearnWithAcel
Platform belajar web development dengan roadmap terstruktur.
- **Tech:** Next.js, Tailwind CSS, Framer Motion
- **Link:** [Live Demo](https://learnwithacel.dev) | [GitHub](https://github.com/...)
- **Cerita:** Dibuat karena dulu bingung mulai belajar dari mana. Fokus pada UX pemula.

### 2. Dashboard Admin
Mini dashboard dengan chart dan tabel data.
- **Tech:** React, Recharts, Tailwind
- **Link:** [Live Demo](#) | [GitHub](#)

## 📬 Kontak
- Email: halo@acel.dev
- LinkedIn: linkedin.com/in/acel
- GitHub: github.com/acel`,
      explanation: "README portfolio yang lemah: tidak ada deskripsi diri, project tanpa konteks, dan tidak ada link live. Yang kuat: ada intro singkat, setiap project punya tech stack, link live + repo, dan cerita singkat kenapa dibuat. Klien ingin lihat proses berpikir, bukan sekadar daftar."
    },
    nextLesson: null,
  },
};

export function getLesson(levelSlug, lessonSlug) {
  const key = `${levelSlug}/${lessonSlug}`;
  return lessonContent[key] || null;
}
