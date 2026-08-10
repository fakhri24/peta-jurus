---
id: ksb-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kesebangunan]
bentuk: uraian
kesulitan: 3
---

## Soal

Pada segitiga $ABC$, titik $M$ adalah titik tengah $AB$ dan titik $N$ adalah titik tengah $AC$.

Buktikan bahwa $MN$ sejajar $BC$ dan $MN = \tfrac{1}{2} BC$.

## Petunjuk

- Yang diminta dua hal sekaligus — kesejajaran dan panjang. Cari satu pernyataan yang menghasilkan keduanya sekaligus, bukan dua pernyataan terpisah.
- Bandingkan $\triangle AMN$ dengan $\triangle ABC$. Keduanya berbagi sudut di $A$, dan dua pasang sisi yang mengapitnya sebanding.
- Setelah kesebangunannya didapat, panjangnya langsung terbaca dari nisbahnya, dan kesejajarannya dari sudut sehadap.

## Pembahasan

**Bandingkan $\triangle AMN$ dengan $\triangle ABC$.**

Karena $M$ titik tengah $AB$ dan $N$ titik tengah $AC$,

$$\frac{AM}{AB} = \frac{1}{2}, \qquad \frac{AN}{AC} = \frac{1}{2}$$

Kedua nisbah itu sama. Ditambah sudut di $A$ yang **dipakai bersama** kedua segitiga — dan
sudut itu tepat terapit oleh keempat sisi tersebut — susunannya S-Sd-S:

$$\triangle AMN \sim \triangle ABC \quad \text{dengan nisbah } k = \tfrac{1}{2}$$

**Panjangnya.** Sisi $MN$ bersesuaian dengan sisi $BC$, sehingga

$$MN = k \times BC = \tfrac{1}{2} BC$$

**Kesejajarannya.** Dari kesebangunan itu, sudut bersesuaian sama besar:

$$\angle AMN = \angle ABC$$

Keduanya sudut **sehadap** pada garis $MN$ dan $BC$ yang dipotong garis $AB$. Sudut sehadap
yang sama besar berarti kedua garisnya sejajar:

$$MN \parallel BC$$

Kedua bagian terbukti. $\blacksquare$

### Satu kesebangunan, dua kesimpulan

Perhatikan bahwa kesejajaran dan panjang **tidak dibuktikan terpisah**. Keduanya keluar dari
satu pernyataan kesebangunan: yang satu dari nisbah sisinya, yang lain dari sudut yang
bersesuaian.

Itu ciri khas kesebangunan sebagai alat — ia menyimpulkan tentang sudut dan panjang sekaligus,
sedangkan kekongruenan hanya berguna kalau ukurannya memang sama persis.

### Perhatikan arah pembuktian kesejajarannya

Kesejajaran **disimpulkan dari** sudut yang sama besar, bukan sebaliknya. Menulis
"karena $MN \parallel BC$ maka $\triangle AMN \sim \triangle ABC$" adalah berputar: kesejajaran
itu justru yang sedang dibuktikan, dan memakainya sebagai bahan membuat seluruh buktinya tidak
membuktikan apa pun.

Urutan yang benar: nisbah sisi $\rightarrow$ sebangun $\rightarrow$ sudut sama besar
$\rightarrow$ sejajar.

### Akibat yang dipakai berulang kali

Ketiga garis tengah sebuah segitiga membelahnya menjadi **empat** segitiga kecil yang semuanya
kongruen dan sebangun dengan segitiga semula, masing-masing dengan nisbah $\tfrac{1}{2}$.
Luas tiap bagiannya karena itu $\left(\tfrac{1}{2}\right)^2 = \tfrac{1}{4}$ dari luas semula —
cocok dengan kenyataan bahwa keempatnya menutupi seluruh segitiga.

Segitiga yang dibentuk ketiga titik tengahnya disebut segitiga tengah, dan ia muncul lagi di
tahap-tahap berikutnya, antara lain pada lingkaran sembilan titik.

## Rubrik

- Menyatakan $\dfrac{AM}{AB} = \dfrac{AN}{AC} = \dfrac{1}{2}$ dari kedua titik tengah
- Menyebut sudut di $A$ dipakai bersama, dan bahwa ia terapit kedua pasang sisi tersebut
- Menyimpulkan $\triangle AMN \sim \triangle ABC$ dengan menyebut alasannya S-Sd-S
- Menurunkan $MN = \tfrac{1}{2} BC$ dari nisbah kesebangunannya
- Menurunkan $\angle AMN = \angle ABC$, lalu menyimpulkan kesejajaran lewat sudut sehadap
- Tidak memakai kesejajaran $MN \parallel BC$ sebagai bahan bukti, sebab itu yang hendak dibuktikan
