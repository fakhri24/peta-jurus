"""Segitiga yang dibagi dua kali: D pada BC, lalu E pada AD.

Kedua nisbahnya — BD : DC = 2 : 1 dan AE : ED = 3 : 1 — dipakai untuk menghitung
letak D dan E, jadi luas yang terarsir di gambar benar-benar sepertengah yang
dimaksud soal. Rajah luas yang nisbahnya meleset mengundang siswa menaksir dari
gambar, dan taksiran itu akan salah.
"""

from rajah import *

A, B, C = titik(1, 6), titik(0, 0), titik(9, 0)
D = bagi(B, C, 2 / 3)             # BD : DC = 2 : 1
E = bagi(A, D, 3 / 4)             # AE : ED = 3 : 1

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar. Titik D pada alas BC, terletak dua "
          "pertiga jarak dari B ke C. Ruas AD digambar, dan titik E terletak pada "
          "AD, tiga perempat jarak dari A ke D. Ruas BE digambar, dan segitiga ABE "
          "diarsir")
    .arsir(A, B, E)
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu")
    .ruas(B, E, gaya="tekan")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.4))
    .titik(C, "C", arah=(1, -0.4))
    .titik(D, "D", arah=(0.2, -1))
    .titik(E, "E", arah=(0.6, 0.8))
)
