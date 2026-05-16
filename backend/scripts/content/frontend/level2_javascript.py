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
    summary="Variable, tipe data, operator, conditional, dan template literal.",
    tools=["Browser modern", "VS Code", "DevTools (F12) → Console"],
    outcomes=[
        "Menulis variable yang aman dengan `const` dan `let`",
        "Memakai operator dan template literal",
        "Membuat percabangan dengan `if/else` dan ternary",
    ],
    tldr=(
        "JavaScript itu sistem listriknya halaman. `const` default, `let` "
        "kalau berubah. Selalu `===` (triple equals). Pakai backtick untuk "
        "template literal."
    ),
    pembuka=dedent(
        """\
        HTML bikin struktur. CSS bikin cantik. Tapi kalau mau halamanmu bisa diklik, hitung, atau bergerak — kamu butuh JavaScript.

        JavaScript itu seperti sistem listrik rumah. Dia yang bikin saklar nyala, kipas berputar, dan pintu garasi bergerak.

        Kabar baiknya: JavaScript jalan langsung di browser. Tidak perlu install apapun untuk mulai.
        """
    ),
    penjelasan=dedent(
        """\
        ### Cara pakai JavaScript

        JS bisa ditulis di file `.js` terpisah lalu disambungkan ke HTML pakai `<script src="app.js"></script>`. Atau langsung di HTML untuk percobaan kecil.

        Untuk debug, pakai `console.log()`. Hasilnya muncul di browser console (Tekan F12 → tab Console). Ini teman terbaikmu saat belajar.

        ### Variable — wadah data

        Anggap variable itu kotak berlabel untuk menyimpan sesuatu.

        - `const` untuk nilai yang tidak akan berubah. **Default pakai ini.**
        - `let` untuk nilai yang memang akan berubah.
        - `var` warisan jaman dulu, hindari.

        Aturan praktis: default `const`, pakai `let` cuma kalau memang harus berubah.

        ### Tipe data dasar

        - `string` untuk teks, ditulis dengan kutip: `"Halo"` atau `'Halo'`.
        - `number` untuk angka: `42`, `3.14`.
        - `boolean` untuk true/false.
        - `null` artinya "ada, tapi sengaja kosong".
        - `undefined` artinya "belum diisi".
        - `array` untuk list: `[1, 2, 3]`.
        - `object` untuk struktur key-value: `{ nama: "Acel", umur: 22 }`.

        ### Operator penting

        Operator matematika seperti biasa: `+`, `-`, `*`, `/`. Tambah satu yang sering muncul: `%` (sisa bagi, modulo).

        Untuk perbandingan, **selalu pakai `===` (triple equals)**, jangan `==` (double). Yang triple ngecek nilai DAN tipe. Yang double sering kasih hasil mengejutkan.

        Operator logika: `&&` (AND), `||` (OR), `!` (NOT).

        ### Template literal

        Daripada gabung string pakai `+`, pakai backtick (`` ` ``). Kamu bisa sisipkan variable dengan `${...}`.

        Backtick ada di pojok kiri atas keyboard, di bawah Esc. Lebih enak baca, dan support baris baru.

        ### Conditional

        `if/else` untuk percabangan. Kalau cuma butuh dua opsi pendek, pakai ternary: `kondisi ? hasil_true : hasil_false`.
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
        "Buat file `app.js` yang berisi variable `namaKamu` dan `tahunLahir`. "
        "Hitung umur dengan asumsi tahun ini 2026. Tampilkan ke console pakai "
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
            "Empat masalah: tutupan kutip string, operator assign vs operator "
            "compare, gabung string yang kurang `+`, dan akhir baris."
        ),
        "answer_explanation": dedent(
            """\
            1. `'Acel;` kurang kutip penutup. Ganti jadi `"Acel"` atau `'Acel'`.
            2. `const umur == 22` salah operator. Untuk assign pakai `=` (single), bukan `==`.
            3. `"Nama: " + nama + ", umur: " umur` kurang `+` antara `", umur: "` dan `umur`.
            4. `console.log("Dewasa")` di blok if sebaiknya diakhiri `;` agar konsisten.
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
            "Mana yang paling tepat untuk variable yang nilainya tidak akan berubah?",
            ["`var`", "`let`", "`const`", "`static`"],
            "C",
            "`const` mengunci variable supaya tidak bisa di-assign ulang. Default pakai `const`, pakai `let` kalau memang harus berubah.",
        ),
        q(
            "Apa hasil dari `5 === \"5\"`?",
            ["`true`", "`false`", "`\"5\"`", "Error"],
            "B",
            "`===` mengecek nilai DAN tipe. Number 5 dan string \"5\" tipe-nya beda, jadi `false`.",
        ),
        q(
            "Apa output dari kode `const a = 4; const b = \"2\"; console.log(a + b);`?",
            ["`6`", "`42`", "`\"42\"`", "Error"],
            "C",
            "Kalau salah satu sisi `+` adalah string, JavaScript ubah yang lain jadi string lalu menggabungkan. Hasilnya string `\"42\"`.",
        ),
        q(
            "Mana cara yang BENAR menulis template literal?",
            [
                "`\"Halo $nama\"`",
                "`'Halo $nama'`",
                "`` `Halo ${nama}` ``",
                "`\"Halo {nama}\"`",
            ],
            "C",
            "Template literal memakai backtick (`` ` ``), bukan kutip biasa, dan placeholder ditulis `${...}`.",
        ),
        q(
            "Apa yang dicetak ke console dari `const status = 50 >= 60 ? \"Lulus\" : \"Coba lagi\"; console.log(status);`?",
            ["`Lulus`", "`Coba lagi`", "`60`", "`undefined`"],
            "B",
            "Ternary: `kondisi ? hasil_true : hasil_false`. `50 >= 60` itu false, jadi yang dijalankan adalah `\"Coba lagi\"`.",
        ),
    ],
    common_mistakes=[
        "Pakai `==` instead of `===`. Bisa kasih hasil mengejutkan, contoh `0 == false` itu `true`.",
        "Lupa kutip penutup string. Sisa baris jadi error parsing.",
        "Tertukar `=` (assign) dan `===` (compare).",
    ],
    checkpoint=[
        "Tahu kapan pakai `const` vs `let`.",
        "Bisa baca tipe data: string, number, boolean, array, object.",
        "Selalu pakai `===` untuk perbandingan.",
        "Bisa pakai template literal untuk gabung string + variable.",
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
        "Menulis function dengan tiga gaya berbeda",
        "Memahami scope dan closure",
        "Memakai `map`, `filter`, dan `reduce` di array",
    ],
    tldr=(
        "Function itu mesin kecil yang terima input dan kembalikan hasil. "
        "Default pakai arrow function. Scope = wilayah hidup variable. "
        "`map`/`filter`/`reduce` itu trio penting di array."
    ),
    pembuka=dedent(
        """\
        Function itu mesin kecil yang menerima input, ngerjain sesuatu, lalu mengembalikan hasil.

        Dengan function, kamu bisa nulis logika sekali lalu pakai berkali-kali.

        Tanpa function, kode kamu cepat berantakan karena harus copy-paste logika yang sama berulang.
        """
    ),
    penjelasan=dedent(
        """\
        ### Tiga gaya menulis function

        Ketiganya melakukan hal yang sama. Aturan praktis: default pakai arrow function, kecuali butuh akses `this` di method object.

        - **Function declaration:** `function sapa(nama) { return ... }`
        - **Function expression:** `const sapa = function(nama) { return ... }`
        - **Arrow function:** `const sapa = (nama) => ...`

        ### Parameter, return, default

        Parameter adalah input yang masuk. Return adalah output yang keluar. Kalau function tidak punya `return`, dia mengembalikan `undefined`.

        Default parameter membuat function tetap jalan walau argumen tidak diberikan, contoh `(nama = "Teman") => ...`.

        ### Scope — wilayah kekuasaan variable

        Variable yang dibuat di dalam function tidak bisa diakses dari luar. Tapi function yang ada di dalam function lain bisa akses variable di luarnya. Ini namanya **closure**.

        ### Closure dengan analogi

        Bayangkan setiap function adalah orang yang bawa tas. Saat function dibuat, dia masukin variable di sekitarnya ke dalam tas. Walau function tersebut "pindah lokasi", isi tasnya tetap dibawa.

        Contohnya saat kamu bikin counter atau private state — closure yang menjaga datanya.

        ### Higher-order function

        Function yang menerima function lain sebagai argumen. Tiga teman karib di JavaScript modern:

        - `map` mengubah setiap elemen array.
        - `filter` memilih elemen yang sesuai kondisi.
        - `reduce` menggabungkan semua elemen jadi satu nilai.

        Ketiganya menggantikan banyak loop manual dan bikin kode lebih ringkas.
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
        "Buat function `hitungTotal(harga, jumlah, diskon)` yang menghitung "
        "harga × jumlah lalu kurangi dengan persentase diskon (`0.1` untuk 10%). "
        "Return total akhir. Panggil dengan `hitungTotal(50000, 3, 0.2)` — "
        "hasil yang diharapkan: 120000."
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
            "dengan `{}` butuh kata kunci eksplisit untuk mengembalikan nilai."
        ),
        "answer_explanation": dedent(
            """\
            1. `function sapa(nama)` kurang `{` setelah parameter.
            2. Arrow function `(a, b) => { a + b }` tidak return apapun. Saat pakai `{}`, kamu wajib tulis `return`. Atau hilangkan `{}` agar return implisit.
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
            "Apa hasil dari `add(2, 3)` jika `const add = (a, b) => a + b;`?",
            ["`undefined`", "`5`", "`\"23\"`", "Error"],
            "B",
            "Arrow function tanpa kurung kurawal otomatis return ekspresi setelah `=>`.",
        ),
        q(
            "Apa beda `(a) => { a + 1 }` dengan `(a) => a + 1`?",
            [
                "Tidak ada beda",
                "Yang pertama tidak return apapun (return undefined). Yang kedua return `a + 1`.",
                "Yang pertama lebih cepat",
                "Yang pertama syntax salah",
            ],
            "B",
            "Saat pakai `{}`, kamu wajib tulis `return` kalau mau mengembalikan nilai. Tanpa `{}`, ekspresi setelah `=>` otomatis di-return.",
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
            "Variable `pesan` cuma hidup di dalam scope function. Di luar function dia tidak ada.",
        ),
        q(
            "Apa hasil `[1,2,3,4].filter(n => n > 2)`?",
            ["`[1, 2, 3, 4]`", "`[3, 4]`", "`[1, 2]`", "`2`"],
            "B",
            "`filter` mengembalikan array berisi elemen yang lulus kondisi. Cuma 3 dan 4 yang lebih besar dari 2.",
        ),
        q(
            "Apa hasil `[1,2,3,4].reduce((acc, n) => acc + n, 0)`?",
            ["`0`", "`4`", "`10`", "`[1,2,3,4]`"],
            "C",
            "`reduce` menggabungkan semua elemen jadi satu nilai. Mulai dari 0, lalu tambahkan: 0+1+2+3+4 = 10.",
        ),
    ],
    common_mistakes=[
        "Pakai arrow function `(a) => { a + 1 }` lalu heran kenapa hasilnya `undefined`. Pakai `return` atau hilangkan `{}`.",
        "Tertukar parameter dan argumen. Parameter adalah nama di definisi function. Argumen adalah nilai yang dikirim saat memanggil.",
        "Mencoba akses variable yang dibuat di dalam function dari luar. Itu di luar scope.",
    ],
    checkpoint=[
        "Bisa menulis function dalam tiga gaya.",
        "Tahu kapan butuh `return` eksplisit di arrow function.",
        "Bisa pakai `map`, `filter`, `reduce` di kasus sederhana.",
        "Paham apa itu scope dan kenapa closure berguna.",
    ],
    xp_reward=100,
)


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 — DOM Manipulation
# ─────────────────────────────────────────────────────────────────────────────

