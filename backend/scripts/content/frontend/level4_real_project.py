"""
Frontend / Level 4 — Real Project (Next.js).

Lessons:
  1. struktur-project-modern
  2. server-vs-client-component
  3. data-fetching-modern
  4. deploy-ke-vercel             (deploy lesson)
  5. mini-project-dashboard       (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Struktur Project Modern
# ─────────────────────────────────────────────────────────────────────────────

LESSON_STRUKTUR = make_lesson(
    title="Struktur Project Modern dengan Next.js",
    slug="struktur-project-modern",
    order_index=1,
    read_time="14 menit",
    summary="Folder structure App Router, konvensi penamaan, dan setup tooling.",
    tools=["Node.js LTS", "VS Code", "Terminal"],
    outcomes=[
        "Setup project Next.js 14 dari nol",
        "Memahami folder structure App Router",
        "Mengatur Tailwind CSS dan absolute import",
    ],
    tldr=(
        "Next.js App Router pakai konvensi 'folder = URL'. File `page.jsx` "
        "untuk halaman, `layout.jsx` untuk pembungkus. Setup awal: "
        "create-next-app, lalu Tailwind + alias `@/`."
    ),
    pembuka=dedent(
        """\
        Sampai di Level 4, kamu sudah bisa bikin landing page dan portfolio. Tapi project profesional butuh struktur yang lebih rapi.

        Next.js adalah framework React paling populer untuk project nyata. Twitch, TikTok, Notion, Vercel — semuanya pakai Next.js.

        Lesson ini bukan ngajarin React lagi. Fokus: bagaimana mengorganisasi project supaya bisa di-maintain berbulan-bulan ke depan.
        """
    ),
    penjelasan=dedent(
        """\
        ### Setup project baru

        Buka terminal di folder kosong:

        ```bash
        npx create-next-app@latest my-app
        ```

        Wizard akan tanya. Pilih ini:

        - TypeScript: Yes (tipe yang aman)
        - ESLint: Yes (bantu cek error)
        - Tailwind CSS: Yes (styling cepat)
        - `src/` directory: Yes (lebih rapi)
        - App Router: Yes (versi modern)
        - Customize import alias: pilih default (`@/*`)

        Lalu:

        ```bash
        cd my-app
        npm run dev
        ```

        Buka [localhost:3000](http://localhost:3000).

        ### Folder structure App Router

        ```text
        my-app/
        ├── src/
        │   └── app/
        │       ├── layout.tsx        ← pembungkus semua halaman
        │       ├── page.tsx          ← halaman /
        │       ├── globals.css
        │       ├── about/
        │       │   └── page.tsx      ← halaman /about
        │       └── blog/
        │           ├── page.tsx      ← halaman /blog
        │           └── [slug]/
        │               └── page.tsx  ← halaman /blog/halo, /blog/dunia, dst
        ├── public/                   ← gambar static, favicon
        ├── next.config.js
        ├── tailwind.config.ts
        └── tsconfig.json
        ```

        Aturan utama:

        - **Folder = URL**. `app/about/` jadi `/about`.
        - `page.tsx` di tiap folder = halaman utama.
        - `layout.tsx` membungkus semua halaman di dalam folder itu.
        - Kurung kotak `[slug]` = parameter dinamis.

        ### File khusus

        - `loading.tsx` — UI saat halaman sedang loading.
        - `error.tsx` — UI saat ada error.
        - `not-found.tsx` — UI saat halaman tidak ada (404).
        - `layout.tsx` — pembungkus persistent (navbar, footer).

        ### Components folder

        Component yang dipakai di banyak halaman taruh di `src/components/`:

        ```text
        src/
        ├── app/
        └── components/
            ├── ui/             ← primitive (Button, Card, Input)
            ├── layout/         ← Navbar, Footer
            └── home/           ← section khusus homepage
        ```

        ### Absolute import

        `tsconfig.json` sudah punya alias `@/*`. Jadi instead of:

        ```ts
        import Button from "../../../components/ui/Button";
        ```

        Cukup:

        ```ts
        import Button from "@/components/ui/Button";
        ```

        Kerja jauh lebih nyaman saat folder dalam-dalam.

        ### Setup Tailwind

        `create-next-app` sudah set Tailwind. Edit `tailwind.config.ts` untuk warna custom:

        ```ts
        export default {
          content: ["./src/**/*.{js,ts,jsx,tsx}"],
          theme: {
            extend: {
              colors: {
                primary: "#4EBAEC",
                background: "#0a0a0a",
              },
            },
          },
        };
        ```

        Pakai dengan `bg-primary text-background` di JSX.
        """
    ),
    contoh_code_md=dedent(
        """\
        Layout yang persistent di setiap halaman:

        ```tsx
        // src/app/layout.tsx
        import "./globals.css";
        import { Inter } from "next/font/google";
        import Navbar from "@/components/layout/Navbar";
        import Footer from "@/components/layout/Footer";

        const inter = Inter({ subsets: ["latin"] });

        export const metadata = {
          title: "My App",
          description: "Aplikasi keren saya",
        };

        export default function RootLayout({ children }) {
          return (
            <html lang="id" className={inter.className}>
              <body>
                <Navbar />
                <main>{children}</main>
                <Footer />
              </body>
            </html>
          );
        }
        ```

        Halaman About sederhana:

        ```tsx
        // src/app/about/page.tsx
        export default function AboutPage() {
          return (
            <section className="mx-auto max-w-3xl px-4 py-16">
              <h1 className="text-4xl font-semibold">Tentang Kami</h1>
              <p className="mt-4 text-gray-400">
                Kami bikin tools yang membantu developer.
              </p>
            </section>
          );
        }
        ```
        """
    ),
    practice=(
        "Bikin project Next.js baru. Tambah halaman `/about` dan `/contact`. "
        "Bikin Navbar di `components/layout/Navbar.tsx` yang punya link ke "
        "kedua halaman. Pakai di `layout.tsx` supaya muncul di semua halaman."
    ),
    fix_error={
        "language": "tsx",
        "broken_code": dedent(
            """\
            // src/app/blog/[slug].tsx
            export default function BlogPost({ params }) {
              return <h1>Post: {params.slug}</h1>;
            }
            """
        ),
        "hint": "App Router butuh struktur folder spesifik untuk URL dinamis. Cek lokasi file.",
        "answer_explanation": dedent(
            """\
            Kesalahan: di App Router, halaman dinamis butuh folder, bukan file langsung.

            Yang benar:

            - File di luar folder `[slug]/`: `app/blog/[slug].tsx` ❌
            - Folder bernama `[slug]/` dengan `page.tsx` di dalamnya ✓
            """
        ),
        "fixed_code": dedent(
            """\
            // src/app/blog/[slug]/page.tsx
            export default function BlogPost({ params }) {
              return <h1>Post: {params.slug}</h1>;
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa fungsi `layout.tsx` di Next.js App Router?",
            [
                "Halaman default",
                "Pembungkus persistent untuk halaman di folder yang sama dan child folder-nya",
                "File CSS",
                "Tidak penting",
            ],
            "B",
            "Layout dipakai untuk navbar, footer, atau wrapper yang muncul di semua halaman dalam folder. Tidak re-render saat pindah halaman.",
        ),
        q(
            "Mana yang BENAR untuk URL dinamis `/blog/halo`?",
            [
                "`app/blog-[slug].tsx`",
                "`app/blog/[slug]/page.tsx`",
                "`app/blog/$slug.tsx`",
                "`app/blog?slug=halo.tsx`",
            ],
            "B",
            "App Router pakai folder dengan kurung kotak `[param]`, lalu `page.tsx` di dalamnya.",
        ),
        q(
            "Apa keuntungan absolute import dengan alias `@/`?",
            [
                "Lebih cepat",
                "Path tidak break saat file dipindahkan, dan lebih bersih daripada `../../../`",
                "Wajib oleh Next.js",
                "Untuk SEO",
            ],
            "B",
            "Path absolut lebih maintain-able. Move file ke folder lain, import-nya tetap valid.",
        ),
        q(
            "File apa yang dipakai untuk halaman 404 di App Router?",
            [
                "`error.tsx`",
                "`not-found.tsx`",
                "`404.tsx`",
                "`fallback.tsx`",
            ],
            "B",
            "`not-found.tsx` adalah file khusus App Router untuk halaman 'tidak ditemukan'.",
        ),
        q(
            "Bagaimana cara menambah halaman `/contact` di Next.js?",
            [
                "Bikin file `contact.tsx` di root",
                "Bikin folder `contact/` dengan `page.tsx` di dalamnya",
                "Edit `pages.tsx`",
                "Tambah route di config",
            ],
            "B",
            "App Router: folder = URL, `page.tsx` = halaman utama. Konsisten.",
        ),
    ],
    common_mistakes=[
        "Bikin `app/blog/[slug].tsx` (file langsung) bukan `app/blog/[slug]/page.tsx` (folder + page).",
        "Pakai relative import panjang (`../../../`) padahal alias `@/` sudah disiapkan.",
        "Lupa import `globals.css` di `layout.tsx`. Tailwind tidak jalan.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Server vs Client Component
# ─────────────────────────────────────────────────────────────────────────────

LESSON_SVR_CLIENT = make_lesson(
    title="Server vs Client Component",
    slug="server-vs-client-component",
    order_index=2,
    read_time="12 menit",
    summary="Kapan pakai server component, kapan butuh client component.",
    tools=["Project Next.js dari lesson 1"],
    outcomes=[
        "Membedakan server dan client component",
        "Tahu kapan butuh `'use client'`",
        "Memilih jenis component yang tepat untuk tiap kasus",
    ],
    tldr=(
        "Server component (default) dirender di server — cepat, akses DB "
        "langsung. Client component butuh `'use client'` di baris pertama, "
        "dipakai saat butuh state, event, atau hook. Mix keduanya bebas."
    ),
    pembuka=dedent(
        """\
        Next.js App Router punya konsep yang awalnya bikin bingung: setiap component bisa berjalan di server atau di browser.

        Default-nya semua component berjalan di server. Itu beda dari React biasa yang semua di browser.

        Setelah lesson ini, kamu bisa pilih dengan tepat: 'ini cukup di server' atau 'ini harus di client'.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa yang dimaksud "server component"

        Server component adalah component yang dirender **di server** sebelum HTML dikirim ke browser. Browser cuma terima hasil render-nya, bukan kode component-nya.

        Keuntungan:

        - Akses database / API key tidak bocor ke browser.
        - Bundle JavaScript di browser jadi lebih kecil = halaman lebih cepat.
        - Bisa pakai `await` langsung di body component.

        Keterbatasan:

        - Tidak bisa pakai `useState`, `useEffect`, hooks lain.
        - Tidak bisa pasang event handler (`onClick`, `onChange`).
        - Tidak bisa akses `window`, `document`, `localStorage`.

        ### Client component

        Client component adalah component yang dirender di **browser**. Untuk menandai, tambah `"use client"` di baris pertama file.

        Keuntungan:

        - Bisa pakai semua React hooks.
        - Bisa pasang event handler.
        - Bisa akses browser API (window, localStorage, dll).

        Keterbatasan:

        - Tidak bisa `await` data fetching langsung.
        - Bundle JavaScript di browser lebih besar.

        ### Cara pilih

        Default: server component. Pindah ke client component kalau butuh **salah satu** dari:

        - State (`useState`).
        - Effect (`useEffect`, `useLayoutEffect`).
        - Event handler (`onClick`, dll).
        - Browser-only API.
        - Library yang dipakainya butuh client (misal `framer-motion`).

        ### Pola umum: page server + island client

        Halaman utama tetap server component, lalu sisipkan client component cuma di bagian yang butuh interaksi.

        ```tsx
        // app/products/page.tsx (server component)
        import { db } from "@/lib/db";
        import AddToCartButton from "./AddToCartButton";

        export default async function ProductsPage() {
          const products = await db.product.findMany();

          return (
            <div>
              {products.map((p) => (
                <article key={p.id}>
                  <h3>{p.name}</h3>
                  <p>Rp {p.price}</p>
                  {/* ↓ Cuma button-nya yang client */}
                  <AddToCartButton productId={p.id} />
                </article>
              ))}
            </div>
          );
        }
        ```

        ```tsx
        // app/products/AddToCartButton.tsx (client component)
        "use client";
        import { useState } from "react";

        export default function AddToCartButton({ productId }) {
          const [adding, setAdding] = useState(false);

          return (
            <button
              onClick={() => {
                setAdding(true);
                /* ... add to cart logic */
              }}
              disabled={adding}
            >
              {adding ? "Menambah..." : "Beli"}
            </button>
          );
        }
        ```

        Pola ini optimal: data fetching di server, interaksi di client.

        ### "use client" mengalir ke child

        Saat component punya `"use client"`, semua child component yang di-import jadi **bagian dari client bundle**.

        Jadi pasang `"use client"` di level se-bawah mungkin (di leaf), bukan di parent yang besar.
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman dashboard yang fetch data di server lalu kasih ke client component:

        ```tsx
        // app/dashboard/page.tsx (server)
        import { db } from "@/lib/db";
        import StatsChart from "./StatsChart";

        export default async function Dashboard() {
          // Fetch langsung di server, tidak butuh useEffect.
          const stats = await db.stat.findMany();

          return (
            <main>
              <h1>Dashboard</h1>
              <StatsChart data={stats} />
            </main>
          );
        }
        ```

        ```tsx
        // app/dashboard/StatsChart.tsx (client)
        "use client";

        import { useState } from "react";

        export default function StatsChart({ data }) {
          const [filter, setFilter] = useState("all");

          const filtered = data.filter(
            (s) => filter === "all" || s.category === filter,
          );

          return (
            <div>
              <select value={filter} onChange={(e) => setFilter(e.target.value)}>
                <option value="all">Semua</option>
                <option value="sales">Sales</option>
                <option value="users">Users</option>
              </select>

              <ul>
                {filtered.map((s) => (
                  <li key={s.id}>{s.label}: {s.value}</li>
                ))}
              </ul>
            </div>
          );
        }
        ```

        Server fetch data lalu kasih sebagai prop. Client component handle interaksi.
        """
    ),
    practice=(
        "Bikin halaman `/counter` dengan dua section: di atas, server component "
        "yang menampilkan tanggal hari ini (dari `new Date()`). Di bawah, client "
        "component dengan tombol counter (`useState`). Buktikan dua-duanya bisa "
        "berdampingan di satu halaman."
    ),
    fix_error={
        "language": "tsx",
        "broken_code": dedent(
            """\
            // app/profile/page.tsx
            import { useState } from "react";

            export default function ProfilePage() {
              const [name, setName] = useState("Acel");
              return (
                <div>
                  <h1>Halo {name}</h1>
                  <button onClick={() => setName("Updated")}>Ubah</button>
                </div>
              );
            }
            """
        ),
        "hint": "Kode ini akan error 'You're importing a component that needs useState'. Apa yang kurang?",
        "answer_explanation": dedent(
            """\
            Kesalahan: component pakai `useState` dan `onClick`, tapi tidak ada `"use client"`. Default-nya adalah server component, dan server component tidak bisa pakai hooks atau event.

            Solusi: tambah `"use client"` di baris pertama.
            """
        ),
        "fixed_code": dedent(
            """\
            // app/profile/page.tsx
            "use client";

            import { useState } from "react";

            export default function ProfilePage() {
              const [name, setName] = useState("Acel");
              return (
                <div>
                  <h1>Halo {name}</h1>
                  <button onClick={() => setName("Updated")}>Ubah</button>
                </div>
              );
            }
            """
        ),
    },
    quiz=[
        q(
            "Default component di Next.js App Router adalah?",
            [
                "Client component",
                "Server component",
                "Static component",
                "Dynamic component",
            ],
            "B",
            "App Router default ke server component. Kamu harus eksplisit pakai `'use client'` untuk pindah ke client component.",
        ),
        q(
            "Mana yang TIDAK BISA dipakai di server component?",
            [
                "`async/await` untuk fetch data",
                "Akses environment variable di server",
                "`useState` dan `onClick`",
                "Import dari node_modules",
            ],
            "C",
            "Hooks dan event handler cuma jalan di browser. Server component tidak bisa pakai keduanya.",
        ),
        q(
            "Kapan kamu butuh `'use client'`?",
            [
                "Selalu",
                "Saat component butuh state, effect, event, atau browser API",
                "Saat ada gambar",
                "Saat pakai Tailwind",
            ],
            "B",
            "Aturan: pakai server component dulu. Pindah ke client cuma kalau memang butuh interaktivitas.",
        ),
        q(
            "Apa pola yang OPTIMAL untuk halaman dengan data + interaksi?",
            [
                "Semua di client component",
                "Page sebagai server component yang fetch data, lalu sisipkan client component cuma di bagian interaktif",
                "Semua di server component",
                "Pakai useEffect untuk fetch",
            ],
            "B",
            "Pola 'page server + island client' kasih combo terbaik: data fetching cepat di server, interaksi di client.",
        ),
        q(
            "Apa yang terjadi saat parent client component import child server component?",
            [
                "Tidak masalah",
                "Child otomatis ikut jadi bagian client bundle — kehilangan keuntungan server",
                "Error",
                "Halaman blank",
            ],
            "B",
            "`'use client'` mengalir ke child. Pasang di level paling bawah (leaf) supaya minimum kode jadi client.",
        ),
    ],
    common_mistakes=[
        "Pakai `useState` di file tanpa `'use client'`. Build error.",
        "Pasang `'use client'` di parent besar. Semua child jadi client bundle, halaman jadi berat.",
        "Coba akses database langsung di client component. Tidak boleh — credentials bocor.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Data Fetching Modern
# ─────────────────────────────────────────────────────────────────────────────

LESSON_FETCH = make_lesson(
    title="Data Fetching Modern",
    slug="data-fetching-modern",
    order_index=3,
    read_time="12 menit",
    summary="Async server component, fetch caching, dan loading.tsx.",
    tools=["Project Next.js dari lesson 1", "Browser DevTools (Network tab)"],
    outcomes=[
        "Fetch data di server component dengan `await`",
        "Mengontrol cache fetch (`no-store`, `revalidate`)",
        "Memakai `loading.tsx` untuk skeleton otomatis",
    ],
    tldr=(
        "Server component bisa `await fetch()` langsung. Default-nya hasil "
        "di-cache. Pakai `cache: 'no-store'` untuk data dinamis. "
        "`loading.tsx` otomatis muncul sambil halaman loading."
    ),
    pembuka=dedent(
        """\
        React biasa fetch data pakai `useEffect`. Banyak boilerplate: state untuk loading, untuk error, untuk data.

        Next.js App Router membuat ini jauh lebih sederhana. Server component bisa `await` data langsung di body — seperti tulis kode biasa.

        Lesson ini fokus ke pola data fetching modern, plus cara handle loading state dengan rapi.
        """
    ),
    penjelasan=dedent(
        """\
        ### Async server component

        Server component bisa `async`. Itu artinya kamu bisa `await` data langsung:

        ```tsx
        export default async function Page() {
          const res = await fetch("https://api.example.com/products");
          const products = await res.json();

          return (
            <ul>
              {products.map((p) => (
                <li key={p.id}>{p.name}</li>
              ))}
            </ul>
          );
        }
        ```

        Tidak ada `useState`, `useEffect`, loading state. Semua handled di server.

        ### Cache behavior

        Default Next.js men-cache hasil `fetch()`. Itu artinya call kedua dengan URL yang sama tidak hit network — instant.

        Tiga mode cache:

        - **Default (cache forever)**. Cocok untuk data yang jarang berubah (artikel blog, produk yang stabil).
        - **`cache: "no-store"`**. Selalu fetch fresh. Cocok untuk data dinamis (notifikasi, dashboard).
        - **`next: { revalidate: 60 }`**. Cache 60 detik, lalu refresh. Cocok untuk data yang berubah perlahan.

        ```tsx
        // Selalu fresh
        const res = await fetch(url, { cache: "no-store" });

        // Refresh setiap 60 detik
        const res = await fetch(url, { next: { revalidate: 60 } });

        // Cache forever (default)
        const res = await fetch(url);
        ```

        ### loading.tsx — skeleton otomatis

        Tambah file `loading.tsx` di folder yang sama dengan `page.tsx`:

        ```tsx
        // app/products/loading.tsx
        export default function Loading() {
          return (
            <div className="animate-pulse">
              <div className="h-8 w-1/3 rounded bg-gray-700" />
              <div className="mt-4 h-4 w-2/3 rounded bg-gray-700" />
              <div className="mt-2 h-4 w-1/2 rounded bg-gray-700" />
            </div>
          );
        }
        ```

        Saat halaman fetch data, Next.js otomatis tampilkan komponen ini sebagai placeholder. Tanpa kamu nulis state apapun.

        ### error.tsx — error UI

        Kalau data fetch gagal, kamu mau tampilan error yang ramah, bukan crash:

        ```tsx
        // app/products/error.tsx
        "use client";

        export default function ProductsError({ reset }) {
          return (
            <div>
              <h2>Ada error nih.</h2>
              <button onClick={reset}>Coba lagi</button>
            </div>
          );
        }
        ```

        `error.tsx` wajib client component karena butuh tombol retry.

        ### Pakai database langsung (Prisma)

        Kalau pakai database sendiri (bukan API publik):

        ```tsx
        import { db } from "@/lib/db";

        export default async function Page() {
          const products = await db.product.findMany({
            orderBy: { created_at: "desc" },
          });
          return <ProductList products={products} />;
        }
        ```

        Lebih cepat dari fetch karena tidak ada round-trip HTTP.

        ### Pararel fetch

        Kalau butuh dua data sekaligus:

        ```tsx
        export default async function Page() {
          // BURUK: sequential, total = a + b
          const a = await fetchA();
          const b = await fetchB();

          // BAIK: parallel, total = max(a, b)
          const [a, b] = await Promise.all([fetchA(), fetchB()]);

          return <div>...</div>;
        }
        ```

        `Promise.all` jalankan dua fetch bersamaan. Lebih cepat.
        """
    ),
    contoh_code_md=dedent(
        """\
        Halaman blog dengan loading state otomatis:

        ```tsx
        // app/blog/page.tsx
        async function getPosts() {
          const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
            next: { revalidate: 300 },  // refresh 5 menit
          });
          if (!res.ok) throw new Error("Gagal ambil post");
          return res.json();
        }

        export default async function BlogPage() {
          const posts = await getPosts();

          return (
            <main className="mx-auto max-w-3xl px-4 py-12">
              <h1 className="text-3xl font-semibold">Blog</h1>
              <ul className="mt-8 space-y-4">
                {posts.slice(0, 10).map((p) => (
                  <li key={p.id} className="rounded-lg border p-4">
                    <h2 className="font-semibold">{p.title}</h2>
                    <p className="mt-2 text-sm text-gray-400">
                      {p.body.substring(0, 120)}...
                    </p>
                  </li>
                ))}
              </ul>
            </main>
          );
        }
        ```

        ```tsx
        // app/blog/loading.tsx
        export default function Loading() {
          return (
            <main className="mx-auto max-w-3xl px-4 py-12">
              <div className="h-9 w-32 animate-pulse rounded bg-gray-800" />
              <div className="mt-8 space-y-4">
                {[1, 2, 3].map((i) => (
                  <div
                    key={i}
                    className="h-24 animate-pulse rounded-lg bg-gray-800"
                  />
                ))}
              </div>
            </main>
          );
        }
        ```

        Saat halaman fetch, `loading.tsx` muncul. Saat data siap, `page.tsx` menggantikan.
        """
    ),
    practice=(
        "Bikin halaman `/users` yang fetch dari "
        "`https://jsonplaceholder.typicode.com/users`. Tampilkan list 10 user "
        "(nama + email). Tambah `loading.tsx` di folder yang sama dengan "
        "skeleton placeholder. Coba refresh halaman — kamu harus lihat "
        "skeleton sebentar."
    ),
    fix_error={
        "language": "tsx",
        "broken_code": dedent(
            """\
            // app/dashboard/page.tsx
            "use client";

            import { useState, useEffect } from "react";

            export default function Dashboard() {
              const [stats, setStats] = useState(null);

              useEffect(() => {
                fetch("/api/stats")
                  .then((r) => r.json())
                  .then(setStats);
              }, []);

              if (!stats) return <p>Loading...</p>;
              return <div>{stats.users} users</div>;
            }
            """
        ),
        "hint": "Pendekatan ini bekerja, tapi bukan pola modern Next.js. Apa yang bisa lebih sederhana?",
        "answer_explanation": dedent(
            """\
            Kesalahan: pakai client component + `useEffect` padahal data tidak butuh interaksi.

            Pola lebih clean: pakai server component dengan `async`. Tidak butuh `useState`, `useEffect`, atau `'use client'`. Loading state bisa di-handle dengan `loading.tsx`.
            """
        ),
        "fixed_code": dedent(
            """\
            // app/dashboard/page.tsx (server component)
            export default async function Dashboard() {
              const res = await fetch("http://localhost:3000/api/stats");
              const stats = await res.json();

              return <div>{stats.users} users</div>;
            }

            // app/dashboard/loading.tsx
            export default function Loading() {
              return <p>Loading...</p>;
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa keuntungan async server component untuk data fetching?",
            [
                "Lebih lambat",
                "Bisa `await` langsung di body, tanpa `useState`/`useEffect`/loading state manual",
                "Cuma untuk static",
                "Tidak ada keuntungan",
            ],
            "B",
            "Server component punya superpower: fetch data langsung dengan `await`. Hemat boilerplate dan render lebih cepat.",
        ),
        q(
            "Apa fungsi `cache: 'no-store'` di fetch?",
            [
                "Tidak ada",
                "Memastikan data selalu fresh — bypass cache",
                "Cache forever",
                "Performance buruk",
            ],
            "B",
            "Default Next.js men-cache. `no-store` matikan cache, cocok untuk data dinamis seperti dashboard real-time.",
        ),
        q(
            "Apa yang terjadi saat ada `loading.tsx` di folder `app/products/`?",
            [
                "Tidak ada efek",
                "Komponen di file itu otomatis muncul sebagai placeholder saat halaman sedang fetch data",
                "Halaman crash",
                "Cuma untuk debug",
            ],
            "B",
            "Convention Next.js. Tidak butuh state apapun dari kamu. Loading muncul saat suspending, hilang saat ready.",
        ),
        q(
            "Mana cara fetch dua API SECARA PARALEL?",
            [
                "`const a = await fetchA(); const b = await fetchB();`",
                "`const [a, b] = await Promise.all([fetchA(), fetchB()]);`",
                "`fetchA(); fetchB();`",
                "`fetch.parallel([a, b])`",
            ],
            "B",
            "Pakai `Promise.all`. Tanpa itu, `await` jalan sequential — total waktu = waktu A + waktu B.",
        ),
        q(
            "Mengapa `error.tsx` HARUS client component?",
            [
                "Tidak harus",
                "Karena butuh tombol retry yang trigger `reset()` — interaktivitas hanya bisa di client",
                "Lebih cepat",
                "Aturan",
            ],
            "B",
            "Tombol retry adalah event handler. Event handler cuma bisa di client component.",
        ),
    ],
    common_mistakes=[
        "Pakai `useEffect` untuk fetch padahal halaman bisa server component.",
        "Lupa cek `res.ok` setelah fetch. Kode lanjut walau API balas error.",
        "Sequential `await` padahal bisa parallel dengan `Promise.all`.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Deploy ke Vercel (DEPLOY LESSON)
# ─────────────────────────────────────────────────────────────────────────────

LESSON_DEPLOY_VERCEL = make_lesson(
    title="Cara Deploy Project ke Internet (Vercel)",
    slug="deploy-ke-vercel",
    order_index=4,
    read_time="14 menit",
    summary="Dari project di laptop, jadi link yang bisa dibuka siapa saja.",
    tools=["Akun GitHub", "Akun Vercel", "Project Next.js dari lesson 1-3"],
    outcomes=[
        "Memahami apa itu deploy dan kenapa penting",
        "Push project ke GitHub",
        "Deploy ke Vercel dan dapat URL publik",
        "Update project setelah deploy (auto-redeploy)",
    ],
    tldr=(
        "Deploy = upload project ke server di internet supaya bisa diakses "
        "siapa saja. Stack untuk Next.js: GitHub untuk simpan kode + Vercel "
        "untuk hosting. Setiap kali push ke GitHub, Vercel otomatis update."
    ),
    pembuka=dedent(
        """\
        Sampai sekarang, project kamu cuma jalan di `localhost:3000`. Itu artinya cuma kamu yang bisa buka, di laptop kamu.

        Banyak pemula heran: "Kok teman saya tidak bisa buka link saya?" Jawabannya: project itu masih di laptop kamu, belum di internet.

        Lesson ini cara mengubah itu. Setelah selesai, kamu punya URL yang bisa kamu kasih ke siapa saja, di HP atau laptop manapun.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu deploy

        Deploy artinya **mengupload project kamu ke komputer lain yang nyala 24 jam dan tersambung ke internet**. Komputer itu disebut **server**.

        Bayangkan begini:

        - Project di laptop kamu = warung makan di rumah kamu. Cuma kamu dan tamu yang ke rumah yang bisa makan.
        - Project di server = warung makan di pinggir jalan. Siapa saja yang lewat bisa mampir.

        Saat kamu deploy, project kamu "pindah" ke pinggir jalan internet. Setiap orang dengan link bisa buka.

        ### Beda local vs live

        - **Local** (di laptop kamu): URL `localhost:3000`. Cuma jalan kalau laptop nyala dan kamu running `npm run dev`. Cuma bisa diakses dari laptop kamu sendiri.
        - **Live** (di server internet): URL seperti `nama-project.vercel.app` atau domain custom. Jalan 24 jam, siapa saja bisa akses dari mana saja.

        ### Kenapa harus pakai Vercel

        Untuk Next.js, Vercel adalah pilihan terbaik. Alasan:

        - Vercel dibuat oleh tim yang juga bikin Next.js.
        - Free tier sangat besar untuk hobi dan portfolio.
        - Deploy otomatis setiap kamu push ke GitHub.
        - SSL (HTTPS) gratis dan otomatis.
        - Setup awalnya literally beberapa klik.

        Alternatif lain: Netlify (juga bagus), Railway (untuk backend), Render. Tapi untuk Next.js, Vercel paling streamlined.

        ### Step 1 — Push project ke GitHub

        Vercel deploy dari GitHub repo. Jadi kode kamu wajib ada di GitHub dulu.

        Buka terminal di folder project:

        ```bash
        # Inisialisasi Git (kalau belum)
        git init
        git add .
        git commit -m "init: project pertama"
        ```

        Buka [github.com/new](https://github.com/new). Isi:

        - Repository name: `my-portfolio` (atau apa saja)
        - Public atau Private (boleh public untuk portfolio)
        - JANGAN centang "Add README" (project sudah punya isi)

        Klik Create. GitHub kasih instruksi:

        ```bash
        git remote add origin https://github.com/USERNAME/my-portfolio.git
        git branch -M main
        git push -u origin main
        ```

        Salin perintah itu, paste di terminal. Refresh halaman GitHub — kode kamu harus muncul.

        ### Step 2 — Connect Vercel ke GitHub

        Buka [vercel.com](https://vercel.com), klik **Sign Up**. Pilih **Continue with GitHub**.

        Vercel akan minta izin akses ke akun GitHub kamu. Klik Authorize.

        Setelah masuk, kamu lihat dashboard Vercel kosong.

        ### Step 3 — Import project

        Klik tombol **Add New → Project**. Vercel tampilkan list repo GitHub kamu.

        Cari `my-portfolio`, klik **Import**.

        Vercel otomatis deteksi: "Oh ini Next.js project". Settings default sudah benar.

        Klik **Deploy**.

        Tunggu 30-60 detik. Vercel sedang:

        1. Download kode dari GitHub.
        2. Run `npm install` (install dependencies).
        3. Run `npm run build` (build production).
        4. Upload hasil build ke server mereka.

        Selesai! Kamu dapat URL `my-portfolio.vercel.app`. Klik buat buka.

        ### Step 4 — Cek live URL

        Buka URL di browser. Halaman kamu live.

        Lebih hebat: kasih URL ke teman lewat WhatsApp. Mereka bisa buka di HP mereka, dari mana saja di Indonesia atau dunia. Itulah yang dimaksud "live di internet".

        ### Step 5 — Update project setelah deploy

        Mau ubah text di homepage? Edit di laptop, lalu push:

        ```bash
        git add .
        git commit -m "fix: ganti tagline hero"
        git push
        ```

        Vercel deteksi push baru. Otomatis re-build dan re-deploy. Sekitar 30-60 detik kemudian, URL kamu sudah update.

        Kamu tidak perlu klik apapun di Vercel. Workflow ini disebut **continuous deployment**.

        ### Custom domain (opsional)

        URL `my-portfolio.vercel.app` panjang. Kalau punya domain sendiri (misal `acel.dev`):

        - Beli domain di [Niagahoster](https://www.niagahoster.co.id) atau [Namecheap](https://www.namecheap.com).
        - Di Vercel: Project → Settings → Domains → Add. Masukkan domain kamu.
        - Vercel kasih instruksi DNS. Salin ke panel domain provider.
        - Tunggu 5-30 menit, domain aktif. SSL otomatis.

        Total cost: domain ~Rp 150rb/tahun. Hosting tetap gratis.

        ### Kalau build error

        Sering kejadian: deploy gagal padahal di laptop jalan.

        Penyebab paling umum:

        - **Environment variable tidak ada di Vercel**. Edit di Project Settings → Environment Variables.
        - **TypeScript error yang di-ignore di dev**. Vercel build strict, harus fix.
        - **File tidak di-commit ke Git**. Cek `git status`, push file yang ketinggalan.

        Cek logs di Vercel (klik deploy yang gagal → Logs). Pesan error spesifik biasanya jelas.
        """
    ),
    contoh_code_md=dedent(
        """\
        Setup awal Git untuk project baru:

        ```bash
        # Di root project
        git init
        echo "node_modules" > .gitignore
        echo ".env.local" >> .gitignore
        echo ".next" >> .gitignore

        git add .
        git commit -m "init: setup project Next.js"
        ```

        Push ke GitHub repo baru:

        ```bash
        git remote add origin https://github.com/USERNAME/REPO.git
        git branch -M main
        git push -u origin main
        ```

        Workflow harian setelah deploy:

        ```bash
        # Setelah edit kode di laptop
        git add .
        git commit -m "feat: tambah halaman about"
        git push

        # Vercel auto-deploy. Cek di vercel.com/dashboard.
        ```
        """
    ),
    practice=(
        "Push project Next.js dari lesson sebelumnya ke GitHub. Lalu import "
        "ke Vercel dan deploy. Salin URL Vercel. Kirim URL itu ke minimal "
        "satu teman lewat chat — pastikan mereka bisa buka di HP. Setelah "
        "itu, edit satu kata di homepage, commit, push, dan tunggu auto-redeploy."
    ),
    fix_error={
        "language": "bash",
        "broken_code": dedent(
            """\
            # User report:
            "Saya sudah deploy ke Vercel, tapi halaman blank putih.
            Logs Vercel bilang: 'Error: NEXT_PUBLIC_API_URL is not defined'."
            """
        ),
        "hint": "Project di laptop pakai file `.env.local`. File itu tidak ke-push ke GitHub karena di-gitignore. Lalu di Vercel?",
        "answer_explanation": dedent(
            """\
            Penyebab: env variable di `.env.local` cuma jalan di laptop kamu. File itu sengaja di-gitignore supaya rahasia (misal API key) tidak bocor ke GitHub.

            Saat deploy ke Vercel, kamu harus tambahkan env variable secara terpisah di Vercel.

            Solusi:

            1. Buka Vercel dashboard → project kamu.
            2. Settings → Environment Variables.
            3. Tambah satu per satu yang ada di `.env.local`.
            4. Klik Save. Re-deploy (klik tombol di tab Deployments).

            Setelah itu halaman akan jalan normal.
            """
        ),
        "fixed_code": dedent(
            """\
            # Di Vercel: Settings → Environment Variables

            Name:  NEXT_PUBLIC_API_URL
            Value: https://api.example.com
            Environments: Production, Preview, Development (centang semua)

            # Klik Save, lalu di tab Deployments → Redeploy.
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dimaksud 'deploy' project?",
            [
                "Menyimpan project di Google Drive",
                "Mengupload project ke server yang nyala 24 jam supaya bisa diakses siapa saja lewat URL publik",
                "Menjalankan `npm run dev`",
                "Membuat backup",
            ],
            "B",
            "Deploy = pindah project dari laptop kamu ke server di internet. Itu yang membedakan 'localhost' dengan 'live'.",
        ),
        q(
            "Kenapa teman tidak bisa buka URL `localhost:3000` yang kamu kirim?",
            [
                "URL salah ketik",
                "`localhost` artinya 'komputer ini sendiri' — cuma device yang menjalankan project yang bisa akses",
                "Internet putus",
                "Wajib pakai HTTPS",
            ],
            "B",
            "`localhost` adalah loopback ke device sendiri. Tidak ada cara teman akses dari laptop atau HP mereka tanpa deploy.",
        ),
        q(
            "Setelah project di-push ke GitHub dan di-deploy ke Vercel, apa yang terjadi saat kamu push lagi?",
            [
                "Tidak ada",
                "Vercel deteksi push baru dan otomatis re-deploy ke URL yang sama",
                "Vercel hapus project lama",
                "Kamu harus deploy manual lagi",
            ],
            "B",
            "Continuous deployment: GitHub-Vercel connection bikin push baru = redeploy otomatis. Workflow super cepat.",
        ),
        q(
            "Apa yang HARUS di-update di Vercel kalau project kamu pakai `.env.local`?",
            [
                "Tidak ada",
                "Tambahkan env variable yang sama di Vercel Settings → Environment Variables",
                "Push `.env.local` ke GitHub",
                "Hapus `.env.local`",
            ],
            "B",
            "`.env.local` di-gitignore (sengaja) supaya tidak bocor. Vercel butuh value-nya dimasukkan terpisah lewat dashboard.",
        ),
        q(
            "Apa keuntungan utama deploy ke Vercel untuk Next.js?",
            [
                "Vercel dibuat oleh tim Next.js, free tier besar, auto-deploy dari GitHub, SSL gratis",
                "Lebih lambat dari hosting lain",
                "Wajib bayar dari hari pertama",
                "Tidak ada keuntungan",
            ],
            "A",
            "Vercel dirancang khusus untuk Next.js. Setup deploy yang biasanya ribet jadi click-click di dashboard mereka.",
        ),
    ],
    common_mistakes=[
        "Push `.env.local` ke GitHub. API key bocor — siapa saja yang lihat repo bisa pakai.",
        "Lupa tambah env variable di Vercel. Halaman live blank atau crash.",
        "Test cuma di laptop sendiri. Tidak buka URL Vercel di HP teman untuk konfirm akses publik.",
    ],
    xp_reward=180,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 5 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_DASHBOARD = make_lesson(
    title="Mini Project — Dashboard Mini dengan Next.js",
    slug="mini-project-dashboard",
    order_index=5,
    read_time="180 menit",
    summary="Dashboard dengan multi-page, data fetching server, dan deploy live.",
    tools=["Next.js + Tailwind", "Cursor / VS Code", "GitHub", "Vercel"],
    outcomes=[
        "Membangun multi-page Next.js app",
        "Mengkombinasikan server dan client component dengan benar",
        "Deploy production-ready ke Vercel",
    ],
    tldr=(
        "Bangun dashboard 3 halaman: Overview (stats), Users (table), "
        "Settings (form). Data dari `data/*.ts`. Server component untuk "
        "halaman, client component untuk form/filter. Deploy ke Vercel."
    ),
    pembuka=dedent(
        """\
        Saatnya kombinasikan semua yang dipelajari di Level 4: struktur Next.js, server vs client component, data fetching, dan deploy.

        Hasilnya: dashboard yang terstruktur seperti app SaaS kecil. Cocok masuk portfolio.

        Ini bukan tutorial step-by-step. Ini spec dengan kebebasan eksekusi — yang penting hasilnya match dengan checklist.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind. Data hardcode di `src/data/*.ts` (tidak butuh database dulu).

        Halaman:

        - `/` — Overview. Stats card (4 angka: Revenue, Users, Orders, Bounce). Recent activity (5 item).
        - `/users` — Users page. Table dengan 10 user dummy. Search input di atas (client component).
        - `/settings` — Settings page. Form profile + theme toggle. Dummy save (alert "Tersimpan").

        Layout persistent:

        - Sidebar di kiri dengan link ke 3 halaman.
        - Header di atas dengan judul halaman + avatar.

        ### Aturan teknis

        - Sidebar adalah server component yang import data nav dari `data/nav.ts`.
        - Search di `/users` adalah client component yang filter data dari prop.
        - Form di `/settings` adalah client component (butuh state).
        - Stats card di `/` boleh server component (data static).
        - Pakai shadcn/ui boleh, atau Tailwind murni.

        ### Polish checklist

        - Active nav state (link halaman aktif terlihat beda).
        - Hover state di setiap link.
        - Empty state di table jika search tidak ada hasil.
        - Loading skeleton di salah satu halaman (pakai `loading.tsx`).
        - Responsive: sidebar collapse di mobile.

        ### Deploy

        - Push ke GitHub.
        - Import ke Vercel.
        - URL publik bisa dibuka.

        ### Submit

        Bagikan URL Vercel ke minimal satu teman. Tanya kesan pertama mereka.
        """
    ),
    contoh_code_md=dedent(
        """\
        Sketsa data file:

        ```ts
        // src/data/users.ts
        export type User = {
          id: string;
          name: string;
          email: string;
          role: "admin" | "member" | "viewer";
          joined: string;
        };

        export const users: User[] = [
          { id: "1", name: "Acel", email: "acel@email.com", role: "admin", joined: "2026-01-15" },
          { id: "2", name: "Budi", email: "budi@email.com", role: "member", joined: "2026-02-03" },
          // tambahkan 8 lagi
        ];
        ```

        ```tsx
        // src/app/users/page.tsx (server)
        import { users } from "@/data/users";
        import UserSearch from "./UserSearch";

        export default function UsersPage() {
          return (
            <main>
              <h1 className="text-2xl font-semibold">Users</h1>
              <UserSearch users={users} />
            </main>
          );
        }
        ```

        ```tsx
        // src/app/users/UserSearch.tsx (client)
        "use client";

        import { useState } from "react";
        import type { User } from "@/data/users";

        export default function UserSearch({ users }: { users: User[] }) {
          const [query, setQuery] = useState("");

          const filtered = users.filter(
            (u) =>
              u.name.toLowerCase().includes(query.toLowerCase()) ||
              u.email.toLowerCase().includes(query.toLowerCase()),
          );

          return (
            <div>
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Cari user..."
                className="w-full rounded border px-4 py-2"
              />

              {filtered.length === 0 ? (
                <p className="mt-6 text-gray-400">Tidak ada hasil.</p>
              ) : (
                <table className="mt-6 w-full text-left text-sm">
                  <thead>
                    <tr>
                      <th>Nama</th>
                      <th>Email</th>
                      <th>Role</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filtered.map((u) => (
                      <tr key={u.id}>
                        <td>{u.name}</td>
                        <td>{u.email}</td>
                        <td>{u.role}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          );
        }
        ```
        """
    ),
    practice=(
        "Bangun dashboard sesuai spec. Total waktu sekitar 6-8 jam, pecah "
        "ke 3-4 sesi. Setelah live di Vercel, share URL ke teman dan tanya "
        "feedback. Update sesuai feedback paling tajam."
    ),
    fix_error={
        "language": "tsx",
        "broken_code": dedent(
            """\
            // src/app/users/page.tsx
            "use client";

            import { useState, useEffect } from "react";

            export default function UsersPage() {
              const [users, setUsers] = useState([]);
              const [query, setQuery] = useState("");

              useEffect(() => {
                import("@/data/users").then((m) => setUsers(m.users));
              }, []);

              return <div>{users.length} users</div>;
            }
            """
        ),
        "hint": "Halaman ini bisa lebih clean. Apa yang tidak perlu jadi client component?",
        "answer_explanation": dedent(
            """\
            Kesalahan: seluruh halaman jadi client component, padahal data static (import dari file lokal). Tidak butuh `useState` atau `useEffect` untuk load data static.

            Solusi: page sebagai server component yang import data langsung. Pisahkan bagian search ke client component sendiri.
            """
        ),
        "fixed_code": dedent(
            """\
            // src/app/users/page.tsx (server)
            import { users } from "@/data/users";
            import UserSearch from "./UserSearch";

            export default function UsersPage() {
              return (
                <main>
                  <h1>Users ({users.length})</h1>
                  <UserSearch users={users} />
                </main>
              );
            }

            // src/app/users/UserSearch.tsx (client)
            "use client";

            import { useState } from "react";

            export default function UserSearch({ users }) {
              const [query, setQuery] = useState("");
              // ... filter & render
            }
            """
        ),
    },
    quiz=[
        q(
            "Mana kombinasi yang BAIK untuk halaman dengan data + filter?",
            [
                "Semua client component dengan useEffect",
                "Page sebagai server component yang import data, lalu kasih ke client component untuk filter UI",
                "Page sebagai client component dengan fetch dari API",
                "Tidak penting",
            ],
            "B",
            "Pola 'page server + island client' = data fast load di server, interaksi (filter) di client. Kombinasi optimal.",
        ),
        q(
            "Apa fungsi `loading.tsx` di folder halaman?",
            [
                "Tidak ada efek",
                "Otomatis muncul sebagai placeholder saat halaman sedang fetch data",
                "Cuma untuk debug",
                "Wajib di setiap folder",
            ],
            "B",
            "Convention Next.js. Bonus UX tanpa nulis state apa pun.",
        ),
        q(
            "Apa yang HARUS dilakukan setelah dashboard selesai di lokal?",
            [
                "Tunggu sempurna baru deploy",
                "Push ke GitHub, deploy ke Vercel, share URL ke teman",
                "Email file zip ke recruiter",
                "Tidak deploy",
            ],
            "B",
            "Filosofi 'live first, polish later'. URL publik = portfolio item.",
        ),
        q(
            "Saat search di `/users` tidak ada hasil, apa yang harus ditampilkan?",
            [
                "Halaman blank",
                "Empty state dengan pesan jelas seperti 'Tidak ada hasil.'",
                "Crash",
                "Error message",
            ],
            "B",
            "Empty state yang ramah membantu user paham. Halaman blank = bug experience.",
        ),
        q(
            "Mana checklist final untuk dashboard yang siap di-share?",
            [
                "URL Vercel publik aktif, responsive di HP, active nav state, empty state, repo GitHub punya README",
                "Cuma URL aktif",
                "Animasi banyak",
                "Logo besar",
            ],
            "A",
            "Polish detail kecil = professional. Setiap item di checklist berkontribusi ke kesan keseluruhan.",
        ),
    ],
    common_mistakes=[
        "Seluruh halaman jadi client component padahal data static.",
        "Tidak ada empty state di table search.",
        "Sidebar tidak responsive — di HP terlihat berantakan.",
    ],
    xp_reward=400,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=4,
    slug="real-project-nextjs",
    title="Real Project (Next.js)",
    subtitle="Build seperti developer beneran",
    description=(
        "Project nyata dengan struktur Next.js modern. Server component, "
        "data fetching, deploy ke Vercel. Tutup level dengan dashboard "
        "multi-page yang live di internet."
    ),
    duration="~3 minggu",
    difficulty="Menengah",
    accent_color="from-emerald-400/30 to-violet-500/10",
    mini_project="Dashboard Mini dengan Next.js",
    tags=["Next.js", "App Router", "Server Component", "Deploy"],
    lessons=[
        LESSON_STRUKTUR,
        LESSON_SVR_CLIENT,
        LESSON_FETCH,
        LESSON_DEPLOY_VERCEL,
        PROJECT_DASHBOARD,
    ],
)
