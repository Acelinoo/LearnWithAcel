/**
 * Static data for jalur (path) onboarding pages.
 *
 * Phase 1 ships the new flow with hardcoded fundamentals content. The
 * shape mirrors what the backend will return in Phase 2 so we can swap
 * the source without touching the page components.
 *
 * Slugs are kept stable on purpose. Once the DB seed lands, these
 * lessons can be moved 1:1 into Categories `manual-fundamentals` and
 * `vibe-fundamentals` without breaking any links shared during testing.
 */

export type JalurPath = "manual" | "vibe";

export type JalurLesson = {
  slug: string;
  title: string;
  duration: string;
  summary: string;
  /** Markdown body. */
  content: string;
};

export type JalurRole = {
  slug: string;
  href: string;
  badge: string;
  title: string;
  tagline: string;
  description: string;
  bullets: string[];
  available: boolean;
};

export type JalurMeta = {
  path: JalurPath;
  badge: string;
  badgeTone: "accent" | "sky";
  eyebrow: string;
  title: string;
  subtitle: string;
  tagline: string;
  intro: string;
  setupHref: string;
  setupCtaLabel: string;
  fullRoadmapHref: string | null;
  fullRoadmapLabel: string;
  roleSectionTitle: string;
  roleSectionSubtitle: string;
  lessons: JalurLesson[];
  roles: JalurRole[];
};

// ─────────────────────────────────────────────────────────────────────
// Manual fundamentals — 6 lessons.
// ─────────────────────────────────────────────────────────────────────

