---
id: ss-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [substitusi-simetri]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Ada berapa akar real dari persamaan

$$x^4 - 5x^3 + 8x^2 - 5x + 1 = 0\ ?$$

## Petunjuk

- Perhatikan koefisiennya: $1, -5, 8, -5, 1$ — membaca sama dari depan dan dari belakang.
- Untuk polinomial semacam itu, bagi kedua ruas dengan $x^2$ lebih dulu. Periksa dulu apakah $x = 0$ solusi.
- Setelah dibagi, kelompokkan menjadi $\left(x^2+\frac{1}{x^2}\right) - 5\left(x+\frac1x\right) + 8$, lalu beri nama $t = x + \frac1x$.

## Pembahasan

**Kenali polanya.** Koefisiennya $1, -5, 8, -5, 1$ — sama dibaca dari kedua arah.
Polinomial semacam ini disebut **palindromik**, dan ia hampir selalu menyerah pada
substitusi $t = x + \frac1x$.

**Periksa $x = 0$.** Substitusikan: $0 - 0 + 0 - 0 + 1 = 1 \ne 0$, jadi $x = 0$ bukan
akar. Karena itu membagi dengan $x^2$ tidak menghilangkan solusi apa pun.

**Bagi dengan $x^2$:**

$$x^2 - 5x + 8 - \frac{5}{x} + \frac{1}{x^2} = 0$$

**Kelompokkan** suku yang berpasangan:

$$\left(x^2 + \frac{1}{x^2}\right) - 5\left(x + \frac{1}{x}\right) + 8 = 0$$

**Substitusikan $t = x + \frac1x$.** Karena $t^2 = x^2 + 2 + \frac{1}{x^2}$, maka
$x^2+\frac{1}{x^2} = t^2 - 2$:

$$\left(t^2 - 2\right) - 5t + 8 = 0 \quad\Longrightarrow\quad t^2 - 5t + 6 = 0$$

Faktorkan: $(t-2)(t-3) = 0$, jadi $t = 2$ atau $t = 3$.

**Kembalikan ke $x$.**

Untuk $t = 2$: $x + \frac1x = 2$, yaitu $x^2 - 2x + 1 = 0$, yaitu $(x-1)^2 = 0$. Memberi
$x = 1$ — **satu** akar (kembar).

Untuk $t = 3$: $x + \frac1x = 3$, yaitu $x^2 - 3x + 1 = 0$. Diskriminannya $9 - 4 = 5 > 0$,
jadi **dua** akar real berbeda, yaitu $\frac{3 \pm \sqrt5}{2}$.

Seluruhnya ada $\boxed{3}$ akar real yang berbeda.

**Batas pada $t$ layak diperiksa.** Untuk $x$ real tak nol, nilai $t = x+\frac1x$ selalu
memenuhi $|t| \ge 2$. Kedua nilai yang diperoleh, $2$ dan $3$, memenuhi syarat itu — jadi
keduanya benar-benar menghasilkan $x$ real. Kalau muncul $t$ dengan $|t| < 2$, ia harus
dibuang.

Perhatikan bahwa persamaan berderajat empat ini runtuh menjadi kuadrat hanya dengan satu
penamaan. Itulah yang ditawarkan jurus ini: **beri nama bentuk yang berulang, dan derajatnya
turun separuh.**
