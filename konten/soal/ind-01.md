---
id: ind-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi, barisan-deret]
bentuk: isian
kesulitan: 2
jawaban: "385"
---

## Soal

Tentukan nilai dari

$$1^2 + 2^2 + 3^2 + \cdots + 10^2$$

## Petunjuk

- Menjumlahkan sepuluh suku bisa, tetapi ada rumus tertutup yang layak dikenali.
- Jumlah kuadrat $n$ bilangan asli pertama adalah $\frac{n(n+1)(2n+1)}{6}$.
- Substitusikan $n = 10$ dan hitung bertahap.

## Pembahasan

Rumus jumlah kuadrat $n$ bilangan asli pertama:

$$1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

Substitusikan $n = 10$:

$$\frac{10 \times 11 \times 21}{6}$$

Hitung bertahap, dan sederhanakan sebelum mengalikan:

$$= \frac{10 \times 11 \times 21}{6} = \frac{2310}{6} = \boxed{385}$$

Periksa dengan menjumlahkan langsung:

$$1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 = 385$$

Cocok.

Rumus itu sendiri dibuktikan dengan induksi, dan pembuktiannya mengikuti pola yang sama:
basis di $n = 1$, lalu tunjukkan

$$\frac{k(k+1)(2k+1)}{6} + (k+1)^2 = \frac{(k+1)(k+2)(2k+3)}{6}$$

Tiga rumus jumlah yang layak dikenali seketika, karena ketiganya muncul terus-menerus:

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}, \qquad
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}, \qquad
\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2$$

Yang ketiga punya bentuk yang mengejutkan: jumlah pangkat tiga selalu sama dengan **kuadrat
dari jumlah** bilangannya.
