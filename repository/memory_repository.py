from abc import ABC, abstractmethod

class KoleksiRepository(ABC):
    @abstractmethod
    def tambah(self, koleksi):
        pass

    @abstractmethod
    def ambil_semua(self):
        pass

    @abstractmethod
    def cari_by_id(self, id_koleksi):
        pass

    @abstractmethod
    def hapus(self, id_koleksi):
        pass


class MemoryRepository(KoleksiRepository):
    def __init__(self):
        self._database = []

    def tambah(self, koleksi):
        if self.cari_by_id(koleksi.id_koleksi):
            return False
        self._database.append(koleksi)
        return True

    def ambil_semua(self):
        return self._database

    def cari_by_id(self, id_koleksi):
        for item in self._database:
            if item.id_koleksi.lower() == id_koleksi.lower():
                return item
        return None

    def hapus(self, id_koleksi):
        item = self.cari_by_id(id_koleksi)
        if item:
            self._database.remove(item)
            return True
        return False
