"""Segitiga sama sisi dengan satu titik di dalamnya, berjarak 3, 4, dan 5 ke sudutnya.

Panjang sisinya tidak dipilih, melainkan **dihitung**: satu-satunya sisi yang memuat
titik berjarak 3, 4, 5 ke ketiga sudutnya adalah sqrt(25 + 12·sqrt3) ≈ 6,7664. Sisi
yang dibulatkan akan menggeser P sedikit, dan sudut APB yang tergambar berhenti
tepat 150° — padahal justru sudut itu yang ditanyakan soal.

Titik hasil putaran sengaja tidak digambar: menemukannya seluruh isi soal.
"""

import math

from rajah import *

SISI = math.sqrt(25 + 12 * math.sqrt(3))

A = titik(0, 0)
B = titik(SISI, 0)
C = titik(SISI / 2, SISI * math.sqrt(3) / 2)

x = (9 - 16 + SISI * SISI) / (2 * SISI)     # dari PA = 3 dan PB = 4
P = titik(x, math.sqrt(9 - x * x))

for nama, titik_sudut, panjang in (("PA", A, 3.0), ("PB", B, 4.0), ("PC", C, 5.0)):
    if abs(jarak(P, titik_sudut) - panjang) > 1e-9:
        raise GagalRajah("%s tergambar %.6f, seharusnya %g" % (nama, jarak(P, titik_sudut), panjang))

RAJAH = (
    rajah("Segitiga sama sisi ABC dengan alas AB mendatar, A di kiri bawah, B di "
          "kanan bawah, dan C di puncak atas. Sebuah titik P berada di dalam "
          "segitiga, agak ke kanan bawah dekat sisi AB. Dari P ditarik ruas "
          "putus-putus ke ketiga titik sudut: PA panjangnya 3, PB panjangnya 4, dan "
          "PC panjangnya 5")
    .poligon(A, B, C)
    .ruas(P, A, gaya="bantu", putus=True)
    .ruas(P, B, gaya="bantu", putus=True)
    .ruas(P, C, gaya="bantu", putus=True)
    .tanda_sama(A, B)
    .tanda_sama(B, C)
    .tanda_sama(C, A)
    # P nyaris menempel AB, jadi arah "menjauhi pusat" melemparkan angka 3 dan 4
    # ke atas sisi AB — di sana keduanya terbaca seolah melabeli bagian AB, bukan
    # ruas ke P. Arahnya karena itu ditentukan tangan, ke dalam segitiga.
    .label(tengah(P, A), "3", arah=(-0.30, 0.95), jauh=15, gaya="ukur")
    .label(tengah(P, B), "4", arah=(0.22, 0.98), jauh=15, gaya="ukur")
    .ukuran(P, C, "5")
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(1, -0.5))
    .titik(C, "C", arah=(0, 1))
    .titik(P)
    .label(P, "P", arah=(-0.77, 0.64), jauh=17)
)