const MANUAL_LESSONS: JalurLesson[] = [
  {
    slug: "cara-kerja-website",
    title: "Cara Kerja Website",
    duration: "8 menit",
    summary:
      "Apa yang sebenernya kejadian saat kamu ngetik URL terus pencet Enter.",
    content: `# Cara Kerja Website

Coba kamu pikirin sebentar. Kamu buka WhatsApp Web. Klik chat. Tiba-tiba muncul pesan. Kok bisa?

Banyak orang pake website tiap hari tanpa pernah tau apa yang terjadi di balik layar. Buat developer, kamu butuh peta sederhana di kepala.

## Analogi: pesen kopi di kafe

Bayangin kamu lagi di kafe.

1. Kamu **datang ke meja** dan baca menu.
2. Kamu **pesan ke pelayan**.
3. Pelayan **bawa pesanan ke dapur**.
4. Dapur **bikin kopinya**.
5. Pelayan **bawa kopi balik ke meja**.

Website kerjanya persis kayak gitu. Cuma istilahnya beda.

## Tiga pemain utama

| Di kafe | Di web | Tugasnya |
| --- | --- | --- |
| Meja kamu | **Browser** | Tempat kamu lihat dan klik |
| Pelayan | **Internet** | Bolak-balik bawa pesan |
| Dapur | **Server** | Tempat data tersimpan, pesanan diproses |

Browser itu Chrome, Safari, Firefox, atau Edge. Server itu komputer di internet yang nyala 24 jam.

## Yang kejadian saat kamu buka google.com

Tiap kali kamu pencet Enter, alurnya kayak gini:

\`\`\`text
Kamu ketik "google.com" + Enter
        ↓
Browser ngomong: "Halo server Google, kasih halamanmu dong"
        ↓
Server Google jawab dengan kirim HTML, CSS, JavaScript
        ↓
Browser baca semua itu, terus susun jadi halaman yang kamu lihat
\`\`\`

Selesai. Itu doang. Tapi prosesnya cuma butuh sepersekian detik.

## Tiga bahasa yang bikin halaman

Halaman web dibangun dari tiga bahasa. Masing-masing punya tugas sendiri.

| Bahasa | Tugasnya | Analogi |
| --- | --- | --- |
| **HTML** | Struktur halaman: judul, paragraf, gambar | Kerangka rumah |
| **CSS** | Tampilan: warna, ukuran, spasi | Cat & furnitur |
| **JavaScript** | Interaksi: klik, animasi, validasi | Listrik & saklar |

Tiga ini selalu jalan bareng. Tanpa salah satu, halaman kerasa kurang.

## Kenapa kamu perlu tau ini

Sebagai developer kamu sering banget ketemu error. Tau bagiannya yang mana bikin debug jauh lebih cepet.

- Tampilan miring sebelah? Cek HTML & CSS.
- Tombol gak respon? Cek JavaScript.
- Halaman gak kebuka sama sekali? Cek server-nya.

Banyak pemula mikir error itu serem. Santai aja. Error itu cuma petunjuk yang ngasih tau "ada yang salah di sini".

## Coba sendiri

Buka browser. Pencet **F12**. Itu jendela ke balik layar website. Kamu bakal ketemu lagi tab itu nanti, sering banget.

Lesson selanjutnya kita masuk ke tiga bahasa wajibnya satu-satu.
`,
  },
  {
    slug: "html-css-js-itu-apa",
    title: "Tiga Bahasa Wajib: HTML, CSS, JS",
    duration: "9 menit",
    summary: "Kenalan singkat sama HTML, CSS, dan JavaScript.",
    content: `# Tiga Bahasa Wajib: HTML, CSS, JS

Lesson ini bukan buat hafalan. Tujuannya cuma satu: kasih kamu **gambaran** apa fungsi masing-masing bahasa.

Detailnya nanti kamu pelajarin pelan-pelan di roadmap. Sekarang yang penting kamu tau "yang mana ngapain".

## HTML — kerangka

HTML itu kayak nulis daftar belanja. Kamu nandain "ini judul", "ini paragraf", "ini link".

\`\`\`html
<h1>Halo, saya Acel</h1>
<p>Belajar coding dari nol.</p>
<a href="/about">Tentang saya</a>
\`\`\`

Tag \`<h1>\` artinya heading utama. \`<p>\` paragraf. \`<a>\` link. Browser baca tag-nya, terus tampilin sesuai aturan.

Itu doang HTML. Strukturnya, bukan tampilannya.

## CSS — gaya

Halaman tanpa CSS keliatan polos banget. Hitam putih, kayak Notepad.

CSS yang bikin halaman jadi **enak diliat**.

\`\`\`css
h1 {
  color: navy;
  font-size: 32px;
}

p {
  line-height: 1.6;
}
\`\`\`

Aturannya simpel: pilih elemen (\`h1\`, \`p\`), terus kasih tau browser mau dibikin gimana (warna apa, ukurannya berapa).

Kamu bisa ubah warna, font, jarak, layout, animasi — semua di CSS.

## JavaScript — interaksi

HTML bikin struktur. CSS bikin cantik. Tapi keduanya **diem aja**.

JavaScript yang bikin halaman bisa nanggepin user.

\`\`\`js
const tombol = document.querySelector("button");

tombol.addEventListener("click", () => {
  alert("Tombolnya kamu klik!");
});
\`\`\`

Kode di atas artinya: "kalau tombol diklik, munculin pesan 'Tombolnya kamu klik!'".

Tanpa JS, tombol cuma kotak yang gak ngapa-ngapain. Sama JS, tombol jadi hidup.

## Beda mereka, ringkesan

| Bahasa | Pertanyaan yang dijawab |
| --- | --- |
| HTML | "Ada apa aja di halaman ini?" |
| CSS | "Tampilannya gimana?" |
| JavaScript | "Kalau diklik, ngapain?" |

Tiga ini selalu jalan bareng. Mau pake framework apa pun nanti (React, Vue, Next.js), kamu tetep ketemu mereka.

## Urutan belajarnya

Saran realistis dari banyak developer:

1. **HTML** — beberapa hari, sampe bisa bikin halaman sederhana.
2. **CSS** — seminggu-dua, sampe paham layout.
3. **JavaScript** — paling lama, karena dia yang paling kompleks.

Jangan nyampur tiga sekaligus di awal. Nanti otaknya overload, dan biasanya pemula nyerah di sini.

Banyak yang ngerasa kebelet pengen langsung React. Tahan dulu. Tiga bahasa ini pondasinya. Tanpa ini, React kerasa magic — dan magic itu susah di-debug.
`,
  },
  {
    slug: "tools-developer",
    title: "Tools yang Dipakai Developer",
    duration: "7 menit",
    summary:
      "Tiga aplikasi yang bakal kamu buka tiap hari sebagai developer.",
    content: `# Tools yang Dipakai Developer

Sebelum nulis kode, kamu butuh beberapa alat. Kabar baiknya semuanya gratis dan ringan.

Lesson ini cuma kenalan. Setup detailnya nanti kamu kerjain pas masuk roadmap.

## Tiga tools utama

| Tools | Fungsinya | Analogi |
| --- | --- | --- |
| **VS Code** | Tempat nulis kode | Microsoft Word buat kode |
| **Chrome / Firefox / Edge** | Tempat lihat hasil | Layar TV |
| **Terminal** | Tempat ngetik perintah | Tombol remote |

Tiga ini bakal kamu buka **setiap hari**. Beneran tiap hari.

## VS Code

VS Code itu code editor paling populer sekarang. Bikinan Microsoft, gratis, ringan, dan dukung hampir semua bahasa.

Bedanya sama Notepad atau Word:

- **Ngewarnain kode** biar gampang dibaca.
- **Ngecek error** sambil kamu ngetik.
- **Ribuan ekstensi** buat bantu kerja.

Download di [code.visualstudio.com](https://code.visualstudio.com), install kayak aplikasi biasa.

> Banyak pemula mikir editor canggih bikin kerjaan lebih cepet. Sebenernya yang penting itu kamu nyaman pake satu editor sampe hafal jalannya. VS Code aman buat ini.

## Browser modern + DevTools

Pake Chrome, Firefox, atau Edge. Ketiganya punya **DevTools** yang dibuka pake **F12**.

DevTools itu jendela ke balik layar website. Di situ kamu bisa:

- Lihat struktur HTML halaman secara live.
- Edit CSS langsung dan lihat efeknya.
- Cek error JavaScript di tab Console.
- Lihat data yang dikirim ke server di tab Network.

Coba sekarang: buka halaman ini, pencet **F12**. Lihat yang muncul. Itu temen kamu seterusnya.

## Terminal

Terminal aplikasi yang nerima perintah lewat tulisan. Awal-awal keliatan serem, tapi sebenernya cuma butuh sedikit perintah.

| Perintah | Fungsi | Contoh |
| --- | --- | --- |
| \`cd\` | Pindah folder | \`cd belajar-web\` |
| \`ls\` (Mac/Linux) atau \`dir\` (Windows) | Lihat isi folder | \`ls\` |
| \`mkdir\` | Bikin folder baru | \`mkdir project-1\` |

Itu doang dulu. Sisanya nyusul pas kebutuhan muncul.

## Ekstensi VS Code yang ngebantu banget

Setelah install VS Code, install dua ini di tab Extensions (icon kotak di sidebar kiri):

- **Live Server** — auto-refresh halaman saat kamu save file. Wajib buat hari pertama belajar HTML.
- **Prettier** — auto-format kode biar rapi. Hemat banget.

Sisanya jangan dulu. Tools terlalu banyak di awal malah bikin bingung.

## Inget aja

Kamu gak perlu setup sekarang. Detailnya ada di halaman **Persiapan**. Lesson ini cuma kasih gambaran besar.

Yang penting: kamu udah tau apa yang bakal jadi temen harian kamu nanti.
`,
  },
  {
    slug: "git-dan-github",
    title: "Git & GitHub: Mesin Waktu buat Kode",
    duration: "10 menit",
    summary:
      "Kenapa developer gak nyimpen kode pake nama 'final-banget-fix-2'.",
    content: `# Git & GitHub: Mesin Waktu buat Kode

Pernah ngerjain dokumen Word terus nyimpen jadi \`tugas-final.docx\`, terus \`tugas-final-banget.docx\`, terus \`tugas-final-ASLI.docx\`?

Itu kacau. Dan dunia kode dulu juga gitu, sampe Git muncul.

## Apa itu Git

Git itu **tools yang nyatat semua perubahan** di kode kamu. Tiap kali kamu mau "nyimpen progress", kamu bikin satu **commit**.

Tiap commit itu kayak checkpoint di game. Kalau sesuatu rusak, kamu bisa balik ke checkpoint sebelumnya.

\`\`\`text
commit-1: bikin halaman home
   ↓
commit-2: tambah navbar
   ↓
commit-3: tambah footer
   ↓
commit-4: oops, footer-nya rusak
   ↓
[balik ke commit-3, semua aman lagi]
\`\`\`

Git jalan di komputer kamu. Gak butuh internet sama sekali.

## Apa itu GitHub

Git nyimpen riwayat di laptop kamu. Tapi gimana kalau laptop rusak?

GitHub itu layanan online buat **nyimpen Git project di internet**. Anggep kayak Google Drive, tapi khusus kode.

| Kalau laptop hilang | Tanpa GitHub | Pake GitHub |
| --- | --- | --- |
| Kode kamu | Hilang | Aman, tinggal download dari GitHub |
| Riwayat commit | Hilang | Aman juga |
| Portfolio | Susah ditunjukin | Bisa dilihat langsung dari profil |

GitHub gratis. Recruiter sering ngecek profil GitHub kamu sebelum interview.

## Tiga perintah harian

Kamu cuma butuh tiga ini buat 80% kerjaan:

\`\`\`bash
git add .
git commit -m "tambah halaman about"
git push
\`\`\`

| Perintah | Artinya |
| --- | --- |
| \`git add .\` | Tandain semua file yang berubah |
| \`git commit -m "..."\` | Bikin checkpoint sama pesan |
| \`git push\` | Kirim semua checkpoint ke GitHub |

Sisanya nyusul pelan-pelan.

## Pesan commit yang bagus

Pesan commit itu pesan dari kamu sekarang ke kamu di masa depan.

\`\`\`text
Jelek:
- "update"
- "fix"
- "wip"

Bagus:
- "perbaiki tombol login yang gak bisa diklik di mobile"
- "tambah validasi email di form register"
\`\`\`

Bayangin kamu balik ke project ini 3 bulan lagi. Pesannya harus bisa kamu pahami sendiri tanpa baca kode.

## Inget tiga hal ini aja

Git itu mesin waktu lokal. GitHub itu cloud-nya. Tiga perintah \`add\` → \`commit\` → \`push\` udah cukup buat hari pertama.

Detailnya nanti kamu pelajarin di roadmap. Yang penting sekarang kamu tau **kenapa** developer pake Git, bukan cuma cara pakenya.
`,
  },
  {
    slug: "deploy-dasar",
    title: "Deploy: Bedanya Localhost vs Live",
    duration: "8 menit",
    summary:
      "Kenapa kode yang jalan di laptop kamu gak otomatis bisa dibuka temen.",
    content: `# Deploy: Bedanya Localhost vs Live

Kasus klasik: kamu bikin website, jalan mulus di laptop sendiri. Kamu kirim link ke temen. Temen buka, tampilannya error.

Kamu cek lagi di laptop. Jalan. Kirim lagi. Tetep error di temen.

Penyebabnya hampir selalu satu hal: link-nya \`localhost\`.

## Apa itu localhost

\`localhost\` artinya **"komputer ini sendiri"**.

Saat kamu jalanin \`npm run dev\` atau pake Live Server, halaman kamu jalan di laptop kamu doang. URL \`http://localhost:3000\` itu cuma bisa dibuka di laptop yang lagi jalanin server-nya.

\`\`\`text
Laptop kamu                    Laptop temen
http://localhost:3000   ≠   http://localhost:3000
(nunjuk ke laptop kamu)     (nunjuk ke laptop dia, kosong)
\`\`\`

Wajar gak nyambung. Mereka beda komputer.

## Apa itu deploy

Deploy itu prosesnya **mindahin website kamu ke komputer di internet** yang nyala 24 jam (server).

Setelah ke-deploy, kamu dapet URL baru, contohnya:

\`\`\`text
https://nama-project.vercel.app
\`\`\`

URL ini bisa dibuka **siapa aja, dari device mana aja, di seluruh dunia**. Itu yang dimaksud "live di internet".

## Bedanya kayak gini

| Aspek | Localhost | Live (di-deploy) |
| --- | --- | --- |
| URL | \`http://localhost:3000\` | \`https://nama.vercel.app\` |
| Yang bisa akses | Cuma laptop kamu | Siapa aja, dari mana aja |
| Server-nya nyala kalau | Kamu nyalain manual | Selalu, 24 jam |
| Cocok buat | Ngoding, testing | Show ke user beneran |

## Platform deploy yang ramah pemula

Ada banyak platform, tapi tiga ini gratis dan paling gampang:

- **Vercel** — paling pas buat Next.js dan landing page modern. Tinggal connect GitHub, klik Deploy, beres.
- **Netlify** — alternatif Vercel, mirip cara kerjanya.
- **GitHub Pages** — gratis dari GitHub, cocok buat HTML/CSS statis.

Saran: kalau project pake Next.js atau React, pake **Vercel**. Kalau cuma HTML/CSS, pake **GitHub Pages** dulu.

## Alur deploy paling sederhana

\`\`\`text
Kode di laptop kamu
        ↓
git push ke GitHub
        ↓
Vercel deteksi push, build & deploy
        ↓
Dapet URL publik
        ↓
Share ke temen, mereka bisa buka
\`\`\`

Tunggu sekitar 1-2 menit, selesai.

## Auto-deploy: enaknya disini

Setelah pertama kali setup, kamu gak perlu deploy ulang manual. Tiap push baru ke GitHub, Vercel otomatis update.

\`\`\`text
Kamu edit kode di laptop
        ↓
git push
        ↓
30 detik kemudian: URL Vercel udah update
\`\`\`

Cara kerja kayak gini disebut **continuous deployment**. Kamu fokus ngoding, mereka urus sisanya.

## Pertama kali deploy bakal nempel

Banyak developer inget jelas momen pertama kali websitenya live. Lihat URL kamu sendiri, bisa dibuka dari HP siapapun — itu rasa yang nempel.

Kamu bakal ngerasain itu juga di roadmap nanti.
`,
  },
  {
    slug: "cara-belajar-efektif",
    title: "Cara Belajar yang Beneran Nempel",
    duration: "8 menit",
    summary:
      "Kebiasaan kecil yang bikin kamu konsisten dan gak gampang nyerah.",
    content: `# Cara Belajar yang Beneran Nempel

Belajar coding itu kayak lari maraton, bukan sprint 100 meter.

Yang penting bukan IQ tinggi atau jam belajar gila-gilaan. Yang penting **konsisten** dan tau cara belajar yang bener.

Lima aturan di bawah ini lebih ngebantu dari tutorial mana pun.

## Aturan #1 — ketik ulang, jangan copy-paste

Saat ikut tutorial, godaan terbesar itu copy-paste kode. Lebih cepet, kelihatan jalan, beres.

Tapi otak kamu **gak nyimpan apa-apa**. Besoknya kamu lupa total.

> Banyak yang nyangkut di sini. Belajar berbulan-bulan ngerasa udah ngerti, eh giliran disuruh nulis dari nol — bingung. Penyebabnya copy-paste melulu.

Ngetik ulang lambat di awal, tapi otak nyatat tiap karakter. Seminggu kemudian kamu bakal kerasa: "Kok udah otomatis ya?"

## Aturan #2 — error itu temen, bukan musuh

Pemula sering panik begitu lihat error merah. Padahal pesan error itu petunjuk yang udah dikasih gratis.

Format error standar:

\`\`\`text
[file]: script.js
[baris]: line 12
[masalah]: Uncaught SyntaxError: Unexpected token
\`\`\`

Tiga info itu udah cukup buat 90% kasus. Sisanya: copy pesan error ke Google. Pasti ada yang udah pernah nanya hal sama.

## Aturan #3 — bangun project, bukan ngabisin tutorial

Tutorial bagus buat ngenalin konsep. Tapi yang nempel itu bikin sendiri.

\`\`\`text
Project kecil yang selesai > project gede yang gak pernah kelar
\`\`\`

Habis lesson, coba bikin sesuatu yang lebih kecil pake materi yang barusan dipelajarin. Gak perlu sempurna. Yang penting jadi.

## Aturan #4 — sisihkan waktu rutin

30 menit tiap hari **lebih ampuh** dari 5 jam seminggu sekali. Otak butuh pengulangan biar inget.

| Pola belajar | Hasil setelah 1 bulan |
| --- | --- |
| 5 jam, sekali seminggu | Lupa terus, ngulang dari awal |
| 30 menit, tiap hari | Konsisten, nempel beneran |

Pilih jam yang paling tenang buat kamu. Pagi sebelum kerja, malem sebelum tidur, terserah. Konsistensi lebih penting dari durasi.

## Aturan #5 — jangan banding-bandingin

Di internet kamu bakal sering lihat orang yang katanya "belajar 3 bulan udah kerja".

Boleh termotivasi, jangan dijadiin ukuran. Setiap orang punya kecepatan sendiri.

Standar sehat yang bisa kamu pake: **kamu hari ini lebih ngerti dari kamu kemarin**. Itu udah cukup.

## Hal terakhir

Tools dan bahasa bisa dipelajarin kapan aja. Tapi mindset belajar yang sehat — itu yang nentuin kamu sampe mana.

Pelan-pelan aja. Tiap commit, tiap halaman yang jadi, tiap bug yang dipecahin — semuanya ngantar kamu ke titik yang lebih maju dari kemaren.

Habis lesson ini, kamu siap pilih spesialisasi: Frontend, Backend, atau Fullstack.
`,
  },
];

