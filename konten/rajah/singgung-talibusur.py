"""Sudut antara garis singgung dan tali busur, beserta sudut keliling seberangnya.

Letak A dihitung dari busur TA = 2 x 58°, jadi sudut antara singgung dan tali
busur di gambar benar-benar 58°. B diletakkan di busur besar — sisi yang berbeda
dari A terhadap tali busur TA — sebab justru sisi itulah yang menentukan
jawabannya.
"""

import math

from rajah import *

JARI = 3.0
DI_T = 58                          # sudut antara singgung TP dan tali busur TA

def di(derajat):
    d = math.radians(derajat)
    return titik(JARI * math.cos(d), JARI * math.sin(d))

O = titik(0, 0)
T = di(270)                        # titik singgung di bawah, singgungnya mendatar
A = di(270 + 2 * DI_T)
B = di(270 + 2 * DI_T + 150)

P = T + titik(2.6, 0)              # titik pada garis singgung, di sisi tempat A
Q = T - titik(2.6, 0)

RAJAH = (
    rajah("Lingkaran dengan garis singgung mendatar yang menyentuhnya di titik T di "
          "bawah. Titik P terletak pada garis singgung di sebelah kanan T. Tali "
          "busur TA ditarik ke titik A di kanan atas lingkaran, dan titik B di kiri "
          "atas lingkaran dihubungkan ke T dan ke A. Sudut PTA besarnya 58 derajat, "
          "dan sudut TBA yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .ruas(Q, P)
    .poligon(T, A, B)
    .tanda_sudut(P, T, A, teks="58°", jauh=40)
    .tanda_sudut(T, B, A, teks="?", jauh=34)
    .titik(T, "T", arah=(-0.5, -1))
    .titik(A, "A", arah=(1, 0.4))
    .titik(B, "B", arah=(-1, 0.3))
    .titik(P, "P", arah=(0.6, -1), gaya="bantu")
)
