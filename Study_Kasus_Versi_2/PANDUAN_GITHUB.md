# Panduan unggah ke GitHub

1. Ekstrak ZIP.
2. Buat repository baru di GitHub.
3. Buka terminal di folder hasil ekstrak.
4. Jalankan:
   ```bash
   git init
   git add .
   git commit -m "Tambah paket studi kasus versi 2"
   git branch -M main
   git remote add origin https://github.com/USERNAME/NAMA-REPO.git
   git push -u origin main
   ```
5. Ganti URL remote dengan alamat repository milik sendiri.
