from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun
        
    @property
    def kode(self):
        return self.__kode
    
    @property
    def judul(self):
        return self.__judul
    
    @property
    def tahun(self):
        return self.__tahun
    
    @abstractmethod
    def tampilkan_data(self):
        pass