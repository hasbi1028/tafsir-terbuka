# Protokol Review (peer review, bukan voting)

## Tujuan
Menjaga agar setiap klaim bisa **direproduksi** pembaca lain dari bukti yang disertakan — bukan
memilih "tafsir pemenang".

## Satu PR = satu unit
- Satu ayat (`tafsir/<surah>/<ayat>.yml`) atau satu kasus (`kasus/*.yml`) atau satu berkas bukti.
- Perubahan lintas banyak ayat dipisah; kecuali koreksi format yang bersifat mekanis.

## Syarat sebelum review diminta
1. `make periksa` lulus (tanpa pelanggaran).
2. Setiap klaim baru membawa minimal satu `dasar` berbentuk `QS x:y`; ayat pada surah yang sudah ada di
   `teks/` wajib benar-benar ada.
3. Kata kunci menyebut akar **dan** pola; yang masih ragu ditandai `perlu_verifikasi: true` +
   `catatan` alasan keraguannya.
4. `bantahan` memuat keberatan terkuat yang Anda ketahui — bukan versi lemah yang mudah dijawab.

## Peran reviewer
- **Reviewer isi (minimal 1)**: menilai apakah argumen bisa diulang dari bukti; menandai lompatan
  logika (mis. akar dianggap makna final tanpa pola/konteks).
- **Reviewer teknis (minimal 1)**: YAML sah, tidak mengubah `teks/`, tidak memakai artefak sebagai
  dasar, tidak menghapus kolom.
- **Penyunting rilis**: menjalankan `make periksa`, menaikkan `VERSI`, menandatangani changelog.

## Yang tidak dilakukan
- Voting mayoritas.
- Menghapus klaim yang diperdebatkan. Yang diperdebatkan dipindahkan ke `status: diperdebatkan`
  dengan dua sisi ditulis lengkap.
- Menolak PR hanya karena pendapatnya tidak populer.

## Bila reviewer dan penulis buntu
Tulis berkas `kasus/` baru yang menguji klaim itu, sertakan dua jawaban, dan biarkan keduanya hidup.
Repo ini menampung ketidaksepakatan; itu bukan kegagalan, itu dokumentasi.

## Etika
Tidak ada serangan pribadi. Kritik diarahkan ke argumen dan bukti. Kontributor yang berulang kali
menyerang pribadi diblokir dari review, bukan karena pendapatnya.

## Pengungkapan AI
Bantuan model bahasa wajib dicantumkan di deskripsi PR ("disusun dengan bantuan AI, diperiksa
manusia"). Tanpa itu, PR ditutup. Atestasi manusia: Anda membaca ayatnya dan mempertanggungjawabkan
klaimnya.
