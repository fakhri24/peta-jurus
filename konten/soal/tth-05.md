---
id: tth-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa persamaan

$$x^2 + y^2 = 11z^2$$

tidak punya solusi bulat selain $(0, 0, 0)$.

## Petunjuk

- Polanya sama seperti pada $7z^2$, tetapi daftar kuadratnya harus disusun ulang untuk modulus yang baru.
- Daftar seluruh kuadrat modulo $11$, lalu periksa pasangan mana yang berjumlah nol.
- Setelah $11 \mid x$ dan $11 \mid y$ terbukti, jangan lupa menurunkan $11 \mid z$ sebelum menutup penurunannya.

## Pembahasan

Andaikan ada solusi bulat tak nol, dan ambil yang $x^2 + y^2 + z^2$ terkecil.

**Langkah kongruensi.** Kuadrat modulo $11$:

$$(\pm 1)^2 \equiv 1, \quad (\pm 2)^2 \equiv 4, \quad (\pm 3)^2 \equiv 9, \quad
(\pm 4)^2 \equiv 5, \quad (\pm 5)^2 \equiv 3$$

bersama $0^2 \equiv 0$. Jadi himpunan kuadrat modulo $11$ adalah

$$\{0,\ 1,\ 3,\ 4,\ 5,\ 9\}$$

Persamaannya menuntut $x^2 + y^2 \equiv 0 \pmod{11}$, yaitu dua anggota himpunan itu yang
berjumlah $11$ atau $0$. Periksa setiap kemungkinan pasangan tak nol:

$$1 + 10, \quad 3 + 8, \quad 4 + 7, \quad 5 + 6, \quad 9 + 2$$

Pasangan yang dibutuhkan — $10$, $8$, $7$, $6$, $2$ — tidak satu pun ada di dalam
himpunan kuadrat. Maka satu-satunya kemungkinan adalah

$$x^2 \equiv 0 \quad \text{dan} \quad y^2 \equiv 0 \pmod{11}$$

Karena $11$ prima, ini memaksa $11 \mid x$ dan $11 \mid y$.

**Langkah turun.** Tulis $x = 11x_1$, $y = 11y_1$:

$$121x_1^2 + 121y_1^2 = 11z^2 \quad\Longrightarrow\quad 11x_1^2 + 11y_1^2 = z^2$$

Ruas kiri habis dibagi $11$, jadi $11 \mid z^2$ dan karenanya $11 \mid z$. Tulis
$z = 11z_1$:

$$x_1^2 + y_1^2 = 11z_1^2$$

**Kontradiksinya.** Solusi barunya bulat, tak nol, dan

$$x_1^2 + y_1^2 + z_1^2 = \frac{x^2+y^2+z^2}{121} < x^2 + y^2 + z^2$$

bertentangan dengan pemilihan yang terkecil. Jadi solusi tak nol tidak ada.
$\blacksquare$

Sama seperti pada $7$, yang menentukan adalah $11 \equiv 3 \pmod 4$. Untuk prima $p$
semacam itu, $x^2 + y^2 \equiv 0 \pmod p$ selalu memaksa $p \mid x$ dan $p \mid y$ — dan
seluruh argumen ini berjalan tanpa perubahan.

## Rubrik

- Mengambil solusi tak nol terkecil, atau menyusun penurunan tak hingga yang setara
- Mendaftar seluruh kuadrat modulo $11$ dengan benar, yaitu $\{0,1,3,4,5,9\}$
- Memeriksa **semua** pasangan dan menyimpulkan hanya $0 + 0$ yang berjumlah nol modulo $11$
- Menyimpulkan $11 \mid x$ dan $11 \mid y$ dengan menyebut $11$ prima
- Menurunkan $11 \mid z$ setelah substitusi
- Menunjukkan solusi barunya lebih kecil dan menutup kontradiksinya
