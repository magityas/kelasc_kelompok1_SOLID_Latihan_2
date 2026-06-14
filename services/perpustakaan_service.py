import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from repository.memory_repository import MemoryRepository
from models.buku import Buku
from models.dvd import DVD
from models.jurnal import Jurnal
from models.majalah import Majalah

class PerpustakaanService:
    def __init__(self):
        self.repository = MemoryRepository()

    def _validasi(self, data: dict) -> str | None:
        """Kembalikan pesan error jika ada field kosong, None jika valid."""
        for nama, nilai in data.items():
            if not str(nilai).strip():
                return f"{nama} tidak boleh kosong."
        return None
    
    def tambah_buku(self, kode, judul, tahun, pengarang, penerbit):
        error = self._validasi({
            "Kode": kode,
            "Judul": judul,
            "Tahun": tahun,
            "Pengarang": pengarang,
            "Penerbit": penerbit
        })
        if error:
            return False, error
        
        buku = Buku(kode, judul, tahun, pengarang, penerbit)
        if not self.repository.tambah(buku):
            return False, "Kode sudah terdaftar."
        return True, f"Buku '{judul}' berhasil ditambahkan."
    
    def tambah_dvd(self, kode, judul, tahun, penerbit, sutradara, durasi, genre):
        error = self._validasi({
            "Kode": kode,
            "Judul": judul,
            "Tahun": tahun,
            "Penerbit": penerbit,
            "Sutradara": sutradara,
            "Durasi": durasi,
            "Genre": genre
        })
        if error:
            return False, error

        dvd = DVD(kode, judul, tahun, penerbit, sutradara, durasi, genre)
        if not self.repository.tambah(dvd):
            return False, "Kode sudah terdaftar."
        return True, f"DVD '{judul}' berhasil ditambahkan."
    
    def tambah_jurnal(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        error = self._validasi({
            "Kode": kode,
            "Judul": judul,
            "Tahun": tahun,
            "Penerbit": penerbit,
            "Bidang Studi": bidang_studi,
            "Impact Factor": impact_factor
        })
        if error:
            return False, error

        jurnal = Jurnal(kode, judul, tahun, penerbit, bidang_studi, impact_factor)
        if not self.repository.tambah(jurnal):
            return False, "Kode sudah terdaftar."
        return True, f"Jurnal '{judul}' berhasil ditambahkan."
    
    def tambah_majalah(self, kode, judul, tahun, penerbit, edisi):
        error = self._validasi({
            "Kode": kode,
            "Judul": judul,
            "Tahun": tahun,
            "Penerbit": penerbit,
            "Edisi": edisi
        })
        if error:
            return False, error

        majalah = Majalah(kode, judul, tahun, penerbit, edisi)
        if not self.repository.tambah(majalah):
            return False, "Kode sudah terdaftar."
        return True, f"Majalah '{judul}' berhasil ditambahkan."
    
    def hapus_koleksi(self,kode):
        if not kode.strip():
            return False, "Kode tidak boleh kosong."
        
        if not self.repository.hapus(kode):
            return False, f"Koleksi dengan kode '{kode}' tidak ditemukan."
        return True, f"Koleksi '{kode}' berhasil dihapus."
    
    def cari_koleksi(self, kode):
        return self.repository.cari(kode)
    
    def ambil_semua(self):
        return self.repository.ambil_semua()