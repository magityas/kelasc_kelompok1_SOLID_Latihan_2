from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun

    @abstractmethod
    def tampilkan_data(self):
        pass

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def tampilkan_data(self):
        print("Jenis : Buku")
        print("Kode :", self.kode)
        print("Judul :", self.judul)
        print("Tahun :", self.tahun)
        print("Pengarang :", self.pengarang)
        print("Penerbit :", self.penerbit)