---
id: asb-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak]
bentuk: isian
kesulitan: 1
jawaban: "4"
---

## Soal

Tentukan hasil kali akar-akar persamaan

$$x^3 - 2x^2 + 3x - 4 = 0$$

## Petunjuk

- Tidak perlu mencari akarnya — persamaan ini bahkan tidak punya akar rasional.
- Hasil kali akar kubik adalah $-\frac{a_0}{a_3}$.
- Perhatikan tanda minus di depannya, dan tanda konstantanya sendiri.

## Pembahasan

Rumus Vieta memberi hasil kali akar kubik:

$$x_1x_2x_3 = -\frac{a_0}{a_3}$$

Di sini $a_0 = -4$ dan $a_3 = 1$, sehingga

$$x_1x_2x_3 = -\frac{-4}{1} = \boxed{4}$$

Dua tanda minus saling menghapus — itu bagian yang paling sering meleset.

Perhatikan bahwa persamaan ini tidak punya akar rasional. Kandidatnya $\pm1, \pm2, \pm4$,
dan tidak satu pun berhasil:

$$P(1) = -2, \quad P(2) = 2, \quad P(4) = 40, \quad P(-1) = -10$$

Jadi mencari akarnya satu per satu memang tidak akan menolong — dan Vieta memberi
jawabannya tanpa menyentuh akarnya sama sekali.

**Tanda pada rumus Vieta bergantung pada derajat.** Untuk kubik hasil kali akarnya
$-\frac{a_0}{a_3}$; untuk kuadrat ia $+\frac{a_0}{a_2}$. Bentuk umumnya

$$x_1x_2\cdots x_n = (-1)^n \frac{a_0}{a_n}$$

Jadi tandanya positif untuk derajat genap dan negatif untuk derajat ganjil. Menghafal
satu kasus lalu memakainya di kasus lain adalah kekeliruan yang wajar tetapi mahal.
