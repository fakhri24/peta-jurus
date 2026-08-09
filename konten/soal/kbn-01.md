---
id: kbn-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 1
jawaban: "21"
---

## Soal

Tentukan koefisien $x^2$ pada penjabaran

$$(1+x)^7$$

## Petunjuk

- Tuliskan bentuk umum suku penjabarannya, lalu cari suku yang pangkat $x$-nya sesuai.
- Karena suku pertamanya $1$, pangkat berapa pun darinya tetap bernilai $1$.
- Yang tersisa hanyalah bilangan di depan sukunya.

## Pembahasan

Menurut teorema binomial,

$$(1+x)^7 = \sum_{k=0}^{7} \binom{7}{k}\, 1^{\,7-k}\, x^{\,k}
= \sum_{k=0}^{7} \binom{7}{k}\, x^{\,k}$$

Karena $1^{\,7-k} = 1$ untuk setiap $k$, bentuknya menjadi sangat bersih: **koefisien
$x^k$ adalah $\binom{7}{k}$ itu sendiri.**

Untuk $x^2$, ambil $k = 2$:

$$\binom{7}{2} = \frac{7 \times 6}{2} = \boxed{21}$$

**Bentuk $(1+x)^n$ layak dikenali secara khusus,** sebab di situ koefisiennya persis
koefisien binomial tanpa gangguan apa pun:

$$(1+x)^n = \binom{n}{0} + \binom{n}{1}x + \binom{n}{2}x^2 + \cdots + \binom{n}{n}x^n$$

Banyak identitas koefisien binomial paling mudah dibuktikan dengan mensubstitusi nilai
tertentu ke bentuk ini. Ambil $x = 1$:

$$2^n = \binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n}$$

Ambil $x = -1$, untuk $n \ge 1$:

$$0 = \binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \cdots$$

**Periksa dengan segitiga Pascal.** Baris ke-$7$ berbunyi

$$1,\ 7,\ 21,\ 35,\ 35,\ 21,\ 7,\ 1$$

Suku ketiga — yaitu koefisien $x^2$, karena penomorannya dimulai dari $x^0$ — memang $21$.
Perhatikan juga jumlah seluruh baris itu $128 = 2^7$, sesuai identitas di atas.
