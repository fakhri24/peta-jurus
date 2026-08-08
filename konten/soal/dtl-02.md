---
id: dtl-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 2
jawaban: "8"
---

## Soal

Ada berapa pasangan bilangan asli $(x, y)$ dengan $x \le y$ yang memenuhi

$$\frac{1}{x} + \frac{1}{y} = \frac{1}{12}\ ?$$

## Petunjuk

- Hilangkan pecahannya lebih dulu dengan mengalikan kedua ruas dengan $12xy$.
- Kamu akan sampai di $xy - 12x - 12y = 0$. Tambahkan konstanta yang tepat supaya bisa difaktorkan.
- Setelah menjadi $(x-12)(y-12) = 144$, tunjukkan kedua faktornya harus positif, lalu cacah pasangan pembagi $144$ dengan $d \le e$.

## Pembahasan

Kalikan kedua ruas dengan $12xy$:

$$12y + 12x = xy \quad\Longrightarrow\quad xy - 12x - 12y = 0$$

Tambahkan $144$ ke kedua ruas agar ruas kiri bisa difaktorkan:

$$xy - 12x - 12y + 144 = 144 \quad\Longrightarrow\quad (x-12)(y-12) = 144$$

**Kedua faktornya positif.** Karena $\frac1x < \frac1{12}$, pastilah $x > 12$; begitu pula
$y > 12$. Jadi $x - 12$ dan $y - 12$ keduanya bilangan asli.

**Cacah pasangan pembagi.** Yang diminta $x \le y$, jadi pasangan $(d,e)$ dengan
$de = 144$ dan $d \le e$. Karena

$$144 = 2^4 \times 3^2 \quad\Longrightarrow\quad \tau(144) = 5 \times 3 = 15$$

banyaknya pasangan dengan $d \le e$ adalah $\frac{15 + 1}{2} = 8$ — pembagi berpasangan
dua-dua, dan $144 = 12^2$ menyisakan satu pasangan berimpit $(12,12)$.

Daftarnya:

$$(1,144),\ (2,72),\ (3,48),\ (4,36),\ (6,24),\ (8,18),\ (9,16),\ (12,12)$$

memberi

$$(x,y) = (13,156),\ (14,84),\ (15,60),\ (16,48),\ (18,36),\ (20,30),\ (21,28),\ (24,24)$$

Ada $\boxed{8}$ pasangan.

Langkah "tunjukkan $x > 12$" itu bukan basa-basi. Tanpanya, pembagi negatif $144$ ikut
terhitung dan cacahnya melonjak — padahal semuanya memberi $x$ atau $y$ tak positif.
