---
id: tsc-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: isian
kesulitan: 3
jawaban: "301"
---

## Soal

Tentukan bilangan asli terkecil yang bersisa $1$ jika dibagi $2$, $3$, $4$, $5$, maupun
$6$, dan habis dibagi $7$.

## Petunjuk

- Lima syarat pertama semuanya bersisa $1$. Bisakah kelimanya diringkas menjadi satu syarat?
- Kalau $n - 1$ habis dibagi $2, 3, 4, 5, 6$, maka $n - 1$ kelipatan KPK-nya.
- Setelah tersisa dua syarat, gabungkan dengan substitusi seperti biasa.

## Pembahasan

**Ringkas lima syarat pertama.** Semuanya berbunyi "bersisa $1$", jadi semuanya sama
dengan mengatakan $n - 1$ habis dibagi $2$, $3$, $4$, $5$, dan $6$. Artinya $n-1$
kelipatan persekutuan kelimanya, yaitu kelipatan

$$\operatorname{lcm}(2,3,4,5,6) = 60$$

Jadi

$$n \equiv 1 \pmod{60}$$

Lima syarat runtuh menjadi satu. Ini yang membuat soalnya jinak — tanpa langkah ini, kamu
akan menggabungkan enam kongruensi satu per satu.

**Gabungkan dengan syarat ketujuh.** Dituntut pula $n \equiv 0 \pmod 7$. Karena
$\gcd(60, 7) = 1$, solusinya tunggal modulo $420$.

Tulis $n = 60t + 1$ dan masukkan ke $n \equiv 0 \pmod 7$:

$$60t + 1 \equiv 0 \pmod 7$$

Karena $60 = 8 \times 7 + 4 \equiv 4 \pmod 7$:

$$4t \equiv -1 \equiv 6 \pmod 7$$

Invers $4$ modulo $7$ adalah $2$, sebab $4 \times 2 = 8 \equiv 1$. Maka

$$t \equiv 2 \times 6 = 12 \equiv 5 \pmod 7 \quad\Longrightarrow\quad t = 7s + 5$$

Substitusikan kembali:

$$n = 60(7s + 5) + 1 = 420s + 301$$

Bilangan asli terkecilnya adalah $\boxed{301}$.

Periksa: $301 = 60 \times 5 + 1$, jadi ia bersisa $1$ dibagi $2,3,4,5,6$. Dan
$301 = 7 \times 43$, jadi habis dibagi $7$. Cocok.

Perhatikan bahwa $\operatorname{lcm}(2,3,4,5,6) = 60$, bukan $720$. Mengalikan seluruh
modulus adalah kekeliruan yang wajar tetapi mahal — ia akan memberi jawaban yang jauh lebih
besar dan salah.
