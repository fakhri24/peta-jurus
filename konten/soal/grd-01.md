---
id: grd-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: isian
kesulitan: 1
jawaban: "45"
---

## Soal

Dalam sebuah turnamen, $10$ tim bertanding dengan sistem setengah kompetisi — setiap tim
bertanding melawan setiap tim lainnya **tepat sekali**.

Ada berapa pertandingan seluruhnya?

## Petunjuk

- Gambarkan sebagai graf: tim menjadi titik, pertandingan menjadi ruas antara dua tim.
- Sebuah pertandingan ditentukan oleh pasangan tim, dan menukar urutan kedua tim tidak menghasilkan pertandingan yang berbeda.
- Boleh juga lewat derajat: tiap tim bermain melawan berapa tim lain?

## Pembahasan

**Cara pertama — cacah pasangannya.** Sebuah pertandingan ditentukan oleh pasangan tim, dan
pasangan $\{A, B\}$ sama dengan $\{B, A\}$:

$$\binom{10}{2} = \frac{10 \times 9}{2} = \boxed{45}$$

**Cara kedua — lewat derajat.** Tiap tim bertanding melawan $9$ tim lainnya, sehingga
grafnya punya $10$ titik masing-masing berderajat $9$:

$$\sum_v \deg(v) = 10 \times 9 = 90 = 2|E| \quad\Longrightarrow\quad |E| = 45$$

Kedua cara bertemu, sebagaimana seharusnya — graf ini adalah **graf lengkap** $K_{10}$,
yaitu graf yang setiap dua titiknya terhubung.

**Rumus umumnya.** Graf lengkap $K_n$ punya

$$\binom{n}{2} = \frac{n(n-1)}{2}$$

ruas, dan tiap titiknya berderajat $n-1$.

**Perhatikan pembagian $2$ pada kedua cara punya alasan yang sama.** Pada cara pertama ia
menghapus urutan pasangan; pada cara kedua ia memperbaiki penghitungan ganda tiap ruas. Itu
bukan kebetulan — keduanya kenyataan yang sama, dilihat dari dua sisi.

**Bandingkan dengan kompetisi penuh** (setiap dua tim bertanding **dua** kali, kandang dan
tandang). Di situ pasangan terurut yang dihitung, sehingga jawabannya

$$10 \times 9 = 90$$

Satu kata pada soal — "tepat sekali" atau "dua kali" — melipatgandakan jawabannya.

**Untuk turnamen sistem gugur** hitungannya berbeda sama sekali dan jauh lebih pendek: tiap
pertandingan menyingkirkan tepat satu tim, dan pada akhirnya $9$ tim tersingkir, sehingga
pertandingannya $9$. Cara pandang "hitung apa yang dihabiskan tiap langkah" itu sering
memangkas soal turnamen menjadi satu baris.
