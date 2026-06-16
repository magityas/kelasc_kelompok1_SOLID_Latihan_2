from abc import ABC

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.__kode = kode
        self.__judul = judul
        self.__tahun = tahun

    @property
    def kode(self):
        return self.__kode

    @property
    def judul(self):
        return self.__judul

    @property
    def tahun(self):
        return self.__tahun