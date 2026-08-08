---
id: ket-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: isian
kesulitan: 2
jawaban: "12"
---

## Soal

Tentukan jumlah semua bilangan bulat positif $n$ sehingga $n^2 + 2n + 7$ habis dibagi $n + 4$.

## Petunjuk

- Sama seperti sebelumnya: bagi bersusun sampai tersisa konstanta.
- $n^2 + 2n + 7 = (n+4)(n-2) + 15$.
- Syaratnya $n + 4 \mid 15$, dengan $n + 4 \ge 5$ karena $n$ positif.

## Pembahasan

$$n^2 + 2n + 7 = (n+4)(n-2) + 15$$

Jadi syaratnya $(n+4) \mid 15$. Pembagi positif $15$ adalah $1, 3, 5, 15$; yang bernilai
minimal $5$ hanya $5$ dan $15$.

- $n + 4 = 5 \Rightarrow n = 1$, dan $1 + 2 + 7 = 10 = 5 \cdot 2$. Benar.
- $n + 4 = 15 \Rightarrow n = 11$, dan $121 + 22 + 7 = 150 = 15 \cdot 10$. Benar.

Jumlahnya $1 + 11 = \boxed{12}$.
