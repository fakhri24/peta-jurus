---
id: asb-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak, suku-banyak]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan rumus Vieta untuk persamaan pangkat tiga: jika $x_1, x_2, x_3$ adalah akar-akar

$$a_3x^3 + a_2x^2 + a_1x + a_0 = 0, \qquad a_3 \ne 0$$

maka

$$\sum x_i = -\frac{a_2}{a_3}, \qquad \sum_{i<j} x_ix_j = \frac{a_1}{a_3},
\qquad x_1x_2x_3 = -\frac{a_0}{a_3}$$

## Petunjuk

- Tulis polinomialnya dalam bentuk terfaktor memakai ketiga akarnya, dengan faktor pengali yang tepat di depan.
- Jabarkan $a_3(x-x_1)(x-x_2)(x-x_3)$ secara teliti, kelompokkan menurut pangkat $x$.
- Bandingkan koefisien tiap pangkat pada kedua ruas.

## Pembahasan

Karena $x_1, x_2, x_3$ akar-akarnya dan $a_3 \ne 0$, polinomialnya bisa ditulis dalam
bentuk terfaktor

$$a_3x^3+a_2x^2+a_1x+a_0 = a_3\left(x-x_1\right)\left(x-x_2\right)\left(x-x_3\right)$$

Faktor $a_3$ di depan diperlukan supaya koefisien $x^3$ pada kedua ruas cocok.

**Jabarkan ruas kanan.** Kalikan dua faktor pertama:

$$(x-x_1)(x-x_2) = x^2 - \left(x_1+x_2\right)x + x_1x_2$$

Kalikan dengan faktor ketiga:

$$\left[x^2 - (x_1+x_2)x + x_1x_2\right](x - x_3)$$

$$= x^3 - (x_1+x_2)x^2 + x_1x_2\,x - x_3x^2 + (x_1+x_2)x_3\,x - x_1x_2x_3$$

Kelompokkan menurut pangkat $x$:

$$= x^3 - \left(x_1+x_2+x_3\right)x^2
+ \left(x_1x_2 + x_1x_3 + x_2x_3\right)x - x_1x_2x_3$$

Kalikan dengan $a_3$:

$$a_3x^3 - a_3\left(\sum x_i\right)x^2 + a_3\left(\sum_{i<j} x_ix_j\right)x
- a_3\,x_1x_2x_3$$

**Bandingkan koefisien.** Kedua ruas adalah polinomial yang sama, jadi koefisien tiap
pangkat $x$ harus cocok:

$$a_2 = -a_3\sum x_i, \qquad a_1 = a_3\sum_{i<j}x_ix_j, \qquad a_0 = -a_3\,x_1x_2x_3$$

Bagi masing-masing dengan $a_3$ — sah karena $a_3 \ne 0$:

$$\sum x_i = -\frac{a_2}{a_3}, \qquad \sum_{i<j} x_ix_j = \frac{a_1}{a_3},
\qquad x_1x_2x_3 = -\frac{a_0}{a_3}$$

$\blacksquare$

**Asal tanda berselang-selingnya sekarang terlihat.** Setiap kali sebuah akar "diambil"
dari faktor $(x - x_i)$, ia membawa tanda minus. Suku dengan satu akar memuat satu minus,
dua akar memuat dua minus yang saling menghapus, tiga akar memuat tiga minus. Karena itu
polanya minus, plus, minus.

Pembuktian yang sama berlaku untuk derajat berapa pun tanpa perubahan gagasan, dan
memberi bentuk umumnya:

$$\sum_{i_1 < \cdots < i_k} x_{i_1}\cdots x_{i_k} = (-1)^k \frac{a_{n-k}}{a_n}$$

**Bahwa polinomialnya bisa ditulis terfaktor** adalah langkah yang bersandar pada teorema
faktor: tiap akar $x_i$ memberi faktor $(x - x_i)$, dan ketiganya sudah menghabiskan
derajatnya.

## Rubrik

- Menulis bentuk terfaktor dengan faktor $a_3$ di depan, beserta alasannya
- Menjabarkan hasil kali tiga faktor secara benar
- Mengelompokkan hasilnya menurut pangkat $x$
- Menyamakan koefisien tiap pangkat pada kedua ruas
- Membagi dengan $a_3$ dan menyebut $a_3 \ne 0$ sebagai alasan sahnya
- Untuk nilai penuh: menjelaskan asal pola tanda berselang-selingnya
