import {
  Code2,
  Chrome,
  Package,
  Github,
  Terminal,
  Database,
  Smartphone,
  Shield,
  Search,
  BrainCircuit,
  Laptop,
  Cpu
} from "lucide-react";

export const rolePreparationData = {
  "frontend-developer": {
    title: "Frontend Developer",
    icon: Code2,
    description: "Pembuat antarmuka website yang dilihat oleh pengguna.",
    skills: ["HTML & CSS", "JavaScript", "React / Next.js", "Tailwind CSS"],
    essentials: [
      { name: "Visual Studio Code", tag: "Code editor", desc: "Tempat menulis kode. Ringan, gratis, dan paling banyak dipakai.", link: "https://code.visualstudio.com", size: "~90 MB", icon: Code2, tone: "from-accent/30 to-accent-hover/10", must: true },
      { name: "Google Chrome", tag: "Browser + DevTools", desc: "Untuk membuka website buatanmu dan cek error.", link: "https://www.google.com/chrome", size: "~100 MB", icon: Chrome, tone: "from-cyan-400/30 to-sky-500/10", must: true },
      { name: "Node.js (LTS)", tag: "Runtime + npm", desc: "Dibutuhkan untuk menjalankan React atau Next.js.", link: "https://nodejs.org", size: "~30 MB", icon: Package, tone: "from-emerald-400/30 to-sky-500/10", must: true },
      { name: "Git + GitHub", tag: "Version control", desc: "Untuk menyimpan kode dan portfolio online.", link: "https://git-scm.com", size: "~40 MB", icon: Github, tone: "from-rose-400/30 to-sky-500/10", must: false }
    ],
    extensions: [
      { name: "Live Server", desc: "Auto-refresh halaman saat kamu save file." },
      { name: "Prettier", desc: "Rapikan kode otomatis saat save." },
      { name: "Tailwind CSS IntelliSense", desc: "Autocomplete class Tailwind." },
      { name: "ES7+ React/Redux snippets", desc: "Auto-generate komponen React." }
    ]
  },
  "backend-developer": {
    title: "Backend Developer",
    icon: Database,
    description: "Arsitek di balik layar yang mengurus server, database, dan logika bisnis.",
    skills: ["Node.js / Python", "Database (SQL)", "API Development", "Authentication"],
    essentials: [
      { name: "Visual Studio Code", tag: "Code editor", desc: "Code editor utama untuk menulis logika backend.", link: "https://code.visualstudio.com", size: "~90 MB", icon: Code2, tone: "from-accent/30 to-accent-hover/10", must: true },
      { name: "Postman / Insomnia", tag: "API Client", desc: "Alat wajib untuk mengetes endpoint API yang kamu buat.", link: "https://www.postman.com/", size: "~150 MB", icon: Terminal, tone: "from-orange-400/30 to-red-500/10", must: true },
      { name: "Node.js / Python", tag: "Runtime", desc: "Environment untuk menjalankan kode backendmu.", link: "https://nodejs.org", size: "~30 MB", icon: Package, tone: "from-emerald-400/30 to-sky-500/10", must: true }
    ],
    extensions: [
      { name: "REST Client", desc: "Untuk testing API langsung di VS Code." },
      { name: "Prettier", desc: "Merakit kode otomatis." },
      { name: "DotENV", desc: "Highlight syntax .env file." }
    ]
  },
  "fullstack-developer": {
    title: "Fullstack Developer",
    icon: Laptop,
    description: "Bisa membuat Frontend sekaligus merancang Backend. Jack of all trades.",
    skills: ["Frontend Skills", "Backend Skills", "System Architecture", "Deployment"],
    essentials: [
      { name: "Visual Studio Code", tag: "Code editor", desc: "Satu editor untuk semua kebutuhanmu.", link: "https://code.visualstudio.com", size: "~90 MB", icon: Code2, tone: "from-accent/30 to-accent-hover/10", must: true },
      { name: "Node.js (LTS)", tag: "Runtime", desc: "Standar industri untuk fullstack JS.", link: "https://nodejs.org", size: "~30 MB", icon: Package, tone: "from-emerald-400/30 to-sky-500/10", must: true },
      { name: "Docker", tag: "Container", desc: "Sangat membantu untuk virtualisasi server.", link: "https://www.docker.com/", size: "~600 MB", icon: Cpu, tone: "from-blue-400/30 to-blue-500/10", must: false }
    ],
    extensions: [
      { name: "Prettier", desc: "Merakit kode otomatis." },
      { name: "Tailwind CSS IntelliSense", desc: "Autocomplete kelas styling." },
      { name: "Prisma", desc: "Bantuan ORM untuk database." }
    ]
  },
  "penetration-tester": {
    title: "Penetration Tester",
    icon: Shield,
    description: "Hacker beretika yang mencari celah keamanan untuk diperbaiki.",
    skills: ["Web Exploitation", "Network Hacking", "Cryptography", "Privilege Escalation"],
    essentials: [
      { name: "Kali Linux", tag: "OS Wajib", desc: "Sistem operasi standar untuk hacking.", link: "https://www.kali.org/", size: "3+ GB", icon: Terminal, tone: "from-blue-400/30 to-sky-500/10", must: true },
      { name: "Burp Suite", tag: "Web Proxy", desc: "Tool utama untuk web application testing.", link: "https://portswigger.net/burp", size: "~200 MB", icon: Shield, tone: "from-orange-400/30 to-red-500/10", must: true },
      { name: "OpenVPN", tag: "VPN Client", desc: "Untuk connect ke lab HackTheBox / TryHackMe.", link: "https://openvpn.net/", size: "~50 MB", icon: Search, tone: "from-emerald-400/30 to-green-500/10", must: true }
    ],
    extensions: [
      { name: "Python", desc: "Dukungan scripting eksploitasi." },
      { name: "Bash IDE", desc: "Untuk nulis shell scripts." }
    ]
  },
  "android-developer": {
    title: "Android Developer",
    icon: Smartphone,
    description: "Pembuat aplikasi native untuk ekosistem Android.",
    skills: ["Kotlin / Java", "Android Studio", "Jetpack Compose", "API Integration"],
    essentials: [
      { name: "Android Studio", tag: "IDE Wajib", desc: "Tool resmi untuk membuat aplikasi Android.", link: "https://developer.android.com/studio", size: "1+ GB", icon: Code2, tone: "from-emerald-400/30 to-green-500/10", must: true },
      { name: "Android Device / Emulator", tag: "Testing", desc: "HP Android asli atau Emulator.", link: "", size: "-", icon: Smartphone, tone: "from-cyan-400/30 to-sky-500/10", must: true },
      { name: "Git", tag: "Version control", desc: "Untuk backup dan kolaborasi kode.", link: "https://git-scm.com", size: "~40 MB", icon: Github, tone: "from-rose-400/30 to-red-500/10", must: false }
    ],
    extensions: [
      { name: "Kotlin", desc: "Bantuan syntax Kotlin." },
      { name: "Android XML", desc: "Preview XML UI." }
    ]
  },
};

export const defaultPreparationData = rolePreparationData["frontend-developer"];
