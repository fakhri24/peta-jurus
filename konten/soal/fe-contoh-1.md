---
id: fe-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fungsi-euler]
bentuk: isian
kesulitan: 1
jawaban: "96"
---

## Soal

Tentukan $\varphi(360)$.

## Petunjuk

- Rumus $\varphi$ bekerja atas faktor prima, jadi langkah pertamanya selalu sama.
- Faktorkan $360$ atas prima: $360 = 2^3 \times 3^2 \times 5$.
- Pakai $\varphi(n) = n \prod_{p \mid n}\left(1 - \frac1p\right)$, dengan hasil kali diambil atas prima **berbeda** yang membagi $n$.

## Pembahasan

Faktorkan lebih dulu:

$$360 = 2^3 \times 3^2 \times 5$$

Prima berbeda yang membagi $360$ adalah $2$, $3$, dan $5$. Maka

$$\varphi(360) = 360\left(1 - \frac12\right)\left(1 - \frac13\right)\left(1 - \frac15\right)
= 360 \times \frac12 \times \frac23 \times \frac45$$

Hitung bertahap:

$$360 \times \frac12 = 180, \qquad 180 \times \frac23 = 120, \qquad 120 \times \frac45 = \boxed{96}$$

Bisa juga lewat sifat multiplikatif, karena $8$, $9$, dan $5$ saling asing berpasangan:

$$\varphi(360) = \varphi(8)\,\varphi(9)\,\varphi(5) = 4 \times 6 \times 4 = 96$$

dengan $\varphi(p^k) = p^k - p^{k-1}$.

Perhatikan bahwa yang masuk ke dalam hasil kali adalah prima **berbeda**, bukan pangkatnya.
Meski $2$ muncul tiga kali dalam faktorisasi, faktor $\left(1 - \frac12\right)$ hanya
dipakai sekali.
