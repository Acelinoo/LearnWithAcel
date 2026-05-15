# Product Requirements Document (PRD)
## LearnWithAcel — Platform Belajar Web Development

| Field | Value |
| :--- | :--- |
| **Versi** | 1.0 |
| **Status** | Active (MVP berjalan) |
| **Last Updated** | 15 Mei 2026 |
| **Owner** | Marchelino Kurniawan (Acel) |
| **Tagline** | *Belajar Web Development Dari Nol — From Beginner to Real Developer.* |

---

## 1. Ringkasan Produk

LearnWithAcel adalah platform belajar web development berbahasa Indonesia, dengan fokus pada user experience minimalis (dark-mode first), kurikulum berjenjang (level-based), dan tracking progress per user. Konten ditulis dalam format Markdown dan dikelola lewat panel admin/CMS internal.

Platform terdiri dari dua bagian:
- **Frontend** — Next.js 14 (App Router) + Tailwind CSS + Framer Motion.
- **Backend** — FastAPI + PostgreSQL + Prisma (Python), JWT auth.

---

## 2. Latar Belakang & Masalah

Sumber belajar web dev untuk pemula Indonesia tersebar dan tidak memiliki jalur yang jelas: tutorial YouTube, artikel acak, dan dokumentasi resmi dalam bahasa Inggris membuat pemula bingung harus mulai dari mana. Platform berbayar global juga sering tidak relevan secara budaya dan bahasa.

LearnWithAcel hadir untuk memberi:
- Roadmap berjenjang yang jelas (Level 1 → Level 5+).
- Materi singkat, padat, gratis, berbahasa Indonesia.
- Progress tracking sehingga learner tahu posisi mereka.
- Multi-jalur (Frontend, Backend, Fullstack, Vibe Coding) sehingga learner bisa memilih spesialisasi.

---

## 3. Tujuan & Metrik Sukses

### 3.1 Tujuan Produk
1. Menjadi gerbang masuk bagi pemula Indonesia ke dunia web development.
2. Membantu learner menyelesaikan satu jalur belajar end-to-end (Frontend MVP terlebih dahulu).
3. Membuka jalur belajar tambahan (Backend, Fullstack, Vibe Coding) secara modular.

### 3.2 Tujuan Teknis
- **Centralized Content** — semua materi tersimpan di database, bukan file `.js` statis.
- **Real Analytics** — angka viewer real (bukan simulasi) di masa depan.
- **Scalability** — arsitektur siap menampung jalur baru tanpa rewrite.

### 3.3 Metrik Sukses (Fase MVP → Growth)
| Metrik | Target Fase MVP | Target Growth |
| :--- | :--- | :--- |
| Registered users | 100 | 5.000 |
| Active learners (≥1 lesson/minggu) | 30 | 1.500 |
| Lessons completed (total) | 500 | 50.000 |
| Completion rate per level | 25% | 40% |
| API p95 latency | < 400ms | < 200ms |
| Frontend Lighthouse (Performance) | ≥ 85 | ≥ 90 |

---

## 4. Persona Pengguna

**1. Learner Pemula (primary)** — Mahasiswa/pelajar 17-25 tahun, belum pernah ngoding, butuh jalur terstruktur. Akses dominan via desktop (saat belajar) + mobile (saat browsing).

**2. Learner Career-switcher** — Profesional 23-35 tahun yang ingin pivot ke web dev. Butuh estimasi waktu, mini project realistis, dan progress yang terukur.

**3. Admin / Content Maintainer** — Acel sendiri (single-admin saat ini). Butuh CMS internal untuk menambah/edit/hapus category, level, dan lesson Markdown.

---

## 5. Lingkup (Scope)

### 5.1 In-Scope (MVP yang sudah berjalan)
- Auth: register, login, logout, profile (`/auth/me`).
- Public content: list categories, full roadmap per category, detail lesson.
- Progress tracking: mark lesson complete (idempotent), stats keseluruhan + per-level.
- Admin CMS: CRUD category, level, lesson (Markdown editor).
- Frontend pages: Home, Roadmap, Materi (lesson viewer), Dashboard, Admin, About, Donate, Login, Register, Onboarding, Pilih Jalur.
- Multi-jalur: Frontend, Backend, Fullstack, Vibe (slug `vibe`).

### 5.2 Out-of-Scope (saat ini)
- Pembayaran / paid tier.
- Komentar, forum, atau social features.
- Sertifikat otomatis.
- Live class / video conferencing.
- Mobile native app.
- Multi-tenant / multi-admin role granular (saat ini hanya boolean `is_admin`).
- Recommendation engine.