LESSON_JS_DOM = make_lesson(
    title="DOM Manipulation",
    slug="dom-manipulation",
    order_index=3,
    read_time="14 menit",
    summary="Memilih elemen, mengubah konten, dan merespons aksi user.",
    tools=["Browser modern", "VS Code", "DevTools (Console + Elements)"],
    outcomes=[
        "Memilih elemen dengan `querySelector`",
        "Mengubah teks dan style dari JavaScript",
        "Merespons klik, input, dan submit dengan event listener",
        "Membuat dan menghapus elemen secara dinamis",
    ],
    tldr=(
        "DOM = peta halaman yang bisa diubah JavaScript. Pilih dengan "
        "`querySelector`. Ubah dengan `textContent`/`classList`. Reaksi pakai "
        "`addEventListener`."
    ),
    pembuka=dedent(
        """\
        Sampai sini, kode JavaScript kamu cuma jalan di console. Saatnya bikin halaman bereaksi ke aksi user.

        Pekerjaan ini namanya DOM manipulation.

        Setelah lesson ini, kamu bisa bikin tombol yang berfungsi, form yang divalidasi, dan list yang bisa ditambah/hapus.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa itu DOM

        DOM (Document Object Model) adalah representasi halaman HTML sebagai object yang bisa dimanipulasi JavaScript.

        Anggap DOM seperti peta rumah versi digital dari HTML. Kamu bisa pakai JavaScript untuk pindah pintu, ganti warna dinding, atau tambah jendela tanpa rewrite seluruh HTML.

        ### Memilih elemen

        - `document.querySelector(...)` mengambil **elemen pertama** yang cocok dengan selector CSS.
        - `document.querySelectorAll(...)` mengambil **semua** yang cocok, dalam bentuk NodeList.

        Selector yang dipakai persis sama dengan CSS: `h1`, `.judul`, `#hero`, `nav a`.

        ### Mengubah konten

        - `el.textContent = "..."` ubah teks (aman dari XSS).
        - `el.innerHTML = "..."` ubah dengan HTML (hati-hati kalau inputnya dari user).

        Aturan praktis: pakai `textContent` kalau cuma ubah teks. Pakai `innerHTML` cuma kalau memang butuh element baru, dan pastikan inputnya bukan dari user.

        ### Mengubah style

        Untuk perubahan kecil pakai `el.style.namaProperty`. Tapi untuk perubahan besar lebih baik **toggle class**:

        - `el.classList.add("active")`
        - `el.classList.remove("hidden")`
        - `el.classList.toggle("dark-mode")`
        - `el.classList.contains("active")` returns boolean.

        Lalu definisikan style-nya di CSS.

        ### Event listener

        `el.addEventListener("namaEvent", callback)` adalah cara modern merespons aksi user.

        Event populer: `click`, `input`, `submit`, `keydown`/`keyup`, `mouseenter`/`mouseleave`.

        Untuk form, `e.preventDefault()` mencegah halaman reload. Untuk link, mencegah navigasi default.

        ### Membuat dan menghapus elemen

        `document.createElement("li")` bikin elemen baru di memory. `parent.appendChild(el)` masukkan ke parent. `el.remove()` hapus dari halaman.

        ### Membaca isi input

        Untuk input field, jangan pakai `textContent`. Pakai `el.value`. Itu property khusus untuk input.
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

          // klik item untuk tandai selesai
          item.addEventListener("click", () => {
            item.classList.toggle("selesai");
          });

          list.appendChild(item);
          input.value = "";           // bersihkan input
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
        "Buat halaman dengan satu tombol bertuliskan 'Klik aku' dan satu "
        "paragraf di bawahnya. Setiap kali tombol diklik, tambahkan angka di "
        "paragraf, dimulai dari 0. Tampilan: 'Klik: 1', lalu 'Klik: 2', dst."
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
            "function, dan property apa yang dipakai untuk ambil nilai input."
        ),
        "answer_explanation": dedent(
            """\
            1. `queryselector` salah. Yang benar `querySelector` (case-sensitive).
            2. Callback `() {}` kurang `=>`. Harus `() => { ... }`.
            3. `input.text` salah. Untuk ambil isi input pakai `input.value`.
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
            "Apa yang dikembalikan `document.querySelectorAll(\".card\")`?",
            [
                "Satu elemen pertama yang cocok",
                "Daftar (NodeList) berisi semua elemen yang cocok",
                "Array elemen",
                "`null` jika tidak ditemukan",
            ],
            "B",
            "`querySelector` ambil yang pertama. `querySelectorAll` ambil semua, dalam bentuk NodeList yang mirip array.",
        ),
        q(
            "Mana cara yang aman untuk update teks elemen tanpa risiko XSS?",
            [
                "`el.innerHTML = userInput`",
                "`el.textContent = userInput`",
                "`el.value = userInput`",
                "`el.text = userInput`",
            ],
            "B",
            "`textContent` memperlakukan input sebagai teks biasa. `innerHTML` mengeksekusi sebagai HTML — risiko inject script kalau dari user.",
        ),
        q(
            "Apa fungsi `e.preventDefault()` di dalam event listener?",
            [
                "Menghentikan event listener",
                "Mencegah perilaku default browser (form submit / link navigasi)",
                "Menghapus elemen",
                "Membatalkan semua event",
            ],
            "B",
            "Form normalnya reload. Link normalnya navigasi. `preventDefault()` mencegah perilaku default itu.",
        ),
        q(
            "Apa output `el.classList.toggle(\"aktif\"); el.classList.toggle(\"aktif\");`?",
            [
                "Class `aktif` tetap menempel",
                "Class `aktif` tidak menempel (kembali ke kondisi awal)",
                "Error",
                "Ditambahkan dua kali",
            ],
            "B",
            "Toggle seperti saklar lampu. Kalau OFF jadi ON, kalau ON jadi OFF. Dua kali toggle balik ke kondisi awal.",
        ),
        q(
            "Mana cara yang BENAR membaca isi `<input id=\"email\">`?",
            [
                "`document.querySelector(\"#email\").text`",
                "`document.querySelector(\"#email\").value`",
                "`document.querySelector(\"#email\").innerHTML`",
                "`document.querySelector(\"#email\").textContent`",
            ],
            "B",
            "Input form menyimpan nilainya di property `value`. `textContent`/`innerHTML` untuk konten teks elemen biasa.",
        ),
    ],
    common_mistakes=[
        "Pakai `el.text` bukan `el.value` untuk input. Hasilnya `undefined`.",
        "Lupa `e.preventDefault()` di handler form. Halaman reload tiap submit.",
        "Pakai `innerHTML` dengan input dari user. Berpotensi XSS.",
    ],
    checkpoint=[
        "Bisa pilih elemen pakai `querySelector`.",
        "Bisa ubah teks dan toggle class.",
        "Bisa pasang event listener untuk klik dan input.",
        "Bisa bikin elemen baru dan masukkan ke halaman.",
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
        "Membangun app dengan siklus input → simpan → render",
        "Memakai `localStorage` untuk menyimpan data lokal",
        "Memisahkan logika state dari logika DOM",
    ],
    tldr=(
        "Bangun todo app yang bisa tambah/tandai/hapus, datanya tersimpan di "
        "`localStorage`. Pakai pola: array of state + function `render()` "
        "yang menggambar ulang dari state."
    ),
    pembuka=dedent(
        """\
        Saatnya bikin app pertama yang menyimpan data dan punya state.

        Setelah project ini, kamu paham siklus dasar app interaktif: input → simpan → tampilkan → ubah → hapus.

        Inilah pola yang dipakai di hampir semua app modern, dari catatan kecil sampai dashboard kompleks.
        """
    ),
    penjelasan=dedent(
        """\
        ### Apa yang kamu bangun

        Todo list yang bisa tambah task, tandai selesai, hapus, dan datanya tetap ada walau halaman di-refresh.

        ### Konsep baru: localStorage

        `localStorage` adalah penyimpanan di browser yang bertahan walau halaman ditutup.

        - `localStorage.setItem("key", "string")` simpan.
        - `localStorage.getItem("key")` ambil (string atau null).
        - `localStorage.removeItem("key")` hapus.

        Karena localStorage cuma simpan string, kalau mau simpan array/object pakai `JSON.stringify()` saat simpan dan `JSON.parse()` saat ambil.

        ### Pola "state + render"

        Pisahkan logika state (array of tasks) dari logika DOM (gambar ulang list).

        - `tugas` = array yang menyimpan semua task.
        - `render()` = function yang gambar ulang list dari `tugas`.
        - `save()` = function yang simpan `tugas` ke localStorage.

        Setiap kali ada perubahan (tambah/edit/hapus), update `tugas`, panggil `save()`, lalu `render()`.

        ### Kenapa pola ini penting

        Pola ini akan kamu pakai sepanjang karier. Library besar seperti React menggunakan ide yang sama, cuma lebih otomatis.
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
        "Selesaikan todo app di atas, lalu tambahkan tombol hapus per item "
        "(misal klik kanan untuk hapus, atau tombol 'x' kecil di sebelah kanan). "
        "Beri styling yang rapi dan deploy ke Vercel."
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
            "localStorage cuma simpan string. Cek bagaimana kamu baca dan tulis "
            "data. Render juga belum bersihkan list lama sebelum menggambar."
        ),
        "answer_explanation": dedent(
            """\
            1. `getItem` mengembalikan string atau null. Harus di-`JSON.parse`. Default-nya `"[]"`, lalu di-parse.
            2. `setItem` butuh string. Harus `JSON.stringify(tugas)`.
            3. `render()` lupa `list.innerHTML = ""` di awal. Hasilnya tiap render ditumpuk dengan list lama.
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
            "Apa yang dikembalikan `localStorage.getItem(\"key\")` saat key belum ada?",
            ["`undefined`", "`null`", "`\"\"`", "Error"],
            "B",
            "Saat key belum ada, `getItem` mengembalikan `null`. Itu kenapa kita pakai `|| \"[]\"` untuk default.",
        ),
        q(
            "Kenapa kita pakai `JSON.stringify` saat menyimpan array ke localStorage?",
            [
                "Supaya lebih cepat",
                "localStorage cuma menyimpan string, jadi array harus diubah jadi string dulu",
                "Untuk enkripsi data",
                "Tidak perlu, sebenarnya",
            ],
            "B",
            "localStorage menyimpan string saja. Array/object harus di-stringify saat simpan dan di-parse saat ambil.",
        ),
        q(
            "Mengapa `render()` membersihkan `list.innerHTML = \"\"` di awal?",
            [
                "Untuk menghemat memori",
                "Supaya isi lama tidak menumpuk dengan isi baru saat digambar ulang",
                "Untuk membersihkan localStorage",
                "Tidak perlu sebenarnya",
            ],
            "B",
            "Tanpa membersihkan, setiap render akan menumpuk item ke list yang sudah ada. Bersihkan dulu, lalu gambar dari state terbaru.",
        ),
        q(
            "Apa praktik yang paling baik dalam pola state + render?",
            [
                "Mutasi DOM langsung dari banyak tempat",
                "Update state, simpan, lalu panggil render() yang gambar ulang dari state",
                "Pakai variabel global untuk segalanya",
                "Tidak perlu render(), cukup append saja",
            ],
            "B",
            "Pola ini bikin satu sumber kebenaran (state) dan render-nya konsisten. Library besar seperti React menggunakan ide yang sama.",
        ),
        q(
            "Saat membuat task baru, kenapa kita pakai `Date.now()` sebagai id?",
            [
                "Karena angka yang besar terlihat profesional",
                "Untuk menghasilkan id unik berdasarkan waktu pembuatan",
                "Karena UUID tidak ada di JavaScript",
                "Tidak ada alasan, bisa juga pakai nama task sebagai id",
            ],
            "B",
            "`Date.now()` mengembalikan timestamp dalam ms. Cukup unik untuk app sederhana. Kalau butuh yang lebih kuat, pakai `crypto.randomUUID()`.",
        ),
    ],
    common_mistakes=[
        "Lupa `JSON.parse` saat baca dari localStorage. Hasilnya `tugas` jadi string, bukan array.",
        "Manipulasi DOM dari banyak tempat tanpa pola render terpusat. Sulit di-debug.",
        "Tidak handle empty state. List kosong bikin halaman terlihat broken.",
    ],
    checkpoint=[
        "App live di Vercel dengan URL publik.",
        "Bisa tambah, tandai selesai, dan hapus task.",
        "Data tetap ada setelah refresh.",
        "Kode dipisah jelas: state, save, render.",
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
    subtitle="Menghidupkan halaman web",
    description=(
        "Variable, function, scope, dan DOM manipulation. "
        "Setelah level ini kamu bisa bikin halaman yang interaktif dan punya "
        "todo app live di internet."
    ),
    duration="~2 minggu",
    difficulty="Pemula → Menengah",
    accent_color="from-amber-400/30 to-violet-500/10",
    mini_project="Interactive Todo App",
    tags=["ES6+", "DOM", "Event", "localStorage"],
    lessons=[LESSON_JS_BASICS, LESSON_JS_FUNCTION, LESSON_JS_DOM, PROJECT_TODO],
)
