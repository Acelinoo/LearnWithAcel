"""
Vibe / Level 3 — Vibe UI Engineering.

Lessons:
  1. design-taste-untuk-builder
  2. fixing-ugly-ai-ui
  3. shadcn-ui-praktis
  4. mini-project-saas-dashboard  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Design Taste untuk Builder
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TASTE = make_lesson(
    title="Design Taste buat Builder",
    slug="design-taste-untuk-builder",
    order_index=1,
    read_time="11 menit",
    summary="Spacing, hierarchy, typography — dasar UI yang bikin user percaya.",
    tools=["Browser", "Figma (opsional, buat inspirasi)", "Notes app"],
    outcomes=[
        "Paham kenapa UI yang bagus bikin user percaya",
        "Bisa kenalin spacing, hierarchy, sama typography yang bagus",
        "Bisa nganalisis UI website yang kamu suka",
    ],
    tldr=(
        "UI yang bagus bukan soal cantik — soal kepercayaan. Ada tiga hal "
        "dasar: spacing yang lega, hierarchy yang jelas, typography yang "
        "konsisten. Latih mata kamu dengan analisa UI yang kamu suka."
    ),
    pembuka=dedent(
        """\
        Pernah buka website terus langsung pergi karena 'kayaknya gak meyakinkan'? Itu bukan kebetulan.

        Otak manusia ngeasses kepercayaan dalam beberapa detik. UI berantakan = sinyal 'mungkin ini scam'. UI rapi = sinyal 'ini serius'.

        Sebagai vibe coder, kamu wajib paham ini. AI bisa generate UI, tapi taste — keputusan mana yang bagus vs jelek — itu kerjaan kamu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Kenapa UI itu sinyal kepercayaan

        User gak bisa cek apakah backend kamu aman. Mereka gak bisa lihat database kamu di-encrypt apa enggak. Yang mereka lihat cuma frontend.

        Jadi mereka pake **patokan**: kalau frontend rapi, kemungkinan tim-nya juga rapi.

        Studi UX panjang nunjukin: aspek visual nentuin kepercayaan dalam < 1 detik. Kamu harus menang di detik itu.

        ### Tiga hal dasar: spacing, hierarchy, typography

        ### 1. Spacing — kasih ruang napas

        Pemula sering numpukin elemen mepet-mepet. Hasilnya: pesannya jadi gak jelas, mata user capek.

        Aturan praktis:

        - Section sama `py-16` minimum, `py-24 sm:py-32` lebih oke.
        - Antar paragraf: `space-y-4` minimum.
        - Card padding: `p-6` minimum.
        - Antar section utama kasih pemisah visual atau spacing gede.

        Whitespace itu bukan ruang kosong yang sia-sia — itu **ruang yang aktif** ngarahin mata user.

        ### 2. Hierarchy — yang penting harus keliatan penting

        Mata user bakal baca dari elemen paling menonjol ke yang paling kecil. Hierarchy yang bagus ngarahin urutan ini.

        Tools buat bikin hierarchy:

        - **Ukuran:** H1 jelas lebih gede dari H2 dari H3 dari body.
        - **Bobot:** `font-semibold` buat judul, `font-normal` buat body.
        - **Warna:** primary text buat konten, muted buat pendukung.
        - **Spacing:** elemen penting berdiri sendiri dengan ruang luas.

        Tes gampang: pejamkan setengah mata kamu, atau buka di mode HP. Apakah kamu masih bisa langsung tau mana yang utama? Kalau iya, hierarchy-nya berhasil.

        ### 3. Typography — pilih sedikit, konsisten

        Aturan: maksimal 2 font family per halaman. Satu buat heading, satu buat body. Atau lebih simpel: satu font buat semua.

        Pilihan aman dari Google Fonts:

        - **Inter** — netral, paling populer buat app modern.
        - **Plus Jakarta Sans** — sedikit lebih ramah.
        - **Space Grotesk** — geometris, cocok buat tema teknologi.
        - **Poppins** — populer di Indonesia, kelihatan ramah.

        Buat weight: pake 2-3 weight aja. Misal `font-normal` (400), `font-medium` (500), `font-semibold` (600).

        Line height penting: `leading-relaxed` buat body yang teksnya panjang. Default Tailwind kadang terlalu rapat.

        ### Bonus: disiplin warna

        - 1 primary/accent color.
        - 2-3 netral (buat background, text, border).
        - 1 buat error (merah), 1 buat success (hijau) — kalau emang butuh.

        Lebih sedikit = lebih elegan. Kalau ragu, kurangin warna.

        ### Latihan: analisis UI

        Buka 3 website yang kamu suka. Buat masing-masing, jawab:

        1. Berapa font family yang dipake?
        2. Apa accent color-nya?
        3. Gimana spacing antar section utama?
        4. Apa elemen pertama yang nangkep mata kamu?
        5. Apa yang bakal kamu ubah kalau kamu jadi designer-nya?

        Latihan kayak gini ngebangun taste secara aktif.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh hero section dengan hierarchy yang jelas:

        ```jsx
        <section className="py-24 sm:py-32">
          <div className="mx-auto max-w-3xl text-center">
            {/* Eyebrow — kecil, muted, set ekspektasi */}
            <p className="text-sm font-medium uppercase tracking-wider text-blue-400">
              Buat web developer pemula
            </p>

            {/* H1 — paling gede, paling tebal */}
            <h1 className="mt-4 text-4xl font-semibold tracking-tight sm:text-6xl">
              Belajar bikin app modern.
              <span className="text-gray-400"> Tanpa overwhelm.</span>
            </h1>

            {/* Subhead — pendukung, lebih kecil */}
            <p className="mt-6 text-lg leading-relaxed text-gray-400">
              Roadmap terstruktur, mini project nyata, sama komunitas yang
              suportif — semua di satu tempat.
            </p>

            {/* CTAs — primary + secondary */}
            <div className="mt-10 flex justify-center gap-4">
              <button className="rounded-lg bg-blue-500 hover:bg-blue-600 px-6 py-3 font-medium text-white">
                Mulai gratis
              </button>
              <button className="rounded-lg border border-gray-700 hover:border-gray-500 px-6 py-3 font-medium">
                Lihat roadmap
              </button>
            </div>
          </div>
        </section>
        ```

        Perhatiin:
        - 4 level hierarchy: eyebrow > H1 > subhead > CTAs.
        - Spacing gede antar elemen (mt-4, mt-6, mt-10).
        - 1 accent color (biru), sisanya grayscale.
        - Typography weight: medium → semibold → normal → medium.
        """
    ),
    practice=(
        "Pilih satu website yang kamu suka. Tulis analisis UI-nya berdasarkan "
        "5 pertanyaan di Penjelasan inti. Simpen di Notes — ini bakal jadi "
        "rujukan pas kamu polish UI app sendiri di lesson berikutnya."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            <section className="py-4">
              <h1 className="text-2xl font-normal">Halo</h1>
              <p className="text-2xl font-bold">Saya developer.</p>
              <p className="text-base">Belajar React.</p>
              <p className="text-base">Belajar Vue.</p>
              <p className="text-base">Belajar Angular.</p>
              <button className="bg-red-500 mt-2">Klik</button>
              <button className="bg-green-500 mt-2">Atau ini</button>
              <button className="bg-purple-500 mt-2">Atau yang ini</button>
            </section>
          """
        ),
        "hint": "Tiga masalah: spacing, hierarchy, sama disiplin warna.",
        "answer_explanation": dedent(
            """\
            1. **Spacing kurang** — `py-4` terlalu sempit buat hero. Pake `py-24 sm:py-32`.
            2. **Hierarchy kebalik** — H1 lebih kecil dari paragraf di bawahnya. Tukar weight sama size-nya.
            3. **Warna chaos** — tiga tombol dengan warna beda. Pilih primary yang paling menonjol, sisanya secondary/ghost.
            """
        ),
        "fixed_code": dedent(
            """\
            <section className="py-24 sm:py-32">
              <div className="mx-auto max-w-3xl text-center">
                <h1 className="text-4xl font-semibold sm:text-6xl">
                  Halo, saya developer.
                </h1>
                <p className="mt-4 text-lg text-gray-400">
                  Lagi belajar React, Vue, sama Angular.
                </p>
                <div className="mt-10 flex justify-center gap-3">
                  <button className="rounded-lg bg-blue-500 px-6 py-3 font-medium text-white">
                    Lihat project
                  </button>
                  <button className="rounded-lg border border-gray-700 px-6 py-3 font-medium">
                    Kontak
                  </button>
                </div>
              </div>
            </section>
            """
        ),
    },
    quiz=[
        q(
            "Kenapa UI yang bagus penting buat vibe coder?",
            [
                "Buat pamer skill",
                "UI itu sinyal kepercayaan — user nilai kredibilitas dari frontend dalam detik pertama",
                "Cuma buat SEO",
                "Gak penting",
            ],
            "B",
            "Studi UX nunjukin kepercayaan dibangun visual sebelum konten dibaca. UI rapi = sinyal kompeten.",
        ),
        q(
            "Mana spacing section yang BAGUS?",
            ["`py-2`", "`py-24 sm:py-32`", "`py-0`", "Gak perlu spacing"],
            "B",
            "Section utama butuh ruang lega biar pesannya jelas dan mata user gak capek.",
        ),
        q(
            "Apa cara bangun hierarchy yang efektif?",
            [
                "Ukur semua sama gede",
                "Kombinasi ukuran, weight, warna, sama spacing — yang penting menonjol",
                "Cuma warna",
                "Cuma ukuran",
            ],
            "B",
            "Empat tools (size, weight, color, spacing) kerja bareng. Hierarchy yang bagus = mata pembaca gerak ke urutan yang kamu mau.",
        ),
        q(
            "Berapa font family yang sebaiknya dipake per halaman?",
            ["Maksimal 2 (atau bahkan 1)", "5 biar kaya", "10", "Bebas aja"],
            "A",
            "Disiplin font. Lebih dari 2 family bikin halaman kerasa berantakan dan gak premium.",
        ),
        q(
            "Mana disiplin warna yang BAGUS?",
            [
                "Banyak warna biar seru",
                "1 accent + 2-3 netral. Tambah merah/hijau kalau perlu.",
                "Pelangi",
                "Hitam putih aja",
            ],
            "B",
            "Sedikit warna dengan kontras yang tepat = elegan dan fokus. Banyak warna = chaos.",
        ),
    ],
    common_mistakes=[
        "Padding section terlalu sempit. Halamannya jadi sumpek.",
        "H1 sama paragraf ukurannya sama. Hierarchy hilang.",
        "Tiga warna primary dengan intensitas sama. Mata user gak tau mana yang utama.",
    ],
    checkpoint=[
        "Bisa identifikasi 3 hal di UI mana aja: spacing, hierarchy, typography.",
        "Tau kapan UI 'kurang lega' dan tau cara benerinya.",
        "Punya 1 analisis website yang kamu suka.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Fixing Ugly AI UI
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FIX_UI = make_lesson(
    title="Benerin UI AI yang Jelek",
    slug="fixing-ugly-ai-ui",
    order_index=2,
    read_time="12 menit",
    summary="5 masalah umum di output AI sama cara prompt revisi yang efektif.",
    tools=["Cursor", "AI assistant", "DevTools"],
    outcomes=[
        "Bisa kenalin 5 masalah klasik di UI buatan AI",
        "Bisa prompt revisi yang spesifik pake kosakata desain",
        "Tau kapan polish manual vs prompt ulang",
    ],
    tldr=(
        "Output AI sering 'ya gitu doang' karena 5 alasan: spacing rapat, "
        "hierarchy lemah, kebanyakan warna, copy generic, sama kurang detail. "
        "Kenalin masalahnya, prompt revisi yang spesifik."
    ),
    pembuka=dedent(
        """\
        Generate UI pake AI itu cepet. Hasilnya 'jalan' tapi sering 'kurang oke'.

        Yang bedain vibe coder pemula sama yang udah lama ngulik: kemampuan **kenalin apa yang kurang** sama **prompt revisi pake kosakata yang tepat**.

        Lesson ini ngebedah 5 masalah yang paling sering muncul, plus formula prompt revisi yang efektif.
        """
    ),
    penjelasan=dedent(
        """\
        ### 5 masalah klasik di UI buatan AI

        ### 1. Spacing terlalu rapat

        AI sering kasih `py-8` atau `py-12` buat hero. Itu kurang.

        **Fix:** "Naikin padding vertical hero jadi `py-24 sm:py-32`. Tambah `mt-8` antara heading sama subhead. Section di bawahnya kasih `mt-16` minimum."

        ### 2. Hierarchy lemah

        H1 sama H2 ukurannya beda tipis. Subhead gak keliatan kayak subhead.

        **Fix:** "Bikin H1 lebih gede: `text-5xl sm:text-7xl`, `font-semibold`, `tracking-tight`. Subhead `text-lg`, `text-gray-400`. Kasih `mt-6` antara keduanya biar jelas terpisah."

        ### 3. Kebanyakan warna

        Tiga tombol dengan tiga warna beda. Card sama border ungu, hover hijau, badge oranye. Chaos.

        **Fix:** "Pake satu accent color (sebut warna spesifik). Sisanya grayscale. Tombol primary pake accent, secondary pake border tipis dengan hover effect halus."

        ### 4. Copy generic / sok English

        "Build amazing apps." "Stunning user experiences." "Empower your business."

        Itu copy stok — gak ada user yang ngerasa ditarget.

        **Fix:** "Ganti copy ke bahasa Indonesia santai-profesional. Spesifik ke target user (sebutin: pemula, profesional, bisnis kecil, dll). Hindari kata buzz kayak 'amazing', 'stunning'."

        ### 5. Gak ada detail

        Tombol tanpa hover state. Card tanpa transition. Gak ada loading skeleton.

        **Fix:** "Tambah hover state di semua tombol dengan transition smooth. Card pake `transition-all hover:border-blue-400 hover:shadow-lg`. Buat loading, kasih skeleton sama `animate-pulse`."

        ### Anatomi prompt revisi yang efektif

        Formula: **lokasi + masalah + arah perbaikan + spesifikasi**.

        Contoh:

        - Jelek: "Hero kurang oke."
        - Cukup: "Spacing hero kurang lega."
        - Bagus: "Hero (di `app/page.tsx`): spacing kurang lega, naikin `py-24` minimum. Heading kurang menonjol — pake `text-6xl font-semibold`. Hapus emoji di tagline, ganti pake dua kata kuat tanpa English."

        AI yang dapet prompt kayak gini bakal ngasih hasil jauh lebih akurat.

        ### Polish manual vs prompt ulang

        Kapan polish sendiri di Cursor (lebih cepet):

        - Ganti 1-2 angka spacing.
        - Tukar warna spesifik.
        - Ubah satu kata copy.

        Kapan prompt ulang ke AI:

        - Restrukturisasi component.
        - Tambah fitur baru.
        - Refactor logika.

        Aturan jempol: kalau perubahannya lebih dari 5 baris kode, prompt. Kurang dari itu, edit manual lebih cepet.

        ### Kosakata desain yang berguna

        Belajar istilah ini biar bisa ngomong sama AI:

        - **Whitespace** — ruang kosong di antara elemen.
        - **Hierarchy** — urutan visual penting ke gak penting.
        - **Contrast ratio** — beda kecerahan biar gampang dibaca.
        - **Tracking** — jarak antar huruf (CSS: letter-spacing).
        - **Leading** — jarak antar baris (CSS: line-height).
        - **Eyebrow** — teks kecil di atas heading utama.
        - **Subhead** — teks pendukung di bawah heading.
        - **CTA** — Call to Action, tombol/link yang ngajak user buat ngelakuin sesuatu.
        - **Skeleton** — placeholder abu-abu pas data lagi loading.
        - **Empty state** — tampilan pas data kosong.

        Pake istilah-istilah ini pas prompt — AI ngerti kosakata kayak gini.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sebelum (output AI generic):

        ```jsx
        <section className="py-8">
          <h1 className="text-2xl font-bold">Welcome to my site</h1>
          <p>Stunning experiences await.</p>
          <button className="bg-blue-500">Get Started</button>
          <button className="bg-purple-500">Learn More</button>
        </section>
        ```

        Sesudah (habis polish dengan prompt revisi):

        ```jsx
        <section className="py-24 sm:py-32">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-sm font-medium uppercase tracking-wider text-blue-400">
              Buat pemula yang serius
            </p>

            <h1 className="mt-4 text-4xl font-semibold tracking-tight sm:text-6xl">
              Belajar coding dari nol.
              <span className="block text-gray-400">Sampe live di internet.</span>
            </h1>

            <p className="mt-6 text-lg leading-relaxed text-gray-400">
              Roadmap terstruktur sama proyek nyata, bukan tutorial yang
              muter-muter.
            </p>

            <div className="mt-10 flex justify-center gap-3">
              <button className="rounded-lg bg-blue-500 px-6 py-3 font-medium text-white transition-colors hover:bg-blue-600">
                Mulai gratis
              </button>
              <button className="rounded-lg border border-gray-700 px-6 py-3 font-medium transition-colors hover:border-gray-500">
                Lihat roadmap
              </button>
            </div>
          </div>
        </section>
        ```

        Yang berubah: spacing dinaikin, hierarchy diperjelas pake eyebrow, copy di-spesifikin, disiplin warna (1 primary biru), hover state ditambahin.
        """
    ),
    practice=(
        "Generate satu landing page sederhana pake AI (boleh di V0). Salin "
        "ke Cursor. Identifikasi minimal 3 dari 5 masalah yang ada di lesson "
        "ini. Prompt revisi pake formula 'lokasi + masalah + arah + "
        "spesifikasi'. Catet hasilnya."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "UI-nya jelek, bikin lebih bagus."
            AI: [generates random new design, masih generic]
            User: "Masih jelek. Bagusin lagi."
            AI: [more random changes]
            ... loop
            """
        ),
        "hint": "Feedback yang vague bikin AI cuma nebak-nebak. Kasih konteks sama kosakata yang tepat.",
        "answer_explanation": dedent(
            """\
            Salahnya: feedback subjektif tanpa instruksi konkret.

            "Jelek" gak ngasih arah. AI gak tau apa yang harus diubah.

            Yang bener: identifikasi masalah spesifik (5 kategori di lesson ini), tentuin arah perbaikan, kasih spesifikasi (angka, nama warna, istilah desain).
            """
        ),
        "fixed_code": dedent(
            """\
            User: "Ada 3 hal yang perlu dibenerin di hero (app/page.tsx):

            1. Spacing terlalu sempit. Naikin py-8 jadi py-24 sm:py-32.
            2. Hierarchy lemah - H1 sama subhead ukurannya beda tipis.
               Bikin H1 text-5xl sm:text-7xl font-semibold, subhead text-lg
               text-gray-400 sama mt-6 di antaranya.
            3. Warna chaos - dua tombol pake warna beda. Tombol pertama
               primary (bg-blue-500), tombol kedua secondary (border tipis
               sama hover effect).

            Pertahanin semua copy dan struktur lain."
            """
        ),
    },
    quiz=[
        q(
            "Mana 5 masalah klasik di output AI yang dibahas di lesson?",
            [
                "Spacing rapat, hierarchy lemah, kebanyakan warna, copy generic, kurang detail",
                "Code panjang, error, slow, ugly, expensive",
                "Gak ada masalah",
                "Cuma masalah backend",
            ],
            "A",
            "Lima ini paling sering muncul. Identifikasi cepet = revisi efektif.",
        ),
        q(
            "Mana formula prompt revisi yang efektif?",
            [
                "Singkat: 'fix it'",
                "Lokasi + masalah + arah perbaikan + spesifikasi",
                "Cuma 'better please'",
                "Gak butuh formula",
            ],
            "B",
            "Formula ini ngasih AI semua yang dibutuhin buat hasil akurat: di mana, apa salahnya, mau jadi apa, sama parameter spesifik.",
        ),
        q(
            "Kapan sebaiknya polish manual di Cursor, bukan prompt AI?",
            [
                "Selalu prompt AI",
                "Buat perubahan kecil (< 5 baris): ganti angka, tukar warna, ubah satu kata",
                "Gak boleh edit manual",
                "Random",
            ],
            "B",
            "Aturan jempol: < 5 baris = manual lebih cepet. Lebih dari itu, prompt biar konsisten.",
        ),
        q(
            "'Eyebrow' di kosakata desain itu apa?",
            [
                "Animasi alis",
                "Teks kecil di atas heading utama yang nyetel ekspektasi",
                "Border atas",
                "Gak ada artinya",
            ],
            "B",
            "Eyebrow itu teks pendek (sering uppercase + tracking) yang muncul di atas H1. Ngasih konteks 'buat siapa' atau 'kategori apa'.",
        ),
        q(
            "Kenapa istilah desain yang tepat penting pas prompt AI?",
            [
                "Buat pamer",
                "AI ngerti istilah ini → output lebih akurat",
                "Gak penting",
                "Cuma buat profesional",
            ],
            "B",
            "Pake bahasa yang sama = pemahaman lebih cepet. 'Hierarchy' lebih konkret daripada 'lebih jelas'.",
        ),
    ],
    common_mistakes=[
        "Feedback subjektif: 'jelek', 'gak oke'. Gak kasih AI arah.",
        "Prompt revisi tanpa spesifikasi angka. Hasilnya balik generic.",
        "Prompt ulang buat perubahan kecil yang lebih cepet di-edit manual.",
    ],
    checkpoint=[
        "Bisa identifikasi 5 masalah klasik di UI AI.",
        "Bisa prompt revisi pake formula 4 bagian.",
        "Tau kapan polish manual vs prompt ulang.",
        "Hafal minimal 5 istilah desain yang dipake dalam prompt.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — shadcn/ui Praktis
# ─────────────────────────────────────────────────────────────────────────────

LESSON_SHADCN = make_lesson(
    title="shadcn/ui buat Vibe Coder",
    slug="shadcn-ui-praktis",
    order_index=3,
    read_time="11 menit",
    summary="Component library yang kamu copy ke project, bukan install package.",
    tools=["Project Next.js + Tailwind", "Cursor", "Terminal"],
    outcomes=[
        "Paham cara kerja shadcn/ui (copy, bukan install)",
        "Bisa setup shadcn di project Next.js",
        "Bisa pake komponen umum: Button, Card, Dialog, Input",
    ],
    tldr=(
        "shadcn/ui = kumpulan component yang kamu copy ke project sendiri. "
        "Bisa diedit total. Dibangun di atas Radix UI + Tailwind. Stack "
        "default buat vibe coder modern."
    ),
    pembuka=dedent(
        """\
        Banyak component library kerjanya kayak package: install, import, pake. Mau ubah, ribet — kadang harus override style atau patch.

        shadcn/ui beda. Kamu copy kode component-nya ke project sendiri. Habis itu, terserah kamu — edit, hapus, modifikasi.

        Filosofinya simpel: "kode kamu, component kamu". Itu yang bikin shadcn jadi favorit di komunitas vibe coding.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu shadcn/ui

        shadcn/ui bukan npm package biasa. Gak ada `import { Button } from "shadcn-ui"`.

        Sebagai gantinya, kamu jalanin CLI yang **nyalin kode component** ke project kamu di folder `components/ui/`. Habis itu, kode itu milik kamu.

        Component-nya dibangun di atas:

        - **Radix UI** — primitives buat accessibility (keyboard nav, ARIA, focus management).
        - **Tailwind CSS** — styling.
        - **CVA (class-variance-authority)** — buat manage variant style.

        Hasilnya: component yang accessible, bisa di-customize, sama gak ada bloat.

        ### Setup di Next.js

        Project Next.js + Tailwind harus udah ada. Terus:

        ```bash
        npx shadcn@latest init
        ```

        Wizard bakal nanyain beberapa hal: gaya (default/new-york), warna utama (slate/zinc/stone/etc), dll. Pilih default-nya kalau ragu.

        Habis init, kamu bisa tambah component:

        ```bash
        npx shadcn@latest add button
        npx shadcn@latest add card dialog input
        ```

        File terbentuk di `components/ui/`. Kamu bisa buka, baca, edit.

        ### Component yang sering dipake

        - **Button** — tombol dengan banyak variant (default, secondary, outline, ghost, destructive).
        - **Card** — card sama Header, Title, Description, Content, Footer.
        - **Dialog** — modal yang accessible.
        - **Input + Label** — form field dengan styling konsisten.
        - **Toast** — notifikasi sementara.
        - **Dropdown Menu** — menu dengan keyboard navigation.
        - **Tabs** — tab switcher.
        - **Avatar** — gambar user dengan fallback inisial.

        Daftar lengkap di [ui.shadcn.com](https://ui.shadcn.com).

        ### Cara pake dasar

        ```jsx
        import { Button } from "@/components/ui/button";

        <Button>Default</Button>
        <Button variant="secondary">Secondary</Button>
        <Button variant="outline">Outline</Button>
        <Button variant="destructive">Hapus</Button>
        <Button size="sm">Kecil</Button>
        <Button size="lg">Gede</Button>
        ```

        ```jsx
        import {
          Card,
          CardHeader,
          CardTitle,
          CardDescription,
          CardContent,
          CardFooter,
        } from "@/components/ui/card";

        <Card>
          <CardHeader>
            <CardTitle>Project Saya</CardTitle>
            <CardDescription>Landing page buat toko kopi</CardDescription>
          </CardHeader>
          <CardContent>
            <p>Konten utama card di sini.</p>
          </CardContent>
          <CardFooter>
            <Button>Lihat Demo</Button>
          </CardFooter>
        </Card>
        ```

        ### Customization — kode milik kamu

        Mau Button kamu beda? Buka `components/ui/button.tsx`, edit. Gak ada lock-in.

        Mau warna primary beda? Edit CSS variable di `app/globals.css`:

        ```css
        :root {
          --primary: 217 91% 60%; /* HSL */
          --primary-foreground: 0 0% 98%;
        }
        ```

        Semua component yang pake `--primary` otomatis update. CVA + Tailwind bikin tema jadi clean banget.

        ### Cara prompt AI pake shadcn

        AI yang updated kenal shadcn. Prompt:

        > "Pake shadcn Button sama Card buat halaman ini. Variant primary di CTA utama, outline di secondary."

        AI bakal generate import statement yang bener sama struktur component yang sesuai gaya shadcn.

        ### Aturan praktis

        - **Jangan langsung pake semua component.** Tambah pas butuh.
        - **Konsisten variant.** Jangan campur Button outline di section A sama ghost di section B tanpa alasan.
        - **Ubah `globals.css`** buat warna utama. Jangan inline override per component.
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman login pake shadcn Card, Input, Label, Button:

        ```jsx
        import {
          Card,
          CardHeader,
          CardTitle,
          CardDescription,
          CardContent,
          CardFooter,
        } from "@/components/ui/card";
        import { Input } from "@/components/ui/input";
        import { Label } from "@/components/ui/label";
        import { Button } from "@/components/ui/button";

        export default function LoginPage() {
          return (
            <div className="min-h-screen flex items-center justify-center p-4">
              <Card className="w-full max-w-md">
                <CardHeader>
                  <CardTitle>Masuk ke akun</CardTitle>
                  <CardDescription>
                    Pake email yang udah terdaftar.
                  </CardDescription>
                </CardHeader>

                <CardContent className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="email">Email</Label>
                    <Input id="email" type="email" placeholder="kamu@email.com" />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="password">Password</Label>
                    <Input id="password" type="password" />
                  </div>
                </CardContent>

                <CardFooter className="flex flex-col gap-3">
                  <Button className="w-full">Masuk</Button>
                  <Button variant="outline" className="w-full">
                    Lanjut pake Google
                  </Button>
                </CardFooter>
              </Card>
            </div>
          );
        }
        ```

        Perhatiin: kode bersih, accessibility udah built-in (label terikat ke input pake htmlFor), sama styling konsisten lewat CSS variable.
        """
    ),
    practice=(
        "Setup shadcn di project Next.js kamu. Tambah component: Button, "
        "Card, Input, Label, Dialog. Bikin halaman dummy yang pake semuanya: "
        "list project (Card), form login (Input + Button), dialog konfirmasi "
        "hapus (Dialog)."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            import Button from "shadcn-ui";

            <Button color="blue" big>
              Klik
            </Button>
            """
        ),
        "hint": "Dua kesalahan utama: cara import sama API props.",
        "answer_explanation": dedent(
            """\
            1. shadcn bukan npm package. Gak ada `from "shadcn-ui"`. Component disalin ke `components/ui/`. Import dari path lokal.
            2. shadcn Button pake props `variant` sama `size`, bukan `color` sama `big`.
            """
        ),
        "fixed_code": dedent(
            """\
            import { Button } from "@/components/ui/button";

            <Button variant="default" size="lg">
              Klik
            </Button>
            """
        ),
    },
    quiz=[
        q(
            "Apa yang ngebedain shadcn/ui dari component library biasa?",
            [
                "Lebih mahal",
                "Component disalin ke project, bukan di-install sebagai npm package",
                "Cuma buat Vue",
                "Gak ada bedanya",
            ],
            "B",
            "Filosofi 'copy, jangan install'. Habis disalin, kode 100% milik kamu — bisa diedit tanpa override.",
        ),
        q(
            "Mana cara yang BENER buat import shadcn Button?",
            [
                "`import Button from \"shadcn-ui\"`",
                "`import { Button } from \"@/components/ui/button\"`",
                "`require('shadcn')`",
                "`<Button>` langsung tanpa import",
            ],
            "B",
            "Component disalin ke `components/ui/`. Import dari path lokal pake alias `@/`.",
        ),
        q(
            "shadcn dibangun pake teknologi apa?",
            [
                "Bootstrap",
                "Material UI",
                "Radix UI primitives + Tailwind CSS + CVA",
                "Vue",
            ],
            "C",
            "Radix kasih accessibility, Tailwind kasih styling, CVA kasih variant management.",
        ),
        q(
            "Cara ngubah warna primary di shadcn?",
            [
                "Edit tiap component manual",
                "Edit CSS variable di `app/globals.css`",
                "Gak bisa diubah",
                "Tukar package",
            ],
            "B",
            "CSS variable di globals.css itu sumber kebenaran tunggal. Edit di sana, semua component update.",
        ),
        q(
            "Variant Button yang TIDAK ada di shadcn default?",
            [
                "default",
                "secondary",
                "outline",
                "rainbow",
            ],
            "D",
            "Variant default: default, secondary, outline, ghost, destructive, link. Gak ada 'rainbow' — kamu bisa tambah sendiri kalau perlu.",
        ),
    ],
    common_mistakes=[
        "Coba `npm install shadcn-ui`. shadcn bukan npm package.",
        "Override style per component. Lebih clean kalau edit CSS variable.",
        "Pake banyak variant tanpa konsistensi. Pilih yang dipake per kasus.",
    ],
    checkpoint=[
        "Setup shadcn di project Next.js.",
        "Bisa add sama pake 5 component umum.",
        "Bisa edit warna primary lewat CSS variable.",
        "Tau kapan tweak component vs prompt AI buat component baru.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_SAAS_DASH = make_lesson(
    title="Mini Project — Dashboard SaaS Modern",
    slug="mini-project-saas-dashboard",
    order_index=4,
    read_time="180 menit",
    summary="Bikin dashboard SaaS yang keliatan siap dipake klien.",
    tools=["Cursor", "Claude / ChatGPT", "Next.js + Tailwind + shadcn", "Vercel"],
    outcomes=[
        "Bisa terapin design taste di project nyata",
        "Bisa pake shadcn buat komponen standar",
        "Bisa bikin dashboard yang keliatan profesional, bukan AI-generated",
    ],
    tldr=(
        "Bangun dashboard SaaS sama sidebar, stats card, table, sama chart "
        "(boleh placeholder). Stack: Next.js + Tailwind + shadcn. Fokus: "
        "polish sampe keliatan siap dipresentasiin ke klien."
    ),
    pembuka=dedent(
        """\
        Dashboard itu tipe UI yang sering dipake SaaS, tools internal, sama admin panel. Tiap vibe coder sebaiknya bisa bikin satu yang layak.

        Yang bakal kamu bangun: dashboard sama sidebar nav, stats overview, table data, sama chart placeholder.

        Tujuan akhirnya: tampilan yang kamu bisa screenshot dan share ke klien tanpa malu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind + shadcn/ui. Tanpa backend dulu, semua data hardcode di array.

        Layout:

        ```text
        ┌────────────────────────────────────────────────────────┐
        │ Sidebar │  Header (search, profile dropdown)           │
        │         ├──────────────────────────────────────────────┤
        │ - Dash  │  Page title                                  │
        │ - Users │                                              │
        │ - Sales │  Stats Cards (4 cards: Revenue, Users, etc.) │
        │ - Set.  │                                              │
        │         │  Chart Section (placeholder boleh)           │
        │         │                                              │
        │         │  Recent Activity (table)                     │
        └─────────┴──────────────────────────────────────────────┘
        ```

        ### Section minimal

        - **Sidebar** — vertical nav sama logo + 4-5 link (Dashboard, Users, Sales, Reports, Settings). Active state jelas. Bisa di-collapse di mobile (pake shadcn Sheet kalau mau).
        - **Header** — search input + user avatar dropdown (logout, settings).
        - **Stats Cards** — 4 card sama label, angka gede, sama delta (misal "+12% dari minggu lalu" warna ijo atau merah).
        - **Chart** — placeholder kotak gradient atau pake library `recharts` kalau sempet.
        - **Table** — 5-10 row recent activity. Pake shadcn Table component.

        ### Polish checklist

        Hal-hal kecil yang nentuin dashboard pro vs amatir:

        - **Active nav state.** Link yang aktif punya background + accent color.
        - **Hover state.** Tiap interactive element punya hover. Halus, gak berlebihan.
        - **Empty state.** Kalau table kosong, tampilin ilustrasi minimal + pesan ramah.
        - **Loading skeleton.** Pas data lagi loading, pake `animate-pulse` skeleton bar.
        - **Responsive.** Sidebar bisa di-collapse di < 768px. Table scrollable horizontal di mobile.
        - **Dark mode toggle.** Opsional tapi enak — pake theme dari shadcn.
        - **Micro-typography.** Angka di stats card pake `tabular-nums` biar rapi.
        - **Border radius konsisten.** Pilih satu nilai (`rounded-xl`) terus pake terus.

        ### Workflow yang efektif

        - **Day 1:** Setup project + shadcn. Bikin sidebar + header layout. Belum ada konten.
        - **Day 2:** Stats cards + chart placeholder.
        - **Day 3:** Table + polish (hover, empty state, responsive).
        - **Day 4:** Polish akhir + deploy.

        Jangan coba selesain semua dalam satu hari. Burnout pasti.

        ### Cara prompt yang efektif

        Pecah jadi satu component per prompt. Contoh:

        - Prompt 1: "Bikin Sidebar component di `components/Sidebar.tsx`. Pake shadcn. Layout: logo di atas, list nav di tengah, info user mini di bawah. 5 nav item. Active state pake bg-accent sama border-l-4."
        - Prompt 2: "Bikin StatsCard component yang terima props: label, value, delta, deltaType ('positive'|'negative'). Pake shadcn Card. Number gede, delta kecil sama icon trend."
        - Prompt 3: "Bikin RecentActivity table sama shadcn Table. Kolom: User, Action, Time, Status (badge). Data dari array hardcode."

        ### Submit

        Live di Vercel. Screenshot mode desktop sama mobile. Share ke 3 orang dengan profesi beda — tanya: "Apakah ini keliatan kayak tools profesional?". Polish berdasarkan feedback.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sketsa StatsCard yang clean:

        ```jsx
        import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
        import { TrendingUp, TrendingDown } from "lucide-react";

        export default function StatsCard({ label, value, delta, deltaType }) {
          const positive = deltaType === "positive";
          const Icon = positive ? TrendingUp : TrendingDown;
          const color = positive ? "text-emerald-500" : "text-red-500";

          return (
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-muted-foreground">
                  {label}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-semibold tabular-nums">{value}</div>
                <p className={`mt-1 text-xs flex items-center gap-1 ${color}`}>
                  <Icon size={12} />
                  {delta}
                </p>
              </CardContent>
            </Card>
          );
        }
        ```

        Cara pakenya:

        ```jsx
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <StatsCard label="Total Revenue" value="Rp 24.7M" delta="+12.5% dari bulan lalu" deltaType="positive" />
          <StatsCard label="Active Users" value="1,284" delta="+3.2% dari minggu lalu" deltaType="positive" />
          <StatsCard label="Bounce Rate" value="42%" delta="-2.1% dari minggu lalu" deltaType="positive" />
          <StatsCard label="Avg. Session" value="3m 24s" delta="-8s dari minggu lalu" deltaType="negative" />
        </div>
        ```
        """
    ),
    practice=(
        "Bangun dashboard sesuai spec di atas. Total waktu sekitar 6-8 jam, "
        "pecah ke 3-4 sesi. Deploy ke Vercel. Sebelum submit, test di mode "
        "HP (DevTools toggle device) — pastiin sidebar bisa di-collapse sama "
        "table scrollable."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            <div>
              <div>Stats Card 1: Revenue: Rp 24.7M (+12%)</div>
              <div>Stats Card 2: Users: 1284 (+3%)</div>
              <div>Stats Card 3: Bounce: 42% (-2%)</div>
              <div>Stats Card 4: Session: 3m 24s (-8s)</div>
            </div>
            """
        ),
        "hint": "Tampilannya nyebut 'Stats Card' tapi visual gak keliatan kayak card. Apa yang kurang?",
        "answer_explanation": dedent(
            """\
            Salahnya: gak ada layout, styling, atau pemisahan visual. User gak bisa scan informasi dengan cepet.

            Yang kurang:

            1. Grid layout biar 4 card sejajar.
            2. Card visual (border, padding, background sedikit beda dari halaman).
            3. Hierarchy dalam tiap card: label kecil + value gede + delta lebih kecil.
            4. Warna buat delta positif vs negatif.
            5. Spacing antar card.
            """
        ),
        "fixed_code": dedent(
            """\
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm text-muted-foreground">
                    Total Revenue
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-semibold">Rp 24.7M</div>
                  <p className="text-xs text-emerald-500 mt-1">+12% dari minggu lalu</p>
                </CardContent>
              </Card>
              {/* 3 card lain dengan struktur sama */}
            </div>
            """
        ),
    },
    quiz=[
        q(
            "Mana hal yang nentuin dashboard 'keliatan profesional'?",
            [
                "Banyak warna",
                "Active nav state, hover state, empty state, loading skeleton, sama responsive layout",
                "Animasi banyak",
                "Logo gede",
            ],
            "B",
            "Polish ada di detail kecil. Tiap interactive state diperhatiin = dashboard kerasa bermakna.",
        ),
        q(
            "Fungsi `tabular-nums` di Tailwind buat dashboard?",
            [
                "Bikin angka muter",
                "Nyamain lebar tiap angka — bagus buat stats yang sebelahan",
                "Ubah warna",
                "Gak ada fungsi",
            ],
            "B",
            "Default proportional fonts bikin angka 1 lebih sempit dari 8. tabular-nums nyamain, hasilnya stats card sebelahan jadi rapi.",
        ),
        q(
            "Apa yang HARUS ada di dashboard buat mobile?",
            [
                "Tampilan sama kayak desktop",
                "Sidebar bisa di-collapse (hamburger menu) sama table yang scrollable horizontal",
                "Hapus semua fitur",
                "Cuma logo",
            ],
            "B",
            "Mobile butuh adaptasi. Sidebar full-width gak masuk akal di HP. Table sama banyak kolom wajib scrollable.",
        ),
        q(
            "Mana strategi prompt yang BAGUS buat dashboard?",
            [
                "Prompt sekali buat seluruh dashboard",
                "Pecah jadi satu component per prompt: Sidebar, Header, StatsCard, Table",
                "Prompt acak",
                "Gak prompt sama sekali",
            ],
            "B",
            "Component-by-component prompt = kontrol lebih bagus, lebih gampang revisi, sama kode hasil AI lebih akurat.",
        ),
        q(
            "Habis dashboard live, apa yang sebaiknya dilakuin?",
            [
                "Tinggalin",
                "Test di mode HP, share ke 3 orang dengan profesi beda buat feedback",
                "Hapus semua",
                "Tunggu klien dateng",
            ],
            "B",
            "Feedback dari mata yang beda ngungkap blind spot. Vibe coder yang oke = seneng dapet feedback awal.",
        ),
    ],
    common_mistakes=[
        "Coba selesain dashboard dalam satu sesi marathon. Burnout.",
        "Sidebar gak responsive. Mobile-nya stuck atau full-width.",
        "Stats card gak punya delta atau hierarchy visual. Kerasa flat.",
    ],
    checkpoint=[
        "Dashboard live di Vercel.",
        "Sidebar + header + stats + table + chart placeholder semua ada.",
        "Active nav state, hover state, empty state, loading skeleton udah dipasang.",
        "Test di mobile mode dan responsive dengan baik.",
        "Udah dapet feedback dari minimal 3 orang.",
    ],
    xp_reward=600,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=3,
    slug="vibe-ui-engineering",
    title="Vibe UI Engineering",
    subtitle="Polish output AI sampe layak dipresentasiin ke klien",
    description=(
        "Belajar prinsip dasar desain (spacing, hierarchy, typography), cara "
        "benerin UI buatan AI, sama setup shadcn/ui sebagai stack default. "
        "Tutup level dengan SaaS dashboard yang keliatan profesional."
    ),
    duration="~2 minggu",
    difficulty="Menengah",
    accent_color="from-rose-400/30 to-violet-500/10",
    mini_project="Modern SaaS Dashboard",
    tags=["Design", "Tailwind", "shadcn", "AI Prompting"],
    lessons=[LESSON_TASTE, LESSON_FIX_UI, LESSON_SHADCN, PROJECT_SAAS_DASH],
)
