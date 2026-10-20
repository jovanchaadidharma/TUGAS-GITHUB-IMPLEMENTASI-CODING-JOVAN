# 2. HPC — Pemrosesan Data Sensor

## Masalah
Sistem sensor menghasilkan banyak angka yang perlu dihitung rata-ratanya. Proyek ini menunjukkan pembagian pekerjaan menjadi beberapa bagian.

## Metode
Menghasilkan data sintetis, menghitung jumlah data dan total nilai secara serial, lalu mengulang dengan multiprocessing. Bandingkan hasil dan waktu.

## Menjalankan
```bash
python sensor_processing.py
```
Waktu bergantung pada perangkat dan overhead proses paralel.
