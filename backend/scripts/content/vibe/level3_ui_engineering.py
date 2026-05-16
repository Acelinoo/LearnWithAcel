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
    title="Design Taste untuk Builder",
    slug="design-taste-untuk-builder",
    order_index=1,
    read_time="11 menit",
    summary="Spacing, hierarchy, typography — fondasi UI yang dipercaya user.",
    tools=["Browser", "Figma (opsional, untuk inspirasi)", "Notes app"],
    outcomes=[
        "Memahami kenapa UI yang baik membangun trust",
        "Mengenali spacing, hierarchy, typography yang baik",
        "Menganalisis UI website yang kamu suka",
    ],
    tldr=(
        "UI yang baik bukan soal cantik — soal trust. Tiga pondasi: "
        "spacing yang lega, hierarchy yang jelas, typography yang konsisten. "
        "Latih mata dengan analisis UI yang kamu suka."
    ),
    pembuka=dedent(
        """\
        Pernah masuk website dan langsung pergi karena 'kelihatan tidak meyakinkan'? Itu bukan kebetulan.

        Otak manusia menilai trust dalam beberapa detik. UI yang berantakan = sinyal 'mungkin ini scam'. UI yang rapi = sinyal 'ini serius'.

        Sebagai vibe coder, kamu wajib paham ini. Karena AI bisa generate UI, tapi taste — keputusan tentang yang baik vs jelek — itu kerja kamu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Kenapa UI itu trust signal

        User tidak bisa cek apakah backend kamu aman. Mereka tidak bisa lihat apakah database kamu di-encrypt. Yang mereka lihat cuma frontend.

        Jadi mereka pakai **proxy**: kalau frontend rapi, kemungkinan tim-nya juga rapi.

        Studi UX panjang menunjukkan: aspek visual menentukan trust dalam < 1 detik. Kamu harus menang di detik itu.

        ### Tiga pondasi: spacing, hierarchy, typography

        ### 1. Spacing — beri ruang bernapas

        Pemula sering tumpukan elemen mepet. Hasilnya: pesan jadi tidak jelas, mata user lelah.

        Aturan praktis:

        - Section dengan `py-16` minimum, `py-24 sm:py-32` lebih baik.
        - Antar paragraf: `space-y-4` minimum.
        - Card padding: `p-6` minimum.
        - Antar section utama beri pemisah visual atau spacing besar.

        Whitespace itu bukan ruang kosong — itu **ruang yang aktif** mengarahkan mata.

        ### 2. Hierarchy — apa yang penting harus terlihat penting

        Mata user akan membaca dari elemen paling menonjol ke yang paling kecil. Hierarchy yang baik mengarahkan urutan ini.

        Tools untuk bikin hierarchy:

        - **Ukuran:** H1 jelas lebih besar dari H2 dari H3 dari body.
        - **Berat:** `font-semibold` untuk judul, `font-normal` untuk body.
        - **Warna:** primary text untuk konten, muted untuk pendukung.
        - **Spacing:** elemen penting berdiri sendiri dengan ruang luas.

        Tes sederhana: squint mata kamu setengah tertutup, atau buka di mode HP. Apakah kamu masih bisa langsung tahu mana yang utama? Kalau iya, hierarchy sukses.

        ### 3. Typography — pilih sedikit, konsisten

        Aturan: maksimal 2 font family per halaman. Satu untuk heading, satu untuk body. Atau lebih sederhana: satu font untuk semua.

        Pilihan aman dari Google Fonts:

        - **Inter** — netral, paling populer untuk app modern.
        - **Plus Jakarta Sans** — sedikit lebih friendly.
        - **Space Grotesk** — geometris, cocok untuk teknologi.
        - **Poppins** — populer di Indonesia, friendly.

        Untuk weight: pakai 2-3 weight saja. Misal `font-normal` (400), `font-medium` (500), `font-semibold` (600).

        Line height penting: `leading-relaxed` untuk body teks panjang. Default Tailwind sering terlalu rapat.

        ### Bonus: color discipline

        - 1 primary/accent color.
        - 2-3 neutral (untuk background, text, border).
        - 1 semantic untuk error (merah), 1 untuk success (hijau) — kalau memang butuh.

        Lebih sedikit = lebih elegan. Kalau ragu, kurangi warna.

        ### Latihan: analisis UI

        Buka 3 website yang kamu suka. Untuk masing-masing, jawab:

        1. Berapa font family yang dipakai?
        2. Apa accent color-nya?
        3. Bagaimana spacing antar section utama?
        4. Apa elemen pertama yang menangkap mata kamu?
        5. Apa yang akan kamu ubah kalau kamu jadi designer-nya?

        Latihan ini membangun taste secara aktif.
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
              Untuk web developer pemula
            </p>

            {/* H1 — paling besar, paling tebal */}
            <h1 className="mt-4 text-4xl font-semibold tracking-tight sm:text-6xl">
              Belajar bikin app modern.
              <span className="text-gray-400"> Tanpa overwhelm.</span>
            </h1>

            {/* Subhead — supporting, lebih kecil */}
            <p className="mt-6 text-lg leading-relaxed text-gray-400">
              Roadmap terstruktur, mini project nyata, dan komunitas yang
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

        Perhatikan:
        - 4 level hierarchy: eyebrow > H1 > subhead > CTAs.
        - Spacing besar antar elemen (mt-4, mt-6, mt-10).
        - 1 accent color (biru), sisanya grayscale.
        - Typography weight: medium → semibold → normal → medium.
        """
    ),
    practice=(
        "Pilih satu website yang kamu suka. Tulis analisis UI-nya berdasarkan "
        "5 pertanyaan di Penjelasan inti. Simpan di Notes — ini akan jadi "
        "rujukan saat kamu polish UI app sendiri di lesson berikutnya."
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
        "hint": "Tiga masalah: spacing, hierarchy, dan color discipline.",
        "answer_explanation": dedent(
            """\
            1. **Spacing kurang** — `py-4` terlalu sempit untuk hero. Pakai `py-24 sm:py-32`.
            2. **Hierarchy terbalik** — H1 lebih kecil dari paragraf di bawahnya. Tukar weight dan size.
            3. **Color chaos** — tiga tombol dengan warna berbeda. Pilih primary yang menonjol, sisanya secondary/ghost.
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
                  Sedang belajar React, Vue, dan Angular.
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
            "Mengapa UI yang baik penting untuk vibe coder?",
            [
                "Untuk pamer skill",
                "UI adalah trust signal — user menilai kredibilitas dari frontend dalam detik pertama",
                "Untuk SEO saja",
                "Tidak penting",
            ],
            "B",
            "Studi UX menunjukkan trust dibangun visual sebelum konten dibaca. UI rapi = sinyal kompeten.",
        ),
        q(
            "Mana praktik spacing section yang BAIK?",
            ["`py-2`", "`py-24 sm:py-32`", "`py-0`", "Tidak perlu spacing"],
            "B",
            "Section utama butuh ruang lega supaya pesannya jelas dan mata user tidak lelah.",
        ),
        q(
            "Apa cara membangun hierarchy yang efektif?",
            [
                "Ukur semua sama besar",
                "Kombinasi ukuran, weight, warna, dan spacing — yang penting menonjol",
                "Cuma warna",
                "Cuma ukuran",
            ],
            "B",
            "Empat tools (size, weight, color, spacing) bekerja sama. Hierarchy yang baik = mata pembaca bergerak ke urutan yang kamu mau.",
        ),
        q(
            "Berapa font family yang sebaiknya dipakai per halaman?",
            ["Maksimal 2 (atau bahkan 1)", "5 supaya kaya", "10", "Tidak ada batasan"],
            "A",
            "Font discipline. Lebih dari 2 family bikin halaman terasa berantakan dan tidak premium.",
        ),
        q(
            "Apa praktik color discipline yang BAIK?",
            [
                "Banyak warna supaya seru",
                "1 accent + 2-3 neutral. Tambah semantic (red/green) kalau perlu.",
                "Pelangi",
                "Black & white only",
            ],
            "B",
            "Sedikit warna dengan kontras yang tepat = elegan dan fokus. Banyak warna = chaos.",
        ),
    ],
    common_mistakes=[
        "Padding section terlalu sempit. Halaman terasa sumpek.",
        "H1 dan paragraf ukuran sama. Hierarchy hilang.",
        "Tiga warna primary dengan intensitas sama. Mata user tidak tahu mana yang utama.",
    ],
    checkpoint=[
        "Bisa identifikasi 3 hal di UI mana saja: spacing, hierarchy, typography.",
        "Tahu kapan UI 'kurang lega' dan tahu cara perbaikinya.",
        "Punya 1 portfolio analysis website yang kamu suka.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Fixing Ugly AI UI
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FIX_UI = make_lesson(
    title="Fixing Ugly AI UI",
    slug="fixing-ugly-ai-ui",
    order_index=2,
    read_time="12 menit",
    summary="5 masalah umum di output AI dan cara prompt revisi yang efektif.",
    tools=["Cursor", "AI assistant", "DevTools"],
    outcomes=[
        "Mengenali 5 masalah klasik di UI buatan AI",
        "Prompt revisi yang spesifik dengan vocabulary desain",
        "Tahu kapan polish manual vs prompt ulang",
    ],
    tldr=(
        "Output AI sering 'mid' karena 5 alasan: spacing rapat, hierarchy "
        "lemah, terlalu banyak warna, copy generic, dan kurang detail. "
        "Identifikasi masalahnya, prompt revisi yang spesifik."
    ),
    pembuka=dedent(
        """\
        Generate UI dengan AI itu cepat. Hasilnya 'jalan' tapi sering 'kurang oke'.

        Yang membedakan vibe coder pemula dari yang berpengalaman: kemampuan **mengenali apa yang kurang** dan **prompt revisi dengan vocabulary yang tepat**.

        Lesson ini bedah 5 masalah paling sering muncul, plus formula prompt revisi yang efektif.
        """
    ),
    penjelasan=dedent(
        """\
        ### 5 masalah klasik di UI buatan AI

        ### 1. Spacing terlalu rapat

        AI sering kasih `py-8` atau `py-12` untuk hero. Itu kurang.

        **Fix:** "Naikkan padding vertical hero jadi `py-24 sm:py-32`. Tambah `mt-8` antara heading dan subhead. Section di bawahnya beri `mt-16` minimum."

        ### 2. Hierarchy lemah

        H1 dan H2 ukurannya beda tipis. Subhead tidak terlihat seperti subhead.

        **Fix:** "Buat H1 lebih besar: `text-5xl sm:text-7xl`, `font-semibold`, `tracking-tight`. Subhead `text-lg`, `text-gray-400`. Beri `mt-6` antara keduanya supaya jelas terpisah."

        ### 3. Terlalu banyak warna

        Tiga tombol dengan tiga warna berbeda. Card dengan border ungu, hover hijau, badge oranye. Chaos.

        **Fix:** "Pakai satu accent color (sebut warna spesifik). Sisanya grayscale. Tombol primary pakai accent, secondary pakai border tipis dengan hover effect halus."

        ### 4. Copy generic / sok English

        "Build amazing apps." "Stunning user experiences." "Empower your business."

        Itu copy stock — tidak ada user yang merasa tertarget.

        **Fix:** "Ganti copy ke bahasa Indonesia santai-profesional. Spesifik ke target user (sebutkan: pemula, profesional, bisnis kecil, dll). Hindari kata-kata buzz seperti 'amazing', 'stunning'."

        ### 5. Tidak ada detail

        Tombol tanpa hover state. Card tanpa transition. Tidak ada loading skeleton.

        **Fix:** "Tambah hover state di semua tombol dengan transition smooth. Card pakai `transition-all hover:border-blue-400 hover:shadow-lg`. Untuk loading, kasih skeleton dengan `animate-pulse`."

        ### Anatomi prompt revisi yang efektif

        Formula: **lokasi + masalah + arah perbaikan + spesifikasi**.

        Contoh:

        - Buruk: "Hero kurang oke."
        - Cukup: "Spacing hero kurang lega."
        - Bagus: "Hero (di `app/page.tsx`): spacing kurang lega. Naikkan `py-24` minimum. Heading kurang menonjol — pakai `text-6xl font-semibold`. Hapus emoji di tagline, ganti dengan dua kata kuat tanpa English."

        AI yang dapat prompt seperti ini akan kasih hasil yang jauh lebih akurat.

        ### Polish manual vs prompt ulang

        Kapan polish sendiri di Cursor (lebih cepat):

        - Ganti 1-2 angka spacing.
        - Tukar warna spesifik.
        - Ubah satu kata copy.

        Kapan prompt ulang ke AI:

        - Restrukturisasi component.
        - Tambah fitur baru.
        - Refactor logic.

        Aturan jempol: kalau perubahannya lebih dari 5 baris kode, prompt. Kurang dari itu, edit manual lebih cepat.

        ### Vocabulary desain yang berguna

        Belajar istilah ini supaya bisa ngomong dengan AI:

        - **Whitespace** — ruang kosong di antara elemen.
        - **Hierarchy** — urutan visual penting ke tidak penting.
        - **Contrast ratio** — perbedaan kecerahan untuk readability.
        - **Tracking** — jarak antar huruf (CSS: letter-spacing).
        - **Leading** — jarak antar baris (CSS: line-height).
        - **Eyebrow** — teks kecil di atas heading utama.
        - **Subhead** — teks pendukung di bawah heading.
        - **CTA** — Call to Action, tombol/link yang ngajak user untuk bertindak.
        - **Skeleton** — placeholder gray saat data loading.
        - **Empty state** — tampilan saat data kosong.

        Pakai istilah-istilah ini saat prompt — AI fluent dengan kosakata ini.
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

        Sesudah (setelah polish dengan prompt revisi):

        ```jsx
        <section className="py-24 sm:py-32">
          <div className="mx-auto max-w-3xl text-center">
            <p className="text-sm font-medium uppercase tracking-wider text-blue-400">
              Untuk pemula yang serius
            </p>

            <h1 className="mt-4 text-4xl font-semibold tracking-tight sm:text-6xl">
              Belajar coding dari nol.
              <span className="block text-gray-400">Sampai live di internet.</span>
            </h1>

            <p className="mt-6 text-lg leading-relaxed text-gray-400">
              Roadmap terstruktur dan proyek nyata, bukan tutorial yang
              berputar-putar.
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

        Perubahan: spacing dinaikkan, hierarchy diperjelas dengan eyebrow, copy dispesifikkan, color discipline (1 primary biru), hover state ditambahkan.
        """
    ),
    practice=(
        "Generate satu landing page sederhana dengan AI (boleh di V0). Salin "
        "ke Cursor. Identifikasi minimal 3 dari 5 masalah yang ada di lesson "
        "ini. Prompt revisi dengan formula 'lokasi + masalah + arah + "
        "spesifikasi'. Catat hasilnya."
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
        "hint": "Feedback vague membuat AI cuma tebak-tebak. Kasih konteks dan kosakata yang tepat.",
        "answer_explanation": dedent(
            """\
            Kesalahan: feedback subjektif tanpa instruksi konkret.

            "Jelek" tidak memberi arah. AI tidak tahu apa yang harus diubah.

            Yang benar: identifikasi masalah spesifik (5 kategori di lesson ini), tentukan arah perbaikan, kasih spesifikasi (angka, nama warna, istilah desain).
            """
        ),
        "fixed_code": dedent(
            """\
            User: "Ada 3 hal yang perlu diperbaiki di hero (app/page.tsx):

            1. Spacing terlalu sempit. Naikkan py-8 jadi py-24 sm:py-32.
            2. Hierarchy lemah - H1 dan subhead ukurannya beda tipis.
               Buat H1 text-5xl sm:text-7xl font-semibold, subhead text-lg
               text-gray-400 dengan mt-6 di antaranya.
            3. Color chaos - dua tombol pakai warna berbeda. Tombol pertama
               primary (bg-blue-500), tombol kedua secondary (border tipis
               dengan hover effect).

            Pertahankan semua copy dan struktur lain."
            """
        ),
    },
    quiz=[
        q(
            "Mana 5 masalah klasik di output AI yang sebutkan di lesson?",
            [
                "Spacing rapat, hierarchy lemah, terlalu banyak warna, copy generic, kurang detail",
                "Code panjang, error, slow, ugly, expensive",
                "Tidak ada masalah",
                "Cuma masalah backend",
            ],
            "A",
            "Lima ini paling sering muncul. Identifikasi cepat = revisi efektif.",
        ),
        q(
            "Mana formula prompt revisi yang efektif?",
            [
                "Singkat: 'fix it'",
                "Lokasi + masalah + arah perbaikan + spesifikasi",
                "Cuma 'better please'",
                "Tidak butuh formula",
            ],
            "B",
            "Formula ini memberi AI semua yang dibutuhkan untuk hasil akurat: di mana, apa salahnya, mau jadi apa, dan parameter spesifik.",
        ),
        q(
            "Kapan sebaiknya polish manual di Cursor, bukan prompt AI?",
            [
                "Selalu prompt AI",
                "Untuk perubahan kecil (< 5 baris): ganti angka, tukar warna, ubah satu kata",
                "Tidak boleh edit manual",
                "Random",
            ],
            "B",
            "Aturan jempol: < 5 baris = manual lebih cepat. Lebih dari itu, prompt agar konsisten.",
        ),
        q(
            "Apa arti 'eyebrow' dalam vocabulary desain?",
            [
                "Animasi alis",
                "Teks kecil di atas heading utama yang men-set ekspektasi",
                "Border atas",
                "Tidak ada artinya",
            ],
            "B",
            "Eyebrow itu teks pendek (sering uppercase + tracking) yang muncul di atas H1. Memberi konteks 'untuk siapa' atau 'kategori apa'.",
        ),
        q(
            "Mengapa istilah desain yang tepat penting saat prompt AI?",
            [
                "Untuk pamer",
                "AI fluent dengan istilah ini → output lebih akurat",
                "Tidak penting",
                "Cuma untuk professional",
            ],
            "B",
            "Bahasa yang sama = pemahaman lebih cepat. 'Hierarchy' lebih konkret daripada 'lebih jelas'.",
        ),
    ],
    common_mistakes=[
        "Feedback subjektif: 'jelek', 'tidak oke'. Tidak kasih AI arah.",
        "Prompt revisi tanpa spesifikasi angka. Hasilnya kembali generic.",
        "Prompt ulang untuk perubahan kecil yang lebih cepat di-edit manual.",
    ],
    checkpoint=[
        "Bisa identifikasi 5 masalah klasik di UI AI.",
        "Bisa prompt revisi dengan formula 4 bagian.",
        "Tahu kapan polish manual vs prompt ulang.",
        "Hafal minimal 5 istilah desain yang dipakai dalam prompt.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — shadcn/ui Praktis
# ─────────────────────────────────────────────────────────────────────────────

LESSON_SHADCN = make_lesson(
    title="shadcn/ui untuk Vibe Coder",
    slug="shadcn-ui-praktis",
    order_index=3,
    read_time="11 menit",
    summary="Component library yang kamu copy ke project, bukan install package.",
    tools=["Next.js + Tailwind project", "Cursor", "Terminal"],
    outcomes=[
        "Memahami filosofi shadcn/ui (copy, bukan install)",
        "Setup shadcn di project Next.js",
        "Memakai komponen umum: Button, Card, Dialog, Input",
    ],
    tldr=(
        "shadcn/ui = kumpulan component yang kamu copy ke project. Bisa "
        "diedit total. Dibangun di atas Radix UI + Tailwind. Stack default "
        "untuk vibe coder modern."
    ),
    pembuka=dedent(
        """\
        Banyak component library bekerja seperti package: install, import, pakai. Kalau mau ubah, ribet — kadang harus override style atau patch.

        shadcn/ui pakai pendekatan beda: kamu copy kode component-nya ke project sendiri. Setelah itu, terserah kamu — edit, hapus, modifikasi.

        Filosofinya simpel: "your code, your component". Itu bikin shadcn jadi favorit di komunitas vibe coding.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu shadcn/ui

        shadcn/ui bukan npm package biasa. Tidak ada `import { Button } from "shadcn-ui"`.

        Sebagai gantinya, kamu jalankan CLI yang **menyalin kode component** ke project kamu di folder `components/ui/`. Setelah itu, kode itu milik kamu.

        Component-nya dibangun di atas:

        - **Radix UI** — primitives untuk accessibility (keyboard nav, ARIA, focus management).
        - **Tailwind CSS** — styling.
        - **CVA (class-variance-authority)** — manage variant style.

        Hasilnya: component yang accessible, customizable, dan tidak ada bloat.

        ### Setup di Next.js

        Project Next.js + Tailwind harus sudah ada. Lalu:

        ```bash
        npx shadcn@latest init
        ```

        Wizard akan tanya beberapa pertanyaan: gaya (default/new-york), warna utama (slate/zinc/stone/etc), dll. Pilih default-nya kalau ragu.

        Setelah init, kamu bisa tambah component:

        ```bash
        npx shadcn@latest add button
        npx shadcn@latest add card dialog input
        ```

        File terbuat di `components/ui/`. Kamu bisa buka, baca, edit.

        ### Component yang sering dipakai

        - **Button** — tombol dengan banyak variant (default, secondary, outline, ghost, destructive).
        - **Card** — card dengan Header, Title, Description, Content, Footer.
        - **Dialog** — modal accessible.
        - **Input + Label** — form field dengan styling konsisten.
        - **Toast** — notifikasi sementara.
        - **Dropdown Menu** — menu dengan keyboard navigation.
        - **Tabs** — tab switcher.
        - **Avatar** — gambar user dengan fallback initial.

        Daftar lengkap di [ui.shadcn.com](https://ui.shadcn.com).

        ### Pemakaian dasar

        ```jsx
        import { Button } from "@/components/ui/button";

        <Button>Default</Button>
        <Button variant="secondary">Secondary</Button>
        <Button variant="outline">Outline</Button>
        <Button variant="destructive">Hapus</Button>
        <Button size="sm">Kecil</Button>
        <Button size="lg">Besar</Button>
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
            <CardDescription>Landing page untuk toko kopi</CardDescription>
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

        Mau Button kamu beda? Buka `components/ui/button.tsx`, edit. Tidak ada lock-in.

        Mau warna primary beda? Edit CSS variable di `app/globals.css`:

        ```css
        :root {
          --primary: 217 91% 60%; /* HSL */
          --primary-foreground: 0 0% 98%;
        }
        ```

        Semua component yang pakai `--primary` otomatis update. CVA + Tailwind bikin theming jadi sangat clean.

        ### Cara prompt AI dengan shadcn

        AI yang updated kenal shadcn. Prompt:

        > "Pakai shadcn Button dan Card untuk halaman ini. Variant primary di CTA utama, outline di secondary."

        AI akan generate import statement yang benar dan struktur component yang sesuai konvensi shadcn.

        ### Aturan praktis

        - **Jangan langsung pakai semua component.** Tambah saat butuh.
        - **Konsisten variant.** Jangan campur Button outline di section A dan ghost di section B tanpa alasan.
        - **Tweak `globals.css`** untuk warna utama. Jangan inline override per component.
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman login pakai shadcn Card, Input, Label, Button:

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
                    Gunakan email yang terdaftar.
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
                    Lanjutkan dengan Google
                  </Button>
                </CardFooter>
              </Card>
            </div>
          );
        }
        ```

        Perhatikan: kode bersih, accessibility built-in (label terkait input dengan htmlFor), dan styling konsisten lewat CSS variable.
        """
    ),
    practice=(
        "Setup shadcn di project Next.js kamu. Tambah component: Button, "
        "Card, Input, Label, Dialog. Bikin halaman dummy yang pakai semuanya: "
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
        "hint": "Dua kesalahan utama: cara import dan API props.",
        "answer_explanation": dedent(
            """\
            1. shadcn bukan npm package. Tidak ada `from "shadcn-ui"`. Component disalin ke `components/ui/`. Import dari path lokal.
            2. shadcn Button pakai props `variant` dan `size`, bukan `color` dan `big`.
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
            "Apa yang membedakan shadcn/ui dari component library biasa?",
            [
                "Lebih mahal",
                "Component disalin ke project, bukan di-install sebagai npm package",
                "Cuma untuk Vue",
                "Tidak ada bedanya",
            ],
            "B",
            "Filosofi 'copy, don't install'. Setelah disalin, kode 100% milik kamu — bisa diedit tanpa override.",
        ),
        q(
            "Mana cara yang BENAR untuk import shadcn Button?",
            [
                "`import Button from \"shadcn-ui\"`",
                "`import { Button } from \"@/components/ui/button\"`",
                "`require('shadcn')`",
                "`<Button>` langsung tanpa import",
            ],
            "B",
            "Component disalin ke `components/ui/`. Import dari path lokal pakai alias `@/`.",
        ),
        q(
            "shadcn dibangun di atas teknologi apa?",
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
            "Cara mengubah warna primary di shadcn?",
            [
                "Edit setiap component manual",
                "Edit CSS variable di `app/globals.css`",
                "Tidak bisa diubah",
                "Tukar package",
            ],
            "B",
            "CSS variable di globals.css adalah single source of truth. Edit di sana, semua component update.",
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
            "Variant default: default, secondary, outline, ghost, destructive, link. Tidak ada 'rainbow' — kamu bisa tambah sendiri kalau perlu.",
        ),
    ],
    common_mistakes=[
        "Coba `npm install shadcn-ui`. shadcn bukan npm package.",
        "Override style per component. Lebih clean dengan edit CSS variable.",
        "Pakai banyak variant tanpa konsistensi. Pilih yang dipakai per kasus.",
    ],
    checkpoint=[
        "Setup shadcn di project Next.js.",
        "Bisa add dan pakai 5 component umum.",
        "Bisa edit warna primary lewat CSS variable.",
        "Tahu kapan tweak component vs prompt AI untuk component baru.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_SAAS_DASH = make_lesson(
    title="Mini Project — Modern SaaS Dashboard",
    slug="mini-project-saas-dashboard",
    order_index=4,
    read_time="180 menit",
    summary="Build dashboard SaaS yang terlihat siap dipakai client.",
    tools=["Cursor", "Claude / ChatGPT", "Next.js + Tailwind + shadcn", "Vercel"],
    outcomes=[
        "Mengaplikasikan design taste di project nyata",
        "Memakai shadcn untuk component standar",
        "Membangun dashboard yang terlihat professional, bukan AI-generated",
    ],
    tldr=(
        "Bangun dashboard SaaS dengan sidebar, stats card, table, dan chart "
        "(boleh placeholder). Stack: Next.js + Tailwind + shadcn. Fokus: "
        "polish sampai terlihat siap presentasi ke client."
    ),
    pembuka=dedent(
        """\
        Dashboard adalah tipe UI yang sering dipakai SaaS, tools internal, dan admin panel. Setiap vibe coder sebaiknya bisa bikin satu yang layak.

        Yang akan kamu bangun: dashboard dengan sidebar nav, stats overview, table data, dan chart placeholder.

        Tujuan akhir: tampilan yang kamu bisa screenshot dan share ke client tanpa malu.
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

        - **Sidebar** — vertical nav dengan logo + 4-5 link (Dashboard, Users, Sales, Reports, Settings). Active state jelas. Collapsible di mobile (pakai shadcn Sheet kalau mau).
        - **Header** — search input + user avatar dropdown (logout, settings).
        - **Stats Cards** — 4 card dengan label, angka besar, dan delta (misal "+12% vs minggu lalu" warna hijau atau merah).
        - **Chart** — placeholder kotak gradient atau pakai library `recharts` kalau sempat.
        - **Table** — 5-10 row recent activity. Pakai shadcn Table component.

        ### Polish checklist

        Hal-hal kecil yang menentukan dashboard pro vs amatir:

        - **Active nav state.** Link yang aktif punya background + accent color.
        - **Hover state.** Setiap interactive element punya hover. Subtle, tidak berlebihan.
        - **Empty state.** Kalau table kosong, tampilkan ilustrasi minimal + pesan friendly.
        - **Loading skeleton.** Saat data loading, pakai `animate-pulse` skeleton bar.
        - **Responsive.** Sidebar collapsible di < 768px. Table scrollable horizontal di mobile.
        - **Dark mode toggle.** Optional tapi nice — pakai theme dari shadcn.
        - **Micro-typography.** Numbers di stats card pakai `tabular-nums` supaya rapi.
        - **Border radius konsisten.** Pilih satu nilai (`rounded-xl`) dan pakai konsisten.

        ### Workflow yang efektif

        - **Day 1:** Setup project + shadcn. Bikin sidebar + header layout. Belum ada konten.
        - **Day 2:** Stats cards + chart placeholder.
        - **Day 3:** Table + polish (hover, empty state, responsive).
        - **Day 4:** Final polish + deploy.

        Jangan coba selesaikan semua dalam satu hari. Burnout jaminan.

        ### Cara prompt yang efektif

        Pecah jadi satu component per prompt. Contoh:

        - Prompt 1: "Bikin Sidebar component di `components/Sidebar.tsx`. Pakai shadcn. Layout: logo di atas, list nav di tengah, user mini-info di bawah. 5 nav item. Active state pakai bg-accent dan border-l-4."
        - Prompt 2: "Bikin StatsCard component yang terima props: label, value, delta, deltaType ('positive'|'negative'). Pakai shadcn Card. Number besar, delta kecil dengan icon trend."
        - Prompt 3: "Bikin RecentActivity table dengan shadcn Table. Kolom: User, Action, Time, Status (badge). Data dari array hardcode."

        ### Submit

        Live di Vercel. Screenshot mode desktop dan mobile. Share ke 3 orang dengan profesi berbeda — tanyakan: "Apakah ini terlihat seperti tools profesional?". Polish berdasarkan feedback.
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

        Pemakaian:

        ```jsx
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <StatsCard label="Total Revenue" value="Rp 24.7M" delta="+12.5% vs bulan lalu" deltaType="positive" />
          <StatsCard label="Active Users" value="1,284" delta="+3.2% vs minggu lalu" deltaType="positive" />
          <StatsCard label="Bounce Rate" value="42%" delta="-2.1% vs minggu lalu" deltaType="positive" />
          <StatsCard label="Avg. Session" value="3m 24s" delta="-8s vs minggu lalu" deltaType="negative" />
        </div>
        ```
        """
    ),
    practice=(
        "Bangun dashboard sesuai spec di atas. Total waktu sekitar 6-8 jam, "
        "pecah ke 3-4 sesi. Deploy ke Vercel. Sebelum submit, test di mode "
        "HP (DevTools toggle device) — pastikan sidebar collapsible dan "
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
        "hint": "Tampilan menyebutkan 'Stats Card' tapi visual tidak terlihat seperti card. Apa yang kurang?",
        "answer_explanation": dedent(
            """\
            Kesalahan: tidak ada layout, styling, atau pemisahan visual. User tidak bisa scan informasi dengan cepat.

            Yang kurang:

            1. Grid layout supaya 4 card sejajar.
            2. Card visual (border, padding, background sedikit beda dari halaman).
            3. Hierarchy dalam tiap card: label kecil + value besar + delta lebih kecil.
            4. Color untuk delta positif vs negatif.
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
              {/* 3 card lain dengan struktur yang sama */}
            </div>
            """
        ),
    },
    quiz=[
        q(
            "Mana hal yang menentukan dashboard 'terlihat profesional'?",
            [
                "Banyak warna",
                "Active nav state, hover state, empty state, loading skeleton, dan responsive layout",
                "Animasi banyak",
                "Logo besar",
            ],
            "B",
            "Polish ada di detail kecil. Setiap interactive state diperhatikan = dashboard terasa bermakna.",
        ),
        q(
            "Apa fungsi `tabular-nums` di Tailwind untuk dashboard?",
            [
                "Buat angka berputar",
                "Menyamakan lebar tiap angka — bagus untuk stats yang berdampingan",
                "Mengubah warna",
                "Tidak ada fungsi",
            ],
            "B",
            "Default proportional fonts membuat angka 1 lebih sempit dari 8. tabular-nums menyamakan, hasilnya stats card sebelahan rapi.",
        ),
        q(
            "Apa yang HARUS ada di dashboard untuk mobile?",
            [
                "Tampilan sama seperti desktop",
                "Sidebar collapsible (hamburger menu) dan table yang scrollable horizontal",
                "Hapus semua fitur",
                "Cuma logo",
            ],
            "B",
            "Mobile butuh adaptasi. Sidebar full-width tidak masuk akal di HP. Table dengan banyak kolom wajib scrollable.",
        ),
        q(
            "Mana strategi prompt yang BAIK untuk dashboard?",
            [
                "Prompt sekali untuk seluruh dashboard",
                "Pecah jadi satu component per prompt: Sidebar, Header, StatsCard, Table",
                "Prompt acak",
                "Tidak prompt sama sekali",
            ],
            "B",
            "Component-by-component prompt = kontrol lebih baik, lebih mudah revisi, dan kode hasil AI lebih akurat.",
        ),
        q(
            "Setelah dashboard live, apa praktik yang BAIK?",
            [
                "Tinggalkan",
                "Test di mode HP, share ke 3 orang dengan profesi berbeda untuk feedback",
                "Hapus semua",
                "Tunggu klien datang",
            ],
            "B",
            "Feedback dari mata berbeda mengungkap blind spot. Vibe coder baik = senang dapat feedback awal.",
        ),
    ],
    common_mistakes=[
        "Coba selesaikan dashboard dalam satu sesi marathon. Burnout.",
        "Sidebar tidak responsive. Mobile-nya stuck atau full-width.",
        "Stats card tidak punya delta atau visual hierarchy. Terasa flat.",
    ],
    checkpoint=[
        "Dashboard live di Vercel.",
        "Sidebar + header + stats + table + chart placeholder semua ada.",
        "Active nav state, hover state, empty state, loading skeleton sudah dipasang.",
        "Test di mobile mode dan responsive dengan baik.",
        "Sudah dapat feedback dari minimal 3 orang.",
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
    subtitle="Polish AI output sampai layak presentasi ke client",
    description=(
        "Belajar prinsip dasar desain (spacing, hierarchy, typography), cara "
        "perbaiki UI buatan AI, dan setup shadcn/ui sebagai stack default. "
        "Tutup level dengan SaaS dashboard yang terlihat profesional."
    ),
    duration="~2 minggu",
    difficulty="Menengah",
    accent_color="from-rose-400/30 to-violet-500/10",
    mini_project="Modern SaaS Dashboard",
    tags=["Design", "Tailwind", "shadcn", "AI Prompting"],
    lessons=[LESSON_TASTE, LESSON_FIX_UI, LESSON_SHADCN, PROJECT_SAAS_DASH],
)
