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
    title="Cara Kerja Web (Plain English)",
    slug="cara-kerja-web-plain-english",
    order_index=1,
    read_time="9 menit",
    summary="Client, server, request/response — tanpa istilah ribet.",
    tools=["Browser modern", "DevTools (Network tab)"],
    outcomes=[
        "Memahami client-server dengan analogi sehari-hari",
        "Membaca alur klik tombol → tampilan baru",
        "Mengenali kapan kamu perlu frontend, backend, atau keduanya",
    ],
    tldr=(
        "Browser (client) tanya, server jawab. Itu inti web. Frontend = "
        "tampilan, backend = logika dan data. Pakai AI untuk implementasi, "
        "tapi paham model mentalnya supaya tidak terjebak saat ada error."
    ),
    pembuka=dedent(
        """\
        Banyak vibe coder bisa generate kode bagus, tapi panik begitu ada error. Penyebabnya satu: mereka tidak paham apa yang sebenarnya terjadi di balik tampilan.

        Lesson ini bukan tutorial coding. Ini peta mental.

        Setelah lesson ini, kamu bisa baca kode AI dan langsung paham: "Oh, yang ini bagian client. Yang ini panggil server."
        """
    ),
    penjelasan=dedent(
        """\
        ### Dua karakter utama: client dan server

        Client = browser HP/laptop kamu. Tempat user lihat dan klik.

        Server = komputer di internet yang jalan 24/7. Tempat data tersimpan dan logika berat dijalankan.

        Mereka bicara via HTTP — protokol percakapan standar di internet.

        ### Analogi: pesan makanan online

        Bayangkan kamu pesan makanan via app:

        1. Kamu buka app, pilih menu, klik "Pesan". Itu **client side**.
        2. App kirim pesanan ke server restoran. Itu **request**.
        3. Server cek stok, kalkulasi harga, simpan ke database. Itu **backend logic**.
        4. Server balas: "OK, pesanan diterima". Itu **response**.
        5. App update tampilan: "Pesanan sedang diproses". Itu **client render ulang**.

        Setiap kali kamu klik sesuatu di internet, alur ini terjadi.

        ### Apa yang terjadi saat kamu buka google.com

        Step by step di balik layar:

        1. Browser terjemahkan `google.com` ke alamat IP via DNS (ibarat buku telepon).
        2. Browser kirim **HTTP GET request** ke server Google.
        3. Server Google balas HTML, CSS, JavaScript.
        4. Browser render HTML jadi tampilan, terapkan CSS, jalankan JavaScript.
        5. Saat kamu ketik sesuatu di kotak search, JavaScript di browser handle aksi itu.
        6. Saat kamu tekan Enter, JavaScript kirim request lagi ke server untuk dapat hasil pencarian.

        Jadi sebenarnya kamu mengunjungi server Google, bukan "membuka" Google.

        ### Frontend vs Backend

        - **Frontend** — semua yang user lihat dan interact. Tombol, animasi, form, layout. Jalan di browser.
        - **Backend** — logika di balik layar. Cek password, simpan ke database, kirim email. Jalan di server.

        Sebagian app cuma butuh frontend (landing page statis). Sebagian butuh backend (login, post, e-commerce).

        ### Kenapa kamu perlu paham ini

        Saat kamu prompt AI dan dapat error, kamu butuh **isolasi masalah**:

        - Apakah error di frontend? Cek browser console (F12).
        - Apakah error di backend? Cek logs di Railway/Vercel function.
        - Apakah error di database? Cek di dashboard Supabase.

        Tanpa peta mental ini, kamu copy-paste seluruh error ke AI dan harap dapat solusi. Sering tidak akurat.

        ### Bahasa di tiap sisi

        - **Frontend modern:** HTML, CSS, JavaScript/TypeScript, React/Next.js, Tailwind.
        - **Backend modern:** Node.js, Python, atau Go. Express/FastAPI/Hono untuk framework.
        - **Database:** PostgreSQL, MongoDB, SQLite.

        Kamu tidak harus jago semua. Tahu apa yang tinggal di mana saja sudah cukup besar.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh percakapan client-server saat user submit form login:

        ```text
        User klik tombol "Login"
            ↓
        Frontend (React/Next.js):
          fetch("https://api.app.com/login", {
            method: "POST",
            body: JSON.stringify({ email, password })
          })
            ↓
        HTTP request lewat internet
            ↓
        Backend (Express):
          - Cek email di database (Postgres)
          - Bandingkan hash password
          - Generate JWT token
            ↓
        HTTP response balik:
          { "access_token": "eyJ..." }
            ↓
        Frontend:
          - Simpan token di cookie
          - Redirect ke /dashboard
          - Tampilkan profil user
        ```

        Lima langkah saja. Yang kelihatan di mata user cuma "klik → tampilan dashboard". Padahal di belakang ada empat layanan yang berkomunikasi.
        """
    ),
    practice=(
        "Buka app/website favorit kamu (Twitter/Tokopedia/Instagram). Tekan "
        "F12 → Network → klik tombol apa saja. Catat: berapa request yang "
        "muncul untuk satu klik? Method-nya apa? Status code-nya apa?"
    ),
    fix_error={
        "language": "text",
        "broken_code": dedent(
            """\
            User: "Saya bikin tombol login. Saat di-klik, langsung redirect ke
            dashboard tanpa cek password. Bug atau fitur?"
            """
        ),
        "hint": "Pikirkan: aksi 'cek password' itu kerjaan client atau server?",
        "answer_explanation": dedent(
            """\
            Itu BUG keamanan, bukan fitur. Client side cuma untuk tampilan dan navigasi. Verifikasi password WAJIB di backend.

            Kalau tombol login langsung redirect tanpa request ke server, siapa pun bisa akses dashboard tanpa login.

            Pola yang benar:
            1. Frontend kumpulkan email + password.
            2. Kirim ke backend lewat HTTP.
            3. Backend verifikasi.
            4. Kalau OK, backend balas token.
            5. Frontend simpan token, redirect.

            Aturan emas: jangan pernah percaya client untuk hal sensitif.
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
            "Apa fungsi server dalam analogi pesan makanan online?",
            [
                "Tampilan menu di app",
                "Restoran yang menerima pesanan, masak, dan kirim balasan",
                "HP user",
                "Internet",
            ],
            "B",
            "Server = restoran. Tempat 'masak' (logika) dan stok (database) tersimpan. Client tinggal pesan dan terima.",
        ),
        q(
            "Apa yang dimaksud 'request' dalam HTTP?",
            [
                "Tampilan halaman",
                "Pesan dari client (browser) yang minta sesuatu ke server",
                "Animasi loading",
                "Logo perusahaan",
            ],
            "B",
            "Request adalah pertanyaan/perintah dari client ke server. Setelahnya, server kirim balik 'response'.",
        ),
        q(
            "Mana tugas yang TIDAK seharusnya di frontend?",
            [
                "Render tombol",
                "Animasi hover",
                "Verifikasi password",
                "Validasi format email (sebagai UX)",
            ],
            "C",
            "Verifikasi password WAJIB di backend. Frontend bisa di-bypass siapa saja yang buka DevTools.",
        ),
        q(
            "Apa fungsi DNS dalam alur 'buka google.com'?",
            [
                "Mempercepat halaman",
                "Menerjemahkan nama domain (google.com) ke alamat IP server",
                "Menghapus cache",
                "Login otomatis",
            ],
            "B",
            "DNS itu seperti buku telepon internet. Browser tidak tahu di mana google.com tinggal sampai DNS kasih alamat IP-nya.",
        ),
        q(
            "Kenapa pemahaman client-server penting untuk vibe coder?",
            [
                "Untuk pamer pengetahuan",
                "Supaya bisa isolasi masalah saat error: apakah di frontend, backend, atau database",
                "Tidak penting",
                "Wajib oleh AI",
            ],
            "B",
            "Tanpa peta mental, vibe coder copy-paste error mentah ke AI dan sering dapat solusi tidak akurat. Paham siapa salah dimana = debugging lebih cepat.",
        ),
    ],
    common_mistakes=[
        "Pikir frontend bisa cek password. Itu bisa di-bypass siapa saja.",
        "Pikir database tinggal di browser. Database tinggal di server, di-akses backend.",
        "Tidak buka DevTools saat error. Network tab dan Console adalah teman terbaik.",
    ],
    checkpoint=[
        "Bisa jelaskan beda client dan server dengan analogi.",
        "Tahu apa yang terjadi setelah klik tombol di app modern.",
        "Bisa isolasi error: apakah di frontend, backend, atau database.",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — React Mental Model untuk Non-Developer
# ─────────────────────────────────────────────────────────────────────────────

LESSON_REACT_MENTAL = make_lesson(
    title="React Mental Model",
    slug="react-mental-model",
    order_index=2,
    read_time="11 menit",
    summary="Component, props, dan state — tanpa nulis React dari nol.",
    tools=["Cursor", "Browser modern"],
    outcomes=[
        "Memahami component sebagai unit UI yang reusable",
        "Mengenali props dan state di kode React",
        "Membaca struktur file Next.js modern",
    ],
    tldr=(
        "Component = lego, satuan UI yang bisa dipakai ulang. Props = "
        "parameter yang dikirim ke component. State = kondisi sekarang yang "
        "bisa berubah. Pahami tiga ini, kamu bisa baca kode React dari AI."
    ),
    pembuka=dedent(
        """\
        Banyak vibe coder generate React app dengan AI tapi takut sentuh kodenya. "Kalau saya ubah, takut rusak."

        Itu wajar di awal. Tapi kalau kamu paham tiga konsep di lesson ini, kamu jadi berani edit dan tahu apa yang aman.

        Tidak perlu jadi React developer. Cukup paham model mentalnya.
        """
    ),
    penjelasan=dedent(
        """\
        ### Component = lego UI

        Component adalah **potongan UI** yang punya tampilan dan logika sendiri.

        Bayangkan lego: tiap kotak punya bentuk dan warnanya sendiri, tapi kamu kombinasi bisa jadi rumah, mobil, robot.

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

        Pakai di tempat lain:

        ```jsx
        <Button onClick={() => alert("Hi!")}>Klik aku</Button>
        ```

        Sekali tulis, pakai berkali-kali. Kalau mau ubah warna semua tombol, edit satu file → semua tombol berubah.

        ### Props = data yang masuk

        Props (singkatan dari "properties") adalah cara mengirim data ke component dari luar.

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

        Anggap props sebagai parameter function. Component itu sendiri mirip function.

        ### State = kondisi sekarang

        State adalah data yang **dimiliki component** dan bisa berubah.

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

        Saat `setCount` dipanggil, React otomatis re-render component. Kamu tidak manipulasi DOM manual.

        ### Aturan emas vibe coder

        - **Props mengalir ke bawah.** Parent kasih data ke child via props. Child tidak bisa ubah props.
        - **State milik satu component.** Tiap component punya state sendiri. Mau share antar component? Naikkan ke parent (lifting state up).
        - **Update state pakai setter.** Selalu pakai `setCount(...)`, jangan `count = count + 1`. React tidak akan re-render kalau di-assign langsung.

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

        ### Cara prompt AI yang efektif

        Setelah paham mental model di atas, prompt kamu jadi lebih akurat.

        Bedakan:

        - "Bikin component" — generic, AI ngarang.
        - "Bikin component Card di `components/Card.jsx` yang terima props `judul` dan `deskripsi`. Pakai Tailwind. Default style minimal." — spesifik, AI hasilnya akurat.

        Saat AI keluar dari pola ini (misal pakai class component lama), kamu langsung tahu dan bisa minta revisi.
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
              <h3>Komentar untuk {author}</h3>

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
        - `text` dan `comments` itu state (dimiliki component).
        - `submit` adalah event handler yang update state.
        """
    ),
    practice=(
        "Buka kode React mana saja dari project yang kamu punya (atau "
        "generate baru pakai AI). Identifikasi 3 hal: 1) berapa component yang "
        "ada, 2) props apa yang diterima setiap component, 3) state apa yang "
        "dimiliki component. Tulis di catatan."
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
            "Console memang menampilkan angka naik, tapi tampilan tombol "
            "tidak berubah. Kenapa?"
        ),
        "answer_explanation": dedent(
            """\
            Kesalahan: `count` ditulis sebagai `let` biasa. React tidak tahu data ini berubah, jadi component tidak re-render.

            React cuma re-render kalau STATE berubah. State dibuat dengan `useState`. Update wajib pakai setter (`setCount`).
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
            "Apa analogi yang paling tepat untuk component di React?",
            [
                "Sebuah halaman lengkap",
                "Lego — potongan kecil yang bisa dikombinasikan jadi tampilan utuh",
                "Tabel database",
                "File CSS",
            ],
            "B",
            "Component = lego. Sekali tulis, pakai berkali-kali, dan bisa dikombinasikan untuk bikin tampilan kompleks.",
        ),
        q(
            "Apa fungsi props di React?",
            [
                "Menyimpan data permanen",
                "Mengirim data dari parent ke child component",
                "Melakukan login",
                "Menggambar UI",
            ],
            "B",
            "Props mirip parameter function. Mengalir top-down dari parent ke child.",
        ),
        q(
            "Apa beda state dan props?",
            [
                "Sama saja",
                "Props dari luar (read-only di child). State dimiliki component dan bisa berubah.",
                "State lebih cepat",
                "Props cuma untuk styling",
            ],
            "B",
            "Aturan: child tidak boleh ubah props. State milik sendiri yang bisa di-update lewat setter.",
        ),
        q(
            "Apa yang terjadi saat `setCount(...)` dipanggil?",
            [
                "Tidak ada",
                "React menjadwalkan re-render component dengan nilai baru",
                "Halaman reload",
                "Database update",
            ],
            "B",
            "Setiap update state trigger re-render component itu (dan child-nya). React update DOM secara efisien.",
        ),
        q(
            "Di Next.js App Router, file `app/blog/[slug]/page.jsx` melayani URL apa?",
            [
                "/blog",
                "/blog/[slug]",
                "/blog/anything (parameter dinamis)",
                "Tidak ada",
            ],
            "C",
            "Kurung kotak `[slug]` membuat segment URL jadi dinamis. `/blog/halo` dan `/blog/world` sama-sama hit page ini.",
        ),
    ],
    common_mistakes=[
        "Update state pakai `=`. React tidak re-render.",
        "Bingung kapan pakai `\"use client\"`. Aturan: kalau butuh hooks atau event, kasih `\"use client\"` di baris pertama.",
        "Pikir component class adalah cara modern React. Modern: function component dengan hooks.",
    ],
    checkpoint=[
        "Bisa jelaskan beda component, props, dan state.",
        "Bisa baca kode React dan identifikasi tiga hal di atas.",
        "Tahu struktur folder dasar Next.js App Router.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — Tailwind untuk Vibe Coder
# ─────────────────────────────────────────────────────────────────────────────

LESSON_TW_VIBE = make_lesson(
    title="Tailwind untuk Vibe Coder",
    slug="tailwind-untuk-vibe-coder",
    order_index=3,
    read_time="10 menit",
    summary="Pakai Tailwind tanpa hafal semua class, bantu AI prompt yang akurat.",
    tools=["Cursor", "AI assistant", "Tailwind docs (referensi)"],
    outcomes=[
        "Mengenali pola class Tailwind tanpa hafal semua",
        "Prompt AI dengan istilah Tailwind yang tepat",
        "Debug tampilan yang berantakan dengan DevTools",
    ],
    tldr=(
        "Tailwind = utility-first CSS. Vibe coder tidak perlu hafal semua "
        "class — paham polanya saja cukup. Pakai AI untuk generate, kamu "
        "yang kasih instruksi visual yang spesifik."
    ),
    pembuka=dedent(
        """\
        Tailwind itu seperti seperangkat alat yang sudah jadi. Kamu tidak perlu bikin alat dulu sebelum mulai kerja.

        Kabar baiknya untuk vibe coder: kamu tidak perlu hafal semua class. Paham polanya saja cukup. AI yang isi detailnya.

        Yang penting: kamu bisa bilang ke AI dengan tepat apa yang kamu mau secara visual.
        """
    ),
    penjelasan=dedent(
        """\
        ### Pola class Tailwind

        Tailwind class itu sangat konsisten. Setelah kamu paham polanya, kamu bisa tebak class baru tanpa lihat docs.

        Pola umum: `[property]-[value]`.

        - **Spacing:** `p-4` (padding), `m-4` (margin), `gap-4`. Angka 4 = `1rem`.
        - **Color:** `bg-blue-500`, `text-red-600`. Format: `[utility]-[color]-[shade]`. Shade 50 paling terang, 950 paling gelap.
        - **Typography:** `text-lg`, `font-semibold`, `tracking-tight`.
        - **Layout:** `flex`, `grid`, `justify-center`, `items-center`.
        - **Sizing:** `w-full`, `h-screen`, `max-w-md`.
        - **Border:** `border`, `rounded-lg`, `rounded-full`.

        Tidak hafal? Cek di docs: [tailwindcss.com/docs](https://tailwindcss.com/docs). Ada search yang super cepat.

        ### Responsive — prefix breakpoint

        Mobile-first. Class tanpa prefix berlaku di semua ukuran. Prefix `sm:`, `md:`, `lg:`, `xl:` aktif dari ukuran itu ke atas.

        ```html
        <h1 class="text-2xl md:text-4xl lg:text-6xl">Judul</h1>
        ```

        Di HP: 2xl. Di tablet: 4xl. Di desktop: 6xl.

        ### Dark mode

        Prefix `dark:` aktif kalau parent punya class `dark` (atau OS user dark mode).

        ```html
        <div class="bg-white dark:bg-gray-900 text-black dark:text-white">
          ...
        </div>
        ```

        ### State variant

        Prefix untuk hover, focus, active, disabled:

        ```html
        <button class="bg-blue-500 hover:bg-blue-600 active:scale-95 disabled:opacity-50">
          Tombol
        </button>
        ```

        ### Cara prompt AI dengan Tailwind

        Buruk: "Bikin tombol bagus."

        Baik: "Bikin button primary dengan padding `px-4 py-2`, background `bg-blue-500`, hover `bg-blue-600`, rounded `rounded-lg`, dan transition smooth."

        Atau bahkan lebih baik (tanpa hafal class spesifik): "Bikin button primary, padding sedang, background biru, hover sedikit lebih gelap, sudut membulat lembut, transition smooth saat hover."

        AI yang fluent Tailwind akan terjemahkan deskripsi visual jadi class yang tepat.

        ### Cara debug tampilan berantakan

        Saat hasil AI jelek atau tidak sesuai keinginan:

        1. Buka DevTools → Elements tab. Klik elemen yang aneh.
        2. Lihat class apa yang aktif. Coba toggle satu per satu di panel Styles → cek mana yang bermasalah.
        3. Atau tweak nilai langsung di DevTools (klik nilai padding misalnya, ganti angkanya). Lihat efeknya real-time.
        4. Setelah tahu yang salah, balik ke kode dan perbaiki.

        Kemampuan ini akan menghemat berjam-jam ketimbang prompt AI bolak-balik.

        ### Bonus: Prettier plugin Tailwind

        Plugin `prettier-plugin-tailwindcss` otomatis sortir class Tailwind sesuai konvensi resmi. Install di Cursor → kode kamu jadi lebih konsisten.
        """
    ),
    contoh_code_md=dedent(
        """\
        Card responsive dengan dark mode dan hover state:

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

        Class banyak tapi konsisten. Setelah kamu sering lihat pola ini, baca jadi cepat.
        """
    ),
    practice=(
        "Buka [v0.dev](https://v0.dev) atau Claude. Prompt: 'Bikin card "
        "product e-commerce dengan gambar di atas, judul, harga, dan tombol "
        "Beli. Style minimal, dark mode, accent biru.' Salin hasilnya ke "
        "Cursor. Edit satu hal kecil (misal ubah accent color) tanpa minta "
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
        "hint": "Tiga class tidak valid. Cek pola Tailwind yang sebenarnya.",
        "answer_explanation": dedent(
            """\
            Tiga kesalahan:

            1. `text-large` tidak valid. Yang benar: `text-lg` atau `text-xl`.
            2. `hover-bg-blue-600` salah pemisah. Pakai `hover:bg-blue-600` (titik dua, bukan tanda strip).
            3. `margin-top-4` tidak ada. Yang benar: `mt-4` (m = margin, t = top).
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
            "Apa filosofi utama Tailwind?",
            [
                "Wajib bikin class CSS sendiri",
                "Utility-first: pasang class kecil di markup, jarang nulis CSS sendiri",
                "Auto-generate component",
                "Hanya untuk Tailwind expert",
            ],
            "B",
            "Tailwind menyediakan banyak utility class kecil yang dikombinasikan langsung di markup. Tidak perlu pindah-pindah file CSS.",
        ),
        q(
            "Mana penulisan padding yang BENAR di Tailwind?",
            ["`padding-4`", "`p-4`", "`pad-1`", "`p4`"],
            "B",
            "Format: `[utility]-[value]`. Padding pakai `p-`, lalu skala (1 = 0.25rem, 4 = 1rem).",
        ),
        q(
            "Apa arti class `md:text-4xl`?",
            [
                "Selalu text 4xl",
                "Text jadi 4xl mulai breakpoint medium ke atas",
                "Cuma di mobile",
                "Error",
            ],
            "B",
            "Mobile-first: tanpa prefix berlaku semua ukuran, prefix `md:` aktif dari medium ke atas.",
        ),
        q(
            "Pemisah yang BENAR untuk state variant Tailwind?",
            ["Tanda strip `-`", "Titik dua `:`", "Underscore `_`", "Tidak ada pemisah"],
            "B",
            "Format: `state:utility`. Contoh `hover:bg-blue-600`, `dark:text-white`, `focus:ring-2`.",
        ),
        q(
            "Cara cepat debug tampilan yang berantakan?",
            [
                "Hapus semua kode dan mulai ulang",
                "Buka DevTools, klik elemen yang aneh, toggle class atau ubah nilai langsung di Styles panel",
                "Restart komputer",
                "Tanya AI tanpa konteks",
            ],
            "B",
            "DevTools menunjukkan class aktif dan efek styling. Tweaking real-time di sana lebih cepat daripada prompt AI bolak-balik.",
        ),
    ],
    common_mistakes=[
        "Hafal class yang tidak ada (`text-large`, `margin-top-4`). Tailwind punya pola spesifik.",
        "Pakai tanda strip untuk state variant (`hover-bg`). Yang benar titik dua (`hover:bg`).",
        "Class urut acak. Pakai prettier-plugin-tailwindcss untuk konsistensi.",
    ],
    checkpoint=[
        "Bisa baca pola class Tailwind tanpa hafal semua.",
        "Bisa prompt AI dengan deskripsi visual yang spesifik.",
        "Bisa pakai DevTools untuk debug styling.",
        "Tahu format responsive dengan prefix breakpoint.",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_PORTFOLIO_CURSOR = make_lesson(
    title="Mini Project — Portfolio Pakai Cursor + Claude",
    slug="mini-project-portfolio-cursor",
    order_index=4,
    read_time="120 menit",
    summary="Build portfolio yang tidak terlihat AI-generated.",
    tools=["Cursor", "Claude atau ChatGPT", "GitHub", "Vercel"],
    outcomes=[
        "Membangun portfolio dengan workflow Cursor + AI",
        "Polish output AI sampai terlihat 'tangan manusia'",
        "Punya URL portfolio yang lebih baik dari Level 1",
    ],
    tldr=(
        "Pakai Cursor + Claude untuk bikin portfolio Next.js + Tailwind. "
        "Fokus polish: spacing, typography, hierarchy. Hasil yang terlihat "
        "intentional, bukan asal generate."
    ),
    pembuka=dedent(
        """\
        Banyak portfolio buatan AI terlihat sama: card padding sedang, accent biru, hero terlalu pucat.

        Tujuan project ini: hasilkan portfolio yang **kelihatan dipikirkan**, bukan asal generate.

        Caranya bukan dengan code lebih banyak — tapi prompt lebih spesifik dan polish lebih telaten.
        """
    ),
    penjelasan=dedent(
        """\
        ### Spec project

        Stack: Next.js 14 + Tailwind. Tanpa backend.

        Section minimal:

        - **Hero** — nama, tagline kuat satu kalimat, dua CTA (lihat project, kontak).
        - **About** — paragraf pendek + skill list dalam grid.
        - **Projects** — minimum 3 card. Data dari array, bukan hardcode.
        - **Contact** — form sederhana atau link langsung email + social.

        ### Workflow Cursor + Claude

        - **Step 1:** Di Claude (atau ChatGPT), kasih konteks lengkap. Stack, tone, dark/light mode, accent color, font, target user. Minta plan struktur file dulu, jangan langsung kode.
        - **Step 2:** Setelah plan disepakati, minta implementasi component per component. Salin tiap output ke Cursor di file yang sesuai.
        - **Step 3:** Test lokal. Buka di Cursor, lihat di browser.
        - **Step 4:** Polish dengan ⌘K di Cursor: "Bikin spacing lebih lega di hero", "Tambah subtle animation saat card di-hover".

        ### Polish checklist

        Hal-hal kecil yang bedakan portfolio amatir vs polished:

        - **Spacing.** Section harus punya `py-24 sm:py-32`. Jangan pelit padding.
        - **Typography hierarchy.** H1 jelas lebih besar dari H2. Body text contrast tinggi dengan background.
        - **Whitespace.** Jangan tumpukan info di satu area. Beri ruang.
        - **Color discipline.** 1 accent + 2-3 grayscale. Tidak lebih.
        - **Konsistensi border-radius.** Pilih satu nilai (misal `rounded-xl`) dan pakai konsisten.
        - **Subtle animation.** `transition-all hover:scale-[1.02]` di card. Tidak berlebihan.
        - **Loading font dari Google Fonts.** Default font Tailwind oke, tapi font dari Google (Inter, Plus Jakarta Sans) lebih premium.
        - **OG image.** Untuk preview saat dibagikan di sosmed. Bisa dibikin di [og-image-builder](https://og-playground.vercel.app/) atau Figma.

        ### Tone yang pas

        Portfolio bahasa Indonesia tanpa terlihat sok English. Pakai gaya santai-profesional:

        - Buruk: "I create stunning user experiences."
        - Baik: "Saya bikin aplikasi web yang dipakai user, bukan cuma demo."

        Spesifik > umum. Honest > exaggerated.

        ### Mini project ke real project

        Portfolio ini akan jadi business card kamu untuk satu tahun ke depan. Update saat ada project baru. Treat it seperti dokumen yang hidup.

        Setelah live, bagikan ke beberapa orang yang berbeda profesi: developer, designer, non-tech. Tanya satu per satu: "Apa yang kamu paham tentang saya dari halaman ini?".

        Feedback dari tiga sudut pandang ini sangat berharga.
        """
    ),
    contoh_code_md=dedent(
        """\
        Contoh prompt komprehensif untuk Claude:

        ```text
        Saya mau bikin portfolio personal sebagai web developer pemula.

        Tech stack:
        - Next.js 14 App Router
        - Tailwind CSS
        - TypeScript
        - Tanpa backend (data project hardcode di file data/projects.ts)

        Style direction:
        - Dark mode default
        - Accent: #4EBAEC (biru terang)
        - Background: #0a0a0a
        - Font: Inter dari Google Fonts
        - Tone visual: minimal, banyak whitespace, subtle hover animations

        Struktur halaman:
        - Hero: nama besar, tagline 1 kalimat, 2 CTA (lihat project, kontak)
        - About: paragraf pendek + 6 skill dalam grid 3 kolom
        - Projects: 3 card minimum, data dari array
        - Contact: link email + social, tidak perlu form

        Tone copy: bahasa Indonesia santai-profesional. Hindari jargon Inggris berlebihan.

        Mulai dari struktur file dulu, jangan langsung kode.
        ```

        Setelah Claude kasih plan, kamu approve atau revisi. Baru implementation.
        """
    ),
    practice=(
        "Selesaikan portfolio sesuai workflow di atas. Deploy ke Vercel. "
        "Catat tiga hal: 1) berapa total prompt yang dibutuhkan? 2) Bagian "
        "mana yang paling memakan waktu? 3) Apa hal yang AI tidak bisa "
        "selesaikan sampai harus di-edit manual?"
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
        "hint": "Output AI tanpa direction = output generic. Kamu yang harus pegang taste-nya.",
        "answer_explanation": dedent(
            """\
            Kesalahan: prompt vague + tidak ada feedback iteratif.

            Hasilnya generic karena AI tidak punya konteks tentang siapa kamu, gaya yang kamu mau, dan target user.

            Yang benar: prompt yang spesifik (lihat contoh di atas), lalu iterasi feedback dengan istilah desain yang tepat. "Spacing-nya kurang lega di hero" lebih efektif dari "kurang oke".
            """
        ),
        "fixed_code": dedent(
            """\
            User: [Prompt komprehensif seperti contoh di atas]
            AI: [Plan struktur file]
            User: "Plan oke. Lanjut implementasi Hero dulu."
            AI: [Hero component]
            User: "Spacing di hero masih sempit. Naikkan py-32 sm:py-48.
                  Tagline masih English. Ubah ke 'Saya bikin aplikasi web
                  yang berguna, bukan cuma demo.'"
            AI: [Hero versi revisi]
            ... [iterasi sampai puas]
            """
        ),
    },
    quiz=[
        q(
            "Apa yang membedakan portfolio polished dari portfolio AI generic?",
            [
                "Banyak animasi mencolok",
                "Spacing yang lega, typography hierarchy jelas, color discipline, konsistensi",
                "Pakai banyak warna",
                "Code yang panjang",
            ],
            "B",
            "Detail kecil ini cumulative effect-nya besar. Portfolio yang terlihat dipikirkan vs asal generate.",
        ),
        q(
            "Mana praktik prompt yang BAIK untuk AI?",
            [
                "Singkat: 'Bikin portfolio'",
                "Konteks lengkap: stack, style, tone, struktur, dan minta plan dulu",
                "Acak-acakan",
                "Cuma sebut warna",
            ],
            "B",
            "Konteks komprehensif = output akurat. Tanpa konteks, AI ngarang dengan bias generic.",
        ),
        q(
            "Apa fungsi 'iterasi feedback' setelah AI kasih draft?",
            [
                "Tidak penting",
                "Untuk arahkan AI ke arah yang lebih spesifik dengan vocabulary desain yang tepat",
                "Untuk basa-basi",
                "Cuma untuk professional",
            ],
            "B",
            "Iterasi adalah inti vibe coding. AI jarang langsung tepat di percobaan pertama. Kamu yang pegang taste.",
        ),
        q(
            "Color discipline yang BAIK untuk portfolio pemula?",
            [
                "Banyak warna supaya menarik",
                "1 accent + 2-3 grayscale",
                "Pelangi",
                "Hitam putih saja",
            ],
            "B",
            "Color theory: terlalu banyak warna = chaos. Sedikit warna dengan kontras yang tepat = polished.",
        ),
        q(
            "Apa hal yang sebaiknya dilakukan setelah portfolio live?",
            [
                "Tinggal lupakan",
                "Bagikan ke 3 orang dari profesi berbeda dan tanya kesan mereka",
                "Update tiap menit",
                "Hapus dan ulang",
            ],
            "B",
            "Feedback dari mata yang berbeda mengungkap blind spot. Tidak semua orang punya konteks teknis kamu.",
        ),
    ],
    common_mistakes=[
        "Prompt vague. Hasilnya generic.",
        "Tidak iterasi. AI jarang langsung kasih hasil paling tepat.",
        "Copy text English yang sok-sokan. Buat copy bahasa Indonesia yang jujur.",
    ],
    checkpoint=[
        "Portfolio live di Vercel.",
        "Kelihatan dipikirkan: spacing, typography, color discipline.",
        "Sudah dapat feedback dari minimal 3 orang dengan profesi berbeda.",
        "Workflow Cursor + AI sudah enak — tahu kapan AI cukup, kapan perlu polish manual.",
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
        "Mental model client-server, React, dan styling cepat dengan "
        "Tailwind. Tutup level dengan portfolio yang dibangun lewat "
        "workflow Cursor + AI yang efektif."
    ),
    duration="~2 minggu",
    difficulty="Pemula → Menengah",
    accent_color="from-pink-400/30 to-violet-500/10",
    mini_project="Portfolio Pakai Cursor + Claude",
    tags=["React", "Tailwind", "Mental Model", "AI Workflow"],
    lessons=[LESSON_WEB, LESSON_REACT_MENTAL, LESSON_TW_VIBE, PROJECT_PORTFOLIO_CURSOR],
)
