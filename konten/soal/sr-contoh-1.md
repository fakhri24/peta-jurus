---
id: sr-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [sistem-residu]
bentuk: isian
kesulitan: 2
jawaban: "16"
---

## Soal

Ada berapa bilangan di antara $1$ sampai $60$ yang relatif prima terhadap $60$?

## Petunjuk

- Yang ditanyakan adalah besarnya sistem residu tereduksi modulo $60$, yaitu $\varphi(60)$.
- Faktorkan $60$ lebih dulu: $60 = 2^2 \cdot 3 \cdot 5$.
- Buang kelipatan tiap prima secara berurutan: kalikan $60$ dengan $\left(1-\tfrac12\right)\left(1-\tfrac13\right)\left(1-\tfrac15\right)$.

## Pembahasan

Yang diminta adalah banyaknya anggota sistem residu **tereduksi** modulo $60$, yaitu
$\varphi(60)$.

Faktorkan: $60 = 2^2 \cdot 3 \cdot 5$. Prima yang muncul adalah $2$, $3$, dan $5$.

$$\varphi(60) = 60\left(1 - \frac12\right)\left(1 - \frac13\right)\left(1 - \frac15\right)
= 60 \cdot \frac12 \cdot \frac23 \cdot \frac45 = 16$$

Jadi ada $\boxed{16}$ bilangan.

Daftarnya: $1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59$ — tepat enam
belas.

Perhatikan bahwa yang menentukan hanyalah **prima mana saja yang muncul**, bukan
pangkatnya. Faktor $2^2$ tetap menyumbang satu kurungan $\left(1-\tfrac12\right)$, sama
seperti kalau pangkatnya satu.
