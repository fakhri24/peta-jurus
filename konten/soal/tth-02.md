---
id: tth-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Ada berapa tripel bilangan bulat $(x, y, z)$ dengan $|x| \le 50$, $|y| \le 50$, dan
$|z| \le 50$ yang memenuhi

$$x^2 + y^2 = 3z^2\ ?$$

## Petunjuk

- Jangan mencacah. Tanyakan lebih dulu: apakah persamaan ini punya solusi tak nol sama sekali?
- Modulo $3$, kuadrat hanya bernilai $0$ atau $1$. Apa yang dipaksakan oleh $x^2 + y^2 \equiv 0$?
- Kalau setiap solusi selalu bisa dibagi $3$ dan menghasilkan solusi lebih kecil, hanya ada satu solusi yang selamat.

## Pembahasan

Pertanyaannya terlihat seperti soal mencacah, tetapi jawabannya ditentukan oleh satu fakta
struktural: persamaan ini **tidak punya solusi bulat selain nol**.

Tinjau modulo $3$. Kuadrat modulo $3$ hanya bernilai $0$ atau $1$, sebab
$0^2 \equiv 0$ dan $(\pm 1)^2 \equiv 1$. Dari persamaannya, $x^2 + y^2 \equiv 0 \pmod 3$.
Kemungkinan jumlahnya hanya $0+0 = 0$, $0+1 = 1$, dan $1+1 = 2$ — dan hanya yang pertama
yang habis dibagi $3$. Maka

$$3 \mid x \quad \text{dan} \quad 3 \mid y$$

Tulis $x = 3x_1$, $y = 3y_1$:

$$9x_1^2 + 9y_1^2 = 3z^2 \quad\Longrightarrow\quad 3x_1^2 + 3y_1^2 = z^2$$

Sehingga $3 \mid z^2$, dan karena $3$ prima, $3 \mid z$. Tulis $z = 3z_1$, lalu

$$x_1^2 + y_1^2 = 3z_1^2$$

Setiap solusi karena itu menghasilkan solusi lain yang seluruh komponennya sepertiga
darinya. Kalau ada solusi tak nol, prosesnya bisa diulang selamanya dan menghasilkan
barisan bilangan asli yang menurun tanpa henti — mustahil.

Jadi satu-satunya solusi bulat adalah $(0, 0, 0)$, dan ia memenuhi seluruh batasan
$|x|, |y|, |z| \le 50$.

Banyaknya tripel adalah $\boxed{1}$.

Batas $50$ pada soal sama sekali tidak berpengaruh — ia hanya membuat pertanyaannya
terlihat seperti pencacahan. Kalau batasnya diganti $10^6$, jawabannya tetap $1$.
