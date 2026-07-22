"use client";

import { Monitor, Smartphone, Shield } from "lucide-react";

export const ROLE_CATEGORIES = [
  {
    id: "web",
    title: "Web Development",
    icon: Monitor,
    description: "Bangun website dan aplikasi web modern yang interaktif.",
    roles: [
      {
        slug: "frontend-developer",
        name: "Frontend Developer",
        description: "Fokus pada antarmuka pengguna (UI/UX) dan pengalaman interaktif di browser web.",
        tasks: ["HTML/CSS/JS", "React", "Next.js"],
      },
      {
        slug: "backend-developer",
        name: "Backend Developer",
        description: "Membangun sistem di balik layar yang memproses data, database, dan logika bisnis.",
        tasks: ["Node.js", "Python", "Database"],
      },
      {
        slug: "fullstack-developer",
        name: "Fullstack Developer",
        description: "Menguasai frontend dan backend, mampu membangun aplikasi web utuh sendirian.",
        tasks: ["Frontend", "Backend", "Integration"],
      },
    ],
  },
  {
    id: "cyber",
    title: "Cybersecurity & Security",
    icon: Shield,
    description: "Amankan sistem, tangani insiden siber, dan uji celah keamanan.",
    roles: [
      {
        slug: "penetration-tester",
        name: "Penetration Tester",
        description: "Hacker etis yang bertugas mencari celah keamanan sistem sebelum diretas pihak jahat.",
        tasks: ["Uji Penetrasi", "OWASP Top 10", "Burp Suite"],
      },
      {
        slug: "soc-analyst",
        name: "SOC Analyst",
        description: "Menganalisis log dan mendeteksi ancaman secara real-time di jaringan.",
        tasks: ["SIEM", "Wireshark", "Log Analysis"],
      },
      {
        slug: "security-engineer",
        name: "Security Engineer",
        description: "Merancang dan membangun arsitektur keamanan untuk sistem perusahaan.",
        tasks: ["Firewall", "IDS/IPS", "Cloud Security"],
      },
      {
        slug: "malware-analyst",
        name: "Malware Analyst",
        description: "Menganalisis dan membedah perangkat lunak berbahaya untuk memahami cara kerjanya.",
        tasks: ["Bahasa C", "Assembly", "Ghidra / IDA"],
      },
    ],
  },
  {
    id: "mobile",
    title: "Mobile Development",
    icon: Smartphone,
    description: "Buat aplikasi native dan cross-platform untuk smartphone.",
    roles: [
      {
        slug: "android-developer",
        name: "Android Developer",
        description: "Membangun aplikasi native khusus untuk sistem operasi Android.",
        tasks: ["Kotlin", "Android Studio", "Compose"],
      },
      {
        slug: "ios-developer",
        name: "iOS Developer",
        description: "Membangun aplikasi native eksklusif untuk ekosistem Apple (iPhone, iPad).",
        tasks: ["Swift", "SwiftUI", "Xcode"],
      },
      {
        slug: "flutter-developer",
        name: "Flutter Developer",
        description: "Membangun aplikasi mobile yang bisa berjalan di Android maupun iOS dengan satu basis kode.",
        tasks: ["Dart", "Flutter UI", "State Management"],
      },
    ],
  },
];
