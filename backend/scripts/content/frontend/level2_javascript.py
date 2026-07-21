"""
Frontend / Level 2 — JavaScript Dasar.

Lessons:
  1. dasar-javascript
  2. function-dan-scope
  3. dom-manipulation
  4. mini-project-interactive-todo  (project)
"""

from textwrap import dedent

from .._template import make_lesson, make_level, q


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 1 — Dasar JavaScript
# ─────────────────────────────────────────────────────────────────────────────

LESSON_JS_BASICS = make_lesson(
    title="Dasar JavaScript",
    slug="dasar-javascript",
    order_index=1,
    read_time="12 menit",
    summary="Variable, tipe data, operator, dan percabangan.",
    tools=["Browser modern", "VS Code", "DevTools (F12) → Console"],
    outcomes=[
        "Bisa nulis variable yang aman pake `const` dan `let`",
        "Bisa pake operator dan template literal",
        "Bisa bikin percabangan dengan `if/else` dan ternary",
    ],
    tldr=(
        "JavaScript itu yang bikin halaman bisa diklik dan bergerak. Default "
        "pake `const`. Pake `let` cuma kalau memang berubah. Selalu pake "
        "`===` (triple equals). Gabung string pake backtick `${...}`."
    ),
    pembuka=dedent(
        """\
        HTML bikin struktur. CSS bikin cantik. Tapi kalau mau halaman kamu bisa diklik, ngitung sesuatu, atau ngegerakin tombol — kamu butuh JavaScript.

        Ibaratin gini: HTML itu kerangka rumah, CSS itu catnya, JavaScript itu yang bikin saklar lampu nyala dan kipas berputar.

        Kabar baiknya: JS jalan langsung di browser. Gak perlu install apa-apa buat mulai.
        """
    ),
    penjelasan=dedent(
        """\
        ### Cara pake JavaScript

        JS bisa ditulis di file `.js` terpisah, terus disambungin ke HTML pake `<script src="app.js"></script>`. Atau langsung di HTML buat coba-coba kecil.

        Buat debug, pake `console.log()`. Hasilnya muncul di browser console (Tekan F12 → tab Console). Ini bakal jadi temen terbaik kamu pas belajar.

        ### Variable — wadah data

        Anggep variable itu kotak yang ada labelnya, buat nyimpen sesuatu.

        - `const` — buat nilai yang gak bakal berubah. **Default pake ini.**
        - `let` — buat nilai yang emang bakal berubah.
        - `var` — peninggalan jaman dulu, hindarin.

        Aturan praktisnya: default `const`, pake `let` cuma kalau memang harus berubah.

        ### Tipe data dasar

        - `string` — buat teks, ditulis pake kutip: `"Halo"` atau `'Halo'`
        - `number` — buat angka: `42`, `3.14`
        - `boolean` — buat true/false
        - `null` — artinya "ada, tapi sengaja kosong"
        - `undefined` — artinya "belum diisi"
        - `array` — buat list: `[1, 2, 3]`
        - `object` — buat struktur key-value: `{ nama: "Acel", umur: 22 }`

        ### Operator yang penting

        Operator matematika kayak biasa: `+`, `-`, `*`, `/`. Tambah satu yang sering muncul: `%` (sisa bagi, modulo).

        Buat ngebandingin, **selalu pake `===` (triple equals)**, jangan `==` (double). Yang triple ngecek nilai DAN tipe. Yang double sering kasih hasil mengejutkan.

        Operator logika: `&&` (AND), `||` (OR), `!` (NOT).

        ### Template literal

        Daripada gabung string pake `+`, mendingan pake backtick (`` ` ``). Kamu bisa nyisipin variable pake `${...}`.

        Backtick itu ada di pojok kiri atas keyboard, di bawah Esc. Lebih enak dibaca, dan support baris baru juga.

        ### Conditional

        `if/else` buat percabangan. Kalau cuma butuh dua opsi pendek, pake ternary: `kondisi ? hasil_true : hasil_false`.

        Banyak pemula awal-awal suka bingung pas liat `===` vs `==`. Aturannya simpel: selalu pake `===`. Itu satu kebiasaan yang bakal nyelametin kamu dari banyak bug aneh.
        """
    ),
    contoh_code_md=dedent(
        """\
        ```js
        const nama = "Acel";
        const umur = 22;
        let saldo = 100000;          // bisa berubah

        // Tipe data
        const teman = ["Andi", "Budi"];
        const profil = { nama: "Acel", umur: 22 };

        // Operator
        console.log(10 / 3);          // 3.333...
        console.log(10 % 3);          // 1
        console.log(5 === "5");       // false (tipe beda)
        console.log(5 === 5);         // true

        // Template literal
        const pesan = `Halo ${nama}, umur ${umur}.`;
        console.log(pesan);

        // Conditional
        const nilai = 75;
        if (nilai >= 80) {
          console.log("Lulus dengan baik");
        } else if (nilai >= 60) {
          console.log("Lulus");
        } else {
          console.log("Coba lagi");
        }

        // Ternary versi pendek
        const status = nilai >= 60 ? "Lulus" : "Tidak lulus";
        console.log(status);
        ```
        """
    ),
    practice=(
        "Bikin file `app.js` isinya variable `namaKamu` dan `tahunLahir`. "
        "Itung umur dengan asumsi tahun ini 2026. Tampilin ke console pake "
        "template literal: `Halo, saya {nama} berumur {umur} tahun.`"
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            let nama = 'Acel;
            const umur == 22
            console.log("Nama: " + nama + ", umur: " umur);

            if (umur > 18) {
              console.log("Dewasa")
            }
            """
        ),
        "hint": (
            "Empat masalah: tutupan kutip string, operator yang salah dipake, "
            "gabung string yang kurang `+`, sama akhir baris."
        ),
        "answer_explanation": dedent(
            """\
            1. `'Acel;` kurang kutip penutup. Ganti jadi `"Acel"` atau `'Acel'`.
            2. `const umur == 22` salah operator. Buat assign pake `=` (single), bukan `==`.
            3. `"Nama: " + nama + ", umur: " umur` kurang `+` antara `", umur: "` sama `umur`.
            4. `console.log("Dewasa")` di blok if mendingan diakhirin `;` biar konsisten.
            """
        ),
        "fixed_code": dedent(
            """\
            const nama = "Acel";
            const umur = 22;
            console.log(`Nama: ${nama}, umur: ${umur}`);

            if (umur > 18) {
              console.log("Dewasa");
            }
            """
        ),
    },
    quiz=[
        q(
            "Mana yang paling tepat buat variable yang nilainya gak bakal berubah?",
            ["`var`", "`let`", "`const`", "`static`"],
            "C",
            "`const` ngunci variable biar gak bisa di-assign ulang. Default pake `const`, pake `let` kalau memang harus berubah.",
        ),
        q(
            "Apa hasil dari `5 === \"5\"`?",
            ["`true`", "`false`", "`\"5\"`", "Error"],
            "B",
            "`===` ngecek nilai DAN tipe. Number 5 sama string \"5\" itu tipenya beda, jadi `false`.",
        ),
        q(
            "Apa output dari `const a = 4; const b = \"2\"; console.log(a + b);`?",
            ["`6`", "`42`", "`\"42\"`", "Error"],
            "C",
            "Kalau salah satu sisi `+` itu string, JavaScript ngubah yang lain jadi string juga, terus digabung. Hasilnya string `\"42\"`.",
        ),
        q(
            "Mana cara yang BENER nulis template literal?",
            [
                "`\"Halo $nama\"`",
                "`'Halo $nama'`",
                "`` `Halo ${nama}` ``",
                "`\"Halo {nama}\"`",
            ],
            "C",
            "Template literal pake **backtick** (`` ` ``), bukan kutip biasa, dan placeholder ditulis `${...}`.",
        ),
        q(
            "Apa yang dicetak ke console dari `const status = 50 >= 60 ? \"Lulus\" : \"Coba lagi\"; console.log(status);`?",
            ["`Lulus`", "`Coba lagi`", "`60`", "`undefined`"],
            "B",
            "Ternary: `kondisi ? hasil_true : hasil_false`. `50 >= 60` itu false, jadi yang dijalanin `\"Coba lagi\"`.",
        ),
    ],
    common_mistakes=[
        "Pake `==` bukan `===`. Bisa kasih hasil mengejutkan, contohnya `0 == false` itu `true`.",
        "Lupa kutip penutup string. Sisa baris jadi error parsing.",
        "Ketuker `=` (assign) sama `===` (compare).",
    ],
    checkpoint=[
        "Tau kapan pake `const` vs `let`",
        "Bisa baca tipe data: string, number, boolean, array, object",
        "Selalu pake `===` buat ngebandingin",
        "Bisa pake template literal buat gabung string + variable",
    ],
    xp_reward=80,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 — Function & Scope
# ─────────────────────────────────────────────────────────────────────────────

LESSON_JS_FUNCTION = make_lesson(
    title="Function & Scope",
    slug="function-dan-scope",
    order_index=2,
    read_time="12 menit",
    summary="Function modern, scope, closure, dan higher-order function.",
    tools=["Browser modern", "VS Code", "Console"],
    outcomes=[
        "Bisa nulis function dalam tiga gaya berbeda",
        "Paham scope dan closure",
        "Bisa pake `map`, `filter`, dan `reduce` di array",
    ],
    tldr=(
        "Function itu mesin kecil yang nerima input dan ngembaliin hasil. "
        "Default pake arrow function. Scope = wilayah hidup variable. "
        "`map`/`filter`/`reduce` itu trio penting di array."
    ),
    pembuka=dedent(
        """\
        Function itu mesin kecil yang nerima input, ngerjain sesuatu, terus ngembaliin hasil.

        Sama function, kamu bisa nulis logika sekali, terus pake berkali-kali.

        Tanpa function, kode kamu cepet berantakan. Kamu bakal copy-paste logika yang sama berulang-ulang.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga gaya nulis function

        Tiganya ngelakuin hal yang sama. Aturan praktisnya: default pake arrow function, kecuali butuh akses `this` di method object.

        - **Function declaration:** `function sapa(nama) { return ... }`
        - **Function expression:** `const sapa = function(nama) { return ... }`
        - **Arrow function:** `const sapa = (nama) => ...`

        ### Parameter, return, default

        Parameter itu input yang masuk. Return itu output yang keluar. Kalau function gak punya `return`, dia ngembaliin `undefined`.

        Default parameter bikin function tetep jalan walau argumen gak dikasih, contohnya `(nama = "Teman") => ...`.

        ### Scope — wilayah kekuasaan variable

        Variable yang dibikin di dalem function gak bisa diakses dari luar. Tapi function yang ada di dalem function lain bisa akses variable di luarnya. Ini namanya **closure**.

        ### Closure dengan analogi

        Anggep tiap function itu orang yang bawa tas. Pas function dibuat, dia masukin variable di sekitarnya ke dalem tas. Walau function-nya "pindah lokasi", isi tasnya tetep dibawa.

        Contohnya pas kamu bikin counter atau private state — closure yang jaga datanya.

        Banyak pemula bingung di bagian ini. Santai aja — kamu bakal sering ketemu pas pake React nanti, dan saat itu konsep ini bakal lebih masuk akal.

        ### Higher-order function

        Function yang nerima function lain sebagai argumen. Tiga teman karib di JavaScript modern:

        - `map` — ngubah tiap elemen array
        - `filter` — milih elemen yang sesuai kondisi
        - `reduce` — ngegabungin semua elemen jadi satu nilai

        Tiganya ngegantiin banyak loop manual dan bikin kode lebih ringkas.
        """
    ),
    contoh_code_md=dedent(
        """\
        ```js
        // Tiga gaya function
        function sapa(nama) {
          return `Halo, ${nama}!`;
        }

        const sapaJuga = function(nama) {
          return `Halo, ${nama}!`;
        };

        const sapaModern = (nama) => `Halo, ${nama}!`;

        // Default parameter
        const beri = (nama = "Teman") => `Halo, ${nama}!`;
        console.log(beri());          // "Halo, Teman!"
        console.log(beri("Acel"));    // "Halo, Acel!"

        // Closure: counter sederhana
        function buatPenghitung() {
          let count = 0;
          return () => {
            count = count + 1;
            return count;
          };
        }

        const naik = buatPenghitung();
        console.log(naik());  // 1
        console.log(naik());  // 2
        console.log(naik());  // 3

        // Higher-order
        const angka = [1, 2, 3, 4, 5];
        const dobel = angka.map(n => n * 2);            // [2, 4, 6, 8, 10]
        const genap = angka.filter(n => n % 2 === 0);   // [2, 4]
        const total = angka.reduce((acc, n) => acc + n, 0);  // 15
        ```
        """
    ),
    practice=(
        "Bikin function `hitungTotal(harga, jumlah, diskon)` yang ngitung "
        "harga × jumlah, terus dikurangin pake persentase diskon (`0.1` buat "
        "10%). Return total akhir. Panggil pake `hitungTotal(50000, 3, 0.2)` "
        "— hasil yang diharapin: 120000."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            function sapa(nama)
              return "Halo, " + nama;
            }

            const tambah = (a, b) => {
              a + b
            };

            console.log(sapa("Acel"));
            console.log(tambah(2, 3));
            """
        ),
        "hint": (
            "Function declaration butuh kurung kurawal pembuka. Arrow function "
            "dengan `{}` butuh kata kunci eksplisit buat ngembaliin nilai."
        ),
        "answer_explanation": dedent(
            """\
            1. `function sapa(nama)` kurang `{` setelah parameter.
            2. Arrow function `(a, b) => { a + b }` gak return apa-apa. Pas pake `{}`, kamu wajib nulis `return`. Atau ilangin `{}`-nya biar return implisit.
            """
        ),
        "fixed_code": dedent(
            """\
            function sapa(nama) {
              return "Halo, " + nama;
            }

            const tambah = (a, b) => {
              return a + b;
            };

            // atau lebih ringkas:
            // const tambah = (a, b) => a + b;

            console.log(sapa("Acel"));
            console.log(tambah(2, 3));
            """
        ),
    },
    quiz=[
        q(
            "Apa hasil `add(2, 3)` kalau `const add = (a, b) => a + b;`?",
            ["`undefined`", "`5`", "`\"23\"`", "Error"],
            "B",
            "Arrow function tanpa kurung kurawal otomatis return ekspresi setelah `=>`.",
        ),
        q(
            "Apa beda `(a) => { a + 1 }` sama `(a) => a + 1`?",
            [
                "Gak ada bedanya",
                "Yang pertama gak return apa-apa (return undefined). Yang kedua return `a + 1`",
                "Yang pertama lebih cepet",
                "Yang pertama syntax salah",
            ],
            "B",
            "Pas pake `{}`, kamu wajib nulis `return` kalau mau ngembaliin nilai. Tanpa `{}`, ekspresi setelah `=>` otomatis di-return.",
        ),
        q(
            "Apa output dari `function tampil() { const pesan = \"Halo\"; } tampil(); console.log(pesan);`?",
            [
                "`\"Halo\"`",
                "`undefined`",
                "Error: `pesan is not defined`",
                "`null`",
            ],
            "C",
            "Variable `pesan` cuma hidup di dalem scope function. Di luar function dia gak ada.",
        ),
        q(
            "Apa hasil `[1,2,3,4].filter(n => n > 2)`?",
            ["`[1, 2, 3, 4]`", "`[3, 4]`", "`[1, 2]`", "`2`"],
            "B",
            "`filter` ngembaliin array yang isinya elemen yang lulus kondisi. Cuma 3 sama 4 yang lebih gede dari 2.",
        ),
        q(
            "Apa hasil `[1,2,3,4].reduce((acc, n) => acc + n, 0)`?",
            ["`0`", "`4`", "`10`", "`[1,2,3,4]`"],
            "C",
            "`reduce` ngegabungin semua elemen jadi satu nilai. Mulai dari 0, terus ditambahin: 0+1+2+3+4 = 10.",
        ),
    ],
    common_mistakes=[
        "Pake arrow function `(a) => { a + 1 }` terus heran kenapa hasilnya `undefined`. Pake `return` atau ilangin `{}`.",
        "Ketuker parameter sama argumen. Parameter itu nama di definisi function. Argumen itu nilai yang dikirim pas manggil.",
        "Coba akses variable yang dibikin di dalem function dari luar. Itu di luar scope.",
    ],
    checkpoint=[
        "Bisa nulis function dalam tiga gaya",
        "Tau kapan butuh `return` eksplisit di arrow function",
        "Bisa pake `map`, `filter`, `reduce` di kasus sederhana",
        "Paham apa itu scope dan kenapa closure berguna",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — DOM Manipulation
# ─────────────────────────────────────────────────────────────────────────────

LESSON_JS_DOM = make_lesson(
    title="DOM Manipulation — Bikin Halaman Bisa Berubah",
    slug="dom-manipulation",
    order_index=3,
    read_time="14 menit",
    summary="Milih elemen, ngubah konten, dan ngerespon aksi user.",
    tools=["Browser modern", "VS Code", "DevTools (Console + Elements)"],
    outcomes=[
        "Bisa milih elemen pake `querySelector`",
        "Bisa ngubah teks dan style dari JavaScript",
        "Bisa ngerespon klik, input, dan submit pake event listener",
        "Bisa bikin dan hapus elemen secara dinamis",
    ],
    tldr=(
        "DOM = peta halaman yang bisa diubah JavaScript. Pilih pake "
        "`querySelector`. Ubah pake `textContent`/`classList`. Reaksi pake "
        "`addEventListener`."
    ),
    pembuka=dedent(
        """\
        Sampe sini, kode JavaScript kamu cuma jalan di console. Saatnya bikin halaman bisa bereaksi ke aksi user.

        Pekerjaan ini namanya DOM manipulation.

        Habis lesson ini, kamu bisa bikin tombol yang berfungsi, form yang divalidasi, dan list yang bisa ditambah/hapus.
        """
    ),
    penjelasan=dedent(
        """\
        ### DOM itu apa

        DOM (Document Object Model) itu cara JavaScript ngeliat halaman HTML — sebagai object yang bisa dimanipulasi.

        Anggep DOM itu peta rumah versi digital dari HTML kamu. Kamu bisa pake JavaScript buat mindahin pintu, ngeganti warna dinding, atau nambah jendela tanpa rewrite seluruh HTML.

        ### Milih elemen

        - `document.querySelector(...)` — ngambil **elemen pertama** yang cocok sama selector CSS
        - `document.querySelectorAll(...)` — ngambil **semua** yang cocok, dalam bentuk NodeList

        Selector yang dipake persis sama dengan CSS: `h1`, `.judul`, `#hero`, `nav a`.

        ### Ngubah konten

        - `el.textContent = "..."` — ubah teks (aman dari XSS)
        - `el.innerHTML = "..."` — ubah pake HTML (hati-hati kalau inputnya dari user)

        Aturan praktisnya: pake `textContent` kalau cuma ubah teks. Pake `innerHTML` cuma kalau memang butuh element baru, dan pastiin inputnya bukan dari user.

        ### Ngubah style

        Buat perubahan kecil pake `el.style.namaProperty`. Tapi buat perubahan gede mendingan **toggle class**:

        - `el.classList.add("active")`
        - `el.classList.remove("hidden")`
        - `el.classList.toggle("dark-mode")`
        - `el.classList.contains("active")` returns boolean

        Terus definisiin style-nya di CSS.

        ### Event listener

        `el.addEventListener("namaEvent", callback)` itu cara modern buat ngerespon aksi user.

        Event yang sering dipake: `click`, `input`, `submit`, `keydown`/`keyup`, `mouseenter`/`mouseleave`.

        Buat form, `e.preventDefault()` ngecegah halaman reload. Buat link, ngecegah navigasi default.

        ### Bikin sama hapus elemen

        `document.createElement("li")` bikin elemen baru di memory. `parent.appendChild(el)` masukin ke parent. `el.remove()` hapus dari halaman.

        ### Baca isi input

        Buat input field, jangan pake `textContent`. Pake `el.value`. Itu property khusus buat input.

        Banyak pemula awalnya kepleset di sini. Mereka pake `textContent` di input dan bingung kenapa hasilnya kosong.
        """
    ),
    contoh_code_md=dedent(
        """\
        Mini todo list:

        ```html
        <input id="input-todo" placeholder="Tulis tugas...">
        <button id="btn-tambah">Tambah</button>
        <ul id="list-todo"></ul>
        ```

        ```js
        const input = document.querySelector("#input-todo");
        const tombol = document.querySelector("#btn-tambah");
        const list = document.querySelector("#list-todo");

        tombol.addEventListener("click", () => {
          const teks = input.value.trim();
          if (!teks) return;          // jangan tambah kalau kosong

          const item = document.createElement("li");
          item.textContent = teks;

          // klik item buat tandain selesai
          item.addEventListener("click", () => {
            item.classList.toggle("selesai");
          });

          list.appendChild(item);
          input.value = "";           // bersihin input
        });
        ```

        ```css
        .selesai {
          text-decoration: line-through;
          opacity: 0.5;
        }
        ```
        """
    ),
    practice=(
        "Bikin halaman dengan satu tombol bertuliskan 'Klik aku' dan satu "
        "paragraf di bawahnya. Tiap kali tombol diklik, tambahin angka di "
        "paragraf, mulai dari 0. Tampilan: 'Klik: 1', terus 'Klik: 2', dst."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            const tombol = document.queryselector("#btn");
            const input = document.querySelector(".input");

            tombol.addEventListener("click", () {
              const nilai = input.text;
              console.log(nilai);
            });
            """
        ),
        "hint": (
            "Cek penulisan nama method (case-sensitive), syntax callback "
            "function, sama property apa yang dipake buat ngambil nilai input."
        ),
        "answer_explanation": dedent(
            """\
            1. `queryselector` salah. Yang bener `querySelector` (case-sensitive).
            2. Callback `() {}` kurang `=>`. Harusnya `() => { ... }`.
            3. `input.text` salah. Buat ngambil isi input pake `input.value`.
            """
        ),
        "fixed_code": dedent(
            """\
            const tombol = document.querySelector("#btn");
            const input = document.querySelector(".input");

            tombol.addEventListener("click", () => {
              const nilai = input.value;
              console.log(nilai);
            });
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dikembaliin `document.querySelectorAll(\".card\")`?",
            [
                "Satu elemen pertama yang cocok",
                "Daftar (NodeList) isinya semua elemen yang cocok",
                "Array elemen",
                "`null` kalau gak ditemuin",
            ],
            "B",
            "`querySelector` ambil yang pertama. `querySelectorAll` ambil semua, dalam bentuk NodeList yang mirip array.",
        ),
        q(
            "Mana cara yang aman buat update teks elemen tanpa risiko XSS?",
            [
                "`el.innerHTML = userInput`",
                "`el.textContent = userInput`",
                "`el.value = userInput`",
                "`el.text = userInput`",
            ],
            "B",
            "`textContent` ngeperlakuin input sebagai teks biasa. `innerHTML` ngeksekusi sebagai HTML — risiko inject script kalau dari user.",
        ),
        q(
            "Apa fungsi `e.preventDefault()` di dalem event listener?",
            [
                "Ngehentiin event listener",
                "Ngecegah perilaku default browser (form submit / link navigasi)",
                "Hapus elemen",
                "Ngebatalin semua event",
            ],
            "B",
            "Form normalnya reload. Link normalnya navigasi. `preventDefault()` ngecegah perilaku default itu.",
        ),
        q(
            "Apa output `el.classList.toggle(\"aktif\"); el.classList.toggle(\"aktif\");`?",
            [
                "Class `aktif` tetep nempel",
                "Class `aktif` gak nempel (balik ke kondisi awal)",
                "Error",
                "Ditambahin dua kali",
            ],
            "B",
            "Toggle kayak saklar lampu. Kalau OFF jadi ON, kalau ON jadi OFF. Dua kali toggle balik ke kondisi awal.",
        ),
        q(
            "Mana cara yang BENER baca isi `<input id=\"email\">`?",
            [
                "`document.querySelector(\"#email\").text`",
                "`document.querySelector(\"#email\").value`",
                "`document.querySelector(\"#email\").innerHTML`",
                "`document.querySelector(\"#email\").textContent`",
            ],
            "B",
            "Input form nyimpen nilainya di property `value`. `textContent`/`innerHTML` buat konten teks elemen biasa.",
        ),
    ],
    common_mistakes=[
        "Pake `el.text` bukan `el.value` buat input. Hasilnya `undefined`.",
        "Lupa `e.preventDefault()` di handler form. Halaman reload tiap submit.",
        "Pake `innerHTML` dengan input dari user. Berpotensi XSS.",
    ],
    checkpoint=[
        "Bisa pilih elemen pake `querySelector`",
        "Bisa ubah teks dan toggle class",
        "Bisa pasang event listener buat klik dan input",
        "Bisa bikin elemen baru dan masukin ke halaman",
    ],
    xp_reward=120,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 — Mini Project (LAST in level)
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_TODO = make_lesson(
    title="Mini Project — Interactive Todo App",
    slug="mini-project-interactive-todo",
    order_index=4,
    read_time="90 menit",
    summary="App pertama dengan state, render, dan localStorage.",
    tools=["VS Code", "Browser modern", "GitHub", "Vercel"],
    outcomes=[
        "Bisa bangun app dengan siklus input → simpan → render",
        "Bisa pake `localStorage` buat nyimpen data lokal",
        "Bisa misahin logika state dari logika DOM",
    ],
    tldr=(
        "Bangun todo app yang bisa tambah/tandain/hapus, datanya tersimpan "
        "di `localStorage`. Pake pola: array of state + function `render()` "
        "yang nge-gambar ulang dari state."
    ),
    pembuka=dedent(
        """\
        Saatnya bikin app pertama yang nyimpen data dan punya state.

        Habis project ini, kamu paham siklus dasar app interaktif: input → simpan → tampilin → ubah → hapus.

        Ini pola yang dipake di hampir semua app modern, dari catatan kecil sampe dashboard kompleks.
        """
    ),
    penjelasan=dedent(
        """\
        ### Yang kamu bangun

        Todo list yang bisa tambah task, tandain selesai, hapus, dan datanya tetep ada walau halaman di-refresh.

        ### Konsep baru: localStorage

        `localStorage` itu tempat nyimpen di browser yang bertahan walau halaman ditutup.

        - `localStorage.setItem("key", "string")` — simpan
        - `localStorage.getItem("key")` — ambil (string atau null)
        - `localStorage.removeItem("key")` — hapus

        Karena localStorage cuma nyimpen string, kalau mau nyimpen array/object pake `JSON.stringify()` pas nyimpen dan `JSON.parse()` pas ngambil.

        ### Pola "state + render"

        Pisahin logika state (array of tasks) dari logika DOM (gambar ulang list).

        - `tugas` = array yang nyimpen semua task
        - `render()` = function yang gambar ulang list dari `tugas`
        - `save()` = function yang simpan `tugas` ke localStorage

        Tiap kali ada perubahan (tambah/edit/hapus), update `tugas`, panggil `save()`, terus `render()`.

        ### Kenapa pola ini penting

        Pola ini bakal kamu pake sepanjang karier. Library gede kayak React pake ide yang sama, cuma lebih otomatis.
        """
    ),
    contoh_code_md=dedent(
        """\
        ```html
        <input id="input" placeholder="Tulis tugas...">
        <button id="tambah">Tambah</button>
        <ul id="list"></ul>
        ```

        ```js
        let tugas = JSON.parse(localStorage.getItem("tugas") || "[]");

        const input = document.querySelector("#input");
        const btn = document.querySelector("#tambah");
        const list = document.querySelector("#list");

        function save() {
          localStorage.setItem("tugas", JSON.stringify(tugas));
        }

        function render() {
          list.innerHTML = "";

          if (tugas.length === 0) {
            const empty = document.createElement("li");
            empty.textContent = "Belum ada tugas";
            empty.classList.add("kosong");
            list.appendChild(empty);
            return;
          }

          for (const t of tugas) {
            const li = document.createElement("li");
            li.textContent = t.teks;
            if (t.selesai) li.classList.add("selesai");

            li.addEventListener("click", () => {
              t.selesai = !t.selesai;
              save();
              render();
            });

            list.appendChild(li);
          }
        }

        btn.addEventListener("click", () => {
          const teks = input.value.trim();
          if (!teks) return;
          tugas.push({ id: Date.now(), teks, selesai: false });
          input.value = "";
          save();
          render();
        });

        render();
        ```
        """
    ),
    practice=(
        "Selesain todo app di atas, terus tambahin tombol hapus per item "
        "(misal klik kanan buat hapus, atau tombol 'x' kecil di sebelah "
        "kanan). Kasih styling yang rapi dan deploy ke Vercel."
    ),
    fix_error={
        "language": "js",
        "broken_code": dedent(
            """\
            let tugas = localStorage.getItem("tugas") || [];

            function save() {
              localStorage.setItem("tugas", tugas);
            }

            function render() {
              for (const t of tugas) {
                const li = document.createElement("li");
                li.textContent = t.teks;
                list.appendChild(li);
              }
            }
            """
        ),
        "hint": (
            "localStorage cuma nyimpen string. Cek gimana kamu baca dan tulis "
            "data. Render juga belum bersihin list lama sebelum gambar."
        ),
        "answer_explanation": dedent(
            """\
            1. `getItem` ngembaliin string atau null. Harus di-`JSON.parse`. Default-nya `"[]"`, terus di-parse.
            2. `setItem` butuh string. Harus `JSON.stringify(tugas)`.
            3. `render()` lupa `list.innerHTML = ""` di awal. Hasilnya tiap render numpuk sama list lama.
            """
        ),
        "fixed_code": dedent(
            """\
            let tugas = JSON.parse(localStorage.getItem("tugas") || "[]");

            function save() {
              localStorage.setItem("tugas", JSON.stringify(tugas));
            }

            function render() {
              list.innerHTML = "";
              for (const t of tugas) {
                const li = document.createElement("li");
                li.textContent = t.teks;
                list.appendChild(li);
              }
            }
            """
        ),
    },
    quiz=[
        q(
            "Apa yang dikembaliin `localStorage.getItem(\"key\")` pas key belum ada?",
            ["`undefined`", "`null`", "`\"\"`", "Error"],
            "B",
            "Pas key belum ada, `getItem` ngembaliin `null`. Itu kenapa kita pake `|| \"[]\"` buat default.",
        ),
        q(
            "Kenapa kita pake `JSON.stringify` pas nyimpen array ke localStorage?",
            [
                "Biar lebih cepet",
                "localStorage cuma nyimpen string, jadi array harus diubah jadi string dulu",
                "Buat enkripsi data",
                "Gak perlu sebenernya",
            ],
            "B",
            "localStorage nyimpen string aja. Array/object harus di-stringify pas nyimpen dan di-parse pas ngambil.",
        ),
        q(
            "Kenapa `render()` ngebersihin `list.innerHTML = \"\"` di awal?",
            [
                "Buat ngehemat memory",
                "Biar isi lama gak numpuk sama isi baru pas digambar ulang",
                "Buat ngebersihin localStorage",
                "Gak perlu sebenernya",
            ],
            "B",
            "Tanpa ngebersihin, tiap render bakal numpuk item ke list yang udah ada. Bersihin dulu, terus gambar dari state terbaru.",
        ),
        q(
            "Mana praktik yang paling baik dalam pola state + render?",
            [
                "Mutasi DOM langsung dari banyak tempat",
                "Update state, simpan, terus panggil render() yang gambar ulang dari state",
                "Pake variable global buat semuanya",
                "Gak perlu render(), cukup append doang",
            ],
            "B",
            "Pola ini bikin satu sumber kebenaran (state) dan render-nya konsisten. Library gede kayak React pake ide yang sama.",
        ),
        q(
            "Pas bikin task baru, kenapa kita pake `Date.now()` sebagai id?",
            [
                "Karena angka yang gede keliatan profesional",
                "Buat ngehasilin id unik berdasarkan waktu pembuatan",
                "Karena UUID gak ada di JavaScript",
                "Gak ada alasan, bisa juga pake nama task sebagai id",
            ],
            "B",
            "`Date.now()` ngembaliin timestamp dalam ms. Cukup unik buat app sederhana. Kalau butuh yang lebih kuat, pake `crypto.randomUUID()`.",
        ),
    ],
    common_mistakes=[
        "Lupa `JSON.parse` pas baca dari localStorage. Hasilnya `tugas` jadi string, bukan array.",
        "Manipulasi DOM dari banyak tempat tanpa pola render terpusat. Susah di-debug.",
        "Gak handle empty state. List kosong bikin halaman keliatan broken.",
    ],
    checkpoint=[
        "App live di Vercel dengan URL publik",
        "Bisa tambah, tandain selesai, dan hapus task",
        "Data tetep ada habis refresh",
        "Kode dipisah jelas: state, save, render",
    ],
    xp_reward=300,
    is_project=True,
)


# ─────────────────────────────────────────────────────────────────────────────
# Level
# ─────────────────────────────────────────────────────────────────────────────

LEVEL = make_level(
    number=2,
    slug="javascript-dasar",
    title="JavaScript Dasar",
    subtitle="Bikin halaman bisa diklik dan bergerak",
    description=(
        "Variable, function, scope, dan DOM manipulation. Habis level ini "
        "kamu bisa bikin halaman yang interaktif dan punya todo app live "
        "di internet."
    ),
    duration="~2 minggu",
    difficulty="Pemula → Menengah",
    accent_color="from-amber-400/30 to-violet-500/10",
    mini_project="Interactive Todo App",
    tags=["ES6+", "DOM", "Event", "localStorage"],
    lessons=[LESSON_JS_BASICS, LESSON_JS_FUNCTION, LESSON_JS_DOM, PROJECT_TODO],
)
