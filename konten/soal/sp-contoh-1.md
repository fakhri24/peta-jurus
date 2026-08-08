---
id: sp-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [sistem-persamaan]
bentuk: isian
kesulitan: 2
jawaban: "21"
---

## Soal

Diketahui $x + y = 10$ dan $x - y = 4$. Tentukan nilai $xy$.

## Petunjuk

- Dua persamaan, dua peubah. Perhatikan apa yang terjadi kalau keduanya dijumlahkan.
- Menjumlahkan menghapus $y$; mengurangkan menghapus $x$.
- Setelah $x$ dan $y$ diketahui, kalikan.

## Pembahasan

**Jumlahkan kedua persamaan.** Suku $y$ dan $-y$ saling menghapus:

$$(x+y) + (x-y) = 10 + 4 \quad\Longrightarrow\quad 2x = 14 \quad\Longrightarrow\quad x = 7$$

**Kurangkan** untuk memperoleh $y$:

$$(x+y) - (x-y) = 10 - 4 \quad\Longrightarrow\quad 2y = 6 \quad\Longrightarrow\quad y = 3$$

Maka

$$xy = 7 \times 3 = \boxed{21}$$

Periksa: $7 + 3 = 10$ dan $7 - 3 = 4$. Cocok.

**Cara kedua, tanpa mencari $x$ dan $y$.** Perhatikan identitas

$$(x+y)^2 - (x-y)^2 = 4xy$$

sehingga

$$xy = \frac{10^2 - 4^2}{4} = \frac{100-16}{4} = \frac{84}{4} = 21$$

Hasil yang sama. Cara pertama lebih alami di sini karena angkanya rapi, tetapi cara kedua
menunjukkan pola yang akan terus dipakai: **kalau yang ditanya bentuk simetris, sering ia
bisa dihitung tanpa mencari peubahnya satu per satu.**

Gerakan "jumlahkan lalu kurangkan" adalah refleks pertama untuk sistem berbentuk
$x+y$ dan $x-y$. Untuk sistem yang lain, eliminasi biasanya menuntut mengalikan salah satu
persamaan lebih dulu supaya koefisiennya bisa saling menghapus.