const MANUAL_ROLES: JalurRole[] = [
  {
    slug: "frontend",
    href: "/roadmap?path=frontend#html-css-dasar",
    badge: "Front-End",
    title: "Frontend Developer",
    tagline: "Yang dilihat & disentuh user.",
    description:
      "Bangun tampilan, animasi, dan interaksi yang user pakai langsung. Cocok kalau kamu suka detail visual dan UX.",
    bullets: [
      "HTML, CSS, JavaScript modern",
      "React, Next.js, Tailwind",
      "Responsive & dark mode",
    ],
    available: true,
  },
  {
    slug: "backend",
    href: "/roadmap?path=backend#backend-beginner",
    badge: "Back-End",
    title: "Backend Developer",
    tagline: "Otaknya aplikasi di balik layar.",
    description:
      "Bangun API, kelola database, dan jaga keamanan data. Cocok kalau kamu suka logika dan struktur data.",
    bullets: [
      "REST API & HTTP",
      "PostgreSQL, Prisma",
      "Auth & deployment",
    ],
    available: true,
  },
  {
    slug: "fullstack",
    href: "/roadmap?path=fullstack#fullstack-beginner",
    badge: "Full-Stack",
    title: "Fullstack Developer",
    tagline: "Generalis dua sisi.",
    description:
      "Gabungin frontend dan backend jadi satu produk utuh. Cocok kalau kamu suka kerja end-to-end.",
    bullets: [
      "Next.js + API routes",
      "Auth & owner-based access",
      "Deploy stack lengkap",
    ],
    available: true,
  },
];

