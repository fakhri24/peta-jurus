---
id: fkl-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: isian
kesulitan: 2
jawaban: "4"
---

## Soal

Tentukan sisa pembagian $3^{100}$ oleh $7$.

## Petunjuk

- $7$ prima dan tidak membagi $3$.
- Fermat Kecil memberi $3^{6} \equiv 1 \pmod 7$.
- Potong $100$ modulo $6$.

## Pembahasan

Karena $7$ prima dan $7 \nmid 3$,

$$3^6 \equiv 1 \pmod 7$$

Bagi eksponennya dengan $6$: $100 = 6 \times 16 + 4$. Maka

$$3^{100} = \left(3^6\right)^{16} \cdot 3^4 \equiv 3^4 = 81 \pmod 7$$

dan $81 = 7 \times 11 + 4$, sehingga sisanya $\boxed{4}$.
