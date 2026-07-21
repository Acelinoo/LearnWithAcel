import { Monitor, Smartphone, Shield, Database } from "lucide-react";

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
        slug: "full-stack-developer",
        name: "Full-Stack Developer",
        description: "Menguasai frontend dan backend, mampu membangun aplikasi web utuh sendirian.",
        tasks: ["Frontend", "Backend", "DevOps Dasar"],
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
        tasks: ["Kotlin", "Android Studio", "UI Mobile"],
      },
      {
        slug: "ios-developer",
        name: "iOS Developer",
        description: "Membangun aplikasi native eksklusif untuk ekosistem Apple (iPhone, iPad).",
        tasks: ["Swift", "Xcode", "Standar Apple"],
      },
      {
        slug: "cross-platform-developer",
        name: "Cross-Platform Developer",
        description: "Membangun aplikasi mobile yang bisa berjalan di Android maupun iOS dengan satu basis kode.",
        tasks: ["Flutter", "React Native", "Optimasi"],
      },
    ],
  },
  {
    id: "cyber",
    title: "Cybersecurity & Network",
    icon: Shield,
    description: "Amankan sistem dan kelola infrastruktur jaringan.",
    roles: [
      {
        slug: "penetration-tester",
        name: "Penetration Tester",
        description: "Hacker etis yang bertugas mencari celah keamanan sistem sebelum diretas pihak jahat.",
        tasks: ["Uji Penetrasi", "Laporan Kerentanan", "Kali Linux"],
      },
      {
        slug: "network-engineer",
        name: "Network Engineer",
        description: "Merancang, mengimplementasikan, dan mengelola jaringan komputer.",
        tasks: ["Routing", "Switching", "TCP/IP"],
      },
    ],
  },
  {
    id: "data",
    title: "Data & AI",
    icon: Database,
    description: "Olah data dan kembangkan model kecerdasan buatan.",
    roles: [
      {
        slug: "data-scientist",
        name: "Data Analyst / Scientist",
        description: "Menganalisis data dalam jumlah besar untuk menemukan pola dan insight bisnis.",
        tasks: ["Python", "SQL", "Visualisasi Data"],
      },
      {
        slug: "machine-learning-engineer",
        name: "Machine Learning Engineer",
        description: "Mengembangkan model kecerdasan buatan (AI) yang dapat belajar dari data.",
        tasks: ["TensorFlow", "PyTorch", "Optimasi AI"],
      },
    ],
  },
];
