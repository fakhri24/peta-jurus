"""Alas tetap, luas tetap: puncaknya bebas bergerak pada satu garis sejajar.

Yang harus terbaca dari gambar ini cuma satu hal, dan ia yang membuka soalnya:
luas tetap dengan alas tetap berarti **tingginya** tetap, sehingga puncaknya
terkurung pada sebuah garis sejajar alas — bukan bebas di seluruh bidang.

Tiga letak puncak digambar sekaligus supaya kebebasan itu terlihat, dan ketiganya
sengaja tidak simetris terhadap titik tengah alas: kalau salah satunya digambar
tepat di tengah, siswa akan mengira gambar sudah menunjukkan jawabannya.

Perbandingan 16 : 6 dipakai apa adanya, jadi tinggi yang tergambar benar-benar
seperempat lebih sedikit dari alasnya.
"""

from rajah import *

KECIL = 0.35
ALAS, TINGGI = 16 * KECIL, 6 * KECIL

A, B = titik(0, 0), titik(ALAS, 0)
C = titik(0.28 * ALAS, TINGGI)
C1 = titik(0.62 * ALAS, TINGGI)
C2 = titik(0.95 * ALAS, TINGGI)

KIRI = titik(-0.12 * ALAS, TINGGI)
KANAN = titik(1.14 * ALAS, TINGGI)

RAJAH = (
    rajah("Sebuah ruas mendatar AB sepanjang 16 di bagian bawah, dengan A di kiri dan "
          "B di kanan. Di atasnya, sejajar AB dan berjarak 6 darinya, digambar sebuah "
          "garis putus-putus yang memanjang melewati kedua ujung AB. Titik C berada "
          "pada garis itu dan dihubungkan ke A dan ke B sehingga terbentuk segitiga "
          "ABC. Dua letak lain untuk C ditandai sebagai titik kosong pada garis yang "
          "sama, menunjukkan bahwa C boleh bergeser sepanjang garis itu tanpa "
          "mengubah luas segitiganya. Jarak antara kedua garis sejajar itu, yaitu "
          "tinggi segitiga, diberi keterangan 6")
    .ruas(KIRI, KANAN, gaya="bantu", putus=True)
    .poligon(A, B, C)
    .ruas(A, titik(0, TINGGI), gaya="bantu", putus=True)
    .tanda_siku(A, titik(0, TINGGI), KANAN)
    .ukuran(A, B, "16")
    .label(tengah(A, titik(0, TINGGI)), "6", arah=(-1, 0), jauh=14, gaya="ukur")
    .titik(A, "A", arah=(-1, -0.5))
    .titik(B, "B", arah=(1, -0.5))
    .titik(C, "C", arah=(-0.5, 1))
    .titik(C1, gaya="bantu")
    .titik(C2, gaya="bantu")
)
