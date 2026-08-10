"""Segitiga sama kaki dengan satu titik pada alasnya, bukan di titik tengahnya.

Dipakai contoh tandingan S-S-Sd: segitiga ABD dan ACD punya dua pasang sisi sama
panjang (AB = AC dan AD berimpit) beserta sepasang sudut sama besar (sudut B dan
sudut C), namun jelas tidak kongruen — BD dan CD berbeda jauh.
"""

from rajah import *

A, B, C = titik(0, 4), titik(-3, 0), titik(3, 0)
D = titik(-2, 0)          # BD = 1, DC = 5 — sengaja jauh dari titik tengah

RAJAH = (
    rajah("Segitiga ABC sama kaki dengan puncak A di atas dan alas BC mendatar. "
          "Sisi AB dan AC ditandai sama panjang. Titik D terletak pada alas BC, "
          "dekat ke B dan jauh dari titik tengahnya, dan dihubungkan ke A")
    .poligon(A, B, C)
    .ruas(A, D, gaya="tekan")
    .tanda_sama(A, B)
    .tanda_sama(A, C)
    .tanda_sudut(A, B, C)
    .tanda_sudut(B, C, A)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.4))
    .titik(C, "C", arah=(1, -0.4))
    .titik(D, "D", arah=(0.2, -1))
)
