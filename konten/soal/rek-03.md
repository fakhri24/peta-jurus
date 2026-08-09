---
id: rek-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 3
jawaban: "55"
---

## Soal

Sebuah papan berukuran $2 \times 9$ akan ditutup seluruhnya dengan domino berukuran
$1 \times 2$. Domino boleh diletakkan mendatar maupun tegak, dan tidak boleh bertumpuk atau
melewati tepi papan.

Ada berapa cara penutupan yang berbeda?

## Petunjuk

- Beri nama untuk jawaban papan $2 \times n$, lalu perhatikan bagaimana **kolom paling kanan** ditutup.
- Kolom paling kanan bisa ditutup oleh satu domino tegak, atau oleh dua domino mendatar yang memakan dua kolom sekaligus.
- Tidak ada kemungkinan ketiga — dan menunjukkan hal itu adalah bagian dari menyusun rekurensnya.

## Pembahasan

Sebut $t_n$ banyaknya penutupan papan $2 \times n$.

**Pecah menurut kolom paling kanan.** Petak kanan atas harus ditutup oleh sebuah domino,
dan hanya ada dua kemungkinan bentuknya:

- **Domino tegak** menutupi seluruh kolom terakhir. Sisanya papan $2 \times (n-1)$, sehingga
  menyumbang $t_{n-1}$.
- **Domino mendatar** menutupi petak kanan atas dan tetangga kirinya. Petak kanan bawah lalu
  **terpaksa** ditutup domino mendatar juga — sebab domino tegak di situ akan menabrak
  domino pertama, dan tidak ada tempat lain. Kedua domino itu memakan dua kolom penuh,
  sehingga sisanya papan $2 \times (n-2)$ dan menyumbang $t_{n-2}$.

Kedua kemungkinan lepas dan menutupi semuanya, jadi

$$t_n = t_{n-1} + t_{n-2}$$

**Perhatikan bagian "terpaksa" di atas.** Ia yang mencegah hitungan ganda: kalau kedua
domino mendatar dianggap dua keputusan bebas, satu penutupan akan terhitung dua kali.
Menunjukkan bahwa domino kedua tidak punya pilihan adalah langkah yang tidak boleh
dilewati.

**Kasus dasarnya.**

$$t_1 = 1 \quad (\text{satu domino tegak})$$

$$t_2 = 2 \quad (\text{dua tegak, atau dua mendatar bertumpuk})$$

**Hitung.**

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
|---|---|---|---|---|---|---|---|---|---|
| $t_n$ | $1$ | $2$ | $3$ | $5$ | $8$ | $13$ | $21$ | $34$ | $\boxed{55}$ |

**Periksa $t_3 = 3$ dengan menggambar.** Papan $2\times3$ dapat ditutup dengan: tiga domino
tegak; satu tegak di kiri lalu dua mendatar; dua mendatar lalu satu tegak di kanan. Tepat
tiga.

**Soal ini, soal tangga, dan soal barisan biner adalah satu soal yang sama.** Ketiganya
punya rekurens $a_n = a_{n-1} + a_{n-2}$, dan yang membedakan hanya kasus dasarnya. Padanan
antara ketiganya bisa dibuat langsung: domino tegak berlaku seperti langkah satu anak
tangga, dan sepasang domino mendatar seperti langkah dua anak tangga.

Mengenali soal yang berpakaian berbeda sebagai soal yang sama adalah keuntungan terbesar
dari melatih rekursi — dan itu sebabnya kasus dasarnya yang harus selalu diperiksa ulang,
sebab hanya itu yang benar-benar berubah.

**Kalau papannya $3 \times n$,** cara ini tidak lagi berlaku apa adanya: kolom terakhirnya
punya lebih banyak kemungkinan bentuk dan sisanya tidak selalu berupa papan persegi panjang
utuh. Soal itu menuntut rekurens dengan lebih dari satu barisan sekaligus.
