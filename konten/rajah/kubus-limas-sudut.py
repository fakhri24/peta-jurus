"""Kubus dengan limas di salah satu pojoknya: A, B, D, E.

Ketiga rusuk yang bertemu di A saling tegak lurus, dan justru itu yang membuat
volumenya bisa dihitung tanpa mencari tinggi apa pun. Sisi miring limasnya,
segitiga BDE, diarsir supaya terlihat sebagai satu bidang datar — di gambar
ruang, bidang miring paling mudah luput.
"""

from rajah import *

R = 4.2                            # panjang rusuk dalam satuan gambar

A, B, C, D = (ruang(0, 0, 0), ruang(R, 0, 0), ruang(R, R, 0), ruang(0, R, 0))
E, F, G, H = (ruang(0, 0, R), ruang(R, 0, R), ruang(R, R, R), ruang(0, R, R))

RAJAH = (
    rajah("Kubus ABCD titik EFGH dengan alas ABCD di bawah dan tutup EFGH di atas, "
          "E tepat di atas A. Rusuk yang tersembunyi di belakang, yaitu yang "
          "melalui titik D, digambar putus-putus. Segitiga BDE diarsir, membentuk "
          "bidang miring limas yang berpojok di A dengan ketiga rusuk AB, AD, dan "
          "AE saling tegak lurus")
    .arsir(B, D, E, gaya="tekan")
    .garis_patah(A, B, C)          # rusuk alas yang terlihat
    .ruas(A, D, putus=True)
    .ruas(D, C, putus=True)
    .poligon(E, F, G, H)           # rusuk tutup
    .ruas(A, E)
    .ruas(B, F)
    .ruas(C, G)
    .ruas(D, H, putus=True)
    .ruas(B, D, gaya="tekan")
    .ruas(D, E, gaya="tekan")
    .ruas(B, E, gaya="tekan")
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(1, -0.5))
    .titik(C, "C", arah=(1, -0.3))
    .titik(D, "D", arah=(-1, 0.3))
    .titik(E, "E", arah=(-1, 0.4))
    .titik(F, "F", arah=(1, -0.2))
    .titik(G, "G", arah=(1, 0.4))
    .titik(H, "H", arah=(-0.4, 1))
)
