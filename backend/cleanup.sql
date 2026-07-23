-- Delete all duplicate 2-hour mini projects
DELETE FROM "lessons" 
WHERE title ILIKE '%Mini Project%' AND duration ILIKE '%2 Jam%';

-- Also update criteria and hints for remaining mini projects (which should be 30-45 mins)
UPDATE "lessons" 
SET criteria = '["Selesaikan seluruh instruksi yang diberikan.", "Terapkan praktik terbaik (best practices) yang telah dipelajari.", "Pastikan fitur atau desain bekerja dengan baik.", "Review ulang kode atau langkah pengerjaanmu."]'::jsonb, 
    hints = '### Tips Pengerjaan
- Jangan ragu untuk mencari referensi di dokumentasi resmi atau Google.
- Terapkan konsep yang sudah kamu pelajari di modul-modul sebelumnya.
- Uji coba secara berkala agar kamu tahu bagian mana yang perlu diperbaiki.'
WHERE title ILIKE '%Mini Project%' AND (criteria IS NULL OR criteria::text = 'null');
