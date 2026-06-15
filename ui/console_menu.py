import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.perpustakaan_service import PerpustakaanService
from models.buku import Buku, BukuPrinter
from models.majalah import Majalah, MajalahPrinter
from models.jurnal import Jurnal, JurnalPrinter
from models.dvd import DVD, DVDPrinter

class UI:
    def __init__(self, service: PerpustakaanService):
        self.service = service
        self.printers = {
            Buku: BukuPrinter(),    
            Majalah: MajalahPrinter(),
            Jurnal: JurnalPrinter(),
            DVD: DVDPrinter()
        }

    def tampilkan_menu(self):
        print("\n"+"="*40)
        print("Menu Program Perpustakaan")
        print("="*40)
        print("1. Tambah Data Koleksi")
        print("2. Hapus Data Koleksi")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")
        print("="*40)

    def tampilkan_pesan(self, success, pesan):
        if success:
            print(f"\n[BERHASIL] {pesan}")
        else:
            print(f"\n[GAGAL] {pesan}")

    def tambah_data(self):
        print("\n=== Tambah Data Koleksi ===")
        print("1. Buku")
        print("2. Majalah")
        print("3. Jurnal")
        print("4. DVD")

        pilih = input("Pilih jenis koleksi: ")
        if pilih not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid!")
            return

        kode = input("Masukkan Kode Koleksi: ")
        judul = input("Masukkan Judul: ")

        try:
            tahun = int(input("Masukkan tahun terbit: "))
        except ValueError:
            print("Tahun terbit harus berupa angka!")
            return

        if pilih == '1':
            pengarang = input("Masukkan Pengarang: ")
            penerbit = input("Masukkan Penerbit: ")
            success, pesan = self.service.tambah_buku(kode, judul, tahun, pengarang, penerbit)

        elif pilih == '2':
            penerbit = input("Masukkan Penerbit: ")
            edisi = input("Masukkan Edisi: ")
            success, pesan = self.service.tambah_majalah(kode, judul, tahun, penerbit, edisi)

        elif pilih == '3':
            penerbit = input("Masukkan Penerbit: ")
            bidang_studi = input("Masukkan Bidang Studi: ")
            try:
                impact_factor = float(input("Masukkan Impact Factor: "))
            except ValueError:
                print("Impact factor harus berupa angka!")
                return
            success, pesan = self.service.tambah_jurnal(kode, judul, tahun, penerbit, bidang_studi, impact_factor)

        elif pilih == '4':
            penerbit = input("Masukkan Penerbit: ")
            sutradara = input("Masukkan Sutradara: ")
            durasi = input("Masukkan Durasi : ")
            genre = input("Masukkan Genre: ")
            success, pesan = self.service.tambah_dvd(kode, judul, tahun, penerbit, sutradara, durasi, genre)

        self.tampilkan_pesan(success, pesan)

    def hapus_data(self):   
        print("\n=== Hapus Data Koleksi ===")
        kode = input("Masukkan Kode Koleksi yang ingin dihapus: ")
        success, pesan = self.service.hapus_koleksi(kode)
        self.tampilkan_pesan(success, pesan)

    def tampilkan_semua_data(self):
        print("\n=== Semua Data Koleksi ===")
        semua_data = self.service.ambil_semua() 
        
        if not semua_data:
            print("Data koleksi kosong!")
            return
        
        for i, item in enumerate(semua_data, start=1):
            print(f"\n Data Koleksi [{i}]")
            printer_ditemukan = False

            for tipe, printer in self.printers.items():
                if isinstance(item, tipe):
                    printer.tampilkan_data(item)
                    printer_ditemukan = True
                    break

            if not printer_ditemukan:
                print("Tipe koleksi tidak dikenali!")
    
    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Masukkan Pilihan Menu: ")
            if pilihan == '1':
                self.tambah_data()
            elif pilihan == '2':
                self.hapus_data()
            elif pilihan == '3':
                self.tampilkan_semua_data()
            elif pilihan == '4':
                print("\nProgram selesai. Terima kasih!")
                break
            else:
                print("Pilihan menu tidak valid! Silakan coba lagi.")   

            input("\nTekan Enter untuk melanjutkan") 