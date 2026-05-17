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
    summary="Sebenernya Vibe Coding itu apa, dan kenapa lagi rame.",
    tools=["Browser apa aja", "Notes / Google Keep buat catat"],
    outcomes=[
        "Tahu Vibe Coding itu apa, jelas",
        "Tahu bedanya sama no-code dan coding manual",
        "Punya gambaran realistis: bisa apa, gak bisa apa",
    ],
    tldr=(
        "Vibe Coding = ngoding tapi AI ikut bantu. Bukan no-code, bukan juga "
        "ngandelin AI 100%. Kamu tetep harus ngerti yang kamu bikin, AI cuma "
        "mempercepat."
    ),
    pembuka=dedent(
        """\
        Lima tahun lalu kalau mau bikin website, kamu wajib hafal HTML, CSS, JavaScript, framework, terus belajar deploy. Lama dan capek.

        Sekarang banyak hal kayak gitu bisa dibantu AI. Tapi yang bikin orang sering ketipu: ngira semua bisa diserahin ke ChatGPT, terus dia bisa langsung jadi developer.

        Vibe Coding itu jalan tengahnya. Kamu pake AI buat ngebantu, tapi kamu tetep yang nyetir.
        """
    ),
    penjelasan=dedent(
        """\
        ### Definisinya simpel

        Vibe Coding artinya kamu ngoding sambil dibantu AI. AI yang dipake buat:

        - Bikin tampilan dengan cepet
        - Nulisin function yang berulang-ulang
        - Bantu cari tau kenapa kode error
        - Refactor kode yang berantakan

        Tapi yang nentuin mau bikin apa, struktur kayak gimana, fitur mana yang penting — itu kamu. Bukan AI.

        ### Empat cara bikin app, beda-beda

        Sekarang ada empat cara orang bikin app. Dari yang paling gampang sampai yang paling fleksibel:

        - **No-code** — kayak Bubble, Webflow. Klik-klik doang, gak nulis kode. Cepet banget buat MVP, tapi kalau app makin kompleks suka mentok.
        - **Low-code** — kayak Retool, Airtable. Setengah visual, setengah kode. Cocok buat bikin tools internal kantor.
        - **AI Coding / Vibe Coding** — kamu nulis app beneran, tapi AI bantu di tiap langkah. Hasilnya kode asli yang bisa kamu modifikasi sendiri.
        - **Manual coding** — semua kamu tulis sendiri. Lambat, tapi paling fleksibel.

        Vibe Coding itu di tengah-tengah. Lebih cepet dari manual, lebih fleksibel dari no-code.

        ### Kenapa lagi rame sekarang

        Tools-nya udah matang. Cursor bisa baca seluruh project kamu. Claude bisa nulis component yang lumayan rumit. Vercel + Supabase bikin deploy gratis dan tinggal klik.

        Yang susah sekarang bukan teknologi. Yang susah itu **taste** — kemampuan kamu buat nilai mana yang bagus, mana yang jelek.

        ### Yang masuk akal

        - Bikin landing page bagus dalam sehari
        - Bikin SaaS sederhana sama auth dan database dalam dua minggu
        - Bikin tools internal buat tim kecil dalam beberapa hari

        ### Yang gak masuk akal

        - Bikin Facebook dalam seminggu
        - "AI yang ngerjain semua, gue tinggal duduk"
        - Bikin app tanpa pernah baca kodenya

        Banyak yang awal-awal ekspektasinya ketinggian. Kalau kamu mikir "saya gak butuh ngerti coding karena ada AI" — itu jebakan. Pasti nyangkut di bug pertama.

        Aturan praktis: kamu tetep harus ngerti, bukan cuma copy-paste.
        """
    ),
    contoh_code_md=dedent(
        """\
        Ini contoh prompt yang biasa saya pake kalau mau bikin landing page baru:

        ```text
        Saya mau bikin landing page buat toko kopi lokal.
        Stack: Next.js 14 App Router + Tailwind + shadcn/ui.

        Section yang dibutuhin:
        1. Hero — judul, tagline, CTA "Pesan sekarang"
        2. Menu produk (4 kopi, masing-masing ada foto, nama, harga)
        3. Tentang Kami (cerita singkat 2-3 paragraf)
        4. Footer — alamat, jam buka, social media

        Style: minimal, dark mode, accent biru #4EBAEC.
        Responsive di HP dan desktop.

        Bikin struktur file dulu ya, jangan langsung kasih semua kode.
        ```

        Yang saya kasih ke AI: konteks, list section, style, behavior. AI yang bagus bakal nanya balik kalau ada yang kurang jelas. Itu sinyal bagus.
        """
    ),
    practice=(
        "Tulis di catatan kamu: satu app yang pengen kamu bikin dalam 3 bulan "
        "ke depan. Satu paragraf aja. Sebutin: target user-nya siapa, masalah "
        "apa yang dipecahin, gimana solusinya. Ini bakal jadi target sambil "
        "kamu jalan di Vibe Coding."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Prompt: "Bikinin saya app."
            """
        ),
        "hint": (
            "Prompt yang singkat banget kayak gini hampir pasti gagal. AI gak "
            "tau kamu mau apa."
        ),
        "answer_explanation": dedent(
            """\
            Prompt kayak gitu pasti dapet hasil generic. AI gak bisa nebak isi kepala kamu.

            Yang lebih baik: sebutin stack-nya, fitur utamanya apa, style-nya kayak gimana, dan minta dia mulai dari struktur file dulu (bukan langsung kode panjang).
            """
        ),
        "fixed_code": dedent(
            """\
            Prompt yang lebih bagus:

            "Bikin todo app sederhana.
            Stack: Next.js 14 + Tailwind.
            Fitur: tambah, hapus, tandai selesai. Data di localStorage.
            Style: minimal, dark mode, font Inter.
            Mulai dari struktur file dulu, terus iterate per komponen."
            """
        ),
    },
    quiz=[
        q(
            "Vibe Coding itu sebenernya apa?",
            [
                "Bikin app tanpa nulis kode sama sekali",
                "Ngoding sambil dibantu AI, tapi kamu tetep yang nyetir keputusan",
                "Bikin app pake tool visual kayak Webflow",
                "Cuma pake ChatGPT buat bikin website",
            ],
            "B",
            "Vibe Coding itu di tengah-tengah no-code dan manual coding. AI bantu, tapi arah kamu yang nentuin.",
        ),
        q(
            "Bedanya Vibe Coding sama No-Code (Webflow, Bubble) apa?",
            [
                "Vibe Coding lebih lambat",
                "Vibe Coding ngehasilin kode beneran yang bisa kamu modif sendiri",
                "Vibe Coding gak butuh internet",
                "Sama aja",
            ],
            "B",
            "No-Code nyembunyiin kode dari kamu. Vibe Coding tetep ngasih kode asli yang bisa kamu baca, edit, dan deploy.",
        ),
        q(
            "Yang BUKAN ekspektasi realistis dari Vibe Coding?",
            [
                "Bikin landing page dalam sehari",
                "Bikin SaaS sederhana dalam dua minggu",
                "Bikin Facebook lengkap dalam seminggu tanpa baca kode sama sekali",
                "Bikin tools internal dalam beberapa hari",
            ],
            "C",
            "Vibe Coding ngebantu kamu lebih cepet, tapi tetep ada batasnya. App segede Facebook butuh tim, infrastruktur, testing — gak bisa dipotong drastis.",
        ),
        q(
            "Kenapa 'taste' (kemampuan nilai bagus/jelek) penting di era Vibe Coding?",
            [
                "Gak penting, AI selalu bener",
                "Karena AI bisa ngehasilin banyak opsi, dan kamu yang harus milih mana yang bagus",
                "Biar keren di depan recruiter",
                "Karena tool-nya butuh sertifikat",
            ],
            "B",
            "AI bisa kasih puluhan versi, tapi yang nentuin mana yang oke buat user kamu — itu kamu.",
        ),
        q(
            "Mana prompt yang lebih bagus buat AI?",
            [
                "\"Bikinin website saya.\"",
                "\"Bikin landing page Next.js + Tailwind buat toko kopi, dark mode, ada section hero/menu/tentang, mulai dari struktur file dulu.\"",
                "\"Tolong bantuin.\"",
                "\"Saya butuh kode.\"",
            ],
            "B",
            "Prompt yang bagus = konteks + spesifik + format output. Tanpa itu AI cuma bisa nebak.",
        ),
    ],
    common_mistakes=[
        "Ngira Vibe Coding = ChatGPT all the way. Padahal kamu tetep harus ngerti yang dibikin.",
        "Skip belajar dasar coding karena ngira AI bisa handle. Pas ada bug pertama, mentok total.",
        "Prompt yang kependekan. AI gak bisa baca pikiran, kasih konteks yang cukup.",
    ],
    checkpoint=[
        "Bisa jelasin Vibe Coding ke temen yang awam coding",
        "Tau bedanya no-code, low-code, AI coding, manual",
        "Udah punya target satu app yang pengen dibikin",
    ],
    xp_reward=50,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Tools Ecosystem
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TOOLS = make_lesson(
    title="Kenalan sama Tools yang Dipakai",
    slug="tools-ecosystem",
    order_index=2,
    read_time="9 menit",
    summary="Cursor, Claude, ChatGPT, V0, Bolt — kapan pake yang mana.",
    tools=[
        "Akun ChatGPT atau Claude (yang gratis dulu)",
        "Akun GitHub",
        "Akun Vercel",
    ],
    outcomes=[
        "Tau tools utama yang dipake di Vibe Coding",
        "Tau kapan pake editor AI vs chat assistant vs UI generator",
        "Punya kombinasi tools yang cocok buat pemula",
    ],
    tldr=(
        "Cursor buat ngoding sehari-hari. Claude/ChatGPT buat diskusi panjang. "
        "V0/Bolt buat generate UI cepet. GitHub + Vercel + Supabase buat simpan, "
        "deploy, dan database. Gak usah pake semua dari awal."
    ),
    pembuka=dedent(
        """\
        Banyak yang bingung mulai dari mana karena tools-nya ada banyak banget. Tiap minggu ada tool baru di Twitter.

        Kabar baiknya: kamu gak perlu pake semua. Mulai dari dua atau tiga, terus tambahin pelan-pelan kalau memang butuh.

        Lesson ini bukan promo tools. Ini peta — biar kamu paham tiap tool itu fungsinya buat apa.
        """
    ),
    penjelasan=dedent(
        """\
        ### Editor sama AI di dalemnya

        - **Cursor** — fork dari VS Code yang udah ada AI built-in. Bisa baca semua file di project kamu. Shortcut yang sering dipake: `⌘K` buat edit kode di tempat, `⌘L` buat ngobrol sama AI.
        - **GitHub Copilot** — plugin di VS Code biasa. Lebih ringan tapi gak sepowerful Cursor buat diskusi multi-file.

        Pilih satu aja. Kalau bingung, mulai dari **Cursor**. Hampir semua indie builder di komunitas pake itu sekarang.

        ### Chat assistant

        - **Claude** (dari Anthropic) — bagus banget buat reasoning panjang dan refactor besar. Output kodenya rapi.
        - **ChatGPT** (dari OpenAI) — versatile, ekosistem plugin banyak. GPT-5 cepet dan akurat buat coding.

        Banyak builder yang pake dua-duanya — Claude buat planning sama refactor, ChatGPT buat eksekusi cepet. Tapi gak wajib. Mulai dari satu dulu.

        ### Generator UI

        - **V0** (dari Vercel) — generate component React + Tailwind dari prompt. Hasilnya tinggal di-paste ke Cursor.
        - **Bolt.new** (dari StackBlitz) — generate full app yang langsung jalan di browser. Cocok buat bikin prototype.
        - **Lovable** — mirip Bolt, fokusnya full-stack.

        Pake ini buat awalan. Lanjutannya biasanya di Cursor.

        ### Tempat simpan dan deploy

        - **GitHub** — buat simpan kode. Wajib.
        - **Vercel** — deploy frontend Next.js dalam 30 detik. Wajib juga.
        - **Supabase** — PostgreSQL hosted gratis + auth + storage. Pintu masuk yang ramah ke backend.

        Semuanya gratis buat pemula. Itu udah cukup buat launch app pertamamu.

        ### Kombinasi pemula

        Cursor + Claude + GitHub + Vercel + Supabase. Lima ini udah cukup buat bikin app produksi sederhana. Jangan tambah lagi sampai kamu beneran butuh.
        """
    ),
    contoh_code_md=dedent(
        """\
        Cara kerja yang umum:

        ```text
        1. Buka V0 → kasih prompt → dapet component React + Tailwind
        2. Salin ke project Next.js di Cursor
        3. Pake ⌘K di Cursor buat modifikasi sesuai kebutuhan
        4. Push ke GitHub
        5. Vercel auto-deploy
        6. Pasang Supabase kalau butuh data yang persisten
        ```

        Yang paling enak dari kombinasi ini: feedback loop-nya cepet. Dari ide ke deploy bisa di bawah satu jam.
        """
    ),
    practice=(
        "Bikin akun di tiga tools wajib: GitHub, Vercel, Cursor. Login, "
        "verifikasi email kalau diminta. Belum perlu install apapun — yang "
        "penting akun-akun udah siap. Catet email-nya biar gak lupa."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            "Saya install semua: Cursor, ChatGPT, Claude, V0, Bolt, Lovable,
            Replit, Supabase, Firebase, Vercel, Netlify, Railway, sama 10
            plugin VS Code. Sekarang malah bingung mulai dari mana."
            """
        ),
        "hint": "Tools yang banyak bukan bikin kamu lebih jago. Sering malah sebaliknya.",
        "answer_explanation": dedent(
            """\
            Salahnya: install semua tools sekaligus tanpa tau mana yang dipake buat apa. Akhirnya energi habis di setup, bukan di bikin sesuatu.

            Yang bener: pilih kombinasi minimal (Cursor + Claude + GitHub + Vercel + Supabase), kuasai itu dulu, baru tambahin kalau ada kebutuhan beneran.
            """
        ),
        "fixed_code": dedent(
            """\
            Stack pemula:
            - Cursor (editor + AI)
            - Claude atau ChatGPT (chat assistant)
            - GitHub (simpan kode)
            - Vercel (deploy frontend)
            - Supabase (database + auth)

            Itu cukup. Tambah tools cuma kalau kamu udah ngerasa kombinasi
            ini gak cukup buat kebutuhan kamu.
            """
        ),
    },
    quiz=[
        q(
            "Cursor itu fungsinya buat apa?",
            [
                "Browser khusus developer",
                "Code editor sama AI built-in yang bisa baca seluruh project",
                "Hosting database",
                "Tempat deploy app",
            ],
            "B",
            "Cursor itu fork dari VS Code yang punya AI bawaan. Beda sama chat assistant biasa karena dia bisa baca konteks project secara luas.",
        ),
        q(
            "Vercel paling sering dipake buat apa?",
            [
                "Bikin database",
                "Generate component UI",
                "Deploy frontend (terutama Next.js) dalam beberapa detik",
                "Editing video",
            ],
            "C",
            "Vercel itu hosting yang dibikin sama tim Next.js sendiri. Push ke GitHub, langsung auto-deploy.",
        ),
        q(
            "V0 fungsinya apa?",
            [
                "Code editor",
                "Generate component React + Tailwind dari prompt",
                "Database",
                "Email hosting",
            ],
            "B",
            "V0 (dari Vercel) itu UI generator. Output-nya kode React + Tailwind yang siap dipake di project.",
        ),
        q(
            "Mana kombinasi minimal yang cocok buat pemula Vibe Coding?",
            [
                "Cursor + Claude/ChatGPT + GitHub + Vercel + Supabase",
                "10 tools sekaligus biar lengkap",
                "Cuma ChatGPT, sisanya gak perlu",
                "Wajib pake Replit sama Railway",
            ],
            "A",
            "Lima tools ini cukup buat launch app produksi sederhana. Tambah tools lain kalau memang ada kebutuhan beneran.",
        ),
        q(
            "Kenapa pemula sebaiknya GAK install semua tools sekaligus?",
            [
                "Karena ribet bayar semuanya",
                "Karena energi bakal habis di setup, bukan di bikin sesuatu. Mending kuasain stack minimal dulu.",
                "Karena dilarang aturan tertentu",
                "Gak ada alasan",
            ],
            "B",
            "Tiap tool butuh waktu adaptasi. Setup overhead bisa bunuh semangat sebelum kamu sempet ngebangun apa-apa.",
        ),
    ],
    common_mistakes=[
        "Install semua tools sebelum bikin apapun. Hasilnya: setup overhead gede, hasil nol.",
        "Bingung mana buat apa, akhirnya nanya pertanyaan yang sama ke beberapa AI.",
        "Skip belajar editor. Cursor punya keyboard shortcut yang ngeboost kecepatan kamu 2x.",
    ],
    checkpoint=[
        "Punya akun GitHub, Vercel, sama Cursor",
        "Tau fungsi tiap tools dalam stack",
        "Udah pilih satu chat assistant utama (Claude atau ChatGPT)",
    ],
    xp_reward=60,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Cara Berpikir dalam Prompt
