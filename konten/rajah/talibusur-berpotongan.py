"""Dua talibusur berpotongan di dalam lingkaran, dengan tiga bagian diketahui.

Keempat ujungnya tidak dipilih dengan mata melainkan dihitung mundur dari panjang
yang diminta soal — 6, 4, dan 3 — supaya bagian keempat benar-benar tergambar 8.
Rajah kuasa titik yang digambar kira-kira justru berbahaya: siswa mengukur di
gambar, dan gambar yang meleset mengajarkan hasil kali yang salah.

Caranya: taruh P sejauh OP dari pusat. Untuk talibusur yang ujungnya sejauh t ke
arah satuan u, syarat |P + t·u| = r menyusut jadi satu persamaan linear dalam P·u,
sehingga u tertentu. Ujung yang berlawanan otomatis ikut benar asalkan hasil kali
kedua panjangnya sama dengan r^2 - OP^2 — dan itu diperiksa di sini, bukan
dipercayai.
"""

import math

from rajah import *

KECIL = 0.5                          # jari-jari 6 terlalu lebar; nisbahnya tetap
JARI = 6.0
OP = math.sqrt(12.0)                 # dipilih supaya kuasa P tepat -24 = -(6·4)

O = titik(0, 0)
P = titik(OP * KECIL, 0)


def arah(maju, mundur, naik=True):
    """Arah satuan talibusur lewat P yang ujungnya sejauh maju dan mundur."""
    if abs(maju * mundur - (JARI * JARI - OP * OP)) > 1e-9:
        raise GagalRajah(
            "hasil kali %g × %g tidak sama dengan kuasa titiknya — kedua ujungnya "
            "tidak mungkin sama-sama jatuh di lingkaran" % (maju, mundur)
        )
    x = (JARI * JARI - OP * OP - maju * maju) / (2 * maju * OP)
    y = math.sqrt(1 - x * x)
    return titik(x, y if naik else -y)


u1 = arah(6.0, 4.0)                  # PA = 6, PB = 4
u2 = arah(3.0, 8.0)                  # PC = 3, PD = 8

A = P + u1 * (6.0 * KECIL)
B = P - u1 * (4.0 * KECIL)
C = P + u2 * (3.0 * KECIL)
D = P - u2 * (8.0 * KECIL)

RAJAH = (
    rajah("Sebuah lingkaran dengan dua talibusur yang berpotongan di titik P di "
          "dalamnya, di sebelah kanan pusat. Talibusur pertama menghubungkan A di "
          "atas dengan B di kanan bawah: jarak dari P ke A adalah 6 dan dari P ke B "
          "adalah 4. Talibusur kedua menghubungkan C di kanan atas dengan D di kiri "
          "bawah: jarak dari P ke C adalah 3, sedangkan jarak dari P ke D belum "
          "diketahui dan ditandai tanda tanya")
    .lingkaran(O, JARI * KECIL, gaya="bantu")
    .ruas(A, B)
    .ruas(C, D)
    .ukuran(P, A, "6")
    .ukuran(P, B, "4")
    .ukuran(P, C, "3")
    .ukuran(P, D, "?")
    .titik(A, "A", arah=(-0.3, 1))
    .titik(B, "B", arah=(0.5, -1))
    .titik(C, "C", arah=(1, 0.3))
    .titik(D, "D", arah=(-0.6, -0.9))
    .titik(P, "P", arah=(1, -0.3))
)
