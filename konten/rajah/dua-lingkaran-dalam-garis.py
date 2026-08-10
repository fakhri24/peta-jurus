"""Dua lingkaran bersinggungan dalam, dan satu garis lewat titik singgungnya.

Lingkaran kecil tidak digambar "kira-kira di dalam": pusatnya dihitung dari syarat
menyinggung dalam, yaitu berjarak R - r dari pusat lingkaran besar pada arah titik
singgungnya. Kalau meleset sedikit saja, nisbah TQ : TP yang tergambar bukan lagi
9 : 3, dan justru nisbah itu satu-satunya isi soalnya.

Titik P dan Q dihitung sebagai perpotongan kedua lingkaran dengan garis lewat T,
bukan ditaruh tangan. Arah garisnya dipilih supaya TP tepat 4 pada skala gambar.
"""

import math

from rajah import *

BESAR, KECIL = 3.0, 1.0             # sebanding 9 : 3; nisbahnya yang penting
TP = 4.0 / 3.0                      # TP = 4 pada skala soal

O2 = titik(0, 0)                    # pusat lingkaran besar
T = titik(BESAR, 0)                 # titik singgung, di kanan
O1 = titik(BESAR - KECIL, 0)        # pusat lingkaran kecil

# Titik kedua tempat garis lewat T memotong sebuah lingkaran: dari |T + t·u - O| = jari
# diperoleh t = -2 (T - O) · u. Arah u dipilih supaya t pada lingkaran kecil = TP.
ux = -TP / (2 * KECIL)
u = titik(ux, math.sqrt(1 - ux * ux))

def kedua(pusat, jari):
    return T + u * (-2 * ((T - pusat).x * u.x + (T - pusat).y * u.y))

P = kedua(O1, KECIL)
Q = kedua(O2, BESAR)

if abs(jarak(T, Q) / jarak(T, P) - BESAR / KECIL) > 1e-9:
    raise GagalRajah("nisbah TQ : TP tidak sama dengan nisbah jari-jarinya")

RAJAH = (
    rajah("Dua lingkaran bersinggungan dari dalam di titik T yang berada di sebelah "
          "kanan. Lingkaran besar berjari-jari 9 berpusat di O, dan lingkaran kecil "
          "berjari-jari 3 berada di dalamnya, menempel di T. Sebuah garis lurus "
          "ditarik dari T ke arah kiri atas; ia memotong lingkaran kecil di titik P "
          "dan meneruskan sampai memotong lingkaran besar di titik Q, dengan P "
          "terletak di antara T dan Q. Panjang TP adalah 4, sedangkan PQ belum "
          "diketahui")
    .lingkaran(O2, BESAR, gaya="bantu")
    .lingkaran(O1, KECIL, gaya="bantu")
    .ruas(T, Q, gaya="tekan")
    .ukuran(T, P, "4", jauh=19)
    .titik(T, "T", arah=(1, -0.3))
    # P duduk di puncak lingkaran kecil dengan garis TQ lewat di atasnya, jadi
    # labelnya ditaruh ke arah dalam lingkaran kecil — satu-satunya sisi yang lapang.
    .titik(P)
    .label(P, "P", arah=(-0.9, -0.5), jauh=15)
    .titik(Q, "Q", arah=(-0.8, 0.6))
    .titik(O2, "O", arah=(0, -1), gaya="bantu")
)
