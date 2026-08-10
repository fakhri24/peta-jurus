"""Diameter AB dengan satu titik di atasnya dan satu titik di bawahnya.

Sisi mana C dan D berada itu bagian dari soalnya, bukan hiasan: kalau keduanya
digambar di sisi yang sama, sudut COD yang ditanyakan berubah nilainya. Karena
itu letak keduanya dihitung dari sudut pusat masing-masing.
"""

import math

from rajah import *

JARI = 3.0
ARAH_C, ARAH_D = 50, 260            # 2 x 25° di atas, 2 x 40° diukur dari A di bawah

O = titik(0, 0)
A, B = titik(-JARI, 0), titik(JARI, 0)
C = titik(JARI * math.cos(math.radians(ARAH_C)), JARI * math.sin(math.radians(ARAH_C)))
D = titik(JARI * math.cos(math.radians(ARAH_D)), JARI * math.sin(math.radians(ARAH_D)))

RAJAH = (
    rajah("Lingkaran berpusat O dengan AB sebagai diameter mendatar, A di kiri dan "
          "B di kanan. Titik C di keliling lingkaran di atas AB, titik D di "
          "keliling lingkaran di bawah AB. Tali busur AC dan BD digambar, begitu "
          "pula jari-jari OC dan OD. Sudut CAB besarnya 25 derajat, sudut DBA "
          "besarnya 40 derajat, dan sudut COD yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .ruas(A, B)
    .ruas(A, C)
    .ruas(B, D)
    .ruas(O, C, gaya="bantu")
    .ruas(O, D, gaya="bantu")
    .tanda_sudut(C, A, B, teks="25°", jauh=46)
    .tanda_sudut(D, B, A, teks="40°", jauh=40)
    .tanda_sudut(C, O, D, teks="?", jauh=34)
    .titik(A, "A", arah=(-1, 0))
    .titik(B, "B", arah=(1, 0))
    .titik(C, "C", arah=(0.5, 1))
    .titik(D, "D", arah=(-0.2, -1))
    .titik(O, "O", arah=(0.9, 0.5), gaya="bantu")
)
