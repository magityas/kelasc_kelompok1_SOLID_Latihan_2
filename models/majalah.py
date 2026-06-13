from koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
      super().__init__(kode, judul, tahun)
      self.__penerbit = penerbit
      self.__edisi = edisi
      
    @property
    def penerbit(self):
        return self.__penerbit
    
    @property
    def edisi(self):
        return self.__edisi
    
    def tampilkan_data(self):
       print(f"=== Data majalah ===")
       print(f"Kode    : {self.kode}")
       print(f"Judul   : {self.judul}")
       print(f"tahun   : {self.tahun}")
       print(f"Penerbit: {self.penerbit}")
       print(f"Edisi   : {self.edisi}")