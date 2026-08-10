---
id: gan-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: isian
kesulitan: 1
jawaban: "10"
---

## Soal

Diketahui titik $A(-3, 4)$ dan $B(5, -2)$.

Tentukan panjang $AB$.

## Petunjuk

- Gambarkan ruas $AB$ sebagai sisi miring sebuah segitiga siku-siku yang kedua sisi lainnya sejajar sumbu.
- Selisih absis memberi sisi mendatar, selisih ordinat memberi sisi tegak.
- Pakai rumus jarak, yang tidak lain Pythagoras yang ditulis dengan lambang lain.

## Pembahasan

**Hitung kedua selisihnya.**

$$\Delta x = 5 - (-3) = 8, \qquad \Delta y = -2 - 4 = -6$$

**Pakai rumus jarak.**

$$AB = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{8^2 + (-6)^2} = \sqrt{64 + 36}
= \sqrt{100} = \boxed{10}$$

**Tripel $(6, 8, 10)$** ✓ — kelipatan dua dari $(3,4,5)$.

### Tanda tidak pernah menjadi masalah

Selisih $\Delta y = -6$ bernilai negatif, tetapi setelah dikuadratkan menjadi $36$. Karena itu
urutan pengurangannya bebas: $-2 - 4$ dan $4 - (-2)$ memberi hasil akhir yang sama.

Yang **tidak** boleh tertukar adalah pasangannya. Menghitung $\sqrt{(x_2 - y_1)^2 + \dots}$ —
mencampur absis dengan ordinat — adalah kekeliruan yang menghasilkan angka wajar tanpa tanda
apa pun bahwa ia salah.

### Rumusnya Pythagoras yang menyamar

Titik $C(5, 4)$ membuat $\triangle ABC$ siku-siku di $C$, dengan

$$AC = |5 - (-3)| = 8 \qquad \text{dan} \qquad BC = |{-2} - 4| = 6$$

Rumus jarak tidak lain Pythagoras pada segitiga itu. Menyadari hal ini berguna saat kamu lupa
rumusnya: gambar segitiga sikunya, dan rumusnya muncul kembali.

### Titik tengah dan pembagian ruas

Dua besaran lain yang sering diminta bersamaan:

$$M = \left(\frac{-3+5}{2}, \frac{4-2}{2}\right) = (1, 1)$$

dan titik yang membagi $AB$ dengan $AP : PB = 3 : 1$:

$$P = \left(\frac{1 \times (-3) + 3 \times 5}{4}, \frac{1 \times 4 + 3 \times (-2)}{4}\right)
= (3, -\tfrac{1}{2})$$

Perhatikan letak angkanya pada rumus pembagian: yang mengalikan koordinat $A$ adalah $n$
(bagian yang **jauh** dari $A$), bukan $m$. Cara memeriksanya: dengan $m : n = 3 : 1$, titik
$P$ harus jauh lebih dekat ke $B$ — dan memang $(3, -\tfrac12)$ dekat ke $B(5,-2)$ ✓.
