# PRINSIP — pasal pengikat

Setiap pembaruan wajib patuh pada pasal-pasal ini. Bila sebuah PR bertabrakan dengan pasal,
**PR-nya yang dibatalkan**, bukan pasalnya (kecuali pasal diubah lewat PR tersendiri + changelog).

## Pasal 1 — Sumber otoritatif tunggal
Al-Quran satu-satunya sumber otoritatif dalam urusan agama. Repo ini tidak menetapkan hukum; ia
menyusun argumen agar bisa diuji.

## Pasal 2 — Tidak menambah syarat tanpa dasar
Tidak boleh ada pernyataan yang menjadikan sesuatu wajib/haram dalam ibadah tanpa dasar eksplisit
dari Al-Quran. Praktik dan tafsir wajib dilabeli sebagai praktik/tafsir.

## Pasal 3 — Ketiadaan penjelasan = kebebasan
Yang tidak dijelaskan tidak otomatis haram.

## Pasal 4 — Rujukan ayat bernomor
Setiap klaim wajib menyebut `QS surah:ayat`. Rujukan tanpa nomor ayat = cacat.

## Pasal 5 — Teks Tier 0 beku
`teks/` (rasm Usmani + imla'i + SHA256SUMS) hanya boleh diubah lewat PR khusus dengan bukti dari
sumber kanonik, dan checksum wajib diperbarui pada PR yang sama.

## Pasal 6 — Akar bukan segalanya
Klaim linguistik wajib menyebut **akar + pola (wazn)**, dan sebaiknya ayat lain dengan bentuk serupa.
Akar tanpa pola = cacat (anti fetisisme akar).

## Pasal 7 — Peka qira'at
Klaim yang bergantung pada satu bacaan wajib berstatus `bersyarat` dan menyebut bacaan alternatifnya.

## Pasal 8 — Artefak bukan dasar
Manuskrip/artefak hanya `tingkat: artefak`, `dasar_hukum: false`, dan tidak boleh muncul di
`klaim.dasar`.

## Pasal 9 — Bantahan tidak boleh kosong
Setiap ayat wajib memuat bantahan dan jawabannya. Kolom kosong = build gagal.

## Pasal 10 — Tanpa voting
Ukurannya reproduksibilitas argumen, bukan jumlah dukungan. Ketidaksepakatan sah disimpan sebagai
`diperdebatkan`.

## Pasal 11 — Ketertelusuran versi
Setiap rilis: naikkan `VERSI`, catat `CHANGELOG.md`, tag `v<versi>`.

## Pasal 12 — Sumber non-Quran berlabel
Kutipan kamus, tafsir, atau riwayat boleh ada sebagai **alat** (Tier 2–4) dan wajib berlabel;
tidak boleh menjadi dasar tuntutan.
