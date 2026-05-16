"""
Category definitions.
"""

import json

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
        "available": True,
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
        "available": True,
        "role": "Full-Stack Developer",
        "side": "Menyeluruh / End-to-End",
        "description": (
            "Full-Stack Developer adalah generalist yang menguasai kedua sisi, "
            "baik Front-End maupun Back-End, lalu menggabungkannya jadi aplikasi utuh."
        ),
        "tasks": (
            "Menghubungkan tampilan depan dengan logika belakang, merancang arsitektur "
            "aplikasi secara keseluruhan, dan men-deploy ke production."
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
            "harus hafal semua syntax — tapi tetap paham apa yang dibangun."
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
