# Membuat sample inheritance dengan method pass
# Membuat kelas superclass animal
class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # Membuat Method Sound
    def sound(self):
        print(f"This {self.name} makes a sound")

# Membuat kelas turunan / subclass Dog
class Dog(Animal):
    pass
name = input("masukkan Nama pets anda: ")
dog = Dog(name, 3)
dog.sound()