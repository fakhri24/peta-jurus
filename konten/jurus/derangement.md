---
id: derangement
nama: Perpindahan Total
pilar: kombinatorika
tahap: osn-p
prasyarat: [inklusi-eksklusi, kombinasi]
contoh: [drg-contoh-1]
latihan: [drg-01, drg-02, drg-03, drg-04, drg-05, drg-06]
---

## Kapan dipakai

Menyusun ulang $n$ objek sehingga **tidak satu pun** menempati tempat asalnya. Pemicunya
hampir selalu berupa cerita: tidak ada orang yang menerima suratnya sendiri, tidak ada tamu
yang duduk di kursi semula, tidak ada anak yang mendapat kado miliknya.

Bentuk yang sedikit berbeda tapi masih jurus ini: "tepat $m$ orang menerima miliknya
sendiri".

## Intinya

Banyaknya susunan tanpa satu pun titik tetap, ditulis $D_n$:

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^{k}}{k!}$$

Rumus itu bukan hafalan lepas — ia keluar langsung dari inklusi–eksklusi. Ambil $A_i$
sebagai himpunan susunan yang membiarkan objek ke-$i$ di tempatnya. Yang diminta adalah
susunan yang tidak masuk satu pun $A_i$, dan irisan sebanyak $k$ di antaranya berukuran
$(n-k)!$.

Bentuk rekursifnya sering lebih cepat dipakai:

$$D_n = (n-1)\left(D_{n-1} + D_{n-2}\right)$$

Nilai awal yang harus dikenali: $D_1 = 0$, $D_2 = 1$, $D_3 = 2$, $D_4 = 9$, $D_5 = 44$.

Untuk **tepat** $m$ objek yang tetap di tempatnya: pilih dulu $m$ yang tetap, lalu paksa
sisanya berpindah semua.

$$\binom{n}{m} D_{n-m}$$

## Jebakan umum

- **Mengurangkan sekali saja.** "Tidak ada yang tetap" bukan $n!$ dikurangi banyaknya
  susunan dengan satu titik tetap; susunan dengan dua titik tetap akan terhitung kacau.
- **Lupa memilih yang tetap.** Untuk tepat $m$ titik tetap, faktor $\binom{n}{m}$ tidak
  boleh hilang.
- **Menulis $D_1 = 1$.** Satu objek tidak punya tempat lain untuk dituju, jadi nilainya
  $0$ — dan salah di sini merusak seluruh rekursinya.
