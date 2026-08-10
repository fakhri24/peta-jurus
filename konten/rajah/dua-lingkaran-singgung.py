"""Dua lingkaran bersinggungan luar dengan garis singgung persekutuannya.

Kedua pusat diletakkan setinggi jari-jarinya masing-masing di atas satu garis
mendatar, jadi garis itu otomatis menyinggung keduanya. Jarak mendatarnya lalu
dihitung dari syarat bersinggungan luar, d = r1 + r2 — dan panjang ruas singgung
di gambar keluar benar dengan sendirinya.
"""

import math

from rajah import *

KECIL = 0.6
R1, R2 = 4 * KECIL, 9 * KECIL

# Jarak pusat harus R1 + R2; selisih tingginya sudah R2 - R1, jadi sisanya mendatar.
d = R1 + R2
mendatar = math.sqrt(d * d - (R2 - R1) ** 2)

O1, O2 = titik(0, R1), titik(mendatar, R2)
X, Y = titik(0, 0), titik(mendatar, 0)          # titik singgung pada garis
S = O1 + (O2 - O1).satuan() * R1                # titik singgung kedua lingkaran

RAJAH = (
    rajah("Dua lingkaran yang bersinggungan dari luar, yang kecil di kiri dan yang "
          "besar di kanan, keduanya menyinggung satu garis mendatar di bawahnya. "
          "Titik singgung pada garis itu adalah X untuk lingkaran kecil dan Y untuk "
          "lingkaran besar. Kedua pusat dihubungkan oleh ruas yang melewati titik "
          "singgung kedua lingkaran, dan tiap jari-jari ke garis mendatar tegak "
          "lurus terhadapnya")
    .lingkaran(O1, R1)
    .lingkaran(O2, R2)
    .ruas(titik(-1.2, 0), titik(mendatar + 1.2, 0), gaya="bantu")
    .ruas(X, Y, gaya="tekan")
    .ruas(O1, X, gaya="bantu", putus=True)
    .ruas(O2, Y, gaya="bantu", putus=True)
    .ruas(O1, O2, gaya="bantu")
    .tanda_siku(O1, X, Y)
    .tanda_siku(X, Y, O2)
    .titik(O1, "P", arah=(-1, 0.3), gaya="bantu")
    .titik(O2, "Q", arah=(1, 0.3), gaya="bantu")
    .titik(X, "X", arah=(-0.6, -1))
    .titik(Y, "Y", arah=(0.6, -1))
    .titik(S, "S", arah=(0.3, 1), gaya="bantu")
)
