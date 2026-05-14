"""
Database seed script.

Migrates static data from the frontend JS files into PostgreSQL via Prisma.
Run with:  python -m scripts.seed

This script is idempotent — it uses upsert so it can be run multiple times safely.
"""

import asyncio
import json
import sys
from pathlib import Path

# Allow running from the backend/ directory
sys.path.insert(0, str(Path(__file__).parent.parent))

from prisma import Prisma

# ── Static data (mirrors src/lib/roadmap.js & vibeRoadmap.js) ────────────────

CATEGORIES = [
    {
        "name": "Frontend",
        "slug": "frontend",
        "available": True,
        "role": "Front-End Developer",
        "side": "Sisi Klien / Client-Side",
        "description": (
            "Front-End Developer bertanggung jawab atas apa yang dilihat, diklik, "
            "dan berinteraksi langsung dengan pengguna di browser. Mereka mengubah "
            "desain visual menjadi kode yang interaktif."
        ),
        "tasks": (
            "Membuat struktur web, mengatur tata letak (layout), animasi, "
            "responsivitas di berbagai perangkat (HP/Laptop), dan memastikan "
            "performa loading halaman yang cepat."
        ),
        "techs": json.dumps([
            {"label": "Dasar", "items": ["HTML", "CSS", "JavaScript"]},
            {"label": "Framework/Library", "items": ["React.js", "Next.js", "Vue.js", "Angular", "Tailwind CSS"]},
        ]),
    },
    {
        "name": "Backend",
        "slug": "backend",
        "available": False,
        "role": "Back-End Developer",
        "side": "Sisi Server / Server-Side",
        "description": (
            "Back-End Developer bertanggung jawab atas logika di balik layar, server, "
            "keamanan, dan bagaimana data disimpan serta dikirim."
        ),
        "tasks": (
            "Membuat API, mengelola database, mengurus autentikasi pengguna, "
            "dan mengoptimalkan performa server."
        ),
        "techs": json.dumps([
            {"label": "Bahasa", "items": ["Node.js", "Python", "Java", "PHP", "Go"]},
            {"label": "Database & ORM", "items": ["PostgreSQL", "MySQL", "MongoDB", "Prisma", "Eloquent"]},
        ]),
    },
    {
        "name": "Fullstack",
        "slug": "fullstack",
        "available": False,
        "role": "Full-Stack Developer",
        "side": "Menyeluruh",
        "description": (
            "Full-Stack Developer adalah generalist yang menguasai kedua sisi, "
            "baik Front-End maupun Back-End."
        ),
        "tasks": (
            "Menghubungkan tampilan depan dengan logika belakang, merancang arsitektur "
            "aplikasi secara keseluruhan."
        ),
        "techs": json.dumps([
            {"label": "Stack populer", "items": [
                "MERN (MongoDB, Express, React, Node.js)",
                "T3 (Next.js, Prisma, Tailwind, TypeScript)",
            ]},
        ]),
    },
    {
        "name": "Vibe Coding",
        "slug": "vibe",
        "available": True,
        "role": "AI Builder / Indie Developer",
        "side": "AI-Assisted Development",
        "description": (
            "Jalur Vibe Coding mengajarkan cara membangun aplikasi nyata menggunakan "
            "AI sebagai asisten coding. Cocok untuk yang ingin build cepat tanpa "
            "harus hafal semua syntax."
        ),
        "tasks": (
            "Prompting AI, generate UI, debugging dengan AI, deploy ke internet, "
            "dan membangun produk dari ide sampai live."
        ),
        "techs": json.dumps([
            {"label": "AI Tools", "items": ["Cursor", "ChatGPT", "Claude", "V0", "Bolt"]},
            {"label": "Stack", "items": ["React", "Next.js", "Tailwind", "Supabase", "Vercel"]},
        ]),
    },
]

