"""Titik di dalam segitiga, dihubungkan ke ketiga titik sudutnya.

Keadaan soalnya saja: yang dicari nilai terkecil PA + PB + PC, dan P masih bebas.

**Titik Fermat sengaja tidak digambar.** Letaknya — yang melihat ketiga sisi dengan
sudut 120 derajat — adalah seluruh jawaban soalnya. P di sini karena itu ditaruh di
tempat yang jelas bukan titik itu, sedikit ke kiri bawah dari titik berat, supaya
ketiga sudut di P terlihat nyata berbeda dan tidak ada yang bisa diukur dari gambar.

Ketiga sudut segitiganya dijaga di bawah 120 derajat, sebab di luar syarat itu
jawabannya berpindah ke titik sudut yang tumpul dan rajah ini akan menggambarkan
soal yang lain.
"""

from rajah import *

A, B, C = titik(0, 0), titik(6.4, 0), titik(1.9, 4.8)
P = titik(2.4, 1.15)

for nama, x, y, z in (("A", B, A, C), ("B", C, B, A), ("C", A, C, B)):
    if sudut(x, y, z) >= 120:
        raise GagalRajah(
            "sudut %s tergambar %.2f derajat — di atas 120 soalnya berubah"
            % (nama, sudut(x, y, z)))

# Titik di dalam segitiga melihat ketiga sisinya dengan jumlah sudut penuh; titik
# di luar tidak. Lebih murah daripada tiga uji sisi, dan pesannya lebih jelas.
keliling_sudut = sudut(A, P, B) + sudut(B, P, C) + sudut(C, P, A)
if abs(keliling_sudut - 360) > 1e-6:
    raise GagalRajah("P tidak berada di dalam segitiga")

RAJAH = (
    rajah("Segitiga ABC dengan A di kiri bawah, B di kanan bawah, dan C di atas agak "
          "ke kiri; ketiga sudutnya lancip. Sebuah titik P berada di dalam segitiga "
          "itu, di bawah dan sedikit ke kiri dari pusatnya, dan dihubungkan dengan "
          "ruas tebal ke ketiga titik sudut sehingga terbentuk ruas PA, PB, dan PC. "
          "Ketiga sudut di P jelas tidak sama besar")
    .poligon(A, B, C)
    .ruas(P, A, gaya="tekan")
    .ruas(P, B, gaya="tekan")
    .ruas(P, C, gaya="tekan")
    .titik(A, "A", arah=(-1, -0.4))
    .titik(B, "B", arah=(1, -0.4))
    .titik(C, "C", arah=(-0.2, 1))
    .titik(P, "P", arah=(0.2, -1))
)
