---
id: ind-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi, barisan-deret]
bentuk: isian
kesulitan: 2
jawaban: "225"
---

## Soal

Tentukan nilai dari

$$1^3 + 2^3 + 3^3 + 4^3 + 5^3$$

## Petunjuk

- Menjumlahkan lima suku memang cepat, tetapi periksa dulu apakah hasilnya punya bentuk yang mengejutkan.
- Jumlah pangkat tiga $n$ bilangan asli pertama sama dengan **kuadrat** dari jumlah bilangannya.
- $1+2+3+4+5 = 15$.

## Pembahasan

Rumus jumlah pangkat tiga:

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2 = \left(1+2+\cdots+n\right)^2$$

Untuk $n = 5$, jumlah bilangannya

$$1+2+3+4+5 = \frac{5 \times 6}{2} = 15$$

sehingga

$$1^3+2^3+3^3+4^3+5^3 = 15^2 = \boxed{225}$$

Periksa dengan menjumlahkan langsung:

$$1 + 8 + 27 + 64 + 125 = 225$$

Cocok.

Kesamaan ini terus berlaku: $1^3+2^3 = 9 = 3^2$, dan $1+2 = 3$; lalu
$1^3+2^3+3^3 = 36 = 6^2$, dan $1+2+3 = 6$. Bahwa jumlah pangkat tiga selalu berupa kuadrat
sempurna — dan tepat kuadrat dari jumlah bilangannya — adalah salah satu kesamaan paling
mengejutkan di aljabar dasar.

**Akibat yang berguna di soal olimpiade:** jumlah pangkat tiga berurutan selalu kuadrat
sempurna. Soal seperti "buktikan $1^3+\cdots+n^3$ kuadrat sempurna" karena itu selesai
seketika begitu rumusnya dikenali.

Untuk menghitungnya cepat, jangan memangkatkan tiga satu per satu lalu menjumlahkan.
Hitung jumlah bilangannya dulu — itu satu perkalian — lalu kuadratkan.
