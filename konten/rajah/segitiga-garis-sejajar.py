"""Segitiga dengan ruas sejajar alas yang memotong kedua sisi lainnya.

D dan E ditaruh pada nisbah yang sama dari A, jadi DE sejajar BC menurut
hitungannya — bukan menurut mata. Kalau digambar kira-kira, gambar yang sedikit
miring justru mengajarkan bahwa "kelihatan sejajar" sudah cukup.
"""

from rajah import *

NISBAH = 0.6                      # AD : AB = 6 : 10

A, B, C = titik(1.2, 5.2), titik(0, 0), titik(7, 0)
D = bagi(A, B, NISBAH)            # bagi(A, B, t): t = 0 di A, t = 1 di B
E = bagi(A, C, NISBAH)

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Titik D pada "
          "sisi AB dan titik E pada sisi AC, dengan ruas DE sejajar alas BC. Ruas "
          "AD panjangnya 6, DB panjangnya 4, AE panjangnya 9, dan EC yang "
          "ditanyakan")
    .poligon(A, B, C)
    .ruas(D, E, gaya="tekan")
    .ukuran(A, D, "6")
    .ukuran(D, B, "4")
    .ukuran(A, E, "9")
    .ukuran(E, C, "?")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    .titik(D, "D", arah=(-1, 0))
    .titik(E, "E", arah=(1, 0.2))
)