// ─────────────────────────────────────────────────────────────────────
// Vibe fundamentals — 6 lessons.
// ─────────────────────────────────────────────────────────────────────

const VIBE_LESSONS: JalurLesson[] = [
  {
    slug: "apa-itu-vibe-coding",
    title: "Apa itu Vibe Coding",
    duration: "8 menit",
    summary:
      "Cara kerja baru: AI nulis kodenya, kamu pegang arahnya.",
    content: `# Apa itu Vibe Coding

Bayangin kamu punya asisten pribadi yang jago banget ngoding. Kamu tinggal bilang "saya mau bikin landing page kafe", dia langsung kerja.

Itu intinya vibe coding. **AI yang nulis kode**, kamu yang **pegang arah, taste, dan kualitas**.

Bukan berarti AI gantiin developer. Justru sebaliknya — kamu makin penting karena kamu yang nentuin AI mau dibawa ke mana.

## Bedanya sama coding biasa

| Coding tradisional | Vibe coding |
| --- | --- |
| "Gimana cara nulis logic ini?" | "Apa yang harus dibangun, dan kenapa?" |
| Hafal banyak syntax | Hafal sedikit, sisanya AI |
| Fokus ke baris kode | Fokus ke produk akhir |
| Lebih lambat tapi dalem | Lebih cepet tapi butuh ngarahin |

Dua-duanya valid. Vibe coding cuma cara baru — bukan pengganti.

## Yang perlu kamu kuasai

Vibe coding bukan jalan pintas. Tetep ada hal yang kamu **wajib paham**:

- Cara kerja web umum (browser, server, internet).
- Mana yang sisi browser, mana yang sisi server.
- Cara kerja database, minimal level dasar.
- Cara baca error dan tau di mana benerin.

> Banyak yang ngira vibe coding artinya gak perlu belajar dasar. Salah besar. Tanpa dasar, kamu bakal panik tiap AI ngasih hasil error — karena gak punya peta buat tau di mana yang salah.

## Kapan vibe coding pas dipake

Cocok banget buat:

- **MVP** yang harus jalan minggu ini, bukan bulan depan.
- **Side project** buat validasi ide.
- **Solo founder** yang shipping cepet tanpa tim.
- **Internal tools** yang butuh dibikin ringan.

Kurang cocok buat sistem mission-critical (rumah sakit, bank) yang butuh code review berlapis. Itu masih ranah engineer manual.

## Mindset yang sehat

Anggap AI itu **junior super produktif yang butuh diarahin**.

\`\`\`text
Kamu kasih perintah jelas      →  hasilnya bagus
Kamu malas mikir, asal nyuruh  →  hasilnya acak
\`\`\`

Kualitas output kamu = kualitas input kamu. Itu inti vibe coding.

## Realistis dari awal

Vibe coding gak bikin kamu langsung jago atau kaya. Yang dia kasih:

- Iterasi lebih cepet.
- Ide cepet jadi produk yang bisa dicoba user.
- Kamu fokus ke "apa", AI urus "gimana".

Sisanya — taste, problem solving, ngerti user — itu tetep kerjaan kamu, bukan AI.
`,
  },
  {
    slug: "cara-kerja-ai-coding",
    title: "Cara Kerja AI Coding",
    duration: "9 menit",
    summary:
      "AI bukan ajaib. Dia nebak kata berikutnya berdasarkan pola — dan itu kunci pakai-nya.",
    content: `# Cara Kerja AI Coding

Banyak orang anggap AI itu kayak otak yang ngerti semua. Padahal cara kerjanya jauh lebih sederhana dari yang kamu kira.

Paham cara kerjanya bikin kamu lebih jago pakenya.

## AI itu mesin tebak kata

Model kayak ChatGPT, Claude, atau Cursor — semuanya **belajar dari miliaran baris kode** yang udah ada di internet.

Cara kerjanya? Kamu kasih kalimat, AI **nebak kata berikutnya yang paling masuk akal** berdasarkan pola yang dia lihat.

\`\`\`text
Kamu ketik:  "Saya mau bikin tombol berwarna ..."
AI nebak:    "biru"   (paling sering muncul di pola "tombol berwarna ___")
\`\`\`

Itu doang. Cuma karena polanya banyak banget, hasilnya bisa keliatan kayak ngerti.

## Konsekuensi yang harus kamu inget

Karena cara kerjanya begitu, ada 3 hal yang sering bikin pemula nyangkut:

| Sifat AI | Artinya buat kamu |
| --- | --- |
| Suka ngarang | Jangan langsung percaya, selalu cek |
| Cuma sebagus konteks | Prompt vague = output vague |
| Gak tau project kamu | Wajib kasih konteks file |

## Halusinasi — masalah utama

Halusinasi itu istilah saat AI ngasih jawaban yang **kelihatan bener tapi salah**.

Contoh paling sering muncul:

- Manggil function yang **gak ada** di library.
- Ngarang nama field di API.
- Bikin import dari package yang **gak ada**.

Solusinya: jangan trust hasil mentah. Jalanin dulu kodenya. Kalau error, kasih error message-nya balik ke AI buat dibetulin.

> Vibe coder yang udah pengalaman gak panik pas AI salah. Mereka tau itu normal, dan iterasi terus sampe bener.

## Tools AI yang sering dipake

Ada tiga jenis besar:

| Jenis | Contoh | Cocok buat |
| --- | --- | --- |
| Chat AI | ChatGPT, Claude | Brainstorm, debug kode kecil |
| Editor AI | Cursor, Copilot | Edit kode langsung di project |
| AI builder | V0, Bolt, Lovable | Generate UI atau project utuh |

Yang paling sering dipake harian: **Cursor**. Karena dia gabungin chat + editor + akses ke seluruh project.

## AI itu pengganda, bukan pengganti

Engineer yang udah bagus, sama AI jadi 5x lebih produktif.

Engineer yang gak ngerti dasar, sama AI **tetep nyangkut** — karena gak bisa baca dan ngecek hasilnya.

\`\`\`text
Engineer bagus + AI = output 5x lipat
Engineer pemula tanpa dasar + AI = output ngarang yang gak ke-deteksi
\`\`\`

Pelajari dasar dengan baik. AI bakal jadi pengali, bukan pengganti otak kamu.

## Sederhana aja inget-nya

AI itu nebak pola. Hasilnya sebagus konteks yang kamu kasih. Selalu cek, jangan langsung percaya.

Sisanya — gimana cara nyusun konteks yang bagus — kita bahas di lesson selanjutnya.
`,
  },
  {
    slug: "cara-ngomong-ke-ai",
    title: "Cara Ngomong ke AI Biar Hasilnya Bagus",
    duration: "10 menit",
    summary:
      "Prompt jelek = output ngarang. Prompt jelas = output presisi.",
    content: `# Cara Ngomong ke AI Biar Hasilnya Bagus

Prompt itu kayak briefing ke karyawan baru.

\`\`\`text
Briefing jelas    →  hasilnya cepet sesuai
Briefing kabur    →  hasilnya juga ngawur
\`\`\`

Skill nulis prompt itu inti dari vibe coding. Beneran. Bukan tentang AI pintar mana — tentang gimana kamu ngomongnya.

## Anatomi prompt yang bagus

Prompt yang efektif punya empat bagian:

| Bagian | Isinya | Contoh |
| --- | --- | --- |
| **Konteks** | Kamu lagi ngapain | "Bikin landing page Next.js + Tailwind" |
| **Goal** | Apa yang mau dihasilin | "Component Hero" |
| **Spesifikasi** | Detail teknis | "File \`components/Hero.jsx\`, headline + 2 tombol" |
| **Constraint** | Apa yang gak boleh | "Jangan pake kata 'amazing' atau 'stunning'" |

## Bandingin dua prompt ini

**Prompt jelek:**

> Bikinin hero yang bagus.

**Prompt bagus:**

> Saya lagi bikin landing page Next.js + Tailwind buat toko kopi. Tolong bikin component Hero di file \`components/Hero.jsx\`. Hero punya headline besar, subheadline 1 kalimat, dan 2 tombol (utama biru, sekunder outline). Pake bahasa Indonesia santai. Hindari kata "amazing" atau "stunning".

Yang mana hasilnya lebih dekat sama yang kamu mau? Yang kedua, jelas.

## Hindari kata samar

Kata-kata yang kerasa "bagus" tapi sebenernya **gak ngasih info apa-apa**:

| Samar (jangan) | Konkret (pake ini) |
| --- | --- |
| "Bikin yang keren" | "Pake spacing lega, padding 96px" |
| "Bikin yang modern" | "Dark mode, accent biru, satu font" |
| "Bikin yang profesional" | "Border radius 12px, hover halus" |

Kalimat samar = AI nebak sendiri = hasilnya generic.

## Iterasi, bukan one-shot

AI **jarang** ngasih hasil sempurna di percobaan pertama. Itu normal.

Strateginya:

1. Kasih prompt awal yang detail.
2. Lihat hasilnya.
3. Identifikasi yang masih kurang.
4. Kasih feedback **spesifik**: "Tombol kedua kekecilan, padding-nya tambahin". Bukan: "Masih kurang oke."
5. Ulangi sampe pas.

\`\`\`text
Prompt awal → hasil 1 → feedback → hasil 2 → feedback → hasil OK
\`\`\`

Vibe coder bagus bisa iterasi cepet karena tau cara nyusun feedback yang konkret.

## Kasih konteks file kalau perlu

Di Cursor, kamu bisa drag file ke chat atau pake \`@filename\`. Itu ngasih AI akses ke isi file beneran.

\`\`\`text
Tanpa konteks file:
  AI nebak struktur project = sering meleset
  
Sama konteks file:
  AI baca file beneran = nyesuaiin sama kode existing
\`\`\`

Kebiasaan yang sehat: tiap minta edit file, kasih juga file yang nyangkut.

## Jangan males nulis

Prompt panjang yang detail itu **investasi waktu**.

\`\`\`text
5 menit nulis prompt detail   →  hasil sekali jadi
1 menit nulis prompt singkat  →  bolak-balik 30 menit revisi
\`\`\`

Vibe coding bukan tentang shortcut. Tentang **cara baru kerja yang butuh komunikasi jelas** sama AI sebagai partner.

## Ringkasan formula

Tiap kali kasih prompt, cek empat hal:

- Udah ada **konteks**?
- Udah jelas **goal**-nya?
- Udah kasih **spesifikasi** detail?
- Udah sebut **constraint** yang penting?

Kalau iya semua, prompt kamu udah siap kirim.
`,
  },
  {
    slug: "workflow-build-cepat",
    title: "Workflow Build Cepat dengan AI",
    duration: "10 menit",
    summary:
      "Cara kerja sehari-hari vibe coder: dari ide ke aplikasi yang live.",
    content: `# Workflow Build Cepat dengan AI

Pernah lihat orang bikin landing page dari ide jadi live cuma dalam 1 jam? Itu bukan magic. Itu workflow.

Ini langkah yang biasa dipake vibe coder produktif.

## Alur 6 langkah

\`\`\`text
1. Tulis ide singkat di notes
        ↓
2. Generate skeleton di V0 atau Cursor
        ↓
3. Iterasi visual di Cursor
        ↓
4. Push ke GitHub
        ↓
5. Deploy ke Vercel
        ↓
6. Update otomatis tiap push baru
\`\`\`

Ayo bedah satu-satu.

## Step 1 — Tulis ide singkat

Sebelum buka editor, tulis dulu di notes 3-5 baris:

- App ini buat siapa?
- Masalah apa yang dipecahin?
- Tampilan utama yang dibutuhin?

Ini jadi acuan tiap kali kamu prompt AI nanti. Tanpa ini, kamu bakal lupa arah di tengah jalan.

## Step 2 — Generate skeleton

Buka **V0** atau **Cursor**. Kasih prompt yang bangun struktur dasar.

Contoh prompt buat V0:

> Bikin landing page Next.js + Tailwind. Section: hero, fitur (3 card), testimoni, footer. Dark mode. Accent biru. Bahasa Indonesia.

V0 bakal kasih kode yang bisa langsung kamu pake. Salin ke project Cursor.

## Step 3 — Iterasi visual

Sekarang kamu di Cursor sama kode awal. Buka di browser pake \`npm run dev\`.

Lihat hasilnya. Identifikasi yang kurang oke. Pake **Cmd+K** atau **Ctrl+K** di Cursor buat minta revisi spesifik:

- "Spacing di hero kekecilan, naikin py-32"
- "Kartu fitur kurang lega, padding p-8"
- "Tombol primary terlalu pucat, ganti biru lebih gelap"

Iterasi sampe puas.

## Step 4 — Push ke GitHub

Setelah versi lokal udah enak:

\`\`\`bash
git init
git add .
git commit -m "init: landing page toko kopi"
git remote add origin https://github.com/USERNAME/landing-kopi.git
git push -u origin main
\`\`\`

Bingung? Tanya ke Cursor: "Tolong setup git buat project ini dan push ke repo \`landing-kopi\`."

## Step 5 — Deploy ke Vercel

Buka [vercel.com/new](https://vercel.com/new). Login pake GitHub. Pilih repo. Klik Deploy.

Tunggu 1-2 menit. Dapet URL publik. Selesai.

## Step 6 — Update otomatis

Tiap push baru ke GitHub, Vercel auto-redeploy. Gak perlu klik apapun.

\`\`\`bash
# Workflow harian setelah app live:
git add .
git commit -m "perbaiki padding hero"
git push

# 30 detik kemudian: URL Vercel udah update
\`\`\`

## Estimasi waktu realistis

Buat landing page sederhana:

| Step | Waktu |
| --- | --- |
| 1-2 (ide + generate) | ~15 menit |
| 3 (iterasi visual) | 30-60 menit |
| 4-5 (push + deploy) | ~15 menit |
| **Total** | **1-2 jam dari nol ke live** |

Buat app yang lebih kompleks (ada database & auth), tambah 2-4 jam. Tetep lebih cepet dari coding manual.

## Yang gak diperlihatin di video

Workflow di atas keliatan smooth. Realitanya selalu ada momen kayak gini:

- AI ngasih kode yang error → kasih error message ke AI → dibetulin.
- Library belum ke-install → install manual.
- Konflik versi → googling 5 menit.

> Itu normal banget. Vibe coder yang bagus bukan yang gak pernah error — tapi yang **cepet pulih dari error**.

## Yang harus kamu inget

Workflow ini bukan rigid. Lama-lama kamu bakal ketemu pola sendiri yang lebih cocok. Yang penting: kamu paham ada **alurnya yang berulang**, bukan asal coba-coba.
`,
  },
  {
    slug: "tools-ai-modern",
    title: "Tools AI Modern Vibe Coder",
    duration: "8 menit",
    summary:
      "Senjata harian yang bakal kamu pake setiap hari.",
    content: `# Tools AI Modern Vibe Coder

Semua tools di sini gratis di tier dasar. Cukup buat pemula sampe pro level menengah.

Kabar baiknya: kamu **gak perlu** install semua. Mulai dari tiga utama dulu.

## Tiga tools wajib pemula

| Tools | Fungsi utama | Kapan dipake |
| --- | --- | --- |
| **Cursor** | Editor sama AI built-in | Tiap hari, pas ngoding |
| **Claude / ChatGPT** | Chat AI buat brainstorm | Pas mikir arsitektur, debug |
| **Vercel** | Deploy otomatis | Pas mau publish |

Cuma tiga ini. Yang lain nyusul kalau udah nyaman.

## Cursor — editor utama

Cursor itu VS Code yang udah dimodif buat AI. Tampilannya sama, tapi punya:

- **Chat AI** di sisi kanan editor.
- **Cmd+K** (atau Ctrl+K) buat edit kode pake bahasa biasa.
- **Composer mode** buat task multi-file.

Kalau cuma boleh punya satu tool, pilih ini.

Download di [cursor.com](https://cursor.com).

## ChatGPT atau Claude — chat AI

Buat hal yang lebih panjang atau abstrak:

- Diskusi arsitektur sebelum mulai coding.
- Brainstorm fitur.
- Belajar konsep baru.
- Debug error yang panjang.

| Pilihan | Kelebihan |
| --- | --- |
| **Claude** ([claude.ai](https://claude.ai)) | Lebih jago coding panjang, output rapi |
| **ChatGPT** ([chat.openai.com](https://chat.openai.com)) | Lebih merata, ekosistem plugin gede |

Versi gratis udah cukup buat awal. Upgrade kalau udah sering banget pake.

## Tools tambahan (bukan wajib)

Setelah tiga di atas nyaman, kamu bisa nambah:

- **V0** ([v0.dev](https://v0.dev)) — generate UI dari teks. Cocok buat eksplorasi visual cepet.
- **Bolt** ([bolt.new](https://bolt.new)) atau **Lovable** ([lovable.dev](https://lovable.dev)) — generate app utuh dari prompt. Cocok buat prototype.
- **GitHub Copilot** — autocomplete pintar. Banyak dilewat sekarang karena Cursor udah punya yang mirip.

> Kebanyakan tool di awal malah bikin bingung. Mulai dari tiga utama, kuasai dulu, baru tambahin.

## Kapan pake mana

Pertanyaan yang sering muncul: "Kalau Cursor udah bisa chat, kenapa masih perlu Claude?"

Jawabannya:

- **Cursor** kuat saat lagi di project. Edit kode, baca file, run command.
- **Claude/ChatGPT** kuat saat **belum mulai coding**. Brainstorm, plan arsitektur, belajar konsep.

\`\`\`text
Brainstorm ide      →  ChatGPT/Claude
Plan arsitektur     →  ChatGPT/Claude
Mulai coding        →  Cursor
Debug pas coding    →  Cursor
Deploy              →  Vercel
\`\`\`

Tiap tool punya tempatnya.

## Inget aja

Tools itu cuma alat. Yang nentuin output kamu **cara mikir kamu**, bukan tools-nya.

Ada yang punya akses ke 10 tools premium tapi outputnya generic. Ada yang cuma pake Cursor tapi shipping app yang dipake ribuan orang.

Yang ngebedain: cara mikir, taste, dan kebiasaan kerja. Tools tinggal nyusul.
`,
  },
  {
    slug: "mindset-builder",
    title: "Mindset Builder, Bukan Sekadar Coder",
    duration: "9 menit",
    summary:
      "Vibe coder yang sukses bukan yang paling jago AI, tapi yang paling jago bikin produk.",
    content: `# Mindset Builder, Bukan Sekadar Coder

Coding itu satu skill. Bikin produk itu skill yang lain.

Vibe coding ngebantu kamu di sisi **coding**. Tapi yang bikin sukses itu sisi **produk**.

## Beda coder dan builder

| Coder | Builder |
| --- | --- |
| "Gimana cara bikin ini jalan?" | "Apakah ini worth dibikin?" |
| Fokus ke kode | Fokus ke user |
| Bisa bikin app technically perfect | Bisa bikin app yang dipake |
| Senang pas kode-nya rapi | Senang pas user-nya nambah |

Coder hebat bisa bikin app perfect tapi gak ada yang pake. Builder hebat bikin app berantakan tapi banyak yang suka.

Tujuannya jadi keduanya. Tapi kalau harus pilih satu di awal — pilih **builder**.

## Pertanyaan yang harus kamu tanya tiap kali mau project

Sebelum buka editor, jawab dulu di notes:

- Siapa yang bakal pake ini?
- Masalah apa yang mereka punya sekarang?
- Kenapa mereka bakal pake punya kamu, bukan yang lain?
- Apa indikator sukses-nya? (1000 user? 10 paying customer? Hilangnya satu masalah personal?)

> Banyak orang skip pertanyaan ini dan langsung coding. Hasilnya: project yang technically jalan tapi gak ada yang butuh. Sayang banget waktunya.

## Ship cepet, dengerin user

Mindset bahaya di pemula: **mau perfect dulu** sebelum show ke orang.

Realitanya: kamu **gak akan** pernah tau apa yang user mau sampe mereka coba. Yang ada di kepala kamu cuma tebakan.

\`\`\`text
Bulan 1-12: ngoding sendiri di laptop
              vs
Bulan 1: ship versi malu-maluin → 5 user nyoba
Bulan 2: dengerin feedback, update
Bulan 3: udah punya 50 user beneran
\`\`\`

Versi ke-2 jauh lebih cepet belajar.

## Refactor itu mahal

Tiap kali kamu mau "rapihin kode" sebelum ship, tanya: **kode itu bakal kepake gak?**

50% project yang kamu bikin di awal bakal di-throw away. Refactor di kode yang gak kepake itu **buang waktu**.

Tunggu sampe sebuah project terbukti penting (banyak user, atau kamu pake setiap hari), baru investasi waktu buat polish.

## Belajar dari user, bukan tutorial

Setelah punya app yang dipake walau cuma 5 orang — feedback mereka **100x lebih berharga** dari tutorial mana pun.

User bakal nunjukin:

- Hal yang kamu pikir "obvious" ternyata bingung.
- Fitur yang kamu pikir penting ternyata gak ada yang pake.
- Bug yang kamu gak sadar.
- Permintaan fitur yang gak kepikiran.

## Realistis tentang vibe coding

Vibe coding bikin building lebih **cepet**. Tapi gak bikin building lebih **gampang**.

Kamu masih harus mikir tentang:

- User mana yang kamu target.
- Fitur mana yang prioritas.
- Tradeoff yang harus diambil.

AI **gak ngerti** konteks personal kamu, partner kamu, atau target market kamu.

Yang bikin kamu menonjol bukan **akses ke AI**. Tapi kemampuan **pake AI buat build something that matters**. Itu skill yang harus dilatih.

## Habis lesson ini

Kamu udah punya pondasi mental vibe coder yang sehat. Selanjutnya kamu bisa:

- Lanjut ke **roadmap Vibe Coding lengkap** buat materi level lanjutan.
- Atau pilih salah satu **role** yang fokusnya lebih spesifik.

Sampe ketemu di lesson berikutnya. Pelan-pelan aja, yang penting konsisten.
`,
  },
];

