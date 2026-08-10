"""Trapesium, kedua diagonalnya, dan ruas lewat titik potongnya sejajar alas.

Nisbah sisi sejajarnya 30 : 15 dipakai apa adanya sebagai lebar bawah dan atas,
supaya letak P di gambar benar-benar membagi diagonalnya 2 : 1 dan ruas MN
tergambar sepanjang 20 pada skala soal — bukan sekadar "kira-kira di tengah".

M dan N dihitung sebagai perpotongan kaki trapesium dengan garis mendatar setinggi
P, bukan ditaruh tangan. Kalau meleset, MP dan PN berhenti sama panjang — padahal
justru itu yang membuat MN jadi rata-rata harmonik.
"""

from rajah import *

BAWAH, ATAS, TINGGI = 4.5, 2.25, 3.0        # sebanding 30 : 15

A, B = titik(0, 0), titik(BAWAH, 0)
D = titik(1.0, TINGGI)
C = D + titik(ATAS, 0)

P = potong(garis(A, C), garis(B, D))
mendatar = garis(P, P + titik(1, 0))
M = potong(garis(A, D), mendatar)
N = potong(garis(B, C), mendatar)

if abs(jarak(M, P) - jarak(P, N)) > 1e-9:
    raise GagalRajah("P seharusnya titik tengah MN")

RAJAH = (
    rajah("Trapesium ABCD dengan sisi AB mendatar di bawah sepanjang 30, dan sisi DC "
          "mendatar di atas sepanjang 15, keduanya sejajar. A di kiri bawah, B di "
          "kanan bawah, C di kanan atas, D di kiri atas. Kedua diagonalnya, AC dan "
          "BD, digambar dan berpotongan di titik P. Melalui P ditarik ruas mendatar "
          "sejajar AB; ia memotong kaki kiri AD di titik M dan kaki kanan BC di titik "
          "N, sehingga P menjadi titik tengah MN")
    .poligon(A, B, C, D)
    .ruas(A, C, gaya="bantu")
    .ruas(B, D, gaya="bantu")
    .ruas(M, N, gaya="tekan")
    .ukuran(A, B, "30")
    .ukuran(D, C, "15")
    .titik(A, "A", arah=(-1, -0.6))
    .titik(B, "B", arah=(1, -0.6))
    .titik(C, "C", arah=(1, 0.6))
    .titik(D, "D", arah=(-1, 0.6))
    .titik(M, "M", arah=(-1, 0.3))
    .titik(N, "N", arah=(1, 0.3))
    .titik(P)
    .label(P, "P", arah=(0.2, 1), jauh=16)
)
