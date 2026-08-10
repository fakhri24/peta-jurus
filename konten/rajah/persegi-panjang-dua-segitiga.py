"""Persegi panjang dengan titik dalam, dan dua segitiga berhadapan yang diarsir.

Tinggi P dihitung dari luas segitiga bawah yang diberikan soal — 30 pada alas 12
berarti tingginya 5 — supaya gambarnya tidak menampilkan P di tengah dan
mengundang tebakan bahwa kedua luasnya sama.
"""

from rajah import *

KECIL = 2.0
LEBAR, TINGGI = 12 / KECIL, 8 / KECIL
NAIK = (2 * 30 / 12) / KECIL      # dari luas segitiga bawah, bukan dikira-kira

A, B = titik(0, 0), titik(LEBAR, 0)
C, D = titik(LEBAR, TINGGI), titik(0, TINGGI)
P = titik(2.2, NAIK)

RAJAH = (
    rajah("Persegi panjang ABCD dengan A di kiri bawah, B di kanan bawah, C di "
          "kanan atas, dan D di kiri atas. Titik P di dalamnya, lebih dekat ke sisi "
          "kiri dan sedikit di atas pertengahan tinggi. Segitiga PAB yang beralas "
          "sisi bawah dan segitiga PCD yang beralas sisi atas keduanya diarsir")
    .arsir(P, A, B)
    .arsir(P, C, D)
    .poligon(A, B, C, D)
    .ruas(P, A, gaya="bantu")
    .ruas(P, B, gaya="bantu")
    .ruas(P, C, gaya="bantu")
    .ruas(P, D, gaya="bantu")
    .titik(A, "A", arah=(-1, -1))
    .titik(B, "B", arah=(1, -1))
    .titik(C, "C", arah=(1, 1))
    .titik(D, "D", arah=(-1, 1))
    .titik(P, "P", arah=(-1, 0.1))
)
