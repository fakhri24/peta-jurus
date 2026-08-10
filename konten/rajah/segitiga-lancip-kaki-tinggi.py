"""Segitiga lancip beserta garis tinggi dari A, untuk menurunkan aturan kosinus.

Sisinya diberi nama huruf, bukan angka: rajah ini menemani sebuah pembuktian, dan
angka di gambar akan membuat siswa mengira buktinya cuma berlaku untuk satu
segitiga. Yang perlu terbaca hanya letak D — di antara B dan C — karena persis di
situ pembuktiannya bercabang untuk kasus tumpul.

Sisi 5-6-7 dipilih karena ketiga sudutnya lancip dengan selisih yang cukup lebar
(44°, 57°, 78°), jadi tidak ada satu pun yang terlihat seperti siku-siku kebetulan.
"""

import math

from rajah import *

a, b, c = 7.0, 6.0, 5.0             # a = BC, b = CA, c = AB

B, C = titik(0, 0), titik(a, 0)
x = (c * c - b * b + a * a) / (2 * a)
A = titik(x, math.sqrt(c * c - x * x))
D = kaki(A, garis(B, C))

RAJAH = (
    rajah("Segitiga ABC dengan ketiga sudutnya lancip. Sisi BC mendatar sebagai "
          "alas, dengan B di kiri bawah dan C di kanan bawah; panjangnya diberi "
          "nama a. Sisi CA di sebelah kanan diberi nama b, dan sisi AB di sebelah "
          "kiri diberi nama c. Puncak A berada di atas, agak ke kiri. Dari A "
          "ditarik garis tinggi putus-putus tegak lurus alas, memotongnya di titik "
          "D yang terletak di antara B dan C. Sudut di titik sudut C ditandai busur "
          "kecil, karena sudut itulah yang muncul dalam rumusnya")
    .poligon(A, B, C)
    .ruas(A, D, gaya="bantu", putus=True)
    .tanda_siku(A, D, C)
    .tanda_sudut(A, C, B)
    .label(tengah(B, C), "a", arah=(0, -1), jauh=16)
    .label(tengah(C, A), "b", arah=(0.70, 0.71), jauh=16)
    .label(tengah(A, B), "c", arah=(-0.84, 0.54), jauh=16)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.4))
    .titik(C, "C", arah=(1, -0.4))
    .titik(D, "D", arah=(0, -1))
)
