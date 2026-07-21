# Learn With Acel

Platform belajar web development modern dengan UI minimalis, clean, dan dark mode first. Dibangun dengan Next.js (App Router), Tailwind CSS, dan Framer Motion.

Tagline: **Belajar Web Development Dari Nol.** — *From Beginner to Real Developer.*

## Getting started

```bash
npm install
npm run dev
```

Buka [http://localhost:3000](http://localhost:3000).

## Scripts

- `npm run dev` — jalankan server development
- `npm run build` — build untuk produksi
- `npm run start` — jalankan hasil build
- `npm run lint` — jalankan linter

## Struktur folder

```
src/
├── app/                 # Next.js App Router pages
│   ├── about/
│   ├── dashboard/
│   ├── donate/
│   ├── materi/[level]/[lesson]/
│   ├── roadmap/
│   ├── layout.jsx
│   └── page.jsx
├── components/
│   ├── home/            # Section components untuk halaman home
│   ├── layout/          # Navbar, Footer
│   ├── lesson/          # Quiz, reading progress
│   └── ui/              # Primitives (Card, Reveal, ProgressBar, ...)
└── lib/                 # Data & helpers (roadmap, lessonContent, utils)
```

## Design tokens

- Background utama: `#0D0D0D`
- Secondary background: `#151515`
- Card: `#1C1C1C`
- Text utama: `#F5F5F5`
- Text secondary: `#A1A1AA`
- Accent utama: `#7C3AED`
- Accent hover: `#8B5CF6`

Semua token tersedia di `tailwind.config.js`.

## Halaman

- `/` Home — hero, roadmap preview, fitur, preview materi, about creator, donation CTA
- `/roadmap` Roadmap 5 level (HTML CSS, JavaScript, React Tailwind, Real Project, Career)
- `/materi/[level]/[lesson]` Materi detail ala dokumentasi premium + quiz
- `/dashboard` Dashboard user dengan progress, bookmark, recently viewed
- `/about` Cerita creator, visi, perjalanan, FAQ
- `/donate` Support dengan QRIS placeholder

## Catatan

Semua materi bersifat data statis di `src/lib/lessonContent.js`. Mudah dipindahkan ke CMS atau MDX saat dibutuhkan.
