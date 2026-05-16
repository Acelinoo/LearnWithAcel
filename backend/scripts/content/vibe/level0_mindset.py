"""
Vibe / Level 0 — Mindset & Orientation.

Lessons:
  1. apa-itu-vibe-coding
  2. tools-ecosystem
  3. cara-berpikir-dalam-prompt
  4. mini-project-mapping-workflow  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Apa itu Vibe Coding
# ─────────────────────────────────────────────────────────────────────────────

LESSON_APA_ITU = make_lesson(
    title="Apa itu Vibe Coding",
    slug="apa-itu-vibe-coding",
    order_index=1,
    read_time="7 menit",
    summary="Mendefinisikan AI-assisted development dan menyetel ekspektasi.",
    tools=["Browser modern", "Notes app untuk catatan"],
    outcomes=[
        "Memahami definisi Vibe Coding dengan jelas",
        "Membedakan No-Code, Low-Code, AI Coding, dan Manual",
        "Menyetel ekspektasi: apa yang realistis dan apa yang tidak",
    ],
    tldr=(
        "Vibe Coding = membangun app modern dengan AI sebagai asisten coding. "
        "Bukan no-code, bukan ngandelin AI sepenuhnya. Kamu tetap harus "
        "ngerti, bukan sekadar copy-paste."
    ),
    pembuka=dedent(
        """\
        Lima tahun lalu, kalau kamu mau bikin website, kamu wajib hafal HTML, CSS, JavaScript, framework, dan deploy.

        Sekarang banyak hal itu bisa dibantu AI. Tapi kabar buruknya: orang yang "cuma copy-paste dari ChatGPT" sering kelihatan banget.

        Vibe Coding adalah jalan tengah: kamu pakai AI sebagai partner, tapi kamu tetap ngerti apa yang kamu bangun.
        """
    ),
    penjelasan=dedent(
        """\
        ### Definisi sederhana

        Vibe Coding adalah AI-assisted development. Kamu pakai AI untuk:

        - Generate UI dengan cepat.
        - Bikin function repetitif.
        - Debug error.
        - Refactor kode.

        Tapi kamu tetap pegang kontrol arah, struktur, dan keputusan akhir.

        ### Empat pendekatan, satu spektrum

        Pikirkan ini sebagai garis horizontal:

        - **No-Code** (Bubble, Webflow). Klik-klik tanpa nulis code. Cocok untuk MVP super cepat. Batasannya banyak begitu app makin kompleks.
        - **Low-Code** (Retool, Airtable). Sebagian visual, sebagian code. Bagus untuk internal tools.
        - **AI Coding / Vibe Coding**. Kamu nulis app, tapi AI bantu di setiap langkah. Hasilnya kode beneran yang kamu sendiri pegang.
        - **Manual Coding**. Semua kamu tulis sendiri. Lambat tapi paling fleksibel.

        Vibe Coding sweet spot di antara dua ujung: lebih cepat dari manual, lebih fleksibel dari no-code.

        ### Kenapa sekarang masuk akal

        Tools-nya sudah matang. Cursor bisa baca seluruh project kamu. Claude bisa nulis komponen kompleks. Vercel + Supabase bikin deploy gratis dan instan.

        Hambatan terbesar bukan teknologi lagi. Hambatan terbesar adalah taste — kemampuan kamu mengenali mana yang bagus dan mana yang jelek.

        ### Yang realistis

        - Bikin landing page bagus dalam satu hari.
        - Bikin SaaS sederhana dengan auth dan database dalam dua minggu.
        - Bikin tools internal untuk tim kecil dalam beberapa hari.

        ### Yang TIDAK realistis

        - Bikin Facebook dalam seminggu.
        - "AI ngerjain semua, saya tinggal duduk".
        - Bikin app tanpa pernah baca kode hasilnya.

        Aturan emas: kamu tetap harus ngerti, bukan sekadar copy-paste.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh prompt awal yang bagus untuk Cursor atau Claude:

        ```text
        Aku mau bikin landing page untuk toko kopi lokal.
        Stack: Next.js 14 App Router + Tailwind + shadcn/ui.

        Section yang dibutuhkan:
        1. Hero dengan judul, tagline, dan CTA "Pesan sekarang".
        2. Menu produk (4 kopi, masing-masing punya foto, nama, harga).
        3. Tentang Kami (cerita singkat 2-3 paragraf).
        4. Footer dengan alamat, jam buka, dan social media.

        Style: minimal, dark mode, accent warna #4EBAEC.
        Responsive untuk mobile dan desktop.

        Mulai dari struktur file dulu, jangan langsung kasih semua kode.
        ```

        Perhatikan: kamu kasih konteks (stack, section, style, behavior). AI yang bagus akan tanya balik kalau ada yang ambigu.
        """
    ),
    practice=(
        "Tulis di catatan kamu: apa satu app yang ingin kamu bangun dalam 3 "
        "bulan ke depan? Tuliskan dalam satu paragraf, sebut user-nya siapa, "
        "masalahnya apa, dan solusinya bagaimana. Ini akan jadi target sambil "
        "kamu jalan di jalur Vibe Coding."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Prompt: "Bikinkan saya app."
            """
        ),
        "hint": (
            "Prompt yang bagus selalu punya konteks (stack), spesifik (apa "
            "yang dibangun), dan format keluaran (struktur file dulu, atau "
            "langsung code)."
        ),
        "answer_explanation": dedent(
            """\
            Prompt minimalis di atas akan kasih hasil generic. AI tidak tahu kamu mau apa.

            Yang lebih baik: sebut stack, fitur utama, style, dan cara mulai (struktur file dulu, bukan langsung implementasi).
            """
        ),
        "fixed_code": dedent(
            """\
            Prompt:
            "Bikin todo app sederhana.
            Stack: Next.js 14 + Tailwind.
            Fitur: tambah, hapus, tandai selesai. Data di localStorage.
            Style: minimal, dark mode, font Inter.
            Mulai dari struktur file, lalu kita iterate per komponen."
            """
        ),
    },
    quiz=[
        q(
            "Mana definisi Vibe Coding yang paling tepat?",
            [
                "Bikin app tanpa nulis kode sama sekali",
                "AI-assisted development di mana kamu pakai AI sebagai partner tapi tetap pegang kontrol",
                "Bikin app dengan visual editor seperti Webflow",
                "Hanya pakai ChatGPT untuk bikin website",
            ],
            "B",
            "Vibe Coding adalah middle ground antara no-code dan manual coding. AI bantu, tapi kamu yang pegang arah.",
        ),
        q(
            "Apa yang membedakan Vibe Coding dari No-Code (Webflow, Bubble)?",
            [
                "Vibe Coding lebih lambat",
                "Vibe Coding menghasilkan kode beneran yang kamu sendiri pegang dan modifikasi",
                "Vibe Coding tidak butuh internet",
                "Tidak ada bedanya",
            ],
            "B",
            "No-Code menyembunyikan kode. Vibe Coding tetap menghasilkan kode yang kamu sendiri bisa baca, modifikasi, dan deploy.",
        ),
        q(
            "Apa yang TIDAK realistis dari Vibe Coding?",
            [
                "Bikin landing page dalam sehari",
                "Bikin SaaS sederhana dalam dua minggu",
                "Bikin Facebook lengkap dalam seminggu tanpa baca kode",
                "Bikin tools internal dalam beberapa hari",
            ],
            "C",
            "Vibe Coding mempercepat, tapi ada batasnya. Project skala besar butuh struktur, testing, infrastruktur — tidak bisa dipotong drastis.",
        ),
        q(
            "Mengapa 'taste' penting di era Vibe Coding?",
            [
                "Tidak penting, AI selalu benar",
                "Karena AI bisa generate banyak hal, kamu yang harus menilai mana yang bagus dan mana yang jelek",
                "Untuk impress recruiter",
                "Karena tools-nya butuh sertifikat",
            ],
            "B",
            "AI bisa kasih banyak opsi, tapi kamu yang pegang taste — yang tahu mana yang bagus untuk user-mu.",
        ),
        q(
            "Mana prompt yang lebih baik untuk AI?",
            [
                "\"Bikin website saya.\"",
                "\"Bikin landing page Next.js + Tailwind untuk toko kopi, dark mode, ada section hero/menu/tentang, mulai dari struktur file dulu.\"",
                "\"Tolong bantu.\"",
                "\"Saya butuh kode.\"",
            ],
            "B",
            "Prompt yang baik = konteks + spesifik + format output. Itu bikin hasil AI lebih akurat dan lebih cepat sampai ke yang kamu mau.",
        ),
    ],
    common_mistakes=[
        "Mengira Vibe Coding = ChatGPT semua. Faktanya: kamu tetap ngerti yang kamu bangun.",
        "Skip dasar coding. Saat ada bug, kamu tidak bisa apa-apa.",
        "Prompt terlalu pendek. AI tidak bisa baca pikiran. Kasih konteks.",
    ],
    checkpoint=[
        "Bisa menjelaskan Vibe Coding ke orang awam.",
        "Tahu beda no-code, low-code, AI coding, manual.",
        "Punya target satu app yang ingin dibangun.",
    ],
    xp_reward=50,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Tools Ecosystem
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TOOLS = make_lesson(
    title="Tools Ecosystem Overview",
    slug="tools-ecosystem",
    order_index=2,
    read_time="9 menit",
    summary="Cursor, Claude, ChatGPT, V0, Bolt — kapan pakai yang mana.",
    tools=[
        "Akun ChatGPT atau Claude (gratis dulu)",
        "Akun GitHub",
        "Akun Vercel",
    ],
    outcomes=[
        "Mengenali tools utama Vibe Coding",
        "Tahu kapan pakai code editor AI vs chat assistant vs UI generator",
        "Memilih kombinasi yang cocok untuk pemula",
    ],
    tldr=(
        "Cursor untuk nulis kode dengan AI di editor. Claude/ChatGPT untuk "
        "diskusi panjang dan refactor. V0/Bolt untuk generate UI. GitHub + "
        "Vercel + Supabase untuk simpan, deploy, dan database."
    ),
    pembuka=dedent(
        """\
        Banyak orang bingung mulai dari mana karena tools-nya banyak.

        Kabar baik: kamu tidak perlu pakai semua. Mulai dengan dua atau tiga, lalu tambah seiring kebutuhan.

        Lesson ini bukan promo tools. Ini peta supaya kamu paham fungsinya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Code Editor dengan AI

        - **Cursor.** Fork dari VS Code yang punya AI built-in. Bisa baca seluruh project. Aksi favorit: ⌘K untuk edit inline, ⌘L untuk chat.
        - **GitHub Copilot.** Plugin di VS Code. Lebih ringan, tapi tidak sepowerful Cursor untuk diskusi multi-file.

        Pilih satu. Kalau ragu, mulai dari **Cursor** karena sudah jadi default banyak indie builder.

        ### Chat Assistant

        - **Claude (Anthropic).** Sangat bagus untuk reasoning panjang dan refactor besar. Output kode-nya rapi.
        - **ChatGPT (OpenAI).** Versatile, ekosistem plugin banyak. GPT-5 cepat dan akurat untuk coding.

        Banyak builder pakai keduanya — Claude untuk perencanaan dan refactor, ChatGPT untuk eksekusi cepat. Tidak wajib. Mulai dari satu.

        ### UI Generator

        - **V0 (Vercel).** Generate komponen React + Tailwind dari prompt. Hasilnya bisa langsung ditempel ke Cursor.
        - **Bolt.new (StackBlitz).** Generate full app yang langsung jalan di browser. Cocok untuk prototyping.
        - **Lovable.** Mirip Bolt, fokus full-stack.

        Pakai ini untuk start awal. Lanjutan biasanya di Cursor.

        ### Hosting & Storage

        - **GitHub.** Tempat simpan kode. Wajib.
        - **Vercel.** Deploy frontend Next.js dalam 30 detik. Wajib.
        - **Supabase.** PostgreSQL hosted gratis + auth + storage. Pintu masuk yang ramah ke backend.

        Ketiganya gratis untuk pemula. Itu sudah cukup untuk launch app pertamamu.

        ### Stack rekomendasi pemula

        Cursor + Claude + GitHub + Vercel + Supabase. Lima ini cukup untuk membangun app produksi sederhana. Jangan tambah lagi sampai kamu butuh.
        """
    ),
    contoh_code_md=dedent(
        """\
        Alur kerja umum:

        ```text
        1. Buka V0 → kasih prompt → dapat komponen React + Tailwind.
        2. Salin ke project Next.js di Cursor.
        3. Pakai ⌘K di Cursor untuk modifikasi sesuai kebutuhan.
        4. Push ke GitHub.
        5. Vercel auto-deploy.
        6. Pasang database via Supabase kalau butuh data persisten.
        ```

        Salah satu kekuatan stack ini: feedback loop yang sangat cepat. Dari ide ke deploy bisa di bawah satu jam.
        """
    ),
    practice=(
        "Buat akun di tiga tools wajib: GitHub, Vercel, dan Cursor. Login, "
        "verifikasi email kalau diminta. Tidak perlu install apa-apa dulu — "
        "tujuannya cuma punya akses siap pakai. Catat email yang dipakai supaya "
        "tidak lupa."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            "Saya install semua: Cursor, ChatGPT, Claude, V0, Bolt, Lovable,
            Replit, Supabase, Firebase, Vercel, Netlify, Railway, dan
            10 plugin VS Code. Tapi sekarang saya bingung mulai dari mana."
            """
        ),
        "hint": "Tools yang banyak bukan masalah skill. Itu masalah fokus.",
        "answer_explanation": dedent(
            """\
            Kesalahan: Pakai semua tools sekaligus tanpa tahu mana yang dipakai untuk apa. Akhirnya energi habis di setup, bukan di membangun.

            Yang benar: pilih stack minimal (Cursor + Claude + GitHub + Vercel + Supabase), kuasai itu dulu, baru tambah kalau ada kebutuhan nyata.
            """
        ),
        "fixed_code": dedent(
            """\
            Stack pemula:
            - Cursor (code editor + AI)
            - Claude atau ChatGPT (chat assistant)
            - GitHub (simpan kode)
            - Vercel (deploy frontend)
            - Supabase (database + auth)

            Itu sudah cukup. Tambah tools cuma kalau kamu sudah merasa
            stack ini terbatas untuk kebutuhanmu.
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi Cursor di alur Vibe Coding?",
            [
                "Browser khusus untuk developer",
                "Code editor dengan AI built-in yang bisa baca seluruh project",
                "Database hosting",
                "Tempat deploy app",
            ],
            "B",
            "Cursor itu fork dari VS Code dengan integrasi AI. Bisa baca konteks project secara luas, beda dari assistant chat biasa.",
        ),
        q(
            "Vercel paling sering dipakai untuk apa?",
            [
                "Bikin database",
                "Generate komponen UI",
                "Deploy frontend (terutama Next.js) dalam beberapa detik",
                "Editing video",
            ],
            "C",
            "Vercel adalah platform hosting yang dibuat oleh tim Next.js. Push ke GitHub, Vercel auto-deploy.",
        ),
        q(
            "Apa fungsi V0?",
            [
                "Code editor",
                "Generate komponen React + Tailwind dari prompt",
                "Database",
                "Email hosting",
            ],
            "B",
            "V0 (Vercel) adalah UI generator. Output-nya kode React + Tailwind yang bisa langsung dipakai di project.",
        ),
        q(
            "Mana stack minimal yang direkomendasikan untuk pemula Vibe Coding?",
            [
                "Cursor + Claude/ChatGPT + GitHub + Vercel + Supabase",
                "10 tools sekaligus supaya komplit",
                "Cuma ChatGPT, sisanya tidak perlu",
                "Wajib pakai Replit dan Railway",
            ],
            "A",
            "Lima tools ini cukup untuk launch app produksi sederhana. Tambah lagi kalau memang ada kebutuhan nyata.",
        ),
        q(
            "Kenapa pemula sebaiknya TIDAK install semua tools sekaligus?",
            [
                "Karena ribet bayar semuanya",
                "Karena energi habis di setup, bukan di membangun. Lebih baik kuasai stack minimal dulu.",
                "Karena dilarang oleh aturan tertentu",
                "Tidak ada alasan",
            ],
            "B",
            "Setiap tools butuh waktu adaptasi. Setup overhead bisa membunuh semangat. Mulai minimal, tambah saat butuh.",
        ),
    ],
    common_mistakes=[
        "Install semua tools sebelum bangun apapun. Hasilnya: setup overhead besar.",
        "Bingung mana untuk apa, lalu nanya ke beberapa AI dengan prompt yang sama.",
        "Skip belajar editor. Cursor punya keyboard shortcut yang menggandakan kecepatan.",
    ],
    checkpoint=[
        "Punya akun GitHub, Vercel, dan Cursor.",
        "Tahu fungsi masing-masing tools dalam stack.",
        "Memilih satu chat assistant utama (Claude atau ChatGPT).",
    ],
    xp_reward=60,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Cara Berpikir dalam Prompt
