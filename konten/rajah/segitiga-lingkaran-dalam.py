"""Segitiga dengan lingkaran dalamnya dan ketiga titik singgungnya."""

from rajah import *

A, B, C = titik(0, 0), titik(6, 0), titik(1.6, 4.2)
I = pusat_dalam(A, B, C)
r = jari_dalam(A, B, C)

# Titik singgung dihitung sebagai kaki tegak lurus dari I ke tiap sisi — sekaligus
# yang membuat rajahnya benar: ketiganya pasti tepat di lingkaran.
X = kaki(I, garis(B, C))
Y = kaki(I, garis(C, A))
Z = kaki(I, garis(A, B))

RAJAH = (
    rajah("Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung "
          "sisi BC di X, sisi CA di Y, dan sisi AB di Z")
    .poligon(A, B, C)
    .lingkaran(I, r, gaya="bantu")
    .ruas(I, X, gaya="bantu", putus=True)
    .tanda_siku(B, X, I)
    .titik(A, "A").titik(B, "B").titik(C, "C")
    .titik(I, "I", gaya="bantu")
    .titik(X, "X", gaya="bantu")
    .titik(Y, "Y", gaya="bantu")
    .titik(Z, "Z", gaya="bantu")
)
