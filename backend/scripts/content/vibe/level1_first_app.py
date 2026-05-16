"""
Vibe / Level 1 — First App Experience.

Lessons:
  1. setup-environment
  2. github-basics
  3. deploy-website-pertama
  4. mini-project-landing-page-live  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Setup Environment
# ─────────────────────────────────────────────────────────────────────────────

LESSON_SETUP = make_lesson(
    title="Setup Environment",
    slug="setup-environment",
    order_index=1,
    read_time="10 menit",
    summary="Install Node.js, Cursor, dan persiapan akun GitHub + Vercel.",
    tools=["Browser", "Node.js LTS", "Cursor", "Akun GitHub", "Akun Vercel"],
    outcomes=[
        "Memasang Node.js dan memverifikasi dari terminal",
        "Memasang Cursor dengan akun login",
        "Menyiapkan akun GitHub dan Vercel yang sudah terhubung",
    ],
    tldr=(
        "Install Node.js LTS, Cursor, lalu login ke GitHub dan Vercel. "
        "Verifikasi semuanya jalan dengan satu perintah `node -v` di terminal."
    ),
    pembuka=dedent(
        """\
        Banyak orang gagal di langkah ini bukan karena susah, tapi karena bingung mulai dari mana.

        Lesson ini super straightforward. Cuma install tiga hal dan buat dua akun.

        Setelah selesai, kamu siap deploy website pertamamu di lesson 3.
        """
    ),
    penjelasan=dedent(
        """\
        ### Step 1 — Install Node.js

        Node.js adalah runtime JavaScript yang dipakai untuk menjalankan tools modern.

        Buka [nodejs.org](https://nodejs.org), download versi **LTS** (Long Term Support, yang stabil). Ikuti installer-nya, klik next next sampai selesai.

        Setelah selesai, buka terminal (Command Prompt di Windows, Terminal di macOS/Linux). Ketik `node -v`. Kalau muncul versi seperti `v20.x.x`, instalasi berhasil.

        ### Step 2 — Install Cursor

        Cursor adalah code editor dengan AI built-in. Buka [cursor.com](https://cursor.com), klik Download, install seperti aplikasi biasa.

        Saat pertama buka, login dengan email atau Google. Pilih theme dark (lebih nyaman untuk sesi panjang).

        ### Step 3 — Akun GitHub

        Buka [github.com](https://github.com), Sign Up. Pilih username yang profesional (akan jadi bagian URL portfolio kamu).

        Verifikasi email. Selesai.

        ### Step 4 — Akun Vercel

        Buka [vercel.com](https://vercel.com), klik Sign Up, pilih **Continue with GitHub**. Vercel langsung connect ke akun GitHub kamu.

        Itu trick-nya: dengan login pakai GitHub, deploy nantinya tinggal pilih repo.

        ### Verifikasi semua siap

        Buka terminal, ketik `node -v` dan `npm -v`. Keduanya harus mengembalikan versi.

        Buka Cursor, klik Settings → Account. Harus ada email kamu di sana.

        Buka [vercel.com/dashboard](https://vercel.com/dashboard). Harus muncul akun kamu, bukan halaman login.

        ### Kalau ada masalah

        - `node` tidak dikenal di Windows? Restart terminal atau restart komputer setelah install.
        - Cursor terasa lambat? Tutup Discord/Spotify yang berat agar RAM lega.
        - Vercel tidak muncul GitHub repos? Reauthorize GitHub di Settings → Git.
        """
    ),
    contoh_code_md=dedent(
        """\
        Verifikasi instalasi via terminal:

        ```bash
        # Cek versi Node.js
        node -v
        # output: v20.18.0 (atau angka serupa)

        # Cek versi npm (Node Package Manager — datang bareng Node)
        npm -v
        # output: 10.x.x
        ```

        Kalau dua perintah di atas mengembalikan versi, kamu siap lanjut ke lesson berikutnya.
        """
    ),
    practice=(
        "Selesaikan empat step di atas: install Node.js, install Cursor, "
        "buat akun GitHub, dan buat akun Vercel (login dengan GitHub). "
        "Verifikasi `node -v` di terminal mengembalikan versi."
    ),
    fix_error={
        "language": "bash",
        "broken_code": dedent(
            """\
            $ node -v
            'node' is not recognized as an internal or external command,
            operable program or batch file.
            """
        ),
        "hint": (
            "Error ini muncul karena terminal belum tahu Node.js sudah "
            "terpasang. Solusinya berkaitan dengan environment, bukan kode."
        ),
        "answer_explanation": dedent(
            """\
            Penyebab: PATH environment variable belum ter-update. Solusi:

            1. Tutup terminal yang lama, buka terminal baru.
            2. Kalau masih error, restart komputer.
            3. Kalau masih, ulangi install Node.js dan saat installer pastikan opsi "Add to PATH" tercentang.
            """
        ),
        "fixed_code": dedent(
            """\
            # Setelah restart terminal:
            $ node -v
            v20.18.0
            $ npm -v
            10.8.2
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dimaksud dengan versi LTS pada Node.js?",
            [
                "Versi terbaru yang baru dirilis hari ini",
                "Long Term Support — versi stabil yang dapat update keamanan dalam jangka panjang",
                "Light Typescript Support",
                "Versi yang gratis",
            ],
            "B",
            "LTS adalah Long Term Support. Versi ini lebih stabil dan aman untuk produksi. Selalu pilih ini untuk pemula.",
        ),
        q(
            "Bagaimana cara verifikasi Node.js sudah terpasang dengan benar?",
            [
                "Buka GitHub",
                "Ketik `node -v` di terminal, harus muncul versi",
                "Cek di Cursor",
                "Tidak ada cara verifikasi",
            ],
            "B",
            "`node -v` adalah cara standar verifikasi instalasi.",
        ),
        q(
            "Kenapa login Vercel pakai GitHub direkomendasikan?",
            [
                "Karena gratis (GitHub berbayar)",
                "Karena Vercel bisa langsung baca dan deploy repo GitHub kamu",
                "Tidak ada alasan",
                "Diwajibkan oleh hukum",
            ],
            "B",
            "Vercel auto-deploy dari GitHub. Login pakai GitHub bikin proses ini langsung tersambung.",
        ),
        q(
            "Apa yang harus dilakukan kalau `node -v` mengembalikan 'not recognized'?",
            [
                "Pakai komputer baru",
                "Tutup terminal lama, buka baru. Kalau masih, restart komputer atau install ulang dengan opsi 'Add to PATH'",
                "Ganti Cursor",
                "Tidak bisa diperbaiki",
            ],
            "B",
            "Error ini soal PATH environment yang belum ter-load. Restart terminal atau komputer biasanya cukup.",
        ),
        q(
            "Mana urutan setup yang paling efisien?",
            [
                "Install semua bareng, lalu setup akun",
                "Node.js → Cursor → akun GitHub → akun Vercel (login pakai GitHub) → verifikasi",
                "Akun dulu semuanya, baru install",
                "Tidak penting urutannya",
            ],
            "B",
            "Urutan ini menghindari error dependency. Akun Vercel via GitHub paling akhir karena butuh akun GitHub dulu.",
        ),
    ],
    common_mistakes=[
        "Skip restart terminal setelah install Node.js. Akhirnya bingung kenapa `node -v` tidak jalan.",
        "Pakai username GitHub yang aneh. Itu akan muncul di URL portfolio.",
        "Lupa login Vercel pakai GitHub. Akhirnya proses deploy nanti lebih ribet.",
    ],
    checkpoint=[
        "`node -v` dan `npm -v` mengembalikan versi.",
        "Cursor terbuka dengan akun login.",
        "Akun GitHub aktif dengan username profesional.",
        "Akun Vercel terhubung ke GitHub.",
    ],
    xp_reward=60,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — GitHub Basics
# ─────────────────────────────────────────────────────────────────────────────

LESSON_GIT = make_lesson(
    title="GitHub Basics",
    slug="github-basics",
    order_index=2,
    read_time="12 menit",
    summary="Repo, commit, push — tiga aksi yang akan kamu lakukan setiap hari.",
    tools=["Cursor", "Akun GitHub", "Terminal"],
    outcomes=[
        "Membuat repository baru di GitHub",
        "Memahami konsep commit dan push dengan analogi sederhana",
        "Menjalankan tiga perintah dasar Git dari terminal Cursor",
    ],
    tldr=(
        "GitHub itu Google Drive untuk kode. Commit = simpan checkpoint. "
        "Push = upload ke GitHub. Tiga perintah cukup untuk hari pertama: "
        "git init, git commit, git push."
    ),
    pembuka=dedent(
        """\
        GitHub bukan cuma "tempat simpan kode". Dia menyimpan SEJARAH kode kamu — kapan kamu ubah apa, kenapa, oleh siapa.

        Anggap GitHub itu Google Drive khusus untuk kode, plus mesin waktu. Kamu bisa kembali ke versi minggu lalu kalau hari ini ada yang rusak.

        Tools-nya namanya Git (lokal di komputer). GitHub adalah layanan online yang menerima Git push kamu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga konsep dasar

        - **Repository (repo).** Folder project kamu yang dilacak Git.
        - **Commit.** Snapshot perubahan dengan pesan. Ibarat checkpoint di game.
        - **Push.** Kirim commit lokal ke GitHub.

        ### Alur kerja standar

        1. Buat folder project baru di komputer.
        2. Inisialisasi Git: `git init`.
        3. Buat file, tulis kode.
        4. `git add .` (tandai semua file untuk dimasukkan ke commit berikut).
        5. `git commit -m "pesan"` (bikin checkpoint).
        6. Buat repo di GitHub.
        7. Hubungkan lokal ke GitHub: `git remote add origin <url>`.
        8. `git push -u origin main` (upload ke GitHub).

        Step 1-7 cuma sekali. Sehari-hari, siklus kerja kamu cuma:

        ```bash
        git add .
        git commit -m "pesan singkat"
        git push
        ```

        ### Pesan commit yang baik

        Tulis pesan yang menjelaskan **kenapa**, bukan **apa**.

        - Buruk: "update file"
        - Baik: "fix bug login saat email kosong"

        Kebiasaan baik: prefix dengan kata kerja imperative. `add`, `fix`, `refactor`, `remove`, `docs`.

        ### Membuat repo di GitHub

        Buka [github.com/new](https://github.com/new). Isi:

        - **Repository name.** Nama project (contoh `landing-toko-kopi`).
        - **Public** atau **Private.** Public boleh untuk portfolio.
        - **Add README** centang (biar repo tidak kosong).

        Klik Create. Selesai.

        ### Cursor punya UI Git built-in

        Tidak harus selalu pakai terminal. Cursor punya tab Source Control (icon cabang di sidebar kiri) yang bisa stage, commit, dan push dengan klik.

        Tapi pelajari dulu perintah terminalnya — kamu akan butuh kalau lagi remote work atau masuk ke server.
        """
    ),
    contoh_code_md=dedent(
        """\
        Buat repo lokal pertama dan push ke GitHub:

        ```bash
        # Di folder project
        mkdir landing-toko-kopi
        cd landing-toko-kopi

        # Inisialisasi Git
        git init

        # Buat file dummy
        echo "# Landing Toko Kopi" > README.md

        # Tandai dan commit
        git add .
        git commit -m "init: setup project"

        # Hubungkan ke GitHub (URL dari halaman repo baru kamu)
        git remote add origin https://github.com/USERNAME/landing-toko-kopi.git

        # Push ke GitHub
        git branch -M main
        git push -u origin main
        ```

        Setelah ini, refresh halaman repo di GitHub. README.md akan muncul.
        """
    ),
    practice=(
        "Buat satu repo baru di GitHub dengan nama `vibe-test`. Clone ke "
        "komputer pakai `git clone <url>`. Buat file `hello.txt` berisi nama "
        "kamu, lalu add → commit → push. Refresh halaman GitHub, file "
        "`hello.txt` harus muncul."
    ),
    fix_error={
        "language": "bash",
        "broken_code": dedent(
            """\
            $ git push
            fatal: not a git repository (or any of the parent directories): .git
            """
        ),
        "hint": "Error ini muncul saat kamu berada di folder yang belum diinisialisasi Git.",
        "answer_explanation": dedent(
            """\
            Penyebab: Folder saat ini belum di-`git init`, atau kamu pindah ke folder lain yang bukan repo.

            Solusi:

            1. Cek lokasi folder dengan `pwd` (macOS/Linux) atau `cd` (Windows).
            2. Pastikan kamu di dalam folder project yang sudah di-init.
            3. Kalau belum, jalankan `git init` dulu.
            """
        ),
        "fixed_code": dedent(
            """\
            $ cd landing-toko-kopi
            $ git status
            On branch main
            ...
            $ git push
            Everything up-to-date
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi `git commit`?",
            [
                "Mengirim kode ke GitHub",
                "Membuat checkpoint perubahan dengan pesan",
                "Menghapus file",
                "Membuat repo baru",
            ],
            "B",
            "Commit menyimpan snapshot perubahan beserta pesan deskriptif. Push baru yang mengirim commit ini ke GitHub.",
        ),
        q(
            "Apa yang dilakukan `git push`?",
            [
                "Membuat snapshot lokal",
                "Mengirim commit lokal ke remote (GitHub)",
                "Mendownload kode dari GitHub",
                "Menghapus repo",
            ],
            "B",
            "`git push` mengupload commit dari lokal ke GitHub.",
        ),
        q(
            "Mana pesan commit yang BAIK?",
            [
                "\"update\"",
                "\"fix bug login saat email kosong\"",
                "\"asdfg\"",
                "\"WIP\"",
            ],
            "B",
            "Pesan yang baik menjelaskan KENAPA dan APA yang berubah secara spesifik. Itu membantu kamu (dan orang lain) di masa depan.",
        ),
        q(
            "Kenapa kamu butuh `git init` di awal?",
            [
                "Tidak butuh, opsional",
                "Untuk memberi tahu Git bahwa folder ini akan dilacak sebagai repo",
                "Untuk membuat akun GitHub",
                "Untuk install Node.js",
            ],
            "B",
            "`git init` membuat folder `.git` yang menyimpan history. Tanpa ini, Git tidak tahu folder kamu adalah repo.",
        ),
        q(
            "Apa siklus harian kerja Git setelah setup awal?",
            [
                "init → init → init",
                "add → commit → push",
                "delete → reinstall",
                "tidak ada siklus",
            ],
            "B",
            "Tiga perintah ini siklus utama: tandai perubahan, commit dengan pesan, push ke GitHub.",
        ),
    ],
    common_mistakes=[
        "Lupa `git init` di awal. Akhirnya `git status` error 'not a git repository'.",
        "Pesan commit asal seperti 'update', 'fix', 'asdf'. Sulit dibaca di history.",
        "Push setiap baris kode. Sebaiknya commit per fitur atau perubahan logis.",
    ],
    checkpoint=[
        "Bisa membuat repo dari nol dan push ke GitHub.",
        "Tahu beda commit dan push.",
        "Bisa menulis pesan commit yang deskriptif.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Deploy Website Pertama
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DEPLOY = make_lesson(
    title="Deploy Website Pertama",
    slug="deploy-website-pertama",
    order_index=3,
    read_time="10 menit",
    summary="Generate landing page dengan AI, push ke GitHub, deploy ke Vercel.",
    tools=["Cursor", "V0 atau Bolt (boleh dilewati)", "GitHub", "Vercel"],
    outcomes=[
        "Generate landing page sederhana lewat AI",
        "Push project ke GitHub",
        "Deploy ke Vercel dan dapat URL publik",
    ],
    tldr=(
        "Generate landing page dengan AI atau template. Buka di Cursor, "
        "push ke GitHub, import di Vercel. Selesai. URL publik dalam < 30 menit."
    ),
    pembuka=dedent(
        """\
        Lesson ini momen krusial. Setelah selesai, kamu punya website live di internet.

        Itu bukan sekadar checklist. Itu sinyal mental bahwa "saya bisa".

        Ada banyak orang yang belajar coding bertahun-tahun tapi tidak pernah punya satu URL pun yang bisa dibuka publik. Kamu akan lompati itu hari ini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Step 1 — Generate landing page

        Pilih salah satu pendekatan:

        **Pendekatan A — pakai V0**

        Buka [v0.dev](https://v0.dev), kasih prompt:

        > Bikin landing page Next.js + Tailwind untuk toko kopi lokal. Dark mode. Section: hero, menu (4 produk dummy), tentang, footer. Style minimal, accent #4EBAEC.

        V0 akan generate kode. Klik tombol "Code" untuk ambil source.

        **Pendekatan B — pakai template**

        Buka terminal di folder kosong:

        ```bash
        npx create-next-app@latest landing-kopi
        ```

        Pilih: TypeScript Yes, Tailwind Yes, App Router Yes, sisanya default.

        ### Step 2 — Buka di Cursor

        Buka folder project di Cursor (File → Open Folder). Edit `app/page.tsx` sesuai kebutuhan. Pakai Cursor AI (⌘K) untuk modifikasi cepat.

        Coba di lokal: `npm run dev` lalu buka [localhost:3000](http://localhost:3000).

        ### Step 3 — Push ke GitHub

        Buat repo baru di GitHub (lihat lesson 2 untuk perintahnya). Lalu di terminal Cursor:

        ```bash
        git init
        git add .
        git commit -m "init: landing page kopi"
        git remote add origin https://github.com/USERNAME/landing-kopi.git
        git branch -M main
        git push -u origin main
        ```

        ### Step 4 — Deploy ke Vercel

        Buka [vercel.com/new](https://vercel.com/new). Pilih repo kamu dari list. Vercel deteksi Next.js otomatis. Klik **Deploy**.

        Tunggu 30-60 detik. Vercel kasih URL `landing-kopi.vercel.app`. Buka di browser, harus tampil halamanmu.

        ### Step 5 — Iterasi

        Mau ubah sesuatu? Edit di Cursor, push ke GitHub, Vercel auto-redeploy. Loop ini cepat sekali — biasanya 1-2 menit dari edit ke live.

        ### Catatan kalau ada error

        - **Build failed di Vercel.** Buka logs di Vercel, biasanya error import atau env yang kurang. Copy error ke Claude/ChatGPT untuk diagnosis.
        - **Halaman 404.** Pastikan struktur file di App Router benar (`app/page.tsx`).
        - **Style tidak muncul.** Pastikan `app/globals.css` di-import di `app/layout.tsx`.
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup Next.js paling cepat:

        ```bash
        # Buat project baru
        npx create-next-app@latest landing-kopi --ts --tailwind --app

        # Masuk ke folder
        cd landing-kopi

        # Test lokal
        npm run dev
        # buka http://localhost:3000

        # Bikin commit pertama
        git init
        git add .
        git commit -m "init: nextjs + tailwind"
        ```

        Deploy ke Vercel sekali klik dari [vercel.com/new](https://vercel.com/new) setelah push ke GitHub.
        """
    ),
    practice=(
        "Selesaikan lima step di atas sampai kamu punya URL Vercel yang bisa "
        "dibuka publik. Tidak harus cantik. Yang penting LIVE. Catat URL-nya."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Build di Vercel gagal:

            Error: Module not found: Can't resolve '@/components/Hero'
            in '/vercel/path0/app/page.tsx'
            """
        ),
        "hint": (
            "Error ini biasanya karena alias `@/` belum dikonfigurasi atau "
            "file yang di-import tidak ada di repo."
        ),
        "answer_explanation": dedent(
            """\
            Dua kemungkinan penyebab:

            1. File `components/Hero.tsx` ada di lokal tapi tidak ter-push ke GitHub. Cek dengan `git status` lalu push file yang ketinggalan.
            2. Alias `@/` belum dikonfigurasi di `tsconfig.json`. Default `create-next-app` sudah set ini, tapi kalau project manual mungkin belum.
            """
        ),
        "fixed_code": dedent(
            """\
            // tsconfig.json
            {
              "compilerOptions": {
                "baseUrl": ".",
                "paths": {
                  "@/*": ["./*"]
                }
              }
            }

            # Lalu pastikan file ke-push:
            git add components/Hero.tsx
            git commit -m "add: Hero component"
            git push
            """
        ),
    },
    quiz=[
        q(
            "Apa gunanya `npm run dev`?",
            [
                "Deploy ke Vercel",
                "Menjalankan project di lokal untuk testing (biasanya di localhost:3000)",
                "Build project",
                "Hapus node_modules",
            ],
            "B",
            "`npm run dev` mengaktifkan development server di komputermu sendiri sehingga kamu bisa preview sebelum deploy.",
        ),
        q(
            "Apa yang terjadi setelah kamu push ke GitHub kalau Vercel sudah connect?",
            [
                "Tidak terjadi apa-apa",
                "Vercel otomatis redeploy",
                "GitHub menghapus repo",
                "Cursor restart",
            ],
            "B",
            "Vercel-GitHub connection bikin auto-redeploy tiap ada push baru ke main branch. Loop cepat untuk iterasi.",
        ),
        q(
            "Kalau build gagal di Vercel, langkah PERTAMA yang sebaiknya dilakukan?",
            [
                "Hapus semua file dan ulangi",
                "Buka logs di Vercel, baca error message-nya, lalu diagnosis",
                "Ganti ke Netlify",
                "Kirim email ke Vercel",
            ],
            "B",
            "Logs di Vercel kasih pesan error spesifik. Dari situ baru kamu bisa diagnosis (atau copy ke AI untuk dibantu).",
        ),
        q(
            "Apa keuntungan login Vercel pakai akun GitHub?",
            [
                "Tidak ada",
                "Vercel langsung lihat repo GitHub kamu, tinggal pilih repo lalu deploy",
                "Akun jadi lebih mahal",
                "GitHub bayar Vercel",
            ],
            "B",
            "Tanpa login GitHub, kamu harus setup webhook manual atau upload manual. Pakai login GitHub jauh lebih cepat.",
        ),
        q(
            "Mana praktik yang BAIK saat pertama kali deploy?",
            [
                "Commit semua kode dalam satu file besar",
                "Bikin halaman sederhana dulu yang penting LIVE, baru iterasi tambah fitur",
                "Tunggu sampai sempurna sebelum push",
                "Tidak deploy, simpan di lokal saja",
            ],
            "B",
            "Filosofi 'live first, polish later' bikin kamu dapat momentum. Halaman sederhana yang live lebih berharga daripada halaman komplit yang masih di lokal.",
        ),
    ],
    common_mistakes=[
        "Tunggu sampai 'sempurna' baru deploy. Akhirnya tidak pernah deploy.",
        "Lupa push file penting yang masih di lokal. Build di Vercel error 'module not found'.",
        "Tidak baca logs Vercel saat build gagal. Langsung tanya AI tanpa konteks.",
    ],
    checkpoint=[
        "Punya URL Vercel publik yang bisa dibuka.",
        "Tahu cara push perubahan dari Cursor sampai live di Vercel.",
        "Bisa baca logs Vercel saat build gagal.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_LANDING_LIVE = make_lesson(
    title="Mini Project — Landing Page Pertamamu yang Live",
    slug="mini-project-landing-page-live",
    order_index=4,
    read_time="60 menit",
    summary="Aplikasikan semuanya: dari prompt ke URL publik dalam satu sesi.",
    tools=["Cursor", "GitHub", "Vercel", "AI assistant pilihanmu"],
    outcomes=[
        "Bangun landing page tema bebas, tampil rapi di HP dan desktop",
        "Punya repo GitHub publik yang rapi",
        "Punya URL Vercel publik yang bisa dibagikan",
    ],
    tldr=(
        "Pilih satu topik (boleh fiksi). Bangun landing page satu halaman "
        "dengan AI. Push ke GitHub. Deploy ke Vercel. Bagikan URL ke teman."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungkan semua yang sudah dipelajari.

        Tidak harus tema bisnis serius. Pilih sesuatu yang kamu suka — band favorit, game lokal, kucing kamu, side hustle, organisasi kampus. Apa saja.

        Yang penting: hari ini selesai dan URL-nya bisa dibagikan ke teman.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Tech stack: Next.js 14 + Tailwind + shadcn/ui (opsional). Tanpa custom backend dulu — fokus tampilan.

        Section minimal:

        - **Hero.** Judul besar, tagline satu kalimat, CTA satu tombol.
        - **Tentang / Fitur.** Tiga atau empat poin pendek dalam grid.
        - **Galeri / Showcase / Menu.** Visual berbentuk grid, minimal empat item.
        - **Footer.** Kontak atau social link.

        ### Alur kerja yang disarankan

        1. **Tulis prompt awal** pakai template Level 0 Lesson 3. Kasih ke Claude/ChatGPT untuk plan struktur file.
        2. **Setup project Next.js** lewat `create-next-app` atau salin dari V0.
        3. **Buka di Cursor**, edit `app/page.tsx`. Pakai ⌘K untuk minta AI bikin section per section.
        4. **Test lokal** dengan `npm run dev`. Buka di mode HP via DevTools (F12 → Toggle device toolbar).
        5. **Push ke GitHub** dengan pesan commit yang rapi.
        6. **Deploy ke Vercel** dengan satu klik.
        7. **Test URL publik** di HP asli, bukan cuma di simulator.

        ### Tips polish

        - Pilih **satu** font Google Fonts (Inter, Poppins, atau Plus Jakarta Sans aman).
        - Pilih **satu** warna aksen. Sisanya pakai abu-abu/putih untuk kontras.
        - Spacing penting. Kasih banyak padding di antar section.
        - Foto bisa pakai [unsplash.com](https://unsplash.com) (gratis, kredit di footer kalau dipakai).
        - Hindari emoji berlebihan. Itu bikin kelihatan amatir.

        ### Submit

        Setelah live, salin URL ke catatan kamu. Bagikan ke minimal satu teman dan tanya: "Apa kesan pertama kamu?". Feedback dari user asli berharga.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sketch struktur file yang masuk akal:

        ```text
        app/
          ├── layout.tsx         (root layout, Tailwind, font)
          ├── page.tsx           (homepage — semua section di sini)
          └── globals.css        (Tailwind base + custom var)
        components/
          ├── Hero.tsx
          ├── Features.tsx
          ├── Showcase.tsx
          └── Footer.tsx
        public/
          └── og-image.png       (untuk preview saat dibagikan di sosmed)
        ```

        Kamu boleh taruh semua section langsung di `app/page.tsx` untuk kesederhanaan. Pisahkan jadi component kalau sudah lebih besar.
        """
    ),
    practice=(
        "Selesaikan project. Target: URL Vercel yang bisa dibuka, tampil bagus "
        "di desktop DAN HP, repo GitHub-nya rapi (ada README minimal). Catat URL "
        "untuk update di portfolio nanti."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Hasil build di Vercel sukses, tapi saat dibuka di HP semua
            text mepet ke pinggir layar dan ada horizontal scroll.
            """
        ),
        "hint": (
            "Dua hal yang sering jadi penyebab: meta viewport tidak ada, dan "
            "elemen lebih lebar dari layar."
        ),
        "answer_explanation": dedent(
            """\
            Penyebab umum:

            1. Tag `<meta viewport>` tidak ada di `<head>`. Untungnya `create-next-app` sudah pasang, jadi cek `app/layout.tsx`.
            2. Ada elemen dengan width fixed (misal `width: 1200px`) yang lebih besar dari layar HP.
            3. Tidak pakai padding horizontal di section.

            Solusi: pakai class Tailwind `mx-auto max-w-screen-xl px-4` di pembungkus konten.
            """
        ),
        "fixed_code": dedent(
            """\
            // app/layout.tsx — pastikan ada
            export const viewport = {
              width: "device-width",
              initialScale: 1,
            };

            // Pembungkus section
            <section className="mx-auto max-w-screen-xl px-4 py-16">
              {/* konten */}
            </section>
            """
        ),
    },
    quiz=[
        q(
            "Mana praktik yang paling baik untuk halaman responsive?",
            [
                "Bikin layout fixed 1200px supaya selalu sama",
                "Pakai class responsive Tailwind dan max-width agar adaptif di mobile dan desktop",
                "Bikin halaman terpisah untuk mobile",
                "Tidak perlu, browser otomatis menyesuaikan",
            ],
            "B",
            "Pakai responsive utilities (sm:, md:, lg:) dan max-width supaya satu halaman jalan di semua device.",
        ),
        q(
            "Apa pesan commit yang BAIK untuk project ini?",
            [
                "\"update\"",
                "\"feat: hero section dengan CTA dan tagline\"",
                "\"asdf\"",
                "\"WIP\"",
            ],
            "B",
            "Pesan commit deskriptif dengan prefix (feat, fix, refactor) bikin history mudah dibaca.",
        ),
        q(
            "Kapan kamu sebaiknya minta feedback ke teman?",
            [
                "Setelah halaman 100% sempurna",
                "Saat halaman sudah live, walau belum 'sempurna' — feedback dari user asli berharga",
                "Tidak perlu feedback",
                "Setelah dapat klien pertama",
            ],
            "B",
            "Feedback dari mata orang lain mengungkap blind spot. Lebih cepat minta feedback, lebih cepat halaman jadi lebih baik.",
        ),
        q(
            "Apa fungsi `<meta viewport>`?",
            [
                "Tidak penting",
                "Memberi tahu browser HP untuk render halaman dengan skala device, bukan desktop",
                "Mempercepat halaman",
                "Untuk SEO saja",
            ],
            "B",
            "Tanpa meta viewport, browser HP merender halaman seperti desktop kecil. Hasilnya semua mepet dan ada zoom default.",
        ),
        q(
            "Mana yang paling penting untuk landing page pertama?",
            [
                "Animasi yang banyak",
                "Halaman LIVE dengan URL publik, tampil rapi di HP",
                "Logo yang dirancang profesional di Adobe Illustrator",
                "Backend dengan database",
            ],
            "B",
            "Yang penting halaman bisa diakses publik dan tampil OK di HP. Polish lain menyusul.",
        ),
    ],
    common_mistakes=[
        "Project terlalu ambisius di hari pertama. Hasilnya tidak selesai.",
        "Lupa test di HP sungguhan. Hanya test di simulator.",
        "Pesan commit asal-asalan. History repo jadi tidak bisa dibaca.",
    ],
    checkpoint=[
        "URL Vercel publik bisa dibuka.",
        "Tampilan rapi di HP dan desktop.",
        "Repo GitHub punya README minimal.",
        "Sudah dibagikan ke minimal satu teman.",
    ],
    xp_reward=200,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=1,
    slug="first-app-experience",
    title="First App Experience",
    subtitle="Rasakan: 'Saya bisa bikin app'",
    description=(
        "Install tools, kuasai dasar Git, lalu deploy landing page pertamamu "
        "ke internet. Tujuan utama level ini: kasih kamu pengalaman pertama "
        "punya URL publik yang bisa dibagikan."
    ),
    duration="~1 minggu",
    difficulty="Pemula",
    accent_color="from-emerald-400/30 to-violet-500/10",
    mini_project="Landing Page Pertamamu yang Live",
    tags=["Setup", "Git", "Deploy", "Vercel", "Next.js"],
    lessons=[LESSON_SETUP, LESSON_GIT, LESSON_DEPLOY, PROJECT_LANDING_LIVE],
)
