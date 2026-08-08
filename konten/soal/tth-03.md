---
id: tth-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa persamaan

$$x^3 + 2y^3 = 4z^3$$

tidak punya solusi bulat selain $(0, 0, 0)$.

## Petunjuk

- Di sini yang dipakai bukan kuadrat modulo prima, melainkan sesuatu yang jauh lebih sederhana: paritas.
- Dari $x^3 = 4z^3 - 2y^3$, ruas kanan genap. Apa yang dipaksakan pada $x$?
- Setelah $x = 2x_1$ disubstitusikan, ulangi penalaran yang sama pada $y$, lalu pada $z$.

## Pembahasan

Andaikan ada solusi bulat tak nol, dan ambil yang $|x| + |y| + |z|$ terkecil.

**Langkah pertama: $x$ genap.** Tulis persamaannya sebagai

$$x^3 = 4z^3 - 2y^3 = 2\left(2z^3 - y^3\right)$$

Ruas kanan genap, jadi $x^3$ genap. Pangkat tiga bilangan ganjil selalu ganjil, sehingga
$x$ sendiri genap. Tulis $x = 2x_1$:

$$8x_1^3 + 2y^3 = 4z^3 \quad\Longrightarrow\quad 4x_1^3 + y^3 = 2z^3$$

**Langkah kedua: $y$ genap.** Dari bentuk terakhir,

$$y^3 = 2z^3 - 4x_1^3 = 2\left(z^3 - 2x_1^3\right)$$

genap, jadi $y$ genap. Tulis $y = 2y_1$:

$$4x_1^3 + 8y_1^3 = 2z^3 \quad\Longrightarrow\quad 2x_1^3 + 4y_1^3 = z^3$$

**Langkah ketiga: $z$ genap.** Ruas kiri genap, jadi $z^3$ genap dan $z$ genap. Tulis
$z = 2z_1$:

$$2x_1^3 + 4y_1^3 = 8z_1^3 \quad\Longrightarrow\quad x_1^3 + 2y_1^3 = 4z_1^3$$

Bentuknya kembali persis seperti semula.

**Kontradiksinya.** Jadi $(x_1, y_1, z_1) = (x/2,\ y/2,\ z/2)$ juga solusi bulat, tak nol,
dengan

$$|x_1| + |y_1| + |z_1| = \frac{|x| + |y| + |z|}{2} < |x| + |y| + |z|$$

bertentangan dengan pemilihan yang terkecil. Maka tidak ada solusi tak nol.
$\blacksquare$

Perhatikan bahwa ketiga langkahnya harus dijalankan berurutan — masing-masing memakai
hasil langkah sebelumnya. Berhenti setelah membuktikan $x$ genap tidak menghasilkan apa
pun: yang menutup soal adalah kembalinya bentuk persamaan ke wujud semula setelah ketiganya
dibagi $2$.

## Rubrik

- Mengambil solusi tak nol terkecil, atau menyusun penurunan tak hingga yang setara
- Membuktikan $x$ genap dari $x^3$ genap, dengan alasan pangkat tiga ganjil selalu ganjil
- Mensubstitusikan $x = 2x_1$ dan menurunkan bentuk barunya dengan benar
- Melanjutkan ke $y$ genap, lalu ke $z$ genap — ketiganya diperlukan
- Menunjukkan persamaannya kembali ke bentuk semula setelah ketiganya dibagi $2$
- Menyatakan solusi barunya bulat, tak nol, dan benar-benar lebih kecil, lalu menutup kontradiksinya
