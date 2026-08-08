---
id: dl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-linear]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Ada berapa pasangan bilangan asli $(x, y)$ yang memenuhi $3x + 5y = 100$?

## Petunjuk

- Periksa dulu apakah solusinya ada sama sekali, sebelum mencari-cari.
- Untuk menyingkirkan satu peubah, ambil persamaannya modulo salah satu koefisien. Modulo $3$ akan melenyapkan $x$.
- Setelah $y$ terkurung dalam satu kelas sisa, tinggal cacah berapa nilai yang muat dalam batas $x, y \ge 1$.

## Pembahasan

**Langkah 1: apakah ada solusi?** $\gcd(3,5) = 1$, dan $1 \mid 100$, jadi solusi bulat
pasti ada.

**Langkah 2: kurung salah satu peubah.** Ambil modulo $3$ supaya $3x$ lenyap:

$$5y \equiv 100 \pmod 3$$

Karena $5 \equiv 2$ dan $100 \equiv 1 \pmod 3$:

$$2y \equiv 1 \pmod 3$$

Coba $y = 0, 1, 2$: nilai $2y$ berturut-turut $0, 2, 1$. Jadi $y \equiv 2 \pmod 3$.

**Langkah 3: pasang batasnya.** Dibutuhkan $y \ge 1$ dan $x \ge 1$. Dari
$3x = 100 - 5y \ge 3$ diperoleh $5y \le 97$, yaitu $y \le 19$.

Nilai $y$ yang memenuhi $y \equiv 2 \pmod 3$ dan $1 \le y \le 19$:

$$y = 2,\ 5,\ 8,\ 11,\ 14,\ 17$$

Masing-masing memberi satu $x$:

$$(x,y) = (30,2),\ (25,5),\ (20,8),\ (15,11),\ (10,14),\ (5,17)$$

Ada $\boxed{6}$ pasangan.

Perhatikan bahwa $y = 20$ juga memenuhi $y \equiv 2 \pmod 3$, tetapi memberi $x = 0$ —
dan $0$ bukan bilangan asli. Batas $x \ge 1$, bukan $x \ge 0$, itulah yang memangkas
cacahnya tepat satu.
