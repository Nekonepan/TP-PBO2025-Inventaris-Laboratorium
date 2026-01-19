# Pengumpulan Portofolio TP-PBO2025 – Pemrograman Berorientasi Objek

## A. Identitas Proyek

**Identitas Mahasiswa**

* Nama : Lutfan Alaudin Naja
* NIM  : 2400018032

* Nama : Audrik Watzala Ziaulhaq
* NIM  : 2400018017

**Judul Proyek**
PERANCANGAN SISTEM MANAJEMEN INVENTARIS LABORATORIUM BERBASIS PEMROGRAMAN BERORIENTASI OBJEK

**Repository Proyek**
GitHub/GitLab: *https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium*

**Tampilan Awal Aplikasi**
Tampilan awal aplikasi berupa **halaman login**, di mana pengguna harus memasukkan username dan password sebelum mengakses sistem.

📷 *Screenshot:*
[docs/screenshot/login.png](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/blob/main/docs/screenshot/login.png)

---

## B. Persoalan Bisnis dan Deskripsi Proyek

Pengelolaan inventaris laboratorium secara manual sering menimbulkan berbagai permasalahan, seperti kesulitan dalam pencatatan alat, kesalahan data, keterlambatan pelaporan, serta sulitnya memantau peminjaman dan pengembalian alat.

Proyek ini bertujuan untuk membangun **Aplikasi Inventaris Laboratorium** berbasis GUI menggunakan konsep **Pemrograman Berorientasi Objek (PBO)** dengan bahasa Python. Aplikasi ini membantu pihak laboratorium dalam mengelola data alat, kategori, pengguna, serta proses peminjaman secara terstruktur, aman, dan efisien.

---

## C. Daftar Spesifikasi Aplikasi

1. Sistem login dan autentikasi pengguna
2. Manajemen data alat laboratorium (tambah, ubah, hapus, lihat)
3. Manajemen kategori alat
4. Manajemen peminjaman alat
5. Dashboard ringkasan data inventaris
6. Penyimpanan data menggunakan database SQLite
7. Antarmuka berbasis GUI
8. Penerapan konsep OOP (class, object, encapsulation, modularisasi)

---

## D. Rancangan Model Diagram UML

Aplikasi ini dirancang menggunakan beberapa diagram UML sebagai berikut:

1. **Use Case Diagram** – Menjelaskan interaksi pengguna dengan sistem
   [docs/uml/usecase.png](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/blob/main/docs/uml/usecase.png)

2. **Class Diagram** – Menunjukkan struktur class dan relasi antar class
   [docs/uml/class.png](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/blob/main/docs/uml/class.png)

3. **Sequence Diagram** – Menjelaskan alur proses interaksi sistem
   [docs/uml/sequence.png](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/blob/main/docs/uml/sequence.png)

---

## E. Rancangan Antarmuka Berbasis GUI

Antarmuka aplikasi dirancang menggunakan GUI berbasis Python yang terdiri dari:

* Halaman Login
* Dashboard
* Halaman Kelola Alat
* Halaman Kategori
* Halaman Peminjaman

*Contoh screenshot antarmuka:*
[docs/screenshot/dashboard.png](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/blob/main/docs/screenshot/dashboard.png)

---

## F. Skrip Program dan Penjelasannya

Struktur utama program:

* `main.py` : Entry point aplikasi
* `gui/` : Berisi modul antarmuka GUI

  * `login.py`
  * `dashboard.py`
  * `alat_gui.py`
  * `kategori_gui.py`
  * `peminjaman_gui.py`
* `src/models/` : Berisi class model (OOP)

  * `alat.py`
  * `kategori.py`
  * `peminjaman.py`
  * `user.py`
* `src/database/` : Koneksi dan pengelolaan database

  * `database.py`

Setiap fitur direpresentasikan dalam bentuk **class**, sehingga memudahkan pemeliharaan, pengembangan, dan penerapan konsep PBO.

---

## G. Penjelasan Screenshot Tampilan Aplikasi

1. **Login** – Autentikasi pengguna sebelum masuk sistem
2. **Dashboard** – Menampilkan ringkasan data inventaris
3. **Kelola Alat** – Mengelola data alat laboratorium
4. **Kategori** – Mengelompokkan alat berdasarkan kategori
5. **Peminjaman Alat** – Mengelola transaksi peminjaman

Screenshot terdapat pada folder [docs/screenshot/](https://github.com/Nekonepan/TP-PBO2025-Inventaris-Laboratorium/tree/main/docs/screenshot)

---

## H. Screenshot Status Unggah Proyek

Proyek ini telah diunggah ke repository GitHub/GitLab hingga versi final.

📷 Screenshot bukti unggah repository:
*(tambahkan screenshot commit & repository di sini)*

---

## I. Analisis Pengerjaan Proyek

**Waktu Pengerjaan**
Proyek dikerjakan selama satu semester dengan pembagian waktu untuk analisis kebutuhan, perancangan UML, implementasi, dan pengujian.

**Ketercapaian Spesifikasi**
Sebagian besar spesifikasi awal berhasil diimplementasikan dengan baik sesuai perencanaan.

**Biaya yang Dibutuhkan**
Tidak memerlukan biaya finansial karena menggunakan perangkat lunak open-source.

**Kendala**

* Perancangan GUI yang konsisten
* Integrasi antar modul
* Pengelolaan database

**Tantangan Masa Depan**

* Pengembangan multi-user
* Integrasi dengan sistem web
* Penambahan laporan dan ekspor data

---

📌 **Catatan:**
Dokumentasi pendukung (UML, screenshot, laporan) tersedia pada folder `docs/`.
