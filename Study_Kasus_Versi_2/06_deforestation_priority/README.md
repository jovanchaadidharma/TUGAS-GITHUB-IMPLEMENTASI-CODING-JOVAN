# 6. Deforestation — Prioritas Pemeriksaan Perubahan Lahan

## Masalah
Petugas lingkungan memiliki beberapa alert perubahan tutupan lahan dan perlu menentukan mana yang diperiksa lebih dahulu.

## Metode
Menggunakan Random Forest pada fitur sintetis: tingkat perubahan vegetasi, kedekatan jalan, dan luas perubahan. Model mengeluarkan kelas prioritas rendah/sedang/tinggi.

## Menjalankan
```bash
python alert_priority.py
```

Ini hanya contoh alur prioritisasi. Tidak menggunakan citra satelit asli, tidak membuktikan deforestasi, dan tidak menentukan penyebab secara faktual.
