"""Dua garis sejajar dengan satu titik di antaranya — bentuk zigzag."""

import math

from rajah import *

# Sudut di B dan di D yang diketahui soal. E dihitung darinya, bukan ditaksir:
# kalau digambar kira-kira, sudut yang tertulis 42° bisa saja tergambar 47°, dan
# siswa yang mengukur gambarnya justru dihukum karena percaya pada rajahnya.
DI_B, DI_D = 42, 63

B = titik(0, 0)
E = B + titik(math.cos(math.radians(DI_B)), math.sin(math.radians(DI_B))) * 2

# D di garis atas (y = 3), pada arah yang membentuk DI_D dengan arah mendatar.
naik = (3 - E.y) / math.sin(math.radians(DI_D))
D = E + titik(-math.cos(math.radians(DI_D)), math.sin(math.radians(DI_D))) * naik

A, C = titik(4.2, 0), titik(4.2, 3)
ujung_l, ujung_m = titik(-1.4, 0), titik(-1.4, 3)

RAJAH = (
    rajah("Garis l dan garis m sejajar mendatar. Titik B pada garis l dan titik D "
          "pada garis m, dengan A pada garis l di sebelah kanan B dan C pada garis "
          "m di sebelah kanan D. Titik E terletak di antara kedua garis, dihubungkan "
          "ke B dan ke D sehingga membentuk zigzag. Sudut ABE besarnya 42 derajat, "
          "sudut CDE besarnya 63 derajat, dan sudut BED yang ditanyakan")
    .ruas(ujung_l, A)
    .ruas(ujung_m, C)
    .garis_patah(B, E, D)
    .tanda_sudut(A, B, E, teks="42°", jauh=36)
    .tanda_sudut(C, D, E, teks="63°", jauh=36)
    .tanda_sudut(B, E, D, teks="?", jauh=30)
    .titik(B, "B", arah=(-0.5, -1))
    .titik(A, "A", arah=(1, -0.5))
    .titik(D, "D", arah=(-0.5, 1))
    .titik(C, "C", arah=(1, 0.5))
    .titik(E, "E", arah=(1, 0))
    .label(ujung_l, "l", arah=(0, -1), gaya="bantu")
    .label(ujung_m, "m", arah=(0, 1), gaya="bantu")
)
