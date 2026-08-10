"""Segitiga dipotong satu garis lurus: dua sisi, satu perpanjangan.

Inilah bentuk yang membedakan Menelaus dari Ceva, dan satu-satunya hal yang harus
terbaca dari gambar ini: titik potong ketiganya tidak mungkin ketiganya berada di
dalam sisi. Sebuah garis lurus memotong dua sisi segitiga dan **perpanjangan** sisi
ketiga — di sini D jatuh di luar BC, di seberang C.

D tidak ditaruh dengan tangan melainkan dihitung sebagai perpotongan garis FE
dengan garis BC. Perbandingan AF : FB = 2 : 3 dan AE : EC = 3 : 1 yang dipilih;
BD : DC = 9 : 2 keluar sendiri, dan justru itu yang ditanyakan soal.
"""

from rajah import *

A, B, C = titik(1.3, 4.7), titik(0, 0), titik(6, 0)

F = bagi(A, B, 2 / 5)               # AF : FB = 2 : 3
E = bagi(A, C, 3 / 4)               # AE : EC = 3 : 1
D = potong(garis(F, E), garis(B, C))

if not (D.x > C.x):
    raise GagalRajah("D seharusnya jatuh di perpanjangan BC melewati C")

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, "
          "dan puncak A di atas agak ke kiri. Sebuah garis lurus memotong sisi AB di "
          "titik F, memotong sisi AC di titik E, lalu diteruskan sampai memotong "
          "perpanjangan alas BC di titik D yang berada di luar segitiga, di sebelah "
          "kanan C. Bagian garis dari E sampai D dan bagian alas dari C sampai D "
          "digambar putus-putus karena keduanya di luar segitiga")
    .poligon(A, B, C)
    .ruas(F, E, gaya="tekan")
    .ruas(E, D, gaya="tekan", putus=True)
    .ruas(C, D, gaya="bantu", putus=True)
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(-0.2, -1))
    .titik(D, "D", arah=(1, -0.4))
    .titik(E, "E", arah=(0.3, 1))
    .titik(F, "F", arah=(-1, 0.2))
)
