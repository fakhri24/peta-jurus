---
id: bij-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 4
jawaban: "42"
---

## Soal

Dalam sebuah pemungutan suara, calon $A$ dan calon $B$ masing-masing memperoleh tepat $5$
suara. Surat suara dihitung satu per satu.

Ada berapa urutan penghitungan sehingga **sepanjang penghitungan** perolehan $A$ tidak
pernah tertinggal dari $B$?

## Petunjuk

- Catat urutan penghitungan sebagai barisan huruf A dan B sepanjang sepuluh, lalu nyatakan syaratnya dalam bahasa barisan itu.
- Syaratnya: pada setiap awalan barisan, banyaknya A tidak kurang dari banyaknya B.
- Hitung seluruh barisan lebih dulu, lalu cari cara memasangkan barisan yang melanggar dengan sesuatu yang mudah dihitung.

## Pembahasan

**Ubah menjadi barisan.** Catat penghitungan sebagai barisan sepanjang $10$ yang memuat $5$
huruf A dan $5$ huruf B. Syaratnya menjadi: **pada setiap awalan, banyaknya A tidak kurang
dari banyaknya B.**

**Seluruh barisan tanpa syarat.**

$$\binom{10}{5} = 252$$

**Pasangkan barisan yang melanggar.** Sebuah barisan melanggar kalau pada suatu saat B
melampaui A. Ambil saat **pertama** hal itu terjadi — pada posisi itu, banyaknya B tepat satu
lebih banyak daripada A.

Sekarang balikkan setiap huruf **sesudah** posisi itu: tiap A menjadi B dan tiap B menjadi A.

Sebelum pembalikan, barisan itu punya $5$ A dan $5$ B. Misalkan sampai posisi pelanggaran
pertama ada $a$ huruf A dan $a+1$ huruf B. Sesudahnya ada $5-a$ huruf A dan $4-a$ huruf B,
dan pembalikan menukar keduanya. Barisan barunya memuat

$$a + (4-a) = 4 \text{ huruf A}, \qquad (a+1) + (5-a) = 6 \text{ huruf B}$$

**Periksa padanannya sah.** Dari sebarang barisan berisi $4$ A dan $6$ B, banyaknya B
melebihi A, jadi pasti ada saat pertama B melampaui A. Balikkan sesudah saat itu, dan
diperoleh kembali barisan berisi $5$ A dan $5$ B yang melanggar. Kedua arah saling
meniadakan, sehingga padanannya satu-satu dan pada.

Maka banyaknya barisan yang melanggar sama dengan

$$\binom{10}{4} = 210$$

**Kurangkan.**

$$252 - 210 = \boxed{42}$$

**Bentuk umumnya** untuk $n$ suara masing-masing:

$$\binom{2n}{n} - \binom{2n}{n-1} = \frac{1}{n+1}\binom{2n}{n}$$

yaitu **bilangan Catalan** ke-$n$. Untuk $n = 5$:

$$\frac{1}{6}\binom{10}{5} = \frac{252}{6} = 42$$

Cocok.

**Yang membuat soal ini berharga** adalah bentuk padanannya. Ia tidak memasangkan objek
yang dicari dengan sesuatu yang mudah — melainkan memasangkan objek yang **melanggar**
dengan sesuatu yang mudah. Cara pembalikan seperti ini muncul berulang kali di soal jalur
dan barisan, dan ia yang melahirkan bilangan Catalan.

Bilangan Catalan $1, 2, 5, 14, 42, 132, \dots$ juga mencacah hal-hal yang tampak jauh
berbeda: susunan tanda kurung yang sah, cara membagi segi banyak menjadi segitiga, dan jalur
kisi yang tidak melewati diagonal. Semuanya berpadanan satu sama lain.
