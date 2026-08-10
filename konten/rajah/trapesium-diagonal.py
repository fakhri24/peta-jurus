"""Trapesium dengan kedua diagonalnya, berpotongan di P.

Nisbah sisi sejajarnya 15 : 10 dipakai apa adanya sebagai lebar atas dan bawah,
supaya letak P di gambar benar-benar membagi diagonalnya 3 : 2 seperti jawabannya.
"""

from rajah import *

BAWAH, ATAS = 4.5, 3.0            # sebanding 15 : 10
TINGGI = 3.2

A, B = titik(0, 0), titik(BAWAH, 0)
D = titik(0.9, TINGGI)
C = D + titik(ATAS, 0)

P = potong(garis(A, C), garis(B, D))

RAJAH = (
    rajah("Trapesium ABCD dengan sisi AB mendatar di bawah dan sisi DC mendatar di "
          "atas, keduanya sejajar dan AB lebih panjang daripada DC. Kedua "
          "diagonalnya, AC dan BD, digambar dan berpotongan di titik P")
    .poligon(A, B, C, D)
    .ruas(A, C, gaya="bantu")
    .ruas(B, D, gaya="bantu")
    .titik(A, "A", arah=(-1, -0.6))
    .titik(B, "B", arah=(1, -0.6))
    .titik(C, "C", arah=(1, 0.6))
    .titik(D, "D", arah=(-1, 0.6))
    .titik(P, "P", arah=(0, 1))
)
