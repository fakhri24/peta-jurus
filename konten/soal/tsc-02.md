---
id: tsc-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: isian
kesulitan: 2
jawaban: "346"
---

## Soal

Tentukan bilangan asli terkecil yang bersisa $3$ jika dibagi $7$, bersisa $4$ jika dibagi
$9$, dan bersisa $5$ jika dibagi $11$.

## Petunjuk

- Modulusnya saling relatif prima berpasangan, jadi solusinya tunggal modulo $7 \times 9 \times 11 = 693$.
- Mulai dari modulus terbesar: tulis $x = 11t + 5$, lalu masukkan ke syarat modulo $9$.
- Kerjakan dua kongruensi dulu sampai tuntas, baru masukkan yang ketiga. Mengerjakan ketiganya sekaligus mudah tersesat.

## Pembahasan

Modulus $7$, $9$, $11$ saling relatif prima berpasangan, jadi solusinya tunggal modulo

$$M = 7 \times 9 \times 11 = 693$$

**Langkah 1: gabungkan modulo $11$ dan modulo $9$.** Dari $x \equiv 5 \pmod{11}$, tulis

$$x = 11t + 5$$

Masukkan ke $x \equiv 4 \pmod 9$:

$$11t + 5 \equiv 4 \pmod 9 \quad\Longrightarrow\quad 2t \equiv -1 \equiv 8 \pmod 9$$

sebab $11 \equiv 2 \pmod 9$. Invers $2$ modulo $9$ adalah $5$, karena
$2 \times 5 = 10 \equiv 1$. Maka

$$t \equiv 5 \times 8 = 40 \equiv 4 \pmod 9 \quad\Longrightarrow\quad t = 9s + 4$$

Substitusikan kembali:

$$x = 11(9s + 4) + 5 = 99s + 49$$

**Langkah 2: masukkan syarat modulo $7$.** Dituntut $x \equiv 3 \pmod 7$:

$$99s + 49 \equiv 3 \pmod 7$$

Karena $99 = 14 \times 7 + 1$ sehingga $99 \equiv 1$, dan $49 \equiv 0 \pmod 7$:

$$s \equiv 3 \pmod 7 \quad\Longrightarrow\quad s = 7u + 3$$

Substitusikan kembali:

$$x = 99(7u + 3) + 49 = 693u + 297 + 49 = 693u + 346$$

Bilangan asli terkecilnya adalah $\boxed{346}$.

Periksa ketiganya: $346 = 7 \times 49 + 3$, $346 = 9 \times 38 + 4$, dan
$346 = 11 \times 31 + 5$. Semuanya cocok.

Perhatikan bahwa $9$ dan $11$ tidak prima maupun berpangkat prima yang sama — yang
dibutuhkan Teorema Sisa Cina hanyalah **saling relatif prima berpasangan**, bukan prima.
Kalau salah satu modulus diganti $21$, syarat itu gugur terhadap $7$ dan teoremanya tidak
lagi berlaku begitu saja.
