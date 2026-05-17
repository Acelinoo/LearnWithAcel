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
    title="Install Tools yang Diperlukan",
    slug="setup-environment",
    order_index=1,
    read_time="10 menit",
    summary="Install Node.js, Cursor, dan siapin akun GitHub + Vercel.",
    tools=["Browser", "Node.js LTS", "Cursor", "Akun GitHub", "Akun Vercel"],
    outcomes=[
        "Bisa install Node.js dan ngecek dari terminal",
        "Bisa install Cursor sama login akun-nya",
        "Punya akun GitHub dan Vercel yang udah saling konek",
    ],
    tldr=(
        "Install Node.js LTS, install Cursor, terus login ke GitHub sama "
        "Vercel. Cek semua jalan dengan ngetik `node -v` di terminal."
    ),
    pembuka=dedent(
        """\
        Banyak orang gagal di langkah ini bukan karena susah, tapi karena bingung mulai dari mana. Ada banyak link, banyak akun, banyak instruksi.

        Lesson ini jelas banget. Cuma install tiga hal sama bikin dua akun.

        Setelah ini selesai, kamu siap deploy website pertamamu di lesson 3.
        """
    ),
    penjelasan=dedent(
        """\
        ### Step 1 — Install Node.js

        Node.js itu mesin yang bikin tools modern bisa jalan di komputer kamu.

        Buka [nodejs.org](https://nodejs.org), download yang versi **LTS** (Long Term Support, yang stabil). Jalanin installer-nya, klik next-next sampai selesai.

        Habis itu, buka terminal (Command Prompt di Windows, Terminal di macOS/Linux). Ketik `node -v`. Kalau muncul versi kayak `v20.x.x`, berarti udah berhasil.

        ### Step 2 — Install Cursor

        Cursor itu code editor yang udah ada AI di dalemnya. Buka [cursor.com](https://cursor.com), klik Download, install kayak aplikasi biasa.

        Pas pertama kali buka, login pake email atau Google. Pilih theme dark (lebih nyaman buat sesi panjang).

        ### Step 3 — Bikin akun GitHub

        Buka [github.com](https://github.com), Sign Up. Pilih username yang profesional — itu bakal jadi bagian URL portfolio kamu nanti.

        Verifikasi email. Selesai.

        ### Step 4 — Bikin akun Vercel

        Buka [vercel.com](https://vercel.com), klik Sign Up, pilih **Continue with GitHub**. Vercel langsung konek ke akun GitHub kamu.

        Trick-nya: dengan login pake GitHub, deploy nanti tinggal pilih repo doang.

        ### Cek semua udah siap

        Buka terminal, ketik `node -v` sama `npm -v`. Dua-duanya harus nge-return versi.

        Buka Cursor, klik Settings → Account. Email kamu harus muncul di sana.

        Buka [vercel.com/dashboard](https://vercel.com/dashboard). Harus muncul akun kamu, bukan halaman login.

        ### Kalau ada masalah

        Yang sering terjadi:

        - `node` gak dikenal di Windows? Tutup terminal lama, buka baru. Kalau masih, restart komputer.
        - Cursor lambat? Tutup Discord/Spotify yang berat biar RAM lega.
        - Vercel gak munculin GitHub repos? Reauthorize GitHub di Settings → Git.
        """
    ),
    contoh_code_md=dedent(
        """\
        Cek instalasi via terminal:

        ```bash
        # Cek versi Node.js
        node -v
        # output: v20.18.0 (atau yang mirip)

        # Cek versi npm (Node Package Manager — bawaan Node)
        npm -v
        # output: 10.x.x
        ```

        Kalau dua command di atas nge-return versi, berarti kamu siap lanjut ke lesson berikutnya.
        """
    ),
    practice=(
        "Selesain empat step di atas: install Node.js, install Cursor, bikin "
        "akun GitHub, bikin akun Vercel (login pake GitHub). Cek `node -v` di "
        "terminal nge-return versi."
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
            "Error ini biasa muncul di Windows habis install Node.js. Bukan "
            "masalah kode — masalah environment."
        ),
        "answer_explanation": dedent(
            """\
            Penyebabnya: PATH environment variable belum ke-update. Solusinya:

            1. Tutup terminal yang lama, buka terminal baru.
            2. Kalau masih error, restart komputer.
            3. Kalau masih juga, install ulang Node.js dan pastiin opsi "Add to PATH" tercentang pas installer jalan.
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
            "LTS di Node.js itu apa?",
            [
                "Versi paling baru yang barusan dirilis hari ini",
                "Long Term Support — versi stabil yang dapet update keamanan jangka panjang",
                "Light Typescript Support",
                "Versi yang gratis",
            ],
            "B",
            "LTS itu Long Term Support. Versi ini lebih stabil dan aman buat produksi. Selalu pilih ini buat pemula.",
        ),
        q(
            "Gimana cara cek Node.js udah ke-install?",
            [
                "Buka GitHub",
                "Ketik `node -v` di terminal, harus muncul versi",
                "Cek di Cursor",
                "Gak ada caranya",
            ],
            "B",
            "`node -v` itu cara standar buat cek instalasi.",
        ),
        q(
            "Kenapa login Vercel pake GitHub direkomendasiin?",
            [
                "Karena gratis (GitHub berbayar)",
                "Karena Vercel bisa langsung baca dan deploy repo GitHub kamu",
                "Gak ada alasan",
                "Diwajibin hukum",
            ],
            "B",
            "Vercel auto-deploy dari GitHub. Login pake GitHub bikin proses ini langsung nyambung.",
        ),
        q(
            "Apa yang harus dilakuin kalau `node -v` nge-return 'not recognized'?",
            [
                "Beli laptop baru",
                "Tutup terminal lama, buka baru. Kalau masih, restart komputer atau install ulang dengan opsi 'Add to PATH'",
                "Ganti Cursor",
                "Gak bisa diperbaiki",
            ],
            "B",
            "Error ini soal PATH environment yang belum ke-load. Restart terminal atau komputer biasanya udah cukup.",
        ),
        q(
            "Mana urutan setup yang paling efisien?",
            [
                "Install semua bareng, terus baru bikin akun",
                "Node.js → Cursor → akun GitHub → akun Vercel (login pake GitHub) → cek semuanya",
                "Akun dulu semua, baru install",
                "Gak penting urutannya",
            ],
            "B",
            "Urutan ini ngehindarin error dependency. Vercel login pake GitHub paling akhir karena butuh akun GitHub udah ada dulu.",
        ),
    ],
    common_mistakes=[
        "Skip restart terminal habis install Node.js. Akhirnya bingung kenapa `node -v` gak jalan.",
        "Pake username GitHub yang aneh. Itu bakal nongol di URL portfolio kamu nanti.",
        "Lupa login Vercel pake GitHub. Akhirnya proses deploy nanti lebih ribet.",
    ],
    checkpoint=[
        "`node -v` sama `npm -v` nge-return versi",
        "Cursor terbuka dengan akun login",
        "Akun GitHub aktif dengan username profesional",
        "Akun Vercel udah konek ke GitHub",
    ],
    xp_reward=60,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — GitHub Basics
# ─────────────────────────────────────────────────────────────────────────────

LESSON_GIT = make_lesson(
    title="GitHub Dasar — Repo, Commit, Push",
    slug="github-basics",
    order_index=2,
    read_time="12 menit",
    summary="Tiga aksi yang bakal kamu lakuin tiap hari sebagai developer.",
    tools=["Cursor", "Akun GitHub", "Terminal"],
    outcomes=[
        "Bisa bikin repository baru di GitHub",
        "Tau commit dan push itu apa, beda di mana",
        "Bisa jalanin tiga command Git dasar dari terminal",
    ],
    tldr=(
        "GitHub itu kayak Google Drive khusus kode, tapi bisa jadi mesin "
        "waktu juga. Commit = simpan checkpoint. Push = upload ke GitHub. "
        "Tiga command cukup buat hari pertama: `git init`, `git commit`, "
        "`git push`."
    ),
    pembuka=dedent(
        """\
        GitHub itu bukan cuma "tempat simpan kode". Dia juga nyimpen SEJARAH kode kamu — kapan kamu ngubah apa, kenapa, sama siapa.

        Bayangin kayak Google Drive khusus kode, plus mesin waktu. Kamu bisa balik ke versi minggu lalu kalau hari ini ada yang rusak.

        Tools-nya namanya Git (yang lokal di komputer). GitHub itu layanan online yang nerima Git push kamu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga konsep dasar

        - **Repository (repo)** — folder project kamu yang dilacak Git.
        - **Commit** — snapshot perubahan plus pesan. Ibarat checkpoint di game.
        - **Push** — kirim commit lokal ke GitHub.

        ### Alur kerja standar

        1. Bikin folder project baru di komputer
        2. Init Git: `git init`
        3. Bikin file, tulis kode
        4. `git add .` (tandain semua file buat masuk ke commit berikut)
        5. `git commit -m "pesan"` (bikin checkpoint)
        6. Bikin repo di GitHub
        7. Konekin lokal ke GitHub: `git remote add origin <url>`
        8. `git push -u origin main` (upload ke GitHub)

        Step 1-7 cuma sekali. Sehari-hari, kerja kamu tinggal:

        ```bash
        git add .
        git commit -m "pesan singkat"
        git push
        ```

        ### Pesan commit yang bagus

        Tulis pesan yang jelasin **kenapa**, bukan **apa**.

        - Jelek: "update file"
        - Bagus: "fix bug login pas email kosong"

        Kebiasaan yang oke: prefix pake kata kerja imperatif. `add`, `fix`, `refactor`, `remove`, `docs`.

        ### Bikin repo di GitHub

        Buka [github.com/new](https://github.com/new). Isi:

        - **Repository name** — nama project (contoh `landing-toko-kopi`)
        - **Public** atau **Private** — Public boleh buat portfolio
        - **Add README** centang aja (biar repo gak kosong)

        Klik Create. Selesai.

        ### Cursor punya UI Git built-in

        Gak harus selalu pake terminal. Cursor punya tab Source Control (icon cabang di sidebar kiri) yang bisa stage, commit, sama push tinggal klik.

        Tapi pelajari dulu command terminal-nya — kamu bakal butuh kalau lagi remote work atau masuk ke server.
        """
    ),
    contoh_code_md=dedent(
        """\
        Bikin repo lokal pertama dan push ke GitHub:

        ```bash
        # Di folder project
        mkdir landing-toko-kopi
        cd landing-toko-kopi

        # Init Git
        git init

        # Bikin file dummy
        echo "# Landing Toko Kopi" > README.md

        # Tandain dan commit
        git add .
        git commit -m "init: setup project"

        # Konekin ke GitHub (URL dari halaman repo baru kamu)
        git remote add origin https://github.com/USERNAME/landing-toko-kopi.git

        # Push ke GitHub
        git branch -M main
        git push -u origin main
        ```

        Habis itu refresh halaman repo di GitHub. README.md bakal nongol.
        """
    ),
    practice=(
        "Bikin satu repo baru di GitHub dengan nama `vibe-test`. Clone ke "
        "komputer pake `git clone <url>`. Bikin file `hello.txt` isinya nama "
        "kamu, terus add → commit → push. Refresh halaman GitHub, file "
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
        "hint": "Error ini muncul kalau kamu di folder yang belum diinit Git.",
        "answer_explanation": dedent(
            """\
            Penyebabnya: folder yang sekarang belum di-`git init`, atau kamu salah pindah ke folder lain yang bukan repo.

            Solusinya:

            1. Cek lokasi folder pake `pwd` (macOS/Linux) atau `cd` (Windows).
            2. Pastiin kamu di dalem folder project yang udah di-init.
            3. Kalau belum, jalanin `git init` dulu.
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
                "Ngirim kode ke GitHub",
                "Bikin checkpoint perubahan dengan pesan",
                "Hapus file",
                "Bikin repo baru",
            ],
            "B",
            "Commit nyimpen snapshot perubahan plus pesan deskriptif. Push baru yang ngirim commit ke GitHub.",
        ),
        q(
            "Apa yang dilakuin `git push`?",
            [
                "Bikin snapshot lokal",
                "Ngirim commit lokal ke remote (GitHub)",
                "Download kode dari GitHub",
                "Hapus repo",
            ],
            "B",
            "`git push` upload commit dari lokal ke GitHub.",
        ),
        q(
            "Mana pesan commit yang BAGUS?",
            [
                "\"update\"",
                "\"fix bug login pas email kosong\"",
                "\"asdfg\"",
                "\"WIP\"",
            ],
            "B",
            "Pesan yang bagus jelasin KENAPA dan APA yang berubah secara spesifik. Itu bantu kamu (dan orang lain) di masa depan.",
        ),
        q(
            "Kenapa harus `git init` di awal?",
            [
                "Gak perlu, opsional",
                "Buat ngasih tau Git kalau folder ini bakal dilacak sebagai repo",
                "Buat bikin akun GitHub",
                "Buat install Node.js",
            ],
            "B",
            "`git init` bikin folder `.git` yang nyimpen history. Tanpa ini, Git gak tau folder kamu adalah repo.",
        ),
        q(
            "Apa siklus harian Git habis setup awal?",
            [
                "init → init → init",
                "add → commit → push",
                "delete → reinstall",
                "Gak ada siklus",
            ],
            "B",
            "Tiga command ini siklus utama: tandain perubahan, commit dengan pesan, push ke GitHub.",
        ),
    ],
    common_mistakes=[
        "Lupa `git init` di awal. Akhirnya `git status` error 'not a git repository'.",
        "Pesan commit asal kayak 'update', 'fix', 'asdf'. History repo jadi gak bisa dibaca.",
        "Push tiap baris kode. Mendingan commit per fitur atau perubahan logis.",
    ],
    checkpoint=[
        "Bisa bikin repo dari nol dan push ke GitHub",
        "Tau bedanya commit dan push",
        "Bisa nulis pesan commit yang deskriptif",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Deploy Website Pertama
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DEPLOY = make_lesson(
    title="Deploy Website Pertama Kamu",
    slug="deploy-website-pertama",
    order_index=3,
    read_time="10 menit",
    summary="Generate landing page pake AI, push ke GitHub, deploy ke Vercel.",
    tools=["Cursor", "V0 atau Bolt (boleh skip)", "GitHub", "Vercel"],
    outcomes=[
        "Bisa generate landing page sederhana pake AI",
        "Push project ke GitHub",
        "Deploy ke Vercel dan dapet URL publik",
    ],
    tldr=(
        "Generate landing page pake AI atau template. Buka di Cursor, push "
        "ke GitHub, import ke Vercel. Selesai. URL publik dalam <30 menit."
    ),
    pembuka=dedent(
        """\
        Lesson ini momen krusial. Selesai ini, kamu punya website yang live di internet.

        Itu bukan sekadar checklist. Itu sinyal mental: "saya bisa".

        Banyak orang udah belajar coding bertahun-tahun tapi belum pernah punya satu URL pun yang bisa dibuka publik. Hari ini kamu lompatin itu.
        """
    ),
    penjelasan=dedent(
        """\
        ### Step 1 — Generate landing page

        Pilih salah satu cara:

        **Cara A — pake V0**

        Buka [v0.dev](https://v0.dev), kasih prompt:

        > Bikin landing page Next.js + Tailwind buat toko kopi lokal. Dark mode. Section: hero, menu (4 produk dummy), tentang, footer. Style minimal, accent #4EBAEC.

        V0 bakal generate kode. Klik tombol "Code" buat ngambil source-nya.

        **Cara B — pake template**

        Buka terminal di folder kosong:

        ```bash
        npx create-next-app@latest landing-kopi
        ```

        Pilih: TypeScript Yes, Tailwind Yes, App Router Yes, sisanya default.

        ### Step 2 — Buka di Cursor

        Buka folder project di Cursor (File → Open Folder). Edit `app/page.tsx` sesuai kebutuhan. Pake AI Cursor (⌘K) buat modifikasi cepet.

        Cek di lokal: `npm run dev`, terus buka [localhost:3000](http://localhost:3000).

        ### Step 3 — Push ke GitHub

        Bikin repo baru di GitHub (cara-nya udah di lesson 2). Terus di terminal Cursor:

        ```bash
        git init
        git add .
        git commit -m "init: landing page kopi"
        git remote add origin https://github.com/USERNAME/landing-kopi.git
        git branch -M main
        git push -u origin main
        ```

        ### Step 4 — Deploy ke Vercel

        Buka [vercel.com/new](https://vercel.com/new). Pilih repo kamu dari list. Vercel auto-detect: "Oh ini Next.js project". Settings default udah bener.

        Klik **Deploy**.

        Tungguin 30-60 detik. Vercel lagi:

        1. Download kode dari GitHub
        2. Run `npm install`
        3. Run `npm run build`
        4. Upload hasil build ke server mereka

        Selesai. Kamu dapet URL `landing-kopi.vercel.app`. Klik buat buka.

        ### Step 5 — Cek live URL

        Buka URL di browser. Halaman kamu live.

        Lebih keren lagi: kasih URL ke temen lewat WhatsApp. Mereka bisa buka dari HP mereka, dari mana aja di Indonesia atau dunia. Itu yang dimaksud "live di internet".

        ### Step 6 — Update project habis deploy

        Mau ubah text di homepage? Edit di laptop, terus push:

        ```bash
        git add .
        git commit -m "fix: ganti tagline hero"
        git push
        ```

        Vercel deteksi push baru. Auto re-build dan re-deploy. Sekitar 30-60 detik kemudian, URL kamu udah update.

        Kamu gak perlu klik apapun di Vercel. Cara kerja kayak gini disebut **continuous deployment**.

        ### Custom domain (opsional)

        URL `landing-kopi.vercel.app` panjang. Kalau punya domain sendiri (misal `acel.dev`):

        - Beli domain di [Niagahoster](https://www.niagahoster.co.id) atau [Namecheap](https://www.namecheap.com).
        - Di Vercel: Project → Settings → Domains → Add. Masukin domain kamu.
        - Vercel kasih instruksi DNS. Salin ke panel domain provider.
        - Tunggu 5-30 menit, domain aktif. SSL otomatis.

        Total cost: domain ~Rp 150rb/tahun. Hosting tetep gratis.

        ### Kalau build error

        Sering kejadian: deploy gagal padahal di laptop jalan.

        Penyebab paling umum:

        - **Environment variable belum ada di Vercel** — edit di Project Settings → Environment Variables.
        - **TypeScript error yang di dev kamu di-ignore** — Vercel build strict, harus diperbaiki.
        - **File belum di-commit ke Git** — cek `git status`, push file yang ketinggalan.

        Cek logs di Vercel (klik deploy yang gagal → Logs). Pesan error spesifik biasanya jelas.
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup awal Git buat project baru:

        ```bash
        # Di root project
        git init
        echo "node_modules" > .gitignore
        echo ".env.local" >> .gitignore
        echo ".next" >> .gitignore

        git add .
        git commit -m "init: setup project Next.js"
        ```

        Push ke GitHub repo baru:

        ```bash
        git remote add origin https://github.com/USERNAME/REPO.git
        git branch -M main
        git push -u origin main
        ```

        Workflow harian habis deploy:

        ```bash
        # Setelah edit kode di laptop
        git add .
        git commit -m "feat: tambah halaman about"
        git push

        # Vercel auto-deploy. Cek di vercel.com/dashboard.
        ```
        """
    ),
    practice=(
        "Push project Next.js dari lesson sebelumnya ke GitHub. Terus import "
        "ke Vercel dan deploy. Salin URL Vercel. Kirim URL itu ke minimal "
        "satu temen lewat chat — pastiin mereka bisa buka di HP. Habis itu, "
        "edit satu kata di homepage, commit, push, dan tunggu auto-redeploy."
    ),
    fix_error={
        "language": "bash",
        "broken_code": dedent(
            """\
            # User report:
            "Saya udah deploy ke Vercel, tapi halamannya blank putih.
            Logs Vercel bilang: 'Error: NEXT_PUBLIC_API_URL is not defined'."
            """
        ),
        "hint": "Project di laptop pake file `.env.local`. File itu gak ke-push ke GitHub karena di-gitignore. Terus di Vercel?",
        "answer_explanation": dedent(
            """\
            Penyebabnya: env variable di `.env.local` cuma jalan di laptop kamu. File itu sengaja di-gitignore biar rahasia (misal API key) gak bocor ke GitHub.

            Pas deploy ke Vercel, kamu harus tambahin env variable secara terpisah di Vercel.

            Solusinya:

            1. Buka Vercel dashboard → project kamu
            2. Settings → Environment Variables
            3. Tambahin satu-satu yang ada di `.env.local`
            4. Klik Save. Re-deploy (klik tombol di tab Deployments)

            Habis itu halaman bakal jalan normal.
            """
        ),
        "fixed_code": dedent(
            """\
            # Di Vercel: Settings → Environment Variables

            Name:  NEXT_PUBLIC_API_URL
            Value: https://api.example.com
            Environments: Production, Preview, Development (centang semua)

            # Klik Save, terus di tab Deployments → Redeploy.
            """
        ),
    },
    quiz=[
        q(
            "'Deploy' project itu apa?",
            [
                "Nyimpen project di Google Drive",
                "Upload project ke server yang nyala 24 jam biar bisa diakses siapa aja lewat URL publik",
                "Jalanin `npm run dev`",
                "Bikin backup",
            ],
            "B",
            "Deploy = pindahin project dari laptop kamu ke server di internet. Itu yang ngebedain 'localhost' sama 'live'.",
        ),
        q(
            "Kenapa temen gak bisa buka URL `localhost:3000` yang kamu kirim?",
            [
                "URL salah ketik",
                "`localhost` artinya 'komputer ini sendiri' — cuma device yang ngejalanin project yang bisa akses",
                "Internet putus",
                "Wajib pake HTTPS",
            ],
            "B",
            "`localhost` itu loopback ke device sendiri. Gak ada cara temen akses dari laptop atau HP mereka tanpa deploy.",
        ),
        q(
            "Habis project kamu di-push ke GitHub dan di-deploy ke Vercel, apa yang terjadi pas kamu push lagi?",
            [
                "Gak ada",
                "Vercel deteksi push baru dan auto-redeploy ke URL yang sama",
                "Vercel hapus project lama",
                "Kamu harus deploy manual lagi",
            ],
            "B",
            "Continuous deployment: GitHub-Vercel connection bikin push baru = redeploy otomatis. Workflow super cepet.",
        ),
        q(
            "Apa yang HARUS di-update di Vercel kalau project kamu pake `.env.local`?",
            [
                "Gak ada",
                "Tambahin env variable yang sama di Vercel Settings → Environment Variables",
                "Push `.env.local` ke GitHub",
                "Hapus `.env.local`",
            ],
            "B",
            "`.env.local` di-gitignore (sengaja) biar gak bocor. Vercel butuh value-nya dimasukin terpisah lewat dashboard.",
        ),
        q(
            "Apa keuntungan utama deploy ke Vercel buat Next.js?",
            [
                "Vercel dibikin sama tim Next.js sendiri, free tier gede, auto-deploy dari GitHub, SSL gratis",
                "Lebih lambat dari hosting lain",
                "Wajib bayar dari hari pertama",
                "Gak ada keuntungan",
            ],
            "A",
            "Vercel dirancang khusus buat Next.js. Setup deploy yang biasanya ribet jadi tinggal klik-klik di dashboard mereka.",
        ),
    ],
    common_mistakes=[
        "Push `.env.local` ke GitHub. API key bocor — siapa aja yang lihat repo bisa pake.",
        "Lupa tambahin env variable di Vercel. Halaman live blank atau crash.",
        "Cuma test di laptop sendiri. Gak buka URL Vercel di HP temen buat konfirm akses publik.",
    ],
    checkpoint=[
        "Punya URL Vercel publik yang bisa dibuka",
        "Bisa push perubahan dari Cursor sampe live di Vercel",
        "Bisa baca logs Vercel kalau build gagal",
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
    summary="Aplikasiin semuanya: dari prompt ke URL publik dalam satu sesi.",
    tools=["Cursor", "GitHub", "Vercel", "AI assistant pilihan kamu"],
    outcomes=[
        "Bisa bangun landing page tema bebas, rapi di HP dan desktop",
        "Punya repo GitHub publik yang rapi",
        "Punya URL Vercel publik yang bisa dibagiin",
    ],
    tldr=(
        "Pilih satu topik (boleh fiksi). Bikin landing page satu halaman pake "
        "AI. Push ke GitHub. Deploy ke Vercel. Bagiin URL ke temen."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungin semua yang udah dipelajari.

        Gak harus tema bisnis serius. Pilih sesuatu yang kamu suka — band favorit, game lokal, kucing kamu, side hustle, organisasi kampus. Apa aja.

        Yang penting: hari ini selesai dan URL-nya bisa dibagiin ke temen.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind + shadcn/ui (opsional). Belum perlu backend custom — fokus tampilan dulu.

        Section minimal:

        - **Hero** — judul gede, tagline kuat satu kalimat, CTA satu tombol
        - **Tentang / Fitur** — tiga atau empat poin pendek dalam grid
        - **Galeri / Showcase / Menu** — visual berbentuk grid, minimal empat item
        - **Footer** — kontak atau social link

        ### Alur kerja yang disaranin

        1. **Tulis prompt awal** pake template Level 0 Lesson 3. Kasih ke Claude/ChatGPT buat plan struktur file
        2. **Setup project Next.js** lewat `create-next-app` atau salin dari V0
        3. **Buka di Cursor**, edit `app/page.tsx`. Pake ⌘K buat minta AI bikin section per section
        4. **Test di lokal** dengan `npm run dev`. Buka di mode HP via DevTools (F12 → Toggle device toolbar)
        5. **Push ke GitHub** dengan pesan commit yang rapi
        6. **Deploy ke Vercel** tinggal klik
        7. **Test URL publik** di HP asli, bukan cuma di simulator

        ### Tips polish

        - Pilih **satu** font Google Fonts (Inter, Poppins, atau Plus Jakarta Sans aman)
        - Pilih **satu** warna aksen. Sisanya pake abu-abu/putih buat kontras
        - Spacing penting. Kasih banyak padding di antar section
        - Foto bisa pake [unsplash.com](https://unsplash.com) (gratis, kredit di footer kalau dipake)
        - Hindari emoji kebanyakan. Itu bikin keliatan amatir

        ### Submit

        Habis live, salin URL ke catatan kamu. Bagiin ke minimal satu temen, terus tanya: "Apa kesan pertama kamu?". Feedback dari user beneran berharga banget.
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
          └── og-image.png       (buat preview pas dibagiin di sosmed)
        ```

        Boleh taro semua section langsung di `app/page.tsx` buat awalnya. Pisahin jadi component kalau udah lebih gede.
        """
    ),
    practice=(
        "Selesain project. Target: URL Vercel yang bisa dibuka, tampil bagus "
        "di desktop DAN HP, repo GitHub-nya rapi (ada README minimal). Catet "
        "URL-nya buat update di portfolio nanti."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Hasil build di Vercel sukses, tapi pas dibuka di HP semua text
            mepet ke pinggir layar dan ada horizontal scroll.
            """
        ),
        "hint": (
            "Dua hal yang sering jadi penyebab: meta viewport gak ada, sama "
            "elemen yang lebih lebar dari layar."
        ),
        "answer_explanation": dedent(
            """\
            Penyebab umum:

            1. Tag `<meta viewport>` gak ada di `<head>`. Untungnya `create-next-app` udah pasang, jadi cek `app/layout.tsx`.
            2. Ada elemen dengan width fixed (misal `width: 1200px`) yang lebih gede dari layar HP.
            3. Gak pake padding horizontal di section.

            Solusinya: pake class Tailwind `mx-auto max-w-screen-xl px-4` di pembungkus konten.
            """
        ),
        "fixed_code": dedent(
            """\
            // app/layout.tsx — pastiin ada
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
            "Mana praktik paling baik buat halaman responsive?",
            [
                "Bikin layout fixed 1200px biar selalu sama",
                "Pake class responsive Tailwind dan max-width biar adaptif di mobile dan desktop",
                "Bikin halaman terpisah buat mobile",
                "Gak perlu, browser auto nyesuaiin",
            ],
            "B",
            "Pake responsive utilities (sm:, md:, lg:) sama max-width biar satu halaman jalan di semua device.",
        ),
        q(
            "Apa pesan commit yang BAGUS buat project ini?",
            [
                "\"update\"",
                "\"feat: hero section dengan CTA dan tagline\"",
                "\"asdf\"",
                "\"WIP\"",
            ],
            "B",
            "Pesan commit deskriptif dengan prefix (feat, fix, refactor) bikin history gampang dibaca.",
        ),
        q(
            "Kapan sebaiknya minta feedback ke temen?",
            [
                "Habis halaman 100% sempurna",
                "Pas halaman udah live, walau belum 'sempurna' — feedback dari user beneran berharga",
                "Gak perlu feedback",
                "Habis dapet klien pertama",
            ],
            "B",
            "Feedback dari mata orang lain ngungkap blind spot. Lebih cepet minta feedback, lebih cepet halaman jadi lebih bagus.",
        ),
        q(
            "Apa fungsi `<meta viewport>`?",
            [
                "Gak penting",
                "Ngasih tau browser HP buat render halaman dengan skala device, bukan desktop",
                "Mempercepat halaman",
                "Buat SEO doang",
            ],
            "B",
            "Tanpa meta viewport, browser HP render halaman kayak desktop kecil. Hasilnya semua mepet dan ada zoom default.",
        ),
        q(
            "Mana yang paling penting buat landing page pertama?",
            [
                "Animasi yang banyak",
                "Halaman LIVE dengan URL publik, tampil rapi di HP",
                "Logo yang dirancang profesional di Adobe Illustrator",
                "Backend dengan database",
            ],
            "B",
            "Yang penting halaman bisa diakses publik dan tampil OK di HP. Polish lain nyusul.",
        ),
    ],
    common_mistakes=[
        "Project kebesaran di hari pertama. Hasilnya gak selesai.",
        "Lupa test di HP sungguhan. Cuma test di simulator.",
        "Pesan commit asal-asalan. History repo jadi gak bisa dibaca.",
    ],
    checkpoint=[
        "URL Vercel publik bisa dibuka",
        "Tampilan rapi di HP dan desktop",
        "Repo GitHub punya README minimal",
        "Udah dibagiin ke minimal satu temen",
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
    subtitle="Rasain pertama kali: 'Saya bisa bikin app'",
    description=(
        "Install tools, kuasain dasar Git, terus deploy landing page pertamamu "
        "ke internet. Tujuan utama level ini: kasih kamu pengalaman pertama "
        "punya URL publik yang bisa dibagiin."
    ),
    duration="~1 minggu",
    difficulty="Pemula",
    accent_color="from-emerald-400/30 to-violet-500/10",
    mini_project="Landing Page Pertamamu yang Live",
    tags=["Setup", "Git", "Deploy", "Vercel", "Next.js"],
    lessons=[LESSON_SETUP, LESSON_GIT, LESSON_DEPLOY, PROJECT_LANDING_LIVE],
)
