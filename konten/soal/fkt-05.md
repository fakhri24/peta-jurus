---
id: fkt-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: isian
kesulitan: 2
jawaban: "2"
---

## Soal

Ada berapa akar real dari persamaan

$$x^4 - 1 = 0\ ?$$

## Petunjuk

- Perhatikan bahwa $x^4$ adalah kuadrat dari sesuatu, dan $1$ juga. Identitas mana yang cocok?
- $x^4 - 1 = \left(x^2\right)^2 - 1^2 = (x^2-1)(x^2+1)$.
- Faktor pertama masih bisa dipecah; faktor kedua tidak pernah bernilai nol untuk $x$ real.

## Pembahasan

Pakai selisih kuadrat, dengan $x^4 = \left(x^2\right)^2$:

$$x^4 - 1 = \left(x^2 - 1\right)\left(x^2 + 1\right)$$

Faktor pertama masih selisih kuadrat:

$$= (x-1)(x+1)\left(x^2+1\right)$$

Sekarang periksa tiap faktor.

- $x - 1 = 0$ memberi $x = 1$.
- $x + 1 = 0$ memberi $x = -1$.
- $x^2 + 1 = 0$ memberi $x^2 = -1$, yang **tidak punya solusi real** — kuadrat bilangan
  real tidak pernah negatif.

Jadi akar realnya $\boxed{2}$ buah, yaitu $1$ dan $-1$.

Perhatikan bahwa persamaan berderajat empat ini hanya punya dua akar real. Derajat memberi
**batas atas** banyaknya akar, bukan jaminan bahwa semuanya real. Dua akar sisanya adalah
$i$ dan $-i$ di ranah bilangan kompleks.

Kesalahan yang sering terjadi adalah berhenti di $(x^2-1)(x^2+1)$ lalu menyimpulkan
$x^2 = 1$ atau $x^2 = -1$ dan menghitung empat akar. Yang kedua harus diperiksa, bukan
diteruskan begitu saja.
