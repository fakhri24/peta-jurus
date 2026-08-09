---
id: rek-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebut $t_n$ banyaknya cara menutup papan $2 \times n$ dengan domino $1 \times 2$.

1. Buktikan bahwa $t_n = t_{n-1} + t_{n-2}$ untuk $n \ge 3$, dengan memeriksa bahwa
   pemecahan kasusnya **lepas** dan **lengkap**.
2. Tebak rumus untuk $t_1 + t_2 + \cdots + t_n$ dari beberapa suku pertama, lalu buktikan
   tebakan itu dengan induksi.

## Petunjuk

- Untuk bagian 1, perhatikan petak kanan atas: ia harus ditutup, dan bentuk dominonya hanya punya dua kemungkinan.
- Kalau dominonya mendatar, tunjukkan petak kanan bawah **tidak punya pilihan** — di situlah letak "lepas"-nya.
- Untuk bagian 2, hitung $t_1, t_1+t_2, t_1+t_2+t_3, \dots$ dan bandingkan tiap hasilnya dengan suku barisan yang sudah kamu punya.

## Pembahasan

### Bagian 1 — rekurensnya

Tinjau petak di **pojok kanan atas**. Ia harus ditutup oleh sebuah domino, dan domino itu
hanya bisa tegak atau mendatar — tidak ada bentuk lain.

**Kasus A — dominonya tegak.** Ia menutupi kedua petak pada kolom terakhir. Sisa papan
adalah $2 \times (n-1)$ yang utuh, dan penutupannya bebas sepenuhnya. Menyumbang $t_{n-1}$.

**Kasus B — dominonya mendatar.** Ia menutupi petak kanan atas beserta tetangga kirinya.
Sekarang tinjau petak kanan bawah:

- Ia tidak bisa ditutup domino tegak, sebab petak di atasnya sudah terpakai.
- Ia tidak bisa ditutup domino mendatar yang menjulur ke kanan, sebab sudah di tepi papan.

Maka ia **terpaksa** ditutup domino mendatar yang menjulur ke kiri. Kedua domino itu
bersama-sama menutupi dua kolom terakhir seluruhnya, dan sisanya papan $2 \times (n-2)$ yang
utuh. Menyumbang $t_{n-2}$.

**Lepas.** Sebuah penutupan tidak mungkin masuk kedua kasus, sebab domino yang menutupi
petak kanan atas hanya satu, dan ia entah tegak entah mendatar.

**Lengkap.** Setiap penutupan pasti menutupi petak kanan atas, sehingga pasti masuk salah
satu kasus.

Karena lepas dan lengkap, aturan jumlah berlaku:

$$t_n = t_{n-1} + t_{n-2} \qquad \blacksquare$$

Perhatikan langkah "terpaksa" pada Kasus B. Tanpanya, penutupan yang sama akan terhitung
lebih dari sekali, dan rekurensnya salah.

### Bagian 2 — jumlah parsialnya

Dengan $t_1 = 1$ dan $t_2 = 2$:

$$t_1, t_2, t_3, \dots = 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ \dots$$

Hitung jumlah parsialnya dan bandingkan dengan barisan aslinya:

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $S_n = t_1 + \cdots + t_n$ | $1$ | $3$ | $6$ | $11$ | $19$ |
| $t_{n+2}$ | $3$ | $5$ | $8$ | $13$ | $21$ |

Selisihnya selalu $2$. Tebakan:

$$S_n = t_{n+2} - 2$$

**Buktikan dengan induksi.**

*Basis.* Untuk $n = 1$: $S_1 = 1$ dan $t_3 - 2 = 3 - 2 = 1$. Cocok.

*Langkah.* Andaikan $S_k = t_{k+2} - 2$ untuk suatu $k \ge 1$. Maka

$$S_{k+1} = S_k + t_{k+1} = \left(t_{k+2} - 2\right) + t_{k+1}$$

Menurut rekurensnya, $t_{k+1} + t_{k+2} = t_{k+3}$, sehingga

$$S_{k+1} = t_{k+3} - 2$$

yaitu pernyataan yang sama untuk $k+1$.

Menurut induksi, $S_n = t_{n+2} - 2$ berlaku untuk setiap $n \ge 1$. $\blacksquare$

### Mengapa tebakannya harus dibuktikan

Kecocokan pada lima suku pertama bukan bukti. Barisan yang sepakat di sepuluh suku pertama
lalu berpisah mudah dibuat, dan pada soal olimpiade pola yang menipu memang sengaja
dipasang.

Yang mengubah tebakan menjadi bukti adalah induksi — dan langkah induksinya di sini bekerja
justru karena rekurens dari bagian 1 sudah tersedia untuk dipakai.

## Rubrik

- Menyatakan petak kanan atas harus ditutup, dan dominonya hanya bisa tegak atau mendatar
- Kasus tegak: menyimpulkan sisanya papan $2\times(n-1)$ utuh
- Kasus mendatar: menunjukkan petak kanan bawah **terpaksa** ditutup domino mendatar, dengan alasan kedua kemungkinan lain tertutup
- Menyatakan kedua kasus lepas, dengan alasan domino penutup petak kanan atas hanya satu
- Menyatakan kedua kasus lengkap, dengan alasan tiap penutupan pasti menutupi petak itu
- Bagian 2: menghitung beberapa jumlah parsial dan menuliskan tebakan $S_n = t_{n+2} - 2$
- Bagian 2: membuktikan tebakan dengan induksi, memakai rekurens pada langkah induksinya
