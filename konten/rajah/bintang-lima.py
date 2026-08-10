"""Bintang lima bersudut ujung tak sama besar.

Sengaja tidak beraturan. Pada bintang beraturan kelima ujungnya 36°, dan siswa
yang mengukurnya di gambar bisa sampai ke 180° tanpa membuktikan apa pun. Dengan
ujung yang jelas berbeda-beda, satu-satunya jalan ke jawabannya adalah alasan.
"""

import math

from rajah import *

JARI = 3.2
ARAH = (20, 96, 155, 212, 290)      # E, A, B, C, D — urut berlawanan jarum jam

E, A, B, C, D = (
    titik(JARI * math.cos(math.radians(d)), JARI * math.sin(math.radians(d)))
    for d in ARAH
)

# Tiap ujung disambungkan ke ujung yang berjarak dua langkah, itu yang membuat
# poligonnya berpotongan sendiri dan tampak sebagai bintang.
RAJAH = (
    rajah("Bintang lima bersudut lima, dengan ujung-ujungnya diberi nama A, B, C, "
          "D, dan E. Kelima sudut di ujung bintang ditandai busur kecil, dan "
          "besarnya jelas tidak sama satu sama lain")
    .poligon(E, B, D, A, C)
    .tanda_sudut(D, A, C)
    .tanda_sudut(E, B, D)
    .tanda_sudut(A, C, E)
    .tanda_sudut(B, D, A)
    .tanda_sudut(C, E, B)
    .titik(A, "A").titik(B, "B").titik(C, "C").titik(D, "D").titik(E, "E")
)
