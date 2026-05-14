# PRODUCT REQUIREMENTS DOCUMENT (PRD)
## LearnWithAcel — Backend Infrastructure (Python FastAPI)

**Version:** 1.0  
**Status:** Draft / Planning  
**Tech Stack:** Python (FastAPI), PostgreSQL, Prisma (Python), JWT Auth  

---

## 1. Overview
Backend ini akan bertugas sebagai pusat data dan logika untuk platform **LearnWithAcel**. Fokus utamanya adalah memigrasi data statis (`roadmap.js` & `lessonContent.js`) ke database, mengelola autentikasi pengguna, dan menyimpan progres belajar setiap user.

---

## 2. Objectives
- **Centralized Data:** Mengelola konten materi, kuis, dan roadmap melalui database.
- **User Progression:** Memungkinkan user untuk login dan menyimpan progres belajar (lesson mana yang sudah selesai).
- **Real Analytics:** Mengganti angka *viewers* simulasi menjadi data asli berdasarkan interaksi user.
- **Scalability:** Menyiapkan infrastruktur untuk jalur belajar lain (Backend & Fullstack) di masa depan.

---

## 3. Tech Stack
| Komponen | Teknologi | Alasan |
| :--- | :--- | :--- |
| **Framework** | FastAPI (Python) | Performa tinggi, dukungan asinkron (async), dan auto-generated dokumentasi (Swagger). |
| **Database** | PostgreSQL | Standar industri untuk data relasional yang kompleks. |
| **ORM** | Prisma (Python) | Konsistensi dengan workflow proyek **Sentra** yang sudah kamu gunakan. |
| **Auth** | JWT (PyJWT) | *Stateless authentication* yang aman untuk integrasi frontend-backend. |
| **Deployment** | Docker / Vercel / Railway | Kemudahan dalam *scaling* dan *deployment*. |

---

## 4. Database Schema (ERD)

### 4.1 Core Tables
1. **User**
   - `id`: UUID (PK)
   - `email`: String (Unique)
   - `full_name`: String
   - `hashed_password`: String
   - `avatar_url`: String
   - `created_at`: DateTime

2. **Category** (Frontend, Backend, Fullstack)
   - `id`: UUID (PK)
   - `name`: String (e.g., "Frontend")
   - `slug`: String (Unique, e.g., "frontend")
   - `available`: Boolean (e.g., true/false)
   - `role`: String (e.g., "Front-End Developer")
   - `side`: String (e.g., "Sisi Klien")
   - `description`: Text
   - `tasks`: Text
   - `techs`: Json (Menyimpan array object seperti `[{ label: "Dasar", items: ["HTML"] }]`)

3. **Level**
   - `id`: UUID (PK)
   - `category_id`: FK (Category)
   - `number`: Int (e.g., 1, 2, 3)
   - `title`: String
   - `slug`: String
   - `subtitle`: String
   - `description`: Text
   - `duration`: String (e.g., "2 minggu")
   - `difficulty`: String (e.g., "Pemula")
   - `accent_color`: String (Gradient CSS class)
   - `mini_project`: String (e.g., "Landing page pribadi")
   - `quiz_count`: Int (e.g., 3)
   - `base_viewers`: Int (Angka viewers simulasi dari frontend)
   - `tags`: Json (Menyimpan array string `["HTML5", "CSS3"]`)

4. **Lesson**
   - `id`: UUID (PK)
   - `level_id`: FK (Level)
   - `title`: String
   - `slug`: String
   - `summary`: Text
   - `content`: Text (Markdown support)
   - `duration`: String (e.g., "15 menit")
   - `base_viewers`: Int (Angka viewers simulasi)
   - `order_index`: Int (Urutan materi dalam satu level)

5. **UserProgress**
   - `id`: UUID (PK)
   - `user_id`: FK (User)
   - `lesson_id`: FK (Lesson)
   - `is_completed`: Boolean
   - `completed_at`: DateTime

---

## 5. API Endpoints (V1)

### 5.1 Authentication
- `POST /auth/register`: Pendaftaran user baru.
- `POST /auth/login`: Login dan mendapatkan JWT Token.
- `GET /auth/me`: Mengambil data profile user yang sedang login.

### 5.2 Public Roadmap & Content (User Facing)
- `GET /categories`: Mengambil semua kategori jalur belajar.
- `GET /roadmap/{category_slug}`: Mengambil semua level dan materi dalam satu jalur.
- `GET /lessons/{level_slug}/{lesson_slug}`: Mengambil detail isi materi.

### 5.3 Progress Tracking (User Facing)
- `POST /progress/complete/{lesson_id}`: Menandai materi sebagai selesai.
- `GET /progress/stats`: Mengambil statistik belajar user (persentase selesai).

### 5.4 Content Management (Admin / CMS)
Untuk mengakomodasi pengelolaan data materi (seperti yang saat ini ada di `roadmap.js`, `lessonContent.js`, dll) dari sisi backend, diperlukan endpoint admin berikut:

**Categories**
- `POST /admin/categories`: Membuat kategori baru.
- `PUT /admin/categories/{id}`: Mengupdate data kategori.
- `DELETE /admin/categories/{id}`: Menghapus kategori.

**Levels**
- `POST /admin/levels`: Membuat level baru dalam kategori tertentu.
- `PUT /admin/levels/{id}`: Mengupdate data level.
- `DELETE /admin/levels/{id}`: Menghapus level.

**Lessons (Materi & Content)**
- `POST /admin/lessons`: Membuat materi/lesson baru. Endpoint ini digunakan untuk melakukan post content materi beserta detail lainnya.
- `PUT /admin/lessons/{id}`: Mengupdate isi materi (termasuk post content berformat markdown).
- `DELETE /admin/lessons/{id}`: Menghapus materi.

---

## 6. Implementation Plan (Fase 1)

1.  **Environment Setup**:
    - Inisialisasi proyek FastAPI.
    - Setup Prisma dengan PostgreSQL.
2.  **Data Migration**:
    - Membuat script untuk memindahkan data dari `roadmap.js` dan `lessonContent.js` ke database PostgreSQL.
3.  **Auth Implementation**:
    - Membuat sistem login/register dengan JWT.
4.  **Frontend Integration**:
    - Mengganti `import` data statis di frontend dengan pemanggilan API (menggunakan `fetch` atau `SWR/TanStack Query`).

---

## 7. Security & Best Practices
- **Password Hashing**: Menggunakan `passlib` dengan algoritma `bcrypt`.
- **CORS Configuration**: Memastikan backend hanya bisa diakses oleh domain frontend LearnWithAcel.
- **Validation**: Menggunakan `Pydantic` untuk validasi input API.
- **Async DB**: Menggunakan fitur asinkron Prisma untuk performa maksimal.
