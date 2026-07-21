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
    duration: "9 menit",
    summary:
      "Apa yang sebenarnya terjadi saat kamu mengetik URL dan menekan Enter.",
    content: `# Cara Kerja Website

Banyak orang pakai website tiap hari tanpa pernah tahu apa yang terjadi di baliknya. Saat kamu mau jadi developer, kamu butuh peta mental yang sederhana.

Anggap aja website itu kayak restoran. Kamu duduk di meja, baca menu, pesan ke pelayan. Pelayan bawa pesanan ke dapur. Dapur masak, lalu pelayan bawa balik makanan ke meja kamu.

Web kerja persis kayak gitu. Cuma istilahnya beda.

## Browser, server, dan internet

- **Browser** itu meja kamu. Tempat kamu lihat, klik, dan ngetik. Chrome, Safari, Firefox itu semua browser.
- **Server** itu dapur. Komputer yang nyala 24 jam, nyimpan halaman dan data. Kamu nggak pernah lihat langsung.
- **Internet** itu jalan antara meja dan dapur. Kabel, WiFi, jaringan operator semuanya nyatu jadi internet.

Saat kamu ketik \`google.com\` lalu pencet Enter, browser kamu kirim "permintaan" ke server Google. Server jawab dengan kode HTML, CSS, dan JavaScript. Browser baca semua itu, lalu nampilin halaman yang kamu lihat.

## Tiga bahasa yang bikin halaman web

- **HTML** — kerangka. Ini judulnya, ini paragraf, ini gambar. Kayak struktur rumah.
- **CSS** — gaya. Warna, spasi, font, layout. Kayak cat dan furnitur.
- **JavaScript** — interaksi. Tombol diklik ngapain, animasi, validasi form. Kayak listrik di rumah.

Tiga ini selalu jalan barengan. Tanpa salah satu, halaman terasa kurang.

## Kenapa kamu perlu paham ini

Sebagai developer kamu sering banget ketemu error. Tau bagiannya yang mana bikin debugging jauh lebih cepet.

- Tampilan rusak? Kemungkinan di HTML atau CSS.
- Tombol nggak respon? Kemungkinan di JavaScript.
- Halaman nggak kebuka sama sekali? Kemungkinan server-nya yang lagi bermasalah.

Mulai sekarang, tiap kali buka website, coba pikirin: "Yang ini browser tampilin apa? Yang dari server apa?". Lama-lama jadi otomatis.
`,
  },
  {
    slug: "html-css-js-itu-apa",
    title: "HTML, CSS, JS — Tiga Bahasa Wajib",
    duration: "10 menit",
    summary: "Kenalan singkat dengan tiga bahasa dasar yang membentuk web.",
    content: `# HTML, CSS, JS — Tiga Bahasa Wajib

Tiga bahasa ini jadi pondasi semua website. Mau pake framework apa pun nanti, kamu tetep ketemu mereka.

Kabar baiknya: kamu nggak perlu hafal semuanya. Cukup paham fungsi masing-masing dan kapan dipakai.

## HTML — kerangka halaman

HTML singkatan dari Hypertext Markup Language. Tugasnya cuma satu: nentuin **struktur** halaman.

\`\`\`html
<h1>Selamat Datang</h1>
<p>Ini paragraf pertama saya.</p>
<a href="/about">Tentang saya</a>
\`\`\`

Tag \`<h1>\` artinya heading utama. \`<p>\` artinya paragraf. \`<a>\` artinya link. Browser baca tag ini terus nampilin sesuai aturannya.

## CSS — gaya halaman

CSS singkatan dari Cascading Style Sheets. Tugasnya bikin halaman **tampak menarik**.

\`\`\`css
h1 {
  color: navy;
  font-size: 32px;
}

p {
  line-height: 1.6;
}
\`\`\`

CSS milih elemen (heading, paragraf, dll), lalu ngasih aturan visual. Warna, ukuran, jarak, semua di sini.

## JavaScript — perilaku halaman

JavaScript bikin halaman jadi **bisa berinteraksi** sama user.

\`\`\`js
const tombol = document.querySelector("button");

tombol.addEventListener("click", () => {
  alert("Tombolnya kamu klik!");
});
\`\`\`

Tanpa JS, halaman cuma teks dan gambar diam. Dengan JS, halaman bisa nanggepin klik, ngirim data ke server, dan update tampilan tanpa reload.

## Urutan belajarnya

Saran realistis: HTML dulu beberapa hari, lanjut CSS, baru JavaScript. Jangan campur aduk di awal — fokus satu bahasa biar otaknya nggak overload.

Setelah ketiga ini lancar, framework kayak React, Vue, atau Next.js bakal jauh lebih masuk akal. Mereka semua dibangun di atas tiga bahasa ini.
`,
  },
  {
    slug: "tools-developer",
    title: "Tools yang Dipakai Developer",
    duration: "8 menit",
    summary:
      "Editor, browser, dan terminal — tiga aplikasi yang akan jadi rumah keduamu.",
    content: `# Tools yang Dipakai Developer

Sebelum nulis kode, kamu butuh beberapa alat. Tenang, semuanya gratis dan ringan.

## VS Code — tempat nulis kode

VS Code itu code editor paling populer sekarang. Ringan, gratis, dan dukung hampir semua bahasa.

Kenapa bukan Notepad? Karena VS Code:

- Ngewarnain kode biar gampang dibaca.
- Ngecek error sambil kamu ngetik.
- Punya ribuan ekstensi buat ngebantu kerja.

Download di [code.visualstudio.com](https://code.visualstudio.com). Install kayak aplikasi biasa.

## Browser modern — tempat lihat hasil

Pake Chrome, Firefox, atau Edge. Ketiganya punya **DevTools** — fitur buat developer yang dibuka pake tombol F12.

DevTools bakal nemenin kamu setiap hari. Di situ kamu bisa:

- Lihat HTML & CSS halaman secara langsung.
- Ngecek error di Console.
- Lihat request yang dikirim ke server.

Kalo belum pernah, coba pencet F12 di halaman manapun. Itu jendela ke "balik layar" website.

## Terminal — tempat ngetik perintah

Terminal itu aplikasi yang nerima perintah lewat tulisan. Di Windows namanya Command Prompt atau PowerShell. Di Mac/Linux namanya Terminal.

Awalnya kelihatan serem, tapi kamu cuma butuh sedikit perintah:

- \`cd folder-nama\` — pindah ke folder.
- \`ls\` (Mac/Linux) atau \`dir\` (Windows) — lihat isi folder.
- \`mkdir folder-baru\` — bikin folder baru.

Nanti pas install Node.js, kamu juga akan pake terminal buat install paket dan jalanin project.

## Ekstensi VS Code yang membantu

Setelah install VS Code, install dua ini di tab Extensions:

- **Live Server** — auto-refresh halaman saat kamu save file. Wajib buat hari pertama belajar HTML.
- **Prettier** — auto-format kode biar rapih. Hemat waktu banget.

Sisanya boleh nyusul pas kebutuhan muncul. Jangan kebanyakan install di awal — cukup yang dipake aja.
`,
  },
  {
    slug: "git-dan-github",
    title: "Git & GitHub — Simpan Kerjaan dengan Aman",
    duration: "11 menit",
    summary:
      "Git itu mesin waktu untuk kode. GitHub itu tempat menyimpan dan berbagi.",
    content: `# Git & GitHub — Simpan Kerjaan dengan Aman

Pernah ngerjain dokumen lalu nge-save \`tugas-final.docx\`, terus \`tugas-final-banget.docx\`, terus \`tugas-final-ASLI.docx\`? Kekacauan.

Git muncul buat ngatasin masalah ini di dunia kode.

## Apa itu Git

Git adalah tools yang nyatat semua perubahan di kode kamu. Setiap kali kamu mau "nyimpan progress", kamu bikin **commit**. Tiap commit kayak checkpoint di game.

Kamu bisa lihat siapa ngubah apa, kapan, dan kenapa. Kalo sesuatu rusak, kamu bisa balik ke versi sebelumnya yang masih jalan.

Git jalan di komputer kamu. Nggak butuh internet sama sekali.

## Apa itu GitHub

GitHub adalah layanan online buat **nyimpen dan berbagi** kode yang udah dipantau Git. Kayak Google Drive, tapi khusus kode.

Manfaatnya:

- Kalo laptop kamu rusak, kode tetap aman.
- Kamu bisa kerja dari device lain, tinggal pull ke laptop baru.
- Recruiter bisa lihat portfolio kamu lewat profil GitHub.

GitHub gratis. Semua project ini bisa kamu push ke akun pribadi.

## Tiga perintah yang dipake tiap hari

\`\`\`bash
git add .
git commit -m "tambah halaman about"
git push
\`\`\`

- \`git add .\` — tandain semua perubahan buat masuk commit.
- \`git commit -m "..."\` — bikin checkpoint dengan pesan singkat.
- \`git push\` — kirim semua commit ke GitHub.

Tiga ini doang udah cukup buat 80% kerjaan harian. Sisanya nyusul.

## Tips pesan commit yang bagus

Pesan commit jelekin kerjaan diri sendiri di masa depan kalo asal. Tulis yang spesifik:

- Jelek: "update", "fix", "wip"
- Bagus: "perbaiki tombol login yang nggak bisa diklik di mobile"

Bayangin kamu balik ke project ini 3 bulan lagi. Pesannya harus bisa kamu pahami sendiri tanpa baca kode.

## Nggak perlu dihafal sekarang

Lesson ini cuma pengantar. Kamu nggak perlu langsung jago Git. Yang penting:

- Tau Git itu mesin waktu, GitHub itu cloud-nya.
- Tau ada \`add\`, \`commit\`, \`push\` sebagai siklus harian.
- Mulai biasakan commit sering — tiap kali nyelesain satu fitur kecil.
`,
  },
  {
    slug: "deploy-dasar",
    title: "Deploy Dasar — Bedanya Localhost & Live",
    duration: "9 menit",
    summary:
      "Kenapa kode yang jalan di laptop tidak otomatis bisa dibuka orang lain.",
    content: `# Deploy Dasar — Bedanya Localhost & Live

Banyak pemula bingung kenapa websitenya jalan di laptop sendiri tapi nggak bisa dibuka temen pas dikirim link-nya. Jawabannya satu: link-nya \`localhost\`.

## Apa itu localhost

\`localhost\` artinya "komputer ini sendiri". Saat kamu pake \`npm run dev\` atau Live Server, halaman kamu jalan di laptop kamu doang.

Kalo kamu kirim link \`http://localhost:3000\` ke temen, di laptop temen link itu nunjuk ke laptop temen, bukan kamu. Wajar nggak nyambung.

## Apa itu deploy

Deploy itu prosesnya **mindahin website kamu ke komputer di internet** yang nyala 24 jam. Komputer itu disebut server.

Setelah ke-deploy, kamu dapet URL baru, contohnya:

\`\`\`
https://nama-project.vercel.app
\`\`\`

URL ini bisa dibuka siapa aja, dari device manapun, di seluruh dunia. Itu yang dimaksud "live di internet".

## Platform yang sering dipake

Untuk awal-awal, pakai yang gampang. Tiga ini gratis dan cocok buat pemula:

- **Vercel** — paling pas buat project Next.js dan landing page modern. Tinggal connect GitHub, push, beres.
- **Netlify** — mirip Vercel, alternatif yang juga populer.
- **GitHub Pages** — gratis dari GitHub, cocok buat HTML/CSS statis.

Saran: mulai dari Vercel kalau projectnya pake Next.js atau React. Mulai dari GitHub Pages kalau cuma HTML/CSS.

## Alur deploy paling sederhana

1. Push project ke GitHub (lihat lesson Git & GitHub).
2. Buka Vercel atau Netlify, login pakai akun GitHub.
3. Pilih repo project kamu.
4. Klik "Deploy".
5. Tunggu sekitar 1-2 menit.
6. Dapet URL publik, share ke siapa aja.

Pertama kali deploy biasanya bikin senang banget. Kamu lihat URL kamu sendiri, hidup di internet, bisa dibuka dari HP. Itu momen yang nempel.

## Setelah ke-deploy

Setiap kali kamu push perubahan baru ke GitHub, Vercel/Netlify otomatis update versinya. Nggak perlu deploy ulang manual.

Cara kerja kayak gini disebut **continuous deployment**. Kamu fokus nulis kode, mereka urus sisanya.
`,
  },
  {
    slug: "cara-belajar-efektif",
    title: "Cara Belajar Coding yang Efektif",
    duration: "8 menit",
    summary:
      "Kebiasaan kecil yang bikin progress kamu konsisten dan nggak gampang nyerah.",
    content: `# Cara Belajar Coding yang Efektif

Belajar coding itu maraton, bukan sprint. Kuncinya bukan IQ tinggi atau jam belajar gila-gilaan. Kuncinya konsisten dan tau cara belajar yang bener.

## Aturan #1 — ngetik ulang, jangan copy-paste

Saat ikut tutorial, godaan terbesar itu copy-paste kode. Lebih cepet, kelihatan jalan.

Tapi otak kamu nggak nyimpan apa-apa. Besoknya kamu nggak inget nulis apa.

Ngetik ulang manual itu lambat di awal, tapi otak nyatat tiap karakter. Setelah seminggu, kamu bakal kerasa: "Kok saya udah hafal pola ini?"

## Aturan #2 — error itu temen, bukan musuh

Pemula sering panik pas lihat error merah. Padahal pesan error itu petunjuk.

Coba baca error pelan-pelan. Biasanya bilang:

- File yang error: \`script.js\`
- Baris berapa: \`line 12\`
- Masalahnya apa: \`Uncaught SyntaxError: Unexpected token\`

Tiga info itu udah cukup buat 90% kasus. Kalo masih bingung, copy pesan error itu ke Google, biasanya udah ada yang nanya hal sama.

## Aturan #3 — bangun project, bukan ngabisin tutorial

Tutorial itu bagus buat ngenalin konsep. Tapi yang nempel di kepala itu bikin sendiri.

Setelah lesson, coba bikin sesuatu yang lebih kecil pake materi yang barusan dipelajari. Nggak perlu sempurna. Yang penting jadi.

Project kecil yang selesai > project besar yang nggak pernah kelar.

## Aturan #4 — sisihkan waktu rutin

30 menit tiap hari lebih ampuh daripada 5 jam seminggu sekali. Otak butuh pengulangan biar inget.

Pilih jam yang paling tenang buat kamu. Pagi sebelum kerja. Malam sebelum tidur. Konsistensi lebih penting dari durasi.

## Aturan #5 — jangan banding-bandingin progress

Di internet kamu bakal sering lihat orang yang katanya "belajar 3 bulan udah jadi developer". Boleh termotivasi, tapi jangan jadikan ukuran.

Setiap orang punya kecepatan sendiri. Banding-bandingin progress diri sama orang lain itu cara tercepat buat nyerah.

Standar yang sehat: kamu hari ini lebih ngerti dari kamu kemarin. Itu udah cukup.

## Hal terakhir

Lesson terakhir di Manual Fundamentals ini sengaja ditaruh di akhir. Karena tools dan bahasa bisa dipelajari kapan aja. Tapi mindset belajar yang sehat — itu yang nentuin kamu sampai mana.

Pelan-pelan aja. Setiap commit, setiap halaman yang jadi, setiap bug yang dipecahin — semuanya ngantar kamu ke titik yang lebih maju dari kemarin.
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
    duration: "9 menit",
    summary:
      "Cara kerja baru: AI yang nulis kode, kamu yang pegang arah dan kualitas.",
    content: `# Apa itu Vibe Coding

Vibe coding itu cara kerja baru di mana **AI yang nulis kode**, dan kamu yang **pegang arah, taste, dan kualitas hasilnya**.

Bukan berarti AI gantiin developer. Justru sebaliknya — kamu jadi makin penting karena kamu yang nentuin AI mau diarahkan ke mana.

## Bedanya sama coding biasa

Coding tradisional fokus di "gimana cara nulis logic ini". Vibe coding fokus di "apa yang harus dibangun, dan kenapa".

Kamu nggak perlu hafal semua syntax. Yang kamu perlu:

- Tau apa yang kamu mau
- Bisa ngomong jelas ke AI
- Bisa baca hasilnya dan ngecek bener atau salah
- Tau kapan minta revisi

Hasilnya: build cepet, iterasi cepet, ide cepet jadi produk.

## Realistis dari awal

Vibe coding bukan jalan pintas yang bikin kamu langsung jago. Tetep ada hal yang kamu harus paham:

- Cara kerja web pada umumnya.
- Mana yang sisi browser, mana yang sisi server.
- Cara kerja database minimal.
- Cara baca error dan tau di mana harus benerin.

Tanpa ini, kamu bakal panik tiap kali AI ngasih hasil yang nggak jalan. Karena kamu nggak punya peta buat tau di mana yang salah.

## Kapan vibe coding cocok

Vibe coding pas banget buat:

- MVP yang harus jalan minggu ini, bukan bulan depan.
- Side project yang fokusnya validasi ide.
- Solo founder yang butuh shipping cepet tanpa tim besar.
- Internal tools tim kamu yang butuh dibikin ringan.

Kurang cocok buat sistem mission-critical yang butuh code review berlapis. Untuk itu, tetep ada engineer manual coding yang ngecek baris per baris.

## Mindset yang sehat

Anggap AI itu junior yang super produktif tapi butuh diarahkan. Kalo kamu kasih perintah jelas, hasilnya bagus. Kalo kamu malas mikir dan asal nyuruh, hasilnya juga acak.

Kualitas output kamu sama dengan kualitas input kamu. Itu inti vibe coding.
`,
  },
  {
    slug: "cara-kerja-ai-coding",
    title: "Cara Kerja AI Coding",
    duration: "10 menit",
    summary:
      "AI bukan ajaib. Dia nebak kata berikutnya berdasarkan pola — dan itu kekuatan sekaligus kelemahannya.",
    content: `# Cara Kerja AI Coding

Banyak orang anggap AI itu kayak otak yang ngerti semua. Padahal cara kerjanya jauh lebih sederhana dari yang kamu kira.

## AI itu mesin pola

Model AI kayak ChatGPT, Claude, atau yang ada di Cursor — mereka semua belajar dari miliaran baris kode yang udah ada di internet.

Cara kerjanya: kamu kasih kalimat, AI nebak **kata berikutnya yang paling masuk akal** berdasarkan pola yang udah dia pelajari.

Itu doang? Iya, itu doang. Tapi karena polanya banyak banget, hasilnya bisa keliatan kayak ngerti.

## Apa artinya buat kamu

Beberapa konsekuensi penting:

- **AI suka ngarang.** Kalo dia nggak yakin, dia tetep bakal kasih jawaban yang kelihatan meyakinkan. Jangan langsung percaya.
- **AI cuma sebagus konteks yang kamu kasih.** Prompt vague = output vague. Prompt detail = output detail.
- **AI nggak tau project kamu.** Kalo nggak dikasih konteks file, struktur, atau goal — dia nebak dari pengetahuan umum.

Tugas kamu: kasih konteks yang cukup biar AI nebaknya tepat.

## Tools AI coding modern

Tiga jenis yang sering dipake:

- **Chat AI** (ChatGPT, Claude) — buat brainstorm, nanya konsep, debug kode kecil yang kamu paste.
- **Editor AI** (Cursor, Copilot) — kerja langsung di kode kamu. Bisa edit file, baca file lain, run command.
- **AI builder** (V0, Bolt, Lovable) — generate UI atau project utuh dari prompt.

Yang paling banyak dipake harian: Cursor. Karena dia gabungin chat + editor + akses ke seluruh project kamu.

## Halusinasi — masalah utama

Halusinasi itu istilah saat AI ngasih jawaban yang **kelihatan bener tapi salah**.

Contoh paling sering:

- Manggil function yang nggak ada di library.
- Ngarang nama field dari API.
- Bikin import dari package yang ternyata nggak ada.

Solusi: jangan langsung trust hasil AI. Coba run, lihat kalo error, lalu kasih tau AI bagian yang error. Iterasi.

## AI bukan pengganti, AI itu pengganda

Engineer yang udah bagus, dengan AI jadi lebih produktif. Tapi engineer yang nggak ngerti dasar, dengan AI tetep nyangkut karena nggak bisa baca hasilnya.

Pelajari dasar dengan baik. AI bakal jadi pengali, bukan pengganti otak kamu.
`,
  },
  {
    slug: "cara-ngomong-ke-ai",
    title: "Cara Ngomong ke AI yang Hasilnya Bagus",
    duration: "11 menit",
    summary:
      "Prompt jelek = hasil ngarang. Prompt jelas = hasil presisi. Begini cara nulis prompt yang efektif.",
    content: `# Cara Ngomong ke AI yang Hasilnya Bagus

Prompt itu kayak briefing ke karyawan baru. Kalo briefing kamu jelas, hasilnya cepet sesuai. Kalo briefing kamu kabur, hasilnya juga ngarang.

## Anatomi prompt yang bagus

Empat bagian wajib:

1. **Konteks** — kamu lagi ngapain, di project apa, stack apa.
2. **Goal** — apa yang kamu mau dihasilin.
3. **Spesifikasi** — detail teknis: nama file, props, format.
4. **Constraint** — apa yang nggak boleh, apa yang harus.

Contoh:

> Saya lagi bikin landing page Next.js + Tailwind buat toko kopi. Tolong bikin component Hero di file \`components/Hero.jsx\`. Hero punya headline besar, subheadline 1 kalimat, dan 2 tombol (utama biru, sekunder outline). Pake bahasa Indonesia santai. Hindari kata "amazing" atau "stunning".

Bandingkan dengan:

> Bikinin hero yang bagus.

Yang mana hasilnya lebih dekat sama yang kamu mau? Pasti yang pertama.

## Hindari kata yang ambigu

Kata-kata yang kerasa "bagus" tapi sebenernya nggak ngasih info:

- "Bikin yang keren"
- "Bikin yang modern"
- "Bikin yang professional"

AI bakal nebak sendiri. Hasilnya generic.

Ganti dengan kata konkret:

- "Hero pake spacing lega, padding vertical 96px ke atas"
- "Pake satu accent color biru, sisanya grayscale"
- "Animasi hover halus di card, naik 2px"

## Iterasi, bukan one-shot

AI jarang ngasih hasil sempurna di percobaan pertama. Itu normal.

Strateginya:

1. Kasih prompt awal yang detail.
2. Lihat hasilnya.
3. Identifikasi yang masih kurang.
4. Kasih feedback spesifik: "Tombol kedua kekecilan, padding-nya tambahin". Bukan: "Masih kurang oke."
5. Ulangi sampai pas.

Vibe coder yang bagus bisa iterasi cepet karena tau cara nyusun feedback yang konkret.

## Kasih konteks file kalau perlu

Di Cursor, kamu bisa drag file ke chat atau pake \`@filename\`. Itu ngasih AI akses ke isi file itu.

Tanpa konteks file, AI bakal nebak struktur project kamu. Sering meleset. Dengan konteks file, dia tau persis apa yang ada dan nyesuaiin sama kode existing.

Kebiasaan yang sehat: tiap kali minta edit file, kasih juga file related sebagai konteks.

## Jangan males nulis

Prompt panjang yang detail itu investasi waktu. Lebih cepet ngetik 5 menit prompt detail daripada bolak-balik 30 menit minta revisi.

Vibe coding bukan tentang shortcut. Tentang cara baru kerja yang **butuh komunikasi yang jelas** sama AI sebagai partner.
`,
  },
  {
    slug: "workflow-build-cepat",
    title: "Workflow Build Cepat dengan AI",
    duration: "10 menit",
    summary:
      "Cara kerja sehari-hari vibe coder: dari ide ke aplikasi yang live di internet.",
    content: `# Workflow Build Cepat dengan AI

Pernah lihat orang yang bisa bikin landing page dari ide jadi live cuma dalam 1 jam? Itu bukan magic. Itu workflow.

Ini langkah yang biasa dipake vibe coder produktif.

## Step 1 — Deskripsi singkat ide

Sebelum buka editor, tulis dulu di notes 3-5 baris tentang:

- App ini buat siapa
- Masalah apa yang dipecahin
- Tampilan utama yang dibutuhin

Ini jadi acuan tiap kali kamu kasih prompt ke AI nanti. Tanpa ini, kamu bakal lupa arah.

## Step 2 — Generate skeleton

Buka Cursor atau V0. Kasih prompt yang ngebangun struktur dasar.

Contoh prompt buat V0:

> Bikin landing page Next.js + Tailwind. Section: hero, fitur (3 card), testimoni, footer. Dark mode. Accent biru. Bahasa Indonesia.

V0 bakal kasih kode yang bisa langsung kamu pake. Salin ke project Cursor.

## Step 3 — Iterasi visual

Sekarang kamu di Cursor dengan kode awal. Buka di browser pake \`npm run dev\`.

Lihat hasilnya. Identifikasi yang kurang oke. Pake Cursor (\`Cmd+K\` atau \`Ctrl+K\`) buat minta revisi spesifik:

- "Spacing di hero kekecilan, naikin py-32"
- "Kartu fitur kurang lega, padding p-8"
- "Tombol primary terlalu pucat, gantiin biru yang lebih gelap"

Iterasi sampai puas.

## Step 4 — Push ke GitHub

Setelah versi lokal udah enak, simpan ke GitHub:

\`\`\`bash
git init
git add .
git commit -m "init: landing page toko kopi"
git remote add origin https://github.com/USERNAME/landing-kopi.git
git push -u origin main
\`\`\`

Kalo bingung, tanya AI: "Tolong setup git buat project ini dan push ke repo \`landing-kopi\`."

## Step 5 — Deploy ke Vercel

Buka [vercel.com/new](https://vercel.com/new). Login pake GitHub. Pilih repo. Klik Deploy.

Tunggu 1-2 menit. Dapet URL publik. Bagikan ke temen.

## Step 6 — Update setelah live

Tiap kali kamu push perubahan baru ke GitHub, Vercel auto-redeploy. Nggak perlu klik apapun.

Workflow harian setelah app live:

\`\`\`bash
git add .
git commit -m "perbaiki padding hero"
git push
\`\`\`

Tunggu 30 detik, cek URL Vercel kamu. Udah update.

## Estimasi waktu realistis

Buat landing page sederhana:

- Step 1-2 (ide + generate): 15 menit
- Step 3 (iterasi visual): 30-60 menit
- Step 4-5 (push + deploy): 15 menit
- **Total: 1-2 jam dari nol ke live**

Buat app yang lebih kompleks dengan database dan auth, tambah 2-4 jam. Tetep lebih cepet daripada coding manual dari nol.

## Yang nggak diperlihatin

Workflow di atas kelihatan smooth. Realitanya ada banyak momen:

- AI ngasih kode yang ada error → kamu kasih error message ke AI → dibetulin.
- Ada library yang nggak ke-install → kamu install manual.
- Ada konflik versi → kamu googling 5 menit.

Itu normal. Vibe coder yang bagus bukan yang nggak pernah error, tapi yang cepet pulih dari error.
`,
  },
  {
    slug: "tools-ai-modern",
    title: "Tools AI Modern yang Dipakai Vibe Coder",
    duration: "8 menit",
    summary:
      "Kenalan singkat sama tools yang akan jadi senjata harian kamu.",
    content: `# Tools AI Modern yang Dipakai Vibe Coder

Semua tools di sini gratis di tier dasar. Cukup buat pemula sampai pro level menengah.

## Cursor — editor utama

Cursor itu VS Code yang udah dimodif buat AI. Tampilannya sama, tapi punya:

- Chat AI di sisi kanan editor.
- \`Cmd+K\` (atau \`Ctrl+K\`) buat edit kode pake natural language.
- Composer mode buat ngerjain task multi-file.

Kalo cuma boleh punya satu tool, pilih ini. Download di [cursor.com](https://cursor.com).

## ChatGPT atau Claude — chat AI

Buat hal yang lebih panjang atau abstrak:

- Diskusi arsitektur sebelum mulai coding.
- Brainstorm fitur.
- Belajar konsep baru.
- Debug error yang panjang.

Claude (claude.ai) biasanya lebih bagus buat coding panjang. ChatGPT (chat.openai.com) lebih merata buat semua hal.

Gratis cukup. Upgrade kalo udah sering banget pake.

## V0 — generate UI dari teks

[v0.dev](https://v0.dev) bikin component React + Tailwind dari deskripsi.

Cocok buat:

- Bikin section landing page cepet.
- Eksplorasi opsi visual sebelum commit ke satu desain.
- Generate form atau dashboard yang lumayan kompleks.

Hasilnya bisa langsung di-copy ke project Cursor kamu.

## Bolt atau Lovable — full app builder

[bolt.new](https://bolt.new) dan [lovable.dev](https://lovable.dev) generate **app utuh** dari prompt. Termasuk file structure, routing, state management.

Cocok buat MVP cepet atau prototype yang harus jalan dalam beberapa jam.

Kelemahannya: kontrol detail kurang. Kalo mau polish, hampir selalu kamu pindah ke Cursor.

## GitHub Copilot — autocomplete pintar

Copilot kayak autocomplete biasa, tapi nebak baris kode penuh berdasarkan konteks file kamu.

Berguna buat ngurangin ngetik repetitif. Free buat student. Berbayar selain itu.

Banyak vibe coder skip ini sekarang karena Cursor udah punya fitur mirip.

## Vercel — deploy gratis

[vercel.com](https://vercel.com) tempat deploy yang paling cocok buat Next.js. Login pake GitHub, pilih repo, klik Deploy.

Free tier-nya udah cukup buat 99% project pribadi.

## Kebutuhan minimum

Kalo kamu baru mulai, cukup tiga ini:

- **Cursor** — buat coding harian.
- **Claude atau ChatGPT** — buat brainstorm.
- **Vercel** — buat deploy.

V0 dan Bolt nyusul kalo udah nyaman. Tools terlalu banyak di awal malah bikin bingung.
`,
  },
  {
    slug: "mindset-builder",
    title: "Mindset Builder — Bukan Sekadar Coder",
    duration: "9 menit",
    summary:
      "Vibe coder yang sukses bukan yang paling jago AI, tapi yang paling jago bikin produk.",
    content: `# Mindset Builder — Bukan Sekadar Coder

Coding itu satu skill. Bikin produk itu skill yang lain.

Vibe coding ngebantu kamu di sisi coding. Tapi yang bikin kamu sukses itu yang sisi produk.

## Apa bedanya coder dan builder

**Coder** fokus ke pertanyaan: "Gimana cara bikin ini jalan?"

**Builder** fokus ke pertanyaan: "Apakah ini worth dibikin? Siapa yang pake? Apa value-nya buat mereka?"

Coder yang bagus bisa bikin app yang technically perfect tapi nggak ada yang pake. Builder yang bagus bikin app yang berantakan tapi banyak yang suka.

Goalnya jadi keduanya. Tapi kalo harus pilih satu di awal — pilih builder.

## Pertanyaan yang harus sering kamu tanya

Sebelum mulai project, jawab dulu:

- Siapa yang bakal pake ini?
- Masalah apa yang mereka punya saat ini?
- Kenapa mereka bakal pake punya kamu, bukan yang lain?
- Apa indikator sukses-nya? (1000 user? 10 paying customer? Hilangnya satu masalah personal?)

Banyak orang skip pertanyaan ini, langsung coding. Hasilnya project yang technically jalan tapi nggak ada yang butuh.

## Ship cepet, dengarin user

Mindset bahaya di pemula: mau perfect dulu sebelum show ke orang.

Realitanya: kamu nggak bakal pernah tau apa yang user mau sampai mereka coba. Yang ada di kepala kamu cuma tebakan.

Aturan: ship versi yang malu-maluin tapi jalan. Kasih ke 5 orang. Dengerin reaksi mereka. Update.

Ini bedanya developer yang setahun-tahun di laptop dengan builder yang sebulan udah punya 50 user.

## Refactor itu mahal, perfeksionis itu bahaya

Tiap kali kamu mau "rapihin kode" sebelum ship — pertimbangkan: kode itu bakal kepake nggak?

50% project yang kamu bikin di awal bakal di-throw away. Refactor di kode yang nggak kepake itu buang waktu.

Tunggu sampai sebuah project terbukti penting (banyak user, atau kamu pake setiap hari), baru investasiin waktu buat kode quality.

## Belajar dari user, bukan dari tutorial

Setelah punya app yang dipake walau cuma 5 orang — feedback mereka 100x lebih berharga daripada tutorial mana pun.

Mereka bakal tunjukin:

- Hal yang kamu pikir "obvious" ternyata bingung.
- Fitur yang kamu pikir penting ternyata nggak ada yang pake.
- Bug yang kamu nggak sadar.
- Permintaan fitur yang nggak kepikiran.

Tugas kamu bukan cuma kasih solusi, tapi juga ngerti masalah lebih dalam dari user-nya sendiri.

## Realistis tentang vibe coding

Vibe coding bikin building lebih cepet. Tapi nggak bikin building lebih gampang.

Kamu masih harus mikir tentang user, fokus, prioritas, tradeoff. AI nggak ngerti konteks kamu, partner-mu, atau target market-mu.

Yang bikin kamu menonjol bukan punya akses ke AI. Yang bikin menonjol kemampuan kamu pake AI buat build something that matters.

Itu skill yang harus dilatih, sama kayak skill lainnya.
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
