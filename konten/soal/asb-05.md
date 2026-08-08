---
id: asb-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak]
bentuk: isian
kesulitan: 3
jawaban: "11"
---

## Soal

Sebuah persamaan pangkat tiga dengan koefisien utama $1$ mempunyai akar-akar $1$, $2$, dan
$3$. Tentukan koefisien $x$ pada persamaan itu.

## Petunjuk

- Alurnya dibalik dari biasanya: akarnya diketahui, koefisiennya yang dicari. Hubungan antara keduanya bekerja ke dua arah.
- Koefisien $x$ pada kubik monik sama dengan jumlah hasil kali akar **berpasangan**.
- Hitung $ab + ac + bc$ untuk $a=1$, $b=2$, $c=3$.

## Pembahasan

**Cara pertama: lewat Vieta.** Untuk kubik monik $x^3 + a_2x^2 + a_1x + a_0$,

$$a_1 = ab+ac+bc$$

yaitu jumlah hasil kali akar berpasangan, dengan tanda **positif**.

Hitung untuk $a=1$, $b=2$, $c=3$:

$$ab+ac+bc = (1)(2) + (1)(3) + (2)(3) = 2 + 3 + 6 = \boxed{11}$$

**Cara kedua: susun polinomialnya.** Karena akarnya diketahui dan koefisien utamanya $1$:

$$P(x) = (x-1)(x-2)(x-3)$$

Jabarkan bertahap:

$$(x-1)(x-2) = x^2 - 3x + 2$$

$$\left(x^2-3x+2\right)(x-3) = x^3 - 3x^2 - 3x^2 + 9x + 2x - 6 = x^3 - 6x^2 + 11x - 6$$

Koefisien $x$-nya $11$. Cocok.

Sekalian periksa yang lain: koefisien $x^2$ adalah $-6 = -(1+2+3)$ ✓, dan konstantanya
$-6 = -(1)(2)(3)$ ✓.

**Arah terbalik ini sering muncul di olimpiade** dengan pembungkus berbeda: "susun
persamaan yang akarnya …", atau "tentukan persamaan baru yang akarnya dua kali akar
persamaan lama". Semuanya diselesaikan dengan menghitung besaran Vieta yang baru, lalu
menyusun polinomialnya dari situ.

Contohnya: kalau akarnya digandakan menjadi $2, 4, 6$, maka jumlahnya menjadi $12$,
jumlah hasil kali berpasangan menjadi $4 \times 11 = 44$, dan hasil kalinya
$8 \times 6 = 48$ — memberi $x^3 - 12x^2 + 44x - 48$.
