---
id: rek-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 3
jawaban: "89"
---

## Soal

Sebuah tangga memiliki $10$ anak tangga. Sekali melangkah, seseorang dapat menaiki **satu**
atau **dua** anak tangga.

Ada berapa cara menaiki tangga itu dari bawah sampai ke atas?

## Petunjuk

- Jangan mencacah langsung. Kerjakan dulu untuk tangga yang sangat pendek — satu, dua, tiga anak tangga — dan catat hasilnya.
- Tanyakan apa yang terjadi pada **langkah terakhir**: ia satu anak tangga, atau dua. Kedua keadaan itu memecah semua cara menjadi dua kelompok.
- Kalau langkah terakhirnya satu, sebelumnya ia berada di anak tangga ke-$9$; kalau dua, di anak tangga ke-$8$.

## Pembahasan

**Beri nama.** Sebut $a_n$ banyaknya cara menaiki tangga berisi $n$ anak tangga.

**Susun rekurensnya lewat langkah terakhir.** Setiap cara berakhir dengan salah satu dari
dua hal:

- **Langkah terakhirnya satu anak tangga.** Sebelum langkah itu ia berada di anak tangga
  ke-$(n-1)$, dan cara mencapainya ada $a_{n-1}$.
- **Langkah terakhirnya dua anak tangga.** Sebelum langkah itu ia berada di anak tangga
  ke-$(n-2)$, dan cara mencapainya ada $a_{n-2}$.

Kedua kelompok ini **lepas** — satu cara tidak mungkin berakhir dengan langkah satu sekaligus
dua — dan **menutupi semuanya**, sebab tiap langkah pasti salah satu di antara keduanya.
Maka aturan jumlah berlaku:

$$a_n = a_{n-1} + a_{n-2}$$

**Tetapkan kasus dasarnya.** Rekurens orde dua membutuhkan dua nilai awal:

$$a_1 = 1 \qquad (\text{satu langkah kecil})$$

$$a_2 = 2 \qquad (1+1 \text{ atau } 2)$$

**Hitung sampai $n = 10$.**

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $a_n$ | $1$ | $2$ | $3$ | $5$ | $8$ | $13$ | $21$ | $34$ | $55$ | $\boxed{89}$ |

**Periksa kasus dasarnya dengan mendaftar.** Untuk $n = 3$ rumusnya memberi $3$, dan memang
hanya ada $1{+}1{+}1$, $1{+}2$, dan $2{+}1$. Untuk $n = 4$ rumusnya memberi $5$, dan
daftarnya $1{+}1{+}1{+}1$, $1{+}1{+}2$, $1{+}2{+}1$, $2{+}1{+}1$, $2{+}2$ — tepat $5$.

**Kasus dasar yang salah merusak seluruh barisan,** dan ia tidak pernah ketahuan di
langkah berikutnya. Kalau $a_2$ ditulis $1$, seluruh tabelnya bergeser dan jawabannya
menjadi $55$. Karena itu kasus dasar selalu diperiksa dengan mendaftar, bukan diduga.

**Barisan ini adalah barisan Fibonacci,** dan ia muncul di banyak soal yang sekilas tidak
berhubungan — barisan biner tanpa dua angka $1$ berdampingan, penutupan papan $2\times n$
dengan domino, himpunan bagian tanpa dua unsur berurutan. Semuanya punya rekurens yang sama,
dan mengenalinya menghemat seluruh pekerjaan menurunkan ulang.

Yang berbeda antar soal itu hanyalah **kasus dasarnya**, dan justru di situ kekeliruan
biasanya masuk.