### 5.3 Nice-to-have (Backlog)
- Bookmark lesson.
- Search global.
- Notifikasi email saat ada lesson baru.
- Export progress sebagai PDF.
- Quiz interaktif terhubung ke progress (saat ini quiz client-side saja).

---

## 6. User Stories & Alur Utama

### 6.1 Onboarding Learner
1. Buka homepage → lihat hero + roadmap preview.
2. Klik **Mulai belajar** atau **Register**.
3. Isi form (email, full_name, password) → JWT diset di cookie httpOnly.
4. Redirect ke `/onboarding` → pilih jalur belajar (Frontend/Backend/Fullstack/Vibe).
5. Masuk ke `/dashboard` melihat progress (initially 0%).

### 6.2 Belajar 1 Lesson
1. Dari Dashboard atau Roadmap, klik lesson.
2. Buka `/materi/[level]/[lesson]` → lihat Markdown content + reading progress bar + quiz (jika ada).
3. Klik **Tandai selesai** → POST `/progress/complete/{lesson_id}`.
4. Stats Dashboard otomatis update (force-dynamic page).

### 6.3 Admin Mengelola Konten
1. Login dengan akun yang `is_admin = true`.
2. Buka `/admin` → lihat panel CMS (`AdminCMS`).
3. Pilih `CategoryManager` / `LevelManager` / `LessonManager`.
4. Buat / edit / hapus → call `/api/v1/admin/...`.
5. Perubahan langsung tercermin di public pages (cache server-side adalah `force-dynamic`).

---

## 7. Functional Requirements

### 7.1 Authentication & Account
| ID | Requirement |
| :--- | :--- |
| FR-A1 | User dapat register dengan email + full_name + password (hashed bcrypt). |
| FR-A2 | User dapat login dan menerima JWT token (HS256, TTL 24 jam default). |
| FR-A3 | Token disimpan di cookie httpOnly oleh frontend (cookie name dari `TOKEN_COOKIE`). |
| FR-A4 | Endpoint `GET /auth/me` mengembalikan profil current user. |
| FR-A5 | User dapat logout (cookie dihapus client-side). |
| FR-A6 | Middleware Next.js memblok akses `/dashboard`, `/onboarding`, `/admin` jika tidak ada token, dan memantulkan user ber-token dari `/login`/`/register` ke `/dashboard`. |
| FR-A7 | Validasi token sebenarnya dilakukan di server component via `getServerUser()` (single source of truth). |

### 7.2 Content (Public)
| ID | Requirement |
| :--- | :--- |
| FR-C1 | `GET /categories` mengembalikan semua category (Frontend/Backend/Fullstack/Vibe) termasuk flag `available`. |
| FR-C2 | `GET /roadmap/{category_slug}` mengembalikan category + nested levels + nested lessons (summary). |
| FR-C3 | `GET /lessons/{level_slug}/{lesson_slug}` mengembalikan Markdown content + metadata. |
| FR-C4 | Semua endpoint content public (tanpa auth). |
| FR-C5 | Frontend merender Markdown via helper `lib/markdown.tsx`. |

### 7.3 Progress
| ID | Requirement |
| :--- | :--- |
| FR-P1 | `POST /progress/complete/{lesson_id}` idempotent — boleh dipanggil berulang. |
| FR-P2 | `GET /progress/stats` mengembalikan: total_lessons, completed_lessons, overall_percentage, by_level breakdown. |
| FR-P3 | Stats dibatasi user yang sedang login (JWT required). |
| FR-P4 | Dashboard menampilkan stats real-time (page `force-dynamic`). |

### 7.4 Admin / CMS
| ID | Requirement |
| :--- | :--- |
| FR-AD1 | Semua endpoint `/admin/*` membutuhkan JWT + flag `is_admin = true` (dependency `get_current_admin`). |
| FR-AD2 | Halaman `/admin` di frontend redirect ke login jika belum auth, dan menampilkan "Akses ditolak" jika non-admin. |
| FR-AD3 | CRUD Category dengan field: name, slug, available, role, side, description, tasks, techs (JSON `[{label, items[]}]`). |
| FR-AD4 | CRUD Level dengan field: number, title, slug, subtitle, description, duration, difficulty, accent_color, mini_project, quiz_count, base_viewers, tags (JSON), coming_soon. |
| FR-AD5 | CRUD Lesson dengan field: title, slug, summary, content (Markdown), duration, base_viewers, order_index. |
| FR-AD6 | DELETE bersifat cascade (delete category menghapus level & lesson di bawahnya, sesuai schema Prisma). |
| FR-AD7 | Update bersifat partial (PATCH-like, hanya field yang dikirim yang berubah). |
| FR-AD8 | Slug Category unik global, slug Level unik per category, slug Lesson unik per level. |

