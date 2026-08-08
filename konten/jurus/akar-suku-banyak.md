---
id: akar-suku-banyak
nama: Akar dan Koefisien Suku Banyak
pilar: aljabar
tahap: osn-p
prasyarat: [vieta, suku-banyak]
contoh: [asb-contoh-1]
latihan: [asb-01, asb-02, asb-03, asb-04, asb-05, asb-06]
---

## Kapan dipakai

Polinomial berderajat tiga ke atas, dan yang ditanya bentuk simetris akar-akarnya —
jumlah, hasil kali, jumlah kuadrat — bukan akarnya satu per satu.

## Intinya

Perluasan Vieta. Untuk $a_n x^n + \cdots + a_0 = 0$ dengan akar $x_1, \dots, x_n$:

$$\sum x_i = -\frac{a_{n-1}}{a_n}, \qquad \sum_{i<j} x_i x_j = \frac{a_{n-2}}{a_n},
\qquad \sum_{i<j<k} x_i x_j x_k = -\frac{a_{n-3}}{a_n}$$

dan seterusnya, dengan tanda berselang-seling, sampai

$$x_1 x_2 \cdots x_n = (-1)^n \frac{a_0}{a_n}$$

Untuk kubik $ax^3+bx^2+cx+d = 0$, ketiganya:

$$x_1+x_2+x_3 = -\frac{b}{a}, \qquad x_1x_2+x_1x_3+x_2x_3 = \frac{c}{a},
\qquad x_1x_2x_3 = -\frac{d}{a}$$

Seperti pada kuadrat, seluruh isinya adalah **menulis ulang bentuk yang ditanya** lewat
ketiganya:

$$\sum x_i^2 = \left(\sum x_i\right)^2 - 2\sum_{i<j} x_i x_j$$

$$\sum \frac{1}{x_i} = \frac{\sum_{i<j} x_i x_j}{x_1x_2x_3}$$

**Akar sekawan.** Kalau koefisiennya real dan $z$ akar kompleks, maka $\bar{z}$ juga akar.
Akibatnya polinomial berderajat ganjil berkoefisien real selalu punya paling sedikit satu
akar real.

## Jebakan umum

- **Salah pola tanda.** Tandanya berselang-seling mulai dari minus; menghafalkannya
  setengah-setengah lebih berbahaya daripada tidak sama sekali.
- **Lupa membagi $a_n$** ketika koefisien utamanya bukan $1$.
- **Mengira akar kompleks datang sendiri-sendiri.** Untuk koefisien real ia selalu
  berpasangan dengan sekawannya.
