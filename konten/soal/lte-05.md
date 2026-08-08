---
id: lte-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 3
jawaban: "256"
---

## Soal

Tentukan bilangan asli terkecil $n$ sehingga $3^n - 1$ habis dibagi $2^{10}$.

## Petunjuk

- Ini soal terbalik: pangkatnya diketahui, eksponennya dicari. Susun dulu $v_2(3^n - 1)$ sebagai fungsi dari $n$.
- Paritas $n$ menentukan rumus mana yang dipakai. Periksa kasus $n$ ganjil lebih dulu — hasilnya akan mengejutkan betapa kecilnya.
- Untuk $n$ genap, rumusnya menyederhana menjadi $v_2(3^n-1) = 2 + v_2(n)$. Dari situ, tentukan $v_2(n)$ terkecil yang cukup.

## Pembahasan

Yang dicari $n$ terkecil dengan $v_2\left(3^n - 1\right) \ge 10$.

**Kasus $n$ ganjil.** Di sini $v_2(a^n - b^n) = v_2(a-b)$, sehingga

$$v_2\left(3^n - 1\right) = v_2(2) = 1$$

Berapa pun besar $n$-nya, hasilnya tetap $1$. Jadi $n$ ganjil tidak pernah cukup.

**Kasus $n$ genap.** Pakai rumus $p = 2$:

$$v_2\left(3^n - 1\right) = v_2(3-1) + v_2(3+1) + v_2(n) - 1 = 1 + 2 + v_2(n) - 1
= 2 + v_2(n)$$

**Selesaikan.** Dituntut

$$2 + v_2(n) \ge 10 \quad\Longrightarrow\quad v_2(n) \ge 8$$

Bilangan asli terkecil dengan $v_2(n) \ge 8$ adalah

$$n = 2^8 = \boxed{256}$$

Periksa batasnya: untuk $n = 256$ diperoleh $v_2 = 2 + 8 = 10$ — tepat cukup. Untuk
$n = 128$ diperoleh $v_2 = 2 + 7 = 9$, kurang satu.

Perhatikan bahwa jawabannya harus pangkat $2$ murni. Bilangan seperti $n = 3 \times 256 =
768$ juga memenuhi $v_2(n) \ge 8$, tetapi lebih besar; sedangkan bilangan yang lebih kecil
dari $256$ tidak mungkin memuat $2^8$.

Soal terbalik semacam ini adalah tempat LTE paling terasa gunanya. Tanpa rumusnya, kamu
harus menghitung $3^n - 1$ untuk $n$ yang membesar dan memeriksa keterbagiannya satu per
satu — dan jawabannya berada di $n = 256$, jauh di luar jangkauan tangan.
