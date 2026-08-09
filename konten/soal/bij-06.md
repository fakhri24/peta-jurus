---
id: bij-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: uraian
kesulitan: 4
---

## Soal

Buktikan bahwa banyaknya himpunan bagian dari $\{1,2,\dots,n\}$ yang **tidak memuat dua
bilangan berurutan** dan **beranggotakan tepat $k$ unsur** adalah

$$\binom{n-k+1}{k}$$

Buktikan dengan membangun padanan satu-satu, dan periksa padanan itu ke **dua arah**.

## Petunjuk

- Kalau anggotanya ditulis terurut naik, syarat "tidak berurutan" berarti selisih tiap dua anggota bertetangga paling sedikit $2$.
- Cari penggeseran yang mengubah syarat "selisih paling sedikit $2$" menjadi "selisih paling sedikit $1$", yaitu himpunan biasa.
- Untuk arah sebaliknya, tunjukkan penggeseran itu bisa dibalik dan hasilnya selalu memenuhi syarat asli.

## Pembahasan

**Tuliskan anggotanya terurut.** Ambil sebuah himpunan bagian yang memenuhi syarat, dan
tulis anggotanya

$$a_1 < a_2 < \cdots < a_k$$

Syarat "tidak memuat dua bilangan berurutan" berarti tidak ada dua anggota yang selisihnya
$1$, yaitu

$$a_{i+1} - a_i \ \ge\ 2 \qquad \text{untuk setiap } i$$

### Padanannya

Tetapkan

$$b_i = a_i - (i-1), \qquad i = 1,\dots,k$$

yaitu geser anggota ke-$i$ ke bawah sebanyak $i-1$.

**Periksa hasilnya himpunan biasa.** Selisih dua anggota bertetangga menjadi

$$b_{i+1} - b_i = \left(a_{i+1} - i\right) - \left(a_i - (i-1)\right) = a_{i+1} - a_i - 1 \ \ge\ 1$$

Jadi $b_1 < b_2 < \cdots < b_k$ — seluruhnya berbeda dan terurut naik, tanpa syarat
tambahan apa pun.

**Periksa jangkauannya.** Anggota terkecil: $b_1 = a_1 \ge 1$. Anggota terbesar:

$$b_k = a_k - (k-1) \le n - k + 1$$

Jadi $\left\{b_1,\dots,b_k\right\}$ adalah himpunan bagian berukuran $k$ dari
$\{1, 2, \dots, n-k+1\}$.

### Arah sebaliknya

Ambil sebarang himpunan bagian berukuran $k$ dari $\{1,\dots,n-k+1\}$, tulis anggotanya
terurut $b_1 < \cdots < b_k$, lalu tetapkan

$$a_i = b_i + (i-1)$$

**Periksa hasilnya memenuhi syarat asli.**

$$a_{i+1} - a_i = \left(b_{i+1} - b_i\right) + 1 \ \ge\ 1 + 1 = 2$$

sehingga tidak ada dua anggota yang berurutan. Anggota terbesarnya

$$a_k = b_k + (k-1) \le (n-k+1) + (k-1) = n$$

sehingga seluruh anggotanya berada di dalam $\{1,\dots,n\}$.

**Kedua arah saling meniadakan,** sebab menggeser turun lalu naik dengan besaran yang sama
mengembalikan bilangan semula. Jadi padanannya satu-satu dan pada.

### Simpulkan

Kedua himpunan sama banyaknya, dan sisi kanannya tinggal dicacah:

$$\binom{n-k+1}{k} \qquad \blacksquare$$

### Mengapa penggesernya $i-1$ dan bukan bilangan tetap

Yang harus dihapus adalah **kelebihan selisih**, dan kelebihan itu menumpuk: anggota kedua
membawa satu kelebihan, anggota ketiga membawa dua, dan seterusnya. Penggeser yang bertambah
seiring $i$ tepat menghapus tumpukan itu.

Menggeser dengan bilangan tetap tidak akan mengubah selisih antar-anggota sama sekali, jadi
syaratnya tidak berubah dan padanannya tidak menolong.

### Periksa dengan kasus kecil

Untuk $n = 5$, $k = 2$, rumusnya memberi $\binom42 = 6$. Daftarnya:

$$\{1,3\},\ \{1,4\},\ \{1,5\},\ \{2,4\},\ \{2,5\},\ \{3,5\}$$

Tepat $6$. Padanannya memetakan $\{2,5\}$ menjadi $\{2,4\}$, dan seterusnya.

## Rubrik

- Menuliskan anggota himpunan terurut dan menyatakan syaratnya sebagai $a_{i+1}-a_i \ge 2$
- Menetapkan penggeseran $b_i = a_i - (i-1)$
- Menghitung $b_{i+1}-b_i \ge 1$, sehingga hasilnya himpunan biasa
- Memeriksa jangkauannya, yaitu $b_k \le n-k+1$
- Arah sebaliknya: menetapkan $a_i = b_i + (i-1)$ dan memeriksa syarat aslinya terpenuhi
- Menyatakan kedua arah saling meniadakan, sehingga padanannya satu-satu dan pada
- Menyimpulkan jawabannya $\binom{n-k+1}{k}$