# ─────────────────────────────────────────────────────────────────────────────

LESSON_PROMPT = make_lesson(
    title="Cara Bikin Prompt yang Hasilnya Bagus",
    slug="cara-berpikir-dalam-prompt",
    order_index=3,
    read_time="10 menit",
    summary="Konteks, spesifik, iteratif — anatomi prompt yang ngehasilin kode bagus.",
    tools=["Akun ChatGPT atau Claude", "Notes app"],
    outcomes=[
        "Tau anatomi prompt yang efektif",
        "Bisa kasih konteks yang cukup ke AI",
        "Bisa iterasi prompt buat perbaikin output yang kurang oke",
    ],
    tldr=(
        "Prompt yang bagus selalu ada tiga hal: konteks (stack, env), spesifik "
        "(apa yang diminta), dan format output (struktur dulu vs code "
        "langsung). Kalau hasil jelek, suruh AI revisi sendiri — jangan mulai "
        "dari nol terus."
    ),
    pembuka=dedent(
        """\
        AI itu bukan dukun. Dia gak bisa baca pikiran kamu.

        Kalau kamu kasih prompt yang vague, hasilnya juga vague. Kalau kamu kasih prompt yang spesifik dan ada konteksnya, hasilnya jauh lebih akurat.

        Prompt itu skill yang bisa diasah. Lesson ini cuma awalnya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga bahan prompt yang bagus

        - **Konteks** — tools, stack, file yang relevan, tujuan akhir.
        - **Spesifik** — kamu mau apa, bukan "bantu dong".
        - **Format output** — mau struktur file dulu? Code langsung? Penjelasan step-by-step?

        Kadang ditambahin: contoh input/output yang kamu harapin.

        ### Prompt yang JELEK

        - "Bikin website."
        - "Tolong dibetulkan."
        - "Code-nya error, fix dong."

        Tiga ini gak ada konteksnya. AI bakal ngarang, gak akurat.

        ### Prompt yang BAGUS

        - "Bikin landing page Next.js 14 + Tailwind buat toko kopi lokal. Section: hero, menu (4 produk dummy), tentang kami, footer. Dark mode, accent #4EBAEC. Mulai dari struktur file dulu."
        - "Saya dapet error 'Cannot read property X of undefined' di file Y baris Z pas klik tombol login. Kode lengkap file-nya: [paste]. Tolong analisis kemungkinan penyebabnya dan kasih saran perbaikannya."

        ### Iterasi itu wajar

        Prompt pertama jarang langsung perfect. Kalau output AI kurang oke, **balik diskusi**, jangan mulai chat baru dari nol.

        Cara minta revisi yang bener:

        - "Kode di atas oke, tapi tolong ganti styling-nya jadi minimal (kurangin shadow, tipisin border). Struktur tetep."
        - "Lupa sebut, semua harus responsive di HP. Update kode di atas."
        - "Hapus library X, ganti pake native Y."

        ### Kapan re-prompt vs mulai chat baru

        Kalau AI mulai keluar topik atau ngotot di solusi yang gak kamu mau setelah 2-3 putaran — buka chat baru dengan prompt yang udah dirapihin.

        ### Kasih AI peran kalau perlu

        "Anggep kamu reviewer kode senior. Cek file ini dan kasih kritik spesifik tentang readability, performance, dan accessibility."

        Kasih peran itu bantu AI fokus ke sudut pandang yang kamu mau.
        """
    ),
    contoh_code_md=dedent(
        """\
        Format prompt template yang bisa kamu pake terus-terusan:

        ```text
        Konteks:
        - Project: [nama / deskripsi singkat]
        - Stack: [Next.js 14, Tailwind, dll.]
        - File yang relevan: [paste atau ringkasan]

        Yang saya butuh:
        - [tugas spesifik, contoh: bikin component Card buat product listing]

        Format output:
        - [Mulai dari struktur dulu / langsung code / explain dulu lalu code]

        Catatan tambahan:
        - [responsive, accessible, dark mode, dll.]
        ```

        Template ini ngehemat waktu di tiap sesi. Salin terus isi sesuai kebutuhan.
        """
    ),
    practice=(
        "Tulis prompt buat bikin component 'NavBar' di Next.js + Tailwind. "
        "Pake template di atas: konteks, kebutuhan, format output, catatan. "
        "Kirim ke ChatGPT/Claude. Terus minta revisi: 'Tambahin dark mode "
        "toggle.'"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "Bikin component tombol."
            AI: [output generic <button>Click me</button>]
            User: "Bukan kayak gitu."
            AI: [output generic kedua, juga gak match]
            User: "Salah lagi!"
            ... loop terus
            """
        ),
        "hint": (
            "Feedback negatif tanpa arah baru bikin AI cuma nebak-nebak doang."
        ),
        "answer_explanation": dedent(
            """\
            Salahnya: user kasih feedback "salah" tanpa jelasin apa yang salah dan apa yang diharapin.

            Yang bener: feedback harus konkret. "Tombolnya terlalu generic. Saya butuh tombol primary dengan icon di kiri, ukuran besar, buat CTA hero. Stack Next.js + Tailwind."
            """
        ),
        "fixed_code": dedent(
            """\
            User: "Bikin component tombol primary dengan icon di kiri,
            padding besar, buat CTA hero. Stack Next.js + Tailwind.
            Background #4EBAEC, hover sedikit lebih gelap. Pake TypeScript."

            AI: [output yang lebih akurat dengan props icon, size, dan style]

            User: "Bagus. Sekarang tambahin variant 'secondary' dengan border
            putih dan background transparan."

            AI: [tambah variant dengan props yang konsisten]
            """
        ),
    },
    quiz=[
        q(
            "Apa tiga bahan utama prompt yang bagus?",
            [
                "Cuma emoji",
                "Konteks, spesifik, dan format output",
                "Sebut nama AI-nya berulang-ulang",
                "Pake bahasa Inggris doang",
            ],
            "B",
            "Konteks (stack/file), spesifik (apa yang diminta), format output (gimana cara penyajiannya). Itu tiga pilarnya.",
        ),
        q(
            "Kalau output AI kurang sesuai, mendingan ngapain?",
            [
                "Mulai chat baru tanpa konteks",
                "Tulis 'salah' aja terus tunggu AI nebak",
                "Iterasi: jelasin SPESIFIK apa yang kurang dan apa yang diharapin",
                "Tinggalin AI, tulis manual",
            ],
            "C",
            "AI butuh feedback konkret. \"Tombolnya terlalu generic, saya butuh primary dengan icon\" jauh lebih efektif daripada \"salah\".",
        ),
        q(
            "Kapan sebaiknya mulai chat baru, bukan iterasi?",
            [
                "Tiap kali",
                "Kalau AI udah keluar topik atau ngotot di solusi yang gak kamu mau setelah 2-3 putaran",
                "Pas capek ngetik",
                "Tiap pagi",
            ],
            "B",
            "Chat lama kadang udah kena kontaminasi asumsi yang salah. Mulai baru dengan prompt yang udah dirapihin biasanya lebih efisien.",
        ),
        q(
            "Mana prompt yang LEBIH BAIK?",
            [
                "\"Tolong fix bug.\"",
                "\"Saya error 'Cannot read property X of undefined' di file Y baris Z pas klik login. Kode file: [paste]. Stack: Next.js + Prisma. Tolong analisis penyebab dan kasih saran perbaikan.\"",
                "\"Code error, gimana?\"",
                "\"Apa salahnya?\"",
            ],
            "B",
            "Prompt yang bagus kasih: pesan error, lokasinya, konteks aksi user, kode terkait, stack, dan format yang kamu mau.",
        ),
        q(
            "Kasih peran ke AI di prompt (contoh: 'Anggep kamu reviewer senior') itu fungsinya apa?",
            [
                "Gak ada fungsinya, basa-basi doang",
                "Bantu AI fokus ke sudut pandang yang kamu mau",
                "Ngubah AI jadi robot",
                "Dilarang aturan",
            ],
            "B",
            "Kasih peran bantu AI nyesuaiin tone dan kedalaman analisisnya. \"Reviewer senior\" bakal lebih kritis daripada AI tanpa peran.",
        ),
    ],
    common_mistakes=[
        "Prompt 'tolong fix'. AI gak tau apa yang harus diperbaikin.",
        "Mulai dari nol tiap kali AI kurang akurat. Mendingan iterasi dengan feedback spesifik.",
        "Gak nyebutin stack. AI milih library default yang mungkin gak cocok sama project kamu.",
    ],
    checkpoint=[
        "Punya template prompt sendiri",
        "Bisa kasih feedback spesifik buat minta revisi",
        "Tau kapan iterasi vs kapan mulai chat baru",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_MAPPING = make_lesson(
    title="Mini Project — Bikin Workflow Pribadi Kamu",
    slug="mini-project-mapping-workflow",
    order_index=4,
    read_time="60 menit",
    summary="Susun workflow Vibe Coding pribadi sebelum mulai bangun app pertama.",
    tools=["Notion / Notes app", "Akun GitHub, Vercel, Cursor"],
    outcomes=[
        "Punya peta workflow pribadi yang jelas",
        "Tau posisi tiap tools di alur kerja kamu",
        "Siap mental buat Level 1: bikin app pertama yang live",
    ],
    tldr=(
        "Bikin dokumen pribadi yang ngerangkum: stack pilihan kamu, alur "
        "kerja dari ide ke deploy, contoh prompt yang bagus, dan goal jangka "
        "pendek. Ini bakal jadi rujukan kamu di level berikutnya."
    ),
    pembuka=dedent(
        """\
        Sebelum mulai ngebangun, mending peta-nya udah jelas dulu.

        Project ini bukan ngoding. Ini bikin dokumen workflow yang bakal kamu pake berulang di level-level berikutnya.

        Tujuannya: kamu gak buang waktu mikir "tools mana ya?" tiap kali mau mulai sesuatu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Outline dokumennya

        Bikin satu file di Notion atau notes app dengan struktur ini:

        - **Stack pilihan saya** — tulis lima tools utama yang bakal kamu pake. Boleh sama dengan rekomendasi (Cursor + Claude/ChatGPT + GitHub + Vercel + Supabase), boleh juga disesuaiin.
        - **Alur kerja saya dari ide ke deploy** — tulis langkah-langkah dalam list bernomor. Contoh: 1) tulis ide, 2) draft prompt awal, 3) generate UI di V0, dst.
        - **Template prompt favorit saya** — salin template dari lesson sebelumnya, sesuaiin sama gaya kamu.
        - **Goal 30 hari ke depan** — satu app yang pengen kamu bikin. Tulis judulnya, user-nya siapa, masalah yang dipecahin, dan satu fitur paling penting.
        - **Daftar tools yang BELUM mau saya install dulu** — penting biar kamu punya batas. "Saya bakal nahan diri install Replit, Railway, atau Lovable sampai memang butuh."

        ### Kenapa ini penting

        Tanpa dokumen ini, kamu bakal terombang-ambing antara tutorial. Tiap tutorial pake stack yang beda. Kalau kamu ikutin semuanya, gak ada yang bakal selesai.

        Dokumen ini jadi alat **fokus**. Pas ragu, balik aja ke dokumen ini.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh isinya kayak gini:

        ```markdown
        # Workflow Vibe Coding Pribadi — [Nama Saya]

        ## Stack pilihan
        - Cursor (editor)
        - Claude (planning + refactor)
        - GitHub (simpan kode)
        - Vercel (deploy frontend)
        - Supabase (database + auth)

        ## Alur kerja standar
        1. Tulis ide singkat di Notes (1 paragraf)
        2. Bikin prompt awal pake template, kirim ke Claude buat planning
        3. Setup project Next.js + Tailwind di Cursor
        4. Generate component UI di V0 saat butuh, salin ke project
        5. Iterate di Cursor (⌘K) buat modifikasi
        6. Push ke GitHub tiap fitur selesai
        7. Vercel auto-deploy. Cek di HP.

        ## Template prompt favorit
        [salin template dari lesson 3]

        ## Goal 30 hari
        - Project: "Habit Tracker buat Pelajar"
        - User: pelajar SMA yang mau bangun rutinitas belajar
        - Masalah: gampang lupa rutinitas baru
        - Fitur paling penting: list rutinitas + check-in harian + streak

        ## Tools yang BELUM mau saya install
        - Replit, Railway, Lovable, Bolt, Firebase
        ```
        """
    ),
    practice=(
        "Bikin dokumen di atas hari ini juga. Gak harus panjang. Yang penting "
        "jujur dan spesifik. Simpen di tempat yang gampang dibuka — Notion "
        "halaman bookmarked atau file Markdown di repo GitHub pribadi."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            "Stack saya: pake apa aja yang lagi trending. Goal: bikin app
            keren. Workflow: improvisasi."
            """
        ),
        "hint": "Komitmen yang vague gak bakal jaga fokus pas tantangan dateng.",
        "answer_explanation": dedent(
            """\
            Salahnya: gak ada keputusan konkret. Pas eksekusi, kamu balik bingung lagi.

            Yang bener: keputusan eksplisit di tiap bagian. Stack disebutin satu-satu. Goal punya user, masalah, fitur. Workflow ada step bernomor.
            """
        ),
        "fixed_code": dedent(
            """\
            Stack: Cursor, Claude, GitHub, Vercel, Supabase.
            Goal 30 hari: Habit Tracker buat pelajar SMA. Fitur paling
            penting: list rutinitas + check-in harian + streak.
            Workflow: 1) draft ide, 2) prompt awal, 3) setup project,
            4) generate UI, 5) iterasi, 6) deploy, 7) test di HP.
            """
        ),
    },
    quiz=[
        q(
            "Tujuan utama Mini Project Level 0 ini apa?",
            [
                "Belajar coding dasar",
                "Bikin dokumen workflow pribadi sebagai alat fokus dan rujukan",
                "Deploy app pertama",
                "Bikin database",
            ],
            "B",
            "Project ini meta — bukan ngoding, tapi nyiapin peta biar level berikutnya lebih efektif.",
        ),
        q(
            "Bagian 'tools yang BELUM mau saya install' fungsinya apa?",
            [
                "Gak penting, basa-basi doang",
                "Jaga fokus dan cegah tools-fatigue",
                "Buat dipamerin",
                "Daftar belanja",
            ],
            "B",
            "Punya batas eksplisit jaga kamu dari godaan install tools baru tiap kali ada hype.",
        ),
        q(
            "'Goal 30 hari' yang bagus itu kayak gimana?",
            [
                "Vague kayak 'bikin app keren'",
                "Spesifik: punya user, masalah, dan satu fitur paling penting",
                "Sangat besar kayak 'clone Instagram'",
                "Tanpa target waktu",
            ],
            "B",
            "Goal yang spesifik bisa dieksekusi. Goal vague atau yang kegedean bikin gampang nyerah.",
        ),
        q(
            "Kenapa 'alur kerja dari ide ke deploy' perlu ditulis?",
            [
                "Biar kelihatan profesional",
                "Biar kamu gak buang waktu mikir step yang sama berulang tiap mulai project",
                "Buat dipajang di GitHub",
                "Gak perlu sebenernya",
            ],
            "B",
            "Alur yang udah disepakati sama diri sendiri ngehemat decision fatigue. Tinggal jalan.",
        ),
        q(
            "Mana yang BUKAN bagian dari dokumen workflow ini?",
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
        "Skip lesson ini karena 'bukan ngoding'. Padahal ini fondasi buat level berikutnya.",
        "Stack ditulis kebanyakan. Tujuannya minimal, bukan komplit.",
        "Goal yang kegedean. 'Clone Instagram dalam 30 hari' itu gak realistis.",
    ],
    checkpoint=[
        "Punya dokumen workflow pribadi yang gampang dibuka",
        "Stack jelas, terbatas di lima tools",
        "Punya satu goal 30 hari yang spesifik",
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
    subtitle="Pahami dulu sebelum nyentuh tools",
    description=(
        "Sebelum buka Cursor atau Claude, pahami dulu Vibe Coding itu apa, "
        "AI coding kerjanya gimana, dan apa yang realistis. Tutup level ini "
        "dengan dokumen workflow pribadi sebagai peta buat level berikutnya."
    ),
    duration="~3 hari",
    difficulty="Pemula",
    accent_color="from-violet-500/30 to-fuchsia-500/10",
    mini_project="Bikin Workflow Pribadi Kamu",
    tags=["AI", "Mindset", "Workflow", "Tools"],
    lessons=[LESSON_APA_ITU, LESSON_TOOLS, LESSON_PROMPT, PROJECT_MAPPING],
)
