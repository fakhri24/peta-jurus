---
id: sbr-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 4
jawaban: "45"
---

## Soal

Ada berapa penyelesaian bilangan bulat tak negatif dari

$$x_1 + x_2 + x_3 = 10$$

yang memenuhi $x_1 \le 4$?

## Petunjuk

- Batas **atas** tidak bisa ditangani dengan penggeseran seperti batas bawah. Cari jalan lain.
- Hitung dulu tanpa memedulikan syarat itu, lalu buang penyelesaian yang melanggarnya.
- "Melanggar" berarti $x_1 \ge 5$ — dan syarat itu sendiri sebuah batas bawah, yang sudah bisa ditangani.

## Pembahasan

**Mengapa penggeseran tidak berlaku.** Untuk batas bawah, menggeser $x' = x - c$ mengubah
syaratnya menjadi tak negatif dan persoalannya tetap berbentuk sama. Untuk batas **atas**,
tidak ada penggeseran yang melakukan hal serupa — karena itu batas atas selalu dikerjakan
dengan membuang yang melanggar.

**Hitung tanpa syarat.** Dengan $n = 10$ dan $k = 3$:

$$\binom{10+3-1}{3-1} = \binom{12}{2} = 66$$

**Hitung yang melanggar.** Melanggar berarti $x_1 \ge 5$. Syarat itu batas **bawah**, jadi
bisa digeser: tulis $x_1' = x_1 - 5$, sehingga $x_1' \ge 0$ dan

$$x_1' + x_2 + x_3 = 10 - 5 = 5$$

Banyaknya penyelesaian tak negatifnya:

$$\binom{5+3-1}{3-1} = \binom72 = 21$$

**Kurangkan.**

$$66 - 21 = \boxed{45}$$

**Mengapa satu pengurangan sudah cukup di sini.** Kalau ada **beberapa** batas atas —
misalnya $x_1 \le 4$ dan $x_2 \le 4$ sekaligus — kelompok yang melanggar bisa saling
beririsan, dan pengurangan lugu akan menghitung ganda. Di situ dibutuhkan inklusi–eksklusi
penuh.

Di soal ini hanya ada satu batas atas, sehingga kelompok pelanggarnya tunggal dan sekali
pengurangan sudah benar.

Periksa juga apakah dua pelanggaran mungkin terjadi bersamaan: kalau syaratnya $x_1 \le 4$
dan $x_2 \le 4$, maka $x_1 \ge 5$ dan $x_2 \ge 5$ menuntut jumlah paling sedikit $10$ —
yang masih mungkin di sini, jadi irisannya tidak kosong dan koreksi memang akan dibutuhkan.

**Periksa dengan menghitung langsung.** Pecah menurut nilai $x_1$; untuk tiap nilai,
$x_2 + x_3$ menentukan sisanya dan punya (sisa $+\,1$) penyelesaian:

| $x_1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| penyelesaian | $11$ | $10$ | $9$ | $8$ | $7$ |

$$11+10+9+8+7 = 45$$

Cocok.
