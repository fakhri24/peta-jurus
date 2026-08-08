---
id: dtl-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 2
jawaban: "4"
---

## Soal

Ada berapa pasangan bilangan asli $(x, y)$ yang memenuhi

$$xy + 2x + 3y = 30\ ?$$

## Petunjuk

- Ruas kirinya hampir bisa difaktorkan. Yang kurang hanyalah sebuah konstanta.
- Untuk $xy + ax + by$, tambahkan $ab$ ke kedua ruas: di sini tambahkan $6$.
- Setelah menjadi $(x+3)(y+2) = 36$, ingat bahwa $x \ge 1$ dan $y \ge 1$ membatasi kedua faktornya.

## Pembahasan

Ruas kiri hampir berbentuk hasil kali. Tambahkan $2 \times 3 = 6$ ke kedua ruas:

$$xy + 2x + 3y + 6 = 36$$

Sekarang ruas kiri bisa difaktorkan:

$$(x + 3)(y + 2) = 36$$

Inilah *pemfaktoran Simon*: pada $xy + ax + by$, tambahan yang tepat selalu $ab$.

**Pasang batasnya.** Karena $x \ge 1$ maka $x + 3 \ge 4$; karena $y \ge 1$ maka
$y + 2 \ge 3$.

Daftar pembagi $36$ sebagai nilai $x+3$, lalu periksa syaratnya:

| $x+3$ | $y+2$ | $x$ | $y$ | memenuhi? |
|---|---|---|---|---|
| $4$ | $9$ | $1$ | $7$ | ya |
| $6$ | $6$ | $3$ | $4$ | ya |
| $9$ | $4$ | $6$ | $2$ | ya |
| $12$ | $3$ | $9$ | $1$ | ya |
| $18$ | $2$ | $15$ | $0$ | tidak, $y = 0$ |
| $36$ | $1$ | $33$ | $-1$ | tidak |

Pembagi $1, 2, 3$ juga gugur karena memberi $x + 3 < 4$.

Ada $\boxed{4}$ pasangan: $(1,7)$, $(3,4)$, $(6,2)$, $(9,1)$.

Periksa satu: $3 \times 4 + 2 \times 3 + 3 \times 4 = 12 + 6 + 12 = 30$. Benar.

Perhatikan bahwa konstanta yang ditambahkan adalah hasil kali koefisien $x$ dan $y$
**bersilang**: koefisien $x$ adalah $2$ dan ia menjadi bagian dari $(y+2)$, sedangkan
koefisien $y$ adalah $3$ dan ia menjadi $(x+3)$. Tertukar sedikit saja, pemfaktorannya
gagal.
