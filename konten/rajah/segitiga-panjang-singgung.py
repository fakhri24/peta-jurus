"""Panjang singgung x, y, z — wujud geometri substitusi Ravi.

Di halaman jurus, substitusi Ravi tertulis sebagai perkara aljabar: setiap segitiga
bisa ditulis a = y+z, b = z+x, c = x+y dengan x, y, z positif. Rajah ini
menunjukkan bahwa ketiga peubah itu bukan karangan — ia panjang singgung dari tiap
titik sudut ke lingkaran dalamnya, dan dua panjang singgung dari satu titik memang
sama panjang.

Begitu itu terlihat, syarat "x, y, z > 0" berhenti terasa sebagai syarat tambahan
yang harus dihafal: ia cuma menyatakan bahwa lingkaran dalamnya ada, yang berlaku
untuk segitiga apa pun.

Titik singgungnya dihitung sebagai kaki tegak lurus dari I, bukan ditaksir — dan
berkas ini menolak dirinya sendiri kalau keenam panjang singgungnya ternyata tidak
berpasangan sama, karena di situlah seluruh isi rajah ini.

Segitiganya sengaja tak sama kaki: pada segitiga simetris, x = y jatuh kebetulan dan
siswa bisa mengira ketiganya memang selalu sama.
"""

from rajah import *

A, B, C = titik(0, 0), titik(7, 0), titik(2.2, 4.6)
I = pusat_dalam(A, B, C)
r = jari_dalam(A, B, C)

X = kaki(I, garis(B, C))
Y = kaki(I, garis(C, A))
Z = kaki(I, garis(A, B))

# Yang membuat rajah ini ada. Kalau ini tidak dijaga, gambarnya masih "hampir benar"
# dan pembacanya tidak akan pernah tahu.
for nama, p, q in (("x", jarak(A, Y), jarak(A, Z)),
                   ("y", jarak(B, Z), jarak(B, X)),
                   ("z", jarak(C, X), jarak(C, Y))):
    if abs(p - q) > 1e-9:
        raise GagalRajah(
            "kedua panjang singgung %s tidak sama: %.6f dan %.6f" % (nama, p, q))

RAJAH = (
    rajah("Segitiga ABC dengan lingkaran dalam berpusat I yang menyinggung sisi BC "
          "di X, sisi CA di Y, dan sisi AB di Z. Keenam ruas dari titik sudut ke "
          "titik singgung terdekatnya diberi keterangan panjang, dan yang berasal "
          "dari titik sudut yang sama selalu sama: dari A panjangnya x ke Y maupun "
          "ke Z, dari B panjangnya y ke Z maupun ke X, dan dari C panjangnya z ke X "
          "maupun ke Y. Akibatnya sisi BC sepanjang y ditambah z, sisi CA sepanjang "
          "z ditambah x, dan sisi AB sepanjang x ditambah y")
    .poligon(A, B, C)
    .lingkaran(I, r, gaya="bantu")
    .ukuran(A, Z, "x")
    .ukuran(Z, B, "y")
    .ukuran(B, X, "y")
    .ukuran(X, C, "z")
    .ukuran(C, Y, "z")
    .ukuran(Y, A, "x")
    .titik(A, "A", arah=(-1, -0.4))
    .titik(B, "B", arah=(1, -0.4))
    .titik(C, "C", arah=(0, 1))
    .titik(I, "I", gaya="bantu", arah=(0, -1))
    .titik(X, "X", gaya="bantu")
    .titik(Y, "Y", gaya="bantu")
    .titik(Z, "Z", gaya="bantu")
)
