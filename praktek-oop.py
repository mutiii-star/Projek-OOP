class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.__buku = [] # Encopulation: data buku disembunyikan

    def tambah_buku(self, buku):
        self.__buku.append(buku)

    def tampilkan_buku(self):
        for buku in self.__buku:
            print(buku.info())

    def __str__(self):
        return f"Perpustakaan: {self.nama}"
    
class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        return f"buku: {self.judul} oleh {self.penulis}"
    
class bukufiksi(buku):
    def __init__(self, judul, penulis, genre):
        super().__init__(judul, penulis)
        self.genre = genre

    def info(self):
        return f"buku fiksi: {self.judul} oleh {self.penulis}, genre: {self.genre}"
    
class bukunonfiksi(buku):
    def __init__(self, judul, penulis, topik):
        super().__init__(judul, penulis)
        self.topik = topik

    def info(self):
        return f"buku non-fiksi: {self.judul} oleh {self.penulis}, topik: {self.topik}"
    
Perpustakaan = Perpustakaan("Perpustakaan kota")

buku1 = bukufiksi("harry potter", "j,k rowling", "fantasi")
buku2 = bukunonfiksi("sapiens", "yuval noah harari", "sejarah")

Perpustakaan.tambah_buku(buku1)
Perpustakaan.tambah_buku(buku2)

print(Perpustakaan)
Perpustakaan.tampilkan_buku()