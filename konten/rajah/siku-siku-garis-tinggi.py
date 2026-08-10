"""Segitiga siku-siku dengan garis tinggi dari titik siku-sikunya ke sisi miring.

Sengaja tanpa angka: rajah yang sama dipakai soal yang memberi potongan sisi
miringnya sebagai bilangan dan soal yang membuktikan hubungannya secara umum.
Perbandingan potongannya dipilih 4 : 9, jadi kakinya jelas tidak sama panjang.
"""

import math

from rajah import *

p, q = 2.0, 4.5                   # sebanding 4 : 9

A, B = titik(0, 0), titik(p + q, 0)
D = titik(p, 0)
C = titik(p, math.sqrt(p * q))     # tinggi = akar pq, jadi sudut C tepat siku-siku

RAJAH = (
    rajah("Segitiga ABC siku-siku di C, dengan sisi miring AB mendatar. Dari C "
          "ditarik garis tinggi yang memotong sisi miring tegak lurus di titik D, "
          "membagi AB menjadi potongan AD yang pendek dan DB yang lebih panjang")
    .poligon(A, B, C)
    .ruas(C, D, gaya="bantu")
    .tanda_siku(A, C, B)
    .tanda_siku(A, D, C)
    .titik(A, "A", arah=(-1, -0.3))
    .titik(B, "B", arah=(1, -0.3))
    .titik(C, "C", arah=(0, 1))
    .titik(D, "D", arah=(0, -1))
)
