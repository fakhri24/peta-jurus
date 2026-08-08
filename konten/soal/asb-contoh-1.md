---
id: asb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Akar-akar persamaan $x^3 - 6x^2 + 11x - 6 = 0$ adalah $a$, $b$, dan $c$. Tentukan nilai
$a+b+c$.

## Petunjuk

- Yang ditanya bentuk simetris akarnya, jadi akarnya sendiri tidak perlu dicari.
- Rumus Vieta berlaku untuk derajat berapa pun, bukan hanya kuadrat.
- Untuk kubik $ax^3+bx^2+cx+d$, jumlah akarnya $-\frac{b}{a}$ — pola yang sama seperti pada kuadrat.

## Pembahasan

Rumus Vieta untuk kubik $a_3x^3 + a_2x^2 + a_1x + a_0 = 0$ dengan akar $x_1, x_2, x_3$:

$$x_1+x_2+x_3 = -\frac{a_2}{a_3}, \qquad
x_1x_2 + x_1x_3 + x_2x_3 = \frac{a_1}{a_3}, \qquad
x_1x_2x_3 = -\frac{a_0}{a_3}$$

Perhatikan **tanda yang berselang-seling**: minus, plus, minus. Polanya berlanjut untuk
derajat yang lebih tinggi.

Di sini $a_3 = 1$, $a_2 = -6$, $a_1 = 11$, $a_0 = -6$, sehingga

$$a+b+c = -\frac{-6}{1} = \boxed{6}$$

Periksa: polinomialnya memang $(x-1)(x-2)(x-3)$, jadi akarnya $1, 2, 3$ dengan jumlah $6$.

Sekalian dua yang lain:

$$ab+ac+bc = \frac{11}{1} = 11, \qquad abc = -\frac{-6}{1} = 6$$

dan memang $1\cdot2 + 1\cdot3 + 2\cdot3 = 11$ serta $1 \cdot 2 \cdot 3 = 6$.

**Cara mengingat tandanya** tanpa menghafal: tulis bentuk terfaktornya
$a_3(x-x_1)(x-x_2)(x-x_3)$ dan jabarkan. Setiap kali sebuah akar diambil, ia membawa tanda
minus — jadi suku dengan satu akar bertanda minus, dua akar bertanda plus, tiga akar
bertanda minus lagi.

Seperti pada kuadrat, seluruh isi jurus ini adalah **menulis ulang bentuk yang ditanya**
lewat ketiga besaran itu.
