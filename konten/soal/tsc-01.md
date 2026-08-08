---
id: tsc-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: isian
kesulitan: 1
jawaban: "17"
---

## Soal

Tentukan bilangan asli terkecil yang bersisa $1$ jika dibagi $4$ dan bersisa $2$ jika
dibagi $5$.

## Petunjuk

- Dua syarat, dan modulusnya relatif prima. Solusinya tunggal modulo $20$.
- Tulis $x = 5t + 2$ dari syarat kedua, lalu masukkan ke syarat pertama.
- Untuk sistem sekecil ini, mendaftar bilangan yang bersisa $2$ dibagi $5$ lalu memeriksanya juga cukup cepat.

## Pembahasan

Karena $\gcd(4,5) = 1$, solusinya tunggal modulo $4 \times 5 = 20$.

**Cara substitusi.** Dari $x \equiv 2 \pmod 5$, tulis

$$x = 5t + 2$$

Masukkan ke $x \equiv 1 \pmod 4$:

$$5t + 2 \equiv 1 \pmod 4 \quad\Longrightarrow\quad t + 2 \equiv 1 \pmod 4$$

sebab $5 \equiv 1 \pmod 4$. Maka

$$t \equiv -1 \equiv 3 \pmod 4 \quad\Longrightarrow\quad t = 4s + 3$$

Substitusikan kembali:

$$x = 5(4s + 3) + 2 = 20s + 17$$

Bilangan asli terkecilnya adalah $\boxed{17}$.

**Cara mendaftar.** Bilangan yang bersisa $2$ dibagi $5$: $2, 7, 12, 17, 22, \ldots$
Sisanya dibagi $4$ berturut-turut $2, 3, 0, 1, 2, \ldots$ — yang pertama memberi $1$
adalah $17$.

Periksa: $17 = 4 \times 4 + 1$ dan $17 = 5 \times 3 + 2$. Cocok.

Untuk sistem dua kongruensi dengan modulus kecil, mendaftar sering lebih cepat daripada
substitusi. Yang perlu dijaga hanya satu: daftarnya dimulai dari modulus **terbesar**,
supaya langkahnya paling sedikit.
