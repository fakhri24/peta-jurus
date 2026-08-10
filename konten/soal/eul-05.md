---
id: eul-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler]
bentuk: uraian
kesulitan: 5
---

## Soal

Pada segitiga $ABC$ dengan sisi $a$, $b$, $c$, jari-jari lingkaran luar $R$, pusat lingkaran
luar $O$, dan titik tinggi $H$.

**(a)** Buktikan bahwa

$$OH^2 = 9R^2 - \left(a^2+b^2+c^2\right)$$

**(b)** Simpulkan bahwa $a^2+b^2+c^2 \le 9R^2$, dan tentukan kapan kesamaannya tercapai.

## Petunjuk

- Pakai vektor dengan $O$ sebagai titik asal, dan modal $\overrightarrow{OH} = \vec a + \vec b + \vec c$.
- Jabarkan $\left|\vec a+\vec b+\vec c\right|^2$; akan muncul suku hasil kali titik seperti $\vec a \cdot \vec b$.
- Nyatakan tiap hasil kali titik dengan panjang sisi: dari $c^2 = \left|\vec a - \vec b\right|^2$ diperoleh $\vec a \cdot \vec b = R^2 - \tfrac{c^2}{2}$.

## Pembahasan

### Bagian (a)

Tulis $\vec a = \overrightarrow{OA}$, $\vec b = \overrightarrow{OB}$,
$\vec c = \overrightarrow{OC}$ dengan $O$ sebagai titik asal, sehingga
$\left|\vec a\right| = \left|\vec b\right| = \left|\vec c\right| = R$.

**Langkah 1 — jabarkan.** Dari $\overrightarrow{OH} = \vec a + \vec b + \vec c$:

$$OH^2 = \left|\vec a+\vec b+\vec c\right|^2
= \left|\vec a\right|^2 + \left|\vec b\right|^2 + \left|\vec c\right|^2
+ 2\left(\vec a\cdot\vec b + \vec b\cdot\vec c + \vec c\cdot\vec a\right)$$

$$= 3R^2 + 2\left(\vec a\cdot\vec b + \vec b\cdot\vec c + \vec c\cdot\vec a\right)$$

**Langkah 2 — ubah hasil kali titik jadi panjang sisi.** Sisi $AB$ adalah selisih kedua
vektornya:

$$c^2 = \left|\vec a - \vec b\right|^2 = \left|\vec a\right|^2 + \left|\vec b\right|^2
- 2\,\vec a\cdot\vec b = 2R^2 - 2\,\vec a\cdot\vec b$$

$$\vec a\cdot\vec b = R^2 - \frac{c^2}{2}$$

Dengan cara yang sama $\vec b\cdot\vec c = R^2 - \dfrac{a^2}{2}$ dan
$\vec c\cdot\vec a = R^2 - \dfrac{b^2}{2}$.

**Langkah 3 — jumlahkan dan rapikan.**

$$\vec a\cdot\vec b + \vec b\cdot\vec c + \vec c\cdot\vec a
= 3R^2 - \frac{a^2+b^2+c^2}{2}$$

$$OH^2 = 3R^2 + 2\left(3R^2 - \frac{a^2+b^2+c^2}{2}\right) = 9R^2 - \left(a^2+b^2+c^2\right)
\qquad \blacksquare$$

### Bagian (b)

Ruas kiri $OH^2$ adalah kuadrat sebuah panjang, jadi tak negatif:

$$9R^2 - \left(a^2+b^2+c^2\right) \ \ge\ 0 \quad \Longrightarrow \quad
a^2+b^2+c^2 \ \le\ 9R^2$$

**Syarat kesamaan.** Kesamaan berlaku tepat ketika $OH = 0$, yaitu $O = H$.

Tunjukkan bahwa itu memaksa segitiganya sama sisi. Kalau $O = H$, maka
$\vec a+\vec b+\vec c = \vec 0$, sehingga juga $\overrightarrow{OG} = \vec 0$ dan $G = O$.
Karena $G = O$, tiap garis berat berimpit dengan garis sumbu sisi yang bersangkutan:
garis berat dari $A$ melalui $O$ dan titik tengah $BC$, sedangkan garis sumbu $BC$ juga
melalui keduanya. Maka garis berat dari $A$ tegak lurus $BC$, dan segitiga yang garis
beratnya sekaligus garis tinggi adalah sama kaki dengan $AB = AC$.

