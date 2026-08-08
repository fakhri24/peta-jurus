---
id: tsc-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: isian
kesulitan: 2
jawaban: "23"
---

## Soal

Tentukan bilangan asli terkecil yang bersisa $2$ jika dibagi $3$, bersisa $3$ jika dibagi
$5$, dan bersisa $2$ jika dibagi $7$.

## Petunjuk

- Tiga syarat sisa sekaligus, dengan modulus yang saling relatif prima — solusinya tunggal modulo hasil kalinya.
- Tidak perlu rumus. Mulai dari modulus terbesar: tulis $x = 7t + 2$, lalu masukkan ke syarat berikutnya.
- Setelah $t$ terkurung oleh syarat modulo $5$, tulis ulang $x$ dan masukkan ke syarat modulo $3$.

## Pembahasan

Modulusnya $3$, $5$, $7$ — saling relatif prima berpasangan, jadi menurut Teorema Sisa
Cina solusinya tunggal modulo $3 \times 5 \times 7 = 105$.

**Mulai dari modulus terbesar.** Dari $x \equiv 2 \pmod 7$, tulis

$$x = 7t + 2$$

**Masukkan ke syarat modulo $5$.** Dituntut $x \equiv 3 \pmod 5$:

$$7t + 2 \equiv 3 \pmod 5 \quad\Longrightarrow\quad 2t \equiv 1 \pmod 5$$

sebab $7 \equiv 2 \pmod 5$. Invers $2$ modulo $5$ adalah $3$, jadi

$$t \equiv 3 \pmod 5 \quad\Longrightarrow\quad t = 5s + 3$$

Substitusikan kembali:

$$x = 7(5s + 3) + 2 = 35s + 23$$

**Masukkan ke syarat modulo $3$.** Dituntut $x \equiv 2 \pmod 3$:

$$35s + 23 \equiv 2 \pmod 3$$

Karena $35 \equiv 2$ dan $23 \equiv 2 \pmod 3$:

$$2s + 2 \equiv 2 \pmod 3 \quad\Longrightarrow\quad 2s \equiv 0 \pmod 3
\quad\Longrightarrow\quad s \equiv 0 \pmod 3$$

Tulis $s = 3u$, sehingga

$$x = 35(3u) + 23 = 105u + 23$$

Bilangan asli terkecilnya diperoleh pada $u = 0$, yaitu $x = \boxed{23}$.

Periksa: $23 = 3 \times 7 + 2$, $23 = 5 \times 4 + 3$, $23 = 7 \times 3 + 2$. Ketiganya
cocok.

Perhatikan bahwa jawabannya berbentuk $105u + 23$ — solusinya tunggal **modulo $105$**,
bukan tunggal secara mutlak. Memulai dari modulus terbesar membuat angka yang dibawa tetap
kecil di setiap langkah.
