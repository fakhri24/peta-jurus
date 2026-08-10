"""Kubus dengan diagonal ruang AG dan segitiga BDE yang ditembusnya.

Titik tembusnya dihitung, bukan ditaruh di tengah-tengah: AG memotong bidang BDE
tepat pada sepertiga panjangnya dari A. Menggambarnya di tengah akan menyarankan
kesimpulan yang salah tentang perbandingan yang justru sedang dipelajari.
"""

from rajah import *

R = 4.2

A, B, C, D = (ruang(0, 0, 0), ruang(R, 0, 0), ruang(R, R, 0), ruang(0, R, 0))
E, F, G, H = (ruang(0, 0, R), ruang(R, 0, R), ruang(R, R, R), ruang(0, R, R))

# Bidang BDE adalah x + y + z = R, jadi AG menembusnya di sepertiga jalan.
P = ruang(R / 3, R / 3, R / 3)

RAJAH = (
    rajah("Kubus ABCD titik EFGH dengan alas ABCD di bawah dan tutup EFGH di atas, "
          "E tepat di atas A. Diagonal ruang dari A ke G digambar tebal, menembus "
          "segitiga BDE di titik P yang terletak sepertiga jalan dari A. Segitiga "
          "BDE diarsir. Rusuk yang tersembunyi di belakang digambar putus-putus")
    .arsir(B, D, E)
    .garis_patah(A, B, C)
    .ruas(A, D, putus=True)
    .ruas(D, C, putus=True)
    .poligon(E, F, G, H)
    .ruas(A, E)
    .ruas(B, F)
    .ruas(C, G)
    .ruas(D, H, putus=True)
    .ruas(B, D, gaya="bantu")
    .ruas(D, E, gaya="bantu")
    .ruas(B, E, gaya="bantu")
    .ruas(A, G, gaya="tekan")
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(1, -0.5))
    .titik(C, "C", arah=(1, -0.3))
    # Label D dan F digeser menjauhi diagonal AG, yang lewat persis di dekat
    # keduanya pada proyeksi ini.
    .titik(D, "D", arah=(-1, -0.6))
    .titik(E, "E", arah=(-1, 0.4))
    .titik(F, "F", arah=(0.9, -0.9))
    .titik(G, "G", arah=(1, 0.4))
    .titik(H, "H", arah=(-0.4, 1))
    .titik(P, "P", arah=(0.9, -0.6), gaya="tekan")
)
