from models.koleksi import Koleksi

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        super().__init__(kode, judul, tahun)
        self.__penerbit = penerbit
        self.__bidang_studi = bidang_studi
        self.__impact_factor = impact_factor
        
    @property
    def penerbit(self):
        return self.__penerbit
    
    @property
    def bidang_studi(self):
        return self.__bidang_studi
    
    @property
    def impact_factor(self):
        return self.__impact_factor
    
    def tampilkan_data(self):
        pass
    
class JurnalPrinter:
    def tampilkan_data(self, koleksi):
        print("=== Data Jurnal ===")
        print(f"Kode        : {koleksi.kode}")
        print(f"Judul       : {koleksi.judul}")
        print(f"Tahun       : {koleksi.tahun}")
        print(f"Penerbit    : {koleksi.penerbit}")
        print(f"Bidang Studi: {koleksi.bidang_studi}")
        print(f"Impact Fact.: {koleksi.impact_factor}")