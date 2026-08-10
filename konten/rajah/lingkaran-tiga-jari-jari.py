"""Tiga titik di keliling lingkaran, ketiganya dihubungkan ke pusat.

Letak A, B, C dipilih dari sudut pusatnya — 130°, 110°, dan 120° — supaya kedua
sudut yang diketahui soal, yaitu 25° dan 35°, keluar tepat. Ketiga jari-jari
digambar sebab justru segitiga sama kaki yang dibentuknya yang menjadi jalan
soalnya.
"""

import math

from rajah import *

JARI = 3.0
ARAH = (220, 90, 340)               # A, B, C

A, B, C = (
    titik(JARI * math.cos(math.radians(d)), JARI * math.sin(math.radians(d)))
    for d in ARAH
)
O = titik(0, 0)

RAJAH = (
    rajah("Lingkaran berpusat O dengan tiga titik A, B, dan C di kelilingnya: A di "
          "kiri bawah, B di atas, dan C di kanan. Ketiganya dihubungkan ke O oleh "
          "jari-jari, dan tali busur AB serta BC digambar. Sudut OAB besarnya 25 "
          "derajat, sudut OCB besarnya 35 derajat, dan sudut AOC yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .garis_patah(A, B, C)
    .ruas(O, A, gaya="bantu")
    .ruas(O, B, gaya="bantu")
    .ruas(O, C, gaya="bantu")
    .tanda_sudut(O, A, B, teks="25°", jauh=44)
    .tanda_sudut(O, C, B, teks="35°", jauh=42)
    .tanda_sudut(A, O, C, teks="?", jauh=30)
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(0, 1))
    .titik(C, "C", arah=(1, -0.2))
    .titik(O, "O", arah=(0.6, 0.8), gaya="bantu")
)
