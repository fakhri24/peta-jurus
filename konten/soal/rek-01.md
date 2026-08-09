---
id: rek-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 2
jawaban: "34"
---

## Soal

Sebuah tangga memiliki $8$ anak tangga. Sekali melangkah, seseorang dapat menaiki satu atau
dua anak tangga.

Ada berapa cara menaiki tangga itu?

## Petunjuk

- Beri nama untuk jawaban tangga berisi $n$ anak tangga, lalu hubungkan dengan tangga yang lebih pendek.
- Pecah menurut langkah terakhirnya: satu anak tangga, atau dua.
- Kerjakan dari tangga terpendek ke atas, dan periksa dua nilai awalnya dengan mendaftar.

## Pembahasan

Sebut $a_n$ banyaknya cara menaiki tangga berisi $n$ anak tangga.

**Rekurensnya.** Pecah menurut langkah terakhir — satu anak tangga dari posisi $n-1$, atau
dua anak tangga dari posisi $n-2$. Kedua kelompok lepas dan menutupi semuanya:

$$a_n = a_{n-1} + a_{n-2}$$

**Kasus dasarnya**, diperiksa dengan mendaftar:

$$a_1 = 1, \qquad a_2 = 2$$

**Hitung.**

$$a_3 = 3, \quad a_4 = 5, \quad a_5 = 8, \quad a_6 = 13, \quad a_7 = 21, \quad a_8 = \boxed{34}$$

**Cara memeriksa tanpa mengulang seluruh hitungan.** Jumlahkan dua suku sebelumnya lagi:
$a_7 + a_6 = 21 + 13 = 34$. Kesalahan penjumlahan di tengah tabel akan terbawa sampai akhir
tanpa tanda apa pun, jadi menuliskan seluruh barisannya — bukan hanya nilai terakhir —
adalah kebiasaan yang menolong.

**Bacaan lain dari soal yang sama.** Menaiki tangga $8$ anak tangga sama artinya dengan
menuliskan $8$ sebagai jumlah terurut dari angka $1$ dan $2$. Misalnya $2+1+2+1+2$ adalah
satu cara. Soal yang bunyinya "ada berapa cara menuliskan $8$ sebagai jumlah terurut dari
$1$ dan $2$" karena itu adalah soal yang sama persis.

**Kalau langkahnya boleh sampai tiga anak tangga,** rekurensnya berubah menjadi

$$a_n = a_{n-1} + a_{n-2} + a_{n-3}$$

dan membutuhkan **tiga** kasus dasar: $a_1 = 1$, $a_2 = 2$, $a_3 = 4$. Perhatikan $a_3$
sekarang $4$, bukan $3$, sebab langkah tunggal sejauh tiga anak tangga kini diizinkan.
Banyaknya kasus dasar selalu sama dengan orde rekurensnya.
