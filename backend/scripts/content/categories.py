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
            {"label": "Framework", "items": ["React", "Next.js", "Tailwind"]},
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
            {"label": "Bahasa", "items": ["Node.js", "Python"]},
            {"label": "Database", "items": ["PostgreSQL", "MongoDB"]},
        ]),
    },
    {
        "name": "Fullstack Developer",
        "slug": "fullstack-developer",
        "available": True,
        "role": "Fullstack Developer",
        "side": "Web Development",
        "description": "Menguasai frontend dan backend, mampu membangun aplikasi web utuh sendirian.",
        "tasks": "Merancang arsitektur aplikasi end-to-end, dari database hingga UI.",
        "techs": json.dumps([
            {"label": "Stack Populer", "items": ["PERN", "MERN", "T3 Stack"]},
        ]),
    },
    # CYBERSECURITY
    {
        "name": "Penetration Tester",
        "slug": "penetration-tester",
        "available": True,
        "role": "Penetration Tester",
        "side": "Cybersecurity",
        "description": "Hacker etis yang bertugas mencari celah keamanan sistem sebelum diretas pihak jahat.",
        "tasks": "Melakukan uji penetrasi, menyusun laporan kerentanan, dan merekomendasikan solusi.",
        "techs": json.dumps([
            {"label": "Tools", "items": ["Kali Linux", "Burp Suite", "Metasploit"]},
        ]),
    },
    {
        "name": "SOC Analyst",
        "slug": "soc-analyst",
        "available": True,
        "role": "SOC Analyst",
        "side": "Cybersecurity",
        "description": "Menganalisis log dan mendeteksi ancaman secara real-time di jaringan.",
        "tasks": "Memantau lalu lintas jaringan, identifikasi anomali, dan menangani insiden siber.",
        "techs": json.dumps([
            {"label": "Tools", "items": ["Splunk", "Wazuh", "Wireshark"]},
        ]),
    },
    {
        "name": "Security Engineer",
        "slug": "security-engineer",
        "available": True,
        "role": "Security Engineer",
        "side": "Cybersecurity",
        "description": "Merancang dan membangun arsitektur keamanan untuk sistem perusahaan.",
        "tasks": "Implementasi firewall, VPN, IAM, dan menjaga keamanan arsitektur cloud.",
        "techs": json.dumps([
            {"label": "Skills", "items": ["Firewalls", "IDS/IPS", "Cloud Security"]},
        ]),
    },
    {
        "name": "Malware Analyst",
        "slug": "malware-analyst",
        "available": True,
        "role": "Malware Analyst",
        "side": "Cybersecurity",
        "description": "Menganalisis dan membedah perangkat lunak berbahaya untuk memahami cara kerjanya.",
        "tasks": "Reverse engineering, analisis statis dan dinamis pada virus/ransomware.",
        "techs": json.dumps([
            {"label": "Tools", "items": ["Ghidra", "IDA Pro", "C/Assembly"]},
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
            {"label": "Bahasa & Tools", "items": ["Kotlin", "Android Studio"]},
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
            {"label": "Bahasa & Tools", "items": ["Swift", "Xcode", "SwiftUI"]},
        ]),
    },
    {
        "name": "Flutter Developer",
        "slug": "flutter-developer",
        "available": True,
        "role": "Flutter Developer",
        "side": "Mobile Development",
        "description": "Membangun aplikasi mobile yang bisa berjalan di Android maupun iOS dengan satu basis kode.",
        "tasks": "Optimasi performa aplikasi di berbagai OS, integrasi fitur native.",
        "techs": json.dumps([
            {"label": "Framework", "items": ["Flutter", "Dart"]},
        ]),
    }
]
