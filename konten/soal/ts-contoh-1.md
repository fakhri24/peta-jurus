---
id: ts-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [tau-sigma]
bentuk: isian
kesulitan: 2
jawaban: "16"
---

## Soal

Ada berapa faktor positif dari $2024$?

## Petunjuk

- Faktorkan $2024$ menjadi perkalian bilangan prima lebih dulu.
- $2024 = 8 \times 253$, dan $253$ masih bisa dipecah.
- $253 = 11 \times 23$. Sekarang pakai rumus $\tau$.

## Pembahasan

Faktorkan lebih dulu:

$$2024 = 8 \times 253 = 2^3 \times 11 \times 23$$

($253$ habis dibagi $11$ karena $2 - 5 + 3 = 0$.)

Setiap faktor positif dibentuk dengan memilih pangkat masing-masing prima secara bebas:

- pangkat $2$: boleh $0, 1, 2, 3$ — ada $4$ pilihan
- pangkat $11$: boleh $0, 1$ — ada $2$ pilihan
- pangkat $23$: boleh $0, 1$ — ada $2$ pilihan

$$\tau(2024) = 4 \times 2 \times 2 = \boxed{16}$$

Kesalahan yang paling sering: memakai pangkatnya langsung, yaitu $3 \times 1 \times 1$.
Yang benar selalu **pangkat ditambah satu**, karena pangkat $0$ juga sebuah pilihan yang
sah.
