"""Dari satu titik luar: sebuah garis singgung, dan sebuah garis potong lewat pusat.

Titik singgung T dihitung dengan singgung(), bukan ditaruh kira-kira — sudut siku
antara OT dan PT adalah satu-satunya alasan mengapa PT^2 = PA · PB berlaku, dan
rajah yang sudutnya meleset menghapus alasan itu dari layar.

Angkanya mengikuti soal: PA = 8, jari-jari 5, sehingga OP = 13 dan PT = 12 —
segitiga siku-siku 5-12-13, yang membuat gambarnya sekaligus jadi pemeriksa.
"""

from rajah import *

KECIL = 0.4                          # OP = 13 terlalu lebar; nisbahnya tetap
JARI = 5.0

O = titik(0, 0)
P = titik(13.0 * KECIL, 0)
A = titik(JARI * KECIL, 0)           # ujung terdekat, PA = 8
B = titik(-JARI * KECIL, 0)          # ujung terjauh, PB = 18
T, _ = singgung(P, O, JARI * KECIL)

RAJAH = (
    rajah("Sebuah lingkaran berpusat O dengan titik P di luarnya, di sebelah kanan. "
          "Dari P ditarik garis singgung yang menyentuh lingkaran di titik T di "
          "kiri atas, dan jari-jari OT digambar putus-putus tegak lurus terhadap "
          "garis singgung itu. Dari P juga ditarik garis potong mendatar yang "
          "melewati pusat lingkaran, menembusnya di titik A yang lebih dekat ke P "
          "dan titik B di seberangnya, sehingga AB adalah garis tengah. Jarak dari "
          "P ke A adalah 8, dan panjang garis singgung PT adalah 12")
    .lingkaran(O, JARI * KECIL, gaya="bantu")
    .ruas(B, P)
    .ruas(P, T)
    .ruas(O, T, gaya="bantu", putus=True)
    .tanda_siku(P, T, O)
    .ukuran(P, A, "8")
    .ukuran(P, T, "12")
    .titik(O, "O", arah=(-0.3, -1))
    .titik(P, "P", arah=(1, -0.3))
    .titik(A, "A", arah=(0.3, -1))
    .titik(B, "B", arah=(-1, -0.3))
    .titik(T, "T", arah=(-0.6, 0.8))
)
