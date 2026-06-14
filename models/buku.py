from models.koleksi import Koleksi 

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.__pengarang = pengarang
        self.__penerbit = penerbit
        
    @property
    def pengarang(self):
        return self.__pengarang
    
    @property
    def penerbit(self):
        return self.__penerbit
    
class BukuPrinter:
    def tampilkan_data(self,koleksi):
        print("=== Data Buku ===")
        print(f"Kode      : {koleksi.kode}")
        print(f"Judul     : {koleksi.judul}")
        print(f"tahun     : {koleksi.tahun}")
        print(f"Pengarang : {koleksi.pengarang}")
        print(f"Penerbit  : {koleksi.penerbit}")