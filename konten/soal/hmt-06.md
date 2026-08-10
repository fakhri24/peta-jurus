---
id: hmt-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti, titik-istimewa]
bentuk: uraian
kesulitan: 5
---

## Soal

Pada segitiga $ABC$, misalkan $G$ titik beratnya dan $M_A$, $M_B$, $M_C$ berturut-turut titik
tengah sisi $BC$, $CA$, $AB$. Segitiga $M_AM_BM_C$ disebut **segitiga titik tengah**.

**(a)** Buktikan bahwa homoteti berpusat $G$ dengan faktor $-\tfrac12$ memetakan $A$ ke
$M_A$, $B$ ke $M_B$, dan $C$ ke $M_C$.

**(b)** Simpulkan bahwa jari-jari lingkaran luar segitiga titik tengah adalah $\tfrac{R}{2}$,
dengan $R$ jari-jari lingkaran luar $\triangle ABC$.

**(c)** Simpulkan bahwa pusat lingkaran luar segitiga titik tengah terletak pada garis yang
melalui $G$ dan $O$, dan tentukan letaknya pada garis itu.

## Petunjuk

- Untuk (a), pakai sifat titik berat: ia membagi tiap garis berat $2:1$ dari titik sudutnya. Nyatakan itu sebagai hubungan antara $\overrightarrow{GA}$ dan $\overrightarrow{GM_A}$.
- Untuk (b), homoteti memetakan lingkaran ke lingkaran dengan jari-jari dikalikan $|k|$. Lingkaran mana terpetakan ke lingkaran mana?
- Untuk (c), pusat lingkaran terpetakan ke pusat lingkaran. Terapkan definisi homoteti pada titik $O$.

## Pembahasan

### Bagian (a)

**Pakai sifat titik berat.** Titik $G$ terletak pada garis berat $AM_A$ dan membaginya dengan
perbandingan $AG : GM_A = 2 : 1$. Karena $G$ berada **di antara** $A$ dan $M_A$, kedua vektor
$\overrightarrow{GA}$ dan $\overrightarrow{GM_A}$ berlawanan arah, sehingga

$$\overrightarrow{GM_A} = -\frac12\,\overrightarrow{GA}$$

Itu persis definisi homoteti berpusat $G$ dengan faktor $-\tfrac12$, jadi $A \mapsto M_A$.

Hal yang sama berlaku untuk garis berat $BM_B$ dan $CM_C$, sebab $G$ membagi ketiganya dengan
perbandingan yang sama. Maka $B \mapsto M_B$ dan $C \mapsto M_C$ $\blacksquare$

Sebut homoteti itu $h$.

### Bagian (b)

Homoteti memetakan lingkaran ke lingkaran, dan memetakan sebuah lingkaran yang melalui tiga
titik ke lingkaran yang melalui ketiga bayangannya.

Lingkaran luar $\triangle ABC$ melalui $A$, $B$, $C$. Bayangannya di bawah $h$ adalah
lingkaran yang melalui $M_A$, $M_B$, $M_C$ — yaitu **lingkaran luar segitiga titik tengah**.

Homoteti mengalikan panjang dengan $|k|$, jadi jari-jarinya menjadi

$$\left|-\tfrac12\right| \cdot R = \frac{R}{2} \qquad \blacksquare$$

### Bagian (c)

Pusat lingkaran terpetakan ke pusat bayangannya, sebab homoteti memetakan seluruh bangun
secara serentak. Sebut $N$ pusat lingkaran luar segitiga titik tengah, maka

$$N = h(O), \qquad \text{yaitu} \qquad \overrightarrow{GN} = -\frac12\,\overrightarrow{GO}$$

Dari situ langsung: $N$ berada pada garis $GO$, di **seberang** $O$ terhadap $G$, dengan

$$GN = \frac12\,GO \qquad \blacksquare$$

Garis $GO$ itu tak lain **garis Euler** segitiga $ABC$, dan $N$ ternyata pusat **lingkaran
sembilan titik** — tetapi itu jurus berikutnya. Yang sudah terbukti di sini: ia ada di garis
yang sama, jari-jarinya $\tfrac{R}{2}$, dan letaknya tertentu.

### Periksa pada segitiga yang bisa dihitung

Ambil $A(0,0)$, $B(4,0)$, $C(0,3)$ — siku-siku di $A$, jadi $R = \tfrac{BC}{2} = 2{,}5$ dan
$O$ titik tengah $BC$, yaitu $(2;\ 1{,}5)$.

