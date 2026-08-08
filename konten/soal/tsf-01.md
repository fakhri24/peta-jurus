---
id: tsf-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor]
bentuk: isian
kesulitan: 1
jawaban: "-6"
---

## Soal

Tentukan sisa pembagian $x^2 + 3x - 4$ oleh $(x + 2)$.

## Petunjuk

- Sisa pembagian oleh bentuk linear diperoleh dengan satu substitusi.
- Perhatikan tandanya: pembaginya $(x+2)$, jadi tulis ulang sebagai $\left(x - (-2)\right)$.
- Sisanya adalah $P(-2)$, bukan $P(2)$.

## Pembahasan

Tulis ulang pembaginya supaya bentuknya jelas:

$$x + 2 = x - (-2)$$

jadi $a = -2$. Menurut teorema sisa, sisanya adalah $P(-2)$:

$$P(-2) = (-2)^2 + 3(-2) - 4 = 4 - 6 - 4 = \boxed{-6}$$

Periksa: $x^2+3x-4 = (x+2)(x+1) - 6$. Jabarkan ruas kanan: $x^2+3x+2-6 = x^2+3x-4$. Cocok.

**Tanda itu yang paling sering meleset.** Kalau dihitung $P(2) = 4 + 6 - 4 = 6$, jawabannya
salah tanda **dan** salah nilai. Kebiasaan yang menyelamatkan: tulis ulang pembaginya
menjadi bentuk $(x - a)$ lebih dulu, lalu baca $a$ dari situ.

Beberapa contoh pembacaan:

| Pembagi | Bentuk $(x-a)$ | Sisanya |
|---|---|---|
| $x - 3$ | $x - 3$ | $P(3)$ |
| $x + 5$ | $x - (-5)$ | $P(-5)$ |
| $2x - 1$ | $2\left(x - \tfrac12\right)$ | $P\!\left(\tfrac12\right)$ |
| $x$ | $x - 0$ | $P(0)$ |

Baris terakhir layak diingat: sisa pembagian oleh $x$ selalu berupa konstanta pada
polinomialnya.
