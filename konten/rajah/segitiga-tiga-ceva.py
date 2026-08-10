"""Tiga ruas dari ketiga titik sudut segitiga, berpotongan di satu titik.

Perbandingannya bukan hiasan: BD : DC = 2 : 3 dan CE : EA = 3 : 4 dipilih lebih
dulu, lalu AF : FB = 2 : 1 dihitung dari teorema Ceva — dan barulah P dicari
sebagai perpotongan AD dengan BE. Rajah ini "berbohong" kalau CF tidak lewat P,
jadi kesegarisan itu diperiksa di sini sebelum berkasnya ditulis.

Kalau ketiga perbandingan dipilih sembarang, ketiga ruasnya membentuk segitiga
kecil di tengah — dan itulah gambar yang justru mengajarkan hal yang salah pada
jurus yang seluruh isinya tentang konkuren.
"""

from rajah import *

A, B, C = titik(1.3, 4.7), titik(0, 0), titik(6, 0)

D = bagi(B, C, 2 / 5)               # BD : DC = 2 : 3
E = bagi(C, A, 3 / 7)               # CE : EA = 3 : 4
F = bagi(A, B, 2 / 3)               # AF : FB = 2 : 1, dari Ceva
P = potong(garis(A, D), garis(B, E))

if jarak(P, kaki(P, garis(C, F))) > 1e-9:
    raise GagalRajah("CF tidak melewati titik potong AD dan BE — perbandingannya salah")

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, "
          "dan puncak A di atas agak ke kiri. Dari A ditarik ruas ke titik D pada "
          "sisi BC, dari B ke titik E pada sisi CA, dan dari C ke titik F pada sisi "
          "AB. Ketiga ruas itu berpotongan di satu titik P di dalam segitiga")
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu")
    .ruas(B, E, gaya="bantu")
    .ruas(C, F, gaya="bantu")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    .titik(D, "D", arah=(0, -1))
    .titik(E, "E", arah=(1, 0.5))
    .titik(F, "F", arah=(-1, 0.2))
    # Enam ruas bertemu di P, jadi labelnya harus ditaruh di celah terlebar di
    # antara keduanya — arah bawaan mana pun akan menimpa salah satu garis.
    .titik(P)
    .label(P, "P", arah=(0.42, 0.91), jauh=19)
)
