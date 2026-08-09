---
id: drg-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 4
jawaban: "1854"
---

## Soal

Tujuh orang menitipkan payungnya, lalu payung itu dikembalikan secara acak — satu payung
per orang.

Ada berapa cara pengembalian sehingga tidak seorang pun menerima payungnya sendiri?

## Petunjuk

- Yang dicari adalah nilai baku untuk tujuh objek. Rekurens jauh lebih cepat daripada rumus jumlah di sini.
- Hitung berurutan dari nilai kecil, dan tuliskan seluruh barisannya supaya bisa diperiksa.
- Periksa hasil akhirnya dengan pendekatan $\frac{n!}{e}$.

## Pembahasan

Yang dicari adalah $D_7$.

**Hitung berurutan.** Pakai $D_n = (n-1)\left(D_{n-1}+D_{n-2}\right)$ dengan $D_1 = 0$,
$D_2 = 1$:

| $n$ | perhitungan | $D_n$ |
|---|---|---|
| $3$ | $2(1+0)$ | $2$ |
| $4$ | $3(2+1)$ | $9$ |
| $5$ | $4(9+2)$ | $44$ |
| $6$ | $5(44+9)$ | $265$ |
| $7$ | $6(265+44)$ | $6 \times 309 = \boxed{1854}$ |

**Periksa dengan pendekatan.**

$$\frac{7!}{e} = \frac{5040}{2{,}71828\ldots} \approx 1854{,}11$$

Bilangan bulat terdekatnya $1854$. Cocok.

**Mengapa rumus jumlah tidak dipakai di sini.** Untuk $n = 7$ ia menuntut

$$D_7 = 5040\left(1 - 1 + \tfrac12 - \tfrac16 + \tfrac1{24} - \tfrac1{120} + \tfrac1{720} - \tfrac1{5040}\right)$$

yaitu delapan pecahan dengan penyebut berbeda yang harus disamakan lalu dijumlahkan.
Rekurens hanya menuntut penjumlahan dan perkalian bilangan bulat, dan tiap barisnya bisa
diperiksa terhadap nilai yang sudah dikenal.

**Kewajaran jawabannya.** Nisbah terhadap seluruh susunan:

$$\frac{1854}{5040} \approx 0{,}3679$$

sangat dekat dengan $\frac1e \approx 0{,}3679$. Nisbah ini nyaris tidak berubah seiring $n$
bertambah — bahkan untuk $n$ sebesar apa pun, kira-kira $37\%$ dari seluruh susunan tidak
punya titik tetap. Kenyataan itu sering mengejutkan, sebab dugaan awal orang biasanya
nisbahnya mengecil.

**Menuliskan seluruh barisannya berguna sebagai kebiasaan:**

$$0,\ 1,\ 2,\ 9,\ 44,\ 265,\ 1854,\ 14833,\ \dots$$

Kekeliruan aritmetika di satu baris akan membuat baris berikutnya menyimpang jauh dari
$\frac{n!}{e}$, dan dengan begitu langsung ketahuan.
