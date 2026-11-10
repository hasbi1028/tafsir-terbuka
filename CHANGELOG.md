# Changelog

## [0.1.0] — 2026-11-10

### Ditambahkan
- Struktur repo tafsir terbuka: `teks/` (Tier 0 + checksum), `tafsir/`, `qiraat/`, `kasus/`,
  `bukti/artefak/`, `protokol/`.
- Pilot **Al-Fatihah 1:1–1:7** — masing-masing dengan kata kunci (akar + pola), bukti internal,
  klaim berstatus, dan bantahan.
- Tiga contoh sulit: verifikasi internal basmalah (QS 27:30), ayat **peka qira'at** (1:4 — `مالك`
  vs `ملك`, klaim `bersyarat`), dan artefak dengan `dasar_hukum: false`.
- `scripts/cek-teks.py` — verifikasi checksum teks kanonik + imla'i tanpa harakat.
- `scripts/periksa.py` — 12 aturan PRINSIP.md ditegakkan mesin (270 pemeriksaan pada pilot ini).
- `make periksa` + CI (GitHub Actions).
- `PRINSIP.md` (12 pasal) dan `protokol/REVIEW.md`.
- Uji negatif terbukti: bantahan kosong, artefak sebagai dasar, teks menyimpang dari Tier 0,
  klaim `bersyarat` dihapus pada ayat peka qira'at, dan pola (wazn) hilang — semuanya ditolak.
