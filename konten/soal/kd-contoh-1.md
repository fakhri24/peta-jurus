---
id: kd-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [kongruensi-dasar]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Tentukan sisa pembagian $7^{100}$ oleh $5$.

## Petunjuk

- Ganti dulu bilangan pokoknya dengan sesuatu yang lebih kecil modulo 5.
- $7 \equiv 2 \pmod 5$, jadi soalnya berubah jadi $2^{100} \bmod 5$.
- Hitung $2^1, 2^2, 2^3, 2^4$ modulo $5$. Kapan hasilnya kembali ke $1$?

## Pembahasan

Sederhanakan bilangan pokoknya lebih dulu: $7 \equiv 2 \pmod 5$, sehingga

$$7^{100} \equiv 2^{100} \pmod 5$$

Sekarang cari polanya:

$$2^1 \equiv 2, \quad 2^2 \equiv 4, \quad 2^3 \equiv 3, \quad 2^4 \equiv 16 \equiv 1 \pmod 5$$

Begitu sampai di $1$, polanya berulang setiap $4$ langkah. Karena $100 = 4 \times 25$,

$$2^{100} = \left(2^{4}\right)^{25} \equiv 1^{25} = 1 \pmod 5$$

Sisanya $\boxed{1}$.

Dua kebiasaan yang layak dibawa dari soal ini: **kecilkan bilangan pokoknya dulu**, lalu
**cari kapan pangkatnya kembali ke $1$**. Panjang siklus itulah yang membuat eksponen
raksasa jadi tidak menakutkan.
