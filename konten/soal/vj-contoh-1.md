---
id: vj-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [vieta-jumping]
bentuk: uraian
kesulitan: 3
---

## Soal

Misalkan $a$ dan $b$ bilangan asli sehingga

$$\frac{a^2 + b^2 + 1}{ab}$$

bernilai bilangan bulat. Buktikan bahwa nilainya selalu $3$.

## Petunjuk

- Beri nama nilainya, lalu ubah menjadi persamaan tanpa pecahan. Perhatikan bentuknya: simetris dan berderajat dua.
- Pandang persamaan itu sebagai kuadrat dalam $a$ saja, dengan $b$ dan nilainya dianggap tetap. Rumus Vieta memberi akar keduanya.
- Ambil solusi dengan $a + b$ terkecil, lalu tunjukkan lompatan Vieta menghasilkan solusi yang lebih kecil — kecuali di kasus dasar.

## Pembahasan

Misalkan nilainya $k$, sehingga

$$a^2 + b^2 + 1 = kab$$

Yang akan dibuktikan: $k = 3$ selalu.

**Ambil solusi terkecil.** Di antara semua pasangan bilangan asli $(a,b)$ yang memenuhi
persamaan untuk nilai $k$ ini, ambil yang $a + b$ terkecil. Karena persamaannya simetris,
boleh diandaikan $a \ge b$.

**Lompatan Vieta.** Pandang persamaannya sebagai kuadrat dalam $a$:

$$a^2 - (kb)\,a + \left(b^2 + 1\right) = 0$$

Bilangan $a$ adalah salah satu akarnya. Sebut akar yang lain $a'$. Rumus Vieta memberi

$$a + a' = kb, \qquad a \cdot a' = b^2 + 1$$

Dari persamaan pertama, $a' = kb - a$ — **bulat**, karena $k$, $b$, dan $a$ semuanya
bulat. Dari persamaan kedua, $a' = \dfrac{b^2+1}{a} > 0$ — jadi $a'$ **bilangan asli**.

Maka $(a', b)$ juga solusi untuk $k$ yang sama.

**Tunjukkan lompatannya menurun.** Andaikan $a > b$. Karena $a \ge b + 1$,

$$a' = \frac{b^2 + 1}{a} \le \frac{b^2 + 1}{b + 1} \le b$$

Ketaksamaan terakhir berlaku sebab $b^2 + 1 \le b(b+1) = b^2 + b$ untuk $b \ge 1$. Jadi
$a' \le b < a$, sehingga $a' + b < a + b$ — bertentangan dengan keminimalan.

Karena itu pengandaian $a > b$ salah, dan pada solusi terkecil pastilah

$$a = b$$

**Kasus dasar.** Substitusikan $a = b$:

$$2a^2 + 1 = ka^2 \quad\Longrightarrow\quad a^2(k - 2) = 1$$

Karena $a$ dan $k$ bulat, satu-satunya kemungkinan adalah $a^2 = 1$ dan $k - 2 = 1$, yaitu

$$a = b = 1, \qquad k = 3$$

Jadi setiap nilai $k$ yang mungkin sama dengan $3$. $\blacksquare$

Solusinya sendiri membentuk barisan yang naik terus:

$$(1,1),\ (1,2),\ (2,5),\ (5,13),\ (13,34),\ (34,89),\ \ldots$$

— yaitu suku Fibonacci berindeks ganjil. Ada tak hingga banyaknya, tetapi nilai $k$-nya
selalu $3$.

## Rubrik

- Menamai nilainya $k$ dan mengubahnya menjadi $a^2 + b^2 + 1 = kab$
- Mengambil solusi dengan $a+b$ terkecil, dan memakai kesimetrian untuk mengandaikan $a \ge b$
- Memandang persamaan sebagai kuadrat dalam $a$ dan menuliskan kedua hubungan Vieta
- Membuktikan $a'$ **bulat** dari $a + a' = kb$ — bukan dari rumus akar kuadrat
- Membuktikan $a' > 0$ dari $a \cdot a' = b^2 + 1$
- Menunjukkan $a' < a$ sehingga bertentangan dengan keminimalan, memaksa $a = b$
- Menyelesaikan kasus dasar $a = b$ dan menyimpulkan $k = 3$
