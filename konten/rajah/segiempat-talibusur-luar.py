"""Segiempat talibusur dengan salah satu sisinya diperpanjang.

Letak keempat titik dihitung dari busur yang dikehendaki: sudut ADC 115° berarti
busur ABC 230°, dan sisanya 130° untuk busur ADC. Dengan begitu sudut luar di B
benar-benar tergambar 115°, bukan sekadar terlihat tumpul.
"""

import math

from rajah import *

JARI = 3.0
ARAH = {"A": 150, "B": 30, "C": 280, "D": 215}    # urut searah jarum jam

def di(nama):
    d = math.radians(ARAH[nama])
    return titik(JARI * math.cos(d), JARI * math.sin(d))

O = titik(0, 0)
A, B, C, D = di("A"), di("B"), di("C"), di("D")
E = B + (B - A).satuan() * 1.9                    # perpanjangan AB melewati B

RAJAH = (
    rajah("Segiempat ABCD yang keempat titik sudutnya terletak pada satu lingkaran, "
          "dengan A di kiri atas, B di kanan atas, C di bawah, dan D di kiri bawah. "
          "Sisi AB diperpanjang melewati B sampai titik E di luar lingkaran. "
          "Sudut ADC besarnya 115 derajat, dan sudut CBE yang ditanyakan")
    .lingkaran(O, JARI, gaya="bantu")
    .poligon(A, B, C, D)
    .ruas(B, E, putus=True)
    .tanda_sudut(A, D, C, teks="115°", jauh=34)
    .tanda_sudut(C, B, E, teks="?", jauh=32)
    .titik(A, "A", arah=(-1, 0.5))
    .titik(B, "B", arah=(0, 1))
    .titik(C, "C", arah=(0.6, -1))
    .titik(D, "D", arah=(-1, -0.5))
    .titik(E, "E", arah=(1, 0.2))
)
