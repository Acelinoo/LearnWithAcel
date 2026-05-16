// Central data source for the learning roadmap.
// Since the platform has no login, user progress is replaced with viewer counts.

export const categories = [
  {
    id: "frontend",
    label: "Frontend",
    available: true,
    role: "Front-End Developer",
    side: "Sisi Klien / Client-Side",
    description:
      "Front-End Developer bertanggung jawab atas apa yang dilihat, diklik, dan berinteraksi langsung dengan pengguna di browser. Mereka mengubah desain visual menjadi kode yang interaktif.",
    tasks:
      "Membuat struktur web, mengatur tata letak (layout), animasi, responsivitas di berbagai perangkat (HP/Laptop), dan memastikan performa loading halaman yang cepat.",
    techs: [
      { label: "Dasar", items: ["HTML", "CSS", "JavaScript"] },
      { label: "Framework/Library", items: ["React.js", "Next.js", "Vue.js", "Angular", "Tailwind CSS"] },
    ],
  },
  {
    id: "backend",
    label: "Backend",
    available: false,
    role: "Back-End Developer",
    side: "Sisi Server / Server-Side",
    description:
      "Back-End Developer bertanggung jawab atas logika di balik layar, server, keamanan, dan bagaimana data disimpan serta dikirim. Pengguna tidak bisa melihat bagian ini, tetapi tanpanya, web tidak akan bisa berfungsi (misalnya: proses login, transaksi, atau menyimpan data).",
    tasks:
      "Membuat API (Application Programming Interface), mengelola database, mengurus autentikasi pengguna (keamanan), dan mengoptimalkan performa server.",
    techs: [
      { label: "Bahasa", items: ["Node.js", "Python", "Java", "PHP", "Go"] },
      { label: "Database & ORM", items: ["PostgreSQL", "MySQL", "MongoDB", "Prisma", "Eloquent"] },
    ],
  },
  {
    id: "fullstack",
    label: "Fullstack",
    available: false,
    role: "Full-Stack Developer",
    side: "Menyeluruh",
    description:
      "Full-Stack Developer adalah generalist yang menguasai kedua sisi, baik Front-End maupun Back-End. Mereka bisa membangun seluruh aplikasi web dari nol, mulai dari tampilan hingga sistem database-nya.",
    tasks:
      "Menghubungkan tampilan depan dengan logika belakang, merancang arsitektur aplikasi secara keseluruhan, dan sering kali menjadi jembatan komunikasi antar tim.",
    techs: [
      { label: "Stack populer", items: ["MERN (MongoDB, Express, React, Node.js)", "T3 (Next.js, Prisma, Tailwind, TypeScript)"] },
    ],
  },
];

