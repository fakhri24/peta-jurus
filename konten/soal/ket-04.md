---
id: ket-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: isian
kesulitan: 3
jawaban: "5"
---

## Soal

Ada berapa pasangan bilangan bulat positif $(a, b)$ dengan $a \le b$ yang memenuhi

$$\frac{1}{a} + \frac{1}{b} = \frac{1}{6}\ ?$$

## Petunjuk

- Hilangkan pecahannya dulu. Kalikan kedua ruas dengan $6ab$.
- Kamu akan sampai di $ab - 6a - 6b = 0$. Ruas kiri hampir bisa difaktorkan — tambahkan sesuatu ke kedua ruas supaya jadi bisa.
- Tambahkan $36$: $(a-6)(b-6) = 36$. Sekarang tinggal mencacah pasangan pembagi $36$.

## Pembahasan

Kalikan dengan $6ab$:

$$6b + 6a = ab \quad\Longrightarrow\quad ab - 6a - 6b = 0$$

Tambahkan $36$ ke kedua ruas supaya ruas kiri bisa difaktorkan:

$$ab - 6a - 6b + 36 = 36 \quad\Longrightarrow\quad (a-6)(b-6) = 36$$

Karena $\frac{1}{a} < \frac{1}{6}$, pastilah $a > 6$, jadi $a - 6$ dan $b - 6$ keduanya
bulat positif. Dengan syarat $a \le b$, pasangan pembagi $36$ yang memenuhi $d \le e$ dan
$de = 36$ ada lima:

$$(1,36),\ (2,18),\ (3,12),\ (4,9),\ (6,6)$$

memberi $(a,b) = (7,42), (8,24), (9,18), (10,15), (12,12)$ — ada $\boxed{5}$ pasangan.

Trik menambahkan konstanta agar bisa difaktorkan ini sering disebut *pemfaktoran
Simon*. Begitu kamu melihat $xy + px + qy$, refleks pertamanya adalah menambahkan $pq$.
