#Membuat Class
class Buku:
    jumlah_buku = 0
    def __init__(self, judul, penulis, tahun_terbit):
        self.judulbuku = judul
        self.penulisbuku = penulis
        self.tahunterbit = tahun_terbit
        Buku.jumlah_buku += 1
    def __str__(self):
        return f"{self.judulbuku}, {self.penulisbuku}, {self.tahunterbit}"
    
    def rev_tahun(self, rev):
        self.tahun_terbit = rev

B1 = Buku("Thus Spake Zarathustra", "Friedrich Nietzsche", 1883)
print(B1)
print("Jumlah Buku: ", Buku.jumlah_buku)
B1.rev_tahun(1883-1885)
print(B1)

B2 = Buku("To Kill a Mockingbird", "Harper Lee", 1960)
print(B2)
print("Jumlah Buku: ", Buku.jumlah_buku)
B2.rev_tahun(1960-1965)
print(B2)