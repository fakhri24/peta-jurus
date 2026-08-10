"""Segitiga 13-14-15 beserta garis tinggi ke sisi yang panjangnya 14.

Koordinatnya diturunkan dari ketiga panjang itu, bukan dipilih supaya "kelihatan
mirip". Kalau digambar kira-kira, kaki garis tingginya bisa jatuh di tempat yang
membuat siswa menebak BD = DC — persis kekeliruan yang soalnya ingin cegah.
"""

import math

from rajah import *

AB, AC, BC = 6.5, 7.5, 7.0        # setengah dari 13, 15, 14

B, C = titik(0, 0), titik(BC, 0)
x = (AB * AB - AC * AC + BC * BC) / (2 * BC)
A = titik(x, math.sqrt(AB * AB - x * x))
D = kaki(A, garis(B, C))

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar. Sisi AB panjangnya 13, sisi AC "
          "panjangnya 15, dan alas BC panjangnya 14. Dari puncak A ditarik garis "
          "tinggi ke alas, memotongnya tegak lurus di titik D yang terletak di "
          "antara B dan C, tetapi bukan di titik tengahnya")
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu", putus=True)
    .tanda_siku(B, D, A)
    .ukuran(A, B, "13")
    .ukuran(A, C, "15")
    .ukuran(B, C, "14")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.4))
    .titik(C, "C", arah=(1, -0.4))
    .titik(D, "D", arah=(-0.3, -1))
)
