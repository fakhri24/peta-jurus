"""Titik tetap di dalam sudut, dan satu segitiga yang kedua titik lainnya bebas.

Yang harus terbaca: A boleh di mana saja pada satu sinar, B boleh di mana saja pada
sinar lainnya, dan P tidak ikut bergerak. Jadi yang dicari nilai terkecilnya adalah
keliling segitiga yang dua titik sudutnya bebas berjalan.

**Kedua cerminan P sengaja tidak digambar.** Menemukan bahwa mencerminkan P pada
kedua sinar mengubah keliling menjadi satu ruas lurus adalah seluruh isi soalnya;
menggambar P1 dan P2 sama saja dengan menuliskan jawabannya di gambar.

Letak A dan B sengaja bukan yang terbaik — yang terbaik ada di OA = 9,16 dan
OB = 8,83 (dihitung dari perpotongan P1P2 dengan kedua sinar), jadi 7,5 dan 10,5
membuat lintasannya terlihat jelas patah, bukan hampir lurus.

Ruas OP tidak digambar meski panjangnya diketahui: pada sudut sesempit 30 derajat,
garis ketiga di dalam bajinya menempel pada keterangan 30 derajat itu sendiri.
Panjang OP disebut di teks soalnya.
"""

from rajah import *

KECIL = 0.5
SUDUT = 30

O = titik(0, 0)
UJUNG_X = titik(11.6 * KECIL, 0)
UJUNG_Y = putar(UJUNG_X, O, SUDUT)

P = putar(titik(10 * KECIL, 0), O, 11)          # di dalam baji, tidak di garis baginya
A = titik(7.5 * KECIL, 0)
B = putar(titik(10.5 * KECIL, 0), O, SUDUT)

if not (0 < sudut(UJUNG_X, O, P) < SUDUT):
    raise GagalRajah("P harus berada di dalam sudut XOY")

RAJAH = (
    rajah("Dua sinar yang keduanya berpangkal di titik O dan mengapit sudut 30 "
          "derajat: sinar OX mendatar ke kanan, dan sinar OY miring ke atas. Sebuah "
          "titik P berada di dalam sudut itu, agak jauh dari O dan lebih dekat ke "
          "sinar OX daripada ke sinar OY. Titik A terletak pada sinar OX, lebih dekat "
          "ke O daripada P, dan titik B pada sinar OY, sedikit lebih jauh dari O "
          "daripada P. Ketiganya dihubungkan menjadi segitiga PAB, yang sisi-sisinya "
          "digambar tebal, dan segitiga itu terlihat jelas tidak simetris")
    .ruas(O, UJUNG_X)
    .ruas(O, UJUNG_Y)
    .tanda_sudut(UJUNG_X, O, UJUNG_Y, teks="30°", jauh=56)
    .poligon(P, A, B, gaya="tekan")
    .label(UJUNG_X, "X", arah=(0.6, -0.8))
    .label(UJUNG_Y, "Y", arah=(0.4, 0.9))
    .titik(O, "O", arah=(-1, -0.3))
    .titik(P, "P", arah=(1, 0.4))
    .titik(A, "A", arah=(-0.2, -1))
    .titik(B, "B", arah=(-0.8, 0.7))
)
