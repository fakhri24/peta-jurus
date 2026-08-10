"""Garis berat AM diperpanjang sejauh dirinya sendiri sampai D, lalu BD ditarik.

Bangunnya dihitung dari panjang yang dipakai soal: AB : AC = 9 : 13, dengan BC
dipilih supaya segitiganya terlihat wajar. Kalau digambar kira-kira, AB bisa saja
tergambar lebih panjang daripada AC dan rajahnya justru melawan soalnya.
"""

import math

from rajah import *

AB, AC, BC = 4.5, 6.5, 7.0        # setengah dari 9, 13, 14

B, C = titik(0, 0), titik(BC, 0)
x = (AB * AB - AC * AC + BC * BC) / (2 * BC)
A = titik(x, math.sqrt(AB * AB - x * x))

M = tengah(B, C)
D = M + (M - A)                   # MD = AM menurut susunannya, bukan menurut mata

RAJAH = (
    rajah("Segitiga ABC dengan M titik tengah sisi BC. Ruas AM diperpanjang lurus "
          "melewati M sampai titik D, sedemikian sehingga MD sama panjang dengan "
          "AM. Titik D dihubungkan ke B, sehingga terbentuk segitiga ABD yang "
          "memuat segitiga ABC")
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu")
    .ruas(B, D)
    .ruas(C, D, gaya="bantu", putus=True)
    .tanda_sama(B, M)
    .tanda_sama(M, C)
    .tanda_sama(A, M, rangkap=2)
    .tanda_sama(M, D, rangkap=2)
    .titik(A, "A", arah=(-0.3, 1))
    .titik(B, "B", arah=(-1, 0))
    .titik(C, "C", arah=(1, 0.4))
    .titik(M, "M", arah=(0, 1))
    .titik(D, "D", arah=(0.4, -1))
)
