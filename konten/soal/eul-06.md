---
id: eul-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler, homoteti]
bentuk: uraian
kesulitan: 5
---

## Soal

Pada segitiga $ABC$ dengan pusat lingkaran luar $O$, titik tinggi $H$, dan jari-jari
lingkaran luar $R$, misalkan $N$ titik tengah $OH$.

![Segitiga ABC lancip dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas. Ketiga garis tingginya digambar putus-putus dan bertemu di titik tinggi H di dalam segitiga. Sebuah lingkaran digambar melalui sembilan titik sekaligus: ketiga titik tengah sisi, ketiga kaki garis tinggi, dan ketiga titik tengah ruas dari H ke tiap titik sudut. Pusatnya N, dan jari-jarinya setengah jari-jari lingkaran luar segitiga. Tiga di antara kesembilan titik itu diberi nama sebagai wakil tiap keluarga: M titik tengah BC, D kaki garis tinggi dari A, dan K titik tengah ruas AH](lingkaran-sembilan-titik.svg)

Buktikan bahwa kesembilan titik berikut terletak pada satu lingkaran berpusat $N$ dan
berjari-jari $\tfrac{R}{2}$:

**(a)** ketiga titik tengah ruas dari $H$ ke tiap titik sudut;

**(b)** ketiga titik tengah sisi;

**(c)** ketiga kaki garis tinggi.

## Petunjuk

- Untuk (a), perhatikan homoteti berpusat $H$ dengan faktor $\tfrac12$. Ke mana ia memetakan $A$, $B$, $C$, dan ke mana ia memetakan lingkaran luar?
- Untuk (b), pakai homoteti berpusat $G$ dengan faktor $-\tfrac12$; ia memetakan titik sudut ke titik tengah sisi. Tunjukkan bahwa pusat lingkaran hasilnya juga $N$.
- Untuk (c), pakai hasil (a) dan (b): tunjukkan titik tengah $BC$ dan titik tengah $AH$ **berseberangan** pada lingkaran itu, lalu ingat bahwa titik yang memandang garis tengah dengan sudut siku-siku ada pada lingkarannya.

## Pembahasan

Pakai vektor dengan $O$ sebagai titik asal, dan modal
$\overrightarrow{OH} = \vec a + \vec b + \vec c$, sehingga

$$\overrightarrow{ON} = \tfrac12\left(\vec a+\vec b+\vec c\right)$$

### Bagian (a) — titik tengah $HA$, $HB$, $HC$

Perhatikan homoteti $h_1$ berpusat $H$ dengan faktor $\tfrac12$.

Bayangan $A$ adalah titik tengah $HA$; begitu pula untuk $B$ dan $C$. Jadi $h_1$ memetakan
ketiga titik sudut ke ketiga titik yang dimaksud bagian (a).

Homoteti memetakan lingkaran ke lingkaran, jadi $h_1$ memetakan lingkaran luar — yang melalui
$A$, $B$, $C$ — ke lingkaran yang melalui ketiga bayangannya. Jari-jarinya
$\tfrac12 R$, dan pusatnya

$$h_1(O) = \text{titik tengah } HO = N$$

Jadi ketiga titik itu ada pada lingkaran berpusat $N$ berjari-jari $\tfrac{R}{2}$
$\blacksquare$

### Bagian (b) — titik tengah sisi

Perhatikan homoteti $h_2$ berpusat $G$ dengan faktor $-\tfrac12$. Karena titik berat membagi
tiap garis berat $2:1$ dari titik sudutnya, $h_2$ memetakan $A$, $B$, $C$ berturut-turut ke
titik tengah $BC$, $CA$, $AB$.

Seperti tadi, $h_2$ memetakan lingkaran luar ke lingkaran berjari-jari $\tfrac{R}{2}$ yang
melalui ketiga titik tengah sisi. Tinggal ditunjukkan pusatnya juga $N$:

$$\overrightarrow{Oh_2(O)} = \overrightarrow{OG} - \tfrac12\left(\overrightarrow{OO} - \overrightarrow{OG}\right)
= \tfrac32\,\overrightarrow{OG}$$

Karena $\overrightarrow{OG} = \tfrac13\left(\vec a+\vec b+\vec c\right)$:

$$\overrightarrow{Oh_2(O)} = \tfrac12\left(\vec a+\vec b+\vec c\right) = \overrightarrow{ON}$$

Jadi $h_2(O) = N$, dan lingkaran hasilnya **sama persis** dengan lingkaran di bagian (a):
pusat sama, jari-jari sama $\blacksquare$

Sampai di sini sudah **enam** titik pada satu lingkaran.

### Bagian (c) — kaki garis tinggi

Misalkan $M$ titik tengah $BC$ dan $K$ titik tengah $AH$; keduanya sudah terbukti ada pada
lingkaran itu.

