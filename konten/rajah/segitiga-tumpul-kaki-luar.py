"""Segitiga tumpul beserta garis tinggi yang kakinya jatuh di luar sisi.

Sisi 4-13-15 dipilih justru karena sudut A-nya 112,6° — cukup tumpul supaya kaki
garis tinggi dari C terlihat jelas berada di perpanjangan BA, bukan di ruas AB.
Kalau digambar kira-kira, D gampang jatuh tepat di A atau sedikit di dalam ruas,
dan seluruh isi soalnya hilang: yang dilatih justru mengenali bahwa kaki garis
tinggi tidak selalu ada di antara kedua ujung sisinya.

Koordinatnya diturunkan dari ketiga panjang itu — A di titik asal, B pada sumbu x
— lalu diperkecil 2/3 supaya tingginya muat di layar ponsel tanpa mengubah nisbah.
"""

from rajah import *

KECIL = 2 / 3                       # 4-13-15 terlalu jangkung untuk viewBox

A = titik(0, 0)
B = titik(4 * KECIL, 0)
C = titik(-5 * KECIL, 12 * KECIL)   # dari AC = 13 dan BC = 15
D = kaki(C, garis(A, B))

RAJAH = (
    rajah("Segitiga ABC dengan sudut di A tumpul. Sisi AB mendatar, dengan A di "
          "tengah gambar dan B di sebelah kanannya, panjangnya 4. Titik C berada "
          "jauh di kiri atas, dengan CA panjangnya 13 dan CB panjangnya 15. Dari C "
          "ditarik garis tinggi ke garis AB. Karena sudut A tumpul, kakinya jatuh "
          "di titik D pada perpanjangan sisi BA di sebelah kiri A — bukan di antara "
          "A dan B. Ruas dari D ke A digambar putus-putus sebagai perpanjangan, dan "
          "sudut di D siku-siku")
    .poligon(A, B, C)
    .ruas(D, A, gaya="bantu", putus=True)
    .ruas(C, D, gaya="bantu", putus=True)
    .tanda_siku(C, D, A)
    .ukuran(A, B, "4")
    # Segitiganya sangat pipih, jadi arah "menjauhi pusat" yang dipakai ukuran()
    # justru melemparkan angka 13 ke dalam segitiga — tepat di antara CA dan CB,
    # sehingga tidak jelas lagi sisi mana yang dilabelinya. Di sini arahnya
    # ditentukan tangan: normal luar sisi CA, menjauhi B.
    .label(tengah(C, A), "13", arah=(-0.93, -0.39), jauh=16, gaya="ukur")
    .ukuran(B, C, "15")
    .titik(A, "A", arah=(0.4, -1))
    .titik(B, "B", arah=(1, -0.4))
    .titik(C, "C", arah=(0, 1))
    .titik(D, "D", arah=(-0.6, -1))
)
