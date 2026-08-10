"""Lingkaran berdiameter AB dengan satu titik C di kelilingnya.

Letak C dihitung dari sudut pusat yang dikehendaki, jadi sudut keliling yang
tertulis 32° benar-benar 32° di gambarnya. Rajah sudut yang meleset lebih buruk
daripada rajah panjang yang meleset: sudut justru yang sedang dibicarakan.
"""

import math

from rajah import *

JARI = 3.0
PUSAT_COB = 64                      # dua kali sudut keliling 32°

O = titik(0, 0)
A, B = titik(-JARI, 0), titik(JARI, 0)
C = titik(JARI * math.cos(math.radians(PUSAT_COB)),
          JARI * math.sin(math.radians(PUSAT_COB)))

RAJAH = (
    rajah("Lingkaran berpusat O dengan AB sebagai diameter mendatar, A di kiri dan "
          "B di kanan. Titik C terletak di keliling lingkaran di atas AB. Tali "
          "busur AC dan CB digambar, begitu pula jari-jari OC. Sudut CAB besarnya "
          "32 derajat, dan sudut COB yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .ruas(A, B)
    .poligon(A, B, C)
    .ruas(O, C, gaya="bantu")
    .tanda_sudut(C, A, B, teks="32°", jauh=42)
    .tanda_sudut(C, O, B, teks="?", jauh=32)
    .titik(A, "A", arah=(-1, -0.2))
    .titik(B, "B", arah=(1, -0.2))
    .titik(C, "C", arah=(0.4, 1))
    .titik(O, "O", arah=(-0.3, -1), gaya="bantu")
)
