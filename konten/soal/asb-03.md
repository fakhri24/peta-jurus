---
id: asb-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak]
bentuk: isian
kesulitan: 2
jawaban: "2"
---

## Soal

Akar-akar persamaan $x^3 - 5x^2 + 8x - 4 = 0$ adalah $a$, $b$, $c$. Tentukan nilai

$$\frac1a + \frac1b + \frac1c$$

## Petunjuk

- Satukan ketiga pecahan menjadi satu pecahan lebih dulu.
- Pembilangnya akan menjadi $bc + ac + ab$, dan penyebutnya $abc$ — keduanya besaran Vieta.
- Ambil kedua nilai itu dari koefisiennya, lalu bagi.

## Pembahasan

Satukan ketiga pecahan dengan penyebut bersama $abc$:

$$\frac1a + \frac1b + \frac1c = \frac{bc + ac + ab}{abc}$$

Kedua bagiannya adalah besaran Vieta. Dengan $a_3 = 1$, $a_1 = 8$, $a_0 = -4$:

$$ab+ac+bc = \frac{a_1}{a_3} = \frac{8}{1} = 8, \qquad
abc = -\frac{a_0}{a_3} = -\frac{-4}{1} = 4$$

Maka

$$\frac1a+\frac1b+\frac1c = \frac{8}{4} = \boxed{2}$$

Periksa: polinomialnya memfaktor menjadi $(x-1)(x-2)^2$, jadi akarnya $1$, $2$, $2$. Dan

$$\frac11 + \frac12 + \frac12 = 2$$

Cocok.

Perhatikan bahwa salah satu akarnya **berulang**. Rumus Vieta tetap berlaku, asalkan akar
kembar dihitung sebanyak kelipatannya — di sini $2$ dihitung dua kali. Kalau tidak, jumlah
akarnya akan terbaca $3$ alih-alih $5$.

**Syarat yang layak diperiksa:** ketiga akarnya tak nol, sebab keduanya menjadi penyebut.
Itu terjamin oleh $abc = 4 \ne 0$. Kalau konstantanya nol, salah satu akarnya nol dan
bentuk yang ditanya tidak terdefinisi.

Pola "satukan pecahan lalu baca sebagai besaran Vieta" bekerja untuk banyak bentuk lain:

$$\frac{1}{ab} + \frac{1}{ac} + \frac{1}{bc} = \frac{c + b + a}{abc}$$
