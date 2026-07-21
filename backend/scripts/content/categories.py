"""
Category definitions based on v1.0.0 roles.
"""

import json

CATEGORIES = [
    # WEB DEVELOPMENT
    {
        "name": "Frontend Developer",
        "slug": "frontend-developer",
        "available": True,
        "role": "Frontend Developer",
        "side": "Web Development",
        "description": "Fokus pada antarmuka pengguna (UI/UX) dan pengalaman interaktif di browser web.",
        "tasks": "Membuat layout web, animasi, dan integrasi dengan API backend.",
        "techs": json.dumps([
            {"label": "Dasar", "items": ["HTML", "CSS", "JavaScript"]},
            {"label": "Framework", "items": ["React", "Vue", "Next.js", "Tailwind"]},
        ]),
    },
    {
        "name": "Backend Developer",
        "slug": "backend-developer",
        "available": True,
        "role": "Backend Developer",
        "side": "Web Development",
        "description": "Membangun sistem di balik layar yang memproses data, database, dan logika bisnis.",
        "tasks": "Membuat API, mengelola database, dan memastikan keamanan server.",
        "techs": json.dumps([
            {"label": "Bahasa", "items": ["Node.js", "Python", "Go", "Java"]},
            {"label": "Database", "items": ["PostgreSQL", "MongoDB", "Redis"]},
        ]),
    },
    {
        "name": "Full-Stack Developer",
        "slug": "full-stack-developer",
        "available": True,
        "role": "Full-Stack Developer",
        "side": "Web Development",
        "description": "Menguasai frontend dan backend, mampu membangun aplikasi web utuh sendirian.",
        "tasks": "Merancang arsitektur aplikasi end-to-end, dari database hingga UI.",
        "techs": json.dumps([
            {"label": "Stack Populer", "items": ["MERN (MongoDB, Express, React, Node)", "T3 Stack"]},
        ]),
    },
    # MOBILE DEVELOPMENT
    {
        "name": "Android Developer",
        "slug": "android-developer",
        "available": True,
        "role": "Android Developer",
        "side": "Mobile Development",
        "description": "Membangun aplikasi native khusus untuk sistem operasi Android.",
        "tasks": "Mengembangkan UI mobile, integrasi API, dan publikasi ke Play Store.",
        "techs": json.dumps([
            {"label": "Bahasa", "items": ["Kotlin", "Java"]},
            {"label": "Tools", "items": ["Android Studio", "Jetpack Compose"]},
        ]),
    },
    {
        "name": "iOS Developer",
        "slug": "ios-developer",
        "available": True,
        "role": "iOS Developer",
        "side": "Mobile Development",
        "description": "Membangun aplikasi native eksklusif untuk ekosistem Apple (iPhone, iPad).",
        "tasks": "Desain UI sesuai standar Apple, publikasi ke App Store.",
        "techs": json.dumps([
            {"label": "Bahasa", "items": ["Swift", "Objective-C"]},
            {"label": "Tools", "items": ["Xcode", "SwiftUI"]},
        ]),
    },
    {
        "name": "Cross-Platform Developer",
        "slug": "cross-platform-developer",
        "available": True,
        "role": "Cross-Platform Developer",
        "side": "Mobile Development",
        "description": "Membangun aplikasi mobile yang bisa berjalan di Android maupun iOS dengan satu basis kode.",
        "tasks": "Optimasi performa aplikasi di berbagai OS, integrasi fitur native.",
        "techs": json.dumps([
            {"label": "Framework", "items": ["Flutter (Dart)", "React Native (JS)"]},
        ]),
    },
    # CYBERSECURITY & NETWORK
    {
        "name": "Penetration Tester",
        "slug": "penetration-tester",
        "available": True,
        "role": "Penetration Tester",
        "side": "Cybersecurity & Network",
        "description": "Hacker etis yang bertugas mencari celah keamanan sistem sebelum diretas pihak jahat.",
        "tasks": "Melakukan uji penetrasi, menyusun laporan kerentanan, dan merekomendasikan solusi.",
        "techs": json.dumps([
            {"label": "Tools", "items": ["Kali Linux", "Metasploit", "Burp Suite", "Wireshark"]},
        ]),
    },
    {
        "name": "Network Engineer",
        "slug": "network-engineer",
        "available": True,
        "role": "Network Engineer",
        "side": "Cybersecurity & Network",
        "description": "Merancang, mengimplementasikan, dan mengelola jaringan komputer.",
        "tasks": "Konfigurasi router/switch, memastikan konektivitas jaringan, troubleshooting masalah jaringan.",
        "techs": json.dumps([
            {"label": "Keahlian", "items": ["Cisco", "TCP/IP", "Routing", "Switching"]},
        ]),
    },
    # DATA & AI
    {
        "name": "Data Analyst / Scientist",
        "slug": "data-scientist",
        "available": True,
        "role": "Data Scientist",
        "side": "Data & AI",
        "description": "Menganalisis data dalam jumlah besar untuk menemukan pola dan insight bisnis.",
        "tasks": "Membersihkan data, membuat visualisasi, memprediksi tren masa depan.",
        "techs": json.dumps([
            {"label": "Bahasa & Tools", "items": ["Python", "SQL", "Pandas", "Tableau"]},
        ]),
    },
    {
        "name": "Machine Learning Engineer",
        "slug": "machine-learning-engineer",
        "available": True,
        "role": "Machine Learning Engineer",
        "side": "Data & AI",
        "description": "Mengembangkan model kecerdasan buatan (AI) yang dapat belajar dari data.",
        "tasks": "Melatih model AI, optimasi performa model, dan deployment AI ke production.",
        "techs": json.dumps([
            {"label": "Framework", "items": ["TensorFlow", "PyTorch", "Scikit-Learn"]},
        ]),
    }
]
