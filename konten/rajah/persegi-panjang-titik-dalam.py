"""Persegi panjang dengan satu titik di dalamnya, dihubungkan ke keempat sudut.

Letak P dihitung dari keempat jaraknya yang dipakai soal — PA = 6, PB = 10,
PC = 17, PD = 15 — lalu semuanya diperkecil sepertiga supaya muat di layar. Yang
penting bentuknya benar: P harus terlihat lebih dekat ke A daripada ke C, sebab
memang begitu angkanya.
"""

import math

from rajah import *

KECIL = 3.0                        # perkecil bersama-sama; bentuknya tidak berubah
PA, PB, PC = 6.0, 10.0, 17.0
y = 4.0                            # satu-satunya kebebasan yang tersisa; dipilih
                                   # supaya P tidak menempel ke sisi bawah
x = math.sqrt(PA * PA - y * y)
lebar = x + math.sqrt(PB * PB - y * y)
tinggi = y + math.sqrt(PC * PC - (lebar - x) ** 2)

A = titik(0, 0)
B = titik(lebar / KECIL, 0)
C = titik(lebar / KECIL, tinggi / KECIL)
D = titik(0, tinggi / KECIL)
P = titik(x / KECIL, y / KECIL)

RAJAH = (
    rajah("Persegi panjang ABCD dengan A di kiri bawah, B di kanan bawah, C di "
          "kanan atas, dan D di kiri atas. Titik P di dalamnya, terletak agak "
          "dekat ke sudut A, dihubungkan dengan ruas garis ke keempat titik sudut")
    .poligon(A, B, C, D)
    .ruas(P, A, gaya="bantu")
    .ruas(P, B, gaya="bantu")
    .ruas(P, C, gaya="bantu")
    .ruas(P, D, gaya="bantu")
    .titik(A, "A", arah=(-1, -1))
    .titik(B, "B", arah=(1, -1))
    .titik(C, "C", arah=(1, 1))
    .titik(D, "D", arah=(-1, 1))
    # Keempat ruas dari P memenuhi sekelilingnya; celah terlebar ada di sisi kiri,
    # antara ruas ke D dan ruas ke A.
    .titik(P, "P", arah=(-1, 0.28))
)
