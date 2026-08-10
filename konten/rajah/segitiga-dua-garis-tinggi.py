"""Segitiga dengan dua garis tinggi, dan ruas yang menghubungkan kedua kakinya.

Kaki garis tingginya dihitung dengan kaki(), jadi kedua sudut siku-sikunya benar
sungguhan — dan justru kedua sudut siku-siku itu yang menjadi pemicu soalnya.
Lingkaran yang melalui B, C, E, F sengaja tidak digambar: menemukannya bagian
dari pekerjaan siswa.
"""

import math

from rajah import *

DI_B, DI_C = 64.0, 50.0           # sudut alas, menentukan bentuk segitiganya
ALAS = 9.0

B, C = titik(0, 0), titik(ALAS, 0)
x = ALAS * math.tan(math.radians(DI_C)) / (
    math.tan(math.radians(DI_B)) + math.tan(math.radians(DI_C)))
A = titik(x, x * math.tan(math.radians(DI_B)))

E = kaki(B, garis(A, C))          # kaki garis tinggi dari B
F = kaki(C, garis(A, B))          # kaki garis tinggi dari C

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Dari B "
          "ditarik garis tinggi ke sisi AC yang memotongnya tegak lurus di E, dan "
          "dari C ditarik garis tinggi ke sisi AB yang memotongnya tegak lurus di "
          "F. Kedua kaki itu dihubungkan oleh ruas EF")
    .poligon(A, B, C)
    .ruas(B, E, gaya="bantu", putus=True)
    .ruas(C, F, gaya="bantu", putus=True)
    .ruas(E, F, gaya="tekan")
    .tanda_siku(A, E, B)
    .tanda_siku(A, F, C)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    .titik(E, "E", arah=(1, 0.4))
    .titik(F, "F", arah=(-1, 0.2))
)
