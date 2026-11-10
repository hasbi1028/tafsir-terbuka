#!/usr/bin/env python3
"""Penjaga isi repo tafsir terbuka.

Menegakkan PRINSIP.md secara mekanis: teks Tier 0 utuh, klaim punya dasar ayat, klaim
yang bergantung bacaan berstatus 'bersyarat', bantahan tidak boleh kosong, dan artefak
tidak boleh dipakai sebagai dasar tuntutan.

Jalankan: `make periksa` (atau `python3 scripts/periksa.py`).
"""
import hashlib
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # interpreter aktif (mis. venv) tidak punya PyYAML
    import os
    for kandidat in ("/usr/bin/python3", "/usr/local/bin/python3"):
        if os.path.exists(kandidat) and os.path.realpath(kandidat) != os.path.realpath(sys.executable):
            os.execv(kandidat, [kandidat, *sys.argv])
    sys.exit("PyYAML tidak tersedia: jalankan `pip install pyyaml`")

AKAR = Path(__file__).resolve().parent.parent
POLA_AYAT = re.compile(r"^QS\s+\d+:\d+$")
POLA_AKAR = re.compile(r"^[\u0621-\u064A](?:-[\u0621-\u064A])+$")
HARAKAT = {chr(c) for c in list(range(0x064B, 0x0660)) + [0x0670] + list(range(0x06D6, 0x06EE))}
STATUS_KLAIM = {"tetap", "bersyarat", "diperdebatkan", "perlu-verifikasi"}

galat: list[str] = []
lulus = 0


def cek(syarat: bool, pesan: str) -> None:
    global lulus
    if syarat:
        lulus += 1
    else:
        galat.append(pesan)


def baca_tsv(nama: str) -> dict[str, str]:
    isi: dict[str, str] = {}
    for baris in (AKAR / "teks" / nama).read_text(encoding="utf-8").splitlines():
        if not baris.strip() or baris.startswith("#"):
            continue
        kunci, nilai = baris.split("\t", 1)
        isi[kunci] = nilai
    return isi


def hash_isi(path: Path) -> str:
    """Hash atas baris isi saja (komentar & baris kosong diabaikan) — sama dengan cek-teks.py."""
    baris = [b for b in path.read_text(encoding="utf-8").splitlines()
             if b.strip() and not b.startswith("#")]
    return hashlib.sha256("\n".join(baris).encode()).hexdigest()


def periksa_checksum() -> None:
    daftar = {}
    for baris in (AKAR / "teks/SHA256SUMS").read_text().splitlines():
        if baris.strip():
            h, nama = baris.split()
            daftar[nama] = h
    for nama, harap in daftar.items():
        cek(hash_isi(AKAR / "teks" / nama) == harap,
            f"teks/{nama}: checksum berubah — teks Tier 0 tidak boleh diubah tanpa PR khusus + SHA256SUMS")


