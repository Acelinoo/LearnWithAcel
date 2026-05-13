// Lesson content for the Vibe Coding (AI-Assisted) learning path.
// Structure mirrors lessonContent.js: keyed by "levelSlug/lessonSlug".

export const vibeContent = {
  // ============================================================
  // LEVEL 0 — Mindset & Orientation
  // ============================================================
  "mindset-orientation/apa-itu-ai-development": {
    title: "Apa Itu AI-Assisted Development",
    description:
      "Pahami apa sebenarnya AI coding itu, bagaimana cara kerjanya, apa yang realistis dan apa yang cuma hype. Fondasi penting sebelum kamu mulai.",
    readTime: "6 menit",
    level: "Level 0 — Mindset & Orientation",
    hero: {
      emoji: "🤖",
      caption: "AI itu seperti junior developer yang sangat cepat — tapi butuh instruksi yang jelas dari kamu.",
    },
    objectives: [
      "Paham apa itu AI-assisted development dan bedanya dengan coding manual",
      "Tahu apa yang bisa dan tidak bisa dilakukan AI saat ini",
      "Punya ekspektasi realistis tentang workflow AI coding",
    ],
    practice: {
      fileName: "catatan-ai.md",
      steps: [
        "Buka browser, pergi ke chat.openai.com (ChatGPT) atau claude.ai",
        "Ketik prompt ini: 'Buatkan kode HTML sederhana untuk halaman yang menampilkan nama saya dan hobi saya'",
        "Perhatikan hasilnya — AI langsung memberikan kode yang bisa jalan",
        "Sekarang coba prompt yang ambigu: 'Buatkan website bagus'. Perhatikan hasilnya kurang spesifik",
        "Tulis di catatan: apa perbedaan hasil dari prompt spesifik vs prompt ambigu?",
      ],
      tip: "Kamu tidak perlu install apapun untuk latihan ini. Cukup buka browser dan akses ChatGPT atau Claude gratis.",
    },
    sections: [
      {
        heading: "Apa Itu AI-Assisted Development?",
        body: [
          "AI-assisted development artinya kamu membangun aplikasi dengan bantuan AI. Kamu tetap yang menentukan apa yang mau dibuat, tapi AI membantu menulis kode, memperbaiki error, dan mempercepat proses.",
          "Analogi: bayangkan kamu seorang arsitek. AI itu seperti tukang bangunan yang sangat cepat. Kamu yang desain rumahnya, AI yang bantu bangun. Tapi kalau instruksimu tidak jelas, hasilnya bisa melenceng.",
        ],
      },
      {
        heading: "Bagaimana AI Coding Bekerja?",
        body: [
          "AI coding tools (seperti ChatGPT, Claude, Cursor) bekerja dengan cara memprediksi kode berdasarkan instruksi yang kamu berikan (disebut 'prompt').",
          "AI sudah dilatih dari jutaan kode yang ada di internet. Jadi dia tahu pola-pola umum. Tapi dia tidak benar-benar 'mengerti' — dia menebak jawaban terbaik berdasarkan pola.",
        ],
        list: [
          "Kamu kasih instruksi (prompt) → AI generate kode",
          "Kamu review hasilnya → perbaiki yang kurang tepat",
          "Kamu iterasi → minta AI revisi sampai sesuai",
          "Kamu deploy → publish ke internet",
        ],
      },
      {
        heading: "Apa yang Realistis?",
        body: [
          "Yang BISA dilakukan AI sekarang: generate UI, menulis fungsi, memperbaiki bug sederhana, menjelaskan kode, membuat boilerplate, dan membantu deploy.",
          "Yang TIDAK BISA dilakukan AI: memahami kebutuhan bisnis yang kompleks, membuat keputusan arsitektur yang tepat tanpa konteks, menjamin kode 100% bebas bug, atau menggantikan pemahaman fundamental.",
        ],
      },
      {
        heading: "Mindset yang Benar",
        body: [
          "Jangan berpikir 'AI akan coding untuk saya'. Berpikirlah 'AI akan mempercepat saya 5-10x'. Kamu tetap perlu paham apa yang terjadi, bisa membaca kode, dan tahu kapan AI salah.",
          "Builder yang sukses dengan AI bukan yang paling jago coding — tapi yang paling jago memberikan instruksi dan mengevaluasi hasil.",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa peran utama kamu sebagai developer saat menggunakan AI?",
          options: [
            { id: "a", text: "Membiarkan AI membuat semua keputusan" },
            { id: "b", text: "Memberikan instruksi jelas dan mengevaluasi hasil AI" },
            { id: "c", text: "Hanya menekan tombol generate" },
            { id: "d", text: "Menghafal semua syntax programming" },
          ],
          answer: "b",
          explanation: "Kamu tetap yang mengarahkan. AI membantu eksekusi, tapi kamu yang menentukan arah dan mengevaluasi hasilnya.",
        },
        {
          question: "Mana yang paling tepat menggambarkan AI coding saat ini?",
          options: [
            { id: "a", text: "AI bisa membuat app lengkap tanpa instruksi apapun" },
            { id: "b", text: "AI seperti junior developer cepat yang butuh instruksi jelas" },
            { id: "c", text: "AI tidak berguna untuk coding" },
            { id: "d", text: "AI hanya bisa membuat website statis" },
          ],
          answer: "b",
          explanation: "AI sangat cepat tapi butuh arahan yang jelas. Semakin spesifik instruksimu, semakin bagus hasilnya.",
        },
        {
          question: "Apa yang TIDAK bisa dilakukan AI coding saat ini?",
          options: [
            { id: "a", text: "Generate kode HTML dan CSS" },
            { id: "b", text: "Memperbaiki bug sederhana" },
            { id: "c", text: "Menjamin kode 100% bebas bug tanpa review" },
            { id: "d", text: "Menjelaskan kode yang sudah ada" },
          ],
          answer: "c",
          explanation: "AI bisa generate dan fix kode, tapi tidak bisa menjamin hasilnya sempurna. Kamu tetap perlu review.",
        },
      ],
    },
    errorChallenge: {
      title: "Prompt yang Bermasalah",
      instruction: "Prompt di bawah ini akan menghasilkan output yang buruk. Coba identifikasi masalahnya dan perbaiki.",
      buggyCode: `Prompt: "Buatkan website"

Hasil AI: *menghasilkan website generic tanpa konten spesifik, 
warna random, layout standar yang tidak sesuai kebutuhan*`,
      hints: [
        "Prompt terlalu pendek dan tidak spesifik — AI tidak tahu website seperti apa yang kamu mau",
        "Tidak ada informasi tentang: tujuan website, konten, warna, layout yang diinginkan",
      ],
      fixedCode: `Prompt yang lebih baik:
"Buatkan landing page untuk toko kue online bernama 'Kue Mama'. 
Warna utama pink pastel. Ada hero section dengan tagline, 
daftar 3 produk populer dengan harga, dan tombol WhatsApp 
untuk order. Style modern dan minimalis."`,
      explanation: "Prompt yang baik harus spesifik: sebutkan jenis halaman, konten, warna, fitur yang diinginkan, dan style. Semakin detail promptmu, semakin mendekati harapanmu hasilnya.",
    },
    nextLesson: {
      href: "/materi/vibe/mindset-orientation/perbedaan-nocode-aicode",
      title: "No-Code vs Low-Code vs AI Coding vs Manual",
    },
  },

  "mindset-orientation/perbedaan-nocode-aicode": {
    title: "No-Code vs Low-Code vs AI Coding vs Manual",
    description:
      "Ada banyak cara bikin app. Mana yang cocok untuk kamu? Pahami perbedaan tiap pendekatan supaya kamu pilih jalur yang tepat.",
    readTime: "8 menit",
    level: "Level 0 — Mindset & Orientation",
    hero: {
      emoji: "🔀",
      caption: "Tidak ada pendekatan yang salah — yang penting cocok dengan tujuanmu.",
    },
    objectives: [
      "Bisa membedakan no-code, low-code, AI coding, dan manual coding",
      "Tahu kelebihan dan kekurangan masing-masing",
      "Paham kenapa jalur Vibe Coding (AI-assisted) dipilih di kursus ini",
    ],
    practice: {
      fileName: "perbandingan.md",
      steps: [
        "Buka browser, kunjungi bubble.io (no-code) — lihat cara kerjanya",
        "Buka v0.dev (AI coding) — coba ketik prompt untuk generate UI",
        "Bandingkan: mana yang lebih fleksibel? Mana yang lebih cepat untuk pemula?",
        "Tulis catatan: untuk project seperti apa kamu akan pakai masing-masing tools?",
      ],
      tip: "v0.dev dari Vercel bisa kamu akses gratis. Coba ketik 'modern pricing page with 3 tiers' dan lihat hasilnya.",
    },
    sections: [
      {
        heading: "Empat Pendekatan Membuat App",
        body: [
          "Di dunia 2025, ada empat cara utama untuk membuat aplikasi. Masing-masing punya trade-off.",
        ],
        list: [
          "No-Code (Bubble, Adalo, Glide): drag-and-drop, tidak perlu nulis kode sama sekali. Cepat untuk prototype, tapi terbatas kalau mau custom",
          "Low-Code (Retool, OutSystems): sebagian besar visual, tapi kadang perlu nulis sedikit kode. Cocok untuk internal tools",
          "AI Coding (Cursor, V0, Bolt, Lovable): kamu kasih instruksi, AI tulis kodenya. Fleksibel seperti manual coding, tapi jauh lebih cepat",
          "Manual Coding (VS Code + nulis sendiri): kontrol penuh, tapi butuh waktu belajar lama. Cocok untuk yang mau jadi software engineer profesional",
        ],
      },
      {
        heading: "Perbandingan Langsung",
        body: [
          "Bayangkan kamu mau bikin landing page untuk bisnis kecil:",
        ],
        list: [
          "No-Code: 30 menit, tapi template terbatas dan susah custom animasi",
          "Low-Code: 1 jam, bisa lebih custom tapi perlu belajar platform-nya",
          "AI Coding: 15 menit, hasilnya kode asli yang bisa kamu edit bebas",
          "Manual: 3-4 jam, kontrol penuh tapi butuh skill HTML/CSS/JS",
        ],
      },
      {
        heading: "Kenapa AI Coding?",
        body: [
          "AI Coding ada di sweet spot: cepat seperti no-code, tapi fleksibel seperti manual coding. Hasilnya kode asli yang bisa kamu deploy di mana saja, edit sesuka hati, dan tidak terkunci di satu platform.",
          "Kekurangannya: kamu tetap perlu paham dasar-dasar (apa itu HTML, bagaimana deploy bekerja). Tapi kamu tidak perlu hafal syntax — cukup paham konsep.",
        ],
      },
      {
        heading: "Kapan Pakai Yang Mana?",
        body: [
          "Tidak ada jawaban mutlak. Tapi sebagai panduan:",
        ],
        list: [
          "Prototype cepat untuk validasi ide → No-Code atau AI Coding",
          "Internal tool perusahaan → Low-Code",
          "Website/app yang mau di-custom penuh → AI Coding atau Manual",
          "Mau jadi software engineer profesional → Manual (tapi tetap pakai AI sebagai asisten)",
          "Mau jadi indie builder/freelancer → AI Coding (jalur ini!)",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa kelebihan utama AI Coding dibanding No-Code?",
          options: [
            { id: "a", text: "Lebih murah" },
            { id: "b", text: "Hasilnya kode asli yang bisa diedit dan deploy di mana saja" },
            { id: "c", text: "Tidak perlu internet" },
            { id: "d", text: "Lebih mudah dipelajari" },
          ],
          answer: "b",
          explanation: "AI Coding menghasilkan kode asli (HTML, CSS, JS) yang tidak terkunci di satu platform. Kamu bisa edit dan deploy sesuka hati.",
        },
        {
          question: "Untuk siapa jalur AI Coding paling cocok?",
          options: [
            { id: "a", text: "Yang mau jadi data scientist" },
            { id: "b", text: "Yang mau bikin app cepat tanpa hafal syntax" },
            { id: "c", text: "Yang sudah expert programming" },
            { id: "d", text: "Yang hanya mau bikin form sederhana" },
          ],
          answer: "b",
          explanation: "AI Coding cocok untuk yang mau membangun app nyata dengan cepat tanpa harus menghafal semua syntax programming.",
        },
        {
          question: "Apa kekurangan No-Code dibanding AI Coding?",
          options: [
            { id: "a", text: "Lebih lambat" },
            { id: "b", text: "Lebih mahal" },
            { id: "c", text: "Terbatas dalam customization dan terkunci di platform" },
            { id: "d", text: "Tidak bisa bikin website" },
          ],
          answer: "c",
          explanation: "No-code tools cepat tapi terbatas. Kalau mau fitur yang tidak disediakan template, kamu stuck. Dan hasilnya terkunci di platform itu.",
        },
      ],
    },
    errorChallenge: {
      title: "Salah Pilih Tools",
      instruction: "Skenario di bawah menunjukkan pemilihan tools yang kurang tepat. Identifikasi masalahnya.",
      buggyCode: `Skenario: Andi mau bikin portfolio website pribadi yang unik 
dengan animasi custom dan layout yang berbeda dari template.

Pilihan Andi: Pakai Wix (no-code drag-and-drop)

Hasil: Andi frustrasi karena tidak bisa bikin animasi yang 
dia mau, layout terbatas template, dan website-nya terlihat 
sama seperti ribuan website Wix lainnya.`,
      hints: [
        "Portfolio yang 'unik dengan animasi custom' butuh fleksibilitas tinggi",
        "No-code tools bagus untuk yang standar, tapi terbatas untuk custom design",
      ],
      fixedCode: `Pilihan yang lebih tepat: AI Coding (Cursor + V0)

Prompt ke V0: "Buatkan portfolio website untuk UI designer 
dengan animasi scroll smooth, layout asymmetric modern, 
dark mode, dan section untuk showcase 6 project"

Hasilnya: kode React + Tailwind yang bisa diedit bebas, 
ditambah animasi custom, dan di-deploy ke Vercel gratis.`,
      explanation: "Untuk kebutuhan yang sangat custom, AI Coding atau manual coding lebih cocok karena tidak ada batasan template. No-code bagus untuk yang standar dan cepat.",
    },
    nextLesson: {
      href: "/materi/vibe/mindset-orientation/workflow-modern-developer",
      title: "Workflow Modern Developer",
    },
  },

  "mindset-orientation/workflow-modern-developer": {
    title: "Workflow Modern Developer 2025",
    description:
      "Bagaimana developer modern bekerja sehari-hari? Bukan duduk menghafal syntax, tapi menggabungkan tools AI untuk membangun dengan cepat.",
    readTime: "7 menit",
    level: "Level 0 — Mindset & Orientation",
    hero: {
      emoji: "⚡",
      caption: "Developer modern bukan yang paling hafal syntax — tapi yang paling efisien menggabungkan tools.",
    },
    objectives: [
      "Paham alur kerja developer modern dari ide sampai deploy",
      "Tahu peran AI di setiap tahap development",
      "Bisa membayangkan workflow harianmu nanti",
    ],
    practice: {
      fileName: "workflow-saya.md",
      steps: [
        "Buka catatan (Notion, Google Docs, atau file .md)",
        "Tulis ide app sederhana yang ingin kamu buat (contoh: 'website portofolio pribadi')",
        "Breakdown jadi langkah-langkah: (1) desain, (2) generate kode, (3) edit, (4) deploy",
        "Untuk setiap langkah, tulis tools apa yang akan kamu pakai",
        "Simpan catatan ini — kamu akan pakai di level berikutnya",
      ],
      tip: "Workflow yang bagus itu yang kamu bisa ulangi. Bikin template langkah-langkah yang sama untuk setiap project baru.",
    },
    sections: [
      {
        heading: "Alur Kerja Developer Modern",
        body: [
          "Developer 2025 tidak mulai dari blank file dan nulis kode dari nol. Mereka punya workflow yang terstruktur:",
        ],
        list: [
          "1. Ideation: tentukan apa yang mau dibuat, untuk siapa, fitur apa saja",
          "2. Design: sketch layout (bisa pakai AI atau Figma), tentukan warna dan style",
          "3. Generate: pakai AI untuk generate kode awal dari prompt",
          "4. Edit & Iterate: perbaiki hasil AI, tambah fitur, sesuaikan detail",
          "5. Test: cek di browser, pastikan responsive dan tidak ada bug",
          "6. Deploy: publish ke internet supaya orang lain bisa akses",
          "7. Iterate: dapat feedback, perbaiki, tambah fitur baru",
        ],
      },
      {
        heading: "Peran AI di Setiap Tahap",
        body: [
          "AI bukan cuma untuk generate kode. Dia bisa membantu di hampir semua tahap:",
        ],
        list: [
          "Ideation: 'Kasih saya 5 ide fitur untuk app todo list' → AI brainstorm",
          "Design: V0.dev bisa generate UI dari deskripsi teks",
          "Generate: Cursor/Bolt bisa bikin seluruh halaman dari prompt",
          "Debug: paste error ke ChatGPT → dapat solusi dalam detik",
          "Deploy: AI bisa bantu setup deployment config",
        ],
      },
      {
        heading: "Contoh Workflow Nyata",
        body: [
          "Misalnya kamu mau bikin landing page untuk jasa desain grafis:",
        ],
        list: [
          "Senin pagi: tulis brief di Notion — siapa target, apa pesannya, fitur apa",
          "Senin siang: buka V0.dev, ketik prompt berdasarkan brief → dapat UI",
          "Senin sore: copy kode ke Cursor, edit warna, ganti teks, tambah gambar",
          "Selasa pagi: test di HP dan laptop, fix responsive issues pakai AI",
          "Selasa siang: push ke GitHub, deploy ke Vercel → website live!",
          "Total waktu aktif: sekitar 4-5 jam. Tanpa AI: bisa 2-3 hari.",
        ],
      },
      {
        heading: "Mindset: Builder, Bukan Coder",
        body: [
          "Kamu bukan 'belajar coding'. Kamu belajar jadi builder — orang yang bisa mewujudkan ide jadi produk nyata. Coding hanyalah salah satu tools-nya.",
          "Sama seperti fotografer tidak perlu bikin kamera sendiri, builder tidak perlu nulis setiap baris kode sendiri. Yang penting: hasilnya bagus dan berfungsi.",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa langkah pertama dalam workflow developer modern?",
          options: [
            { id: "a", text: "Langsung nulis kode" },
            { id: "b", text: "Install banyak tools" },
            { id: "c", text: "Tentukan apa yang mau dibuat dan untuk siapa" },
            { id: "d", text: "Belajar programming language baru" },
          ],
          answer: "c",
          explanation: "Selalu mulai dari ide dan tujuan. Tanpa kejelasan ini, kode yang dihasilkan AI pun akan berantakan.",
        },
        {
          question: "Di tahap mana AI paling sering digunakan?",
          options: [
            { id: "a", text: "Hanya di tahap generate kode" },
            { id: "b", text: "Di hampir semua tahap: ideation, generate, debug, deploy" },
            { id: "c", text: "Hanya di tahap deploy" },
            { id: "d", text: "AI tidak digunakan dalam workflow modern" },
          ],
          answer: "b",
          explanation: "AI bisa membantu di semua tahap — dari brainstorm ide sampai fix bug dan setup deployment.",
        },
        {
          question: "Apa mindset yang benar untuk AI builder?",
          options: [
            { id: "a", text: "Harus hafal semua syntax sebelum mulai" },
            { id: "b", text: "Fokus pada hasil: mewujudkan ide jadi produk yang berfungsi" },
            { id: "c", text: "Jangan pernah edit kode yang dihasilkan AI" },
            { id: "d", text: "Coding manual selalu lebih baik" },
          ],
          answer: "b",
          explanation: "Builder fokus pada hasil akhir. Coding adalah tools, bukan tujuan. Yang penting produknya jadi dan berfungsi.",
        },
      ],
    },
    errorChallenge: {
      title: "Workflow yang Berantakan",
      instruction: "Developer di bawah punya workflow yang tidak efisien. Identifikasi masalahnya.",
      buggyCode: `Workflow Budi:
1. Langsung buka Cursor, ketik prompt random
2. Dapat kode, langsung deploy tanpa test
3. Website error di production
4. Panik, hapus semua, mulai dari awal
5. Ulangi langkah 1-4 berkali-kali

Hasil: 3 hari dan website masih belum jadi.`,
      hints: [
        "Tidak ada tahap planning — langsung generate tanpa tahu mau bikin apa",
        "Tidak ada tahap testing sebelum deploy",
        "Tidak ada iterasi yang terstruktur — langsung hapus semua saat error",
      ],
      fixedCode: `Workflow yang lebih baik:
1. Tulis brief: "Landing page toko kue, 3 section, warna pink"
2. Generate di V0/Cursor berdasarkan brief
3. Review hasil, edit yang kurang sesuai
4. Test di browser (desktop + mobile)
5. Fix issues yang ditemukan (pakai AI untuk bantu debug)
6. Deploy ke Vercel
7. Cek lagi di production, fix kalau ada masalah kecil

Hasil: 4-5 jam, website jadi dan berfungsi.`,
      explanation: "Workflow yang baik selalu dimulai dari planning, ada tahap review dan testing sebelum deploy, dan iterasi yang terstruktur (bukan hapus semua dan mulai ulang).",
    },
    nextLesson: {
      href: "/materi/vibe/mindset-orientation/tools-ecosystem",
      title: "Tools Ecosystem Overview",
    },
  },

  "mindset-orientation/tools-ecosystem": {
    title: "Tools Ecosystem Overview",
    description:
      "Cursor, ChatGPT, Claude, V0, Bolt, Lovable, GitHub, Vercel, Supabase — banyak banget! Di sini kamu akan paham masing-masing untuk apa.",
    readTime: "10 menit",
    level: "Level 0 — Mindset & Orientation",
    hero: {
      emoji: "🧰",
      caption: "Kamu tidak perlu pakai semua tools. Cukup tahu mana yang cocok untuk kebutuhanmu.",
    },
    objectives: [
      "Kenal tools utama dalam ekosistem AI development",
      "Tahu fungsi dan kapan pakai masing-masing tools",
      "Bisa memilih kombinasi tools yang tepat untuk projectmu",
    ],
    practice: {
      fileName: "tools-saya.md",
      steps: [
        "Buka browser dan kunjungi satu per satu: cursor.com, v0.dev, bolt.new, lovable.dev",
        "Di setiap website, baca tagline-nya dan coba fitur gratisnya",
        "Buat tabel perbandingan: nama tools | fungsi | gratis/bayar | kapan pakai",
        "Pilih 3 tools yang akan jadi 'starter kit' kamu",
        "Tulis alasannya kenapa kamu pilih kombinasi itu",
      ],
      tip: "Untuk pemula, starter kit yang direkomendasikan: Cursor (code editor) + ChatGPT/Claude (AI chat) + GitHub (simpan kode) + Vercel (deploy). Empat ini cukup untuk bikin dan publish website.",
    },
    sections: [
      {
        heading: "Kategori Tools",
        body: [
          "Tools AI development bisa dibagi jadi beberapa kategori berdasarkan fungsinya:",
        ],
        list: [
          "AI Chat (brainstorm & debug): ChatGPT, Claude, Gemini",
          "AI Code Editor (nulis kode): Cursor, Windsurf, GitHub Copilot",
          "AI App Generator (generate app langsung): V0, Bolt, Lovable",
          "Version Control (simpan & kolaborasi kode): GitHub, GitLab",
          "Deployment (publish ke internet): Vercel, Netlify, Railway",
          "Database (simpan data): Supabase, Firebase, PlanetScale",
        ],
      },
      {
        heading: "Tools yang Akan Kita Pakai",
        body: [
          "Di kursus ini, kita fokus ke kombinasi yang paling efisien untuk pemula:",
        ],
        list: [
          "Cursor: code editor berbasis VS Code + AI built-in. Kamu nulis prompt, dia generate kode langsung di editor",
          "ChatGPT / Claude: untuk brainstorm, tanya konsep, debug error yang kompleks",
          "V0.dev: generate UI/komponen dari deskripsi teks. Bagus untuk dapat starting point",
          "GitHub: tempat simpan kode online. Seperti Google Drive tapi untuk kode",
          "Vercel: platform deploy. Connect ke GitHub, setiap push otomatis update website",
          "Supabase (nanti di level 4): database gratis. Untuk simpan data user, login, dll",
        ],
      },
      {
        heading: "Cursor vs ChatGPT — Apa Bedanya?",
        body: [
          "Pertanyaan yang sering muncul: kenapa perlu Cursor kalau sudah ada ChatGPT?",
          "ChatGPT itu AI chat — kamu tanya, dia jawab di chat. Kamu harus copy-paste kode ke file sendiri.",
          "Cursor itu code editor + AI — AI-nya langsung edit file kamu. Tidak perlu copy-paste. Dia bisa lihat seluruh project kamu dan edit banyak file sekaligus.",
          "Analogi: ChatGPT itu seperti konsultan yang kasih saran lewat telepon. Cursor itu seperti asisten yang duduk di sebelahmu dan langsung bantu kerjakan.",
        ],
      },
      {
        heading: "V0 vs Bolt vs Lovable",
        body: [
          "Ketiganya adalah AI app generator, tapi beda fokus:",
        ],
        list: [
          "V0 (by Vercel): fokus generate komponen UI React. Hasilnya kode bersih yang bisa langsung dipakai",
          "Bolt (by StackBlitz): generate full app di browser. Bisa langsung preview dan edit",
          "Lovable: mirip Bolt tapi lebih fokus ke non-technical users. Interface lebih simpel",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa perbedaan utama Cursor dengan ChatGPT?",
          options: [
            { id: "a", text: "Cursor lebih murah" },
            { id: "b", text: "Cursor langsung edit file di project, ChatGPT hanya jawab di chat" },
            { id: "c", text: "ChatGPT lebih pintar" },
            { id: "d", text: "Tidak ada perbedaan" },
          ],
          answer: "b",
          explanation: "Cursor terintegrasi langsung dengan code editor — AI-nya bisa lihat dan edit file projectmu. ChatGPT hanya bisa jawab di chat window.",
        },
        {
          question: "Tools mana yang dipakai untuk menyimpan kode online?",
          options: [
            { id: "a", text: "Vercel" },
            { id: "b", text: "Cursor" },
            { id: "c", text: "GitHub" },
            { id: "d", text: "V0" },
          ],
          answer: "c",
          explanation: "GitHub adalah platform version control — tempat menyimpan kode online, melacak perubahan, dan kolaborasi.",
        },
        {
          question: "Untuk deploy website ke internet, tools mana yang dipakai?",
          options: [
            { id: "a", text: "GitHub" },
            { id: "b", text: "Vercel" },
            { id: "c", text: "Cursor" },
            { id: "d", text: "Supabase" },
          ],
          answer: "b",
          explanation: "Vercel adalah platform deployment. Connect ke GitHub repo, dan setiap kamu push kode baru, website otomatis update.",
        },
      ],
    },
    errorChallenge: {
      title: "Salah Pakai Tools",
      instruction: "Developer di bawah menggunakan tools yang kurang tepat. Identifikasi dan sarankan yang lebih baik.",
      buggyCode: `Masalah: Dina mau bikin landing page sederhana.

Yang dia lakukan:
1. Setup Firebase (database) — padahal tidak butuh database
2. Belajar Docker (containerization) — padahal cuma website statis
3. Setup AWS EC2 (server) — padahal bisa pakai Vercel gratis
4. Nulis kode dari nol tanpa AI — padahal bisa generate

Hasil: 2 minggu dan belum jadi juga. Overwhelmed.`,
      hints: [
        "Landing page sederhana tidak butuh database, Docker, atau AWS",
        "Untuk website statis, Vercel gratis dan setup-nya 2 menit",
        "AI bisa generate landing page dalam hitungan menit",
      ],
      fixedCode: `Yang seharusnya dilakukan Dina:
1. Buka V0.dev → ketik deskripsi landing page → dapat kode
2. Copy ke Cursor → edit teks, warna, gambar
3. Push ke GitHub
4. Connect GitHub ke Vercel → deploy

Total waktu: 2-3 jam. Tidak perlu database, Docker, atau AWS.
Pilih tools sesuai kebutuhan, jangan over-engineer!`,
      explanation: "Kesalahan umum pemula: over-engineering. Untuk landing page sederhana, kamu hanya butuh code editor + AI + GitHub + Vercel. Jangan tambah tools yang tidak perlu.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/install-tools",
      title: "Install Tools",
    },
  },

  // ============================================================
  // LEVEL 1 — First App Experience
  // ============================================================
  "first-app/install-tools": {
    title: "Install Tools: Setup Cursor, GitHub & Vercel",
    description:
      "Langkah pertama: install semua tools yang kamu butuhkan. Ikuti step by step, dalam 30 menit kamu siap mulai build.",
    readTime: "10 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "🛠️",
      caption: "Setup yang benar di awal = workflow lancar ke depannya.",
    },
    objectives: [
      "Berhasil install Cursor (code editor + AI)",
      "Punya akun GitHub dan tahu cara buat repository",
      "Punya akun Vercel yang terconnect ke GitHub",
    ],
    practice: {
      fileName: "checklist-setup.md",
      steps: [
        "Download Cursor di cursor.com → klik Download → install seperti biasa",
        "Buka Cursor → saat pertama kali buka, dia akan minta login. Buat akun pakai email atau Google",
        "Buka github.com → klik Sign Up → buat akun baru (gratis)",
        "Buka vercel.com → klik Sign Up → pilih 'Continue with GitHub' supaya langsung terconnect",
        "Kembali ke Cursor → buka terminal (Ctrl + `) → ketik: git --version. Kalau muncul angka versi, Git sudah terinstall",
        "Kalau Git belum ada: download di git-scm.com → install dengan setting default (next-next-next)",
      ],
      tip: "Cursor sudah include AI (Claude/GPT) di dalamnya. Kamu bisa langsung pakai tanpa setup API key terpisah. Versi gratis sudah cukup untuk belajar.",
    },
    sections: [
      {
        heading: "Step 1: Install Cursor",
        body: [
          "Cursor adalah code editor (tempat nulis kode) yang sudah ada AI-nya built-in. Dia berbasis VS Code, jadi kalau kamu pernah pakai VS Code, tampilannya mirip.",
        ],
        list: [
          "Buka browser → pergi ke cursor.com",
          "Klik tombol 'Download' (otomatis detect OS kamu)",
          "Buka file yang terdownload → install seperti biasa (Next → Next → Install)",
          "Buka Cursor → login/buat akun saat diminta",
          "Selesai! Cursor siap dipakai",
        ],
      },
      {
        heading: "Step 2: Buat Akun GitHub",
        body: [
          "GitHub adalah tempat menyimpan kode online. Seperti Google Drive, tapi khusus untuk kode. Nanti kamu akan push (upload) kode dari Cursor ke GitHub.",
        ],
        list: [
          "Buka github.com → klik 'Sign up'",
          "Masukkan email, buat password, pilih username",
          "Verifikasi email (cek inbox)",
          "Selesai! Akun GitHub kamu sudah aktif",
        ],
      },
      {
        heading: "Step 3: Install Git",
        body: [
          "Git adalah tools yang menghubungkan Cursor dengan GitHub. Biasanya sudah terinstall di Mac. Di Windows perlu install manual.",
        ],
        list: [
          "Buka Cursor → tekan Ctrl + ` (backtick, tombol di bawah Esc) untuk buka Terminal",
          "Ketik: git --version lalu Enter",
          "Kalau muncul 'git version 2.xx.x' → sudah terinstall, skip ke step berikutnya",
          "Kalau muncul error → buka git-scm.com → Download → install dengan setting default",
          "Setelah install, tutup dan buka ulang Cursor, coba lagi git --version",
        ],
      },
      {
        heading: "Step 4: Buat Akun Vercel",
        body: [
          "Vercel adalah platform untuk deploy (publish) website ke internet. Gratis untuk project personal.",
        ],
        list: [
          "Buka vercel.com → klik 'Sign Up'",
          "Pilih 'Continue with GitHub' (ini penting! supaya nanti deploy otomatis)",
          "Authorize Vercel untuk akses GitHub kamu",
          "Selesai! Nanti tinggal connect repo dan website langsung live",
        ],
      },
      {
        heading: "Verifikasi Setup",
        body: [
          "Pastikan semua sudah benar dengan checklist ini:",
        ],
        list: [
          "✅ Cursor terbuka dan kamu sudah login",
          "✅ Terminal di Cursor bisa jalankan 'git --version' tanpa error",
          "✅ Akun GitHub aktif (bisa login di github.com)",
          "✅ Akun Vercel aktif dan terconnect ke GitHub",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa fungsi utama Cursor?",
          options: [
            { id: "a", text: "Tempat deploy website" },
            { id: "b", text: "Code editor dengan AI built-in untuk nulis kode" },
            { id: "c", text: "Tempat simpan kode online" },
            { id: "d", text: "Browser khusus developer" },
          ],
          answer: "b",
          explanation: "Cursor adalah code editor (tempat nulis kode) yang sudah terintegrasi AI. Kamu bisa nulis prompt dan AI langsung generate/edit kode di file.",
        },
        {
          question: "Kenapa saat sign up Vercel sebaiknya pilih 'Continue with GitHub'?",
          options: [
            { id: "a", text: "Supaya lebih murah" },
            { id: "b", text: "Supaya Vercel bisa otomatis deploy dari GitHub repo" },
            { id: "c", text: "Karena tidak ada pilihan lain" },
            { id: "d", text: "Supaya GitHub jadi lebih cepat" },
          ],
          answer: "b",
          explanation: "Dengan connect ke GitHub, setiap kamu push kode baru ke repo, Vercel otomatis deploy ulang. Tidak perlu manual upload.",
        },
        {
          question: "Bagaimana cara buka Terminal di Cursor?",
          options: [
            { id: "a", text: "Klik File → Terminal" },
            { id: "b", text: "Tekan Ctrl + ` (backtick)" },
            { id: "c", text: "Klik kanan di desktop" },
            { id: "d", text: "Buka Command Prompt terpisah" },
          ],
          answer: "b",
          explanation: "Shortcut Ctrl + ` (backtick, tombol di bawah Esc) membuka terminal terintegrasi di dalam Cursor.",
        },
      ],
    },
    errorChallenge: {
      title: "Error Saat Setup",
      instruction: "Pemula sering dapat error ini saat setup. Coba identifikasi solusinya.",
      buggyCode: `Terminal di Cursor:
$ git --version
'git' is not recognized as an internal or external command

$ node --version
'node' is not recognized as an internal or external command`,
      hints: [
        "Error 'not recognized' artinya program belum terinstall atau belum masuk PATH",
        "Setelah install program baru, kadang perlu restart Cursor/terminal",
      ],
      fixedCode: `Solusi:
1. Git belum terinstall → download di git-scm.com → install
2. Node belum terinstall → download di nodejs.org → pilih LTS → install
3. PENTING: setelah install, tutup Cursor lalu buka lagi
4. Coba lagi di terminal:

$ git --version
git version 2.43.0  ✓

$ node --version
v20.11.0  ✓

Kalau masih error setelah restart: restart komputer.`,
      explanation: "Error 'not recognized' berarti program belum terinstall. Solusinya: install program tersebut, lalu restart Cursor (atau restart komputer) supaya PATH ter-update.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/github-basics",
      title: "GitHub Basics",
    },
  },

  "first-app/github-basics": {
    title: "GitHub Basics: Simpan Kode Online",
    description:
      "Belajar cara membuat repository, push kode, dan memahami dasar Git. Supaya kode kamu aman dan bisa diakses dari mana saja.",
    readTime: "8 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "🐙",
      caption: "GitHub itu seperti Google Drive untuk kode — tapi jauh lebih powerful.",
    },
    objectives: [
      "Bisa membuat repository baru di GitHub",
      "Paham konsep commit dan push",
      "Bisa push kode dari Cursor ke GitHub",
    ],
    practice: {
      fileName: "latihan-github",
      steps: [
        "Buka github.com → klik tombol '+' di kanan atas → 'New repository'",
        "Nama repo: 'latihan-pertama' → centang 'Add a README file' → klik 'Create repository'",
        "Buka Cursor → tekan Ctrl + ` untuk buka terminal",
        "Ketik: git clone https://github.com/USERNAME/latihan-pertama.git (ganti USERNAME dengan username GitHub kamu)",
        "Ketik: cd latihan-pertama",
        "Buat file baru: di Explorer panel kiri, klik New File → ketik 'halo.txt' → tulis apa saja di dalamnya",
        "Di terminal ketik satu per satu: git add . lalu Enter, git commit -m 'file pertama' lalu Enter, git push lalu Enter",
        "Buka github.com/USERNAME/latihan-pertama → file halo.txt sudah muncul!",
      ],
      tip: "Pertama kali push, Git mungkin minta login. Pilih 'Sign in with browser' saat muncul popup. Setelah itu tidak perlu login lagi.",
    },
    sections: [
      {
        heading: "Apa Itu Repository?",
        body: [
          "Repository (repo) adalah folder project yang disimpan di GitHub. Satu project = satu repo. Di dalamnya ada semua file kode, gambar, dan konfigurasi project.",
          "Analogi: repo itu seperti folder di Google Drive. Bedanya, Git melacak setiap perubahan yang kamu buat (history lengkap).",
        ],
      },
      {
        heading: "Konsep Dasar Git",
        body: [
          "Git punya 3 langkah utama untuk menyimpan perubahan:",
        ],
        list: [
          "git add: pilih file mana yang mau disimpan perubahannya (seperti centang file)",
          "git commit: simpan snapshot perubahan dengan pesan penjelasan (seperti 'Save as' dengan catatan)",
          "git push: upload perubahan ke GitHub (seperti sync ke cloud)",
        ],
      },
      {
        heading: "Langkah: Buat Repo dan Push",
        body: [
          "Ikuti langkah ini untuk pertama kali push kode ke GitHub:",
        ],
        code: `# Di terminal Cursor:

# 1. Clone repo (download dari GitHub ke komputer)
git clone https://github.com/username/nama-repo.git

# 2. Masuk ke folder repo
cd nama-repo

# 3. Setelah edit/tambah file, simpan perubahan:
git add .
git commit -m "deskripsi perubahan"
git push`,
        list: [
          "git clone: download repo dari GitHub ke komputer kamu",
          "git add . (pakai titik): tambahkan SEMUA file yang berubah",
          "git commit -m '...': simpan dengan pesan. Pesan harus singkat dan jelas",
          "git push: upload ke GitHub. Setelah ini, perubahan muncul di github.com",
        ],
      },
      {
        heading: "Tips Penting",
        body: [
          "Commit sering, jangan tunggu sampai selesai semua. Setiap kali satu fitur jadi atau satu bug fixed, commit. Ini seperti save game — kalau ada masalah, kamu bisa kembali ke titik sebelumnya.",
        ],
        list: [
          "Commit message yang bagus: 'tambah hero section', 'fix responsive navbar', 'update warna tema'",
          "Commit message yang jelek: 'update', 'fix', 'asdf', 'wip'",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa urutan yang benar untuk menyimpan perubahan ke GitHub?",
          options: [
            { id: "a", text: "push → commit → add" },
            { id: "b", text: "commit → add → push" },
            { id: "c", text: "add → commit → push" },
            { id: "d", text: "add → push → commit" },
          ],
          answer: "c",
          explanation: "Urutannya: add (pilih file) → commit (simpan snapshot) → push (upload ke GitHub).",
        },
        {
          question: "Apa fungsi perintah 'git clone'?",
          options: [
            { id: "a", text: "Menghapus repository" },
            { id: "b", text: "Download repository dari GitHub ke komputer" },
            { id: "c", text: "Membuat file baru" },
            { id: "d", text: "Upload kode ke GitHub" },
          ],
          answer: "b",
          explanation: "git clone men-download seluruh repository (termasuk history) dari GitHub ke komputer lokal kamu.",
        },
        {
          question: "Commit message yang baik itu seperti apa?",
          options: [
            { id: "a", text: "'update'" },
            { id: "b", text: "'fix bug di navbar responsive'" },
            { id: "c", text: "'asdf'" },
            { id: "d", text: "'changes'" },
          ],
          answer: "b",
          explanation: "Commit message harus singkat tapi jelas menjelaskan APA yang berubah. Supaya nanti mudah dicari kalau perlu rollback.",
        },
      ],
    },
    errorChallenge: {
      title: "Error Git Push",
      instruction: "Error di bawah sering muncul saat pertama kali push. Cari tahu penyebab dan solusinya.",
      buggyCode: `$ git push
fatal: not a git repository (or any of the parent directories): .git

# Atau error ini:
$ git push
error: failed to push some refs to 'https://github.com/user/repo.git'
hint: Updates were rejected because the remote contains work that you do not have locally.`,
      hints: [
        "Error pertama: kamu belum di dalam folder yang benar (bukan git repo)",
        "Error kedua: ada perubahan di GitHub yang belum kamu download",
      ],
      fixedCode: `# Solusi error 1: pastikan kamu di folder yang benar
$ cd nama-repo    # masuk ke folder repo dulu
$ git push        # sekarang baru push

# Solusi error 2: pull dulu sebelum push
$ git pull        # download perubahan terbaru dari GitHub
$ git push        # sekarang push bisa jalan

# Tips: selalu pastikan kamu di folder repo yang benar
# Cek dengan: pwd (Mac/Linux) atau cd (Windows)`,
      explanation: "Error 'not a git repository' artinya kamu belum masuk ke folder repo. Error 'failed to push' artinya ada perubahan di GitHub yang belum kamu pull. Solusi: pull dulu, baru push.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/prompt-basics",
      title: "Prompt Basics",
    },
  },

  "first-app/prompt-basics": {
    title: "Prompt Basics: Cara Bicara dengan AI",
    description:
      "Prompt adalah instruksi yang kamu berikan ke AI. Prompt yang bagus = hasil yang bagus. Di sini kamu belajar formula menulis prompt yang efektif.",
    readTime: "12 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "💬",
      caption: "Skill paling penting di era AI bukan coding — tapi komunikasi yang jelas.",
    },
    objectives: [
      "Paham anatomi prompt yang baik",
      "Bisa membedakan prompt bagus vs prompt jelek",
      "Tahu formula CRAFT untuk menulis prompt",
      "Bisa menulis prompt yang menghasilkan kode berkualitas",
    ],
    practice: {
      fileName: "latihan-prompt.md",
      steps: [
        "Buka Cursor → tekan Ctrl + K (atau Cmd + K di Mac) untuk buka AI prompt",
        "Coba prompt JELEK: 'buatkan website' → lihat hasilnya (generic, tidak sesuai)",
        "Sekarang coba prompt BAGUS: 'Buatkan hero section untuk website portfolio developer. Dark mode, gradient purple ke blue, ada heading besar, subtitle, dan tombol CTA. Pakai Tailwind CSS.'",
        "Bandingkan kedua hasil — mana yang lebih mendekati harapanmu?",
        "Coba 3 prompt lagi dengan formula CRAFT yang diajarkan di bawah",
        "Screenshot atau catat: prompt mana yang hasilnya paling bagus?",
      ],
      tip: "Di Cursor, Ctrl+K untuk prompt inline (edit satu bagian), Ctrl+L untuk chat (tanya/diskusi). Pakai Ctrl+K untuk generate kode, Ctrl+L untuk tanya konsep.",
    },
    sections: [
      {
        heading: "Kenapa Prompt Itu Penting?",
        body: [
          "AI itu seperti genie (jin) — dia akan memberikan PERSIS apa yang kamu minta. Masalahnya: kebanyakan orang tidak tahu cara minta dengan jelas.",
          "Prompt yang ambigu → hasil yang ambigu. Prompt yang spesifik → hasil yang mendekati harapan. Ini skill yang bisa dilatih.",
        ],
      },
      {
        heading: "Formula CRAFT",
        body: [
          "Gunakan formula CRAFT untuk menulis prompt yang efektif:",
        ],
        list: [
          "C - Context: kasih konteks. Ini untuk apa? (portfolio, toko online, blog)",
          "R - Role: tentukan style/framework. (pakai React, Tailwind, dark mode)",
          "A - Action: apa yang harus dilakukan AI? (buatkan, perbaiki, tambahkan)",
          "F - Format: format output yang diinginkan. (komponen React, HTML biasa, dengan komentar)",
          "T - Tone/Details: detail tambahan. (warna, ukuran, animasi, responsive)",
        ],
      },
      {
        heading: "Contoh: Prompt Jelek vs Bagus",
        body: [
          "Lihat perbedaan drastis antara prompt yang jelek dan yang bagus:",
        ],
        code: `// ❌ PROMPT JELEK:
"buatkan navbar"

// Hasil: navbar generic, warna random, tidak responsive, 
// tidak sesuai style project kamu

// ✅ PROMPT BAGUS (pakai CRAFT):
"Buatkan responsive navbar untuk website portfolio.
- Framework: React + Tailwind CSS
- Style: dark mode, background blur, border-bottom subtle
- Items: Home, Projects, About, Contact
- Mobile: hamburger menu yang slide dari kanan
- Logo: teks 'DevName' dengan font bold
- Active state: underline gradient purple"

// Hasil: navbar yang spesifik, sesuai kebutuhan, siap pakai`,
      },
      {
        heading: "Tips Prompt untuk Pemula",
        body: [
          "Beberapa tips yang langsung bisa kamu pakai:",
        ],
        list: [
          "Selalu sebutkan framework/tools: 'pakai React + Tailwind' atau 'HTML biasa'",
          "Sebutkan style: 'dark mode', 'minimalis', 'modern', 'colorful'",
          "Kasih contoh referensi: 'seperti navbar di stripe.com'",
          "Minta penjelasan: tambahkan 'dengan komentar di setiap bagian penting'",
          "Iterasi: kalau hasil kurang bagus, jangan tulis ulang dari awal. Bilang 'ubah warnanya jadi biru' atau 'tambahkan animasi hover'",
        ],
      },
      {
        heading: "Kesalahan Umum",
        body: [
          "Hindari kesalahan ini saat menulis prompt:",
        ],
        list: [
          "Terlalu pendek: 'buatkan form' → AI tidak tahu form untuk apa",
          "Terlalu panjang tanpa struktur: paragraf panjang yang membingungkan",
          "Tidak menyebut teknologi: AI bisa kasih jQuery padahal kamu pakai React",
          "Minta terlalu banyak sekaligus: 'buatkan full website dengan 10 halaman' → pecah jadi per-komponen",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa kepanjangan formula CRAFT untuk menulis prompt?",
          options: [
            { id: "a", text: "Code, Run, Apply, Fix, Test" },
            { id: "b", text: "Context, Role, Action, Format, Tone/Details" },
            { id: "c", text: "Create, Review, Adjust, Finalize, Transfer" },
            { id: "d", text: "Copy, Rewrite, Add, Format, Try" },
          ],
          answer: "b",
          explanation: "CRAFT = Context (konteks), Role (style/framework), Action (apa yang dilakukan), Format (format output), Tone/Details (detail tambahan).",
        },
        {
          question: "Mana prompt yang lebih baik untuk generate navbar?",
          options: [
            { id: "a", text: "'buatkan navbar'" },
            { id: "b", text: "'buatkan responsive navbar dark mode dengan React + Tailwind, 4 menu items, hamburger di mobile'" },
            { id: "c", text: "'navbar yang bagus dong'" },
            { id: "d", text: "'saya butuh navigasi'" },
          ],
          answer: "b",
          explanation: "Prompt yang spesifik menyebutkan framework, style, jumlah item, dan behavior responsive. Hasilnya jauh lebih sesuai harapan.",
        },
        {
          question: "Apa yang harus dilakukan kalau hasil AI kurang sesuai?",
          options: [
            { id: "a", text: "Tulis ulang prompt dari awal" },
            { id: "b", text: "Ganti AI tools" },
            { id: "c", text: "Iterasi: minta AI revisi bagian yang kurang tepat" },
            { id: "d", text: "Menyerah dan coding manual" },
          ],
          answer: "c",
          explanation: "Iterasi lebih efisien daripada mulai ulang. Bilang spesifik apa yang kurang: 'ubah warnanya', 'tambah padding', 'bikin responsive'.",
        },
      ],
    },
    errorChallenge: {
      title: "Prompt yang Menghasilkan Kode Buruk",
      instruction: "Prompt di bawah menghasilkan kode yang bermasalah. Identifikasi kenapa dan perbaiki promptnya.",
      buggyCode: `Prompt: "buatkan halaman login"

Hasil AI:
<div>
  <input type="text">
  <input type="text">
  <button>Login</button>
</div>

Masalah:
- Tidak ada label (accessibility buruk)
- Password field pakai type="text" (password terlihat!)
- Tidak ada styling
- Tidak ada validasi
- Tidak responsive`,
      hints: [
        "Prompt tidak menyebutkan detail: field apa saja, styling, accessibility",
        "Prompt tidak menyebutkan framework atau design requirements",
      ],
      fixedCode: `Prompt yang diperbaiki:
"Buatkan halaman login dengan React + Tailwind CSS.
- Fields: email (type email) dan password (type password)
- Setiap field ada label yang jelas
- Tombol login warna blue-600, full width
- Validasi: tampilkan error kalau field kosong
- Style: card centered, dark mode, rounded-xl
- Responsive: padding lebih kecil di mobile
- Ada link 'Lupa password?' di bawah tombol"

Hasil: form login yang lengkap, accessible, dan styled.`,
      explanation: "Prompt yang detail menghasilkan kode yang lebih lengkap. Sebutkan: fields, types, styling, validasi, accessibility, dan responsive behavior.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/generate-landing-page",
      title: "Generate Landing Page",
    },
  },

  "first-app/generate-landing-page": {
    title: "Generate Landing Page dengan AI",
    description:
      "Saatnya praktek! Kamu akan generate landing page lengkap menggunakan AI, dari prompt sampai jadi halaman yang bisa dilihat di browser.",
    readTime: "15 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "🚀",
      caption: "Dari nol ke landing page dalam 15 menit. Ini kekuatan AI coding.",
    },
    objectives: [
      "Bisa generate landing page lengkap dari prompt",
      "Paham cara menggunakan V0.dev atau Cursor untuk generate UI",
      "Bisa melihat hasil di browser lokal",
    ],
    practice: {
      fileName: "landing-page/",
      steps: [
        "Buka Cursor → File → Open Folder → buat folder baru 'landing-page-pertama'",
        "Tekan Ctrl + L untuk buka AI chat di Cursor",
        "Ketik prompt: 'Buatkan landing page untuk kursus online belajar coding. Pakai HTML + Tailwind CDN. Dark mode, hero section dengan heading besar, 3 feature cards, testimonial section, dan CTA button. Style modern dan clean.'",
        "AI akan generate kode — klik 'Apply' untuk simpan ke file",
        "Klik kanan file index.html → Open with Live Server (atau buka langsung di browser)",
        "Lihat hasilnya! Kalau ada yang kurang, ketik di chat: 'Tambahkan gradient di hero' atau 'Ubah warna jadi purple'",
      ],
      tip: "Kalau pakai V0.dev: buka v0.dev di browser, ketik prompt yang sama, lalu copy kode hasilnya ke Cursor. V0 bagus untuk dapat inspirasi visual.",
    },
    sections: [
      {
        heading: "Cara 1: Generate di Cursor (Recommended)",
        body: [
          "Cursor adalah cara paling langsung. AI generate kode dan langsung masuk ke file project kamu.",
        ],
        list: [
          "Buka Cursor → buat folder baru untuk project",
          "Tekan Ctrl + L → ketik prompt landing page kamu",
          "AI generate kode → klik Apply untuk simpan",
          "Buka file di browser untuk lihat hasil",
          "Iterasi: minta AI edit bagian yang kurang sesuai",
        ],
      },
      {
        heading: "Cara 2: Generate di V0.dev",
        body: [
          "V0.dev dari Vercel bagus untuk generate komponen UI. Hasilnya visual dan bisa langsung di-preview.",
        ],
        list: [
          "Buka v0.dev di browser",
          "Ketik prompt di chat box",
          "V0 akan generate UI dan menampilkan preview langsung",
          "Kalau suka, klik 'Code' untuk lihat kodenya",
          "Copy kode ke project Cursor kamu",
        ],
      },
      {
        heading: "Prompt untuk Landing Page",
        body: [
          "Ini contoh prompt yang menghasilkan landing page bagus:",
        ],
        code: `// Prompt untuk Cursor atau V0:

"Buatkan landing page untuk platform belajar coding online 
bernama 'CodeMaster'. Spesifikasi:

1. Hero section:
   - Heading: 'Belajar Coding dari Nol, Dibantu AI'
   - Subtitle: penjelasan singkat 2 baris
   - 2 tombol: 'Mulai Gratis' (primary) dan 'Lihat Kurikulum' (secondary)
   - Background: gradient gelap dengan accent purple

2. Features section (3 cards):
   - Card 1: AI-Powered Learning
   - Card 2: Project-Based
   - Card 3: Community Support
   - Setiap card ada icon, judul, dan deskripsi singkat

3. Testimonial section:
   - 3 testimonial dengan foto, nama, dan quote
   
4. CTA section:
   - Heading ajakan
   - Tombol sign up

Tech: HTML + Tailwind CDN. Dark mode. Responsive."`,
      },
      {
        heading: "Melihat Hasil di Browser",
        body: [
          "Setelah AI generate kode, kamu perlu melihat hasilnya di browser:",
        ],
        list: [
          "Cara 1 (Live Server): klik kanan file HTML → Open with Live Server. Otomatis buka browser",
          "Cara 2 (manual): buka File Explorer → double-click file index.html → terbuka di browser",
          "Cara 3 (terminal): ketik 'npx serve .' di terminal Cursor → buka localhost yang muncul",
        ],
      },
      {
        heading: "Iterasi: Memperbaiki Hasil",
        body: [
          "Hasil pertama jarang sempurna. Iterasi adalah bagian normal dari workflow:",
        ],
        list: [
          "Warna kurang cocok? → 'Ubah warna primary jadi violet-600'",
          "Font terlalu kecil? → 'Perbesar heading jadi text-6xl'",
          "Kurang animasi? → 'Tambahkan hover effect di cards dan fade-in saat scroll'",
          "Tidak responsive? → 'Pastikan layout stack vertical di mobile'",
          "Mau tambah section? → 'Tambahkan pricing section dengan 3 tier'",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Shortcut apa untuk membuka AI chat di Cursor?",
          options: [
            { id: "a", text: "Ctrl + K" },
            { id: "b", text: "Ctrl + L" },
            { id: "c", text: "Ctrl + P" },
            { id: "d", text: "Ctrl + N" },
          ],
          answer: "b",
          explanation: "Ctrl + L membuka AI chat panel di Cursor. Ctrl + K untuk inline prompt (edit satu bagian kode).",
        },
        {
          question: "Apa yang harus dilakukan setelah AI generate kode?",
          options: [
            { id: "a", text: "Langsung deploy tanpa cek" },
            { id: "b", text: "Lihat hasilnya di browser, lalu iterasi kalau perlu" },
            { id: "c", text: "Hapus dan generate ulang" },
            { id: "d", text: "Tulis ulang manual" },
          ],
          answer: "b",
          explanation: "Selalu preview hasil di browser dulu. Kalau ada yang kurang, iterasi dengan prompt tambahan. Jangan langsung deploy tanpa cek.",
        },
        {
          question: "Cara paling cepat melihat file HTML di browser dari Cursor?",
          options: [
            { id: "a", text: "Upload ke internet dulu" },
            { id: "b", text: "Klik kanan file → Open with Live Server" },
            { id: "c", text: "Kirim lewat email" },
            { id: "d", text: "Print halaman" },
          ],
          answer: "b",
          explanation: "Live Server extension membuka file HTML langsung di browser dan auto-refresh setiap kamu save. Cara paling cepat untuk preview.",
        },
      ],
    },
    errorChallenge: {
      title: "Landing Page yang Berantakan",
      instruction: "Hasil generate AI di bawah punya masalah. Identifikasi dan tulis prompt untuk memperbaikinya.",
      buggyCode: `Hasil AI (masalah yang terlihat di browser):
- Hero section: teks putih di background putih (tidak terbaca!)
- Cards: semua menumpuk vertikal bahkan di desktop
- Tombol: tidak ada hover effect, terlihat flat
- Mobile: teks overflow keluar layar
- Gambar: broken image (src="placeholder.jpg" tidak ada)`,
      hints: [
        "Masalah kontras warna: background dan teks warnanya sama",
        "Layout cards harusnya grid di desktop",
        "Responsive issues: perlu breakpoint yang benar",
      ],
      fixedCode: `Prompt perbaikan ke AI:
"Perbaiki landing page ini:
1. Hero: ubah background jadi dark (bg-gray-900) dengan teks putih
2. Cards: tampilkan 3 kolom di desktop (grid-cols-3), stack di mobile
3. Tombol: tambah hover effect (hover:bg-violet-700) dan transition
4. Mobile: pastikan semua teks wrap dengan benar, tambah padding
5. Gambar: ganti dengan emoji atau icon dari Lucide React
   sebagai placeholder"

Atau lebih singkat:
"Fix contrast issue di hero, bikin cards grid 3 kolom di desktop,
tambah hover effects, fix responsive, ganti broken images 
dengan emoji icons"`,
      explanation: "Saat hasil AI bermasalah, jangan generate ulang dari awal. Identifikasi masalah spesifik dan minta AI fix satu per satu. Ini lebih efisien.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/edit-hasil-ai",
      title: "Edit Hasil AI",
    },
  },

  "first-app/edit-hasil-ai": {
    title: "Edit Hasil AI: Cara Memperbaiki Output",
    description:
      "AI jarang menghasilkan kode yang 100% sempurna. Di sini kamu belajar cara mengedit, menyesuaikan, dan mempoles hasil AI supaya sesuai keinginanmu.",
    readTime: "10 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "✏️",
      caption: "AI generate draft pertama. Kamu yang memoles jadi karya final.",
    },
    objectives: [
      "Bisa mengedit teks, warna, dan layout dari kode yang di-generate AI",
      "Paham cara menggunakan Ctrl+K di Cursor untuk edit inline",
      "Tahu kapan edit manual vs minta AI revisi",
    ],
    practice: {
      fileName: "landing-page/index.html",
      steps: [
        "Buka project landing page yang kamu generate di materi sebelumnya",
        "Coba edit MANUAL: ganti teks heading langsung di kode (cari teksnya, ketik yang baru)",
        "Coba edit DENGAN AI: select bagian yang mau diubah → tekan Ctrl+K → ketik instruksi",
        "Contoh Ctrl+K: select card section → 'ubah jadi 4 cards dengan icon emoji, warna gradient berbeda tiap card'",
        "Coba ganti warna: cari 'blue' di kode (Ctrl+H) → replace semua jadi 'violet'",
        "Save (Ctrl+S) dan lihat perubahan di browser",
      ],
      tip: "Ctrl+H (Find and Replace) sangat berguna untuk ganti warna atau teks secara massal. Misalnya ganti semua 'blue-500' jadi 'purple-500' sekaligus.",
    },
    sections: [
      {
        heading: "Dua Cara Edit",
        body: [
          "Ada dua cara mengedit hasil AI di Cursor:",
        ],
        list: [
          "Edit manual: langsung ketik/hapus di kode. Cocok untuk ganti teks, angka, atau perubahan kecil",
          "Edit dengan AI (Ctrl+K): select kode → tekan Ctrl+K → tulis instruksi. Cocok untuk perubahan besar atau yang kamu tidak tahu cara manualnya",
        ],
      },
      {
        heading: "Kapan Edit Manual?",
        body: [
          "Edit manual lebih cepat untuk perubahan sederhana:",
        ],
        list: [
          "Ganti teks: heading, paragraf, nama tombol",
          "Ganti warna: ubah 'blue-500' jadi 'violet-500'",
          "Ganti ukuran: ubah 'text-2xl' jadi 'text-4xl'",
          "Hapus bagian: delete baris yang tidak perlu",
          "Ganti link: ubah href='#' jadi href yang benar",
        ],
      },
      {
        heading: "Kapan Pakai AI (Ctrl+K)?",
        body: [
          "Minta AI edit kalau perubahannya kompleks atau kamu tidak tahu caranya:",
        ],
        list: [
          "Tambah animasi: 'tambahkan fade-in animation saat scroll'",
          "Ubah layout: 'ubah dari 2 kolom jadi 3 kolom dengan gap lebih besar'",
          "Tambah fitur: 'tambahkan dark/light mode toggle'",
          "Fix responsive: 'bikin section ini stack vertical di mobile'",
          "Refactor: 'pisahkan CSS inline jadi class Tailwind yang rapi'",
        ],
      },
      {
        heading: "Teknik Edit yang Sering Dipakai",
        body: [
          "Beberapa teknik yang akan sering kamu pakai:",
        ],
        code: `// 1. Find and Replace (Ctrl+H)
// Ganti semua warna sekaligus:
Find: blue-500
Replace: violet-500
→ Klik "Replace All"

// 2. Multi-cursor (Alt+Click)
// Klik sambil tahan Alt di beberapa tempat
// Lalu ketik — semua cursor bergerak bersamaan

// 3. Select line (Ctrl+L)
// Pilih seluruh baris untuk dihapus atau dipindah

// 4. Duplicate line (Alt+Shift+Down)
// Duplikat baris ke bawah — berguna untuk bikin item serupa`,
      },
      {
        heading: "Tips: Jangan Takut Rusak",
        body: [
          "Kalau kamu sudah commit ke Git, kamu selalu bisa kembali ke versi sebelumnya. Jadi jangan takut eksperimen!",
          "Kalau edit kamu bikin error: tekan Ctrl+Z berkali-kali untuk undo. Atau minta AI: 'fix error yang muncul di kode ini'.",
        ],
        list: [
          "Ctrl+Z: undo perubahan terakhir",
          "Ctrl+Shift+Z: redo (kembalikan undo)",
          "Git: kalau sudah commit, bisa rollback kapan saja",
          "AI: paste error message ke chat, minta fix",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Shortcut apa untuk edit kode dengan AI di Cursor?",
          options: [
            { id: "a", text: "Ctrl + L" },
            { id: "b", text: "Ctrl + K (select kode dulu, lalu Ctrl+K)" },
            { id: "c", text: "Ctrl + S" },
            { id: "d", text: "Ctrl + Z" },
          ],
          answer: "b",
          explanation: "Select kode yang mau diedit → Ctrl+K → tulis instruksi. AI akan mengedit bagian yang kamu select sesuai instruksi.",
        },
        {
          question: "Untuk mengganti semua warna 'blue' jadi 'purple' sekaligus, cara tercepat?",
          options: [
            { id: "a", text: "Edit satu per satu" },
            { id: "b", text: "Ctrl+H (Find and Replace) → Replace All" },
            { id: "c", text: "Hapus file dan generate ulang" },
            { id: "d", text: "Minta AI rewrite seluruh file" },
          ],
          answer: "b",
          explanation: "Find and Replace (Ctrl+H) bisa mengganti semua kemunculan sekaligus. Jauh lebih cepat daripada edit satu per satu.",
        },
        {
          question: "Apa yang harus dilakukan kalau edit kamu bikin kode error?",
          options: [
            { id: "a", text: "Hapus seluruh project" },
            { id: "b", text: "Ctrl+Z untuk undo, atau minta AI fix errornya" },
            { id: "c", text: "Buat project baru" },
            { id: "d", text: "Abaikan error" },
          ],
          answer: "b",
          explanation: "Ctrl+Z untuk undo perubahan terakhir. Atau copy error message, paste ke AI chat, minta dia fix. Jangan panik!",
        },
      ],
    },
    errorChallenge: {
      title: "Edit yang Bikin Rusak",
      instruction: "Developer mengedit kode tapi malah bikin error. Identifikasi masalahnya.",
      buggyCode: `<!-- Kode asli (benar): -->
<div class="grid grid-cols-3 gap-4">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</div>

<!-- Setelah diedit (error): -->
<div class="grid grid-cols-3 gap-4">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3
</div>

<!-- Browser: Card 3 tidak muncul, layout berantakan -->`,
      hints: [
        "Perhatikan tag penutup </div> pada Card 3",
        "Ada tag yang hilang — setiap <div> harus punya </div> pasangannya",
      ],
      fixedCode: `<!-- Perbaikan: tambahkan </div> yang hilang -->
<div class="grid grid-cols-3 gap-4">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</div>

<!-- Tips: di Cursor, hover di error (garis merah) 
untuk lihat penjelasan. Atau tekan Ctrl+Shift+M 
untuk lihat semua error di file. -->`,
      explanation: "Saat edit manual, sering tidak sengaja menghapus tag penutup. Selalu pastikan setiap tag pembuka punya pasangan penutupnya. Cursor biasanya menandai error dengan garis merah.",
    },
    nextLesson: {
      href: "/materi/vibe/first-app/deploy-website",
      title: "Deploy Website",
    },
  },

  "first-app/deploy-website": {
    title: "Deploy Website: Publish ke Internet",
    description:
      "Website kamu sudah jadi di komputer. Sekarang saatnya publish ke internet supaya semua orang bisa akses. Pakai Vercel, gratis dan cuma butuh 5 menit.",
    readTime: "8 menit",
    level: "Level 1 — First App Experience",
    hero: {
      emoji: "🌐",
      caption: "Dari localhost ke internet. Momen pertama website kamu bisa diakses dunia.",
    },
    objectives: [
      "Bisa push kode ke GitHub",
      "Bisa connect GitHub repo ke Vercel",
      "Website live di internet dengan URL .vercel.app",
    ],
    practice: {
      fileName: "deploy-checklist.md",
      steps: [
        "Pastikan project landing page kamu sudah final (sudah diedit dan terlihat bagus di browser lokal)",
        "Buka terminal di Cursor (Ctrl + `)",
        "Kalau belum jadi git repo: ketik 'git init' lalu Enter",
        "Ketik: git add . (tambah semua file)",
        "Ketik: git commit -m 'landing page pertama'",
        "Buka github.com → klik '+' → New repository → nama: 'landing-page-pertama' → Create (JANGAN centang README)",
        "Copy perintah yang muncul di GitHub (bagian 'push an existing repository') → paste di terminal Cursor",
        "Buka vercel.com → klik 'Add New Project' → pilih repo 'landing-page-pertama' → klik Deploy",
        "Tunggu 30-60 detik → website kamu LIVE! Copy URL-nya dan buka di browser/HP",
      ],
      tip: "Setelah connect ke Vercel, setiap kamu push ke GitHub, website otomatis update. Tidak perlu deploy manual lagi!",
    },
    sections: [
      {
        heading: "Step 1: Push ke GitHub",
        body: [
          "Pertama, kode kamu harus ada di GitHub. Ikuti langkah ini:",
        ],
        code: `# Di terminal Cursor:

# Kalau folder belum jadi git repo:
git init

# Tambah semua file
git add .

# Commit
git commit -m "landing page pertama"

# Buat repo baru di github.com, lalu:
git remote add origin https://github.com/USERNAME/landing-page-pertama.git
git branch -M main
git push -u origin main`,
        list: [
          "git init: jadikan folder ini sebagai git repository",
          "git add .: tambahkan semua file ke staging",
          "git commit: simpan snapshot dengan pesan",
          "git remote add origin: hubungkan ke repo GitHub",
          "git push: upload ke GitHub",
        ],
      },
      {
        heading: "Step 2: Deploy di Vercel",
        body: [
          "Setelah kode ada di GitHub, deploy ke Vercel sangat mudah:",
        ],
        list: [
          "Buka vercel.com → login (pastikan sudah connect ke GitHub)",
          "Klik 'Add New...' → 'Project'",
          "Pilih repository 'landing-page-pertama' dari daftar",
          "Framework Preset: pilih 'Other' (karena ini HTML biasa)",
          "Klik 'Deploy'",
          "Tunggu 30-60 detik... Done! 🎉",
          "Vercel kasih URL seperti: landing-page-pertama.vercel.app",
          "Buka URL itu di browser atau HP — website kamu sudah live!",
        ],
      },
      {
        heading: "Auto-Deploy: Update Otomatis",
        body: [
          "Setelah connect, setiap kamu push ke GitHub, Vercel otomatis deploy ulang. Workflow-nya jadi:",
        ],
        list: [
          "Edit kode di Cursor",
          "git add . → git commit -m 'update hero section' → git push",
          "Vercel detect perubahan → auto deploy (30 detik)",
          "Website di internet otomatis update!",
          "Tidak perlu buka Vercel lagi — semua otomatis",
        ],
      },
      {
        heading: "Custom Domain (Opsional)",
        body: [
          "URL default dari Vercel sudah cukup untuk belajar. Tapi kalau mau domain sendiri (misal: namakamu.com):",
        ],
        list: [
          "Beli domain di Namecheap, Niagahoster, atau provider lain (~Rp 100-200rb/tahun)",
          "Di Vercel dashboard → Settings → Domains → Add domain",
          "Ikuti instruksi untuk setting DNS",
          "Dalam 5-30 menit, domain custom kamu aktif",
        ],
      },
      {
        heading: "Selamat! 🎉",
        body: [
          "Kalau kamu sampai di sini dan website kamu sudah live di internet — selamat! Kamu sudah menyelesaikan siklus lengkap: ide → generate → edit → deploy.",
          "Ini adalah workflow yang akan kamu ulangi terus. Setiap project baru, langkahnya sama. Yang berubah hanya kompleksitas dan fiturnya.",
        ],
      },
    ],
    quiz: {
      questions: [
        {
          question: "Apa yang terjadi setelah kamu connect GitHub repo ke Vercel?",
          options: [
            { id: "a", text: "Harus deploy manual setiap kali ada perubahan" },
            { id: "b", text: "Setiap push ke GitHub, Vercel otomatis deploy ulang" },
            { id: "c", text: "Website hanya bisa diakses dari komputer sendiri" },
            { id: "d", text: "Perlu bayar untuk setiap deployment" },
          ],
          answer: "b",
          explanation: "Vercel punya auto-deploy: setiap kamu push ke GitHub, dia otomatis build dan deploy ulang. Gratis untuk project personal.",
        },
        {
          question: "Urutan yang benar untuk deploy pertama kali?",
          options: [
            { id: "a", text: "Deploy → Push → Commit" },
            { id: "b", text: "Push ke GitHub → Connect Vercel → Deploy" },
            { id: "c", text: "Beli domain → Deploy → Push" },
            { id: "d", text: "Deploy → Beli domain → Push" },
          ],
          answer: "b",
          explanation: "Pertama push kode ke GitHub, lalu connect repo ke Vercel, lalu Vercel deploy otomatis. Domain custom opsional.",
        },
        {
          question: "Berapa lama biasanya Vercel deploy website sederhana?",
          options: [
            { id: "a", text: "30-60 detik" },
            { id: "b", text: "1-2 jam" },
            { id: "c", text: "24 jam" },
            { id: "d", text: "1 minggu" },
          ],
          answer: "a",
          explanation: "Untuk website sederhana (HTML + CSS), Vercel deploy dalam 30-60 detik. Sangat cepat!",
        },
      ],
    },
    errorChallenge: {
      title: "Deploy Gagal",
      instruction: "Vercel menampilkan error saat deploy. Identifikasi penyebab dan solusinya.",
      buggyCode: `Vercel Build Log:
Error: Build failed
> Build command: npm run build
> Exit code: 1

Error output:
sh: next: command not found

Atau error lain:
404 - Page not found (setelah deploy berhasil tapi 
halaman kosong)`,
      hints: [
        "Error 'next: command not found' — Vercel mengira ini project Next.js padahal cuma HTML biasa",
        "Error 404 — mungkin file utama bukan di root atau namanya bukan index.html",
      ],
      fixedCode: `Solusi error 1 (build command salah):
- Di Vercel saat deploy → buka "Build & Development Settings"
- Framework Preset: pilih "Other" (bukan Next.js)
- Build Command: kosongkan (leave empty)
- Output Directory: "." (titik, artinya root folder)
- Klik Deploy lagi

Solusi error 2 (404 setelah deploy):
- Pastikan file utama bernama "index.html" (bukan "home.html" 
  atau "main.html")
- Pastikan file ada di ROOT folder (bukan di dalam subfolder)
- Struktur yang benar:
  /index.html  ← file utama di root
  /styles.css
  /images/`,
      explanation: "Error deploy paling umum: (1) Vercel salah detect framework — fix dengan pilih 'Other' dan kosongkan build command. (2) File utama harus bernama index.html dan ada di root folder.",
    },
    nextLesson: {
      href: "/materi/vibe/basic-app-building/frontend-backend",
      title: "Frontend & Backend",
    },
  },
};

// Helper function to get a specific vibe lesson by level and lesson slug
export function getVibeLesson(levelSlug, lessonSlug) {
  const key = `${levelSlug}/${lessonSlug}`;
  return vibeContent[key] || null;
}
