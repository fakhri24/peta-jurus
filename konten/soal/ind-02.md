---
id: ind-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa untuk setiap bilangan asli $n$,

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2$$

## Petunjuk

- Alurnya sama seperti pembuktian jumlah biasa: basis, lalu langkah $k \to k+1$.
- Pada langkah induksi, tambahkan $(k+1)^3$ ke hipotesis.
- Yang perlu ditunjukkan: $\left(\frac{k(k+1)}{2}\right)^2 + (k+1)^3 = \left(\frac{(k+1)(k+2)}{2}\right)^2$. Keluarkan $(k+1)^2$ sebagai faktor persekutuan.

## Pembahasan

### Basis

Untuk $n = 1$: ruas kiri $= 1$, dan ruas kanan $= \left(\frac{1 \cdot 2}{2}\right)^2 = 1$.
Cocok.

### Langkah induksi

Andaikan benar untuk $n = k$:

$$1^3 + 2^3 + \cdots + k^3 = \left(\frac{k(k+1)}{2}\right)^2 = \frac{k^2(k+1)^2}{4}$$

Tambahkan suku berikutnya:

$$1^3 + \cdots + k^3 + (k+1)^3 = \frac{k^2(k+1)^2}{4} + (k+1)^3$$

**Keluarkan $(k+1)^2$ sebagai faktor persekutuan** — ini langkah kuncinya:

$$= (k+1)^2\left[\frac{k^2}{4} + (k+1)\right] = (k+1)^2 \cdot \frac{k^2 + 4k + 4}{4}$$

Pembilangnya kuadrat sempurna:

$$= (k+1)^2 \cdot \frac{(k+2)^2}{4} = \frac{(k+1)^2(k+2)^2}{4}
= \left(\frac{(k+1)(k+2)}{2}\right)^2$$

Itu persis bentuk yang diminta untuk $n = k+1$.

### Kesimpulan

Basis benar dan langkah induksinya berlaku, jadi pernyataannya benar untuk setiap bilangan
asli $n$. $\blacksquare$

Perhatikan bahwa ruas kanannya tidak lain adalah $\left(1+2+\cdots+n\right)^2$. Jadi yang
baru saja dibuktikan bisa dibaca:

$$1^3 + 2^3 + \cdots + n^3 = \left(1 + 2 + \cdots + n\right)^2$$

Untuk $n = 4$ misalnya: $1 + 8 + 27 + 64 = 100 = 10^2$, dan $1+2+3+4 = 10$. Kesamaan yang
tidak terduga itu punya bukti tanpa kata lewat susunan persegi — tetapi induksi
membuktikannya tanpa perlu gambar sama sekali.

Langkah "keluarkan $(k+1)^2$" adalah bagian yang paling sering macet. Aturan umumnya: pada
langkah induksi, **carilah faktor persekutuan antara hipotesis dan suku baru** sebelum
menjabarkan apa pun. Menjabarkan lebih dulu hampir selalu menghasilkan polinomial berderajat
empat yang harus difaktorkan ulang.

## Rubrik

- Memeriksa basis pada $n = 1$
- Menuliskan hipotesis induksi untuk $n = k$ secara eksplisit
- Menambahkan $(k+1)^3$ dan memakai hipotesis
- Mengeluarkan $(k+1)^2$ sebagai faktor persekutuan
- Mengenali $k^2+4k+4 = (k+2)^2$ dan menyusun kembali ke bentuk yang diminta
- Menutup dengan prinsip induksi
