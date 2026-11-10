#!/usr/bin/env python3
"""Memastikan teks Tier 0 tidak berubah dan turunan imla'i tetap bersih.

Dipakai CI sebelum pemeriksaan isi: kalau teks kanonik bergeser satu harakat, tidak ada
tafsir di repo ini yang bisa dipercaya.
"""
import hashlib
import sys
from pathlib import Path

AKAR = Path(__file__).resolve().parent.parent
HARAKAT = {chr(c) for c in list(range(0x064B, 0x0660)) + [0x0670] + list(range(0x06D6, 0x06EE))}


def hash_isi(path: Path) -> str:
    """Hash atas baris isi saja (komentar & baris kosong diabaikan)."""
    baris = [b for b in path.read_text(encoding="utf-8").splitlines()
             if b.strip() and not b.startswith("#")]
    return hashlib.sha256("\n".join(baris).encode()).hexdigest()


def main() -> int:
    salah = 0
    for baris in (AKAR / "teks/SHA256SUMS").read_text().splitlines():
        if not baris.strip():
            continue
        harap, nama = baris.split()
        dapat = hash_isi(AKAR / "teks" / nama)
        status = "ok   " if dapat == harap else "GAGAL"
        print(f"  {status} {nama}  {dapat[:16]}")
        salah += dapat != harap

    imlai = AKAR / "teks/al-fatihah.imlai.tsv"
    kotor = [b for b in imlai.read_text(encoding="utf-8").splitlines()
             if b and not b.startswith("#") and (set(b.split("\t")[-1]) & HARAKAT)]
    print(f"  {'ok   ' if not kotor else 'GAGAL'} imlai tanpa harakat ({len(kotor)} baris kotor)")
    salah += bool(kotor)
    return 1 if salah else 0


if __name__ == "__main__":
    sys.exit(main())
