---
id: uk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [uji-keterbagian]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Ada berapa digit $a$ sehingga bilangan empat digit $\overline{7a52}$ habis dibagi $12$?

## Petunjuk

- $12$ bukan prima. Pecah dulu jadi dua syarat yang lebih mudah diperiksa.
- $12 = 4 \times 3$, dan $\gcd(4,3) = 1$, jadi cukup periksa keterbagian oleh $4$ dan oleh $3$ secara terpisah.
- Keterbagian oleh $4$ hanya melihat dua digit terakhir; oleh $3$ melihat jumlah digitnya.

## Pembahasan

Karena $12 = 4 \times 3$ dengan $\gcd(4,3) = 1$, bilangan itu habis dibagi $12$ tepat
ketika habis dibagi $4$ **dan** habis dibagi $3$.

**Keterbagian oleh 4.** Hanya bergantung pada dua digit terakhir, yaitu $52$. Karena
$52 = 4 \times 13$, syarat ini selalu terpenuhi — tidak peduli berapa $a$.

**Keterbagian oleh 3.** Jumlah digitnya $7 + a + 5 + 2 = 14 + a$, dan syaratnya

$$14 + a \equiv 0 \pmod 3 \quad\Longrightarrow\quad a \equiv -14 \equiv 1 \pmod 3$$

Digit yang memenuhi: $a \in \{1, 4, 7\}$ — ada $\boxed{3}$ nilai.

Cek satu: $7152 = 12 \times 596$. Benar.

Perhatikan langkah pertamanya. Memecah $12$ jadi $4 \times 3$ hanya sah karena keduanya
relatif prima. Memecah $12$ jadi $6 \times 2$ akan salah — $6$ dan $2$ berbagi faktor,
dan syaratnya jadi terlalu longgar.
