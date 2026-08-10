"""Tiga tali busur lewat satu titik tetap di dalam lingkaran, beserta titik tengahnya.

Yang harus terbaca: tali busurnya boleh diputar sesuka hati asal tetap lewat A, dan
tiap kali titik tengahnya berpindah. Pertanyaannya ke mana.

**Lingkaran berdiameter OA sengaja tidak digambar**, sebab bangun itu jawabannya.
Yang digambar cuma tiga titik tengah, dan menaruh tiga titik memang menggoda mata
untuk menghubungkannya — itu justru langkah pertama yang benar. Ruas OM juga tidak
digambar: bahwa OM tegak lurus tali busurnya adalah kunci buktinya, dan
menggambarnya sama saja dengan menuliskan buktinya di gambar.

A ditaruh jelas di luar pusat. Kalau A jatuh di O, ketiga tali busur menjadi
diameter dan ketiga titik tengahnya menumpuk di satu titik — kasus merosot yang
membuat soalnya terlihat kosong.

Ketiga arahnya juga tidak boleh dipilih sembarangan, dan alasannya justru jawaban
soalnya: M adalah kaki tegak lurus dari O ke tali busurnya, jadi saat tali busurnya
berputar M mengelilingi lingkaran berdiameter OA. Tali busur yang searah OA
menjatuhkan M tepat di O; yang tegak lurus OA menjatuhkan M tepat di A. Dua-duanya
menghasilkan gambar yang terbaca sebagai kebetulan. Ketiga arah di bawah karena itu
dijaga menyudut 30 sampai 125 derajat terhadap OA — tersebar, tetapi tidak berjarak
sama supaya tidak ada kesan keteraturan sudutnya yang menentukan.
"""

import math

from rajah import *

O, JARI = titik(0, 0), 3.2
A = titik(2.0, 0.9)                              # titik tetap, jelas bukan pusat

if jarak(O, A) >= JARI:
    raise GagalRajah("A harus di dalam lingkaran")

ARAH_OA = math.degrees(math.atan2(A.y, A.x))

tali, tengah_tali = [], []
for derajat in (55, 85, 145):
    if not 25 <= (derajat - ARAH_OA) % 180 <= 155:
        raise GagalRajah(
            "tali busur %g derajat terlalu searah atau terlalu tegak lurus OA — "
            "titik tengahnya jatuh nyaris tepat di O atau di A" % derajat)
    u = titik(math.cos(math.radians(derajat)), math.sin(math.radians(derajat)))
    # Akar-akar |A + t u| = JARI. Jumlah akarnya -2(A.u), jadi titik tengahnya
    # jatuh di t = -(A.u) — sekaligus kaki tegak lurus dari O ke tali busurnya.
    au = A.x * u.x + A.y * u.y
    akar = math.sqrt(au ** 2 - (A.x ** 2 + A.y ** 2) + JARI ** 2)
    P, Q = A + u * (-au + akar), A + u * (-au - akar)
    M = A + u * (-au)
    for T in (P, Q):
        if abs(jarak(O, T) - JARI) > 1e-9:
            raise GagalRajah("ujung tali busur meleset dari lingkaran")
    if jarak(tengah(P, Q), M) > 1e-9:
        raise GagalRajah("M bukan titik tengah tali busurnya")
    tali.append((P, Q))
    tengah_tali.append(M)

# Yang membuat rajah ini ada: ketiganya memang jatuh pada satu lingkaran — yang
# berdiameter OA. Kalau ini meleset, gambarnya mengajarkan tempat kedudukan yang salah.
pusat_jawaban, jari_jawaban = tengah(O, A), jarak(O, A) / 2
for M in tengah_tali:
    if abs(jarak(pusat_jawaban, M) - jari_jawaban) > 1e-9:
        raise GagalRajah("titik tengah meleset dari lingkaran berdiameter OA")

RAJAH = (
    rajah("Sebuah lingkaran berpusat O. Di dalamnya ada titik tetap A yang letaknya "
          "jelas bukan di pusat, melainkan di kanan atas O. Tiga tali busur digambar, "
          "ketiganya melalui A dengan arah yang berbeda-beda, sehingga A menjadi satu-"
          "satunya titik yang dilalui ketiganya. Titik tengah masing-masing tali busur "
          "ditandai dan diberi nama M, N, dan K. Ketiga titik tengah itu tidak segaris "
          "dan letaknya berkumpul di daerah antara O dan A")
    .lingkaran(O, JARI)
    .ruas(*tali[0], gaya="bantu")
    .ruas(*tali[1], gaya="bantu")
    .ruas(*tali[2], gaya="bantu")
    .titik(O, "O", arah=(-0.9, -0.5))
    .titik(A, "A", arah=(0.9, 0.5))
    .titik(tengah_tali[0], "M", gaya="tekan", arah=(-0.4, -1))
    .titik(tengah_tali[1], "N", gaya="tekan", arah=(1, -0.4))
    .titik(tengah_tali[2], "K", gaya="tekan", arah=(-0.6, 0.9))
)
