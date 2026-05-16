"""
Frontend / Level 3 — React & Tailwind.

Lessons:
  1. pengenalan-react
  2. state-dan-hooks
  3. tailwind-untuk-react
  4. mini-project-portfolio-react  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Pengenalan React
# ─────────────────────────────────────────────────────────────────────────────

LESSON_REACT_INTRO = make_lesson(
    title="Pengenalan React",
    slug="pengenalan-react",
    order_index=1,
    read_time="14 menit",
    summary="Component, JSX, props, dan cara berpikir React.",
    tools=["Node.js LTS", "VS Code", "Browser modern"],
    outcomes=[
        "Setup project React baru dengan Vite",
        "Menulis component dengan JSX",
        "Mengirim data lewat props",
        "Memecah UI jadi bagian kecil yang reusable",
    ],
    tldr=(
        "React = UI library berbasis component. JSX itu HTML di dalam JS. "
        "Component fungsinya seperti lego — nulis sekali, pakai berkali-kali. "
        "Kirim data antar component pakai props."
    ),
    pembuka=dedent(
        """\
        Bayangkan kamu bikin website dengan 100 tombol yang tampilannya sama tapi isinya beda.

        Dengan HTML biasa, kamu harus tulis `<button>` 100 kali. Lelah. Salah satu, harus fix di 100 tempat.

        Dengan React, kamu tulis `Button` sekali — pakai 100 kali dengan props yang berbeda. Itu inti React.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu React

        React adalah library JavaScript untuk bangun UI. Buatan Facebook, sekarang dipakai Instagram, Netflix, Airbnb, dan ratusan ribu app lain.

        Ide utamanya: UI dipecah jadi **component** — potongan kecil yang berdiri sendiri. Tiap component punya tampilan dan logikanya sendiri.

        ### Setup project pertama dengan Vite

        Vite adalah bundler modern yang cepat. Buka terminal di folder kosong:

        ```bash
        npm create vite@latest portfolio -- --template react
        cd portfolio
        npm install
        npm run dev
        ```

        Buka `http://localhost:5173`. Kamu sudah punya project React yang jalan.

        ### JSX — HTML di dalam JavaScript

        Buka `src/App.jsx`. Kamu akan lihat sesuatu seperti ini:

        ```jsx
        function App() {
          return (
            <div>
              <h1>Halo React!</h1>
              <p>Ini component pertama saya.</p>
            </div>
          );
        }
        ```

        Itu JSX. Kelihatan seperti HTML, tapi sebenarnya ditulis di dalam JavaScript. Bedanya:

        - `class` jadi `className` (karena `class` keyword JavaScript).
        - `for` (di label) jadi `htmlFor`.
        - Tag self-closing wajib slash, misal `<img />`, bukan `<img>`.
        - Bisa sisipkan JS pakai kurung kurawal `{ }`.

        ### Component itu cuma function

        Component React adalah function yang return JSX. Aturannya:

        - Nama component **harus diawali huruf kapital** (`Card`, `Button`, `Hero`).
        - Cuma boleh return **satu** root element. Kalau butuh lebih, bungkus dengan `<>...</>` (Fragment).

        ```jsx
        function Card() {
          return (
            <div>
              <h2>Halo</h2>
              <p>Saya component pertama.</p>
            </div>
          );
        }
        ```

        Pakai dengan `<Card />` di component lain.

        ### Props — kirim data antar component

        Component sering butuh data dari luar. Kamu kirim lewat **props** seperti atribut HTML.

        ```jsx
        function Card({ judul, deskripsi }) {
          return (
            <div className="card">
              <h2>{judul}</h2>
              <p>{deskripsi}</p>
            </div>
          );
        }

        function App() {
          return (
            <main>
              <Card judul="Halo" deskripsi="Component reusable" />
              <Card judul="Lagi" deskripsi="Pakai berkali-kali" />
            </main>
          );
        }
        ```

        Notasi `{ judul, deskripsi }` itu **destructuring** — ambil property dari object yang masuk.

        ### Cara berpikir React

        Lupakan dulu kebiasaan "ambil elemen, ubah pakai DOM". Ganti dengan:

        - **Pecah UI jadi component kecil.** Hero, Card, Button, Navbar — masing-masing satu file.
        - **Data mengalir top-down.** Parent component kirim props ke child, bukan sebaliknya.
        - **JSX itu deskriptif.** Kamu mendeskripsikan tampilan akhir, React yang urus DOM.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card list dengan props dan array map:

        ```jsx
        // src/components/Card.jsx
        function Card({ judul, deskripsi, link }) {
          return (
            <article className="card">
              <h3>{judul}</h3>
              <p>{deskripsi}</p>
              <a href={link}>Pelajari →</a>
            </article>
          );
        }

        export default Card;
        ```

        ```jsx
        // src/App.jsx
        import Card from "./components/Card";

        const projects = [
          { judul: "Toko Kopi", deskripsi: "Landing page kopi lokal", link: "#" },
          { judul: "Todo App", deskripsi: "Latihan state management", link: "#" },
          { judul: "Portfolio", deskripsi: "Site pribadi pertama", link: "#" },
        ];

        function App() {
          return (
            <main>
              <h1>Project saya</h1>
              {projects.map((p) => (
                <Card
                  key={p.judul}
                  judul={p.judul}
                  deskripsi={p.deskripsi}
                  link={p.link}
                />
              ))}
            </main>
          );
        }

        export default App;
        ```

        Kunci: `key` di tiap item. React butuh ini untuk track tiap item secara unik.
        """
    ),
    practice=(
        "Buat component `Profile` yang menerima props `nama`, `role`, dan "
        "`bio`. Pakai di `App.jsx` dua kali dengan data berbeda. Tampilannya "
        "boleh sederhana — fokus dulu pada cara kirim data lewat props."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            function card(props) {
              return (
                <div class="card">
                  <h2>{props.judul}</h2>
                  <p>{props.deskripsi}</p>
                </div>
                <p>Catatan kecil</p>
              );
            }

            export default card;
            """
        ),
        "hint": (
            "Tiga masalah: penamaan component, atribut JSX, dan jumlah root element."
        ),
        "answer_explanation": dedent(
            """\
            1. Nama component HARUS diawali huruf kapital: `Card`, bukan `card`. Lowercase dianggap HTML tag biasa.
            2. JSX pakai `className`, bukan `class`. `class` itu keyword JavaScript.
            3. Component cuma boleh return satu root element. Bungkus pakai Fragment `<>...</>` atau `<div>` jika butuh dua atau lebih siblings.
            """
        ),
        "fixed_code": dedent(
            """\
            function Card(props) {
              return (
                <>
                  <div className="card">
                    <h2>{props.judul}</h2>
                    <p>{props.deskripsi}</p>
                  </div>
                  <p>Catatan kecil</p>
                </>
              );
            }

            export default Card;
            """
        ),
    },
    quiz=[
        q(
            "Apa nama tempat menulis HTML di dalam JavaScript di React?",
            ["HTMX", "JSX", "TSX-only", "Mustache"],
            "B",
            "JSX (JavaScript XML) adalah ekstensi sintaks yang memungkinkan menulis tag mirip HTML di dalam JavaScript.",
        ),
        q(
            "Kenapa nama component WAJIB diawali huruf kapital?",
            [
                "Untuk estetika",
                "Karena nama lowercase dianggap HTML tag biasa oleh React",
                "Karena diwajibkan ECMAScript",
                "Tidak wajib, opsional",
            ],
            "B",
            "React membedakan component dari HTML tag lewat huruf kapital. `<Card />` dianggap component, `<card />` dianggap HTML.",
        ),
        q(
            "Cara mengirim data dari parent ke child component?",
            ["Pakai global variable", "Lewat props", "Lewat localStorage", "Pakai cookies"],
            "B",
            "Props adalah cara standar mengirim data top-down dari parent ke child di React.",
        ),
        q(
            "Apa beda `className` dengan `class` di JSX?",
            [
                "Tidak ada beda",
                "JSX pakai `className` karena `class` adalah keyword JavaScript",
                "`className` lebih lambat",
                "`class` cuma untuk TypeScript",
            ],
            "B",
            "`class` di JavaScript dipakai untuk class declaration. JSX pakai `className` agar tidak bentrok.",
        ),
        q(
            "Apa fungsi prop `key` saat render list dengan `.map()`?",
            [
                "Untuk styling",
                "Untuk membantu React mengenali item secara unik saat list berubah",
                "Tidak ada fungsi, opsional",
                "Untuk login",
            ],
            "B",
            "`key` membantu React men-track tiap item. Tanpa key (atau key yang sama), React bisa keliru saat update list — re-render jadi tidak efisien.",
        ),
    ],
    common_mistakes=[
        "Pakai `class` bukan `className`. Browser tetap render, tapi React kasih warning.",
        "Lupa `key` saat `.map()`. List tetap muncul, tapi update bisa aneh.",
        "Return dua sibling tanpa Fragment. Error: 'Adjacent JSX elements must be wrapped'.",
    ],
    checkpoint=[
        "Bisa setup project React baru dengan Vite.",
        "Bisa buat component dan pakai di parent.",
        "Bisa kirim data lewat props dan render list dengan `.map()`.",
        "Tahu kapan butuh Fragment.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — State & Hooks
# ─────────────────────────────────────────────────────────────────────────────

LESSON_STATE = make_lesson(
    title="State & Hooks",
    slug="state-dan-hooks",
    order_index=2,
    read_time="16 menit",
    summary="useState, useEffect, conditional rendering, dan event di React.",
    tools=["Project React + Vite dari lesson 1", "Browser DevTools"],
    outcomes=[
        "Memakai `useState` untuk data yang berubah",
        "Memakai `useEffect` untuk side effect",
        "Conditional rendering dan event handler",
    ],
    tldr=(
        "State = kondisi sekarang component. Pakai `useState` untuk data "
        "berubah, `useEffect` untuk side effect (fetch, timer, listener). "
        "Update state = component re-render."
    ),
    pembuka=dedent(
        """\
        Sampai sini component kamu masih statis. Saatnya kasih dia kondisi yang bisa berubah.

        Bayangkan tombol yang menampilkan jumlah klik. Counternya berubah, dan halaman ikut update.

        Itulah yang disebut state. Dan cara React mengelolanya disebut hooks.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu state

        State adalah data yang **dimiliki component** dan bisa berubah seiring waktu.

        Saat state berubah, React otomatis re-render component itu. Kamu tidak perlu manipulasi DOM manual.

        ### useState — hook pertama

        `useState` mengembalikan dua hal: nilai sekarang dan function untuk update.

        ```jsx
        import { useState } from "react";

        function Counter() {
          const [count, setCount] = useState(0);

          return (
            <div>
              <p>Klik: {count}</p>
              <button onClick={() => setCount(count + 1)}>Tambah</button>
            </div>
          );
        }
        ```

        Notasi `[count, setCount]` itu array destructuring. Convention-nya nama setter pakai prefix `set`.

        Setiap kali `setCount` dipanggil, React re-render component dengan nilai baru.

        ### Aturan penting

        - **Jangan ubah state langsung.** Salah: `count = count + 1`. Benar: `setCount(count + 1)`.
        - **State bersifat asynchronous.** Kalau update beberapa kali sekaligus, pakai callback: `setCount(prev => prev + 1)`.
        - **Hooks cuma dipanggil di top level component.** Jangan di dalam if, loop, atau function nested.

        ### Event handling

        Mirip JavaScript biasa, tapi camelCase: `onClick`, `onChange`, `onSubmit`.

        ```jsx
        function Form() {
          const [nama, setNama] = useState("");

          return (
            <form onSubmit={(e) => {
              e.preventDefault();
              alert(`Halo, ${nama}!`);
            }}>
              <input
                value={nama}
                onChange={(e) => setNama(e.target.value)}
                placeholder="Nama kamu"
              />
              <button type="submit">Kirim</button>
            </form>
          );
        }
        ```

        Pola input + state ini disebut **controlled component** — input sepenuhnya dikontrol React.

        ### Conditional rendering

        Kalau mau tampilkan UI berbeda berdasarkan state:

        ```jsx
        {isLogin ? <Dashboard /> : <LoginForm />}
        {error && <p className="error">{error}</p>}
        ```

        Operator ternary untuk dua kemungkinan. `&&` untuk render kalau true.

        ### useEffect — side effect

        Kalau butuh ngerjain sesuatu di luar render (fetch data, set timer, pasang listener), pakai `useEffect`.

        ```jsx
        import { useState, useEffect } from "react";

        function Clock() {
          const [time, setTime] = useState(new Date());

          useEffect(() => {
            const id = setInterval(() => setTime(new Date()), 1000);
            return () => clearInterval(id); // cleanup
          }, []);

          return <p>{time.toLocaleTimeString()}</p>;
        }
        ```

        Argumen kedua `[]` adalah dependency array:

        - `[]` jalan **sekali** saat component pertama mount.
        - `[var]` jalan saat `var` berubah.
        - Tanpa array, jalan **setiap render** (jarang dipakai).

        Function yang di-return adalah cleanup, jalan saat component unmount.
        """
    ),
    contoh_code_md=dedent(
        """\
        Toggle dark mode + counter dalam satu component:

        ```jsx
        import { useState } from "react";

        function App() {
          const [count, setCount] = useState(0);
          const [dark, setDark] = useState(false);

          return (
            <div className={dark ? "app dark" : "app"}>
              <button onClick={() => setDark(!dark)}>
                {dark ? "☀️ Light" : "🌙 Dark"}
              </button>

              <h1>Counter: {count}</h1>

              <button onClick={() => setCount(count + 1)}>+1</button>
              <button onClick={() => setCount((prev) => prev - 1)}>-1</button>
              <button onClick={() => setCount(0)}>Reset</button>

              {count > 5 && <p>Kamu sudah klik banyak banget!</p>}
            </div>
          );
        }

        export default App;
        ```

        Perhatikan: `setCount((prev) => prev - 1)` versi callback — aman saat ada beberapa update beruntun.
        """
    ),
    practice=(
        "Buat component `LoginForm` dengan dua input (email, password) yang "
        "controlled. Pasang tombol 'Login'. Saat submit, tampilkan pesan "
        "'Halo, [email]!' dan kosongkan password. Pakai `useState` dan "
        "`onSubmit`."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            import { useState } from "react";

            function Counter() {
              let count = 0;

              function tambah() {
                count = count + 1;
              }

              return (
                <div>
                  <p>{count}</p>
                  <button onClick={tambah}>+</button>
                </div>
              );
            }
            """
        ),
        "hint": (
            "Tampilan tidak update saat tombol diklik. Perhatikan cara "
            "menyimpan dan mengubah `count`."
        ),
        "answer_explanation": dedent(
            """\
            Kesalahan: `count` ditulis sebagai `let` biasa. React tidak tahu data ini berubah, jadi tidak re-render.

            Solusi: pakai `useState`. Update dengan `setCount`, jangan assign langsung.
            """
        ),
        "fixed_code": dedent(
            """\
            import { useState } from "react";

            function Counter() {
              const [count, setCount] = useState(0);

              return (
                <div>
                  <p>{count}</p>
                  <button onClick={() => setCount(count + 1)}>+</button>
                </div>
              );
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dikembalikan `useState`?",
            [
                "Single value",
                "Array dengan dua elemen: nilai sekarang dan function untuk update",
                "Object",
                "Promise",
            ],
            "B",
            "`useState(initial)` mengembalikan `[value, setValue]`. Ini array destructuring.",
        ),
        q(
            "Mana cara yang BENAR update state?",
            [
                "`count = count + 1`",
                "`setCount(count + 1)`",
                "`useState(count + 1)`",
                "`document.querySelector` lalu ubah",
            ],
            "B",
            "State HARUS di-update lewat setter (`setCount`). Assign langsung tidak trigger re-render.",
        ),
        q(
            "Kapan callback `useEffect` dengan `[]` dijalankan?",
            [
                "Setiap render",
                "Sekali saat component pertama mount",
                "Tidak pernah",
                "Saat user logout",
            ],
            "B",
            "Dependency array kosong `[]` artinya 'jalan sekali saat mount, tidak peduli render selanjutnya'.",
        ),
        q(
            "Apa yang terjadi kalau kamu return function dari useEffect?",
            [
                "Error",
                "Function itu jadi cleanup — dipanggil saat component unmount atau effect dijalankan ulang",
                "Function dieksekusi tiap detik",
                "Tidak ada efek",
            ],
            "B",
            "Cleanup function ideal untuk `clearInterval`, `removeEventListener`, atau abort request — supaya tidak ada memory leak.",
        ),
        q(
            "Mana cara yang AMAN saat update state berdasarkan nilai sebelumnya?",
            [
                "`setCount(count + 1)` di dua tempat berturut-turut",
                "`setCount(prev => prev + 1)` versi callback",
                "Tidak ada bedanya",
                "Pakai global variable",
            ],
            "B",
            "Update beruntun dengan `setCount(count + 1)` bisa miss karena state asynchronous. Versi callback `prev => prev + 1` selalu pakai nilai terbaru.",
        ),
    ],
    common_mistakes=[
        "Update state pakai `=` langsung. Component tidak re-render.",
        "Pasang useEffect tanpa dependency array. Effect jalan tiap render — sering bikin infinite loop.",
        "Lupa `e.preventDefault()` di handler form. Halaman reload setiap submit.",
    ],
    checkpoint=[
        "Bisa pakai `useState` untuk data yang berubah.",
        "Bisa handle event `onClick`, `onChange`, `onSubmit`.",
        "Bisa render conditional dengan `?` dan `&&`.",
        "Tahu fungsi dependency array di `useEffect`.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Tailwind untuk React
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TAILWIND = make_lesson(
    title="Tailwind untuk React",
    slug="tailwind-untuk-react",
    order_index=3,
    read_time="12 menit",
    summary="Utility-first styling, responsive, dark mode, dan setup di Vite.",
    tools=["Project React + Vite dari lesson 1", "Tailwind CSS"],
    outcomes=[
        "Setup Tailwind di project Vite",
        "Memakai utility class untuk styling cepat",
        "Membuat layout responsive dan dark mode",
    ],
    tldr=(
        "Tailwind = library CSS utility-first. Daripada nulis CSS manual, "
        "kamu pasang class kecil di JSX. Cepat, konsisten, mudah responsive "
        "dengan prefix `sm:`, `md:`, `lg:`."
    ),
    pembuka=dedent(
        """\
        Setiap kali nulis CSS dari nol untuk button, kamu pasti ulangi pola yang sama: padding, border-radius, hover.

        Tailwind menyederhanakan ini. Daripada bikin class baru, kamu pasang class utility yang sudah jadi.

        Kelihatan ribet di awal, tapi setelah beberapa hari kamu jadi sangat cepat — dan style-nya konsisten antar component.
        """
    ),
    penjelasan=dedent(
        """\
        ### Setup di Vite

        Di project React + Vite kamu, jalankan:

        ```bash
        npm install -D tailwindcss postcss autoprefixer
        npx tailwindcss init -p
        ```

        Edit `tailwind.config.js`:

        ```js
        export default {
          content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
          theme: { extend: {} },
          plugins: [],
        };
        ```

        Edit `src/index.css`:

        ```css
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
        ```

        Pastikan `index.css` di-import di `src/main.jsx`. Jalankan `npm run dev`. Selesai.

        ### Anatomi class Tailwind

        Class Tailwind itu pendek dan konsisten:

        - **Spacing** — `p-4` (padding 1rem), `m-2` (margin 0.5rem), `gap-3`.
        - **Color** — `bg-blue-500`, `text-white`, `border-gray-200`.
        - **Typography** — `text-lg`, `font-semibold`, `tracking-tight`.
        - **Layout** — `flex`, `grid`, `grid-cols-3`, `items-center`, `justify-between`.
        - **Sizing** — `w-full`, `h-screen`, `max-w-md`.
        - **Border** — `border`, `border-2`, `rounded-lg`, `rounded-full`.

        Contoh button minimal:

        ```jsx
        <button className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
          Klik aku
        </button>
        ```

        Tidak ada CSS file untuk button ini. Semua di JSX.

        ### Responsive — prefix breakpoint

        Tailwind mobile-first. Class tanpa prefix berlaku untuk semua. Prefix `sm:`, `md:`, `lg:`, `xl:` aktif **dari ukuran itu ke atas**.

        ```jsx
        <h1 className="text-2xl md:text-4xl lg:text-6xl">
          Judul yang menyesuaikan
        </h1>
        ```

        Di HP: 2xl. Di tablet: 4xl. Di desktop: 6xl.

        ### State variant — hover, focus, active

        ```jsx
        <button className="bg-blue-500 hover:bg-blue-600 active:scale-95 focus:ring-2 focus:ring-blue-300">
          Tombol
        </button>
        ```

        Prefix `hover:`, `focus:`, `active:` aktif saat user interact.

        ### Dark mode

        Tambahkan di `tailwind.config.js`:

        ```js
        export default {
          darkMode: "class",
          // ...
        };
        ```

        Pasang class `dark` di `<html>` (atau elemen wrapper) untuk activate. Lalu pakai prefix `dark:`:

        ```jsx
        <div className="bg-white text-black dark:bg-gray-900 dark:text-white">
          Konten
        </div>
        ```

        ### Aturan praktis

        - **Pendek tapi banyak.** Tailwind mengandalkan kombinasi class. Itu normal.
        - **Buang class yang ragu.** Kalau kamu copy-paste class dari ChatGPT yang banyak, biasanya bisa diringkas.
        - **Pakai `clsx` atau template string** untuk conditional class.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card dengan Tailwind, responsive, dan hover state:

        ```jsx
        function Card({ judul, deskripsi }) {
          return (
            <article className="rounded-2xl border border-white/10 bg-white/5 p-6 transition-all hover:border-white/20 hover:bg-white/10">
              <h3 className="text-lg font-semibold tracking-tight">{judul}</h3>
              <p className="mt-2 text-sm text-gray-400">{deskripsi}</p>
            </article>
          );
        }

        function App() {
          return (
            <main className="min-h-screen bg-gray-950 text-white">
              <div className="mx-auto max-w-4xl px-4 py-16">
                <h1 className="text-3xl font-semibold sm:text-5xl">
                  Project Saya
                </h1>

                <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                  <Card judul="Toko Kopi" deskripsi="Landing kopi" />
                  <Card judul="Todo App" deskripsi="State & DOM" />
                  <Card judul="Portfolio" deskripsi="Site pertama" />
                </div>
              </div>
            </main>
          );
        }
        ```

        Notasi `bg-white/5` berarti white dengan opacity 5%. Pola ini sering dipakai di dark mode untuk subtle layering.
        """
    ),
    practice=(
        "Style ulang component `Profile` dari lesson 1 pakai Tailwind. "
        "Buat layout dua kolom di desktop (`md:grid-cols-2`), satu kolom di "
        "mobile. Tambahkan hover state pada card."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            <div class="bg-blue-500 padding-4">
              <h1 class="font-size-large">Halo</h1>
              <button class="hover-bg-blue-600">Klik</button>
            </div>
            """
        ),
        "hint": "Cek nama class — apakah sesuai konvensi Tailwind. Dan ingat aturan JSX untuk class.",
        "answer_explanation": dedent(
            """\
            1. JSX pakai `className`, bukan `class`.
            2. Tailwind: padding pakai `p-4`, bukan `padding-4`.
            3. Tailwind: ukuran teks pakai `text-lg`, `text-xl`, dst — bukan `font-size-large`.
            4. Tailwind: hover state pakai prefix `hover:bg-blue-600`, bukan `hover-bg-blue-600`.
            """
        ),
        "fixed_code": dedent(
            """\
            <div className="bg-blue-500 p-4">
              <h1 className="text-lg">Halo</h1>
              <button className="hover:bg-blue-600">Klik</button>
            </div>
            """
        ),
    },
    quiz=[
        q(
            "Apa filosofi utama Tailwind CSS?",
            [
                "Setiap component butuh CSS file sendiri",
                "Utility-first: pasang class kecil di markup, jarang nulis CSS sendiri",
                "Auto-generate kode CSS",
                "Wajib pakai SCSS",
            ],
            "B",
            "Tailwind = utility-first. Class kecil yang dikombinasi langsung di JSX, bukan abstraksi tinggi.",
        ),
        q(
            "Mana penulisan padding 1rem yang BENAR di Tailwind?",
            ["`padding-4`", "`p-4`", "`padding: 1rem`", "`pad-1`"],
            "B",
            "Tailwind pakai `p-4` (padding 1rem). Skala 1 = 0.25rem, jadi 4 = 1rem.",
        ),
        q(
            "Apa arti class `md:text-4xl`?",
            [
                "Selalu text 4xl",
                "Text jadi 4xl mulai dari breakpoint medium ke atas",
                "Cuma di mobile",
                "Error syntax",
            ],
            "B",
            "Prefix `md:` aktif dari breakpoint medium ke atas. Mobile-first: kalau tidak ada prefix, berlaku untuk semua ukuran.",
        ),
        q(
            "Bagaimana cara aktifkan dark mode di Tailwind?",
            [
                "Otomatis aktif",
                "Set `darkMode: 'class'` di config, lalu pasang class `dark` di parent, dan pakai prefix `dark:` di class",
                "Install plugin terpisah saja",
                "Tidak support dark mode",
            ],
            "B",
            "Mode `class` paling fleksibel — kamu yang kontrol kapan dark active dengan toggle class `dark`.",
        ),
        q(
            "Apa fungsi `hover:bg-blue-600` di Tailwind?",
            [
                "Background biru selalu",
                "Background jadi biru-600 saat di-hover",
                "Animasi otomatis",
                "Tidak ada fungsi",
            ],
            "B",
            "Prefix `hover:` mengubah utility menjadi state-aware — aktif hanya saat mouse di atas elemen.",
        ),
    ],
    common_mistakes=[
        "Pakai `class` bukan `className`. JSX akan complain.",
        "Hafal class yang tidak ada (misal `hover-bg-blue`). Dokumentasi Tailwind teman terbaik.",
        "Setup tanpa update `content` di config. Class tidak ter-generate, halaman terlihat polos.",
    ],
    checkpoint=[
        "Bisa setup Tailwind di project Vite.",
        "Bisa style component pakai utility class.",
        "Bisa bikin layout responsive dengan prefix `sm:`/`md:`/`lg:`.",
        "Bisa pakai dark mode dengan prefix `dark:`.",
    ],
    xp_reward=140,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_PORTFOLIO_REACT = make_lesson(
    title="Mini Project — Portfolio Website (React + Tailwind)",
    slug="mini-project-portfolio-react",
    order_index=4,
    read_time="120 menit",
    summary="Bangun portfolio responsive berbasis component dan deploy ke Vercel.",
    tools=["Vite + React", "Tailwind CSS", "GitHub", "Vercel"],
    outcomes=[
        "Membangun multi-component app dari nol",
        "Memakai props dan map untuk data-driven UI",
        "Deploy build production ke Vercel",
    ],
    tldr=(
        "Bangun portfolio dengan minimum 4 component (Navbar, Hero, About, "
        "Projects, Footer). Project list dari array, bukan hardcode. "
        "Responsive + dark mode + deploy."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungkan semua: component, props, state, hooks, Tailwind, dan deploy.

        Hasilnya akan jadi portfolio yang lebih profesional dari Level 1 — kali ini berbasis component yang bisa dimaintain.

        Yang ini layak masuk ke CV beneran.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Tech stack: Vite + React + Tailwind. Tanpa backend.

        Struktur file yang disarankan:

        ```text
        src/
          ├── App.jsx              (router section + layout)
          ├── main.jsx             (entry)
          ├── index.css            (Tailwind directives)
          ├── data/
          │   └── projects.js      (array data project)
          └── components/
              ├── Navbar.jsx
              ├── Hero.jsx
              ├── About.jsx
              ├── Projects.jsx
              ├── ProjectCard.jsx
              └── Footer.jsx
        ```

        ### Section minimal

        - **Navbar** dengan brand di kiri, link section di kanan. Sticky di top.
        - **Hero** dengan nama, tagline, dan dua CTA (lihat project, kontak).
        - **About** dengan paragraf singkat dan list skill (grid 2 atau 4 kolom).
        - **Projects** dengan minimum 3 card. Data dari array di `data/projects.js`. Tiap card punya gambar (boleh placeholder), judul, deskripsi singkat, link demo, link source.
        - **Footer** dengan copyright dan social link.

        ### Aturan tambahan

        - Project list di-render via `.map()`, **bukan** hardcode tag JSX 3 kali.
        - Pakai prop yang bersih, bukan `props.props.title`.
        - Dark mode by default (lebih cepat dari implementasi toggle, dan match dengan vibe modern).
        - Mobile-first. Test di DevTools mode HP.

        ### Tips polish

        - Pakai satu accent color saja (misal `#4EBAEC` atau `tailwind sky-400`).
        - Spacing penting. Section harus punya `py-16 sm:py-24`.
        - Foto project boleh dari `https://placehold.co/600x400` atau Unsplash.
        - Deploy seperti biasa: GitHub → Vercel → URL publik.

        ### Submit

        Salin URL deploy. Buka di HP teman. Tanya kesan pertama. Update sesuai feedback paling tajam.
        """
    ),
    contoh_code_md=dedent(
        """\
        Skeleton minimum untuk memulai:

        ```js
        // src/data/projects.js
        export const projects = [
          {
            id: "landing-kopi",
            title: "Toko Kopi Lokal",
            description: "Landing page untuk kedai kopi lokal di Jogja.",
            image: "https://placehold.co/600x400",
            demo: "https://...",
            source: "https://github.com/...",
            tags: ["HTML", "CSS"],
          },
          // tambahkan lagi
        ];
        ```

        ```jsx
        // src/components/Projects.jsx
        import { projects } from "../data/projects";
        import ProjectCard from "./ProjectCard";

        export default function Projects() {
          return (
            <section id="projects" className="mx-auto max-w-6xl px-4 py-24">
              <h2 className="text-3xl font-semibold sm:text-4xl">
                Project saya
              </h2>
              <p className="mt-2 text-gray-400">
                Hasil belajar dan eksperimen.
              </p>

              <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {projects.map((p) => (
                  <ProjectCard key={p.id} {...p} />
                ))}
              </div>
            </section>
          );
        }
        ```

        ```jsx
        // src/components/ProjectCard.jsx
        export default function ProjectCard({ title, description, image, demo, source, tags }) {
          return (
            <article className="overflow-hidden rounded-2xl border border-white/10 bg-white/5 transition-all hover:border-white/20">
              <img src={image} alt={title} className="aspect-video w-full object-cover" />
              <div className="p-5">
                <h3 className="font-semibold">{title}</h3>
                <p className="mt-2 text-sm text-gray-400">{description}</p>
                <div className="mt-3 flex flex-wrap gap-2">
                  {tags.map((t) => (
                    <span key={t} className="rounded-full bg-white/10 px-2 py-0.5 text-xs">
                      {t}
                    </span>
                  ))}
                </div>
                <div className="mt-4 flex gap-3 text-sm">
                  <a href={demo} className="text-sky-400 hover:underline">Demo →</a>
                  <a href={source} className="text-gray-400 hover:underline">Source →</a>
                </div>
              </div>
            </article>
          );
        }
        ```
        """
    ),
    practice=(
        "Selesaikan portfolio sesuai spec di atas. Push ke GitHub, deploy ke "
        "Vercel. Salin URL publik dan repo. Pastikan tidak ada warning di "
        "Console saat dibuka."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            export default function Projects() {
              return (
                <div className="grid grid-cols-3">
                  {projects.map((p) => (
                    <ProjectCard title={p.title} description={p.description} />
                  ))}
                </div>
              );
            }
            """
        ),
        "hint": "Console akan munculkan warning. Apa yang React keluhkan saat render list?",
        "answer_explanation": dedent(
            """\
            Dua masalah:

            1. `key` tidak diset di tiap `ProjectCard`. React kasih warning dan update list jadi tidak efisien.
            2. Grid `grid-cols-3` tanpa responsive akan jelek di HP. Tambah `sm:grid-cols-2 lg:grid-cols-3`.
            """
        ),
        "fixed_code": dedent(
            """\
            export default function Projects() {
              return (
                <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                  {projects.map((p) => (
                    <ProjectCard
                      key={p.id}
                      title={p.title}
                      description={p.description}
                    />
                  ))}
                </div>
              );
            }
            """
        ),
    },
    quiz=[
        q(
            "Mana praktik yang BAIK untuk render list di React?",
            [
                "Hardcode `<Card />` 3 kali",
                "Simpan data di array, render via `.map()` dengan prop `key` unik",
                "Pakai `for` loop di dalam JSX",
                "Pakai `while` loop",
            ],
            "B",
            "Pola standar: data sebagai array, render dengan `.map()`. Prop `key` wajib untuk efisiensi.",
        ),
        q(
            "Kenapa data project sebaiknya dipisah ke `data/projects.js`?",
            [
                "Untuk gaya saja",
                "Memisahkan data dari UI bikin component reusable dan mudah update",
                "Wajib oleh React",
                "Performance",
            ],
            "B",
            "Pisah data dan UI adalah pola yang scaleable. Update data tidak perlu sentuh component, dan component bisa dipakai dengan dataset lain.",
        ),
        q(
            "Mana langkah yang BENAR setelah portfolio jadi di lokal?",
            [
                "Tunggu sampai sempurna baru deploy",
                "Push ke GitHub, deploy ke Vercel, dapat URL publik",
                "Email file zip ke teman",
                "Simpan di Google Drive",
            ],
            "B",
            "Filosofi 'live first, polish later'. Hosting gratis di Vercel, prosesnya menit-menitan.",
        ),
        q(
            "Apa keuntungan pakai `key={p.id}` daripada `key={index}`?",
            [
                "Tidak ada bedanya",
                "ID stabil saat list di-reorder atau di-delete. Index bisa berubah.",
                "Index lebih cepat",
                "ID lebih panjang",
            ],
            "B",
            "Saat list di-reorder, index tiap item berubah, padahal isinya sama. Pakai ID stabil supaya React tidak salah track.",
        ),
        q(
            "Mana yang TIDAK perlu di portfolio pertama?",
            [
                "Section About",
                "Section Projects dengan data dari array",
                "Backend API custom",
                "Footer dengan kontak",
            ],
            "C",
            "Portfolio statis tidak butuh backend. Fokus dulu di tampilan dan struktur. Backend menyusul saat ada kebutuhan nyata.",
        ),
    ],
    common_mistakes=[
        "Lupa `key` di list. Console keluhkan, update list jadi pelan.",
        "Hardcode 3 card padahal tinggal map dari array. Susah update.",
        "Grid tanpa responsive prefix. Layout berantakan di HP.",
    ],
    checkpoint=[
        "Portfolio live di Vercel dengan URL publik.",
        "Minimum 5 component yang dipisah file.",
        "Project list dari array, di-render via `.map()`.",
        "Tampil rapi di HP dan desktop, dark mode default.",
    ],
    xp_reward=400,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=3,
    slug="react-tailwind",
    title="React & Tailwind",
    subtitle="UI modern berbasis komponen",
    description=(
        "Bangun UI dengan komponen reusable, props, state, dan hooks. "
        "Styling cepat dengan Tailwind CSS, lalu deploy portfolio yang "
        "siap dipakai di CV."
    ),
    duration="~3 minggu",
    difficulty="Menengah",
    accent_color="from-cyan-400/30 to-violet-500/10",
    mini_project="Portfolio Website (React + Tailwind)",
    tags=["React", "Hooks", "Tailwind", "Vite"],
    lessons=[LESSON_REACT_INTRO, LESSON_STATE, LESSON_TAILWIND, PROJECT_PORTFOLIO_REACT],
)
