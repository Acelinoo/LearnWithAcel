"""
Frontend / Level 5 — Career & Freelance.

Lessons:
  1. membangun-portfolio
  2. github-profile-yang-menarik
  3. cari-project-pertama
  4. mini-project-portfolio-final  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Membangun Portfolio
# ─────────────────────────────────────────────────────────────────────────────

LESSON_PORTFOLIO = make_lesson(
    title="Membangun Portfolio yang Dipercaya",
    slug="membangun-portfolio",
    order_index=1,
    read_time="11 menit",
    summary="Apa yang harus ada, cara presentasi project, dan kesalahan umum.",
    tools=["Notes app", "Browser"],
    outcomes=[
        "Memahami fungsi portfolio (bukan sekadar resume)",
        "Mengetahui struktur portfolio yang baik",
        "Bisa menulis case study project dengan format problem → solution",
    ],
    tldr=(
        "Portfolio = bukti kerja. CV cuma daftar klaim. Yang menentukan: "
        "3-5 project nyata, deskripsi jelas (problem → solution → tech), "
        "live demo, source code di GitHub."
    ),
    pembuka=dedent(
        """\
        Pernah lihat dua kandidat developer? Satu cuma kasih CV teks. Satu lagi kirim link portfolio dengan project live.

        Recruiter atau client hampir selalu pilih yang kedua. Kenapa? Karena CV cuma daftar klaim, sementara portfolio adalah bukti.

        Lesson ini bukan teori karier. Ini panduan konkret: apa yang harus ada di portfolio kamu sebelum apply kerja atau cari klien.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tujuan portfolio

        Satu kalimat: **menunjukkan apa yang bisa kamu kerjakan, dengan bukti**.

        Bukan tempat untuk pamer skill yang dipelajari. Bukan tempat untuk daftar sertifikat. Tempat untuk show, not tell.

        ### Yang HARUS ada

        Lima section minimum:

        - **Hero** — nama kamu, tagline satu kalimat (apa yang kamu lakukan), satu CTA (lihat project / kontak).
        - **About** — paragraf pendek. Dari mana kamu, lagi belajar apa, target karier apa. Jujur > sok-sokan.
        - **Projects** — minimum 3, idealnya 4-6 project. Setiap project punya halaman detail.
        - **Skills** — list teknologi yang kamu kuasai. Realistis, bukan semua yang pernah kamu sentuh.
        - **Contact** — email + LinkedIn + GitHub. Form opsional.

        ### Format project yang efektif

        Jangan cuma nulis "Todo App" + screenshot. Itu tidak cukup. Pakai struktur ini:

        - **Title** — nama project.
        - **Problem** — apa yang dipecahkan? Untuk siapa? (1-2 kalimat)
        - **Solution** — apa yang kamu bangun? Fitur utama? (2-3 kalimat)
        - **Tech stack** — list teknologi. (badge style)
        - **Demo** — link live URL.
        - **Source** — link GitHub.
        - **Lessons learned** — apa yang kamu pelajari saat bangun ini? (1 paragraf, opsional)

        Format ini menunjukkan kamu **berpikir** sebelum coding, bukan asal nyontek tutorial.

        ### Project yang masuk vs yang skip

        **Masuk:**

        - Project nyata dengan problem yang jelas (todo app yang menyimpan data per user, blog dengan CMS, dashboard analytics).
        - Project unik atau personal (tools untuk hobi kamu, app untuk teman).
        - Project dengan teknologi terkini (Next.js, TypeScript, Tailwind).

        **Skip:**

        - 100 todo app yang sama persis dengan tutorial YouTube.
        - Project yang setengah jadi atau ada bug obvious.
        - Project yang tidak deploy (cuma di laptop).
        - Project yang README-nya kosong.

        ### Aturan deploy

        **Setiap project di portfolio HARUS bisa diakses lewat URL publik.**

        Tidak ada excuse. Kalau ada project yang bagus tapi belum deploy, deploy dulu, baru masuk portfolio.

        URL di laptop = project tidak ada untuk recruiter.

        ### Visual matters

        Portfolio yang kelihatan amatir bikin orang ragu. Beberapa hal yang sering luput:

        - **Spacing**. Section harus punya padding minimal `py-24`. Jangan pelit.
        - **Hierarchy**. H1 jelas lebih besar dari H2 dari body text.
        - **Color discipline**. 1 accent color + grayscale. Tidak lebih.
        - **Typography**. Pakai 1-2 font Google (Inter aman). Jangan Comic Sans.
        - **Mobile**. Test di HP. Setiap section harus terbaca tanpa zoom.

        Detail ini terlihat sepele tapi berdampak besar pada first impression.

        ### Tone copy

        Hindari English yang sok-sokan. Kalau target audience kamu Indonesia, bahasa Indonesia santai-profesional.

        - Buruk: "I create stunning user experiences with cutting-edge technologies."
        - Baik: "Saya bikin aplikasi web. Fokus di UX yang bersih dan deploy yang cepat."

        Spesifik > umum. Jujur > exaggerated.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh format project di portfolio (markdown atau JSX):

        ```text
        ──────────────────────────────────────────────────────
        Toko Kopi Lokal
        ──────────────────────────────────────────────────────

        Problem
        Kedai kopi keluarga di Jogja butuh kehadiran online sederhana —
        menu, jam buka, lokasi.

        Solution
        Landing page satu halaman dengan section menu (8 produk dengan
        foto), tentang kami, dan info kontak. Mobile-first, dark mode.

        Tech stack
        Next.js 14 · Tailwind CSS · Vercel

        [Demo →]  [Source →]
        ──────────────────────────────────────────────────────
        ```

        Notice: format ini menjual project, bukan cuma menampilkan.
        """
    ),
    practice=(
        "Buka 3 portfolio developer yang kamu suka (cari di Google "
        "'developer portfolio Indonesia' atau di Twitter). Untuk masing-masing, "
        "tulis di catatan: apa yang membuat portfolio itu kelihatan profesional? "
        "Apa yang akan kamu adopsi untuk portfolio kamu?"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            Project di portfolio:
            - Todo App (cuma screenshot, no link, no source)
            - Calculator
            - Snake Game
            - Tic Tac Toe
            - Counter App
            - Hello World
            """
        ),
        "hint": "Recruiter buka portfolio ini, apa kesannya? Apa yang membedakannya dari ribuan tutorial follower?",
        "answer_explanation": dedent(
            """\
            Kesalahan: project yang dipajang terlihat sebagai tutorial follower. Tidak ada problem statement, tidak ada link, tidak ada konteks.

            Yang lebih efektif:

            - Pilih 3-4 project yang BERBEDA secara fungsi (bukan 6 todo variasi).
            - Setiap project: deploy dengan URL hidup + README yang menjelaskan problem dan solution.
            - Hilangkan project sederhana seperti calculator/counter — itu tidak menambah nilai portfolio.

            Less is more. 3 project bagus kalahkan 10 project medioker.
            """
        ),
        "fixed_code": dedent(
            """\
            Project di portfolio (versi efektif):

            1. Habit Tracker
               - Problem: pelajar butuh cara konsisten bangun rutinitas.
               - Solution: web app dengan check-in harian + streak counter.
               - Stack: Next.js, Prisma, Supabase, NextAuth.
               - [Demo] [Source]

            2. Toko Kopi Landing
               - Problem: kedai kopi lokal butuh online presence.
               - Solution: landing page minimal dengan menu + kontak.
               - Stack: Next.js, Tailwind.
               - [Demo] [Source]

            3. Dashboard SaaS Mini
               - Problem: latihan struktur data-driven UI.
               - Solution: dashboard dengan stats, table, settings.
               - Stack: Next.js, shadcn/ui.
               - [Demo] [Source]
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi portfolio yang membedakannya dari CV?",
            [
                "Tidak ada beda",
                "CV daftar klaim, portfolio adalah bukti — kamu bisa menunjukkan project yang sudah jalan",
                "Portfolio lebih cepat dibuat",
                "Wajib oleh hukum",
            ],
            "B",
            "Recruiter / client lihat portfolio karena bisa langsung verifikasi: 'Oh, dia memang bisa bikin yang dia klaim.'",
        ),
        q(
            "Apa minimum yang HARUS ada di setiap project di portfolio?",
            [
                "Cuma screenshot",
                "Problem statement, solution, tech stack, link demo live, link source GitHub",
                "Cuma source code",
                "Cuma demo",
            ],
            "B",
            "Konteks dan bukti. Tanpa problem statement, project terlihat seperti tutorial yang asal contek.",
        ),
        q(
            "Berapa project ideal di portfolio pemula?",
            [
                "10 lebih supaya kelihatan rajin",
                "3-4 project nyata yang berbeda fungsi, dengan kualitas yang tinggi",
                "1 saja",
                "0",
            ],
            "B",
            "Less is more. 3 project bagus dengan deploy hidup dan README jelas kalahkan 10 project medioker.",
        ),
        q(
            "Apa yang membuat tone portfolio terkesan profesional?",
            [
                "English yang ribet",
                "Bahasa Indonesia santai-profesional, spesifik, dan jujur — bukan jargon dan exaggerated",
                "Banyak emoji",
                "Caps lock",
            ],
            "B",
            "'Stunning user experiences' = generic. 'Bikin web yang dipakai user' = jujur dan langsung. Yang kedua lebih meyakinkan.",
        ),
        q(
            "Mana praktik yang HARUS dilakukan untuk setiap project di portfolio?",
            [
                "Tunggu sempurna baru deploy",
                "Deploy ke URL publik. Project di laptop = tidak ada untuk recruiter",
                "Cuma push ke GitHub",
                "Email file zip",
            ],
            "B",
            "Recruiter cek dalam 5 detik. Mereka tidak akan clone repo dan run lokal. URL hidup = project ada.",
        ),
    ],
    common_mistakes=[
        "Pajang 10 todo app yang mirip-mirip. Recruiter langsung tahu itu tutorial follower.",
        "Project tanpa link demo. Sama saja dengan project tidak ada.",
        "Portfolio kelihatan amatir karena spacing sempit dan terlalu banyak warna.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — GitHub Profile
# ─────────────────────────────────────────────────────────────────────────────

LESSON_GITHUB = make_lesson(
    title="GitHub Profile yang Menjual",
    slug="github-profile-yang-menarik",
    order_index=2,
    read_time="10 menit",
    summary="Profile README, pinned repos, dan README per project yang dibaca recruiter.",
    tools=["Akun GitHub", "Browser"],
    outcomes=[
        "Membuat profile README yang ramah pembaca",
        "Mengoptimasi pinned repos",
        "Menulis README per project yang menjelaskan apa, bagaimana, dan kenapa",
    ],
    tldr=(
        "GitHub adalah portfolio kedua kamu. Profile README untuk first "
        "impression. 6 pinned repos pilihan terbaik. Setiap repo wajib README "
        "yang jelas — itu yang dibaca duluan."
    ),
    pembuka=dedent(
        """\
        Banyak developer pemula salah kaprah: mereka pikir GitHub cuma tempat simpan kode.

        Kenyataan: GitHub adalah portfolio kedua kamu. Recruiter sering klik link GitHub kamu sebelum baca CV. Pertama yang mereka lihat: profile page kamu.

        Lesson ini cara mengubah profile GitHub kosong jadi profile yang ngomong: "Orang ini serius."
        """
    ),
    penjelasan=dedent(
        """\
        ### Profile README

        Buat repo dengan nama persis sama dengan username kamu. Misal username `acel`, repo `acel`.

        Tambah file `README.md`. Isi-nya akan otomatis muncul di profile page kamu.

        Format yang efektif:

        ```markdown
        # Halo, saya Acel

        Web developer pemula yang lagi bangun jalur karier dari Indonesia.
        Fokus saat ini: Next.js, React, dan deploy ke production.

        ## Lagi belajar
        - Next.js App Router
        - Database dengan Prisma + PostgreSQL
        - Auth dengan NextAuth

        ## Project yang sedang dibangun
        - [Habit Tracker](https://...) — web app harian dengan streak.
        - [Portfolio](https://...) — site personal pertama.

        ## Kontak
        - Email: saya@email.com
        - Twitter: [@username](https://twitter.com/username)
        ```

        Aturan: pendek, jelas, jujur. Hindari emoji berlebihan dan badge dekoratif yang tidak menambah info.

        ### Pinned repositories

        GitHub kasih kamu 6 slot pinned di profile. Itu real estate paling berharga.

        Pilih 6 yang terbaik:

        - 3-4 project portfolio yang sudah deploy.
        - 1-2 contribution publik (kalau ada) atau learning project yang menarik.

        Skip:

        - Repo template tutorial yang belum dimodifikasi.
        - Repo yang tidak ada README.
        - Project yang setengah jadi.

        ### README per project

        Setiap repo yang kamu pajang **wajib** punya README. Ini template minimum yang efektif:

        ```markdown
        # Nama Project

        Deskripsi satu kalimat tentang apa yang dipecahkan.

        ![screenshot](./screenshot.png)

        ## Live Demo
        [demo.vercel.app](https://demo.vercel.app)

        ## Tech Stack
        - Next.js 14 (App Router)
        - Tailwind CSS
        - Prisma + PostgreSQL
        - Vercel (deploy)

        ## Fitur
        - Login dengan Google
        - Tambah / edit / hapus task
        - Data tersimpan per user

        ## Cara jalankan di lokal
        ~~~bash
        git clone https://github.com/username/repo.git
        cd repo
        npm install
        npm run dev
        ~~~

        ## Lessons learned
        Saat bikin ini saya belajar tentang server vs client component
        di Next.js App Router. Jebakan paling besar adalah lupa tambah
        env variable di Vercel — halaman blank tanpa pesan.
        ```

        Notice screenshot di bagian atas. Itu yang dilihat duluan.

        ### Contribution graph

        Square hijau di profile menunjukkan aktivitas commit. Tidak harus penuh, tapi konsisten lebih baik daripada burst.

        Tips: commit tiap kali kamu beneran kerja, jangan force commit kosong cuma untuk graph. Recruiter tahu bedanya.

        ### Repo yang tidak perlu di-pajang

        - Tutorial follower yang persis sama (bisa dihapus atau di-archive).
        - Project setengah jadi tanpa README.
        - Repo yang isinya cuma file dummy.

        Hapus atau archive supaya profile kamu tidak terlihat berantakan.

        ### Bonus: contribution ke open source

        Kalau punya waktu, satu small contribution ke open source project menonjol di portfolio. Tidak harus besar:

        - Fix typo di docs.
        - Tambah tests.
        - Translate dokumentasi ke Indonesia.

        Cari issue dengan label `good first issue` di repo populer.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh structure profile README yang baik:

        ```markdown
        # Halo, saya Acel 👋

        Web developer pemula. Lagi membangun karier dari nol di Indonesia.

        - 🚀 Fokus: Next.js, TypeScript, Tailwind
        - 📚 Lagi belajar: Database, auth, deploy production
        - 💼 Portfolio: [acel.dev](https://acel.dev)

        ---

        ### Project yang lagi aktif

        🍵 **[Habit Tracker](https://habit-tracker.vercel.app)**
        Web app harian dengan check-in dan streak.
        `Next.js` `Prisma` `Supabase` `NextAuth`

        🎨 **[Portfolio](https://acel.dev)**
        Site personal yang dibangun dari nol.
        `Next.js` `Tailwind` `Vercel`

        ---

        ### Kontak

        - 📧 saya@email.com
        - 🐦 [@username](https://twitter.com/username)
        - 💼 [LinkedIn](https://linkedin.com/in/username)
        ```

        Pendek tapi padat. Recruiter dapat info yang dia butuhkan dalam 10 detik.
        """
    ),
    practice=(
        "Buat profile README untuk akun GitHub kamu (repo nama sama dengan "
        "username). Isi sesuai contoh di atas. Lalu pin 3-4 project terbaik "
        "yang sudah deploy. Setiap repo yang di-pin pastikan punya README "
        "minimal dengan deskripsi + link demo."
    ),
    fix_error={
        "language": "markdown",
        "broken_code": dedent(
            """\
            # username

            🚀🔥💯💻✨ Hi! I'm a passionate full-stack developer with
            10+ years of experience in cutting-edge technologies! 🌟

            ![](badge1.png) ![](badge2.png) ![](badge3.png) ![](badge4.png)
            ![](badge5.png) ![](badge6.png) ![](badge7.png) ![](badge8.png)

            ## Tech Stack
            HTML CSS JavaScript TypeScript React Next.js Vue Angular Svelte
            Node.js Express Fastify NestJS Go Rust Python Django Flask FastAPI
            MongoDB PostgreSQL MySQL Redis ElasticSearch Docker Kubernetes
            AWS GCP Azure Vercel Netlify Heroku Firebase Supabase

            ## Stats
            ![GitHub stats](badge.png)
            ![Languages](badge.png)
            ![Streaks](badge.png)
            """
        ),
        "hint": "Apa yang akan recruiter pikirkan saat lihat ini?",
        "answer_explanation": dedent(
            """\
            Kesalahan: profile ini terlihat tidak jujur dan over the top.

            Masalah:

            - "10+ years experience" untuk pemula = obvious lie.
            - List 30 teknologi tanpa konteks = tidak ada satu yang dikuasai.
            - Banyak emoji + badge dekoratif tanpa info.
            - Tidak ada link ke project nyata.

            Yang efektif: jujur tentang level kamu, fokus ke 3-5 teknologi yang benar-benar dikuasai, dan link ke project yang real.
            """
        ),
        "fixed_code": dedent(
            """\
            # Halo, saya [Nama]

            Web developer pemula dari Indonesia. Lagi belajar dan membangun
            project untuk pivot karier ke developer.

            ## Lagi fokus
            - Next.js (App Router)
            - TypeScript
            - Tailwind CSS

            ## Project yang aktif
            - [Habit Tracker](https://...) — Next.js + Prisma
            - [Portfolio](https://...) — Next.js + Tailwind

            ## Kontak
            - Email: saya@email.com
            - LinkedIn: [profil](https://...)
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi profile README di GitHub?",
            [
                "Tidak ada fungsi",
                "Muncul di profile page sebagai first impression — yang dilihat recruiter sebelum repo",
                "Dekorasi",
                "Wajib oleh GitHub",
            ],
            "B",
            "Profile README adalah real estate utama. Manfaatkan untuk perkenalan singkat dan link ke project terbaik.",
        ),
        q(
            "Berapa jumlah pinned repo yang OPTIMAL?",
            [
                "10",
                "6 (maksimum yang GitHub izinkan), pilih yang terbaik",
                "Pajang semua",
                "0",
            ],
            "B",
            "GitHub kasih 6 slot pinned. Pakai semua, isi dengan project terbaik dengan README dan deploy.",
        ),
        q(
            "Apa yang HARUS ada di README setiap repo yang dipajang?",
            [
                "Cuma judul",
                "Deskripsi singkat, screenshot, link demo, tech stack, dan cara run di lokal",
                "Cuma kode",
                "Tidak ada README",
            ],
            "B",
            "README adalah cover letter project. Tanpa itu, repo kamu cuma timbunan file.",
        ),
        q(
            "Mana praktik yang BURUK di profile GitHub?",
            [
                "List 30 teknologi tanpa konteks dan klaim '10+ years experience' padahal pemula",
                "Tulis 3 teknologi yang benar-benar dikuasai",
                "Pajang 3 project dengan README jelas",
                "Profile README pendek dan jujur",
            ],
            "A",
            "Klaim berlebihan langsung terdeteksi recruiter senior. Lebih efektif jujur tentang level + bukti project nyata.",
        ),
        q(
            "Apa yang sebaiknya dilakukan dengan repo tutorial follower yang dulu kamu bikin?",
            [
                "Pajang semua",
                "Hapus atau archive supaya profile tidak terlihat berantakan",
                "Pin",
                "Bikin trending",
            ],
            "B",
            "Profile yang berantakan dengan banyak repo medioker mengurangi sinyal. Bersihkan supaya yang berkualitas menonjol.",
        ),
    ],
    common_mistakes=[
        "Profile README dengan klaim berlebihan (`'10+ years experience'` padahal pemula).",
        "Pin repo yang README-nya kosong atau cuma judul.",
        "Pajang semua repo tutorial follower. Profile jadi noise.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Cari Project Pertama
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FREELANCE = make_lesson(
    title="Cari Project Pertama (Realistis)",
    slug="cari-project-pertama",
    order_index=3,
    read_time="13 menit",
    summary="Platform freelance, direct client, rate awal, dan strategi yang masuk akal.",
    tools=["Akun LinkedIn", "Twitter / X (opsional)", "Notes app"],
    outcomes=[
        "Memahami opsi cari project pertama: platform vs direct client",
        "Tahu cara menentukan rate yang masuk akal untuk pemula",
        "Punya strategi konkret untuk minggu pertama",
    ],
    tldr=(
        "Tiga jalan untuk project pertama: platform (Upwork/Fiverr), direct "
        "client (UMKM lokal/teman), atau internship. Direct paling cocok "
        "untuk pemula. Rate awal: cukup untuk dapat experience, bukan untuk "
        "kaya."
    ),
    pembuka=dedent(
        """\
        "Saya udah belajar 6 bulan. Project udah 3. Tapi gimana cara dapat klien pertama?"

        Ini pertanyaan yang banyak ditanya. Lesson ini jawaban realistis — bukan strategi guru-guru online yang janji "5 juta per minggu".

        Kabar baik dan buruk: jalan pertama selalu lebih lambat dari yang dibayangkan, tapi memang ada jalan yang masuk akal.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga jalan utama

        **1. Platform freelance** (Upwork, Fiverr, Freelancer.com)

        - **Plus**: marketplace dengan banyak client global. Pembayaran terjamin.
        - **Minus**: kompetisi sangat tinggi. Pemula sulit menonjol di antara expert. Komisi platform 10-20%.
        - **Cocok untuk**: kamu yang siap kompetitif dan punya kesabaran tinggi.

        **2. Direct client** (UMKM lokal, teman, network)

        - **Plus**: kompetisi rendah. Bisa kasih harga lebih tinggi karena value langsung. Bangun reputasi lokal.
        - **Minus**: butuh networking. Pembayaran kadang seret.
        - **Cocok untuk**: pemula. Direct client kasih experience dengan ramah hati.

        **3. Internship / part-time job**

        - **Plus**: belajar dari developer senior. Mentor, code review, struktur tim.
        - **Minus**: rate sering lebih rendah dari freelance.
        - **Cocok untuk**: kamu yang ingin jalur karier full-time.

        Rekomendasi untuk pemula: **direct client**. Cari UMKM atau teman yang butuh website / landing page sederhana. Kerja dengan harga reasonable, bangun referensi.

        ### Cara cari direct client pertama

        - **Network langsung.** Posting di LinkedIn, Facebook, Twitter: "Saya web developer pemula, lagi cari satu klien untuk project pertama. Bisa bantu UMKM lokal kalau ada yang butuh website sederhana." Spread the word.
        - **Pendekatan UMKM**. Lihat sekitar: warung, kedai kopi, klinik, salon. Banyak yang belum punya website. DM Instagram mereka, tawarkan harga ramah.
        - **Komunitas online**. Discord/Telegram developer Indonesia. Ada thread "siapa butuh apa". Jangan cuma promote diri, ikut diskusi dulu.
        - **Cold email**. Email bisnis kecil dengan portfolio kamu. Conversion rate rendah, tapi 1 dari 50 bisa convert.

        ### Rate untuk pemula

        Pertanyaan paling umum: "Berapa harga yang masuk akal?"

        Realistis untuk pemula Indonesia, project landing page satu halaman:

        - **Range bottom**: Rp 500rb - Rp 1.5jt. Ini untuk teman atau UMKM yang baru kenal kamu.
        - **Range middle**: Rp 1.5jt - Rp 3jt. Untuk client yang lihat portfolio dan trust kamu.
        - **Range top**: Rp 3jt - Rp 5jt. Untuk client yang butuh fitur custom (CMS, multi-page, integrasi).

        Project yang lebih kompleks (web app dengan auth + database) mulai dari Rp 5jt - Rp 15jt.

        Aturan jempol: **3 project pertama, prioritaskan experience dan testimonial, bukan profit**. Dari project ke-4 mulai naikin rate.

        ### Cara nolak project yang tidak masuk akal

        Kamu akan dapat tawaran macam:

        - "Bikin Tokopedia tapi gratis, nanti saya kasih saham."
        - "Bikinkan website lengkap, deadline 2 hari."
        - "Saya cuma punya budget Rp 200rb."

        Tolak dengan sopan. Reputasi kamu lebih penting daripada satu project bermasalah.

        Template tolakan halus:

        > "Terima kasih atas kepercayaannya. Sayangnya scope project ini di luar yang bisa saya selesaikan dengan kualitas yang baik di rate dan timeline tersebut. Semoga sukses dengan project-nya."

        ### Apa yang client butuh dari kamu

        Selain hasil akhir:

        - **Komunikasi**. Update progress reguler, walau tidak ditanya.
        - **Pertanyaan yang tepat**. Sebelum mulai, klarifikasi scope, deadline, jumlah revisi. Jangan tebak.
        - **Demo cepat**. Deploy versi awal dalam 2-3 hari. Client lihat progress = trust naik.
        - **Dokumen handover**. Setelah selesai, kasih dokumen: cara update content, login admin, kontak support kamu.

        Banyak developer fokus ke kode dan lupa soft skill ini. Mereka yang bisa keduanya jauh lebih dihargai.

        ### Strategi minggu pertama

        Minggu 1 setelah portfolio kamu live:

        - Hari 1: Update LinkedIn dan tulis post: "Saya available untuk project freelance web development. Berikut portfolio saya: [URL]."
        - Hari 2-3: Cari 5-10 UMKM lokal yang website-nya bisa diperbaiki atau belum punya. Catat kontak mereka.
        - Hari 4: Kirim DM atau email ke mereka. Pendekatan ramah, tawarkan harga reasonable.
        - Hari 5-7: Follow up. Sambil itu, kontribusi di komunitas (jawab pertanyaan pemula di Discord, dll).

        Jangan harapkan respons cepat. Lanjutkan rutinitas ini setiap minggu.
        """
    ),
    contoh_code_md=dedent(
        """\
        Template DM ke calon client UMKM:

        ```text
        Halo [Nama],

        Saya [Nama]. Saya web developer yang sedang membangun portfolio.
        Lihat usaha [Nama Usaha] di [platform]. Keren!

        Saya perhatikan [Nama Usaha] belum punya website / website-nya
        bisa dipoles. Saya available untuk bantu bikin landing page
        sederhana yang bisa menampilkan menu, jam buka, dan kontak.

        Saya pakai teknologi modern (Next.js + Tailwind) dengan
        deploy ke domain yang fast loading. Bisa selesai 5-7 hari.

        Untuk pricing, saya tawarkan rate ramah karena ini salah satu
        project pertama saya. Range Rp 800rb - Rp 1.5jt tergantung
        scope.

        Mau ngobrol singkat untuk diskusi kebutuhan?

        Portfolio saya: [URL]

        Terima kasih,
        [Nama]
        ```

        Tidak salesy, tidak desperate. Spesifik, jujur, dan kasih opsi
        diskusi tanpa tekanan.
        """
    ),
    practice=(
        "Tulis di catatan: 5 nama UMKM atau bisnis kecil di sekitar kamu "
        "yang website-nya belum optimal atau tidak ada. Cari kontak mereka "
        "(Instagram DM atau email). Jangan kirim dulu — siapkan template "
        "pendekatan dulu, dan minta feedback ke teman developer kamu sebelum "
        "kirim."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            DM ke calon client:

            "BIKIN WEBSITE MURAH MERIAH! 100% PUAS!
            Cuma Rp 50.000! BURUAN BANG INI HARGA KHUSUS HARI INI!
            Bayar dulu baru kerja!"
            """
        ),
        "hint": "Apa yang akan calon client pikirkan saat baca DM ini?",
        "answer_explanation": dedent(
            """\
            Kesalahan: terlalu sales-y, terlalu murah, terlalu tidak profesional. Pesan ini akan langsung di-block atau di-ignore.

            Sinyal merah:

            - Caps lock dan banyak tanda seru = scam vibe.
            - Harga tidak realistis = tidak ada developer serius yang bekerja segitu.
            - "Bayar dulu baru kerja" = red flag. Standar industri: 50% di awal, 50% di akhir.
            - Tidak ada portfolio atau bukti.

            Yang benar: tone profesional, harga realistis, link portfolio, opsi diskusi tanpa tekanan.
            """
        ),
        "fixed_code": dedent(
            """\
            DM yang lebih efektif:

            "Halo, saya [Nama], web developer pemula dari Jogja. Saya
            perhatikan [Nama Usaha] belum punya website. Saya tawarkan
            bantuan bikin landing page sederhana — menu, kontak, lokasi.

            Range pricing: Rp 800rb - Rp 1.5jt, tergantung scope.
            Pembayaran 50% di awal, 50% setelah live di internet.
            Selesai 5-7 hari kerja.

            Portfolio saya: [URL]

            Mau ngobrol singkat untuk lihat kebutuhan?"
            """
        ),
    },
    quiz=[
        q(
            "Mana jalan paling COCOK untuk dapat project pertama bagi pemula?",
            [
                "Platform global seperti Upwork (kompetisi expert)",
                "Direct client lokal (UMKM, teman, network) dengan harga ramah",
                "Tunggu recruiter datang sendiri",
                "Pasang iklan Google Ads",
            ],
            "B",
            "Direct client kompetisi lebih rendah dan client lebih ramah ke pemula. Platform global lebih cocok setelah punya reputasi.",
        ),
        q(
            "Range pricing yang REALISTIS untuk landing page satu halaman dari pemula Indonesia?",
            [
                "Rp 50rb",
                "Rp 800rb - Rp 1.5jt untuk client baru, naik bertahap setelah punya 3-4 project",
                "Rp 50jt",
                "Gratis selalu",
            ],
            "B",
            "Range ini realistis, kasih kamu experience tanpa eksploitasi. Naikin rate setelah portfolio kuat.",
        ),
        q(
            "Apa yang BUKAN red flag dari calon client?",
            [
                "Tawaran 'bayar nanti, sekarang kerja dulu'",
                "Klien bayar 50% di awal, 50% di akhir",
                "Scope berubah tiap hari tanpa kompensasi",
                "Budget tidak masuk akal seperti Rp 100rb untuk web app full",
            ],
            "B",
            "50/50 split adalah standar industri. Sisanya = red flag yang harus kamu hindari.",
        ),
        q(
            "Apa yang HARUS dilakukan SEBELUM mulai project?",
            [
                "Langsung coding",
                "Klarifikasi scope, deadline, jumlah revisi, dan harga dengan client",
                "Cuma terima brief lisan",
                "Cuma percayai client",
            ],
            "B",
            "Scope yang jelas di awal mencegah konflik di akhir. Tulis hitam di atas putih (dokumen kontrak ringkas).",
        ),
        q(
            "Apa strategi yang TEPAT untuk minggu pertama setelah portfolio live?",
            [
                "Tunggu klien datang sendiri",
                "Update LinkedIn, cari 5-10 UMKM lokal, DM dengan template profesional, follow up dengan sabar",
                "Spam ke 1000 orang",
                "Bayar iklan",
            ],
            "B",
            "Outreach proaktif tapi terstruktur. Volume rendah dengan kualitas tinggi kalahkan spam.",
        ),
    ],
    common_mistakes=[
        "Pasang harga terlalu rendah (Rp 50rb-Rp 200rb) — terlihat tidak profesional dan eksploitatif diri sendiri.",
        "Tidak klarifikasi scope. Project terus-menerus expand tanpa kompensasi.",
        "Skip kontrak / dokumen tertulis. Saat konflik, tidak ada referensi.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_FINAL = make_lesson(
    title="Mini Project — Portfolio Final yang Production-Ready",
    slug="mini-project-portfolio-final",
    order_index=4,
    read_time="240 menit",
    summary="Polish portfolio jadi production-quality, siap dikirim ke recruiter atau client.",
    tools=["Next.js + Tailwind", "GitHub", "Vercel", "Custom domain (opsional)"],
    outcomes=[
        "Portfolio dengan minimum 3 case study lengkap",
        "Performance Lighthouse score > 80",
        "Custom domain (atau subdomain Vercel yang clean)",
        "Contact form atau link kontak yang berfungsi",
    ],
    tldr=(
        "Ini bukan portfolio latihan. Ini portfolio yang akan kamu kirim "
        "ke recruiter dan client sebenarnya. Setiap detail penting: "
        "case study, performance, custom domain, kontak yang berfungsi."
    ),
    pembuka=dedent(
        """\
        Ini project final dari roadmap Frontend. Kalau kamu sudah sampai sini dan menyelesaikan setiap level — kamu sudah punya skill dasar yang dibutuhkan untuk apply junior developer atau cari freelance.

        Project ini rangkum semuanya. Bukan latihan. Hasilnya akan jadi business card kamu untuk satu tahun ke depan.

        Treat seperti project untuk klien sebenarnya. Karena itu yang akan kamu lakukan setelah ini.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind + (opsional) shadcn/ui. Tanpa backend kompleks (kecuali kalau mau tambah blog).

        Halaman:

        - `/` — Hero, About, Featured Projects (3 case study), Skills, CTA contact.
        - `/projects` — Semua project (4-6 item) dengan filter tag.
        - `/projects/[slug]` — Detail per project dengan case study lengkap.
        - `/about` (opsional) — Cerita lebih panjang tentang kamu.
        - `/contact` (opsional) — Form atau link langsung.

        ### Case study format (per project)

        Tiap project di `/projects/[slug]` punya konten:

        - **Hero image** — screenshot kerja.
        - **Title + tagline** — nama project + satu kalimat.
        - **Tech stack** — badge dengan teknologi yang dipakai.
        - **Problem** — apa yang dipecahkan? Untuk siapa?
        - **Solution** — pendekatan kamu. Fitur utama.
        - **Process** — cara kamu kerja. Challenge yang dihadapi.
        - **Result** — hasil akhir. Live demo + source link.
        - **Lessons learned** — apa yang dipelajari.

        Format ini menunjukkan kamu **berpikir** sebelum koding. Itu yang membedakan junior dengan pemula.

        ### Polish checklist

        Detail kecil yang menentukan profesional vs amatir:

        - **Performance**. Lighthouse score (Performance + Accessibility) > 80. Cek di DevTools → Lighthouse.
        - **Image optimization**. Pakai `next/image` untuk semua gambar. Auto-resize + lazy load.
        - **Typography**. Plus Jakarta Sans, Inter, atau Geist. Hierarchy jelas.
        - **Color discipline**. 1 accent + grayscale.
        - **Spacing**. Section `py-24` minimum. Generous, bukan pelit.
        - **Mobile**. Tested di HP nyata, bukan cuma simulator.
        - **Loading state**. `loading.tsx` di halaman yang fetch data.
        - **404 page**. Custom `not-found.tsx` yang ramah.
        - **OG image**. Buat preview saat di-share di sosmed.
        - **Favicon**. Yang menarik, bukan default Next.js.

        ### Contact yang berfungsi

        Pilih satu:

        - **Direct link** ke email + LinkedIn + GitHub. Paling sederhana.
        - **Contact form** dengan service seperti Formspree / Resend / EmailJS.

        Jangan pasang form yang rusak. Lebih baik link langsung.

        ### Custom domain

        Opsional tapi nice. URL `acel.dev` atau `acel.codes` lebih impressive dari `acel.vercel.app`.

        Cara:

        - Beli domain di Niagahoster (Indonesia) atau Namecheap (luar). Range Rp 150rb-Rp 300rb/tahun.
        - Vercel: Project → Settings → Domains → Add. Ikuti instruksi DNS.
        - Tunggu 5-30 menit, domain aktif dengan SSL.

        ### Final review checklist

        Sebelum bilang "selesai":

        - [ ] Buka di HP teman dari koneksi internet berbeda.
        - [ ] Cek di Chrome, Firefox, Safari (kalau bisa).
        - [ ] Run Lighthouse, score > 80.
        - [ ] Klik setiap link, pastikan tidak ada 404.
        - [ ] Test contact (kirim email ke diri sendiri lewat form, kalau pakai).
        - [ ] Share URL ke 3 teman dengan profesi berbeda. Tanya kesan pertama.
        - [ ] Update sesuai feedback paling tajam.

        Setelah pass semua, kamu siap kirim portfolio ini ke recruiter atau client.

        ### Submit

        Salin URL final + repo GitHub. Update pinned di GitHub. Pasang link di:

        - LinkedIn headline.
        - Twitter / X bio.
        - Email signature.
        - WhatsApp bio.

        Gunakan portfolio ini untuk semua interaksi profesional kamu sebagai developer.
        """
    ),
    contoh_code_md=dedent(
        """\
        Pola data project yang scalable:

        ```ts
        // src/data/projects.ts
        export type Project = {
          slug: string;
          title: string;
          tagline: string;
          summary: string;
          coverImage: string;
          techStack: string[];
          tags: string[];
          problem: string;
          solution: string;
          process: string;
          result: string;
          lessons: string;
          demoUrl: string;
          sourceUrl: string;
          year: string;
          featured: boolean;
        };

        export const projects: Project[] = [
          {
            slug: "habit-tracker",
            title: "Habit Tracker",
            tagline: "Web app untuk konsistensi rutinitas harian",
            summary: "...",
            coverImage: "/projects/habit-tracker.png",
            techStack: ["Next.js", "Prisma", "Supabase", "NextAuth"],
            tags: ["fullstack", "saas"],
            problem: "Pelajar SMA susah konsisten...",
            solution: "Web app dengan check-in harian dan streak counter...",
            process: "Mulai dari mockup di Figma...",
            result: "Live di habit-tracker.acel.dev. 50+ user beta.",
            lessons: "Belajar tentang server vs client component...",
            demoUrl: "https://habit-tracker.acel.dev",
            sourceUrl: "https://github.com/username/habit-tracker",
            year: "2026",
            featured: true,
          },
          // ... 4-5 project lain
        ];
        ```

        Dengan data terstruktur seperti ini, halaman list dan detail tinggal map.
        """
    ),
    practice=(
        "Bangun portfolio final sesuai spec. Total waktu sekitar 12-20 jam, "
        "pecah jadi 1-2 minggu. Setelah selesai, run final review checklist. "
        "Update URL portfolio di LinkedIn, Twitter, dan email signature. "
        "Mulai outreach ke client / recruiter."
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            "Saya udah bikin portfolio. Live di Vercel. Tapi belum ada
            project di sana — masih placeholder 'Coming soon'. Kapan
            boleh kirim ke recruiter?"
            """
        ),
        "hint": "Kira-kira recruiter mikir apa kalau mereka klik portfolio dan lihat 'Coming soon'?",
        "answer_explanation": dedent(
            """\
            Jangan kirim portfolio yang masih placeholder. Recruiter akan bookmark sebagai "follower yang belum siap" dan jarang klik lagi.

            Aturan: portfolio kamu harus 100% siap saat dikirim.

            - Minimum 3 project nyata dengan case study lengkap.
            - Live demo yang bisa dibuka.
            - Source code di GitHub dengan README yang jelas.
            - Performance dan responsive sudah di-check.

            Kalau belum, tunda outreach. Selesaikan dulu portfolio. First impression cuma dapat sekali.
            """
        ),
        "fixed_code": dedent(
            """\
            Sebelum apply / outreach, pastikan:

            ✓ Portfolio live di URL publik
            ✓ Minimum 3 case study lengkap
            ✓ Setiap project punya demo + source link
            ✓ Tidak ada placeholder "Coming soon"
            ✓ Lighthouse score > 80
            ✓ Mobile-tested
            ✓ Sudah dapat feedback dari minimal 3 orang

            Setelah semua ✓, baru kirim.
            """
        ),
    },
    quiz=[
        q(
            "Apa minimum yang HARUS ada di portfolio production-ready?",
            [
                "1 project saja",
                "Minimum 3 case study lengkap dengan demo + source, performance score > 80, contact yang berfungsi",
                "Cuma hero section",
                "Banyak animasi",
            ],
            "B",
            "Portfolio production-ready bukan portfolio latihan. Setiap detail penting karena ini dikirim ke audience nyata.",
        ),
        q(
            "Kenapa case study format (problem → solution → process → result) PENTING?",
            [
                "Tidak penting",
                "Menunjukkan kamu BERPIKIR sebelum coding — itu yang membedakan junior siap kerja dengan tutorial follower",
                "Cuma estetika",
                "Wajib oleh hukum",
            ],
            "B",
            "Recruiter cari orang yang bisa pecahkan masalah, bukan cuma copy-paste. Case study = bukti kamu bisa.",
        ),
        q(
            "Apa yang TIDAK BOLEH ada di portfolio yang akan dikirim ke recruiter?",
            [
                "Project nyata dengan demo",
                "Placeholder 'Coming soon' atau halaman 'Under construction'",
                "Custom domain",
                "Case study lengkap",
            ],
            "B",
            "First impression cuma dapat sekali. Portfolio dengan placeholder = sinyal 'belum siap'.",
        ),
        q(
            "Berapa target Lighthouse score yang DIREKOMENDASIKAN?",
            [
                "Tidak penting",
                "Performance + Accessibility > 80, idealnya 90+",
                "0",
                "Harus 100",
            ],
            "B",
            "Recruiter senior sering cek Lighthouse. Score rendah = sinyal kamu belum aware dengan optimization.",
        ),
        q(
            "Setelah portfolio final selesai, apa langkah berikutnya?",
            [
                "Tunggu klien datang sendiri",
                "Update URL di LinkedIn, Twitter, email signature, dan mulai outreach ke recruiter atau client",
                "Buang portfolio",
                "Tidak melakukan apa-apa",
            ],
            "B",
            "Portfolio yang tidak di-share = portfolio yang tidak ada. Aktif promosikan setelah selesai.",
        ),
    ],
    common_mistakes=[
        "Kirim portfolio dengan 'Coming soon'. Recruiter coret langsung.",
        "Lupa cek di HP. Halaman berantakan di mobile = first impression rusak.",
        "Pasang contact form yang rusak. Kalau ragu, pakai link email langsung.",
    ],
    xp_reward=700,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=5,
    slug="career-freelance",
    title="Career & Freelance",
    subtitle="Dari belajar ke berpenghasilan",
    description=(
        "Cara membangun portfolio yang dipercaya, GitHub profile yang menjual, "
        "dan strategi konkret untuk dapat project pertama. Tutup roadmap "
        "Frontend dengan portfolio production-ready yang siap dikirim."
    ),
    duration="~2 minggu",
    difficulty="Lanjutan",
    accent_color="from-rose-400/30 to-violet-500/10",
    mini_project="Portfolio Final Production-Ready",
    tags=["Portfolio", "GitHub", "Freelance", "Career"],
    lessons=[
        LESSON_PORTFOLIO,
        LESSON_GITHUB,
        LESSON_FREELANCE,
        PROJECT_FINAL,
    ],
)
