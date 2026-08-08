---
id: bz-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [bezout]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan bilangan asli terkecil $x$ yang memenuhi $17x + 5y = 1$ untuk suatu bilangan
bulat $y$.

## Petunjuk

- Persamaan itu punya solusi karena $\gcd(17,5) = 1$. Yang dicari hanya $x$-nya, jadi $y$ boleh disingkirkan.
- Menyingkirkan $y$ berarti bekerja modulo $5$: dari $17x + 5y = 1$ diperoleh $17x \equiv 1 \pmod 5$.
- Sederhanakan $17 \equiv 2 \pmod 5$, lalu selesaikan $2x \equiv 1 \pmod 5$.

## Pembahasan

Karena $\gcd(17, 5) = 1$, identitas Bézout menjamin ada bulat $x, y$ dengan
$17x + 5y = 1$.

Untuk mencari $x$ saja, tinjau persamaannya modulo $5$ — suku $5y$ lenyap:

$$17x \equiv 1 \pmod 5$$

Karena $17 = 3 \times 5 + 2$, kita punya $17 \equiv 2 \pmod 5$, sehingga

$$2x \equiv 1 \pmod 5$$

Coba $x = 0, 1, 2, 3, 4$: nilai $2x$ berturut-turut $0, 2, 4, 6 \equiv 1, 8 \equiv 3$.
Yang memberi $1$ adalah $x = 3$.

Jadi $x \equiv 3 \pmod 5$, dan bilangan asli terkecilnya adalah $\boxed{3}$.

Periksa: $17 \times 3 = 51$, dan $51 + 5y = 1$ memberi $y = -10$. Memang
$17(3) + 5(-10) = 51 - 50 = 1$.

Perhatikan $y$ bernilai negatif. Itu bukan kekeliruan — pada identitas Bézout hampir
selalu salah satu dari $x$ atau $y$ negatif, sebab $ax$ dan $by$ harus saling meniadakan
sampai tersisa bilangan sekecil $\gcd(a,b)$.
