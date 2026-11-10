SHELL := /bin/bash
PY ?= python3

.PHONY: periksa teks bantuan

periksa: teks
	@$(PY) scripts/periksa.py

teks:
	@$(PY) scripts/cek-teks.py

bantuan:
	@echo "make teks     : verifikasi checksum teks kanonik (Tier 0)"
	@echo "make periksa  : jalankan seluruh penjaga isi (PRINSIP.md)"