---

## 8. Information Architecture (Halaman Frontend)

| Path | Akses | Tipe Render | Deskripsi |
| :--- | :--- | :--- | :--- |
| `/` | Public | Static | Home — hero, roadmap preview, fitur, materi preview, about, donate CTA. |
| `/roadmap` | Public | Server | Roadmap multi-jalur. |
| `/roadmap/vibe` | Public | Server | Detail roadmap jalur Vibe Coding. |
| `/materi/[level]/[lesson]` | Public | Server | Lesson viewer (Markdown). |
| `/materi/vibe/[level]/[lesson]` | Public | Server | Lesson viewer untuk jalur vibe. |
| `/persiapan` | Public | Server | Halaman persiapan / tools. |
| `/persiapan/vibe` | Public | Server | Persiapan jalur vibe. |
| `/about` | Public | Static | Cerita creator + visi. |
| `/donate` | Public | Static | Halaman dukungan (QRIS placeholder). |
| `/login` | Public (gated jika sudah login) | Client form | Form login + redirectTo support. |
| `/register` | Public (gated jika sudah login) | Client form | Form register. |
| `/onboarding` | Authenticated | Server + Client | Pilih path setelah register. |
| `/pilih-jalur` | Public | Server | Pilih jalur belajar dari beranda. |
| `/dashboard` | Authenticated | Server (force-dynamic) | Stats user, materi populer, leaderboard level. |
| `/admin` | Admin only | Server (force-dynamic) | CMS untuk category/level/lesson. |

---

## 9. Data Model (PostgreSQL via Prisma)

```text
User
  id (uuid PK), email (unique), full_name, hashed_password,
  avatar_url?, is_admin (bool, default false), created_at
  └── 1:N UserProgress

Category
  id (uuid PK), name, slug (unique), available (bool),
  role, side, description, tasks, techs (Json: [{label, items[]}])
  └── 1:N Level

Level
  id (uuid PK), category_id (FK), number, title, slug,
  subtitle, description, duration, difficulty, accent_color,
  mini_project, quiz_count, base_viewers, tags (Json: string[]),
  coming_soon (bool)
  unique(category_id, slug)
  └── 1:N Lesson

Lesson
  id (uuid PK), level_id (FK), title, slug, summary,
  content (Markdown text), duration, base_viewers, order_index
  unique(level_id, slug)
  └── 1:N UserProgress

UserProgress
  id (uuid PK), user_id (FK), lesson_id (FK),
  is_completed (bool), completed_at (DateTime?)
  unique(user_id, lesson_id)
```

Cascade delete: hapus Category → cascade hapus Level → cascade hapus Lesson → cascade hapus UserProgress.

---

## 10. API Contract (V1)

Base URL: `http://127.0.0.1:8000/api/v1` (dev) — frontend membaca dari `NEXT_PUBLIC_API_URL`.

### 10.1 Auth
| Method | Path | Auth | Body / Response |
| :--- | :--- | :--- | :--- |
| POST | `/auth/register` | — | Body: `{email, full_name, password}` → 201 `UserResponse` |
| POST | `/auth/login` | — | Body: `{email, password}` → `{access_token, token_type}` |
| GET | `/auth/me` | Bearer | → `UserResponse` |

### 10.2 Content
| Method | Path | Auth | Response |
| :--- | :--- | :--- | :--- |
| GET | `/categories` | — | `CategoryResponse[]` |
| GET | `/roadmap/{category_slug}` | — | `RoadmapResponse` (category + levels[] + lessons[]) |
| GET | `/lessons/{level_slug}/{lesson_slug}` | — | `LessonDetail` (incl. Markdown content) |

### 10.3 Progress
| Method | Path | Auth | Response |
| :--- | :--- | :--- | :--- |
| POST | `/progress/complete/{lesson_id}` | Bearer | `ProgressResponse` |
| GET | `/progress/stats` | Bearer | `StatsResponse` (overall + by_level[]) |

### 10.4 Admin
| Method | Path | Auth |
| :--- | :--- | :--- |
| POST/PUT/DELETE | `/admin/categories[/{id}]` | Admin |
| POST/PUT/DELETE | `/admin/levels[/{id}]` | Admin |
| POST/PUT/DELETE | `/admin/lessons[/{id}]` | Admin |

