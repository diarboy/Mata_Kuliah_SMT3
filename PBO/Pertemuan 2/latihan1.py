#Membuat Class
class Mobil:
    #Membuat class variable
    jumlah_mobil = 0

    #Membuat Construktor
    def __init__(self, ban, merek, cc):
        #Instance Variable
        self.merkban = ban
        self.merkmobil = merek
        self.cilinder = cc
        Mobil.jumlah_mobil += 1

    #Membuat method string
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.cilinder}"
    
    #Membuat method baru, contohnya "BORE UP" peningkatan kapasitas
    def boreup(self, bore):
        self.cilinder += bore

#Membuat Objek Baru M1
M1 = Mobil("Bridgestone", "Toyota-Kijang", 1500)
print(M1)
print("Jumlah Mobil: ", Mobil.jumlah_mobil)
M1.boreup(500)
print(M1)

#Membuat Objek Baru M2
M2 = Mobil("Michelin", "Toyota-86", 1998)
print(M2)
print("Jumlah Mobil: ", Mobil.jumlah_mobil)
M2.boreup(500)
print(M2)