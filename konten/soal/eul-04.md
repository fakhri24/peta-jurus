---
id: eul-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler, titik-istimewa]
bentuk: uraian
kesulitan: 5
---

## Soal

Pada segitiga $ABC$ yang bukan sama sisi, misalkan $O$ pusat lingkaran luar, $G$ titik berat,
dan $H$ titik tinggi.

Buktikan bahwa $O$, $G$, dan $H$ terletak pada satu garis, dan bahwa

$$HG : GO = 2 : 1$$

## Petunjuk

- Pakai vektor dengan $O$ sebagai titik asal. Titik berat mudah ditulis begitu: $\overrightarrow{OG} = \tfrac13\left(\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}\right)$.
- Untuk $H$, jangan mencarinya — **tebak** dulu titik $P$ dengan $\overrightarrow{OP} = \overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}$, lalu buktikan $P$ memang titik tinggi.
- Untuk membuktikan $P$ titik tinggi, cukup tunjukkan $\overrightarrow{AP} \perp \overrightarrow{BC}$ dan seterusnya. Pakai $\left|\overrightarrow{OA}\right| = \left|\overrightarrow{OB}\right| = \left|\overrightarrow{OC}\right| = R$.

## Pembahasan

Tulis $\vec a = \overrightarrow{OA}$, $\vec b = \overrightarrow{OB}$, $\vec c = \overrightarrow{OC}$,
dengan $O$ sebagai titik asal. Karena $O$ pusat lingkaran luar,

$$\left|\vec a\right| = \left|\vec b\right| = \left|\vec c\right| = R$$

**Langkah 1 — tebak titik tingginya.** Perhatikan titik $P$ dengan

$$\overrightarrow{OP} = \vec a + \vec b + \vec c$$

Akan ditunjukkan $P = H$.

**Langkah 2 — buktikan $AP \perp BC$.**

$$\overrightarrow{AP} = \overrightarrow{OP} - \vec a = \vec b + \vec c, \qquad
\overrightarrow{BC} = \vec c - \vec b$$

Hasil kali titiknya:

$$\left(\vec b + \vec c\right)\cdot\left(\vec c - \vec b\right)
= \left|\vec c\right|^2 - \left|\vec b\right|^2 = R^2 - R^2 = 0$$

Jadi $AP \perp BC$, sehingga $P$ terletak pada garis tinggi dari $A$.

Perhatikan bahwa satu-satunya keterangan yang dipakai adalah $\left|\vec b\right| =
\left|\vec c\right|$ — yaitu bahwa $O$ berjarak sama ke $B$ dan $C$. Di situlah sifat pusat
lingkaran luar masuk.

**Langkah 3 — ulangi untuk dua sisi lainnya.** Karena bentuk $\vec a + \vec b + \vec c$
setangkup terhadap ketiga hurufnya, perhitungan yang sama memberi $BP \perp CA$ dan
$CP \perp AB$. Jadi $P$ terletak pada **ketiga** garis tinggi, sehingga

$$P = H, \qquad \text{yaitu} \qquad \overrightarrow{OH} = \vec a + \vec b + \vec c$$

**Langkah 4 — bandingkan dengan titik berat.** Menurut rumus titik berat,

$$\overrightarrow{OG} = \tfrac13\left(\vec a + \vec b + \vec c\right)$$

Maka

$$\overrightarrow{OH} = 3\,\overrightarrow{OG}$$

Kedua vektor itu **sejajar** dan berpangkal di titik yang sama, jadi $O$, $G$, $H$ segaris
$\blacksquare$

**Langkah 5 — perbandingannya.** Dari $\overrightarrow{OH} = 3\overrightarrow{OG}$:

$$\overrightarrow{GH} = \overrightarrow{OH} - \overrightarrow{OG} = 2\,\overrightarrow{OG}$$

Karena $\overrightarrow{GH}$ dan $\overrightarrow{OG}$ searah dengan panjang berbanding
$2 : 1$, titik $G$ berada **di antara** $O$ dan $H$ dengan

$$HG : GO = 2 : 1 \qquad \blacksquare$$

### Kenapa "menebak lalu memeriksa" itu sah

