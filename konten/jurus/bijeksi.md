---
id: bijeksi
nama: Bijeksi
pilar: kombinatorika
tahap: osn-p
prasyarat: [kombinasi, stars-and-bars]
contoh: [bij-contoh-1]
latihan: [bij-01, bij-02, bij-03, bij-04, bij-05, bij-06]
---

## Kapan dipakai

Himpunan yang harus dicacah terasa rumit, tapi kamu menduga jumlahnya sama dengan sesuatu
yang sudah kamu tahu cara menghitungnya. Pemicu yang sering: hasil hitungan tangan untuk
$n$ kecil ternyata $2^n$, $n!$, atau bilangan yang sudah kamu kenal.

Juga dipakai ketika soal memang meminta membuktikan dua himpunan **sama banyak**, tanpa
menghitung keduanya.

## Intinya

Buat padanan satu-satu antara himpunan yang ditanya dan himpunan yang sudah diketahui
jumlahnya. Kalau padanannya sah, kedua himpunan pasti sama banyak.

Supaya sah, padanan itu harus **satu-satu** dan **pada**: tidak ada dua anggota yang
dipetakan ke tempat yang sama, dan tidak ada anggota tujuan yang terlewat. Cara terpendek
membuktikan keduanya sekaligus adalah **menunjukkan cara membalikkannya** — tulis
padanannya, tulis kebalikannya, lalu tunjukkan keduanya saling meniadakan.

Padanan baku yang sering dipakai kembali:

- Himpunan bagian dari $n$ unsur ↔ barisan $0$ dan $1$ sepanjang $n$, memberi $2^{n}$.
- Penyelesaian $x_1 + \cdots + x_k = n$ ↔ susunan bintang dan sekat.
- Jalur pada kisi dari satu pojok ke pojok lain ↔ pemilihan langkah mana yang ke kanan.

**Bijeksi juga alat pembuktian, bukan cuma alat hitung.** Banyak identitas koefisien
binomial paling jelas dibuktikan dengan memasangkan objek kedua sisi.

## Jebakan umum

- **Memberi padanan tanpa memeriksa kebalikannya.** Aturan yang terdengar wajar bisa saja
  memetakan dua objek berbeda ke tempat yang sama.
- **Padanan yang bocor.** Kalau ada anggota tujuan yang tidak pernah tercapai, yang kamu
  buktikan cuma "tidak lebih banyak", bukan "sama banyak".
- **Berpindah ke himpunan yang sama sulitnya.** Padanan hanya berguna kalau sisi tujuannya
  benar-benar sudah bisa dihitung.
