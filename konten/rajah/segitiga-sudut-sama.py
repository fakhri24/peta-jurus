"""Segitiga ABC dengan D pada BC, disusun supaya sudut BAD sama besar sudut BCA.

Letak A dihitung dari AB = 8, BD = 4, BC = 16 yang dipakai soal — dan kesamaan
sudutnya lalu keluar sendiri, berapa pun arah A dipilih. Itu sekaligus isi
soalnya: yang menentukan bukan bentuk segitiganya, melainkan AB kuadrat sama
dengan BD kali BC.
"""

import math

from rajah import *

ARAH_A = 40                       # bebas; kesamaan sudutnya tidak bergantung padanya
KECIL = 2.0

B, C = titik(0, 0), titik(16 / KECIL, 0)
D = titik(4 / KECIL, 0)
A = titik(8 / KECIL * math.cos(math.radians(ARAH_A)),
          8 / KECIL * math.sin(math.radians(ARAH_A)))

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Titik D "
          "terletak pada alas BC, lebih dekat ke B daripada ke C, dan dihubungkan "
          "ke A. Sudut BAD dan sudut BCA ditandai sama besar")
    .poligon(A, B, C)
    .ruas(A, D, gaya="tekan")
    .tanda_sudut(B, A, D, teks="α", jauh=40)
    .tanda_sudut(B, C, A, teks="α", jauh=40)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.4))
    .titik(C, "C", arah=(1, -0.4))
    .titik(D, "D", arah=(0.2, -1))
)