FRONTEND_LEVELS = [
    {
        "number": 1,
        "slug": "html-css",
        "title": "HTML & CSS",
        "subtitle": "Fondasi sebuah halaman web",
        "description": "Pahami struktur HTML semantik dan gaya dengan CSS modern. Kamu akan belajar layout, flexbox, grid, dan responsive design dari nol.",
        "duration": "2 minggu",
        "difficulty": "Pemula",
        "accent_color": "from-violet-500/30 to-fuchsia-500/10",
        "mini_project": "Landing page pribadi",
        "quiz_count": 3,
        "base_viewers": 4281,
        "tags": json.dumps(["HTML5", "CSS3", "Flexbox", "Grid", "Responsive"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "mengenal-html",
                "title": "Mengenal HTML",
                "summary": "Struktur dasar halaman web dan tag yang sering dipakai.",
                "content": "# Mengenal HTML\n\nHTML adalah singkatan dari HyperText Markup Language...",
                "duration": "8 menit",
                "base_viewers": 3128,
                "order_index": 1,
            },
            {
                "slug": "css-fundamental",
                "title": "CSS Fundamental",
                "summary": "Selector, specificity, dan cara menata tampilan.",
                "content": "# CSS Fundamental\n\nKalau HTML adalah kerangka, CSS adalah cat dan dekorasinya...",
                "duration": "12 menit",
                "base_viewers": 2745,
                "order_index": 2,
            },
            {
                "slug": "flexbox-grid",
                "title": "Flexbox & Grid Modern",
                "summary": "Membangun layout yang rapi dan responsif.",
                "content": "# Flexbox & Grid Modern\n\nDua sistem layout paling penting di CSS hari ini...",
                "duration": "15 menit",
                "base_viewers": 2103,
                "order_index": 3,
            },
        ],
    },
    {
        "number": 2,
        "slug": "javascript",
        "title": "JavaScript",
        "subtitle": "Menghidupkan halaman web",
        "description": "Dari variable dan function hingga DOM, event, dan async. Kamu akan mulai membuat halaman yang interaktif.",
        "duration": "3 minggu",
        "difficulty": "Pemula - Menengah",
        "accent_color": "from-amber-400/30 to-violet-500/10",
        "mini_project": "Todo list interaktif",
        "quiz_count": 4,
        "base_viewers": 3127,
        "tags": json.dumps(["ES6+", "DOM", "Fetch API", "Async"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "dasar-javascript",
                "title": "Dasar JavaScript",
                "summary": "Variable, type, operator, dan control flow.",
                "content": "# Dasar JavaScript\n\nJavaScript adalah bahasa yang bikin halaman web hidup...",
                "duration": "14 menit",
                "base_viewers": 2456,
                "order_index": 1,
            },
            {
                "slug": "function-dan-scope",
                "title": "Function & Scope",
                "summary": "Cara kerja closure dan scope di JavaScript.",
                "content": "# Function & Scope\n\nFunction adalah blok kode yang bisa dipanggil berulang kali...",
                "duration": "12 menit",
                "base_viewers": 1892,
                "order_index": 2,
            },
            {
                "slug": "dom-manipulation",
                "title": "DOM Manipulation",
                "summary": "Mengubah isi halaman secara dinamis.",
                "content": "# DOM Manipulation\n\nDOM (Document Object Model) adalah representasi halaman web sebagai objek...",
                "duration": "16 menit",
                "base_viewers": 1634,
                "order_index": 3,
            },
        ],
    },
    {
        "number": 3,
        "slug": "react-tailwind",
        "title": "React & Tailwind",
        "subtitle": "UI modern yang scalable",
        "description": "Bangun UI berbasis komponen dengan React dan percantik dengan Tailwind.",
        "duration": "4 minggu",
        "difficulty": "Menengah",
        "accent_color": "from-cyan-400/30 to-violet-500/10",
        "mini_project": "Dashboard admin mini",
        "quiz_count": 5,
        "base_viewers": 2043,
        "tags": json.dumps(["React", "Hooks", "Tailwind", "Component"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "pengenalan-react",
                "title": "Pengenalan React",
                "summary": "Komponen, props, dan cara berpikir React.",
                "content": "# Pengenalan React\n\nReact adalah library JavaScript untuk membangun UI berbasis komponen...",
                "duration": "18 menit",
                "base_viewers": 1287,
                "order_index": 1,
            },
            {
                "slug": "state-dan-hooks",
                "title": "State & Hooks",
                "summary": "useState, useEffect, dan pola umum hooks.",
                "content": "# State & Hooks\n\nState adalah data yang bisa berubah dan mempengaruhi tampilan...",
                "duration": "20 menit",
                "base_viewers": 1054,
                "order_index": 2,
            },
        ],
    },
    {
        "number": 4,
        "slug": "real-project",
        "title": "Real Project",
        "subtitle": "Build seperti developer beneran",
        "description": "Saatnya membangun project nyata dengan best practice industri.",
        "duration": "4 minggu",
        "difficulty": "Menengah",
        "accent_color": "from-emerald-400/30 to-violet-500/10",
        "mini_project": "Clone landing page SaaS",
        "quiz_count": 2,
        "base_viewers": 1256,
        "tags": json.dumps(["Project", "Next.js", "Deployment"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "struktur-project-modern",
                "title": "Struktur Project Modern",
                "summary": "Folder, konvensi, dan clean code.",
                "content": "# Struktur Project Modern\n\nProject yang terstruktur baik lebih mudah di-maintain...",
                "duration": "10 menit",
                "base_viewers": 892,
                "order_index": 1,
            },
        ],
    },
    {
        "number": 5,
        "slug": "career-freelance",
        "title": "Career & Freelance",
        "subtitle": "Dari belajar ke berpenghasilan",
        "description": "Siapkan portfolio, CV, GitHub, dan cara mencari project freelance pertama.",
        "duration": "2 minggu",
        "difficulty": "Lanjutan",
        "accent_color": "from-rose-400/30 to-violet-500/10",
        "mini_project": "Portfolio website + studi kasus",
        "quiz_count": 1,
        "base_viewers": 892,
        "tags": json.dumps(["Portfolio", "CV", "Freelance", "Career"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "membangun-portfolio",
                "title": "Membangun Portfolio",
                "summary": "Apa yang harus ditampilkan untuk menarik klien.",
                "content": "# Membangun Portfolio\n\nPortfolio adalah kartu nama digital seorang developer...",
                "duration": "12 menit",
                "base_viewers": 734,
                "order_index": 1,
            },
        ],
    },
]

