# Tafsir Terbuka (quran alone)

Repositori tafsir berbasis **teks Arab** yang bisa diuji ulang siapa pun. Bukan "tafsir resmi":
tidak ada satu `main` yang dianggap benar. Yang dijaga mesin bukan kesimpulan, melainkan
**syarat argumen**: ayat yang benar, akar + pola yang disebut, dasar yang berbentuk ayat, dan
bantahan yang tidak boleh dikosongkan.

> Prinsip kerja: **yang tidak dapat direproduksi pembaca lain, bukan argumen — itu opini.**

## Isi

| Jalur | Isi |
| --- | --- |
| `teks/` | Tier 0 — rasm Usmani (mushaf Hafs) + turunan imla'i + `SHA256SUMS`. **Beku**: tidak boleh diubah tanpa PR khusus. |
| `tafsir/<surah>/<ayat>.yml` | Satu ayat satu berkas: teks, kata kunci (akar + pola), bukti internal, klaim, bantahan, status. |
| `qiraat/` | Berkas varian bacaan. Wajib ada bila sebuah ayat "peka bacaan". |
| `kasus/` | Pertanyaan nyata + ayat rujukan = bahan uji. Siapa pun bisa menguji ulang jawabannya. |
| `bukti/artefak/` | Tingkat 3: manuskrip/artefak. **Tidak pernah** menjadi dasar tuntutan. |
| `protokol/` | Aturan review dan cara menyatakan ketidaksepakatan. |
| `scripts/` | `cek-teks.py` (checksum Tier 0) dan `periksa.py` (penjaga isi). |

## Coba

```bash
pip install -r requirements.txt
make periksa      # verifikasi teks + seluruh isi
```

Contoh keluaran: `7 berkas ayat, 270 pemeriksaan lulus, 0 pelanggaran`.

## Lima aturan yang ditegakkan mesin

1. Teks ayat **wajib identik** dengan `teks/al-fatihah.uthmani.tsv` (checksum dijaga).
2. Setiap klaim wajib punya `dasar` berbentuk `QS surah:ayat` — artefak/tafsir **ditolak** sebagai dasar.
3. Setiap kata kunci wajib menyebut **akar + pola (wazn)**; akar saja dianggap cacat.
4. Kolom `bantahan` tidak boleh kosong — ayat tanpa bantahan berarti belum diteliti.
5. Ayat yang punya berkas `qiraat/` dengan `peka_qiraat: true` wajib memuat minimal satu klaim
   berstatus `bersyarat` yang menyebut bacaan alternatifnya.

## Pilot: Al-Fatihah

Tujuh ayat, masing-masing dengan kata kunci berakar, bukti internal antar-ayat, klaim berstatus,
dan bantahan. Tiga contoh yang sengaja dipilih sulit:

- **1:1** — basmalah diverifikasi lewat QS 27:30 (pola pembukaan kitab yang sama).
- **1:4** — **peka qira'at**: Hafs `مَالِكِ` (pemilik) vs bacaan lain `مَلِكِ` (raja). Klaimnya
  berstatus `bersyarat`, bukan dipilih diam-diam. Lihat `qiraat/001-004.yml`.
- **1:7** — bantahan: sebagian menetapkan identitas kelompok tertentu; repo menolak karena ayatnya
  tidak menyebut identitas (Pasal 2).

Artefak contoh: `bukti/artefak/sanaa-palimpsest.yml` — memuat apa yang dibuktikan dan **apa yang
tidak**, dengan `dasar_hukum: false`.

## Cara berkontribusi

Baca `protokol/REVIEW.md`. Ringkasnya: satu PR = satu ayat atau satu kasus; setiap klaim baru wajib
membawa ayat pendukung; reviewer menilai **reproduksibilitas**, bukan kesepakatan; kesimpulan yang
diperdebatkan dibiarkan berstatus `diperdebatkan` dan tidak dipaksa merge.

## Batas

Repo ini tidak menetapkan hukum dan tidak menggantikan bacaan pembaca. Ia memetakan argumen dan
menjaga syaratnya tetap bisa diperiksa. Lisensi teks & berkas: CC BY-SA 4.0.