# ─────────────────────────────────────────────────────────────────────────────

LESSON_PROMPT = make_lesson(
    title="Cara Berpikir dalam Prompt",
    slug="cara-berpikir-dalam-prompt",
    order_index=3,
    read_time="10 menit",
    summary="Konteks, spesifik, iteratif — anatomi prompt yang menghasilkan kode bagus.",
    tools=["Akun ChatGPT atau Claude", "Notes app"],
    outcomes=[
        "Memahami anatomi prompt yang efektif",
        "Memberikan konteks yang cukup ke AI",
        "Iterasi prompt untuk perbaiki output yang kurang",
    ],
    tldr=(
        "Prompt yang bagus punya konteks (stack, env), spesifik (apa yang "
        "diminta), dan format output (struktur dulu vs code langsung). "
        "Kalau hasil jelek, suruh AI revisi outputnya sendiri."
    ),
    pembuka=dedent(
        """\
        AI bukan dukun. Dia tidak bisa baca pikiran kamu.

        Kalau kamu kasih prompt yang vague, hasilnya juga vague. Kalau kamu kasih prompt yang spesifik dengan konteks, hasilnya jauh lebih akurat.

        Prompt itu skill yang bisa diasah. Lesson ini cuma awalnya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Anatomi prompt yang baik

        Tiga bagian:

        - **Konteks.** Tools, stack, file yang relevan, tujuan akhir.
        - **Spesifik.** Apa yang kamu mau, bukan "bantu dong".
        - **Format output.** Mau dapat struktur file dulu? Code langsung? Penjelasan step-by-step?

        Tambahan opsional: contoh input/output yang kamu harapkan.

        ### Prompt yang BURUK

        - "Bikin website."
        - "Tolong dibetulkan."
        - "Code-nya error, fix."

        Ketiganya minim konteks. AI akan ngarang.

        ### Prompt yang BAIK

        - "Bikin landing page Next.js 14 + Tailwind untuk toko kopi lokal. Ada section hero, menu (4 produk dummy), tentang kami, footer. Dark mode, accent #4EBAEC. Mulai dari struktur file dulu."
        - "Saya dapat error 'Cannot read property X of undefined' di file Y baris Z saat klik tombol login. Berikut kode lengkap file-nya: [paste]. Tolong analisis kemungkinan penyebab dan kasih saran perbaikan."

        ### Iteratif itu wajar

        Prompt pertama jarang langsung perfect. Kalau output AI kurang, **balik diskusi**, jangan mulai dari nol.

        Cara minta revisi yang baik:

        - "Kode di atas oke, tapi tolong ganti styling jadi minimal (kurangi shadow, tipiskan border). Pertahankan struktur."
        - "Lupa sebut, semua harus responsive di HP. Update kode di atas."
        - "Hapus penggunaan library X, ganti dengan native Y."

        ### Kapan re-prompt vs re-mulai?

        Kalau AI mulai keluar dari topik atau ngotot di solusi yang tidak kamu mau setelah 2-3 putaran — buka chat baru dengan prompt yang sudah dirapikan.

        ### Kasih AI peran kalau perlu

        "Anggap kamu reviewer kode senior. Cek file ini dan kasih kritik yang spesifik tentang readability, performance, dan accessibility."

        Kasih peran membantu AI fokus ke sudut pandang yang kamu mau.
        """
    ),
    contoh_code_md=dedent(
        """\
        Format prompt template yang bisa kamu pakai berkali-kali:

        ```text
        Konteks:
        - Project: [nama / deskripsi singkat]
        - Stack: [Next.js 14, Tailwind, dll.]
        - File yang relevan: [paste atau ringkasan]

        Yang saya butuhkan:
        - [tugas spesifik, misal: bikin komponen Card untuk product listing]

        Format output:
        - [Mulai dari struktur dulu / langsung code / explain dulu lalu code]

        Catatan tambahan:
        - [responsive, accessible, dark mode, dll.]
        ```

        Template ini menghemat waktu di setiap sesi. Salin lalu isi.
        """
    ),
    practice=(
        "Tulis prompt untuk bikin component 'NavBar' di Next.js + Tailwind. "
        "Pakai template di atas: konteks, kebutuhan, format output, catatan. "
        "Kirim ke ChatGPT/Claude. Lalu minta revisi: 'Tambah dark mode toggle.'"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "Bikin komponen tombol."
            AI: [output generic <button>Click me</button>]
            User: "Bukan kayak gitu."
            AI: [output generic kedua, juga tidak match]
            User: "Salah lagi!"
            """
        ),
        "hint": (
            "User memberi feedback negatif tanpa kasih arah baru. AI butuh "
            "informasi konkret tentang APA yang kurang."
        ),
        "answer_explanation": dedent(
            """\
            Kesalahan: User memberi feedback "salah" tanpa menjelaskan apa yang salah dan apa yang diharapkan.

            Yang benar: feedback harus konkret. "Tombol terlalu generic. Saya butuh tombol primary dengan icon di kiri, ukuran besar, untuk CTA hero. Stack Next.js + Tailwind."
            """
        ),
        "fixed_code": dedent(
            """\
            User: "Bikin komponen tombol primary dengan icon di kiri, padding
            besar, untuk CTA hero. Stack Next.js + Tailwind. Background
            #4EBAEC, hover sedikit lebih gelap. Pakai TypeScript."

            AI: [output yang lebih akurat dengan props icon, size, dan style]

            User: "Bagus. Sekarang tambah variant 'secondary' dengan border
            putih dan background transparan."

            AI: [tambah variant dengan props yang konsisten]
            ```
        """),
    },
    quiz=[
        q(
            "Mana komponen utama dari prompt yang baik?",
            [
                "Hanya emoji",
                "Konteks, spesifik, dan format output",
                "Sebut nama AI-nya secara berulang",
                "Pakai bahasa Inggris saja",
            ],
            "B",
            "Konteks (stack/file), spesifik (apa yang diminta), format output (cara penyajian) — itu tiga pilar prompt yang efektif.",
        ),
        q(
            "Apa yang lebih baik dilakukan saat output AI kurang sesuai?",
            [
                "Mulai chat baru tanpa konteks",
                "Tulis 'salah' lalu tunggu AI menebak",
                "Iterasi: jelaskan SPESIFIK apa yang kurang dan apa yang diharapkan",
                "Tinggalkan AI dan tulis manual",
            ],
            "C",
            "AI butuh feedback konkret. \"Tombolnya terlalu generic, saya butuh primary dengan icon\" jauh lebih efektif daripada \"salah\".",
        ),
        q(
            "Kapan sebaiknya mulai chat baru, bukan iterasi?",
            [
                "Setiap kali",
                "Saat AI sudah keluar topik atau ngotot di solusi yang tidak kamu mau setelah 2-3 putaran",
                "Saat capek mengetik",
                "Setiap pagi",
            ],
            "B",
            "Chat lama bisa terkontaminasi dengan asumsi salah. Mulai baru dengan prompt yang sudah dirapikan biasanya lebih efisien.",
        ),
        q(
            "Mana prompt yang LEBIH BAIK?",
            [
                "\"Tolong fix bug.\"",
                "\"Saya error 'Cannot read property X of undefined' di file Y baris Z saat klik login. Kode file: [paste]. Stack: Next.js + Prisma. Tolong analisis penyebab dan kasih saran perbaikan.\"",
                "\"Code error, gimana?\"",
                "\"Apa salahnya?\"",
            ],
            "B",
            "Prompt yang baik kasih: error message, lokasi, konteks tindakan user, kode terkait, stack, dan format yang kamu mau.",
        ),
        q(
            "Apa fungsi 'kasih peran' di prompt (misal: 'Anggap kamu reviewer senior')?",
            [
                "Tidak ada fungsi, sekadar basa-basi",
                "Membantu AI fokus ke sudut pandang yang kamu mau",
                "Mengubah AI jadi kode robot",
                "Dilarang oleh aturan",
            ],
            "B",
            "Memberi peran membantu AI menyesuaikan tone dan kedalaman analisis. \"Reviewer senior\" akan lebih kritis dan spesifik daripada AI tanpa peran.",
        ),
    ],
    common_mistakes=[
        "Prompt 'tolong fix'. AI tidak tahu apa yang harus diperbaiki tanpa konteks.",
        "Mulai dari nol setiap kali AI kurang akurat. Lebih efisien iterasi dengan feedback spesifik.",
        "Tidak menyebut stack. AI memilih library default yang mungkin tidak cocok dengan project-mu.",
    ],
    checkpoint=[
        "Punya template prompt sendiri.",
        "Bisa kasih feedback spesifik untuk minta revisi.",
        "Tahu kapan iterasi vs kapan mulai chat baru.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_MAPPING = make_lesson(
    title="Mini Project — Mapping Workflow Pribadi",
    slug="mini-project-mapping-workflow",
    order_index=4,
    read_time="60 menit",
    summary="Susun workflow Vibe Coding pribadi sebelum bangun app pertama.",
    tools=["Notion / Notes app", "Akun GitHub, Vercel, Cursor"],
    outcomes=[
        "Punya peta workflow pribadi yang jelas",
        "Tahu posisi tiap tools dalam alur kerja",
        "Siap mental untuk Level 1: bangun app pertama yang live",
    ],
    tldr=(
        "Buat dokumen pribadi yang merangkum: stack pilihan, alur kerja dari "
        "ide ke deploy, contoh prompt yang bagus, dan goal jangka pendek. "
        "Ini akan jadi rujukan kamu di level berikutnya."
    ),
    pembuka=dedent(
        """\
        Sebelum mulai bangun, mari pastikan peta sudah jelas.

        Project ini bukan coding. Ini dokumen workflow yang akan kamu pakai berulang di level-level berikutnya.

        Tujuannya: kamu tidak buang waktu mikir "tools mana ya?" setiap kali mau mulai sesuatu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Outline dokumen yang dibuat

        Buat satu file di Notion atau notes app dengan struktur berikut.

        - **Stack pilihan saya.** Tulis lima tools utama yang akan kamu pakai. Boleh sama dengan rekomendasi (Cursor + Claude/ChatGPT + GitHub + Vercel + Supabase), boleh disesuaikan.
        - **Alur kerja saya dari ide ke deploy.** Tulis langkah-langkah dalam list bernomor. Misal: 1) tulis ide, 2) draft prompt awal, 3) generate UI di V0, dst.
        - **Template prompt favorit saya.** Salin template dari lesson sebelumnya, sesuaikan dengan gaya kamu.
        - **Goal 30 hari ke depan.** Satu app yang ingin kamu bangun. Tulis judul, user-nya siapa, masalah yang dipecahkan, dan satu fitur paling penting.
        - **Daftar tools yang TIDAK akan saya install dulu.** Penting supaya kamu punya batas. "Saya akan tahan godaan install Replit, Railway, atau Lovable sampai saya butuh."

        ### Kenapa ini penting

        Tanpa dokumen ini, kamu akan terombang-ambing antar tutorial. Tiap tutorial punya stack berbeda. Kalau kamu ikuti semua, kamu tidak akan menyelesaikan apapun.

        Dokumen ini jadi alat **fokus**. Ketika ragu, kembalikan ke dokumen.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh isi dokumen:

        ```markdown
        # Workflow Vibe Coding Pribadi — [Nama Saya]

        ## Stack pilihan
        - Cursor (editor)
        - Claude (planning + refactor)
        - GitHub (simpan kode)
        - Vercel (deploy frontend)
        - Supabase (database + auth)

        ## Alur kerja standar saya
        1. Tulis ide singkat di Notes (1 paragraf).
        2. Buat prompt awal pakai template, kirim ke Claude untuk plan.
        3. Setup project Next.js + Tailwind di Cursor.
        4. Generate komponen UI di V0 saat butuh, salin ke project.
        5. Iterasi di Cursor (⌘K) untuk modifikasi.
        6. Push ke GitHub setiap fitur selesai.
        7. Vercel auto-deploy. Cek di HP.

        ## Template prompt favorit
        [salin template dari lesson 3]

        ## Goal 30 hari
        - Project: "Habit Tracker untuk Pelajar".
        - User: pelajar SMA yang mau bangun rutinitas belajar.
        - Masalah: gampang lupa rutinitas baru.
        - Fitur paling penting: list rutinitas + check-in harian + streak.

        ## Tools yang TIDAK saya install dulu
        - Replit, Railway, Lovable, Bolt, Firebase.
        ```
        """
    ),
    practice=(
        "Buat dokumen di atas hari ini. Tidak harus panjang. Cukup jujur dan "
        "spesifik. Simpan di tempat yang gampang kamu buka, misal Notion "
        "halaman bookmarked atau file Markdown di GitHub repo pribadi."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            "Stack saya: pakai apa saja yang lagi trending. Goal: bikin app
            keren. Workflow: improvisasi."
            """
        ),
        "hint": "Komitmen yang vague tidak akan menjaga fokus saat tantangan datang.",
        "answer_explanation": dedent(
            """\
            Kesalahan: Tidak ada keputusan konkret. Saat eksekusi, kamu akan kembali bingung.

            Yang benar: keputusan eksplisit di tiap bagian. Stack disebutkan satu per satu. Goal punya user, masalah, fitur. Workflow punya step bernomor.
            """
        ),
        "fixed_code": dedent(
            """\
            Stack: Cursor, Claude, GitHub, Vercel, Supabase.
            Goal 30 hari: Habit Tracker untuk pelajar SMA. Fitur paling
            penting: list rutinitas + check-in harian + streak.
            Workflow: 1) draft ide, 2) prompt awal, 3) setup project,
            4) generate UI, 5) iterasi, 6) deploy, 7) test di HP.
            """
        ),
    },
    quiz=[
        q(
            "Apa tujuan utama Mini Project Level 0 ini?",
            [
                "Belajar coding dasar",
                "Membuat dokumen workflow pribadi sebagai alat fokus dan rujukan",
                "Deploy app pertama",
                "Bikin database",
            ],
            "B",
            "Project ini meta — bukan coding, tapi menyiapkan peta agar level berikutnya lebih efektif.",
        ),
        q(
            "Bagian 'tools yang TIDAK akan saya install dulu' itu fungsinya apa?",
            [
                "Tidak penting, hanya basa-basi",
                "Menjaga fokus dan mencegah tools-fatigue",
                "Untuk dipamerkan",
                "Sebagai daftar belanja",
            ],
            "B",
            "Punya batas eksplisit menjaga kamu dari godaan install tools baru tiap kali ada hype.",
        ),
        q(
            "Apa karakteristik 'goal 30 hari' yang baik?",
            [
                "Vague seperti 'bikin app keren'",
                "Spesifik: punya user, masalah, dan satu fitur paling penting",
                "Sangat besar seperti 'clone Instagram'",
                "Tanpa target waktu",
            ],
            "B",
            "Goal yang spesifik bisa dieksekusi. Goal vague atau terlalu besar bikin kamu gampang menyerah.",
        ),
        q(
            "Kenapa 'alur kerja dari ide ke deploy' perlu ditulis?",
            [
                "Supaya kelihatan profesional",
                "Supaya kamu tidak buang waktu mikir step yang sama berulang setiap mulai project",
                "Supaya bisa dipajang di GitHub",
                "Tidak perlu sebenarnya",
            ],
            "B",
            "Alur yang sudah disepakati dengan diri sendiri menghemat decision fatigue. Tinggal jalan.",
        ),
        q(
            "Apa yang BUKAN bagian dari dokumen workflow ini?",
            [
                "Stack pilihan",
                "Template prompt favorit",
                "Goal 30 hari",
                "Daftar 50 framework yang harus dikuasai",
            ],
            "D",
            "Dokumen ini soal fokus dan minimalis. Bukan checklist materi belajar.",
        ),
    ],
    common_mistakes=[
        "Skip lesson ini karena 'bukan coding'. Padahal foundation untuk level berikutnya.",
        "Stack ditulis terlalu banyak. Tujuannya minimal, bukan komprehensif.",
        "Goal terlalu besar. 'Clone Instagram dalam 30 hari' tidak realistis.",
    ],
    checkpoint=[
        "Punya dokumen workflow pribadi yang bisa dibuka dengan cepat.",
        "Stack jelas, terbatas pada lima tools.",
        "Punya satu goal 30 hari yang spesifik.",
    ],
    xp_reward=120,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=0,
    slug="mindset-orientation",
    title="Mindset & Orientation",
    subtitle="Pahami dunia AI coding sebelum mulai",
    description=(
        "Sebelum menyentuh tools, pahami dulu apa itu Vibe Coding, bagaimana "
        "AI coding bekerja, dan apa yang realistis dan tidak. Tutup level ini "
        "dengan dokumen workflow pribadi sebagai peta untuk level berikutnya."
    ),
    duration="~3 hari",
    difficulty="Pemula",
    accent_color="from-violet-500/30 to-fuchsia-500/10",
    mini_project="Mapping Workflow Pribadi",
    tags=["AI", "Mindset", "Workflow", "Tools"],
    lessons=[LESSON_APA_ITU, LESSON_TOOLS, LESSON_PROMPT, PROJECT_MAPPING],
)
