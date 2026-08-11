---
id: fkl-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [fermat-kecil]
bentuk: isian
kesulitan: 3
jawaban: "5"
---

## Soal

Tentukan sisa pembagian $5^{2026}$ oleh $11$.

## Petunjuk

- Modulusnya prima dan basisnya tidak habis dibagi olehnya. Pangkat sebesar $2026$ tidak perlu dihitung — pangkat-pangkat $5$ modulo $11$ pasti berulang, dan yang perlu diketahui cuma panjang putarannya.
- Fermat Kecil memberi $5^{10} \equiv 1 \pmod{11}$, jadi potong $2026$ modulo $10$: $2026 = 10 \times 202 + 6$.
- Tinggal $5^6 \bmod 11$. Hitung bertahap: $5^2 \equiv 3$, lalu $5^4 \equiv 9$, lalu $5^6 = 5^4 \cdot 5^2$.

## Pembahasan

Karena $11$ prima dan $11 \nmid 5$, berlaku $5^{10} \equiv 1 \pmod{11}$. Dari
$2026 = 10 \times 202 + 6$,

$$5^{2026} \equiv 5^6 \pmod{11}$$

Hitung bertahap supaya angkanya tetap kecil:

$$5^2 = 25 \equiv 3, \qquad 5^4 \equiv 3^2 = 9, \qquad 5^6 \equiv 9 \cdot 3 = 27 \equiv 5 \pmod{11}$$

Sisanya $\boxed{5}$.

Kalau kamu menghitung siklusnya sendiri, ternyata $5^5 \equiv 1 \pmod{11}$ — ordenya $5$,
bukan $10$. Fermat Kecil selalu bekerja, tapi tidak selalu memberi siklus terpendek. Itu
wilayah orde elemen.
