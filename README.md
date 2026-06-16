# 📚 Sistem Informasi Perpustakaan

Proyek latihan implementasi prinsip **SOLID** menggunakan Python. Aplikasi ini merupakan sistem manajemen koleksi perpustakaan berbasis command-line yang memungkinkan pengguna untuk mengelola berbagai jenis koleksi seperti buku, majalah, jurnal, dan DVD.

---

## 👥 Kelompok 1 — Kelas C

| NIM      | Nama                          | GitHub                                           | Bagian                                                            |
| -------- | ----------------------------- | ------------------------------------------------ | ----------------------------------------------------------------- |
| K3525075 | Tsalits In'am Illiyyin        | [@tsaliy](https://github.com/tsaliy)             | UI (`ui/console_menu.py`)                                         |
| K3525028 | Immelda Sekar Mellinda        | [@lmmelda](https://github.com/lmmelda)           | Models (`models/buku.py`, `models/majalah.py`)                    |
| K3525064 | Maulana Shandy Eka Saputra    | [@shandyeka491](https://github.com/shandyeka491) | Models (`models/dvd.py`, `models/jurnal.py`, `models/koleksi.py`) |
| K3525086 | Thiraza Naufal Zhafran Windra | [@zhafraz](https://github.com/zhafraz)           | Main Code (`main.py`, `services/perpustakaan_service.py`)         |
| K3525085 | Sabrosa Noval Rachmadhani     | [@SabronR](https://github.com/SabronR)           | Memory (`repository/memory_repository.py`)                        |
| K3525079 | Maychel Agitya Prasetyo       | [@Magityas](https://github.com/Magityas)         | Repository (`repository/memory_repository.py`)                    |

---

## 🗂️ Struktur Proyek

```
SOLID-Latihan-2/
├── main.py
├── models/
│   ├── koleksi.py         # Abstract base class Koleksi
│   ├── buku.py            # Model Buku & BukuPrinter
│   ├── dvd.py             # Model DVD & DVDPrinter
│   ├── jurnal.py          # Model Jurnal & JurnalPrinter
│   └── majalah.py         # Model Majalah & MajalahPrinter
├── repository/
│   └── memory_repository.py   # Abstract repository + implementasi in-memory
├── services/
│   └── perpustakaan_service.py  # Business logic & validasi
└── ui/
    └── console_menu.py    # Antarmuka pengguna berbasis konsol
```

---

## 🧱 Implementasi Prinsip SOLID

### S — Single Responsibility Principle

Setiap class memiliki satu tanggung jawab:

- `Buku`, `DVD`, `Jurnal`, `Majalah` → hanya menyimpan data koleksi
- `BukuPrinter`, `DVDPrinter`, dll → hanya menangani tampilan data
- `PerpustakaanService` → hanya menangani logika bisnis & validasi
- `UI` → hanya menangani interaksi dengan pengguna

### O — Open/Closed Principle

Sistem terbuka untuk ekstensi (menambah jenis koleksi baru) tanpa mengubah kode yang sudah ada. Cukup buat class baru yang mewarisi `Koleksi` dan tambahkan `Printer`-nya.

### L — Liskov Substitution Principle

`Buku`, `DVD`, `Jurnal`, dan `Majalah` merupakan turunan dari `Koleksi` dan dapat digunakan secara bergantian di repository tanpa mengubah perilaku sistem.

### I — Interface Segregation Principle

`KoleksiRepository` mendefinisikan antarmuka yang ramping dan fokus (`tambah`, `ambil_semua`, `cari`, `hapus`) sehingga implementasi tidak dipaksa mengimplementasikan method yang tidak relevan.

### D — Dependency Inversion Principle

`PerpustakaanService` bergantung pada abstraksi `KoleksiRepository`, bukan pada implementasi konkret `MemoryRepository`. `UI` bergantung pada `PerpustakaanService`, bukan langsung ke repository.

---

## ✨ Fitur

- ➕ **Tambah koleksi** — Buku, Majalah, Jurnal, atau DVD
- 🗑️ **Hapus koleksi** — berdasarkan kode unik
- 📋 **Tampilkan semua koleksi** — dengan format tampilan per tipe
- ✅ **Validasi input** — field kosong dan kode duplikat terdeteksi otomatis

---

## 🚀 Cara Menjalankan

**Prasyarat:** Python 3.10 atau lebih baru

```bash
# Clone repositori
git clone https://github.com/magityas/kelasc_kelompok1_SOLID-Latihan-2
cd SOLID-Latihan-2

# Jalankan aplikasi
python main.py
```

---

## 🖥️ Contoh Penggunaan

```
=========================================
     SISTEM INFORMASI PERPUSTAKAAN
=========================================

========================================
Menu Program Perpustakaan
========================================
1. Tambah Data Koleksi
2. Hapus Data Koleksi
3. Tampilkan Semua Data
4. Keluar
========================================
```

---

## 🛠️ Teknologi

- **Python 3.10+**
- `abc` — Abstract Base Class untuk interface dan class abstrak
- Penyimpanan data **in-memory** (tidak menggunakan database eksternal)
