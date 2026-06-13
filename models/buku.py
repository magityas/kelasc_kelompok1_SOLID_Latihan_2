from koleksi import Koleksi 

class Buku(Koleksi):
    def __init__(self, Kode, judul, tahun, pengarang, penerbit):
        super().__init__(Kode, judul, tahun)
        self.__pengarang = pengarang
        self.__penerbit = penerbit
        
    @property
    def penarang(self):
        return self.__pengarang
    
    @property
    def penerbit(self):
        return self.__penerbit
    
    def tampilkan_data(self):
        print("=== Data Buku ===")
        print(f"Kode      : {self.kode}")
        print(f"Judul     : {self.judul}")
        print(f"tahun     : {self.tahun}")
        print(f"Pengarang : {self.penarang}")
        print(f"Penerbit  : {self.penerbit}")