---
id: oe-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [orde-elemen]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan $\operatorname{ord}_7(2)$, yaitu bilangan asli terkecil $d$ dengan
$2^d \equiv 1 \pmod 7$.

## Petunjuk

- Sebelum mencoba satu per satu, persempit dulu daftar kandidatnya.
- Orde selalu membagi $\varphi(n)$. Di sini $\varphi(7) = 6$, jadi $d$ hanya bisa $1$, $2$, $3$, atau $6$.
- Uji kandidat dari yang terkecil, dan berhenti pada yang pertama memberi $1$.

## Pembahasan

**Persempit kandidatnya.** Karena $\gcd(2,7) = 1$, ordenya ada. Sifat pokoknya:

$$a^k \equiv 1 \pmod n \iff \operatorname{ord}_n(a) \mid k$$

Teorema Euler memberi $2^{\varphi(7)} = 2^6 \equiv 1 \pmod 7$, jadi ordenya membagi $6$.
Pembagi $6$ adalah $1, 2, 3, 6$ — hanya empat kandidat, bukan enam.

**Uji dari yang terkecil.**

$$2^1 = 2 \not\equiv 1$$
$$2^2 = 4 \not\equiv 1$$
$$2^3 = 8 = 7 + 1 \equiv 1 \pmod 7$$

Yang pertama memberi $1$ adalah $d = \boxed{3}$.

Perhatikan bahwa ordenya $3$, bukan $6$. Orde membagi $\varphi(n)$, tetapi tidak harus
sama dengannya — dan menyamakan keduanya adalah kekeliruan yang paling sering terjadi pada
jurus ini.

Sebagai akibatnya, $2^k \equiv 1 \pmod 7$ tepat ketika $3 \mid k$. Contohnya
$2^{100}$: karena $100 = 3 \times 33 + 1$, diperoleh $2^{100} \equiv 2^1 = 2 \pmod 7$ —
jauh lebih cepat daripada memakai eksponen $6$ dari Euler.
