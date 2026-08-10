"""Dua garis singgung dari sebuah titik yang bergerak pada garis di luar lingkaran.

Keadaan soalnya: P boleh berjalan ke mana saja sepanjang garis l, dan tiap kali
kedua titik singgungnya berpindah sehingga tali busur XY ikut berayun. Yang
ditanyakan apa yang tetap.

**Hanya satu letak P yang digambar, dan titik tetapnya tidak digambar.** Dua letak P
sekaligus akan memberikan jawabannya cuma-cuma: kedua tali busurnya berpotongan di
layar, dan mata pembaca menemukan titik tetap itu tanpa membuktikan apa pun.

Yang digambar adalah yang boleh dianggap modal: kedua jari-jari ke titik singgung
beserta tanda sikunya, sebab garis singgung tegak lurus jari-jari di titik
singgungnya adalah sifat yang sudah dimiliki siswa sebelum masuk jurus ini.

Garis l dibuat tegak lurus OP-nya bukan karena harus, melainkan supaya P mudah
dibayangkan berjalan naik-turun tanpa mengubah jarak garisnya ke pusat.
"""

from rajah import *

O, JARI = titik(0, 0), 2.0
GARIS_X = 5.0                                    # garis l: tegak, x = 5

P = titik(GARIS_X, 1.4)
BAWAH, ATAS = titik(GARIS_X, -3.0), titik(GARIS_X, 3.3)

if GARIS_X <= JARI:
    raise GagalRajah("garis l harus seluruhnya di luar lingkaran")

X, Y = singgung(P, O, JARI)

for nama, T in (("X", X), ("Y", Y)):
    if abs(jarak(O, T) - JARI) > 1e-9:
        raise GagalRajah("%s tidak berada pada lingkaran" % nama)
    # Singgung sejati: jari-jari ke titik singgung tegak lurus garis singgungnya.
    if abs(sudut(O, T, P) - 90) > 1e-9:
        raise GagalRajah(
            "P%s bukan garis singgung — sudut O%sP tergambar %.6f" % (nama, nama, sudut(O, T, P)))

RAJAH = (
    rajah("Sebuah lingkaran berpusat O di sebelah kiri, dan sebuah garis tegak "
          "bernama l di sebelah kanan yang tidak menyentuh lingkaran itu sama sekali. "
          "Titik P berada pada garis l, agak di atas ketinggian O. Dari P ditarik dua "
          "garis singgung ke lingkaran, menyentuhnya di X pada sisi atas dan Y pada "
          "sisi bawah. Ruas XY digambar tebal sebagai tali busur yang menghubungkan "
          "kedua titik singgung itu, memotong daerah antara O dan P. Jari-jari OX dan "
          "OY digambar putus-putus, dan pada X maupun Y diberi tanda siku-siku yang "
          "menyatakan bahwa jari-jari tegak lurus garis singgungnya")
    .lingkaran(O, JARI)
    .ruas(BAWAH, ATAS)
    .ruas(P, X)
    .ruas(P, Y)
    .ruas(X, Y, gaya="tekan")
    .ruas(O, X, gaya="bantu", putus=True)
    .ruas(O, Y, gaya="bantu", putus=True)
    .tanda_siku(O, X, P)
    .tanda_siku(P, Y, O)
    .label(ATAS, "l", arah=(0.9, 0.5), jauh=14)
    .titik(O, "O", arah=(-0.9, -0.5))
    .titik(P, "P", arah=(1, 0.4))
    .titik(X, "X", arah=(-0.3, 1))
    .titik(Y, "Y", arah=(-0.5, -0.9))
)
