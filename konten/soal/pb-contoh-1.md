---
id: pb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: aljabar
tahap: osn
jurus: [polinomial-bulat, keterbagian]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Polinomial $P$ berkoefisien bulat memenuhi $P(2) = 3$. Tentukan sisa pembagian $P(9)$
oleh $7$.

## Petunjuk

- Kamu tidak tahu $P$ sama sekali, jadi jawabannya harus datang dari sifat umum polinomial berkoefisien bulat.
- Sifat pokoknya: $(a-b)$ selalu membagi $P(a) - P(b)$ untuk $a, b$ bulat.
- Di sini $9 - 2 = 7$ — persis modulus yang ditanyakan.

## Pembahasan

**Sifat pokok jurus ini:** untuk polinomial $P$ berkoefisien bulat dan bilangan bulat
$a$, $b$,

$$(a-b) \ \big|\ \left(P(a) - P(b)\right)$$

Alasannya dari faktorisasi $a^k - b^k = (a-b)\left(a^{k-1} + \cdots + b^{k-1}\right)$ pada
tiap suku, lalu dijumlahkan dengan koefisiennya yang bulat.

Terapkan dengan $a = 9$ dan $b = 2$:

$$(9 - 2) \ \big|\ \left(P(9) - P(2)\right) \quad\Longrightarrow\quad
7 \ \big|\ \left(P(9) - 3\right)$$

Artinya

$$P(9) \equiv 3 \pmod 7$$

Sisanya adalah $\boxed{3}$.

**Perhatikan bahwa $P$ tidak pernah diketahui**, dan memang tidak perlu. Ada tak hingga
banyak polinomial berkoefisien bulat dengan $P(2) = 3$ — misalnya $P(x) = x+1$,
$P(x) = x^2 - 1$, atau $P(x) = 3$. Periksa ketiganya:

$$9 + 1 = 10 \equiv 3, \qquad 81 - 1 = 80 = 11 \times 7 + 3, \qquad 3 \equiv 3$$

Semuanya bersisa $3$ modulo $7$ — persis seperti yang dijamin sifatnya.

**Bacaan yang paling berguna:** untuk polinomial berkoefisien bulat, nilai
$P(n) \bmod m$ hanya bergantung pada $n \bmod m$. Jadi memeriksa $m$ nilai sudah menutup
seluruh bilangan bulat — dan itu mengubah pernyataan tentang tak hingga banyak bilangan
menjadi pemeriksaan berhingga.

**Syarat koefisien bulat wajib.** Untuk $P(x) = \frac{x}{2}$, nilai $P(9) - P(2) = 3{,}5$
bahkan bukan bilangan bulat, jadi sifatnya gugur seluruhnya.
