"""Dua garis tinggi segitiga lancip, beserta titik potongnya.

Kaki kedua garis tinggi dihitung dengan kaki() dan titik potongnya dengan potong(),
jadi ketiga hal yang jadi tumpuan soal — dua sudut siku-siku dan kesegarisan A, H, D
— benar sungguhan.

Lingkaran yang melalui A, B, D, E sengaja tidak digambar: menemukan lingkaran itu
justru seluruh isi soalnya. Yang digambar cuma apa yang disebut soal.

Sudut alasnya dipilih lancip dan tidak sama besar supaya H jatuh jelas di dalam
segitiga tanpa terlihat seperti titik istimewa yang lain.
"""

import math

from rajah import *

DI_B, DI_C = 62.0, 54.0
ALAS = 8.0

B, C = titik(0, 0), titik(ALAS, 0)
x = ALAS * math.tan(math.radians(DI_C)) / (
    math.tan(math.radians(DI_B)) + math.tan(math.radians(DI_C)))
A = titik(x, x * math.tan(math.radians(DI_B)))

D = kaki(A, garis(B, C))          # kaki garis tinggi dari A
E = kaki(B, garis(A, C))          # kaki garis tinggi dari B
H = potong(garis(A, D), garis(B, E))

RAJAH = (
    rajah("Segitiga ABC lancip dengan alas BC mendatar, B di kiri bawah, C di kanan "
          "bawah, dan puncak A di atas. Dari A ditarik garis tinggi ke alas, "
          "memotongnya tegak lurus di titik D di antara B dan C. Dari B ditarik "
          "garis tinggi ke sisi AC, memotongnya tegak lurus di titik E. Kedua garis "
          "tinggi itu berpotongan di titik H di dalam segitiga")
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu")
    .ruas(B, E, gaya="bantu")
    .tanda_siku(A, D, C)
    .tanda_siku(B, E, A)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    .titik(D, "D", arah=(-0.3, -1))
    .titik(E, "E", arah=(1, 0.5))
    .titik(H, "H", arah=(-1, 0.3))
)