$$G = \left(\tfrac{0+4+0}{3},\ \tfrac{0+0+3}{3}\right) = \left(\tfrac43,\ 1\right)$$

Titik tengah sisinya: $M_A(2;\ 1{,}5)$, $M_B(0;\ 1{,}5)$, $M_C(2;\ 0)$.

Periksa (a) pada $A$: $\overrightarrow{GA} = \left(-\tfrac43,\ -1\right)$, dan
$-\tfrac12 \overrightarrow{GA} = \left(\tfrac23,\ \tfrac12\right)$, sehingga
$G + \left(\tfrac23, \tfrac12\right) = \left(2;\ 1{,}5\right) = M_A$ ✓

Periksa (b): sisi $\triangle M_AM_BM_C$ adalah $2$, $1{,}5$, $2{,}5$ — separuh dari $4$, $3$,
$5$, dan siku-siku juga. Jari-jari luarnya $\tfrac{2{,}5}{2} = 1{,}25 = \tfrac{R}{2}$ ✓

Periksa (c): $N = h(O) = G - \tfrac12\left(O - G\right) = \left(\tfrac43,1\right) -
\tfrac12\left(\tfrac23,\ \tfrac12\right) = \left(1;\ 0{,}75\right)$. Jarak $N$ ke ketiga titik
tengah: ke $M_A(2;1{,}5)$ adalah $\sqrt{1 + 0{,}5625} = 1{,}25$ ✓, ke $M_B(0;1{,}5)$ adalah
$\sqrt{1+0{,}5625} = 1{,}25$ ✓, ke $M_C(2;0)$ adalah $\sqrt{1+0{,}5625} = 1{,}25$ ✓

Ketiganya sama, jadi $N$ memang pusatnya, dan jari-jarinya memang $\tfrac{R}{2}$.

### Kenapa faktornya negatif, dan kenapa itu penting

Faktor $-\tfrac12$, bukan $+\tfrac12$, karena $G$ terletak **di antara** tiap titik sudut dan
titik tengah sisi seberangnya. Tanda itulah yang membuat segitiga titik tengah tampak
**terbalik** terhadap aslinya — sisi $M_BM_C$ sejajar $BC$ tetapi arah kelilingnya berbalik.

Kalau tandanya ditulis positif, bagian (b) tetap keluar benar — sebab jari-jari memakai
$|k|$. Yang keliru bagian (c): $N$ akan diletakkan sepihak dengan $O$ terhadap $G$, di tempat
yang salah pada garis Euler.

Itu pola umum: **tanda $k$ tidak pernah mengubah panjang, tetapi hampir selalu mengubah
letak.**

### Ke mana ini bermuara

Bagian (c) baru saja menempatkan tiga titik pada satu garis: $G$, $O$, dan $N$. Jurus
berikutnya menambahkan yang keempat, titik tinggi $H$, dan menunjukkan bahwa $N$ tepat titik
tengah $OH$ — sehingga lingkaran berjari-jari $\tfrac{R}{2}$ yang baru ditemukan ternyata
melalui sembilan titik, bukan tiga.

Homoteti yang mengerjakannya di situ juga homoteti ini, dipandang dari pusat yang berbeda.

## Rubrik

- **(a)** Menyatakan sifat titik berat $AG : GM_A = 2 : 1$ dan menyebut bahwa $G$ berada di
  antara keduanya
- **(a)** Menerjemahkannya menjadi $\overrightarrow{GM_A} = -\tfrac12 \overrightarrow{GA}$
  dan mengenalinya sebagai definisi homoteti
- **(a)** Menyatakan bahwa hal yang sama berlaku untuk dua titik sudut lainnya
- **(b)** Menyatakan bahwa lingkaran luar $\triangle ABC$ terpetakan ke lingkaran luar
  $\triangle M_AM_BM_C$, dengan alasan homoteti memetakan lingkaran melalui tiga titik ke
  lingkaran melalui ketiga bayangannya
- **(b)** Memakai $|k| = \tfrac12$ untuk memperoleh jari-jarinya
- **(c)** Menyatakan $N = h(O)$ dengan alasan pusat terpetakan ke pusat
- **(c)** Menuliskan $\overrightarrow{GN} = -\tfrac12 \overrightarrow{GO}$ dan menyimpulkan
  letak $N$ pada garis $GO$ **beserta sisinya**, bukan hanya jaraknya

Jawaban (c) yang hanya menyebut $GN = \tfrac12 GO$ tanpa menyatakan $N$ berada di seberang
$O$ dinilai belum lengkap: ada dua titik pada garis itu yang berjarak segitu dari $G$.
