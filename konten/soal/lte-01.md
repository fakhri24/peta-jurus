---
id: lte-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 1
jawaban: "3"
---

## Soal

Tentukan pangkat tertinggi $5$ yang membagi $6^{25} - 1$.

## Petunjuk

- Tulis dalam bentuk $a^n - b^n$ lebih dulu, lalu periksa ketiga syarat rumusnya.
- Di sini $a = 6$, $b = 1$, $n = 25$, dan $a - b = 5$ — memang habis dibagi $5$.
- Rumusnya menjumlahkan dua suku: $v_5(a-b)$ dan $v_5(n)$.

## Pembahasan

Tulis $6^{25} - 1 = 6^{25} - 1^{25}$, jadi $a = 6$, $b = 1$, $n = 25$.

**Periksa syaratnya.** Prima $p = 5$ ganjil, $a - b = 5$ sehingga $5 \mid a - b$, dan
$5$ tidak membagi $6$ maupun $1$. Semua terpenuhi.

**Terapkan rumusnya.**

$$v_5\left(6^{25} - 1\right) = v_5(6 - 1) + v_5(25) = v_5(5) + v_5\left(5^2\right)
= 1 + 2 = \boxed{3}$$

Jadi $5^3 = 125$ membagi $6^{25} - 1$, dan $5^4$ tidak.

Untuk merasakan besarnya penghematan: $6^{25}$ adalah bilangan berdigit $20$, dan
menghitungnya lalu memfaktorkan hasilnya jauh lebih mahal daripada menjumlahkan dua angka
kecil.

Perhatikan bahwa suku kedua, $v_5(n)$, sepenuhnya ditentukan oleh **eksponennya** — bukan
oleh basisnya. Kalau soalnya diganti menjadi $6^{125} - 1$, jawabannya menjadi $1 + 3 = 4$.
