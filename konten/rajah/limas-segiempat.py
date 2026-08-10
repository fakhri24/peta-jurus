"""Limas segiempat beraturan beserta diagonal alas dan tingginya.

Tingginya digambar sebanding dengan angka soal — alas 12, tinggi 7 — supaya
limasnya tidak tergambar lebih jangkung atau lebih ceper daripada yang dibicarakan.
Rusuk yang tersembunyi di belakang digambar putus-putus, seperti kebiasaan
menggambar bangun ruang.
"""

from rajah import *

SISI = 4.2
TINGGI = SISI * 7 / 12            # nisbah tinggi terhadap sisi, dari angka soal

A = ruang(0, 0, 0)
B = ruang(SISI, 0, 0)
C = ruang(SISI, SISI, 0)
D = ruang(0, SISI, 0)
O = ruang(SISI / 2, SISI / 2, 0)
T = ruang(SISI / 2, SISI / 2, TINGGI)

RAJAH = (
    rajah("Limas segiempat beraturan dengan alas persegi ABCD dan puncak T tepat di "
          "atas titik potong diagonal alas. Titik O adalah perpotongan diagonal AC "
          "dan BD, dan ruas TO digambar putus-putus sebagai tinggi limas, tegak "
          "lurus alas. Rusuk AD, DC, dan TD tersembunyi di belakang sehingga "
          "digambar putus-putus")
    .garis_patah(A, B, C)
    .ruas(A, D, putus=True)
    .ruas(D, C, putus=True)
    .ruas(T, A)
    .ruas(T, B)
    .ruas(T, C)
    .ruas(T, D, putus=True)
    .ruas(A, C, gaya="bantu", putus=True)
    .ruas(B, D, gaya="bantu", putus=True)
    .ruas(T, O, gaya="tekan", putus=True)
    .tanda_siku(T, O, A)
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(1, -0.5))
    .titik(C, "C", arah=(1, 0.2))
    .titik(D, "D", arah=(-0.6, 0.8))
    .titik(O, "O", arah=(0.4, -1), gaya="bantu")
    .titik(T, "T", arah=(0, 1))
)
