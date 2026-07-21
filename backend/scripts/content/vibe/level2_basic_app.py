"""
Vibe / Level 2 — Basic App Building.

Lessons:
  1. cara-kerja-web-plain-english
  2. react-mental-model
  3. tailwind-untuk-vibe-coder
  4. mini-project-portfolio-cursor  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Cara Kerja Web (Plain English)
# ─────────────────────────────────────────────────────────────────────────────

LESSON_WEB = make_lesson(
    title="Cara Kerja Web (Bahasa Manusia)",
    slug="cara-kerja-web-plain-english",
    order_index=1,
    read_time="9 menit",
    summary="Browser, server, sama bolak-balik request — tanpa istilah ribet.",
    tools=["Browser modern", "DevTools (tab Network)"],
    outcomes=[
        "Bisa jelasin browser-server pake bahasa sehari-hari",
        "Tau alur dari klik tombol sampai tampilan baru muncul",
        "Bisa nebak: ini masalah di sisi mana ya",
    ],
    tldr=(
        "Browser kamu nanya, server jawab. Itu inti web. Frontend = yang "
        "keliatan di layar. Backend = yang nyimpen data sama ngolah logika. "
        "Ngerti ini bikin kamu gak panik tiap kali ada error."
    ),
    pembuka=dedent(
        """\
        Banyak orang bisa generate kode bagus pake AI tapi langsung panik begitu ada error. Penyebabnya satu: gak tau apa yang sebenernya jalan di balik tampilan.

        Lesson ini bukan ngajarin coding. Tujuannya bikin peta di kepala kamu.

        Habis ini kamu bisa baca kode AI dan langsung paham: "Oh yang ini di sisi browser. Yang ini manggil server."
        """
    ),
    penjelasan=dedent(
        """\
        ### Dua pemain utama: browser sama server

        Browser = aplikasi yang kamu pake buat buka web. Chrome, Safari, Firefox. Itu yang user lihat dan klik.

        Server = komputer di internet yang nyala 24 jam. Tempat data tersimpan dan logika berat dijalanin.

        Kedua-duanya ngobrol pake aturan namanya HTTP. Anggap aja kayak bahasa standar buat ngobrol di internet.

        ### Contoh gampang: pesen makanan online

        Kamu pesen makanan via app. Yang sebenernya kejadian:

        1. Kamu buka app, pilih menu, klik "Pesan". Itu **di HP kamu**.
        2. App ngirim pesenan ke server restoran. Itu **request**.
        3. Server cek stok, hitung harga, simpen ke database. Itu **logika di backend**.
        4. Server jawab: "Oke, pesenan diterima". Itu **response**.
        5. App update tampilan: "Lagi diproses". Itu **HP kamu nge-render ulang**.

        Tiap kali kamu klik sesuatu di internet, alur kayak gini terjadi.

        ### Apa yang kejadian pas kamu buka google.com

        Step by step di balik layar:

        1. Browser nerjemahin `google.com` ke alamat IP lewat DNS. DNS itu mirip buku telepon internet.
        2. Browser ngirim request ke server Google.
        3. Server Google jawab dengan kirim HTML, CSS, sama JavaScript.
        4. Browser baca HTML, terapin CSS, jalanin JavaScript-nya.
        5. Pas kamu ngetik di kotak search, JavaScript di browser yang nge-handle.
        6. Pas kamu pencet Enter, JavaScript ngirim request lagi ke server buat dapet hasil pencarian.

        Jadi kamu sebenernya lagi ngobrol sama server Google, bukan "buka" Google.

        ### Frontend vs Backend

        - **Frontend** — semua yang user lihat dan bisa di-klik. Tombol, animasi, form, layout. Jalan di browser.
        - **Backend** — yang gak keliatan. Cek password, simpen ke database, kirim email. Jalan di server.

        Sebagian web cuma butuh frontend (kayak landing page biasa). Sebagian butuh backend juga (login, posting, e-commerce).

        ### Kenapa kamu wajib paham ini

        Tau bagian-bagian ini ngebantu kamu pas ada error.

        - Error di tampilan? Buka browser console (F12).
        - Error di logika server? Cek logs di Railway atau Vercel function.
        - Error di database? Cek dashboard Supabase.

        Tanpa peta kayak gini, kamu bakal copy seluruh error ke AI dan harap dapet jawaban. Sering gak tepat.

        ### Bahasa di tiap sisi

        - **Buat frontend modern:** HTML, CSS, JavaScript/TypeScript, React/Next.js, Tailwind.
        - **Buat backend modern:** Node.js, Python, atau Go. Express/FastAPI/Hono buat framework.
        - **Buat database:** PostgreSQL, MongoDB, SQLite.

        Kamu gak harus jago semua. Tau apa tinggal di mana udah modal gede.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh percakapan browser-server pas user submit form login:

        ```text
        User klik tombol "Login"
            ↓
        Frontend (React/Next.js):
          fetch("https://api.app.com/login", {
            method: "POST",
            body: JSON.stringify({ email, password })
          })
            ↓
        Request lewat internet
            ↓
        Backend (Express):
          - Cek email di database (Postgres)
          - Bandingin hash password
          - Bikin JWT token
            ↓
        Response balik:
          { "access_token": "eyJ..." }
            ↓
        Frontend:
          - Simpen token di cookie
          - Pindah ke /dashboard
          - Tampilin profil user
        ```

        Cuma lima langkah. Yang user lihat cuma "klik → masuk dashboard". Padahal di belakang ada empat layanan yang ngobrol.
        """
    ),
    practice=(
        "Buka app/web favorit kamu (Twitter/Tokopedia/Instagram). Pencet F12, "
        "buka tab Network, terus klik tombol apa aja. Catat: berapa request "
        "yang muncul buat satu klik? Method-nya apa? Status code-nya apa?"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "Saya bikin tombol login. Pas di-klik, langsung redirect ke
            dashboard tanpa cek password. Bug atau fitur?"
            """
        ),
        "hint": "Mikir dulu: cek password itu kerjaan browser atau server?",
        "answer_explanation": dedent(
            """\
            Itu BUG bahaya banget, bukan fitur. Sisi browser tuh cuma buat tampilan sama navigasi. Verifikasi password WAJIB di server.

            Kalau tombol login langsung redirect tanpa nanya server, siapa pun bisa masuk dashboard tanpa login.

            Pola yang bener:

            1. Frontend kumpulin email + password.
            2. Kirim ke backend lewat HTTP.
            3. Backend cek beneran apa enggak.
            4. Kalau bener, backend kirim balik token.
            5. Frontend simpen token, baru redirect.

            Aturan emas: jangan pernah percaya browser buat hal sensitif.
            """
        ),
        "fixed_code": dedent(
            """\
            // Frontend
            const handleLogin = async () => {
              const res = await fetch("/api/auth/login", {
                method: "POST",
                body: JSON.stringify({ email, password }),
              });

              if (!res.ok) {
                setError("Email atau password salah");
                return;
              }

              const { access_token } = await res.json();
              localStorage.setItem("token", access_token);
              router.push("/dashboard");
            };

            // Backend yang verifikasi password & generate token.
            // Frontend cuma tampilan dan trigger.
            """
        ),
    },
    quiz=[
        q(
            "Server itu kayak apa di analogi pesen makanan?",
            [
                "Tampilan menu di app",
                "Restoran yang nerima pesenan, masak, sama kirim balasan",
                "HP user",
                "Internet",
            ],
            "B",
            "Server = restoran. Tempat 'masak' (logika) dan stok (database) tersimpan. Browser tinggal pesen dan terima.",
        ),
        q(
            "'Request' di HTTP itu apa?",
            [
                "Tampilan halaman",
                "Pesen dari browser yang minta sesuatu ke server",
                "Animasi loading",
                "Logo perusahaan",
            ],
            "B",
            "Request = pertanyaan atau perintah dari browser ke server. Habis itu server kirim balik 'response'.",
        ),
        q(
            "Mana tugas yang TIDAK boleh di frontend?",
            [
                "Render tombol",
                "Animasi hover",
                "Verifikasi password",
                "Cek format email biar UX bagus",
            ],
            "C",
            "Verifikasi password WAJIB di backend. Frontend bisa di-bypass siapa aja yang buka DevTools.",
        ),
        q(
            "DNS itu fungsinya apa?",
            [
                "Bikin halaman lebih cepet",
                "Nerjemahin nama domain (google.com) ke alamat IP server",
                "Hapus cache",
                "Login otomatis",
            ],
            "B",
            "DNS itu kayak buku telepon internet. Browser gak tau di mana google.com tinggal sampe DNS kasih alamat IP-nya.",
        ),
        q(
            "Kenapa vibe coder wajib paham browser-server?",
            [
                "Buat pamer pengetahuan",
                "Biar bisa pisahin: errornya di tampilan, logika server, atau database",
                "Gak penting",
                "Wajib menurut AI",
            ],
            "B",
            "Tanpa peta mental, kamu bakal copy error mentah-mentah ke AI dan sering dapet jawaban yang gak tepat. Tau siapa salah dimana = debugging lebih cepet.",
        ),
    ],
    common_mistakes=[
        "Mikir frontend bisa cek password. Itu bisa di-bypass siapa aja.",
        "Mikir database tinggal di browser. Database tinggal di server, dipanggil sama backend.",
        "Gak buka DevTools pas error. Tab Network sama Console itu temen terbaik.",
    ],
    checkpoint=[
        "Bisa jelasin beda browser sama server pake bahasa sendiri.",
        "Tau apa yang kejadian habis klik tombol di app modern.",
        "Bisa nebak: errornya di tampilan, server, atau database.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — React Mental Model untuk Non-Developer
# ─────────────────────────────────────────────────────────────────────────────

LESSON_REACT_MENTAL = make_lesson(
    title="Cara Mikir Pas Pake React",
    slug="react-mental-model",
    order_index=2,
    read_time="11 menit",
    summary="Component, props, sama state — tanpa harus nulis React dari nol.",
    tools=["Cursor", "Browser modern"],
    outcomes=[
        "Bisa lihat component sebagai potongan UI yang reusable",
        "Bisa kenalin props sama state di kode React",
        "Bisa baca struktur file Next.js modern",
    ],
    tldr=(
        "Component = lego, satuan UI yang bisa dipake berkali-kali. Props = "
        "data yang dikirim ke component. State = kondisi sekarang yang bisa "
        "berubah. Paham tiga ini doang, kamu udah bisa baca kode React dari AI."
    ),
    pembuka=dedent(
        """\
        Banyak vibe coder generate React app pake AI tapi takut nyentuh kodenya. "Kalau saya ubah, takut rusak."

        Wajar di awal. Tapi kalau kamu paham tiga hal di lesson ini, kamu jadi berani edit dan tau mana yang aman.

        Gak perlu jadi React developer. Cukup paham cara mikirnya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Component = lego UI

        Component itu **potongan UI** yang punya tampilan sama logika sendiri.

        Mirip lego: tiap kotak punya bentuk dan warna sendiri, tapi kalau dikombinasi bisa jadi rumah, mobil, robot.

        Contoh component:

        ```jsx
        function Button({ children, onClick }) {
          return (
            <button
              className="px-4 py-2 bg-blue-500 text-white rounded-lg"
              onClick={onClick}
            >
              {children}
            </button>
          );
        }
        ```

        Pake di tempat lain:

        ```jsx
        <Button onClick={() => alert("Hi!")}>Klik aku</Button>
        ```

        Sekali nulis, pake berkali-kali. Mau ubah warna semua tombol? Edit satu file → semua tombol berubah.

        ### Props = data yang masuk

        Props itu cara ngirim data ke component dari luar. Singkatan dari "properties".

        ```jsx
        function Card({ judul, deskripsi }) {
          return (
            <div>
              <h2>{judul}</h2>
              <p>{deskripsi}</p>
            </div>
          );
        }

        <Card judul="Halo" deskripsi="Saya component" />
        ```

        Anggap props itu kayak parameter function. Component sendiri juga mirip function.

        ### State = kondisi sekarang

        State itu data yang **dimiliki component** dan bisa berubah.

        ```jsx
        import { useState } from "react";

        function Counter() {
          const [count, setCount] = useState(0);

          return (
            <div>
              <p>Sekarang: {count}</p>
              <button onClick={() => setCount(count + 1)}>+</button>
            </div>
          );
        }
        ```

        Pas `setCount` dipanggil, React otomatis nge-render ulang component-nya. Kamu gak perlu otak-atik DOM manual.

        ### Aturan yang gak bisa ditawar

        - **Props ngalir ke bawah.** Parent kasih data ke child lewat props. Child gak boleh ubah props.
        - **State milik satu component.** Tiap component punya state sendiri. Mau share antar component? Naikin ke parent.
        - **Update state pake setter.** Selalu pake `setCount(...)`, jangan `count = count + 1`. React gak bakal re-render kalau di-assign langsung.

        Banyak pemula bingung di poin ketiga ini. Santai aja. Inget aja: pake setter selalu.

        ### Struktur file Next.js App Router

        ```text
        app/
          ├── layout.jsx        ← bungkus semua halaman (navbar, footer)
          ├── page.jsx          ← halaman /
          ├── about/
          │   └── page.jsx      ← halaman /about
          ├── blog/
          │   ├── page.jsx      ← halaman /blog
          │   └── [slug]/
          │       └── page.jsx  ← halaman /blog/[slug]
        components/
          ├── Navbar.jsx
          └── Footer.jsx
        ```

        Aturan: **folder = URL path**. File `page.jsx` di tiap folder = halaman utama folder itu. Kurung kotak `[slug]` = parameter dinamis.

        ### Cara prompt AI biar akurat

        Habis paham hal-hal di atas, prompt kamu jadi lebih tepat.

        Bedain:

        - "Bikin component" — terlalu umum, AI ngarang.
        - "Bikin component Card di `components/Card.jsx` yang terima props `judul` sama `deskripsi`. Pake Tailwind. Default style minimal." — spesifik, hasilnya akurat.

        Pas AI keluar dari pola ini (misal pake class component lama), kamu langsung tau dan bisa minta revisi.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh component dengan props + state — kombinasi keduanya:

        ```jsx
        // components/CommentBox.jsx
        "use client";

        import { useState } from "react";

        export default function CommentBox({ author }) {
          const [text, setText] = useState("");
          const [comments, setComments] = useState([]);

          const submit = () => {
            if (!text.trim()) return;
            setComments([
              ...comments,
              { id: Date.now(), author, text }
            ]);
            setText("");
          };

          return (
            <div className="space-y-3">
              <h3>Komentar buat {author}</h3>

              <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Tulis komentar..."
                className="w-full rounded border p-2"
              />
              <button
                onClick={submit}
                className="rounded bg-blue-500 px-3 py-1 text-white"
              >
                Kirim
              </button>

              <ul>
                {comments.map((c) => (
                  <li key={c.id}>
                    <strong>{c.author}:</strong> {c.text}
                  </li>
                ))}
              </ul>
            </div>
          );
        }
        ```

        - `author` itu props (dari luar).
        - `text` sama `comments` itu state (dimiliki component).
        - `submit` itu event handler yang update state.
        """
    ),
    practice=(
        "Buka kode React dari project apa aja yang kamu punya (atau generate "
        "baru pake AI). Identifikasi tiga hal: 1) berapa component yang ada, "
        "2) props apa yang diterima tiap component, 3) state apa yang dimiliki "
        "component. Tulis di catetan."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            "use client";
            import { useState } from "react";

            export default function Counter() {
              let count = 0;

              function tambah() {
                count = count + 1;
                console.log(count);
              }

              return (
                <button onClick={tambah}>
                  Klik: {count}
                </button>
              );
            }
            """
        ),
        "hint": (
            "Console emang nampilin angkanya naik, tapi tampilan tombol gak "
            "berubah. Kenapa ya?"
        ),
        "answer_explanation": dedent(
            """\
            Salahnya: `count` ditulis pake `let` biasa. React gak tau data ini berubah, jadinya component-nya gak re-render.

            React cuma re-render kalau STATE berubah. State dibikin pake `useState`. Update wajib pake setter (`setCount`).
            """
        ),
        "fixed_code": dedent(
            """\
            "use client";
            import { useState } from "react";

            export default function Counter() {
              const [count, setCount] = useState(0);

              return (
                <button onClick={() => setCount(count + 1)}>
                  Klik: {count}
                </button>
              );
            }
            """
        ),
    },
    quiz=[
        q(
            "Component di React paling pas dianggap kayak apa?",
            [
                "Halaman lengkap",
                "Lego — potongan kecil yang bisa digabung jadi tampilan utuh",
                "Tabel database",
                "File CSS",
            ],
            "B",
            "Component = lego. Sekali nulis, pake berkali-kali, dan bisa digabung buat bikin tampilan kompleks.",
        ),
        q(
            "Fungsi props di React itu apa?",
            [
                "Nyimpen data permanen",
                "Ngirim data dari parent ke child component",
                "Buat login",
                "Nge-render UI",
            ],
            "B",
            "Props mirip parameter function. Ngalir dari atas (parent) ke bawah (child).",
        ),
        q(
            "Beda state sama props itu apa?",
            [
                "Sama aja",
                "Props dari luar (read-only di child). State dimiliki component dan bisa berubah.",
                "State lebih cepet",
                "Props cuma buat styling",
            ],
            "B",
            "Aturannya: child gak boleh ubah props. State punya sendiri yang bisa di-update lewat setter.",
        ),
        q(
            "Kalau `setCount(...)` dipanggil, apa yang terjadi?",
            [
                "Gak ada apa-apa",
                "React jadwalin re-render component dengan nilai baru",
                "Halaman reload",
                "Database ke-update",
            ],
            "B",
            "Tiap update state trigger re-render component itu (sama child-nya). React update DOM secara efisien.",
        ),
        q(
            "Di Next.js App Router, file `app/blog/[slug]/page.jsx` ngurusin URL apa?",
            [
                "/blog",
                "/blog/[slug]",
                "/blog/anything (parameter dinamis)",
                "Gak ada",
            ],
            "C",
            "Kurung kotak `[slug]` bikin segment URL jadi dinamis. `/blog/halo` sama `/blog/world` sama-sama hit page ini.",
        ),
    ],
    common_mistakes=[
        "Update state pake `=`. React gak re-render — biasanya pemula lupa di sini.",
        "Bingung kapan pake `\"use client\"`. Aturan: kalau butuh hooks atau event, kasih `\"use client\"` di baris pertama.",
        "Mikir class component itu cara modern React. Sekarang yang dipake function component sama hooks.",
    ],
    checkpoint=[
        "Bisa jelasin beda component, props, sama state.",
        "Bisa baca kode React dan nemuin tiga hal di atas.",
        "Tau struktur folder dasar Next.js App Router.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Tailwind untuk Vibe Coder
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TW_VIBE = make_lesson(
    title="Tailwind buat Vibe Coder",
    slug="tailwind-untuk-vibe-coder",
    order_index=3,
    read_time="10 menit",
    summary="Pake Tailwind tanpa hafal semua class, plus prompt AI yang lebih akurat.",
    tools=["Cursor", "AI assistant", "Tailwind docs (referensi)"],
    outcomes=[
        "Bisa baca pola class Tailwind tanpa hafal semuanya",
        "Bisa prompt AI pake istilah Tailwind yang tepat",
        "Bisa debug tampilan berantakan pake DevTools",
    ],
    tldr=(
        "Tailwind itu CSS yang udah disiapin pecahan kecil-kecil. Kamu gak "
        "perlu hafal semua class — paham polanya aja udah cukup. AI yang "
        "isi detailnya, kamu yang kasih instruksi visual."
    ),
    pembuka=dedent(
        """\
        Tailwind itu mirip seperangkat alat siap pakai. Kamu gak perlu bikin alat dulu sebelum mulai kerja.

        Kabar baik buat vibe coder: gak perlu hafal semua class. Tau polanya aja cukup. AI yang bakal isi detailnya.

        Yang penting kamu bisa kasih tau AI tepat apa yang kamu mau secara visual.
        """
    ),
    penjelasan=dedent(
        """\
        ### Pola class Tailwind

        Class Tailwind itu konsisten banget. Habis paham polanya, kamu bisa nebak class baru tanpa lihat docs.

        Pola umumnya: `[apa]-[nilai]`.

        - **Spacing:** `p-4` (padding), `m-4` (margin), `gap-4`. Angka 4 = `1rem`.
        - **Warna:** `bg-blue-500`, `text-red-600`. Format: `[apa]-[warna]-[shade]`. Shade 50 paling terang, 950 paling gelap.
        - **Typography:** `text-lg`, `font-semibold`, `tracking-tight`.
        - **Layout:** `flex`, `grid`, `justify-center`, `items-center`.
        - **Ukuran:** `w-full`, `h-screen`, `max-w-md`.
        - **Border:** `border`, `rounded-lg`, `rounded-full`.

        Lupa? Buka [tailwindcss.com/docs](https://tailwindcss.com/docs). Search-nya cepet banget.

        ### Responsive — pake prefix breakpoint

        Tailwind itu mobile-first. Class tanpa prefix berlaku di semua ukuran. Prefix `sm:`, `md:`, `lg:`, `xl:` aktif dari ukuran itu ke atas.

        ```html
        <h1 class="text-2xl md:text-4xl lg:text-6xl">Judul</h1>
        ```

        Di HP: 2xl. Di tablet: 4xl. Di desktop: 6xl.

        ### Dark mode

        Prefix `dark:` aktif kalau parent punya class `dark` (atau OS user lagi dark mode).

        ```html
        <div class="bg-white dark:bg-gray-900 text-black dark:text-white">
          ...
        </div>
        ```

        ### State variant

        Prefix buat hover, focus, active, disabled:

        ```html
        <button class="bg-blue-500 hover:bg-blue-600 active:scale-95 disabled:opacity-50">
          Tombol
        </button>
        ```

        ### Cara prompt AI pake Tailwind

        Jelek: "Bikin tombol bagus."

        Bagus: "Bikin button primary, padding `px-4 py-2`, background `bg-blue-500`, hover `bg-blue-600`, rounded `rounded-lg`, sama transition smooth."

        Atau lebih bagus lagi (tanpa hafal class spesifik): "Bikin button primary, padding sedang, background biru, hover sedikit lebih gelap, sudut membulat halus, sama transition smooth pas hover."

        AI yang ngerti Tailwind bakal nerjemahin deskripsi visual kamu jadi class yang tepat.

        ### Cara debug tampilan berantakan

        Pas hasil AI jelek atau gak sesuai keinginan:

        1. Buka DevTools → tab Elements. Klik elemen yang aneh.
        2. Lihat class apa yang aktif. Toggle satu-satu di panel Styles → cari mana yang masalah.
        3. Atau ubah nilai langsung di DevTools (klik nilai padding misalnya, ganti angkanya). Lihat efeknya real-time.
        4. Habis tau yang salah, balik ke kode dan benerin.

        Skill ini bakal hemat banget waktu kamu daripada bolak-balik prompt AI.

        ### Bonus: Prettier plugin Tailwind

        Plugin `prettier-plugin-tailwindcss` otomatis sortir class Tailwind sesuai urutan resmi. Install di Cursor → kode kamu jadi lebih konsisten.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card responsive plus dark mode plus hover state:

        ```jsx
        <article className="
          rounded-2xl
          border border-gray-200 dark:border-gray-800
          bg-white dark:bg-gray-900
          p-6
          transition-all
          hover:border-blue-400 hover:shadow-lg
        ">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
            Judul Card
          </h3>
          <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Deskripsi singkat di sini.
          </p>

          <button className="
            mt-4
            inline-flex items-center gap-2
            rounded-lg bg-blue-500 hover:bg-blue-600
            px-4 py-2
            text-sm font-medium text-white
            transition-colors
          ">
            Pelajari →
          </button>
        </article>
        ```

        Class banyak tapi konsisten. Kalau udah sering lihat pola kayak gini, baca jadi cepet.
        """
    ),
    practice=(
        "Buka [v0.dev](https://v0.dev) atau Claude. Prompt: 'Bikin card "
        "produk e-commerce dengan gambar di atas, judul, harga, sama tombol "
        "Beli. Style minimal, dark mode, accent biru.' Salin hasilnya ke "
        "Cursor. Edit satu hal kecil (misal ganti accent color) tanpa minta "
        "AI lagi."
    ),
    fix_error={
        "language": "jsx",
        "broken_code": dedent(
            """\
            <div className="bg-blue-500 text-white">
              <h1 className="text-large">Judul</h1>
              <button className="hover-bg-blue-600">Klik</button>
              <p className="margin-top-4">Paragraf</p>
            </div>
            """
        ),
        "hint": "Tiga class gak valid. Cek pola Tailwind yang sebenarnya.",
        "answer_explanation": dedent(
            """\
            Tiga salahnya:

            1. `text-large` gak ada. Yang bener: `text-lg` atau `text-xl`.
            2. `hover-bg-blue-600` salah pemisah. Pake `hover:bg-blue-600` (titik dua, bukan strip).
            3. `margin-top-4` gak ada. Yang bener: `mt-4` (m = margin, t = top).
            """
        ),
        "fixed_code": dedent(
            """\
            <div className="bg-blue-500 text-white">
              <h1 className="text-lg">Judul</h1>
              <button className="hover:bg-blue-600">Klik</button>
              <p className="mt-4">Paragraf</p>
            </div>
            """
        ),
    },
    quiz=[
        q(
            "Apa cara kerja utama Tailwind?",
            [
                "Wajib bikin class CSS sendiri",
                "Pasang class kecil langsung di markup, jarang nulis CSS sendiri",
                "Auto-generate component",
                "Cuma buat Tailwind expert",
            ],
            "B",
            "Tailwind nyediain banyak utility class kecil yang dikombinasi langsung di markup. Gak perlu pindah-pindah file CSS.",
        ),
        q(
            "Mana penulisan padding yang BENER di Tailwind?",
            ["`padding-4`", "`p-4`", "`pad-1`", "`p4`"],
            "B",
            "Format: `[apa]-[nilai]`. Padding pake `p-`, lalu skala (1 = 0.25rem, 4 = 1rem).",
        ),
        q(
            "Class `md:text-4xl` artinya apa?",
            [
                "Selalu text 4xl",
                "Text jadi 4xl mulai dari breakpoint medium ke atas",
                "Cuma di mobile",
                "Error",
            ],
            "B",
            "Mobile-first: tanpa prefix berlaku semua ukuran, prefix `md:` aktif dari medium ke atas.",
        ),
        q(
            "Pemisah yang BENER buat state variant Tailwind?",
            ["Strip `-`", "Titik dua `:`", "Underscore `_`", "Gak ada pemisah"],
            "B",
            "Format: `state:utility`. Contoh `hover:bg-blue-600`, `dark:text-white`, `focus:ring-2`.",
        ),
        q(
            "Cara cepet debug tampilan berantakan?",
            [
                "Hapus semua kode dan mulai ulang",
                "Buka DevTools, klik elemen yang aneh, toggle class atau ubah nilai langsung di Styles panel",
                "Restart komputer",
                "Tanya AI tanpa konteks",
            ],
            "B",
            "DevTools nampilin class yang aktif sama efek styling. Tweaking real-time di sana lebih cepet daripada bolak-balik prompt AI.",
        ),
    ],
    common_mistakes=[
        "Hafal class yang gak ada (`text-large`, `margin-top-4`). Tailwind punya pola spesifik.",
        "Pake strip buat state variant (`hover-bg`). Yang bener titik dua (`hover:bg`).",
        "Class urutannya acak. Pake prettier-plugin-tailwindcss biar konsisten.",
    ],
    checkpoint=[
        "Bisa baca pola class Tailwind tanpa hafal semuanya.",
        "Bisa prompt AI pake deskripsi visual yang spesifik.",
        "Bisa pake DevTools buat debug styling.",
        "Tau format responsive pake prefix breakpoint.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_PORTFOLIO_CURSOR = make_lesson(
    title="Mini Project — Portfolio Pake Cursor + Claude",
    slug="mini-project-portfolio-cursor",
    order_index=4,
    read_time="120 menit",
    summary="Bikin portfolio yang gak keliatan AI-generated.",
    tools=["Cursor", "Claude atau ChatGPT", "GitHub", "Vercel"],
    outcomes=[
        "Bisa bangun portfolio pake workflow Cursor + AI",
        "Bisa polish output AI sampe keliatan dipikirin",
        "Punya URL portfolio yang lebih bagus dari Level 1",
    ],
    tldr=(
        "Pake Cursor + Claude buat bikin portfolio Next.js + Tailwind. Fokus "
        "polish: spacing, typography, hierarchy. Hasilnya keliatan dipikirin, "
        "bukan asal generate."
    ),
    pembuka=dedent(
        """\
        Banyak portfolio buatan AI keliatan sama: card padding sedang, accent biru, hero pucat banget.

        Tujuan project ini: hasilin portfolio yang **keliatan dipikirin**, bukan asal generate.

        Caranya bukan dengan code lebih banyak — tapi prompt yang lebih spesifik dan polish yang lebih telaten.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind. Tanpa backend.

        Section minimal:

        - **Hero** — nama, tagline kuat satu kalimat, dua CTA (lihat project, kontak).
        - **About** — paragraf pendek + skill list dalam grid.
        - **Projects** — minimum 3 card. Data dari array, bukan hardcode di tiap card.
        - **Contact** — form sederhana atau link langsung ke email + social.

        ### Workflow Cursor + Claude

        - **Step 1:** Di Claude (atau ChatGPT), kasih konteks lengkap. Stack, gaya, dark/light mode, accent color, font, target user. Minta plan struktur file dulu, jangan langsung kode.
        - **Step 2:** Habis plan disepakatin, minta implementasi component per component. Salin tiap output ke Cursor di file yang sesuai.
        - **Step 3:** Test di lokal. Buka di Cursor, lihat di browser.
        - **Step 4:** Polish pake ⌘K di Cursor: "Bikin spacing lebih lega di hero", "Tambah animation halus pas card di-hover".

        ### Polish checklist

        Hal-hal kecil yang bedain portfolio amatir vs polished:

        - **Spacing.** Section harus `py-24 sm:py-32`. Jangan pelit padding.
        - **Typography hierarchy.** H1 jelas lebih gede dari H2. Body text kontras tinggi sama background.
        - **Whitespace.** Jangan tumpuk info di satu area. Kasih ruang.
        - **Disiplin warna.** 1 accent + 2-3 grayscale. Gak lebih.
        - **Border-radius konsisten.** Pilih satu nilai (misal `rounded-xl`) terus pake terus.
        - **Animation halus.** `transition-all hover:scale-[1.02]` di card. Jangan berlebihan.
        - **Pake font dari Google Fonts.** Default font Tailwind oke, tapi font dari Google (Inter, Plus Jakarta Sans) lebih kerasa premium.
        - **OG image.** Buat preview pas dibagiin di sosmed. Bisa dibikin di [og-image-builder](https://og-playground.vercel.app/) atau Figma.

        ### Bahasa yang pas

        Portfolio bahasa Indonesia tanpa keliatan sok English. Pake gaya santai-profesional:

        - Jelek: "I create stunning user experiences."
        - Bagus: "Saya bikin aplikasi web yang dipake user, bukan cuma demo."

        Spesifik > umum. Jujur > lebay.

        ### Mini project ke real project

        Portfolio ini bakal jadi kartu nama kamu buat satu tahun ke depan. Update kalau ada project baru. Anggap kayak dokumen yang hidup.

        Habis live, share ke beberapa orang dengan profesi beda: developer, designer, non-tech. Tanya satu-satu: "Apa yang kamu paham tentang saya dari halaman ini?".

        Feedback dari tiga sudut pandang ini berharga banget.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh prompt komprehensif buat Claude:

        ```text
        Saya mau bikin portfolio personal sebagai web developer pemula.

        Tech stack:
        - Next.js 14 App Router
        - Tailwind CSS
        - TypeScript
        - Tanpa backend (data project hardcode di file data/projects.ts)

        Style:
        - Dark mode default
        - Accent: #4EBAEC (biru terang)
        - Background: #0a0a0a
        - Font: Inter dari Google Fonts
        - Vibe visual: minimal, banyak whitespace, hover animation halus

        Struktur halaman:
        - Hero: nama gede, tagline 1 kalimat, 2 CTA (lihat project, kontak)
        - About: paragraf pendek + 6 skill dalam grid 3 kolom
        - Projects: 3 card minimum, data dari array
        - Contact: link email + social, gak perlu form

        Bahasa copy: Indonesia santai-profesional. Hindari jargon Inggris berlebihan.

        Mulai dari struktur file dulu, jangan langsung kode.
        ```

        Habis Claude kasih plan, kamu approve atau revisi. Baru lanjut implementasi.
        """
    ),
    practice=(
        "Selesain portfolio sesuai workflow di atas. Deploy ke Vercel. Catet "
        "tiga hal: 1) total prompt yang dibutuhin berapa? 2) Bagian mana yang "
        "paling makan waktu? 3) Apa hal yang AI gak bisa selesain dan harus "
        "kamu edit manual?"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "Bikin portfolio."
            AI: [output: portfolio dengan card padding sedang, hero pucat,
                 spacing biasa-biasa, copy text generic English yang sok-sokan]

            User: "Bagus."
            """
        ),
        "hint": "Output AI tanpa arahan = output generic. Kamu yang harus pegang taste-nya.",
        "answer_explanation": dedent(
            """\
            Salahnya: prompt vague + gak ada feedback berulang.

            Hasilnya generic karena AI gak punya konteks tentang siapa kamu, gaya yang kamu mau, sama target user-nya.

            Yang bener: prompt yang spesifik (lihat contoh di atas), terus iterasi feedback dengan istilah desain yang tepat. "Spacing-nya kurang lega di hero" lebih efektif daripada "kurang oke".
            """
        ),
        "fixed_code": dedent(
            """\
            User: [Prompt komprehensif kayak contoh di atas]
            AI: [Plan struktur file]
            User: "Plan oke. Lanjut implementasi Hero dulu."
            AI: [Hero component]
            User: "Spacing di hero masih sempit. Naikin py-32 sm:py-48.
                  Tagline masih English. Ganti ke 'Saya bikin aplikasi web
                  yang berguna, bukan cuma demo.'"
            AI: [Hero versi revisi]
            ... [lanjut sampe puas]
            """
        ),
    },
    quiz=[
        q(
            "Apa yang ngebedain portfolio polished sama portfolio AI generic?",
            [
                "Banyak animasi mencolok",
                "Spacing yang lega, hierarchy jelas, disiplin warna, sama konsistensi",
                "Pake banyak warna",
                "Code yang panjang",
            ],
            "B",
            "Detail kecil ini efeknya kumulatif. Portfolio yang keliatan dipikirin vs asal generate.",
        ),
        q(
            "Mana cara prompt yang BAGUS buat AI?",
            [
                "Singkat: 'Bikin portfolio'",
                "Konteks lengkap: stack, gaya, bahasa, struktur, sama minta plan dulu",
                "Acak-acakan",
                "Cuma sebut warna",
            ],
            "B",
            "Konteks komprehensif = output akurat. Tanpa konteks, AI ngarang dengan pola generic.",
        ),
        q(
            "Apa fungsi 'iterasi feedback' habis AI kasih draft?",
            [
                "Gak penting",
                "Buat ngarahin AI ke arah yang lebih spesifik pake kosakata desain yang tepat",
                "Buat basa-basi",
                "Cuma buat profesional",
            ],
            "B",
            "Iterasi itu inti vibe coding. AI jarang langsung tepat di percobaan pertama. Kamu yang pegang taste.",
        ),
        q(
            "Disiplin warna yang BAGUS buat portfolio pemula?",
            [
                "Banyak warna biar menarik",
                "1 accent + 2-3 grayscale",
                "Pelangi",
                "Hitam putih aja",
            ],
            "B",
            "Aturan warna: kebanyakan warna = chaos. Sedikit warna dengan kontras yang tepat = polished.",
        ),
        q(
            "Apa yang sebaiknya dilakuin habis portfolio live?",
            [
                "Lupain aja",
                "Share ke 3 orang dari profesi beda dan tanya kesan mereka",
                "Update tiap menit",
                "Hapus dan ulang",
            ],
            "B",
            "Feedback dari mata yang beda ngungkap blind spot. Gak semua orang punya konteks teknis kayak kamu.",
        ),
    ],
    common_mistakes=[
        "Prompt vague. Hasilnya generic.",
        "Gak iterasi. AI jarang langsung kasih hasil paling tepat.",
        "Copy text English yang sok-sokan. Bikin copy bahasa Indonesia yang jujur.",
    ],
    checkpoint=[
        "Portfolio live di Vercel.",
        "Keliatan dipikirin: spacing, typography, disiplin warna.",
        "Udah dapet feedback dari minimal 3 orang dengan profesi beda.",
        "Workflow Cursor + AI udah enak — tau kapan AI cukup, kapan perlu polish manual.",
    ],
    xp_reward=400,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=2,
    slug="basic-app-building",
    title="Basic App Building",
    subtitle="Dari prompt ke struktur app yang masuk akal",
    description=(
        "Ngobrolin browser-server, React, sama styling cepet pake Tailwind. "
        "Tutup level dengan portfolio yang dibangun lewat workflow Cursor + "
        "AI yang efektif."
    ),
    duration="~2 minggu",
    difficulty="Pemula → Menengah",
    accent_color="from-pink-400/30 to-violet-500/10",
    mini_project="Portfolio Pakai Cursor + Claude",
    tags=["React", "Tailwind", "Mental Model", "AI Workflow"],
    lessons=[LESSON_WEB, LESSON_REACT_MENTAL, LESSON_TW_VIBE, PROJECT_PORTFOLIO_CURSOR],
)
