from abc import ABC, abstractmethod

class KoleksiRepository(ABC):
    @abstractmethod
    def tambah(self, koleksi):
        pass

    @abstractmethod
    def ambil_semua(self):
        pass

    @abstractmethod
    def cari(self, kode):
        pass

    @abstractmethod
    def hapus(self, kode):
        pass


class MemoryRepository(KoleksiRepository):
    def __init__(self):
        self._database = []

    def tambah(self, koleksi):
        if self.cari(koleksi.kode):
            return False
        self._database.append(koleksi)
        return True

    def ambil_semua(self):
        return self._database

    def cari(self, kode):
        for item in self._database:
            if item.kode.lower() == kode.lower():
                return item
        return None

    def hapus(self, kode):
        item = self.cari(kode)
        if item:
            self._database.remove(item)
            return True
        return False