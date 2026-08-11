---
id: bezout
nama: Identitas Bézout
pilar: teori-bilangan
tahap: osn-p
prasyarat: [algoritma-euklid]
contoh: [bz-contoh-1]
latihan: [bz-01, bz-02, bz-03, bz-04, bz-05, bz-06]
---

## Kapan dipakai

Kamu perlu **membuat** sebuah bilangan dari dua bilangan lain lewat penjumlahan
berkelipatan. Sering berbaju cerita: takaran air dengan dua ember, perangko dua nilai,
langkah maju dan mundur sepanjang lingkaran.

Pemicu kedua, dan ini yang membuatnya alat bukti: soal meminta membuktikan sesuatu **ada**
tanpa perlu menemukannya. "Tunjukkan ada bulat $x, y$ dengan …" dijawab dengan memeriksa
satu syarat keterbagian, bukan dengan mencari.

Pemicu ketiga: soal memuat **dua bilangan yang relatif prima** dan meminta kesimpulan
darinya. Di situ $\gcd = 1$, jadi setiap bilangan bulat bisa dibentuk — dan itu biasanya
langkah yang membuka sisanya.

Pemicu keempat: soal menuntut **invers modulo**. Mencari $a^{-1}$ modulo $m$ persis mencari
$x$ pada $ax + my = 1$, jadi keberadaannya dan cara menemukannya sama-sama dijawab di sini.

Bedakan dari Algoritma Euklid: yang di sana **menghitung** FPB, yang di sini menyatakan apa
yang bisa dibangun darinya. Euklid diperluas memberi keduanya sekaligus.

## Intinya

Untuk sembarang bulat $a, b$ tidak keduanya nol, ada bulat $x, y$ dengan

$$ax + by = \gcd(a, b)$$

Akibat pentingnya: $ax + by$ bisa bernilai $n$ untuk bulat $x, y$ **tepat ketika**
$\gcd(a,b) \mid n$. Jadi himpunan semua nilai yang bisa dibentuk persis himpunan kelipatan
FPB-nya — tidak lebih, tidak kurang.

Bentuk yang paling sering dipakai di olimpiade adalah kasus $\gcd(a,b) = 1$: ada $x, y$
dengan $ax + by = 1$. Dari sini lahir **invers modulo**: kalau $\gcd(a,m) = 1$, maka $x$
pada $ax + my = 1$ memenuhi $ax \equiv 1 \pmod m$ — dan itulah satu-satunya alasan
pembagian dalam kongruensi kadang boleh dilakukan.

Untuk mencari $x$ dan $y$ secara nyata, jalankan algoritma Euklid lalu telusuri balik.

## Jebakan umum

- **Mengira $x$ dan $y$ tunggal.** Tidak. Kalau $(x_0, y_0)$ satu solusi, maka
  $(x_0 + kb/d,\ y_0 - ka/d)$ juga, untuk setiap bulat $k$.
- **Mengira $x, y$ pasti positif.** Hampir selalu salah satunya negatif.
- **Memakainya untuk mencari solusi padahal soal hanya butuh keberadaan.** Bézout paling
  kuat justru sebagai alat eksistensi — sering kamu tidak perlu tahu $x$ dan $y$-nya sama
  sekali.
