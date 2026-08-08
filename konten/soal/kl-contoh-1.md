---
id: kl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [kongruensi-linear]
bentuk: isian
kesulitan: 2
jawaban: "5"
---

## Soal

Tentukan bilangan bulat $x$ dengan $0 \le x < 11$ yang memenuhi

$$5x \equiv 3 \pmod{11}$$

## Petunjuk

- Periksa dulu apakah solusinya ada, dan kalau ada, ada berapa.
- Karena $\gcd(5, 11) = 1$, solusinya tunggal modulo $11$. Yang dibutuhkan adalah invers $5$.
- Cari $x$ dengan $5x \equiv 1 \pmod{11}$ lebih dulu, lalu kalikan hasilnya dengan $3$.

## Pembahasan

**Ada berapa solusi?** Menurut aturannya, $ax \equiv b \pmod m$ punya solusi tepat ketika
$d = \gcd(a,m)$ membagi $b$, dan kalau ada, solusinya tepat $d$ buah modulo $m$.

Di sini $\gcd(5, 11) = 1$, yang membagi $3$. Jadi solusinya ada dan tunggal.

**Cari invers $5$ modulo $11$.** Yang dicari $t$ dengan $5t \equiv 1 \pmod{11}$. Coba
kelipatan $5$:

$$5, \quad 10, \quad 15 \equiv 4, \quad 20 \equiv 9, \quad 25 \equiv 3, \quad
30 \equiv 8, \quad 35 \equiv 2, \quad 40 \equiv 7, \quad 45 \equiv 1$$

Jadi $5 \times 9 \equiv 1$, sehingga $5^{-1} \equiv 9 \pmod{11}$.

**Selesaikan.** Kalikan kedua ruas dengan $9$:

$$x \equiv 9 \times 3 = 27 \equiv 5 \pmod{11}$$

Jadi $x = \boxed{5}$.

Periksa: $5 \times 5 = 25 = 2 \times 11 + 3$. Benar.

Perhatikan apa yang sebenarnya dilakukan: bukan "membagi kedua ruas dengan $5$", melainkan
mengalikan dengan invers $5$. Pembagian dalam kongruensi tidak selalu sah — yang selalu sah
adalah mengalikan, dan invers hanya ada ketika pengalinya relatif prima terhadap modulus.