VIBE_LEVELS = [
    {
        "number": 0,
        "slug": "mindset-orientation",
        "title": "Mindset & Orientation",
        "subtitle": "Pahami dunia AI coding sebelum mulai",
        "description": "Sebelum menyentuh tools, kamu perlu paham: apa itu vibe coding, bagaimana AI coding bekerja, apa yang realistis dan apa yang tidak.",
        "duration": "3 hari",
        "difficulty": "Pemula",
        "accent_color": "from-violet-500/30 to-fuchsia-500/10",
        "mini_project": "Mapping tools & workflow pribadi",
        "quiz_count": 3,
        "base_viewers": 2841,
        "tags": json.dumps(["AI", "Mindset", "Workflow", "Tools"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "apa-itu-ai-development",
                "title": "Apa Itu AI-Assisted Development",
                "summary": "Memahami cara kerja AI dalam membantu coding.",
                "content": "# Apa Itu AI-Assisted Development\n\nAI-assisted development artinya kamu membangun aplikasi dengan bantuan AI...",
                "duration": "6 menit",
                "base_viewers": 2103,
                "order_index": 1,
            },
            {
                "slug": "perbedaan-nocode-aicode",
                "title": "No-Code vs Low-Code vs AI Coding vs Manual",
                "summary": "Kapan pakai yang mana.",
                "content": "# No-Code vs Low-Code vs AI Coding vs Manual\n\nAda banyak cara bikin app...",
                "duration": "8 menit",
                "base_viewers": 1892,
                "order_index": 2,
            },
            {
                "slug": "workflow-modern-developer",
                "title": "Workflow Modern Developer",
                "summary": "Alur kerja developer 2025 yang realistis.",
                "content": "# Workflow Modern Developer 2025\n\nDeveloper 2025 tidak mulai dari blank file...",
                "duration": "7 menit",
                "base_viewers": 1756,
                "order_index": 3,
            },
            {
                "slug": "tools-ecosystem",
                "title": "Tools Ecosystem Overview",
                "summary": "Cursor, ChatGPT, Claude, Bolt, Lovable, V0, GitHub, Vercel, Supabase.",
                "content": "# Tools Ecosystem Overview\n\nTools AI development bisa dibagi jadi beberapa kategori...",
                "duration": "10 menit",
                "base_viewers": 2045,
                "order_index": 4,
            },
        ],
    },
    {
        "number": 1,
        "slug": "first-app",
        "title": "First App Experience",
        "subtitle": "Rasakan: 'Saya bisa bikin app'",
        "description": "Install tools, tulis prompt pertama, generate landing page, edit hasilnya, dan deploy ke internet.",
        "duration": "1 minggu",
        "difficulty": "Pemula",
        "accent_color": "from-emerald-400/30 to-violet-500/10",
        "mini_project": "Landing page sederhana (live di internet)",
        "quiz_count": 3,
        "base_viewers": 3127,
        "tags": json.dumps(["Setup", "Prompt", "Deploy", "Vercel"]),
        "coming_soon": False,
        "lessons": [
            {
                "slug": "install-tools",
                "title": "Install Tools",
                "summary": "Setup Cursor, GitHub, dan Vercel.",
                "content": "# Install Tools\n\nLangkah pertama: install semua tools yang kamu butuhkan...",
                "duration": "10 menit",
                "base_viewers": 2456,
                "order_index": 1,
            },
            {
                "slug": "github-basics",
                "title": "GitHub Basics",
                "summary": "Buat repo, push, dan kolaborasi dasar.",
                "content": "# GitHub Basics\n\nGitHub adalah tempat menyimpan kode online...",
                "duration": "8 menit",
                "base_viewers": 1987,
                "order_index": 2,
            },
            {
                "slug": "prompt-basics",
                "title": "Prompt Basics",
                "summary": "Cara menulis prompt yang menghasilkan kode bagus.",
                "content": "# Prompt Basics\n\nPrompt yang baik adalah kunci mendapatkan kode yang bagus dari AI...",
                "duration": "12 menit",
                "base_viewers": 2234,
                "order_index": 3,
            },
            {
                "slug": "generate-landing-page",
                "title": "Generate Landing Page",
                "summary": "Bikin halaman pertama pakai AI.",
                "content": "# Generate Landing Page\n\nSaatnya bikin halaman pertamamu dengan AI...",
                "duration": "15 menit",
                "base_viewers": 2678,
                "order_index": 4,
            },
            {
                "slug": "edit-hasil-ai",
                "title": "Edit Hasil AI",
                "summary": "Cara memperbaiki dan menyesuaikan output AI.",
                "content": "# Edit Hasil AI\n\nAI menghasilkan kode yang bagus, tapi selalu perlu disesuaikan...",
                "duration": "10 menit",
                "base_viewers": 1845,
                "order_index": 5,
            },
            {
                "slug": "deploy-website",
                "title": "Deploy Website",
                "summary": "Publish ke internet lewat Vercel.",
                "content": "# Deploy Website\n\nSaatnya publish website kamu ke internet...",
                "duration": "8 menit",
                "base_viewers": 2123,
                "order_index": 6,
            },
        ],
    },
]