Hal yang sama berlaku dari $B$, jadi $BA = BC$ juga. Ketiga sisinya sama, dan segitiganya
sama sisi.

Sebaliknya, untuk segitiga sama sisi bersisi $s$ berlaku $R = \dfrac{s}{\sqrt3}$, sehingga

$$9R^2 = 9 \cdot \frac{s^2}{3} = 3s^2 = a^2+b^2+c^2 \quad ✓$$

Jadi kesamaannya tercapai **tepat** pada segitiga sama sisi $\blacksquare$

### Periksa pada dua segitiga

**Siku-siku $6$-$8$-$10$.** Di sini $R = 5$ (sisi miring garis tengah), dan
$a^2+b^2+c^2 = 36+64+100 = 200$:

$$OH^2 = 9(25) - 200 = 25 \quad \Longrightarrow \quad OH = 5$$

Cocok dengan yang bisa dilihat langsung: pada segitiga siku-siku, $H$ berimpit dengan titik
sudut siku-sikunya dan $O$ titik tengah sisi miring, jadi $OH$ tak lain jari-jarinya, $5$ ✓

**Segitiga $7$-$13$-$15$.** Dengan $R^2 = \tfrac{169}{3}$:

$$OH^2 = 507 - 443 = 64 \quad \Longrightarrow \quad OH = 8$$

### Apa yang sebenarnya dikatakan bagian (b)

Ketaksamaan $a^2+b^2+c^2 \le 9R^2$ berbunyi: **di antara semua segitiga dengan lingkaran luar
yang sama, yang sama sisi punya jumlah kuadrat sisi terbesar.**

Itu sekaligus contoh pola yang berulang di ketaksamaan geometri: sebuah **kesamaan** yang
ruas kirinya kuadrat — yaitu tak negatif — langsung melahirkan ketaksamaan beserta syarat
kesamaannya, tanpa perlu teknik ketaksamaan sama sekali.

Bandingkan dengan ketaksamaan Euler $R \ge 2r$, yang lahir dengan cara yang persis sama dari
kesamaan $OI^2 = R^2 - 2Rr$.

### Bentuk lain rumus yang sama

Karena $a = 2R\sin A$ dan seterusnya, rumus bagian (a) bisa ditulis

$$OH^2 = R^2\left(9 - 4\left(\sin^2 A + \sin^2 B + \sin^2 C\right)\right)$$

dan dengan identitas segitiga $\sin^2 A+\sin^2 B+\sin^2 C = 2 + 2\cos A\cos B\cos C$ ia
menjadi

$$OH^2 = R^2\left(1 - 8\cos A\cos B\cos C\right)$$

Bentuk terakhir itu yang paling sering dikutip, dan ia langsung memperlihatkan bahwa
$OH < R$ tepat ketika $\cos A\cos B\cos C > 0$ — yaitu ketika segitiganya lancip.

## Rubrik

- Menetapkan $O$ sebagai titik asal, menyatakan ketiga vektornya berpanjang $R$, dan memakai
  $\overrightarrow{OH} = \vec a+\vec b+\vec c$
- **(a)** Menjabarkan $\left|\vec a+\vec b+\vec c\right|^2$ lengkap dengan suku hasil kali
  titiknya
- **(a)** Menurunkan $\vec a\cdot\vec b = R^2 - \tfrac{c^2}{2}$ dari $c^2 = \left|\vec a-\vec b\right|^2$,
  dan menyebut kedua bentuk lainnya
- **(a)** Menjumlahkan dan menyederhanakan sampai bentuk yang diminta
- **(b)** Memakai $OH^2 \ge 0$ untuk memperoleh ketaksamaannya
- **(b)** Menyatakan kesamaan setara dengan $O = H$
- **(b)** Membuktikan $O = H$ memaksa segitiganya sama sisi — bukan sekadar menyebutkannya —
  dan memeriksa arah sebaliknya dengan perhitungan pada segitiga sama sisi

Menyebut "kesamaan tercapai pada segitiga sama sisi" tanpa membuktikan kedua arahnya dinilai
belum lengkap: soal ketaksamaan menuntut ditunjukkan bahwa batasnya benar-benar tercapai.
