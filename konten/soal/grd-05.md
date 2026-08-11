---
id: grd-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: uraian
kesulitan: 4
---

## Soal

Buktikan bahwa dalam sebuah kelompok yang beranggotakan paling sedikit dua orang, selalu ada
**dua orang yang banyaknya kenalan sama** di dalam kelompok itu.

(Perkenalan bersifat timbal balik.)

## Petunjuk

- Bandingkan dua hitungan: ada berapa orang, dan ada berapa nilai berbeda yang mungkin bagi banyaknya kenalan seseorang.
- Gambarkan sebagai graf dan nyatakan lewat derajat. Untuk $n$ titik, derajat hanya bisa bernilai $0$ sampai $n-1$ — sama banyak dengan titiknya.
- Angkanya ternyata pas — dan pas berarti prinsipnya belum menggigit. Tunjukkan dua nilai ekstrem tidak bisa muncul bersamaan.

## Pembahasan

Buat graf dengan $n \ge 2$ titik, satu untuk tiap orang, dan pasang ruas di antara dua titik
tepat ketika keduanya saling kenal. Yang harus dibuktikan: **ada dua titik yang derajatnya
sama.**

### Langkah 1 — daftar nilai derajat yang mungkin

Derajat sebuah titik paling sedikit $0$ — tidak kenal siapa pun — dan paling banyak $n-1$ —
kenal semua orang lain. Jadi nilainya berasal dari

$$\{0, 1, 2, \dots, n-1\}$$

yaitu $n$ nilai untuk $n$ titik.

**Prinsip sarang merpati belum menggigit di sini.** Merpatinya $n$, sarangnya juga $n$ —
sehingga masih mungkin tiap titik menempati nilai yang berbeda. Dibutuhkan satu langkah
lagi.

### Langkah 2 — dua nilai ekstrem tidak bisa muncul bersamaan

Andaikan ada titik berderajat $0$ **dan** titik berderajat $n-1$, sebut keduanya $u$ dan
$w$.

- $\deg(w) = n-1$ berarti $w$ terhubung ke **semua** titik lain, termasuk $u$.
- $\deg(u) = 0$ berarti $u$ tidak terhubung ke titik mana pun, termasuk $w$.

Kedua pernyataan itu bertentangan. Maka **paling banyak satu** di antara nilai $0$ dan $n-1$
benar-benar muncul.

### Langkah 3 — terapkan prinsip sarang merpati

Karena salah satu dari kedua nilai ekstrem itu pasti tidak terpakai, nilai derajat yang
benar-benar mungkin paling banyak

$$n - 1$$

Sementara titiknya ada $n$. Karena $n > n-1$, ada dua titik yang derajatnya sama.
$\blacksquare$

### Mengapa langkah 2 adalah inti seluruh bukti

Tanpa langkah itu, sarangnya sebanyak merpatinya dan tidak ada yang bisa disimpulkan. Yang
dikerjakan langkah 2 adalah **memperkecil sarangnya** — dan itulah pola yang berulang di
banyak soal sarang merpati: prinsipnya sendiri satu baris, sedangkan pekerjaan sesungguhnya
adalah menunjukkan sarangnya lebih sedikit daripada yang terlihat.

### Periksa pada kasus kecil

Untuk $n = 2$: derajat yang mungkin $\{0,1\}$, tetapi keduanya tidak bisa muncul bersamaan.
Jadi kedua orang berderajat $0$ (tidak saling kenal) atau keduanya berderajat $1$ (saling
kenal). Bagaimanapun, keduanya sama.

Untuk $n = 3$: kalau seseorang kenal kedua orang lain, tidak ada yang berderajat $0$,
sehingga derajat yang mungkin tinggal $\{1,2\}$ untuk tiga orang — pasti ada yang sama.

### Syarat $n \ge 2$

Untuk $n = 1$ pernyataannya tidak berlaku, sebab tidak ada dua orang untuk dibandingkan.
Menyebutkan syarat ini bagian dari menuliskan buktinya dengan lengkap.

## Rubrik

- Menerjemahkan ke graf dan menyatakan yang dibuktikan sebagai "ada dua titik berderajat sama"
- Menyatakan derajat yang mungkin adalah $0$ sampai $n-1$, yaitu $n$ nilai
- Menyadari prinsip sarang merpati belum menggigit karena sarangnya sebanyak merpatinya
- Mengandaikan derajat $0$ dan $n-1$ muncul bersamaan, lalu menurunkan pertentangannya
- Menyimpulkan nilai derajat yang terpakai paling banyak $n-1$
- Menerapkan prinsip sarang merpati dengan $n$ titik pada paling banyak $n-1$ nilai
