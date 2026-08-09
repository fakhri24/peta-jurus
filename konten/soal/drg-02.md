---
id: drg-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 3
jawaban: "265"
---

## Soal

Enam orang duduk di enam kursi bernomor sesuai nama mereka. Setelah istirahat, mereka duduk
kembali secara acak — satu orang per kursi.

Ada berapa cara duduk sehingga **tidak seorang pun** menempati kursinya semula?

## Petunjuk

- Ini persoalan baku dengan lambang tersendiri; yang dicari nilainya untuk enam objek.
- Rekurensnya menghubungkan nilai untuk $n$ dengan dua nilai sebelumnya, jadi hitung berurutan dari yang kecil.
- Periksa hasilnya dengan pendekatan $\frac{n!}{e}$.

## Pembahasan

Yang dicari adalah $D_6$.

**Hitung berurutan dengan rekurens** $D_n = (n-1)\left(D_{n-1}+D_{n-2}\right)$, mulai dari
$D_1 = 0$ dan $D_2 = 1$:

| $n$ | perhitungan | $D_n$ |
|---|---|---|
| $3$ | $2(1+0)$ | $2$ |
| $4$ | $3(2+1)$ | $9$ |
| $5$ | $4(9+2)$ | $44$ |
| $6$ | $5(44+9)$ | $\boxed{265}$ |

**Periksa dengan pendekatan.**

$$\frac{6!}{e} = \frac{720}{2{,}71828\ldots} \approx 264{,}87$$

Bilangan bulat terdekatnya $265$. Cocok.

**Periksa juga dengan rumus jumlah.**

$$D_6 = 720\left(1 - 1 + \tfrac12 - \tfrac16 + \tfrac1{24} - \tfrac1{120} + \tfrac1{720}\right)$$

Suku-suku di dalam kurung berjumlah $\frac{265}{720}$, sehingga hasilnya $265$.

**Mengapa rekurens biasanya lebih cepat di ujian.** Rumus jumlah menuntut menghitung tujuh
pecahan dengan penyebut berbeda lalu menjumlahkannya — pekerjaan yang mudah keliru. Rekurens
hanya menuntut penjumlahan dan perkalian bilangan bulat, dan tiap langkahnya memberi nilai
yang bisa dicocokkan dengan daftar yang sudah dihafal.

**Alasan bentuk rekurensnya**, sebagai gambaran singkat. Tinjau ke mana orang pertama duduk:
ada $n-1$ pilihan, sebab ia tidak boleh kembali ke kursinya sendiri. Misalkan ia duduk di
kursi $k$. Lalu tinjau orang ke-$k$:

- kalau ia duduk di kursi orang pertama, sisanya adalah persoalan yang sama pada $n-2$ orang;
- kalau tidak, kursi orang pertama menjadi "kursi terlarang" baginya, dan sisanya adalah
  persoalan yang sama pada $n-1$ orang.

Kedua kasus itu memberi $D_{n-2} + D_{n-1}$, dan faktor $n-1$ dari pilihan pertama tadi
melengkapinya. Pembuktian penuhnya ada di latihan terakhir jurus ini.