Langkah 1 terlihat seperti kebetulan yang beruntung, tetapi ia bentuk pembuktian yang lengkap:
sebuah titik didefinisikan dengan rumus, lalu **dibuktikan** memenuhi sifat yang
mendefinisikan titik tinggi. Tidak ada yang diandaikan.

Yang membuatnya sah adalah ketunggalan: titik tinggi didefinisikan sebagai perpotongan ketiga
garis tinggi, dan ketiga garis itu berpotongan di paling banyak satu titik. Begitu $P$
terbukti ada di ketiganya, $P$ **adalah** titik tingginya.

Pola ini berulang di seluruh geometri olimpiade, dan sering jauh lebih pendek daripada
mencari titiknya dari nol.

### Cara kedua: lewat homoteti

Perhatikan homoteti $h$ berpusat $G$ dengan faktor $-\tfrac12$. Ia memetakan $A$, $B$, $C$
berturut-turut ke titik tengah sisi seberangnya, jadi ia memetakan $\triangle ABC$ ke
**segitiga titik tengah**.

Sekarang perhatikan garis tinggi segitiga titik tengah. Garis tinggi dari titik tengah $BC$
tegak lurus sisi seberangnya, yaitu ruas yang menghubungkan titik tengah $CA$ dan $AB$ —
dan ruas itu sejajar $BC$. Jadi garis tinggi itu adalah garis lewat titik tengah $BC$ yang
tegak lurus $BC$, yakni **garis sumbu** $BC$.

Ketiga garis tinggi segitiga titik tengah karena itu adalah ketiga garis sumbu
$\triangle ABC$, yang bertemu di $O$. Maka titik tinggi segitiga titik tengah adalah $O$.

Karena homoteti memetakan titik tinggi ke titik tinggi,

$$h(H) = O \quad \Longrightarrow \quad \overrightarrow{GO} = -\tfrac12\,\overrightarrow{GH}$$

yang persis memberi kesegarisan beserta perbandingan $2 : 1$ ✓

Bukti ini tidak memakai vektor sama sekali, dan ia menjelaskan **mengapa** angkanya $2:1$:
karena faktor homotetinya $-\tfrac12$.

### Kenapa "bukan sama sisi" disyaratkan

Untuk segitiga sama sisi, $O = G = H$ menyatu di satu titik. Pernyataan "terletak pada satu
garis" jadi hampa — tiga titik yang berimpit ada pada tak hingga banyak garis, dan tidak ada
satu pun yang layak disebut garis Euler.

Perbandingan $HG : GO$ pun menjadi $0 : 0$, yang tidak terdefinisi. Bukti di atas tetap sah
sampai Langkah 4; yang gugur cuma penamaan garisnya.

## Rubrik

- Menetapkan $O$ sebagai titik asal dan menyatakan $\left|\vec a\right| = \left|\vec b\right|
  = \left|\vec c\right| = R$ sebagai sifat pusat lingkaran luar
- Mendefinisikan $P$ lewat $\overrightarrow{OP} = \vec a+\vec b+\vec c$ dan menyatakan bahwa
  yang akan dibuktikan adalah $P = H$
- Menghitung $\overrightarrow{AP}\cdot\overrightarrow{BC} = 0$ lengkap dengan penjabarannya
- Menyebut bahwa kesetangkupan bentuknya memberi dua hubungan tegak lurus lainnya, sehingga
  $P$ ada di ketiga garis tinggi
- Menyatakan ketunggalan titik tinggi sebagai alasan menyimpulkan $P = H$
- Menuliskan $\overrightarrow{OG} = \tfrac13(\vec a+\vec b+\vec c)$ dan menyimpulkan
  $\overrightarrow{OH} = 3\overrightarrow{OG}$, lalu kesegarisannya
- Menurunkan $\overrightarrow{GH} = 2\overrightarrow{OG}$ dan menyatakan $G$ berada **di
  antara** $O$ dan $H$, bukan hanya nisbah panjangnya

Bukti lewat homoteti dinilai penuh, asalkan langkah "garis tinggi segitiga titik tengah
adalah garis sumbu $\triangle ABC$" dibuktikan, bukan sekadar dinyatakan.
