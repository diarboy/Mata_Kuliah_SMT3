# Membuat sebuah Super Class
class Animal:
    # Membuat konstruktor untuk menampung attribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras
    # Membuat method bersuara
    def Speaks(self):
        print(f"{self.name} bisa bersuara")

# Membuat class turunan dari Super Class
class Cat(Animal):
    def speaksCat(self):
        print(f"Nama {self.name} dengan Ras {self.ras} bersuara 'Meooowww!'")

# Membuat Objek
cat = Cat("Kitty", "Angora")
cat.speaksCat()

class Dog(Animal):
    def speaksDog(self):
        print(f"Nama {self.name} dari Ras {self.ras} bersuara 'Guk Guk!'")

# Membuat Objek
dog = Dog("Puppy", "Pitbull")
dog.speaksDog()