---
id: fkl-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [fermat-kecil]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $n^7 - n$ habis dibagi $42$ untuk setiap bilangan bulat $n$.

## Petunjuk

- Faktorkan $42$ jadi prima. Ketiganya relatif prima berpasangan, jadi bisa diperiksa terpisah.
- $42 = 2 \times 3 \times 7$. Untuk $7$, pakai bentuk Fermat Kecil yang tanpa syarat: $a^p \equiv a \pmod p$.
- Untuk $3$, mulai dari $n^3 \equiv n \pmod 3$ lalu dorong sampai pangkat tujuh.

## Pembahasan

Karena $42 = 2 \times 3 \times 7$ dengan ketiganya relatif prima berpasangan, cukup
dibuktikan $n^7 - n$ habis dibagi oleh masing-masing.

**Modulo 7.** Bentuk kedua Fermat Kecil berlaku tanpa syarat:

$$n^7 \equiv n \pmod 7$$

**Modulo 2.** Fermat Kecil memberi $n^2 \equiv n \pmod 2$. Menerapkannya berulang,
$n^7 \equiv n \pmod 2$. (Langsung juga terlihat: $n^7$ selalu berparitas sama dengan $n$.)

**Modulo 3.** Fermat Kecil memberi $n^3 \equiv n \pmod 3$. Maka

$$n^7 = \left(n^3\right)^2 \cdot n \equiv n^2 \cdot n = n^3 \equiv n \pmod 3$$

Jadi $2$, $3$, dan $7$ semuanya membagi $n^7 - n$. Karena ketiganya relatif prima
berpasangan, hasil kalinya juga membagi:

$$42 \mid n^7 - n$$

untuk setiap bilangan bulat $n$. $\blacksquare$

## Rubrik

- Memfaktorkan $42 = 2 \times 3 \times 7$ dan menyatakan cukup memeriksa masing-masing secara terpisah
- Membuktikan $n^7 \equiv n \pmod 7$ dengan bentuk $a^p \equiv a$ (yang berlaku juga saat $p \mid n$)
- Membuktikan $n^7 \equiv n \pmod 2$
- Membuktikan $n^7 \equiv n \pmod 3$, misalnya lewat $n^7 = (n^3)^2 \cdot n$
- Menyimpulkan kembali ke $42$ **dengan menyebut** alasan relatif prima berpasangan