**Keduanya berseberangan.** Titik tengah $MK$ adalah

$$\tfrac12\left(\overrightarrow{OM} + \overrightarrow{OK}\right)
= \tfrac12\left(\tfrac{\vec b+\vec c}{2} + \tfrac{\vec a + \left(\vec a+\vec b+\vec c\right)}{2}\right)
= \tfrac12\left(\vec a+\vec b+\vec c\right) = \overrightarrow{ON}$$

Jadi $N$ titik tengah $MK$, sehingga $MK$ adalah **garis tengah** lingkaran itu.

**Kaki garis tinggi memandangnya siku-siku.** Misalkan $D$ kaki garis tinggi dari $A$. Titik
$D$ terletak pada $BC$, jadi pada garis $MD$; dan pada garis tinggi $AH$, jadi pada garis
$KD$. Karena garis tinggi tegak lurus $BC$,

$$\angle MDK = 90^\circ$$

Titik yang memandang sebuah garis tengah dengan sudut $90^\circ$ terletak pada lingkarannya —
kebalikan teorema sudut pada setengah lingkaran. Maka $D$ ada pada lingkaran itu.

Hal yang sama berlaku untuk kedua kaki lainnya $\blacksquare$

Kesembilan titik terbukti berada pada satu lingkaran berpusat $N$ berjari-jari $\tfrac{R}{2}$.

### Kasus yang perlu disebut

Argumen bagian (c) memakai segitiga $MDK$, yang menyusut kalau $D$ berimpit dengan $M$ atau
dengan $K$:

- $D = M$ terjadi kalau kaki garis tinggi dari $A$ tepat titik tengah $BC$, yaitu kalau
  $AB = AC$. Di situ $D$ jelas pada lingkarannya, sebab ia **adalah** $M$.
- $D = K$ terjadi kalau $H$ berimpit $D$, yaitu kalau $\angle A = 90^\circ$. Alasannya sama.

Jadi kedua kasus merosot itu tidak merusak apa pun, tetapi menyebutkannya bagian dari bukti
yang lengkap.

### Kenapa dua homoteti yang berbeda memberi lingkaran yang sama

Ini bagian yang paling layak direnungkan. Homoteti $h_1$ berpusat $H$ dan $h_2$ berpusat $G$
sama sekali berbeda — pusatnya lain, faktornya lain ($\tfrac12$ lawan $-\tfrac12$) — namun
keduanya memetakan lingkaran luar ke lingkaran yang **persis sama**.

Sebabnya: kedua homoteti itu memetakan $O$ ke titik yang sama, dan mengalikan jari-jari
dengan besar yang sama. Sebuah lingkaran ditentukan sepenuhnya oleh pusat dan jari-jarinya,
jadi hasilnya tidak bisa berbeda — meski **titik demi titik** keduanya memetakan hal yang
berlainan: $h_1$ membawa $A$ ke titik tengah $AH$, $h_2$ membawa $A$ ke titik tengah $BC$.

Dari situlah keajaiban lingkaran sembilan titik: bukan satu keluarga titik yang kebetulan
selingkaran, melainkan dua keluarga yang tiba di lingkaran yang sama lewat dua jalan berbeda —
dan keluarga ketiga menyusul karena keduanya berpasangan berseberangan.

## Rubrik

- Menetapkan $O$ sebagai titik asal dan menyatakan $\overrightarrow{ON} = \tfrac12(\vec a+\vec b+\vec c)$
- **(a)** Menyebut homoteti berpusat $H$ faktor $\tfrac12$, menyatakan bayangan tiap titik
  sudut, dan menyimpulkan pusat serta jari-jari lingkaran hasilnya
- **(b)** Menyebut homoteti berpusat $G$ faktor $-\tfrac12$ beserta alasan ia memetakan titik
  sudut ke titik tengah sisi
- **(b)** Menghitung $h_2(O)$ dan menunjukkan hasilnya sama dengan $N$, lalu menyimpulkan
  kedua lingkarannya berimpit
- **(c)** Membuktikan $N$ titik tengah $MK$, sehingga $MK$ garis tengah
- **(c)** Menyatakan $\angle MDK = 90^\circ$ **beserta alasan** $D$ ada pada garis $BC$ dan
  pada garis tinggi
- **(c)** Memakai kebalikan teorema sudut pada setengah lingkaran untuk menyimpulkan $D$ pada
  lingkarannya
- Menyebut kasus merosot $D = M$ dan $D = K$

Bukti yang hanya mengerjakan (a) dan (b) memperoleh enam titik dan dinilai sebagian: bagian
(c) yang paling sering dilewatkan, dan justru ia yang membuat namanya "sembilan titik".
