---
id: fermat-kecil
nama: Teorema Fermat Kecil
pilar: teori-bilangan
tahap: osn-p
prasyarat: [sistem-residu]
contoh: [fkl-contoh-1]
latihan: [fkl-01, fkl-02, fkl-03, fkl-04, fkl-05, fkl-06]
---

## Kapan dipakai

Ada **pangkat besar** dan **modulus prima**. Begitu kamu melihat $2^{2019} \bmod 13$ atau
sejenisnya, ini jurus pertama yang dicoba.

## Intinya

Kalau $p$ prima dan $p \nmid a$:

$$a^{p-1} \equiv 1 \pmod p$$

Ada bentuk kedua yang berlaku **tanpa syarat**, termasuk saat $p \mid a$:

$$a^p \equiv a \pmod p$$

Cara memakainya selalu sama: eksponennya dipotong modulo $p - 1$.

> $2^{2019} \bmod 13$. Di sini $p - 1 = 12$, dan $2019 = 12 \cdot 168 + 3$. Jadi
> $2^{2019} \equiv 2^3 = 8 \pmod{13}$.

Perhatikan pergantian modulusnya: **bilangan pokok dihitung modulo $p$, eksponen dihitung
modulo $p-1$.** Dua modulus berbeda dalam satu langkah — di situlah kebanyakan orang
tergelincir.

## Jebakan umum

- **Lupa memeriksa $p \nmid a$.** Bentuk $a^{p-1} \equiv 1$ batal kalau $p$ membagi $a$.
  Kalau ragu, pakai bentuk $a^p \equiv a$ yang selalu aman.
- **Memakainya untuk modulus komposit.** $n = 15$ bukan prima, jadi $a^{14} \equiv 1
  \pmod{15}$ tidak benar. Untuk komposit, yang berlaku adalah Teorema Euler.
- **Mereduksi eksponen modulo $p$, bukan $p-1$.** Kesalahan yang paling sering, dan paling
  sulit terlihat karena hasilnya tetap "kelihatan masuk akal".
- **Mengira kebalikannya benar.** $a^{n-1} \equiv 1 \pmod n$ tidak menjamin $n$ prima —
  ada bilangan Carmichael yang lolos uji ini padahal komposit.
