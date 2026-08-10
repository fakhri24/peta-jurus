"""Segitiga siku-siku 6-8-10 beserta lingkaran dalam dan lingkaran luarnya.

Kedua pusat dihitung — pusat_dalam() dan pusat_luar() — bukan ditaruh kira-kira.
Yang harus terbaca dari gambar ini justru bahwa keduanya **titik yang berbeda**:
menukar pusat dalam dengan pusat luar adalah kekeliruan paling sering di seluruh
jurus ini, dan rajah yang menaruh keduanya berdempetan malah memupuknya.

Sekalian ia memperlihatkan satu sifat yang tidak disebut soal: pada segitiga
siku-siku, pusat lingkaran luar jatuh tepat di titik tengah sisi miring. Itu keluar
sendiri dari perhitungan, bukan dipasang tangan.

Koordinatnya diperkecil 0,7 supaya lingkaran luar berjari-jari 5 muat di layar
ponsel; nisbahnya tetap, jadi angka pada gambar tetap boleh dipercaya.
"""

from rajah import *

KECIL = 0.7

A = titik(0, 0)
B = titik(6 * KECIL, 0)
C = titik(0, 8 * KECIL)

I = pusat_dalam(A, B, C)
O = pusat_luar(A, B, C)

if jarak(O, tengah(B, C)) > 1e-9:
    raise GagalRajah("pusat luar segitiga siku-siku harus di titik tengah sisi miring")

RAJAH = (
    rajah("Segitiga ABC siku-siku di A, dengan A di kiri bawah, B di kanan pada "
          "garis mendatar, dan C di atas A pada garis tegak. Sisi AB panjangnya 6, "
          "sisi AC panjangnya 8, dan sisi miring BC panjangnya 10. Lingkaran dalam "
          "berpusat I menyinggung ketiga sisinya dari dalam. Lingkaran luar berpusat "
          "O melalui ketiga titik sudutnya, dan O terletak tepat di titik tengah sisi "
          "miring BC. Ruas putus-putus menghubungkan I dengan O")
    .lingkaran(O, jari_luar(A, B, C), gaya="bantu")
    .lingkaran(I, jari_dalam(A, B, C), gaya="bantu")
    .poligon(A, B, C)
    .tanda_siku(B, A, C)
    .ruas(I, O, gaya="tekan", putus=True)
    .ukuran(A, B, "6")
    .ukuran(C, A, "8")
    # Titik tengah BC justru tempat O berdiri, jadi ukuran() menimpakan angka 10
    # tepat di atas labelnya. Digeser ke sepertiga sisi, arah normal luar.
    .label(bagi(B, C, 0.3), "10", arah=(0.8, 0.6), jauh=15, gaya="ukur")
    .titik(A, "A", arah=(-0.8, -0.8))
    .titik(B, "B", arah=(1, -0.4))
    .titik(C, "C", arah=(-0.4, 1))
    .titik(I, "I", arah=(-0.9, 0.5), gaya="bantu")
    .titik(O, "O", arah=(1, 0.5), gaya="bantu")
)
