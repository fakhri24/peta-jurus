"""Dua titik di sisi yang sama dari sebuah garis, dan satu titik singgah di garis itu.

Yang digambar hanya keadaan soalnya — cerminan A belum ada. Itu disengaja: seluruh
isi jurus ini adalah menemukan bahwa mencerminkan salah satu titik mengubah soal
jarak jadi soal garis lurus, dan menggambar cerminannya sama saja dengan menuliskan
jawabannya di gambar.

Titik P digambar sengaja **tidak** di tempat yang terbaik (yang benar di x = 8/3
dari kaki A), supaya lintasan yang tergambar terlihat patah — bukan hampir lurus.

Perbandingannya dijaga 2 : 4 : 8 meski koordinatnya diperkecil, jadi angka pada
gambar tetap boleh dipercaya.
"""

from rajah import *

KECIL = 0.7

A0 = titik(0, 0)                     # kaki tegak lurus dari A
B0 = titik(8 * KECIL, 0)             # kaki tegak lurus dari B
A = titik(0, 2 * KECIL)
B = titik(8 * KECIL, 4 * KECIL)
P = titik(5 * KECIL, 0)              # sengaja bukan titik terbaiknya
KIRI = titik(-1.6 * KECIL, 0)
KANAN = titik(9.8 * KECIL, 0)

RAJAH = (
    rajah("Sebuah garis lurus mendatar bernama l. Di atasnya ada titik A di kiri, "
          "berjarak 2 dari garis itu, dan titik B di kanan, berjarak 4 dari garis "
          "itu. Kedua kaki tegak lurusnya pada garis l berjarak 8 satu sama lain. "
          "Sebuah titik P berada pada garis l di antara kedua kaki itu, dan lintasan "
          "patah dari A ke P lalu ke B digambar putus-putus")
    .ruas(KIRI, KANAN, gaya="bantu")
    .ruas(A, A0, gaya="bantu", putus=True)
    .ruas(B, B0, gaya="bantu", putus=True)
    .tanda_siku(A, A0, B0)
    .tanda_siku(B, B0, A0)
    .garis_patah(A, P, B, gaya="tekan", putus=True)
    .ukuran(A0, A, "2")
    .ukuran(B, B0, "4")
    .label(tengah(A0, B0), "8", arah=(0, -1), jauh=16, gaya="ukur")
    .label(KANAN, "l", arah=(0, 1), jauh=14)
    .titik(A, "A", arah=(-0.8, 0.6))
    .titik(B, "B", arah=(0.8, 0.6))
    .titik(P, "P", arah=(0.3, -1))
)