const VIBE_ROLES: JalurRole[] = [
  {
    slug: "prompt-architect",
    href: "/roadmap/vibe/prompt-architect",
    badge: "AI Prompt",
    title: "AI Prompt Architect",
    tagline: "Sutradara di balik layar AI.",
    description:
      "Spesialis ngomong sama AI. Tau gimana nyusun prompt yang hasilnya konsisten, memimpin AI buat ngerjain task multi-step.",
    bullets: [
      "Prompt engineering lanjutan",
      "Multi-step task orchestration",
      "Reusable prompt library",
    ],
    available: false,
  },
  {
    slug: "product-curator",
    href: "/roadmap/vibe/product-curator",
    badge: "Product & UX",
    title: "Product & UX Curator",
    tagline: "Jaga rasa & arah produk.",
    description:
      "Fokus ke design taste dan user experience. AI yang generate, kamu yang nentuin mana yang masuk dan mana yang dibuang.",
    bullets: [
      "Design critique & polish",
      "User journey mapping",
      "Output AI yang siap dipake user",
    ],
    available: false,
  },
  {
    slug: "code-reviewer",
    href: "/roadmap/vibe/code-reviewer",
    badge: "Code Review",
    title: "Code Reviewer & Debugger",
    tagline: "Mata kedua untuk kode AI.",
    description:
      "Ngecek output AI sebelum dipake. Tau kapan kode AI bagus, kapan harus ditolak, kapan harus minta revisi.",
    bullets: [
      "Spot common AI bugs",
      "Security & performance review",
      "Test strategy untuk kode AI",
    ],
    available: false,
  },
  {
    slug: "solo-founder",
    href: "/roadmap/vibe/solo-founder",
    badge: "Indie Hacker",
    title: "Solo Founder / Indie Hacker",
    tagline: "Build, ship, monetize sendirian.",
    description:
      "Akhir dari jalan vibe coder: bikin produk sendiri, deploy, dapet user, monetize. Kombinasi semua skill plus business.",
    bullets: [
      "MVP to revenue dalam minggu",
      "Marketing & distribution dasar",
      "Stripe, analytics, support",
    ],
    available: false,
  },
];

