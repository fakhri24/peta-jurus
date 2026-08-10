"""Lingkaran sembilan titik: tiga titik tengah sisi, tiga kaki garis tinggi, tiga
titik tengah antara H dan titik sudut.

Kesembilan titiknya dihitung, dan berkas ini menolak dirinya sendiri kalau salah
satu di antaranya meleset dari lingkaran berpusat titik tengah OH berjari-jari R/2.
Justru itu isi seluruh rajahnya: sembilan titik yang datang dari tiga sumber yang
sama sekali berbeda ternyata jatuh pada satu lingkaran, dan gambar yang "kira-kira
lewat" tidak membuktikan apa-apa.

Hanya tiga di antaranya diberi nama — satu wakil tiap keluarga — sebab sembilan
label pada bangun selebar 200 piksel akan saling menimpa. Sisanya digambar sebagai
titik dan dijelaskan di alt.

Segitiganya lancip supaya H di dalam dan ketiga kaki garis tinggi jatuh di dalam
sisinya; pada segitiga tumpul semuanya tetap berlaku, tetapi gambarnya melebar
sampai rajahnya tidak lagi terbaca di layar ponsel.
"""

from rajah import *

A, B, C = titik(2.2, 4.4), titik(0, 0), titik(6.4, 0)

O = pusat_luar(A, B, C)
H = titik_tinggi(A, B, C)
N = tengah(O, H)
jari = jari_luar(A, B, C) / 2

tengah_sisi = [tengah(B, C), tengah(C, A), tengah(A, B)]
kaki_tinggi = [kaki(A, garis(B, C)), kaki(B, garis(C, A)), kaki(C, garis(A, B))]
tengah_h = [tengah(H, A), tengah(H, B), tengah(H, C)]

for p in tengah_sisi + kaki_tinggi + tengah_h:
    if abs(jarak(N, p) - jari) > 1e-9:
        raise GagalRajah("ada titik yang meleset dari lingkaran sembilan titik")

RAJAH = rajah(
    "Segitiga ABC lancip dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, "
    "dan puncak A di atas. Ketiga garis tingginya digambar putus-putus dan bertemu di "
    "titik tinggi H di dalam segitiga. Sebuah lingkaran digambar melalui sembilan "
    "titik sekaligus: ketiga titik tengah sisi, ketiga kaki garis tinggi, dan ketiga "
    "titik tengah ruas dari H ke tiap titik sudut. Pusatnya N, dan jari-jarinya "
    "setengah jari-jari lingkaran luar segitiga. Tiga di antara kesembilan titik itu "
    "diberi nama sebagai wakil tiap keluarga: M titik tengah BC, D kaki garis tinggi "
    "dari A, dan K titik tengah ruas AH"
)

RAJAH.lingkaran(N, jari, gaya="tekan")
RAJAH.poligon(A, B, C)
for p, q in zip((A, B, C), kaki_tinggi):
    RAJAH.ruas(p, q, gaya="bantu", putus=True)
for p in tengah_sisi + kaki_tinggi + tengah_h:
    RAJAH.titik(p, gaya="tekan")
(RAJAH
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    # Enam kaki garis tinggi bertemu di H; arahnya ditentukan tangan ke celah
    # terlebar yang tidak menimpa salah satu dari sembilan titik pada lingkarannya.
    .titik(H)
    .label(H, "H", arah=(-0.45, -0.9), jauh=17)
    .label(tengah_sisi[0], "M", arah=(0.3, -1), jauh=15, gaya="tekan")
    .label(kaki_tinggi[0], "D", arah=(-0.8, -0.8), jauh=15, gaya="tekan")
    .label(tengah_h[0], "K", arah=(0.9, 0.4), jauh=15, gaya="tekan")
    .label(N, "N", arah=(1, -0.4), jauh=15, gaya="tekan"))
