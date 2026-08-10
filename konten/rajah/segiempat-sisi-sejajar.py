"""Segiempat dengan sepasang sisi berhadapan sejajar dan sama panjang."""

from rajah import *

A, B = titik(0, 0), titik(5, 0)
# D digeser dari A, C digeser dari B dengan pergeseran yang sama — itu yang membuat
# DC sejajar AB sekaligus sama panjang, tanpa perlu ditaksir.
geser = titik(1.6, 3)
D, C = A + geser, B + geser

RAJAH = (
    rajah("Segiempat ABCD dengan sisi AB mendatar di bawah dan sisi DC mendatar di "
          "atas, keduanya sama panjang dan sejajar. Diagonal AC digambar, membagi "
          "segiempat itu menjadi segitiga ABC dan segitiga CDA")
    .poligon(A, B, C, D)
    .ruas(A, C, gaya="bantu")
    .tanda_sama(A, B)
    .tanda_sama(D, C)
    .tanda_sudut(B, A, C, teks="α")
    .tanda_sudut(D, C, A, teks="α")
    .titik(A, "A", arah=(-1, -0.6))
    .titik(B, "B", arah=(1, -0.6))
    .titik(C, "C", arah=(1, 0.6))
    .titik(D, "D", arah=(-1, 0.6))
)