### 10.5 Health
| Method | Path |
| :--- | :--- |
| GET | `/health` → `{status, version}` |

---

## 11. Authentication & Authorization

- **Hash**: bcrypt cost 12 (passlib).
- **Token**: JWT HS256, secret dari env `JWT_SECRET_KEY`, TTL default 1440 menit (24 jam) — `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`.
- **Storage frontend**: token disimpan di cookie httpOnly via helper `lib/auth/token.ts`. Tidak menggunakan localStorage.
- **Authorization model**:
  - Public — endpoint content.
  - Authenticated — endpoint progress.
  - Admin — endpoint `/admin/*`, ditegakkan via dependency `get_current_admin` yang memeriksa `is_admin = true`.
- **Promosi admin**: lewat script CLI `python -m scripts.promote_admin <email>`.
- **Timing-safe comparison** dipakai saat login untuk mencegah user enumeration.

---

## 12. Non-Functional Requirements

### 12.1 Performance
- API p95 < 400 ms (MVP), < 200 ms (Growth).
- Frontend FCP < 1.5s pada koneksi 4G.
- Dashboard & Admin pakai `dynamic = "force-dynamic"` agar data segar; halaman lain server-rendered atau static.

### 12.2 Security
- HTTPS only di production.
- CORS dibatasi via env `CORS_ORIGINS` (default include `http://localhost:3000`, `https://learnwithacel.vercel.app`).
- Validasi input via Pydantic v2 + Zod (`lib/validators/auth.ts`).
- Tidak menyimpan password plain di log atau response.
- Cookie token: httpOnly, Secure (di production), SameSite=Lax.

### 12.3 Reliability
- Database connection lifecycle dikelola via FastAPI lifespan (Prisma connect/disconnect).
- Idempotency: progress complete idempotent.
- Cascade delete dijaga di schema Prisma untuk konsistensi.

### 12.4 Accessibility
- Kontras WCAG AA pada palet dark mode (background `#0D0D0D`, text `#F5F5F5`).
- Komponen form punya label terkait (auth `FormField`).
- Navigasi keyboard didukung (lucide-react icons + button native).
- Validasi penuh aksesibilitas memerlukan manual testing dengan assistive technology — di luar cakupan otomatis.

### 12.5 Internasionalisasi
- Single language: Bahasa Indonesia.
- Tidak ada i18n framework; copy hard-coded untuk MVP.

### 12.6 Observability
- Backend pakai exception handler terpusat (`http_exception_handler`, `unhandled_exception_handler`).
- Logging via uvicorn default — di production sebaiknya disambungkan ke Sentry/Logtail (backlog).

---

## 13. Tech Stack

### 13.1 Frontend (`/Frontend`)
| Layer | Tool |
| :--- | :--- |
| Framework | Next.js 14.2.5 (App Router) |
| Language | TypeScript + JSX hybrid |
| Styling | Tailwind CSS 3.4 |
| Animation | framer-motion 11.3 |
| Icons | lucide-react 0.427 |
| Forms | react-hook-form + zod (`@hookform/resolvers`) |
| Auth helpers | Cookie-based (`lib/auth/token.ts`) + middleware |
| Data fetching | Native `fetch` via `lib/api/client.ts` (with `ApiError`) |

### 13.2 Backend (`/backend`)
| Layer | Tool |
| :--- | :--- |
| Framework | FastAPI 0.115 + uvicorn 0.32 |
| Language | Python 3.12 |
| Database | PostgreSQL 16 |
| ORM | Prisma Client Python 0.15 (asyncio interface) |
| Auth | PyJWT 2.10 + passlib[bcrypt] 1.7 |
| Validation | Pydantic 2.10 + pydantic-settings |
| HTTP client | httpx 0.28 (Prisma internal) |

### 13.3 Tooling & Deployment
- Dev DB: PostgreSQL via Prisma Cloud / Docker.
- Container: `Dockerfile` + `docker-compose.yml` di `/backend`.
- Frontend deploy target: Vercel.
- Backend deploy target: Railway / Fly.io / VPS Docker.

---

## 14. Environment Variables

### 14.1 Backend (`backend/.env`)
| Variable | Required | Default | Catatan |
| :--- | :--- | :--- | :--- |
| `DATABASE_URL` | ✅ | — | PostgreSQL connection string |
| `JWT_SECRET_KEY` | ✅ | — | Secret untuk sign JWT — wajib diganti di production |
| `JWT_ALGORITHM` | ❌ | `HS256` | |
| `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` | ❌ | `1440` | TTL token (menit) |
| `CORS_ORIGINS` | ❌ | `http://localhost:3000` | comma-separated |
| `DEBUG` | ❌ | `false` | |