export const levels = [
  {
    id: "level-1",
    number: 1,
    slug: "html-css",
    category: "frontend",
    title: "HTML & CSS",
    subtitle: "Fondasi sebuah halaman web",
    description:
      "Pahami struktur HTML semantik dan gaya dengan CSS modern. Kamu akan belajar layout, flexbox, grid, dan responsive design dari nol.",
    duration: "2 minggu",
    difficulty: "Pemula",
    viewers: 4281,
    lessonsCount: 12,
    miniProject: "Landing page pribadi",
    quizCount: 3,
    accent: "from-violet-500/30 to-fuchsia-500/10",
    tags: ["HTML5", "CSS3", "Flexbox", "Grid", "Responsive"],
    lessons: [
      {
        slug: "mengenal-html",
        title: "Mengenal HTML",
        summary: "Struktur dasar halaman web dan tag yang sering dipakai.",
        duration: "8 menit",
        viewers: 3128,
      },
      {
        slug: "css-fundamental",
        title: "CSS Fundamental",
        summary: "Selector, specificity, dan cara menata tampilan.",
        duration: "12 menit",
        viewers: 2745,
      },
      {
        slug: "flexbox-grid",
        title: "Flexbox & Grid Modern",
        summary: "Membangun layout yang rapi dan responsif.",
        duration: "15 menit",
        viewers: 2103,
      },
    ],
  },
  {
    id: "level-2",
    number: 2,
    slug: "javascript",
    category: "frontend",
    title: "JavaScript",
    subtitle: "Menghidupkan halaman web",
    description:
      "Dari variable dan function hingga DOM, event, dan async. Kamu akan mulai membuat halaman yang interaktif dan bereaksi terhadap user.",
    duration: "3 minggu",
    difficulty: "Pemula - Menengah",
    viewers: 3127,
    lessonsCount: 18,
    miniProject: "Todo list interaktif",
    quizCount: 4,
    accent: "from-amber-400/30 to-violet-500/10",
    tags: ["ES6+", "DOM", "Fetch API", "Async"],
    lessons: [
      {
        slug: "dasar-javascript",
        title: "Dasar JavaScript",
        summary: "Variable, type, operator, dan control flow.",
        duration: "14 menit",
        viewers: 2456,
      },
      {
        slug: "function-dan-scope",
        title: "Function & Scope",
        summary: "Cara kerja closure dan scope di JavaScript.",
        duration: "12 menit",
        viewers: 1892,
      },
      {
        slug: "dom-manipulation",
        title: "DOM Manipulation",
        summary: "Mengubah isi halaman secara dinamis.",
        duration: "16 menit",
        viewers: 1634,
      },
    ],
  },
  {
    id: "level-3",
    number: 3,
    slug: "react-tailwind",
    category: "frontend",
    title: "React & Tailwind",
    subtitle: "UI modern yang scalable",
    description:
      "Bangun UI berbasis komponen dengan React dan percantik dengan Tailwind. Belajar hooks, state, dan pola component yang rapi.",
    duration: "4 minggu",
    difficulty: "Menengah",
    viewers: 2043,
    lessonsCount: 22,
    miniProject: "Dashboard admin mini",
    quizCount: 5,
    accent: "from-cyan-400/30 to-violet-500/10",
    tags: ["React", "Hooks", "Tailwind", "Component"],
    lessons: [
      {
        slug: "pengenalan-react",
        title: "Pengenalan React",
        summary: "Komponen, props, dan cara berpikir React.",
        duration: "18 menit",
        viewers: 1287,
      },
      {
        slug: "state-dan-hooks",
        title: "State & Hooks",
        summary: "useState, useEffect, dan pola umum hooks.",
        duration: "20 menit",
        viewers: 1054,
      },
    ],
  },
  {
    id: "level-4",
    number: 4,
    slug: "real-project",
    category: "frontend",
    title: "Real Project",
    subtitle: "Build seperti developer beneran",
    description:
      "Saatnya membangun project nyata: landing page startup, blog modern, dan dashboard SaaS sederhana dengan best practice industri.",
    duration: "4 minggu",
    difficulty: "Menengah",
    viewers: 1256,
    lessonsCount: 10,
    miniProject: "Clone landing page SaaS",
    quizCount: 2,
    accent: "from-emerald-400/30 to-violet-500/10",
    tags: ["Project", "Next.js", "Deployment"],
    lessons: [
      {
        slug: "struktur-project-modern",
        title: "Struktur Project Modern",
        summary: "Folder, konvensi, dan clean code.",
        duration: "10 menit",
        viewers: 892,
      },
    ],
  },
  {
    id: "level-5",
    number: 5,
    slug: "career-freelance",
    category: "frontend",
    title: "Career & Freelance",
    subtitle: "Dari belajar ke berpenghasilan",
    description:
      "Siapkan portfolio, CV, GitHub, dan cara mencari project freelance pertama. Termasuk tips interview dan komunikasi dengan klien.",
    duration: "2 minggu",
    difficulty: "Lanjutan",
    viewers: 892,
    lessonsCount: 8,
    miniProject: "Portfolio website + studi kasus",
    quizCount: 1,
    accent: "from-rose-400/30 to-violet-500/10",
    tags: ["Portfolio", "CV", "Freelance", "Career"],
    lessons: [
      {
        slug: "membangun-portfolio",
        title: "Membangun Portfolio",
        summary: "Apa yang harus ditampilkan untuk menarik klien.",
        duration: "12 menit",
        viewers: 734,
      },
    ],
  },
];

// Backend levels (coming soon)
export const backendLevels = [
  {
    id: "be-level-1",
    number: 1,
    slug: "node-fundamentals",
    category: "backend",
    title: "Node.js Fundamentals",
    subtitle: "Server-side JavaScript",
    description:
      "Pelajari dasar Node.js, module system, file system, dan cara membangun server pertamamu.",
    duration: "3 minggu",
    difficulty: "Pemula",
    viewers: 0,
    lessonsCount: 14,
    miniProject: "REST API sederhana",
    quizCount: 3,
    accent: "from-green-500/30 to-emerald-500/10",
    tags: ["Node.js", "Express", "REST API", "NPM"],
    lessons: [],
    comingSoon: true,
  },
  {
    id: "be-level-2",
    number: 2,
    slug: "database",
    category: "backend",
    title: "Database & ORM",
    subtitle: "Menyimpan dan mengelola data",
    description:
      "Belajar SQL, NoSQL, dan ORM populer. Dari desain schema hingga query yang efisien.",
    duration: "3 minggu",
    difficulty: "Pemula - Menengah",
    viewers: 0,
    lessonsCount: 12,
    miniProject: "CRUD app dengan database",
    quizCount: 3,
    accent: "from-blue-500/30 to-cyan-500/10",
    tags: ["PostgreSQL", "MongoDB", "Prisma", "SQL"],
    lessons: [],
    comingSoon: true,
  },
  {
    id: "be-level-3",
    number: 3,
    slug: "auth-security",
    category: "backend",
    title: "Auth & Security",
    subtitle: "Keamanan aplikasi web",
    description:
      "Implementasi authentication, authorization, JWT, OAuth, dan best practice keamanan.",
    duration: "2 minggu",
    difficulty: "Menengah",
    viewers: 0,
    lessonsCount: 10,
    miniProject: "Login system lengkap",
    quizCount: 2,
    accent: "from-red-500/30 to-orange-500/10",
    tags: ["JWT", "OAuth", "Bcrypt", "Security"],
    lessons: [],
    comingSoon: true,
  },
  {
    id: "be-level-4",
    number: 4,
    slug: "deployment-devops",
    category: "backend",
    title: "Deployment & DevOps",
    subtitle: "Dari lokal ke production",
    description:
      "Deploy aplikasi ke cloud, CI/CD pipeline, Docker dasar, dan monitoring.",
    duration: "2 minggu",
    difficulty: "Menengah - Lanjutan",
    viewers: 0,
    lessonsCount: 8,
    miniProject: "Full-stack app deployed",
    quizCount: 2,
    accent: "from-purple-500/30 to-indigo-500/10",
    tags: ["Docker", "CI/CD", "Vercel", "AWS"],
    lessons: [],
    comingSoon: true,
  },
];

