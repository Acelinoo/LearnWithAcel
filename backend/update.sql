UPDATE "lessons" SET criteria = '["Buat struktur HTML dasar lengkap (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).", "Gunakan semantic tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).", "Terapkan CSS Reset / Normalize dasar.", "Styling tampilan dengan Flexbox atau Grid (Mobile Responsive).", "Hubungkan file CSS eksternal dengan benar.", "Pastikan halaman berhasil di-deploy ke Vercel / Netlify dan live URL bisa diakses."]'::jsonb, hints = '### Langkah-langkah Pengerjaan
1. Buka VS Code dan buat folder baru untuk proyek ini.
2. Buat file `index.html` dan ketik `!` lalu tekan Tab untuk struktur dasar.
3. Buat file `style.css` dan hubungkan ke HTML dengan `<link>`.
4. Tambahkan struktur semantik pada HTML (Header, Main, Section, Footer).
5. Terapkan CSS styling, gunakan display flex/grid.
6. Push kode ke GitHub, lalu deploy melalui Vercel.' WHERE slug = 'mini-project-personal-landing-page';
