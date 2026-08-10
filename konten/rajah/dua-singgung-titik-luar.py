"""Dua garis singgung dari satu titik di luar lingkaran.

Jarak OP dihitung dari sudut APB yang dikehendaki — 48° berarti setengahnya 24°,
sehingga OP = r dibagi sin 24°. Titik singgungnya lalu diambil dari singgung(),
jadi kedua sudut siku-sikunya benar sungguhan, bukan digambar mendekati siku.
"""

import math

from rajah import *

JARI = 3.0
DI_P = 48                          # sudut APB yang dikehendaki

O = titik(0, 0)
jauh = JARI / math.sin(math.radians(DI_P / 2))
P = titik(jauh, 0)
A, B = singgung(P, O, JARI)

RAJAH = (
    rajah("Lingkaran berpusat O dengan titik P di luarnya, di sebelah kanan. Dari P "
          "ditarik dua garis singgung yang menyentuh lingkaran di A di atas dan di B "
          "di bawah. Jari-jari OA dan OB digambar dan keduanya tegak lurus garis "
          "singgungnya. Ruas OP digambar putus-putus. Sudut APB besarnya 48 derajat, "
          "dan sudut AOB yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .ruas(P, A)
    .ruas(P, B)
    .ruas(O, A, gaya="bantu")
    .ruas(O, B, gaya="bantu")
    .ruas(O, P, gaya="bantu", putus=True)
    .tanda_siku(O, A, P)
    .tanda_siku(P, B, O)
    .tanda_sudut(A, P, B, teks="48°", jauh=40)
    .tanda_sudut(A, O, B, teks="?", jauh=34)
    .titik(A, "A", arah=(0.2, 1))
    .titik(B, "B", arah=(0.2, -1))
    .titik(P, "P", arah=(1, 0))
    .titik(O, "O", arah=(-1, 0), gaya="bantu")
)
