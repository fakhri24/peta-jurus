---
id: vt-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [vieta]
bentuk: isian
kesulitan: 2
jawaban: "25"
---

## Soal

Akar-akar persamaan $x^2 - 7x + 12 = 0$ adalah $x_1$ dan $x_2$. Tentukan nilai
$x_1^2 + x_2^2$.

## Petunjuk

- Yang ditanya bentuk simetris akar-akarnya, bukan akarnya sendiri. Itu tanda paling jelas untuk jurus ini.
- Rumus Vieta memberi $x_1+x_2 = -\frac{b}{a}$ dan $x_1x_2 = \frac{c}{a}$ tanpa menghitung akar.
- Tulis ulang $x_1^2+x_2^2$ lewat kedua bentuk itu.

## Pembahasan

Rumus Vieta untuk $ax^2+bx+c = 0$:

$$x_1 + x_2 = -\frac{b}{a}, \qquad x_1 x_2 = \frac{c}{a}$$

Di sini $a = 1$, $b = -7$, $c = 12$, sehingga

$$x_1 + x_2 = 7, \qquad x_1 x_2 = 12$$

Tulis ulang yang ditanya:

$$x_1^2 + x_2^2 = \left(x_1+x_2\right)^2 - 2x_1x_2 = 7^2 - 2(12) = 49 - 24 = \boxed{25}$$

Periksa: akarnya memang $3$ dan $4$, dan $9 + 16 = 25$.

Di sini akarnya kebetulan rasional, jadi mencarinya juga bisa. Tetapi kekuatan Vieta baru
terasa ketika akarnya tidak rasional. Pada $x^2 - 7x + 11 = 0$ misalnya, akarnya
$\frac{7 \pm \sqrt5}{2}$ — dan menghitung $x_1^2+x_2^2$ darinya jauh lebih panjang,
padahal Vieta langsung memberi $49 - 22 = 27$.

**Aturan kerjanya selalu sama:** tulis ulang bentuk yang ditanya lewat $x_1+x_2$ dan
$x_1x_2$. Beberapa yang sering muncul:

$$\frac{1}{x_1} + \frac{1}{x_2} = \frac{x_1+x_2}{x_1x_2}, \qquad
\left(x_1-x_2\right)^2 = \left(x_1+x_2\right)^2 - 4x_1x_2$$
