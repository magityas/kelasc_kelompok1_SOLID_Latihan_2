from koleksi import Koleksi

class DVD(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, sutradara, durasi, genre):
        super().__init__(kode, judul, tahun)
        self.__penerbit = penerbit
        self.__sutradara = sutradara
        self.__durasi = durasi
        self.__genre = genre
        
    @property
    def penerbit(self):
        return self.__penerbit
    
    @property
    def sutradara(self):
        return self.__sutradara
    
    @property
    def durasi(self):
        return self.__durasi
    
    @property
    def genre(self):
        return self.__genre
    
    def tampilkan_data(self):
        pass
    
class DVDPrinter:
    def tampilkan_data(self, koleksi):
        print("=== Data DVD ===")
        print(f"Kode        : {koleksi.kode}")
        print(f"Judul       : {koleksi.judul}")
        print(f"Tahun       : {koleksi.tahun}")
        print(f"Penerbit    : {koleksi.penerbit}")
        print(f"Sutradara   : {koleksi.sutradara}")
        print(f"Durasi      : {koleksi.durasi}")
        print(f"Genre       : {koleksi.genre}")