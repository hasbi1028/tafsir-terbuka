# Tingkat bukti

Aturan pokok: **tier rendah tidak membatalkan tier tinggi, dan tier tinggi tidak boleh menjadi
satu-satunya dasar sebuah tuntutan.**

| Tier | Isi | Boleh jadi dasar klaim? | Catatan |
| --- | --- | --- | --- |
| 0 | Rasm Usmani (mushaf Hafs) + turunan imla'i | Ya, wajib | Dibekukan; checksum dijaga `scripts/cek-teks.py` |
| 1 | Qira'at (varian bacaan) | Ya, tetapi klaim harus `bersyarat` | Setiap ayat peka bacaan wajib punya berkas `qiraat/` |
| 2 | Korpus bahasa: kamus klasik, morfologi, syair pra-Islam | Tidak sendirian | Wajib disertai ayat penopang; dipakai untuk medan makna akar |
| 3 | Artefak/manuskrip (Birmingham, Topkapi, palimpsest Sanaa) | **Tidak** | Hanya informasi sejarah teks; `dasar_hukum: false` |
| 4 | Tafsir/riwayat belakangan | **Tidak** | Berstatus sejarah pembacaan |

## Konsekuensi praktis

- `klaim.dasar` hanya menerima bentuk `QS surah:ayat`. Menulis nama artefak di situ = build gagal.
- Klaim linguistik: sebut **akar + pola**; kalau hanya akar, dianggap cacat (Pasal 6).
- Kalau sebuah kata kunci masih diperdebatkan, tandai `perlu_verifikasi: true` dan tulis alasannya.
- Qira'at bukan ancaman: ia data. Yang berbahaya adalah memilih satu bacaan tanpa memberi tahu pembaca.
