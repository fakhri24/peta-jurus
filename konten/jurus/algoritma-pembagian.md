---
id: algoritma-pembagian
nama: Algoritma Pembagian
pilar: teori-bilangan
tahap: osn-k
prasyarat: [keterbagian]
contoh: [ap-contoh-1]
latihan: [ap-01, ap-02, ap-03]
---

## Kapan dipakai

Soal berbicara tentang **sisa**, atau kamu ingin membagi semua bilangan bulat menjadi
beberapa golongan untuk diperiksa satu per satu.

## Intinya

Untuk sembarang bulat $a$ dan bulat positif $b$, ada tepat satu pasang $q$ dan $r$ dengan

$$a = bq + r, \qquad 0 \le r < b$$

Kata **tepat satu** itu yang bekerja. Karena sisanya tunggal dan pasti berada di
$\{0, 1, \dots, b-1\}$, seluruh bilangan bulat terbelah rapi jadi $b$ golongan.

Dari sini lahir jurus paling murah dalam teori bilangan: **periksa semua kemungkinan
sisa**. Kalau soal melibatkan pembagian oleh $3$, cukup tulis $n = 3k$, $n = 3k+1$,
$n = 3k+2$ dan kerjakan tiga kasus. Tiga kasus itu meliputi semua bilangan bulat di
dunia — tanpa terkecuali.

## Jebakan umum

- **Menganggap sisa boleh negatif.** Menurut definisinya $0 \le r < b$. Untuk $a = -7$
  dan $b = 3$, sisanya $2$ (karena $-7 = 3(-3) + 2$), bukan $-1$.
- **Lupa kasus $r = 0$.** Saat memeriksa golongan sisa, $n = 3k$ sama pentingnya dengan
  dua golongan lainnya.
- **Memilih pembagi yang salah.** Kalau soal berbicara tentang kuadrat, periksa sisa
  terhadap $4$ atau $8$ — bukan $2$. Kuadrat hanya bersisa $0$ atau $1$ modulo $4$, dan
  fakta itu jauh lebih tajam.