### 14.2 Frontend (`Frontend/.env.local`)
| Variable | Required | Default |
| :--- | :--- | :--- |
| `NEXT_PUBLIC_API_URL` | ✅ | `http://127.0.0.1:8000` |

---

## 15. Roadmap & Milestones

### Fase 1 — MVP (DONE)
- [x] Schema Prisma + migrasi.
- [x] Auth (register/login/me) + JWT.
- [x] Public content endpoints.
- [x] Progress tracking + stats.
- [x] Admin CMS endpoints + frontend AdminCMS.
- [x] Frontend pages: Home, Roadmap, Materi, Dashboard, Admin, About, Donate, Onboarding, Pilih Jalur.
- [x] Multi-jalur (Frontend, Backend, Fullstack, Vibe).
- [x] Seed script (migrasi dari `.js` static ke DB).

### Fase 2 — Polish & Launch (Q3 2026)
- [ ] Sentry / error monitoring.
- [ ] Rate limiting (slowapi atau gateway).
- [ ] Email verification + password reset.
- [ ] SEO: dynamic OG image, robots, sitemap detail.
- [ ] Bookmark lesson (UserBookmark model).
- [ ] Avatar upload (S3 / Supabase Storage).

### Fase 3 — Growth (Q4 2026)
- [ ] Quiz tersinkron ke progress + skor.
- [ ] Sertifikat auto-generated per level.
- [ ] Search global (Postgres FTS / Meilisearch).
- [ ] Notifikasi email mingguan.
- [ ] Public viewer counter real-time (replace `base_viewers` simulasi).

### Fase 4 — Future
- [ ] Multi-admin role + permissions granular.
- [ ] Komunitas / komentar per lesson.
- [ ] Mobile PWA optimization.
- [ ] Pembayaran (Stripe / Midtrans) untuk premium track.

---

## 16. Risiko & Asumsi

### Risiko
| Risiko | Mitigasi |
| :--- | :--- |
| Konten Markdown tidak tervalidasi → potensi XSS | Sanitasi saat render Markdown di `lib/markdown.tsx`; admin endpoint hanya untuk admin tepercaya |
| JWT secret bocor | Wajib rotasi & simpan di secret manager production |
| Dependensi DB tunggal (PostgreSQL) → single point of failure | Backup otomatis + plan untuk replica |
| Admin tunggal → bottleneck konten | Roadmap multi-admin di Fase 4 |
| Cookie auth tidak dishared cross-domain | Dokumentasikan kebutuhan deploy di domain yang sama / subdomain |

### Asumsi
- Learner punya akses internet stabil dan device modern (browser ES2020+).
- Admin punya kemampuan basic Markdown.
- Skala awal di bawah 10K user, sehingga single-instance backend cukup.

---

## 17. Glossary

- **Category** — Jalur belajar utama (Frontend / Backend / Fullstack / Vibe).
- **Level** — Tahap dalam satu category (Level 1, 2, 3, ...).
- **Lesson** — Materi tunggal dalam Markdown, milik satu Level.
- **Progress** — Status `is_completed` per pasangan (user, lesson).
- **Vibe Coding** — Jalur belajar khusus berbasis pendekatan AI-assisted development.
- **CMS** — Panel admin internal di `/admin` untuk mengelola konten.

---

## 18. Lampiran — Struktur Repo

```
LearnWithAcel/
├── backend/
│   ├── app/
│   │   ├── api/v1/         # auth.py, content.py, progress.py, admin.py, router.py
│   │   ├── core/           # config, database (Prisma), deps, exceptions, security
│   │   ├── schemas/        # Pydantic models
│   │   ├── services/       # auth, content, progress, admin business logic
│   │   └── main.py         # app factory + lifespan
│   ├── prisma/schema.prisma
│   ├── scripts/            # seed.py, promote_admin.py
│   ├── Dockerfile, docker-compose.yml
│   └── requirements.txt
└── Frontend/
    ├── src/
    │   ├── app/            # Next.js App Router pages
    │   ├── components/     # admin, auth, dashboard, home, layout, lesson, ui
    │   └── lib/            # api/, auth/, validators/, markdown.tsx, utils.js
    ├── middleware.ts       # auth gate
    ├── tailwind.config.js
    └── package.json
```
