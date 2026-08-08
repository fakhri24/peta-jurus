---
id: tth-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa persamaan

$$x^2 + y^2 = 7z^2$$

tidak punya solusi bulat selain $(0, 0, 0)$.

## Petunjuk

- Kongruensi dulu, penurunan kemudian. Modulo berapa yang paling menjanjikan di sini?
- Daftar nilai kuadrat modulo $7$. Himpunannya sempit, dan itu membatasi $x^2 + y^2$ dengan keras.
- Setelah terbukti $7 \mid x$ dan $7 \mid y$, substitusikan dan lihat apa yang terjadi pada $z$.

## Pembahasan

Andaikan ada solusi bulat tak nol. Ambil solusi $(x, y, z)$ dengan $x^2 + y^2 + z^2$
**terkecil** di antara semua solusi tak nol.

**Langkah kongruensi.** Tinjau persamaannya modulo $7$. Kuadrat modulo $7$ hanya bernilai

$$0^2 \equiv 0, \quad (\pm 1)^2 \equiv 1, \quad (\pm 2)^2 \equiv 4, \quad (\pm 3)^2 \equiv 2$$

jadi himpunan kuadrat modulo $7$ adalah $\{0, 1, 2, 4\}$.

Persamaannya memberi $x^2 + y^2 \equiv 0 \pmod 7$. Periksa semua pasangan dari himpunan itu
yang jumlahnya habis dibagi $7$:

- $1 + 6$: tetapi $6 \notin \{0,1,2,4\}$
- $2 + 5$: tetapi $5 \notin \{0,1,2,4\}$
- $4 + 3$: tetapi $3 \notin \{0,1,2,4\}$
- $0 + 0$: **memenuhi**

Satu-satunya kemungkinan adalah $x^2 \equiv 0$ dan $y^2 \equiv 0 \pmod 7$. Karena $7$
prima, ini memaksa

$$7 \mid x \quad \text{dan} \quad 7 \mid y$$

**Langkah turun.** Tulis $x = 7x_1$ dan $y = 7y_1$. Substitusikan:

$$49x_1^2 + 49y_1^2 = 7z^2 \quad\Longrightarrow\quad 7x_1^2 + 7y_1^2 = z^2$$

Ruas kirinya habis dibagi $7$, jadi $7 \mid z^2$, dan karena $7$ prima, $7 \mid z$. Tulis
$z = 7z_1$:

$$7x_1^2 + 7y_1^2 = 49z_1^2 \quad\Longrightarrow\quad x_1^2 + y_1^2 = 7z_1^2$$

Jadi $(x_1, y_1, z_1) = (x/7,\ y/7,\ z/7)$ juga solusi bulat, dan ia tak nol karena
$(x,y,z)$ tak nol.

**Kontradiksinya.** Tetapi

$$x_1^2 + y_1^2 + z_1^2 = \frac{x^2 + y^2 + z^2}{49} < x^2 + y^2 + z^2$$

bertentangan dengan pemilihan $(x,y,z)$ sebagai yang terkecil.

Jadi tidak ada solusi tak nol, dan satu-satunya solusi bulat adalah $(0,0,0)$.
$\blacksquare$

Yang membuat argumen ini bekerja adalah $7 \equiv 3 \pmod 4$. Untuk prima semacam itu,
$-1$ bukan kuadrat modulo $p$, sehingga $x^2 + y^2 \equiv 0$ memang memaksa keduanya nol.
Bandingkan dengan $p = 5$: di sana $1 + 4 \equiv 0$, dan persamaannya punya solusi tak nol
seperti $(1, 2, 1)$.

## Rubrik

- Mengambil solusi tak nol dengan ukuran terkecil — atau menyusun penurunan tak hingga yang setara
- Mendaftar seluruh nilai kuadrat modulo $7$, yaitu $\{0,1,2,4\}$
- Memeriksa semua pasangan dan menyimpulkan hanya $0 + 0$ yang memenuhi
- Menyimpulkan $7 \mid x$ dan $7 \mid y$, dengan menyebut $7$ prima sebagai alasannya
- Mensubstitusikan dan menurunkan $7 \mid z$ juga — langkah ini sering terlewat
- Menunjukkan solusi barunya bulat, tak nol, dan **benar-benar lebih kecil**, lalu menyatakan kontradiksinya
