from models.koleksi import Koleksi

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
    
class MajalahPrinter:
    def tampilkan_data(self,koleksi):
       print(f"=== Data majalah ===")
       print(f"Kode    : {koleksi.kode}")
       print(f"Judul   : {koleksi.judul}")
       print(f"tahun   : {koleksi.tahun}")
       print(f"Penerbit: {koleksi.penerbit}")
       print(f"Edisi   : {koleksi.edisi}")