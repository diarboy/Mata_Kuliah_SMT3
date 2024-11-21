# Tanpa Implementasi Polimorfisme
class Penjumlahan:
    def tambah( n1, n2): #perlu deklarasi satu per satu objek
        print (f"Contoh Pertama Hasilnya: {n1+n2}")
objek3 = Penjumlahan
objek3.tambah(2,3) # Argumen harus sesuai dengan parameter

# Implementasi Polimorfisme
#Lebih Fleksibel
class Penjumlahan:
    def tambah(*num):
        return sum(num)
objek1 = Penjumlahan
print(f"Contoh Kedua Hasilnya: {objek1.tambah(2,3,5,10)}")

#Default Parameter
class Default:
    def tambah2(self, a, b=0, c=0, d=0, e=0):
        print (f"Contoh Ketiga Hasilnya: {a+b+c+d+e}")
objek2 = Default
objek2.tambah2(2,4,2,1,1)