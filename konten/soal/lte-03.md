---
id: lte-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 2
jawaban: "5"
---

## Soal

Tentukan pangkat tertinggi $3$ yang membagi $4^{27} + 5^{27}$.

## Petunjuk

- Ini bentuk **jumlah** pangkat, bukan selisih. Rumusnya berbeda, dan syaratnya juga.
- Untuk $a^n + b^n$, dibutuhkan $n$ ganjil dan $p \mid a + b$. Periksa keduanya.
- Rumusnya $v_p(a^n + b^n) = v_p(a+b) + v_p(n)$.

## Pembahasan

Di sini $a = 4$, $b = 5$, dan $n = 27$.

**Periksa syaratnya.** Untuk bentuk jumlah, yang dibutuhkan ada tiga:

- $n$ ganjil: $27$ ganjil $\checkmark$
- $p \mid a + b$: $a + b = 9$, dan $3 \mid 9$ $\checkmark$
- $p \nmid a$ dan $p \nmid b$: $3 \nmid 4$ dan $3 \nmid 5$ $\checkmark$

Semua terpenuhi, jadi

$$v_3\left(a^n + b^n\right) = v_3(a + b) + v_3(n)$$

**Hitung kedua sukunya.**

$$v_3(a+b) = v_3(9) = 2, \qquad v_3(n) = v_3(27) = v_3\left(3^3\right) = 3$$

Maka

$$v_3\left(4^{27} + 5^{27}\right) = 2 + 3 = \boxed{5}$$

Syarat "$n$ ganjil" itu tidak boleh dilewati. Untuk $n$ genap, bentuk $a^n + b^n$ tidak
punya rumus semacam ini sama sekali — dan memang tidak bisa: $4^2 + 5^2 = 41$ tidak habis
dibagi $3$, padahal $3 \mid 4 + 5$.

Alasannya terlihat dari pemfaktoran. Untuk $n$ ganjil, $a + b$ selalu membagi $a^n + b^n$;
untuk $n$ genap, tidak.