// ─────────────────────────────────────────────────────────────────────
// Public meta object — used by pages.
// ─────────────────────────────────────────────────────────────────────

export const JALUR_META: Record<JalurPath, JalurMeta> = {
  manual: {
    path: "manual",
    badge: "Manual Coding",
    badgeTone: "accent",
    eyebrow: "Manual Coding Fundamentals",
    title: "Belajar dari dasarnya, biar tahan lama.",
    subtitle:
      "Pondasi yang kuat itu modal sepanjang karir. Kita kenalan dulu sama cara kerja web, tools developer, dan kebiasaan belajar yang sehat — sebelum pilih spesialisasi.",
    tagline: "Six fundamentals · clean foundation",
    intro:
      "Selesain enam lesson di bawah ini sebelum masuk ke roadmap. Total sekitar 1 jam baca santai. Setelah itu kamu pilih mau spesialis di Frontend, Backend, atau Fullstack.",
    setupHref: "/persiapan",
    setupCtaLabel: "Setup tools dulu",
    fullRoadmapHref: "/roadmap",
    fullRoadmapLabel: "Lihat roadmap manual lengkap",
    roleSectionTitle: "Sudah selesai fundamentals? Pilih spesialisasi.",
    roleSectionSubtitle:
      "Tiga jalur, masing-masing punya roadmap level lengkap. Kamu bisa pindah jalur kapan saja.",
    lessons: MANUAL_LESSONS,
    roles: MANUAL_ROLES,
  },
  vibe: {
    path: "vibe",
    badge: "Vibe Coding",
    badgeTone: "sky",
    eyebrow: "Vibe Coding Fundamentals",
    title: "Build cepet bareng AI, tapi tetap dengan arah.",
    subtitle:
      "Vibe coding bukan jalan pintas. Ini cara kerja baru — kamu yang pegang arah, AI yang bantu eksekusi. Kita bahas fondasinya dulu sebelum kamu masuk ke roadmap atau pilih role yang lebih spesifik.",
    tagline: "Six fundamentals · realistic AI workflow",
    intro:
      "Enam lesson di bawah ini biar kamu nggak tersesat di hype AI. Total sekitar 1 jam baca santai. Habis itu kamu boleh masuk ke roadmap level Vibe Coding, atau pilih role yang fokusnya lebih spesifik.",
    setupHref: "/persiapan/vibe",
    setupCtaLabel: "Setup tools AI dulu",
    fullRoadmapHref: "/roadmap/vibe",
    fullRoadmapLabel: "Lihat roadmap Vibe Coding lengkap",
    roleSectionTitle: "Atau pilih role yang lebih spesifik.",
    roleSectionSubtitle:
      "Empat role di bawah ini sedang disiapkan. Roadmap-nya akan dirilis bertahap.",
    lessons: VIBE_LESSONS,
    roles: VIBE_ROLES,
  },
};

export function getJalurMeta(path: string): JalurMeta | null {
  if (path === "manual" || path === "vibe") return JALUR_META[path];
  return null;
}

export function getJalurLesson(
  path: JalurPath,
  slug: string,
): JalurLesson | null {
  const meta = JALUR_META[path];
  return meta.lessons.find((l) => l.slug === slug) ?? null;
}

export function getAllJalurPaths(): { path: JalurPath; slug: string }[] {
  const out: { path: JalurPath; slug: string }[] = [];
  (Object.keys(JALUR_META) as JalurPath[]).forEach((p) => {
    JALUR_META[p].lessons.forEach((l) => out.push({ path: p, slug: l.slug }));
  });
  return out;
}
