"""Segiempat talibusur beserta kedua diagonalnya.

Busur AB dipilih 84° dan busur BC 76°, jadi sudut ADB tepat 42° dan sudut BDC
tepat 38° — kedua angka yang diberikan soal. Sudut yang ditanyakan lalu tergambar
benar dengan sendirinya, dan itu memang inti soalnya.
"""

import math

from rajah import *

JARI = 3.0
ARAH = {"A": 150, "B": 66, "C": -10, "D": 250}    # urut searah jarum jam

def di(nama):
    d = math.radians(ARAH[nama])
    return titik(JARI * math.cos(d), JARI * math.sin(d))

O = titik(0, 0)
A, B, C, D = di("A"), di("B"), di("C"), di("D")

RAJAH = (
    rajah("Segiempat ABCD yang keempat titik sudutnya terletak pada satu lingkaran, "
          "dengan A di kiri, B di kanan atas, C di kanan, dan D di bawah. "
          "Kedua diagonalnya, AC dan BD, digambar. Di titik D, diagonal DB membagi "
          "sudut ADC menjadi sudut ADB yang besarnya 42 derajat dan sudut BDC yang "
          "besarnya 38 derajat")
    .lingkaran(O, JARI, gaya="bantu")
    .poligon(A, B, C, D)
    .ruas(A, C, gaya="bantu")
    .ruas(B, D, gaya="bantu")
    .tanda_sudut(A, D, B, teks="42°", jauh=46)
    .tanda_sudut(B, D, C, teks="38°", jauh=44)
    .titik(A, "A", arah=(-1, 0.4))
    .titik(B, "B", arah=(0.6, 1))
    .titik(C, "C", arah=(1, -0.2))
    .titik(D, "D", arah=(-0.4, -1))
)