def periksa_ayat(berkas: Path, teks_uth: dict[str, str], teks_iml: dict[str, str]) -> None:
    d = yaml.safe_load(berkas.read_text(encoding="utf-8")) or {}
    nama = f"tafsir/{berkas.parent.name}/{berkas.name}"
    wajib = ["surah", "ayat", "arab", "imlai", "terjemah_minimal", "kata_kunci",
             "bukti_internal", "klaim", "bantahan", "status"]
    for kunci in wajib:
        cek(kunci in d, f"{nama}: kolom wajib '{kunci}' tidak ada")
    if any(k not in d for k in wajib):
        return

    kode = f"{int(d['surah'])}:{int(d['ayat'])}"
    cek(kode in teks_uth, f"{nama}: ayat {kode} tidak ada di teks kanonik")
    if kode in teks_uth:
        cek(d["arab"] == teks_uth[kode], f"{nama}: teks arab berbeda dari teks kanonik Tier 0")
        cek(d["imlai"] == teks_iml[kode], f"{nama}: teks imlai berbeda dari turunan kanonik")
    cek(not (set(d["imlai"]) & HARAKAT), f"{nama}: kolom imlai masih memuat harakat")

    cek(bool(d["kata_kunci"]), f"{nama}: kata_kunci kosong")
    for w in d["kata_kunci"]:
        label = f"{nama}: kata '{w.get('kata', '?')}'"
        cek(bool(w.get("kata")), f"{label}: 'kata' kosong")
        cek(bool(w.get("pola")), f"{label}: 'pola' (wazn) wajib — akar saja dianggap cacat")
        akar = w.get("akar")
        if akar is not None:
            cek(bool(POLA_AKAR.match(str(akar))), f"{label}: akar '{akar}' tidak berbentuk 'ح-ر-ف'")
        if w.get("perlu_verifikasi"):
            cek(bool(str(w.get("catatan", "")).strip()),
                f"{label}: ditandai perlu_verifikasi tetapi 'catatan' kosong")

    cek(bool(d["klaim"]), f"{nama}: klaim kosong")
    ada_bersyarat = False
    for k in d["klaim"]:
        isi = str(k.get("isi", ""))[:48]
        cek(bool(str(k.get("isi", "")).strip()), f"{nama}: ada klaim tanpa 'isi'")
        dasar = k.get("dasar") or []
        cek(bool(dasar), f"{nama}: klaim '{isi}...' tanpa dasar ayat")
        for rujukan in dasar:
            cek(bool(POLA_AYAT.match(str(rujukan))),
                f"{nama}: dasar '{rujukan}' bukan bentuk 'QS x:y' (artefak/tafsir tidak boleh jadi dasar)")
            m = re.match(r"^QS\s+(\d+):(\d+)$", str(rujukan))
            if m and int(m.group(1)) == int(d["surah"]):
                cek(f"{d['surah']}:{int(m.group(2))}" in teks_uth,
                    f"{nama}: dasar '{rujukan}' tidak ada di teks kanonik")
        st = str(k.get("status", ""))
        cek(st in STATUS_KLAIM, f"{nama}: status klaim '{st}' tidak dikenal (pakai: {sorted(STATUS_KLAIM)})")
        if st == "bersyarat":
            ada_bersyarat = True
            cek(bool(str(k.get("syarat", "")).strip()), f"{nama}: klaim bersyarat wajib menyebut 'syarat'")

    cek(bool(d["bantahan"]), f"{nama}: kolom bantahan kosong — ayat tanpa bantahan berarti belum diteliti")
    for b in d["bantahan"]:
        cek(bool(str(b.get("isi", "")).strip()), f"{nama}: bantahan tanpa 'isi'")
        cek(bool(str(b.get("jawaban", "")).strip()), f"{nama}: bantahan tanpa 'jawaban'")

    qiraat = AKAR / "qiraat" / f"{int(d['surah']):03d}-{int(d['ayat']):03d}.yml"
    if qiraat.exists():
        q = yaml.safe_load(qiraat.read_text(encoding="utf-8")) or {}
        if q.get("peka_qiraat"):
            cek(ada_bersyarat,
                f"{nama}: berkas qira'at menandai ayat ini peka bacaan, tetapi tidak ada klaim berstatus 'bersyarat'")


def main() -> int:
    teks_uth = baca_tsv("al-fatihah.uthmani.tsv")
    teks_iml = baca_tsv("al-fatihah.imlai.tsv")
    periksa_checksum()

    berkas_ayat = sorted((AKAR / "tafsir").rglob("*.yml"))
    cek(bool(berkas_ayat), "tafsir/: tidak ada berkas ayat")
    for b in berkas_ayat:
        periksa_ayat(b, teks_uth, teks_iml)

    for b in sorted((AKAR / "bukti/artefak").glob("*.yml")):
        d = yaml.safe_load(b.read_text(encoding="utf-8")) or {}
        cek(d.get("dasar_hukum") is False,
            f"bukti/artefak/{b.name}: wajib 'dasar_hukum: false' — artefak bukan dasar hukum")

    for b in sorted((AKAR / "kasus").glob("*.yml")):
        d = yaml.safe_load(b.read_text(encoding="utf-8")) or {}
        nama = f"kasus/{b.name}"
        for kunci in ("id", "pertanyaan", "ayat_rujukan", "jawaban_ringkas", "status"):
            cek(kunci in d, f"{nama}: kolom '{kunci}' tidak ada")
        for r in d.get("ayat_rujukan") or []:
            cek(bool(POLA_AYAT.match(str(r))), f"{nama}: rujukan '{r}' bukan bentuk 'QS x:y'")

    print(f"Berkas ayat      : {len(berkas_ayat)}")
    print(f"Pemeriksaan lulus: {lulus}")
    print(f"Pelanggaran      : {len(galat)}")
    if galat:
        print()
        for g in galat:
            print(f"  GAGAL {g}")
        print("\nTIDAK LULUS — perbaiki dulu sebelum commit/tag.")
        return 1
    print("\nLULUS — isi konsisten dengan PRINSIP.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
