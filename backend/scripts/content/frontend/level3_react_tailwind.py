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
    title="Kenalan sama React",
    slug="pengenalan-react",
    order_index=1,
    read_time="14 menit",
    summary="Component, JSX, props, sama cara mikir pas pake React.",
    tools=["Node.js LTS", "VS Code", "Browser modern"],
    outcomes=[
        "Bisa setup project React baru pake Vite",
        "Bisa nulis component pake JSX",
        "Bisa kirim data antar component lewat props",
        "Bisa pecah UI jadi bagian kecil yang reusable",
    ],
    tldr=(
        "React = library buat bikin UI berbasis component. JSX itu HTML di "
        "dalem JS. Component fungsinya mirip lego — nulis sekali, pake "
        "berkali-kali. Kirim data antar component pake props."
    ),
    pembuka=dedent(
        """\
        Coba kamu bayangin bikin website sama 100 tombol yang tampilannya sama tapi isinya beda.

        Pake HTML biasa, kamu harus nulis `<button>` 100 kali. Capek. Salah satu, harus benerin di 100 tempat.

        Pake React, kamu nulis `Button` sekali — pake 100 kali dengan props yang beda. Itu inti React.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu React

        React itu library JavaScript buat bangun UI. Buatan Facebook, sekarang dipake Instagram, Netflix, Airbnb, sama ratusan ribu app lain.

        Ide utamanya: UI dipecah jadi **component** — potongan kecil yang berdiri sendiri. Tiap component punya tampilan sama logikanya sendiri.

        ### Setup project pertama pake Vite

        Vite itu bundler modern yang cepet. Buka terminal di folder kosong:

        ```bash
        npm create vite@latest portfolio -- --template react
        cd portfolio
        npm install
        npm run dev
        ```

        Buka `http://localhost:5173`. Kamu udah punya project React yang jalan.

        ### JSX — HTML di dalem JavaScript

        Buka `src/App.jsx`. Kamu bakal lihat sesuatu kayak gini:

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

        Itu JSX. Keliatan kayak HTML, tapi sebenernya ditulis di dalem JavaScript. Bedanya:

        - `class` jadi `className` (karena `class` itu keyword JavaScript).
        - `for` (di label) jadi `htmlFor`.
        - Tag self-closing wajib slash, misal `<img />`, bukan `<img>`.
        - Bisa selipin JS pake kurung kurawal `{ }`.

        ### Component itu cuma function

        Component React itu function yang return JSX. Aturannya:

        - Nama component **wajib diawali huruf kapital** (`Card`, `Button`, `Hero`).
        - Cuma boleh return **satu** root element. Kalau butuh lebih, bungkus pake `<>...</>` (Fragment).

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

        Pake pake `<Card />` di component lain.

        ### Props — kirim data antar component

        Component sering butuh data dari luar. Kamu kirim lewat **props** kayak atribut HTML.

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
              <Card judul="Lagi" deskripsi="Pake berkali-kali" />
            </main>
          );
        }
        ```

        Notasi `{ judul, deskripsi }` itu **destructuring** — ngambil property dari object yang masuk.

        ### Cara mikir pas pake React

        Lupain dulu kebiasaan "ambil elemen, ubah pake DOM". Ganti pake:

        - **Pecah UI jadi component kecil.** Hero, Card, Button, Navbar — masing-masing satu file.
        - **Data ngalir dari atas ke bawah.** Parent component kirim props ke child, bukan sebaliknya.
        - **JSX itu deskripsi.** Kamu mendeskripsikan tampilan akhir, React yang urus DOM.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card list pake props sama array map:

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

        Kunci: `key` di tiap item. React butuh ini buat track tiap item secara unik.
        """
    ),
    practice=(
        "Bikin component `Profile` yang nerima props `nama`, `role`, sama "
        "`bio`. Pake di `App.jsx` dua kali sama data beda. Tampilannya boleh "
        "sederhana — fokus dulu di cara kirim data lewat props."
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
            "Tiga masalah: penamaan component, atribut JSX, sama jumlah root element."
        ),
        "answer_explanation": dedent(
            """\
            1. Nama component WAJIB diawali huruf kapital: `Card`, bukan `card`. Lowercase dianggep HTML tag biasa.
            2. JSX pake `className`, bukan `class`. `class` itu keyword JavaScript.
            3. Component cuma boleh return satu root element. Bungkus pake Fragment `<>...</>` atau `<div>` kalau butuh dua atau lebih siblings.
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
            "Apa nama tempat nulis HTML di dalem JavaScript di React?",
            ["HTMX", "JSX", "TSX-only", "Mustache"],
            "B",
            "JSX (JavaScript XML) itu ekstensi sintaks yang ngebolehin nulis tag mirip HTML di dalem JavaScript.",
        ),
        q(
            "Kenapa nama component WAJIB diawali huruf kapital?",
            [
                "Buat estetika",
                "Karena nama lowercase dianggep HTML tag biasa sama React",
                "Karena diwajibin ECMAScript",
                "Gak wajib, opsional",
            ],
            "B",
            "React ngebedain component dari HTML tag lewat huruf kapital. `<Card />` dianggep component, `<card />` dianggep HTML.",
        ),
        q(
            "Cara ngirim data dari parent ke child component?",
            ["Pake global variable", "Lewat props", "Lewat localStorage", "Pake cookies"],
            "B",
            "Props itu cara standar ngirim data dari atas ke bawah dari parent ke child di React.",
        ),
        q(
            "Apa beda `className` sama `class` di JSX?",
            [
                "Gak ada bedanya",
                "JSX pake `className` karena `class` itu keyword JavaScript",
                "`className` lebih lambat",
                "`class` cuma buat TypeScript",
            ],
            "B",
            "`class` di JavaScript dipake buat class declaration. JSX pake `className` biar gak bentrok.",
        ),
        q(
            "Apa fungsi prop `key` pas render list pake `.map()`?",
            [
                "Buat styling",
                "Buat ngebantu React kenalin tiap item secara unik pas list berubah",
                "Gak ada fungsi, opsional",
                "Buat login",
            ],
            "B",
            "`key` ngebantu React track tiap item. Tanpa key (atau key yang sama), React bisa keliru pas update list — re-render jadi gak efisien.",
        ),
    ],
    common_mistakes=[
        "Pake `class` bukan `className`. Browser tetep render, tapi React kasih warning.",
        "Lupa `key` pas `.map()`. List tetep muncul, tapi update bisa aneh.",
        "Return dua sibling tanpa Fragment. Error: 'Adjacent JSX elements must be wrapped'.",
    ],
    checkpoint=[
        "Bisa setup project React baru pake Vite.",
        "Bisa bikin component sama pake di parent.",
        "Bisa kirim data lewat props sama render list pake `.map()`.",
        "Tau kapan butuh Fragment.",
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
    summary="useState, useEffect, conditional rendering, sama event di React.",
    tools=["Project React + Vite dari lesson 1", "Browser DevTools"],
    outcomes=[
        "Bisa pake `useState` buat data yang berubah",
        "Bisa pake `useEffect` buat side effect",
        "Bisa conditional rendering sama event handler",
    ],
    tldr=(
        "State = kondisi sekarang component. Pake `useState` buat data yang "
        "berubah, `useEffect` buat side effect (fetch, timer, listener). "
        "Update state = component re-render."
    ),
    pembuka=dedent(
        """\
        Sampe sini component kamu masih statis. Saatnya kasih dia kondisi yang bisa berubah.

        Bayangin tombol yang nampilin jumlah klik. Counternya berubah, sama halaman ikut update.

        Itu yang disebut state. Sama cara React ngeurusinnya disebut hooks.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu state

        State itu data yang **dimiliki component** dan bisa berubah seiring waktu.

        Pas state berubah, React otomatis nge-render ulang component itu. Kamu gak perlu otak-atik DOM manual.

        ### useState — hook pertama

        `useState` ngembaliin dua hal: nilai sekarang sama function buat update.

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

        Notasi `[count, setCount]` itu array destructuring. Kebiasaan-nya nama setter pake prefix `set`.

        Tiap kali `setCount` dipanggil, React nge-render ulang component sama nilai baru.

        ### Aturan penting

        - **Jangan ubah state langsung.** Salah: `count = count + 1`. Bener: `setCount(count + 1)`.
        - **State itu asynchronous.** Kalau update beberapa kali sekaligus, pake callback: `setCount(prev => prev + 1)`.
        - **Hooks cuma dipanggil di top level component.** Jangan di dalem if, loop, atau function nested.

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

        Kalau mau nampilin UI beda berdasarkan state:

        ```jsx
        {isLogin ? <Dashboard /> : <LoginForm />}
        {error && <p className="error">{error}</p>}
        ```

        Operator ternary buat dua kemungkinan. `&&` buat render kalau true.

        ### useEffect — side effect

        Kalau butuh ngerjain sesuatu di luar render (fetch data, set timer, pasang listener), pake `useEffect`.

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

        Argumen kedua `[]` itu dependency array:

        - `[]` jalan **sekali** pas component pertama mount.
        - `[var]` jalan pas `var` berubah.
        - Tanpa array, jalan **tiap render** (jarang dipake).

        Function yang di-return itu cleanup, jalan pas component unmount.
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

              {count > 5 && <p>Kamu udah klik banyak banget!</p>}
            </div>
          );
        }

        export default App;
        ```

        Perhatiin: `setCount((prev) => prev - 1)` versi callback — aman pas ada beberapa update beruntun.
        """
    ),
    practice=(
        "Bikin component `LoginForm` sama dua input (email, password) yang "
        "controlled. Pasang tombol 'Login'. Pas submit, tampilin pesan "
        "'Halo, [email]!' sama kosongin password. Pake `useState` sama "
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
            "Tampilan gak update pas tombol diklik. Perhatiin cara nyimpen "
            "sama ngubah `count`."
        ),
        "answer_explanation": dedent(
            """\
            Salahnya: `count` ditulis pake `let` biasa. React gak tau data ini berubah, jadinya gak re-render.

            Solusinya: pake `useState`. Update pake `setCount`, jangan assign langsung.
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
            "Apa yang dikembaliin `useState`?",
            [
                "Single value",
                "Array sama dua elemen: nilai sekarang sama function buat update",
                "Object",
                "Promise",
            ],
            "B",
            "`useState(initial)` ngembaliin `[value, setValue]`. Ini array destructuring.",
        ),
        q(
            "Mana cara yang BENER buat update state?",
            [
                "`count = count + 1`",
                "`setCount(count + 1)`",
                "`useState(count + 1)`",
                "`document.querySelector` terus ubah",
            ],
            "B",
            "State HARUS di-update lewat setter (`setCount`). Assign langsung gak trigger re-render.",
        ),
        q(
            "Kapan callback `useEffect` sama `[]` dijalanin?",
            [
                "Tiap render",
                "Sekali pas component pertama mount",
                "Gak pernah",
                "Pas user logout",
            ],
            "B",
            "Dependency array kosong `[]` artinya 'jalan sekali pas mount, gak peduli render selanjutnya'.",
        ),
        q(
            "Apa yang terjadi kalau kamu return function dari useEffect?",
            [
                "Error",
                "Function itu jadi cleanup — dipanggil pas component unmount atau effect dijalanin ulang",
                "Function dieksekusi tiap detik",
                "Gak ada efek",
            ],
            "B",
            "Cleanup function pas banget buat `clearInterval`, `removeEventListener`, atau abort request — biar gak ada memory leak.",
        ),
        q(
            "Mana cara yang AMAN pas update state berdasarkan nilai sebelumnya?",
            [
                "`setCount(count + 1)` di dua tempat berturut-turut",
                "`setCount(prev => prev + 1)` versi callback",
                "Gak ada bedanya",
                "Pake global variable",
            ],
            "B",
            "Update beruntun pake `setCount(count + 1)` bisa miss karena state asynchronous. Versi callback `prev => prev + 1` selalu pake nilai terbaru.",
        ),
    ],
    common_mistakes=[
        "Update state pake `=` langsung. Component gak re-render.",
        "Pasang useEffect tanpa dependency array. Effect jalan tiap render — sering bikin infinite loop.",
        "Lupa `e.preventDefault()` di handler form. Halaman reload tiap submit.",
    ],
    checkpoint=[
        "Bisa pake `useState` buat data yang berubah.",
        "Bisa handle event `onClick`, `onChange`, `onSubmit`.",
        "Bisa render conditional pake `?` sama `&&`.",
        "Tau fungsi dependency array di `useEffect`.",
    ],
    xp_reward=160,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Tailwind untuk React
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TAILWIND = make_lesson(
    title="Tailwind buat React",
    slug="tailwind-untuk-react",
    order_index=3,
    read_time="12 menit",
    summary="Utility-first styling, responsive, dark mode, sama setup di Vite.",
    tools=["Project React + Vite dari lesson 1", "Tailwind CSS"],
    outcomes=[
        "Bisa setup Tailwind di project Vite",
        "Bisa pake utility class buat styling cepet",
        "Bisa bikin layout responsive sama dark mode",
    ],
    tldr=(
        "Tailwind = library CSS utility-first. Daripada nulis CSS manual, "
        "kamu pasang class kecil di JSX. Cepet, konsisten, gampang bikin "
        "responsive lewat prefix `sm:`, `md:`, `lg:`."
    ),
    pembuka=dedent(
        """\
        Tiap kali nulis CSS dari nol buat button, kamu pasti ngulang pola yang sama: padding, border-radius, hover.

        Tailwind nyederhanain ini. Daripada bikin class baru, kamu pasang class utility yang udah jadi.

        Keliatan ribet di awal, tapi habis beberapa hari kamu jadi cepet banget — sama style-nya konsisten antar component.
        """
    ),
    penjelasan=dedent(
        """\
        ### Setup di Vite

        Di project React + Vite kamu, jalanin:

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

        Pastiin `index.css` di-import di `src/main.jsx`. Jalanin `npm run dev`. Selesai.

        ### Anatomi class Tailwind

        Class Tailwind itu pendek sama konsisten:

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

        Gak ada CSS file buat button ini. Semua di JSX.

        ### Responsive — prefix breakpoint

        Tailwind itu mobile-first. Class tanpa prefix berlaku buat semua. Prefix `sm:`, `md:`, `lg:`, `xl:` aktif **dari ukuran itu ke atas**.

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

        Prefix `hover:`, `focus:`, `active:` aktif pas user interact.

        ### Dark mode

        Tambahin di `tailwind.config.js`:

        ```js
        export default {
          darkMode: "class",
          // ...
        };
        ```

        Pasang class `dark` di `<html>` (atau elemen wrapper) buat aktifin. Terus pake prefix `dark:`:

        ```jsx
        <div className="bg-white text-black dark:bg-gray-900 dark:text-white">
          Konten
        </div>
        ```

        ### Aturan praktis

        - **Pendek tapi banyak.** Tailwind ngandalin kombinasi class. Itu normal.
        - **Buang class yang ragu.** Kalau kamu copy-paste class dari ChatGPT yang banyak, biasanya bisa diringkes.
        - **Pake `clsx` atau template string** buat conditional class.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card sama Tailwind, responsive, sama hover state:

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

        Notasi `bg-white/5` artinya white sama opacity 5%. Pola ini sering dipake di dark mode buat layering halus.
        """
    ),
    practice=(
        "Style ulang component `Profile` dari lesson 1 pake Tailwind. Bikin "
        "layout dua kolom di desktop (`md:grid-cols-2`), satu kolom di "
        "mobile. Tambahin hover state di card."
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
        "hint": "Cek nama class — apakah sesuai pola Tailwind. Sama inget aturan JSX buat class.",
        "answer_explanation": dedent(
            """\
            1. JSX pake `className`, bukan `class`.
            2. Tailwind: padding pake `p-4`, bukan `padding-4`.
            3. Tailwind: ukuran teks pake `text-lg`, `text-xl`, dst — bukan `font-size-large`.
            4. Tailwind: hover state pake prefix `hover:bg-blue-600`, bukan `hover-bg-blue-600`.
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
            "Apa cara kerja utama Tailwind CSS?",
            [
                "Tiap component butuh CSS file sendiri",
                "Pasang class kecil di markup, jarang nulis CSS sendiri",
                "Auto-generate kode CSS",
                "Wajib pake SCSS",
            ],
            "B",
            "Tailwind = utility-first. Class kecil yang dikombinasi langsung di JSX, bukan abstraksi tinggi.",
        ),
        q(
            "Mana penulisan padding 1rem yang BENER di Tailwind?",
            ["`padding-4`", "`p-4`", "`padding: 1rem`", "`pad-1`"],
            "B",
            "Tailwind pake `p-4` (padding 1rem). Skala 1 = 0.25rem, jadi 4 = 1rem.",
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
            "Prefix `md:` aktif dari breakpoint medium ke atas. Mobile-first: kalau gak ada prefix, berlaku buat semua ukuran.",
        ),
        q(
            "Gimana cara aktifin dark mode di Tailwind?",
            [
                "Otomatis aktif",
                "Set `darkMode: 'class'` di config, terus pasang class `dark` di parent, sama pake prefix `dark:` di class",
                "Install plugin terpisah aja",
                "Gak support dark mode",
            ],
            "B",
            "Mode `class` paling fleksibel — kamu yang kontrol kapan dark active sama toggle class `dark`.",
        ),
        q(
            "Apa fungsi `hover:bg-blue-600` di Tailwind?",
            [
                "Background biru selalu",
                "Background jadi biru-600 pas di-hover",
                "Animasi otomatis",
                "Gak ada fungsi",
            ],
            "B",
            "Prefix `hover:` ngubah utility jadi state-aware — aktif cuma pas mouse di atas elemen.",
        ),
    ],
    common_mistakes=[
        "Pake `class` bukan `className`. JSX bakal complain.",
        "Hafal class yang gak ada (misal `hover-bg-blue`). Dokumentasi Tailwind temen terbaik.",
        "Setup tanpa update `content` di config. Class gak ke-generate, halaman keliatan polos.",
    ],
    checkpoint=[
        "Bisa setup Tailwind di project Vite.",
        "Bisa style component pake utility class.",
        "Bisa bikin layout responsive sama prefix `sm:`/`md:`/`lg:`.",
        "Bisa pake dark mode sama prefix `dark:`.",
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
    summary="Bangun portfolio responsive berbasis component sama deploy ke Vercel.",
    tools=["Vite + React", "Tailwind CSS", "GitHub", "Vercel"],
    outcomes=[
        "Bisa bangun multi-component app dari nol",
        "Bisa pake props sama map buat data-driven UI",
        "Bisa deploy build production ke Vercel",
    ],
    tldr=(
        "Bangun portfolio sama minimum 4 component (Navbar, Hero, About, "
        "Projects, Footer). Project list dari array, bukan hardcode. "
        "Responsive + dark mode + deploy."
    ),
    pembuka=dedent(
        """\
        Saatnya gabungin semua: component, props, state, hooks, Tailwind, sama deploy.

        Hasilnya bakal jadi portfolio yang lebih profesional dari Level 1 — kali ini berbasis component yang bisa di-maintain.

        Yang ini layak masuk ke CV beneran.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Tech stack: Vite + React + Tailwind. Tanpa backend.

        Struktur file yang disaranin:

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

        - **Navbar** sama brand di kiri, link section di kanan. Sticky di top.
        - **Hero** sama nama, tagline, sama dua CTA (lihat project, kontak).
        - **About** sama paragraf singkat sama list skill (grid 2 atau 4 kolom).
        - **Projects** sama minimum 3 card. Data dari array di `data/projects.js`. Tiap card punya gambar (boleh placeholder), judul, deskripsi singkat, link demo, link source.
        - **Footer** sama copyright sama social link.

        ### Aturan tambahan

        - Project list di-render lewat `.map()`, **bukan** hardcode tag JSX 3 kali.
        - Pake prop yang bersih, bukan `props.props.title`.
        - Dark mode by default (lebih cepet daripada implementasi toggle, sama match sama vibe modern).
        - Mobile-first. Test di DevTools mode HP.

        ### Tips polish

        - Pake satu accent color aja (misal `#4EBAEC` atau `tailwind sky-400`).
        - Spacing penting. Section harus punya `py-16 sm:py-24`.
        - Foto project boleh dari `https://placehold.co/600x400` atau Unsplash.
        - Deploy kayak biasa: GitHub → Vercel → URL publik.

        ### Submit

        Salin URL deploy. Buka di HP temen. Tanya kesan pertama. Update sesuai feedback paling tajam.
        """
    ),
    contoh_code_md=dedent(
        """\
        Skeleton minimum buat mulai:

        ```js
        // src/data/projects.js
        export const projects = [
          {
            id: "landing-kopi",
            title: "Toko Kopi Lokal",
            description: "Landing page buat kedai kopi lokal di Jogja.",
            image: "https://placehold.co/600x400",
            demo: "https://...",
            source: "https://github.com/...",
            tags: ["HTML", "CSS"],
          },
          // tambahin lagi
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
                Hasil belajar sama eksperimen.
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
        "Selesain portfolio sesuai spec di atas. Push ke GitHub, deploy ke "
        "Vercel. Salin URL publik sama repo. Pastiin gak ada warning di "
        "Console pas dibuka."
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
        "hint": "Console bakal muncul warning. Apa yang React keluhin pas render list?",
        "answer_explanation": dedent(
            """\
            Dua masalah:

            1. `key` gak diset di tiap `ProjectCard`. React kasih warning sama update list jadi gak efisien.
            2. Grid `grid-cols-3` tanpa responsive bakal jelek di HP. Tambah `sm:grid-cols-2 lg:grid-cols-3`.
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
            "Mana cara yang BAGUS buat render list di React?",
            [
                "Hardcode `<Card />` 3 kali",
                "Simpen data di array, render lewat `.map()` sama prop `key` unik",
                "Pake `for` loop di dalem JSX",
                "Pake `while` loop",
            ],
            "B",
            "Pola standar: data sebagai array, render pake `.map()`. Prop `key` wajib buat efisiensi.",
        ),
        q(
            "Kenapa data project sebaiknya dipisah ke `data/projects.js`?",
            [
                "Buat gaya aja",
                "Misahin data dari UI bikin component reusable sama gampang di-update",
                "Wajib menurut React",
                "Performance",
            ],
            "B",
            "Pisah data sama UI itu pola yang scalable. Update data gak perlu sentuh component, sama component bisa dipake sama dataset lain.",
        ),
        q(
            "Mana langkah yang BENER habis portfolio jadi di lokal?",
            [
                "Tunggu sampe sempurna baru deploy",
                "Push ke GitHub, deploy ke Vercel, dapet URL publik",
                "Email file zip ke temen",
                "Simpen di Google Drive",
            ],
            "B",
            "Filosofi 'live duluan, polish belakangan'. Hosting gratis di Vercel, prosesnya menit-menitan.",
        ),
        q(
            "Apa keuntungan pake `key={p.id}` daripada `key={index}`?",
            [
                "Gak ada bedanya",
                "ID stabil pas list di-reorder atau di-delete. Index bisa berubah.",
                "Index lebih cepet",
                "ID lebih panjang",
            ],
            "B",
            "Pas list di-reorder, index tiap item berubah, padahal isinya sama. Pake ID stabil biar React gak salah track.",
        ),
        q(
            "Mana yang TIDAK perlu di portfolio pertama?",
            [
                "Section About",
                "Section Projects sama data dari array",
                "Backend API custom",
                "Footer sama kontak",
            ],
            "C",
            "Portfolio statis gak butuh backend. Fokus dulu di tampilan sama struktur. Backend nyusul pas ada kebutuhan nyata.",
        ),
    ],
    common_mistakes=[
        "Lupa `key` di list. Console keluhin, update list jadi pelan.",
        "Hardcode 3 card padahal tinggal map dari array. Susah update.",
        "Grid tanpa responsive prefix. Layout berantakan di HP.",
    ],
    checkpoint=[
        "Portfolio live di Vercel sama URL publik.",
        "Minimum 5 component yang dipisah file.",
        "Project list dari array, di-render lewat `.map()`.",
        "Tampil rapi di HP sama desktop, dark mode default.",
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
        "Bangun UI sama komponen reusable, props, state, sama hooks. "
        "Styling cepet pake Tailwind CSS, terus deploy portfolio yang siap "
        "dipake di CV."
    ),
    duration="~3 minggu",
    difficulty="Menengah",
    accent_color="from-cyan-400/30 to-violet-500/10",
    mini_project="Portfolio Website (React + Tailwind)",
    tags=["React", "Hooks", "Tailwind", "Vite"],
    lessons=[LESSON_REACT_INTRO, LESSON_STATE, LESSON_TAILWIND, PROJECT_PORTFOLIO_REACT],
)
