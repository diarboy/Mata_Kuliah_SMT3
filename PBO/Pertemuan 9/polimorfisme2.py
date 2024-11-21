# Implementasi Polimorfisme dengan mencari Bangun Datar
class BangunDatar: #Abstract Class
    def luas(self): #Abstract Method
        raise NotImplementedError("Method ini Wajib diimplementasikan")
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        print(f"Luas Persegi adalah {self.sisi**2} m2")

class Segitiga(BangunDatar): #Kelas Turunan 2
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        print(f"Luas Segitiga adalah: {(self.alas*self.tinggi)/2}")

class __Lingkaran(BangunDatar): # Kelas turunan 2 #private 2 underscore
    def __init__(self, r=0, pi=3.14):
        self.pi = pi
        self.r = r
    def luas(self):
        print(f"Luas Lingkaran adalah: {self.pi*self.r**2}")

objek1 = Persegi(8)
objek2 = Segitiga(2,3)
objek3 = __Lingkaran(5) #private 2 underscore
objek1.luas()
objek2.luas()
objek3.luas()