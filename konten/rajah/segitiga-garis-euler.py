"""Garis Euler: titik tinggi, titik berat, pusat lingkaran luar, dan pusat sembilan titik.

Keempat titiknya dihitung — titik_tinggi(), titik_berat(), pusat_luar(), dan titik
tengah OH — bukan ditaruh berjajar dengan tangan. Kesegarisan yang tergambar karena
itu benar-benar hasil, bukan janji: kalau salah satu rumusnya keliru, keempatnya
berhenti segaris dan berkas ini menolak dirinya sendiri lewat pemeriksaan di bawah.

Segitiganya sengaja tidak sama kaki dan sengaja jauh dari sama sisi. Pada segitiga
sama sisi keempat titiknya menyatu dan garisnya tidak ada; pada yang hampir sama
sisi OH menyusut, dan karena GN = OH/6 keempatnya berdesakan sampai nisbah
HG : GO = 2 : 1 tidak lagi terbaca. Bentuk yang dipakai di sini memberi OH sekitar
2,8 pada segitiga selebar 6,5 — cukup renggang tanpa harus tumpul.
"""

from rajah import *

A, B, C = titik(0.9, 2.6), titik(0, 0), titik(6.5, 0)

O = pusat_luar(A, B, C)
H = titik_tinggi(A, B, C)
G = titik_berat(A, B, C)
N = tengah(O, H)

if jarak(G, kaki(G, garis(O, H))) > 1e-9:
    raise GagalRajah("G tidak jatuh pada garis OH — salah satu rumus titik istimewanya keliru")
if abs(jarak(H, G) / jarak(G, O) - 2) > 1e-9:
    raise GagalRajah("HG : GO bukan 2 : 1")

# Garisnya diperpanjang sedikit di kedua ujung supaya terbaca sebagai garis.
arah = (O - H).satuan()
ujung_h = H - arah * 0.8
ujung_o = O + arah * 0.8

RAJAH = (
    rajah("Segitiga ABC yang ketiga sisinya berbeda panjang, dengan alas BC mendatar, "
          "B di kiri bawah, C di kanan bawah, dan puncak A di atas agak ke kiri. Di "
          "dalamnya digambar sebuah garis lurus yang melalui empat titik sekaligus: "
          "titik tinggi H, pusat lingkaran sembilan titik N, titik berat G, dan pusat "
          "lingkaran luar O, terurut demikian sepanjang garis itu. Jarak dari H ke G "
          "tepat dua kali jarak dari G ke O, dan N tepat di tengah antara H dan O. "
          "Garis itu disebut garis Euler")
    .poligon(A, B, C)
    .ruas(ujung_h, ujung_o, gaya="tekan")
    .titik(A, "A", arah=(0, 1))
    .titik(B, "B", arah=(-1, -0.5))
    .titik(C, "C", arah=(1, -0.5))
    .titik(H, "H", arah=(0.6, 0.9), gaya="tekan")
    .titik(N, "N", arah=(0.6, 0.9), gaya="tekan")
    .titik(G, "G", arah=(-0.6, -0.9), gaya="tekan")
    .titik(O, "O", arah=(0.6, 0.9), gaya="tekan")
)
