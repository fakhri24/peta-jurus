---
id: hmt-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti, kesebangunan]
bentuk: isian
kesulitan: 4
jawaban: "20"
---

## Soal

Pada trapesium $ABCD$ dengan $AB \parallel DC$, diketahui $AB = 30$ dan $DC = 15$. Kedua
diagonalnya berpotongan di $P$. Melalui $P$ ditarik ruas sejajar $AB$ yang memotong kaki $AD$
di $M$ dan kaki $BC$ di $N$.

![Trapesium ABCD dengan sisi AB mendatar di bawah sepanjang 30, dan sisi DC mendatar di atas sepanjang 15, keduanya sejajar. A di kiri bawah, B di kanan bawah, C di kanan atas, D di kiri atas. Kedua diagonalnya, AC dan BD, digambar dan berpotongan di titik P. Melalui P ditarik ruas mendatar sejajar AB; ia memotong kaki kiri AD di titik M dan kaki kanan BC di titik N, sehingga P menjadi titik tengah MN](trapesium-ruas-lewat-potong.svg)

Tentukan panjang $MN$.

## Petunjuk

- Kedua alasnya sejajar, jadi $\triangle PAB$ dan $\triangle PCD$ sebangun dengan $P$ sebagai titik tetapnya. Perbandingan $30 : 15$ itulah yang menentukan letak $P$ pada tiap diagonal.
- Titik $P$ adalah pusat homoteti yang memetakan ruas $AB$ ke ruas $CD$, dengan faktor $-\tfrac{15}{30} = -\tfrac12$ — jadi $AP : PC = 2 : 1$ dan $P$ membagi tiap diagonal $2:1$.
- Hitung $MP$ lewat $\triangle AMP \sim \triangle ADC$, lalu $PN$ dengan cara yang sama dari sisi lain.

## Pembahasan

**Kenali homoteti di $P$.** Karena $AB \parallel DC$, homoteti berpusat $P$ memetakan $A$ ke
$C$ dan $B$ ke $D$. Faktornya nisbah kedua sisi sejajarnya, dengan tanda negatif sebab kedua
bangunnya berseberangan terhadap $P$:

$$k = -\frac{DC}{AB} = -\frac{15}{30} = -\frac12$$

Akibatnya $P$ membagi kedua diagonal dengan perbandingan yang sama:

$$\frac{AP}{PC} = \frac{BP}{PD} = 2 : 1$$

**Hitung $MP$.** Pada $\triangle ADC$, ruas $MP$ sejajar $DC$ dengan $M$ pada $AD$ dan $P$
pada $AC$. Karena $\dfrac{AP}{AC} = \dfrac{2}{3}$:

$$MP = \frac{2}{3} \cdot DC = \frac23 \times 15 = 10$$

**Hitung $PN$.** Pada $\triangle BDC$, ruas $PN$ sejajar $DC$ dengan $P$ pada $BD$ dan $N$
pada $BC$. Karena $\dfrac{BP}{BD} = \dfrac{2}{3}$:

$$PN = \frac{2}{3} \cdot DC = 10$$

**Jumlahkan.**

$$MN = MP + PN = 10 + 10 = \boxed{20}$$

### Yang baru saja terbukti sambil lalu

$MP = PN$, jadi **$P$ adalah titik tengah $MN$**. Itu berlaku pada setiap trapesium, berapa
pun kedua sisi sejajarnya — hasil sampingan yang sering ditanyakan sebagai soal tersendiri.

### Rumus umumnya: rata-rata harmonik

Ulangi langkahnya dengan huruf. Dengan $AB = a$ dan $DC = b$, perbandingannya
$\dfrac{AP}{AC} = \dfrac{a}{a+b}$, sehingga

$$MP = PN = \frac{a}{a+b} \cdot b \quad \Longrightarrow \quad MN = \frac{2ab}{a+b}$$

Itu **rata-rata harmonik** dari kedua sisi sejajarnya. Periksa:
$\dfrac{2 \times 30 \times 15}{45} = \dfrac{900}{45} = 20$ ✓

Bandingkan dengan ruas tengah trapesium — yang menghubungkan titik tengah kedua kakinya —
panjangnya $\dfrac{a+b}{2} = 22{,}5$, yaitu rata-rata **aritmetika**. Dan ruas sejajar yang
membagi trapesium jadi dua bagian sama luas panjangnya $\sqrt{\dfrac{a^2+b^2}{2}}$.

Tiga ruas sejajar, tiga rata-rata berbeda, dan urutannya selalu

$$\underbrace{20}_{\text{harmonik}} \ \le\ \underbrace{22{,}5}_{\text{aritmetika}}$$

Ruas lewat $P$ selalu yang **terpendek** di antara ketiganya.

### Jebakan: memakai $22{,}5$

Kekeliruan paling sering adalah menjawab $\dfrac{30+15}{2} = 22{,}5$ — itu ruas tengah, yang
melalui titik tengah kedua kakinya, **bukan** melalui $P$. Keduanya berimpit hanya kalau
$a = b$, yaitu kalau bangunnya jajaran genjang.

Pemeriksaan cepat: $P$ membagi diagonal $2:1$, jadi tingginya $\tfrac23$ dari alas bawah —
lebih tinggi daripada titik tengah kaki, yang $\tfrac12$. Semakin dekat ke sisi atas yang
pendek, semakin pendek ruasnya. Jadi jawabannya harus **kurang dari** $22{,}5$ ✓

### Kenapa tandanya negatif

Faktor $k = -\tfrac12$, bukan $+\tfrac12$, karena $P$ berada **di antara** $A$ dan $C$. Kalau
tandanya ditulis positif, $C$ akan diletakkan sepihak dengan $A$ terhadap $P$ — dan bangun
yang terbentuk bukan trapesium lagi, melainkan dua ruas yang tumpang tindih.

Yang tidak terpengaruh tanda: perbandingan panjang, sebab yang dipakai $|k|$. Itu sebabnya
perhitungan tadi tetap jalan meski tandanya diabaikan — tetapi pada soal yang menanyakan
letak, tandanya yang menentukan jawabannya.