async def seed():
    db = Prisma()
    await db.connect()

    print("🌱 Starting database seed...")

    # ── Categories ────────────────────────────────────────────────────────────
    for cat_data in CATEGORIES:
        category = await db.category.upsert(
            where={"slug": cat_data["slug"]},
            data={
                "create": cat_data,
                "update": {k: v for k, v in cat_data.items() if k != "slug"},
            },
        )
        print(f"  ✓ Category: {category.name}")

        # ── Levels for this category ──────────────────────────────────────────
        levels_data = []
        if cat_data["slug"] == "frontend":
            levels_data = FRONTEND_LEVELS
        elif cat_data["slug"] == "vibe":
            levels_data = VIBE_LEVELS

        for level_data in levels_data:
            lessons_data = level_data.pop("lessons", [])

            level = await db.level.upsert(
                where={"category_id_slug": {
                    "category_id": category.id,
                    "slug": level_data["slug"],
                }},
                data={
                    "create": {**level_data, "category_id": category.id},
                    "update": {k: v for k, v in level_data.items() if k != "slug"},
                },
            )
            print(f"    ✓ Level {level.number}: {level.title}")

            for lesson_data in lessons_data:
                lesson = await db.lesson.upsert(
                    where={"level_id_slug": {
                        "level_id": level.id,
                        "slug": lesson_data["slug"],
                    }},
                    data={
                        "create": {**lesson_data, "level_id": level.id},
                        "update": {k: v for k, v in lesson_data.items() if k != "slug"},
                    },
                )
                print(f"      ✓ Lesson: {lesson.title}")

            # Restore lessons list for potential re-use
            level_data["lessons"] = lessons_data

    await db.disconnect()
    print("\n✅ Seed completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed())