// Fullstack levels (coming soon)
export const fullstackLevels = [
  {
    id: "fs-level-1",
    number: 1,
    slug: "fullstack-fundamentals",
    category: "fullstack",
    title: "Fullstack Fundamentals",
    subtitle: "Menghubungkan frontend dan backend",
    description:
      "Pahami arsitektur fullstack, bagaimana frontend berkomunikasi dengan backend melalui API, dan cara berpikir end-to-end.",
    duration: "2 minggu",
    difficulty: "Menengah",
    viewers: 0,
    lessonsCount: 10,
    miniProject: "Fullstack todo app",
    quizCount: 3,
    accent: "from-indigo-500/30 to-violet-500/10",
    tags: ["API Integration", "Fullstack", "Architecture"],
    lessons: [],
    comingSoon: true,
  },
  {
    id: "fs-level-2",
    number: 2,
    slug: "nextjs-fullstack",
    category: "fullstack",
    title: "Next.js Fullstack",
    subtitle: "Framework fullstack modern",
    description:
      "Bangun aplikasi fullstack dengan Next.js — server actions, API routes, database integration, dan deployment dalam satu framework.",
    duration: "4 minggu",
    difficulty: "Menengah",
    viewers: 0,
    lessonsCount: 16,
    miniProject: "SaaS app sederhana",
    quizCount: 4,
    accent: "from-slate-400/30 to-indigo-500/10",
    tags: ["Next.js", "Server Actions", "Prisma", "Vercel"],
    lessons: [],
    comingSoon: true,
  },
  {
    id: "fs-level-3",
    number: 3,
    slug: "testing-optimization",
    category: "fullstack",
    title: "Testing & Optimization",
    subtitle: "Kualitas dan performa",
    description:
      "Unit testing, integration testing, performance optimization, caching, dan monitoring untuk aplikasi fullstack production-ready.",
    duration: "3 minggu",
    difficulty: "Lanjutan",
    viewers: 0,
    lessonsCount: 12,
    miniProject: "Production-ready app",
    quizCount: 3,
    accent: "from-teal-500/30 to-cyan-500/10",
    tags: ["Jest", "Cypress", "Performance", "Caching"],
    lessons: [],
    comingSoon: true,
  },
];

export const frontendLevels = levels.filter((l) => l.category === "frontend");

export function getLevelBySlug(slug) {
  return levels.find((l) => l.slug === slug);
}

export function getLessonBySlug(levelSlug, lessonSlug) {
  const level = getLevelBySlug(levelSlug);
  if (!level) return null;
  const lesson = level.lessons.find((l) => l.slug === lessonSlug);
  return lesson ? { level, lesson } : null;
}

// Total viewers across the platform (minimum floor enforced elsewhere).
export const totalViewers = levels.reduce((sum, l) => sum + l.viewers, 0);

export const totalLessons = levels.reduce((sum, l) => sum + l.lessonsCount, 0);

// Most popular level (by viewers)
export const topLevel = [...levels].sort((a, b) => b.viewers - a.viewers)[0];

// Flatten lessons with their parent level, sorted by viewers (desc).
export function getPopularLessons(limit = 5) {
  const all = levels.flatMap((level) =>
    level.lessons.map((lesson) => ({
      ...lesson,
      levelSlug: level.slug,
      levelTitle: level.title,
      levelNumber: level.number,
    }))
  );
  return all.sort((a, b) => b.viewers - a.viewers).slice(0, limit);
}
