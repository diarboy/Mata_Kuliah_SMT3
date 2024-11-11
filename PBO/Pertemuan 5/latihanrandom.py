import random

# Membuat daftar mahasiswa (misalnya mahasiswa 1 sampai 100)
# mahasiswa = [f"Mahasiswa {i+1}" for i in range(100)]

mahasiswa = [
    "Indah Rizkika", "Dimas Dwi Rianto", "Dimas Surya Putra", "Aurelia Septia Apriani", "Muhamad Septian Ardiansyah Yudhono", "Muhammad Labbiibul Muhsin", "Ardiyansyah", "Fasya Mahesa", "Muhammad Rizki", "Jaisyi Bagir Rafsyahid", "Muhamad Fuad Aziz", "Sabili Muhammad Azka"
]

# Daftar topik yang akan dibagikan
topik = [
    "Topik 1: Arsitektur X86", 
    "Topik 2: Arsitektur ARM", 
    "Topik 3: Perkembangan Prosesor Intel", 
    "Topik 4: Perkembangan Prosesor AMD", 
    "Topik 5: Perbedaan CPU, GPU, dan NPU"
]

# Mengacak urutan mahasiswa
random.shuffle(mahasiswa)
random.shuffle(topik)

# Tentukan jumlah kelompok
jumlah_kelompok = 4

# Pembagian mahasiswa ke dalam kelompok
kelompok = {f"Kelompok {i+1}": mahasiswa[i::jumlah_kelompok] for i in range(jumlah_kelompok)}

# Mengambil 4 topik secara acak dan membagikan ke kelompok
kelompok_topik = {f"Kelompok {i+1}": topik[i] for i in range(jumlah_kelompok)}

# Menampilkan hasil pembagian kelompok
for k, v in kelompok.items():
    print(k, v)
    
# # Menampilkan hasil pembagian kelompok dan topik
# for k in kelompok:
#     print(f"{k} : {kelompok[k]}")
#     print(f"Topik yang diberikan : {kelompok_topik[k]}")
#     print()  # Baris kosong untuk pemisah antar kelompok