"""Segitiga sama sisi pada lingkaran luarnya, dengan satu titik di busur BC.

Letak P dihitung mundur dari PB = 2: sudut pusat busur BP diambil dari panjang
talibusurnya, bukan dikira-kira. Sisi segitiganya pun tidak dipilih melainkan
keluar dari PB = 2 dan PC = 5 lewat aturan kosinus pada sudut BPC = 120°,
menghasilkan sisi sqrt(39) dan jari-jari sqrt(13).

Kalau P ditaruh sembarang, ketiga panjangnya tidak lagi memenuhi PA = PB + PC —
dan justru kesamaan itu yang harus terlihat masuk akal saat siswa mengukur gambar
dengan mata.
"""

import math

from rajah import *

PB, PC = 2.0, 5.0

SISI = math.sqrt(PB * PB + PC * PC + PB * PC)      # aturan kosinus, sudut BPC = 120°
JARI = SISI / math.sqrt(3)

def di(derajat):
    d = math.radians(derajat)
    return titik(JARI * math.cos(d), JARI * math.sin(d))

O = titik(0, 0)
A, B, C = di(90), di(210), di(330)

# Sudut pusat busur BP, dari panjang talibusurnya: PB = 2·R·sin(busur/2)
busur = 2 * math.degrees(math.asin(PB / (2 * JARI)))
P = di(210 + busur)

if abs(jarak(P, A) - (PB + PC)) > 1e-9:
    raise GagalRajah("PA tergambar %.6f, seharusnya PB + PC = %g" % (jarak(P, A), PB + PC))

RAJAH = (
    rajah("Segitiga sama sisi ABC dengan ketiga titik sudutnya pada sebuah "
          "lingkaran: A di puncak atas, B di kiri bawah, C di kanan bawah. Titik P "
          "berada pada busur BC yang tidak memuat A, lebih dekat ke B daripada ke C. "
          "Dari P ditarik ruas ke ketiga titik sudut. Ruas PB panjangnya 2, ruas PC "
          "panjangnya 5, dan ruas PA — yang memotong sisi BC — panjangnya belum "
          "diketahui dan ditandai tanda tanya")
    .lingkaran(O, JARI, gaya="bantu")
    .poligon(A, B, C)
    .tanda_sama(A, B)
    .tanda_sama(B, C)
    .tanda_sama(C, A)
    .ruas(P, B, gaya="tekan")
    .ruas(P, C, gaya="tekan")
    .ruas(P, A, gaya="tekan", putus=True)
    .ukuran(P, B, "2")
    .ukuran(P, C, "5")
    .label(bagi(P, A, 0.72), "?", arah=(1, 0.2), jauh=15, gaya="ukur")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, 0.2))
    .titik(C, "C", arah=(1, 0.2))
    .titik(P, "P", arah=(-0.6, -0.9))
)
