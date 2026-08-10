"""Persegi di dalam segitiga: satu sisinya pada alas, dua sudutnya pada kedua kaki.

Sisi perseginya tidak dipilih melainkan dihitung — s = ab/(a+b) dengan a alas dan b
tinggi — lalu keempat titiknya diturunkan dari situ. Rajah yang perseginya digambar
kira-kira akan punya sudut atas yang meleset dari sisi segitiganya, dan itu persis
syarat yang menentukan jawabannya.

Alas 12 dan tinggi 6 memberi s = 4 tepat. Puncaknya sengaja tidak di tengah, supaya
tidak ada yang mengira jawabannya bergantung pada segitiga sama kaki.
"""

from rajah import *

ALAS, TINGGI = 6.0, 3.0             # sebanding 12 : 6
SISI = ALAS * TINGGI / (ALAS + TINGGI)

B, C = titik(0, 0), titik(ALAS, 0)
A = titik(0.38 * ALAS, TINGGI)

# Sisi atas persegi berada di ketinggian SISI; kedua ujungnya pada AB dan AC.
kiri = potong(garis(A, B), garis(titik(0, SISI), titik(1, SISI)))
kanan = potong(garis(A, C), garis(titik(0, SISI), titik(1, SISI)))

if abs(jarak(kiri, kanan) - SISI) > 1e-9:
    raise GagalRajah("lebar segitiga di ketinggian s tidak sama dengan s")

Q = titik(kiri.x, 0)                # kaki kiri persegi pada alas
R = titik(kanan.x, 0)               # kaki kanan

RAJAH = (
    rajah("Segitiga ABC dengan alas BC mendatar sepanjang 12, B di kiri bawah dan C "
          "di kanan bawah, serta puncak A di atas agak ke kiri sehingga tingginya 6. "
          "Sebuah persegi digambar di dalam segitiga: sisi bawahnya terletak pada "
          "alas BC, sudut kiri atasnya menyentuh sisi AB, dan sudut kanan atasnya "
          "menyentuh sisi AC. Panjang sisi persegi itu belum diketahui. Tinggi "
          "segitiga dari A ke alas digambar putus-putus")
    .poligon(A, B, C)
    .arsir(Q, R, kanan, kiri)
    .poligon(Q, R, kanan, kiri)
    .ruas(A, kaki(A, garis(B, C)), gaya="bantu", putus=True)
    .tanda_siku(A, kaki(A, garis(B, C)), C)
    .ukuran(B, C, "12")
    # Titik tengah garis tingginya jatuh di dalam persegi, tempat angkanya terbaca
    # seperti keterangan perseginya. Digeser ke atas, ke bagian tinggi yang di luar.
    .label(bagi(A, kaki(A, garis(B, C)), 0.28), "6", arah=(1, 0), jauh=14, gaya="ukur")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
)
