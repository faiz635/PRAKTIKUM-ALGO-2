# import math
# nilai1 = float(input('masukkan nilai A = '))
# nilai2 = float(input('masukkan nilai B = '))

# penjumlahan = nilai1 + nilai2
# print(f'hasil dari penjumlahan A + B adalah {float(penjumlahan)}')

# selisih = nilai1 - nilai2
# print(f'selisih antara nilai A dan B adalah {float(selisih)}')

# perkalian = nilai1 * nilai2
# print(f'jumlah A dikali B adalah {float(perkalian)}')

# pembagian = nilai1 / nilai2
# print(f'jumlah A di bagi B adalah {float(pembagian)}')

# modulus = nilai1 % nilai2
# print(f'jumlah sisa pembagian dari A dan B adalah {float(modulus)}')

# pangkat = nilai1 ** nilai2
# print(f'hasil A dipangkat B adalah {float(pangkat)}')

# logA = math.log(nilai1)
# print(f'hasil dari log A adalah {float(logA)}')



#FAIZ NUGROHO
#065002400003

import math

lintang1 = math.radians(float(input("Lintang Kota 1 = ")))
bujur1 = math.radians(float(input("Bujur Kota 1 = ")))
lintang2 = math.radians(float(input("Lintang kota 2 = ")))
bujur2 = math.radians(float(input("Bujur kota 2 = ")))

radius = 6371
lat = lintang2 - lintang1
long = bujur2 - bujur1

a =  math.sin(lat/2)*2 + math.cos(lintang1) * math.cos(lintang2) * math.sin(long/2)*2
C3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = radius * C3

print(f"jarak antara dua titik tersebut adalah ", (d) , "kilometer")

