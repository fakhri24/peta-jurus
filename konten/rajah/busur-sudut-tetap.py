"""Dua busur bercermin pada AB: tempat kedudukan titik yang melihat AB dengan sudut tetap.

Yang harus terbaca: jawabannya **dua** busur, bukan satu, dan keduanya bayangan
cermin satu sama lain terhadap AB. Melupakan busur yang kedua adalah kekeliruan
paling sering di jurus ini, dan gambar yang cuma memuat satu busur mengajarkannya.

Sudut 150 derajat dipilih, bukan 30, justru supaya busurnya bisa digambar. Keduanya
milik lingkaran yang sama berjari-jari 8: dari busur kecil ruas AB terlihat 150
derajat, dari busur besarnya 30 derajat. Busur besarnya nyaris satu lingkaran penuh
dan pusatnya jauh di seberang AB, jadi menggambarnya menghasilkan gambar yang
sebagian besar ruang kosong. Busur kecilnya pendek dan menempel pada AB.

Titik Q di busur bawah sengaja tidak di puncaknya, supaya terlihat bahwa sudutnya
tetap 150 derajat di sepanjang busur, bukan hanya di tempat yang simetris.

Keterangan 150 derajat ditaruh tangan di atas kanan P. Arah bawaan tanda_sudut
mengikuti garis bagi sudutnya, dan pada sudut selebar ini garis bagi itu menunjuk
lurus ke bawah — tepat ke ruas AB yang jaraknya cuma sekitar 30 piksel.
"""

import math

from rajah import *

KECIL = 0.85
SETENGAH, JARI = 4 * KECIL, 8 * KECIL

A, B = titik(-SETENGAH, 0), titik(SETENGAH, 0)
JAUH = math.sqrt(JARI ** 2 - SETENGAH ** 2)      # jarak pusat ke tali busur AB

O_ATAS = titik(0, -JAUH)                         # pusat busur yang di atas AB
O_BAWAH = titik(0, JAUH)

P = O_ATAS + titik(0, JARI)                      # puncak busur atas
Q = O_BAWAH + titik(JARI * math.cos(math.radians(265)),
                    JARI * math.sin(math.radians(265)))

for nama, T in (("P", P), ("Q", Q)):
    if abs(sudut(A, T, B) - 150) > 1e-6:
        raise GagalRajah(
            "sudut A%sB tergambar %.4f derajat, seharusnya 150" % (nama, sudut(A, T, B)))
    if abs(jarak(O_ATAS if T is P else O_BAWAH, T) - JARI) > 1e-9:
        raise GagalRajah("%s tidak jatuh pada busurnya" % nama)

RAJAH = (
    rajah("Sebuah ruas mendatar AB dengan A di kiri dan B di kanan. Melalui A dan B "
          "digambar dua busur lingkaran yang dangkal dan sama bentuknya: satu "
          "melengkung ke atas AB, satu lagi melengkung ke bawah, saling bercermin "
          "pada AB sehingga bersama-sama membentuk bangun seperti lensa. Titik P "
          "berada di puncak busur atas dan dihubungkan ke A dan ke B; sudut di P "
          "besarnya 150 derajat dan tampak sangat tumpul. Titik Q berada pada busur "
          "bawah, tidak di titik terendahnya melainkan agak ke kiri, dan juga "
          "dihubungkan ke A dan ke B dengan ruas putus-putus. Sudut di Q sama "
          "tumpulnya dengan sudut di P")
    .ruas(A, B)
    .busur(O_ATAS, JARI, 60, 120, gaya="tekan")
    .busur(O_BAWAH, JARI, 240, 300, gaya="tekan")
    .ruas(P, A)
    .ruas(P, B)
    .ruas(Q, A, gaya="bantu", putus=True)
    .ruas(Q, B, gaya="bantu", putus=True)
    .tanda_sudut(A, P, B)
    .tanda_sudut(A, Q, B, gaya="bantu")
    .label(P, "150°", arah=(0.8, 0.75), jauh=26, gaya="ukur")
    .titik(A, "A", arah=(-1, 0.2))
    .titik(B, "B", arah=(1, 0.2))
    .titik(P, "P", arah=(-0.7, 0.7))
    .titik(Q, "Q", arah=(-0.5, -0.9))
)
