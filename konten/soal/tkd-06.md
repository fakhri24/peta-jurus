---
id: tkd-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan, garis-singgung]
bentuk: uraian
kesulitan: 5
---

## Soal

Diberikan lingkaran $\omega$ berpusat $O$ berjari-jari $R$, dan sebuah garis $\ell$ yang
seluruhnya berada di luar $\omega$. Jarak $O$ ke $\ell$ adalah $d$, jadi $d > R$.

Untuk setiap titik $P$ pada $\ell$, tarik kedua garis singgung dari $P$ ke $\omega$,
menyentuhnya di $X$ dan $Y$.

![Sebuah lingkaran berpusat O di sebelah kiri, dan sebuah garis tegak bernama l di sebelah kanan yang tidak menyentuh lingkaran itu sama sekali. Titik P berada pada garis l, agak di atas ketinggian O. Dari P ditarik dua garis singgung ke lingkaran, menyentuhnya di X pada sisi atas dan Y pada sisi bawah. Ruas XY digambar tebal sebagai tali busur yang menghubungkan kedua titik singgung itu, memotong daerah antara O dan P. Jari-jari OX dan OY digambar putus-putus, dan pada X maupun Y diberi tanda siku-siku yang menyatakan bahwa jari-jari tegak lurus garis singgungnya](singgung-dari-titik-pada-garis.svg)

**(a)** Buktikan bahwa garis $XY$ selalu melalui satu titik tetap, dan tentukan letak
titik itu.

**(b)** Tunjukkan bahwa titik tetap itu berada di dalam $\omega$.

## Petunjuk

- Yang tetap dalam soal ini cuma $O$, $R$, dan $\ell$. Jadi titik tetapnya hanya boleh bergantung pada ketiganya — dan menurut kesetangkupan, ia mestinya ada pada garis dari $O$ yang tegak lurus $\ell$.
- Pakai koordinat. Taruh $O$ di pangkal dan $\ell$ sebagai garis tegak $x = d$. Cari satu persamaan yang dipenuhi $X$ maupun $Y$.
- Singgung berarti $OX \perp XP$. Tuliskan itu sebagai hasil kali titik, lalu pakai $|X|^2 = R^2$.
- Kalau syarat itu berbunyi $X \cdot P = R^2$ dan $Y \cdot P = R^2$, maka $X$ dan $Y$ dua-duanya memenuhi satu persamaan **linear** — jadi persamaan itu adalah persamaan garis $XY$.

## Pembahasan

### Bagian (a)

**Beri koordinat.** Taruh $O = (0,0)$ dan $\ell$ sebagai garis $x = d$. Sebuah titik pada
$\ell$ berbentuk

$$P = (d, p) \qquad (p \text{ bebas})$$

**Ubah syarat singgung jadi persamaan.** Titik $X$ adalah titik singgung, jadi jari-jari
$OX$ tegak lurus garis singgung $XP$:

$$\vec{OX} \cdot \vec{XP} = 0$$

Tulis dengan vektor posisi, $\vec{OX} = X$ dan $\vec{XP} = P - X$:

$$X \cdot (P - X) = 0 \quad \Longrightarrow \quad X \cdot P = |X|^2 = R^2$$

sebab $X$ ada pada $\omega$. Jadi

$$X \cdot P = R^2$$

Alasan yang sama berlaku untuk $Y$:

$$Y \cdot P = R^2$$

**Kenali persamaannya.** Untuk $P$ yang sudah tertentu, pandang

$$Q \cdot P = R^2$$

sebagai syarat atas titik $Q = (x,y)$. Dengan $P = (d,p)$ ia berbunyi

$$dx + py = R^2$$

Itu persamaan **derajat satu**, jadi himpunan penyelesaiannya sebuah garis. Karena $X$
dan $Y$ dua-duanya memenuhinya dan $X \ne Y$, garis itu tidak lain garis $XY$.

**Cari titik tetapnya.** Yang dicari adalah titik $T$ yang memenuhi persamaan tersebut
untuk **setiap** $p$. Tulis ulang:

$$dx - R^2 + py = 0 \qquad \text{untuk semua } p$$

Ruas kiri adalah fungsi linear dalam $p$; supaya ia nol untuk semua $p$, koefisien $p$
harus nol dan sisanya juga harus nol:

$$y = 0 \qquad \text{dan} \qquad dx = R^2$$

Jadi ada tepat satu titik seperti itu:

$$T = \left(\frac{R^2}{d},\ 0\right)$$

Setiap garis $XY$ melalui $T$ $\blacksquare$

Dalam bahasa tanpa koordinat: $T$ terletak pada ruas dari $O$ yang tegak lurus $\ell$,
dengan

$$OT = \frac{R^2}{d}$$

### Bagian (b)

Karena $d > R$,

$$OT = \frac{R^2}{d} \ <\ \frac{R^2}{R} = R$$

Jadi $OT < R$, artinya $T$ berada **di dalam** $\omega$ $\blacksquare$

Itu masuk akal: $XY$ adalah tali busur $\omega$, dan setiap titik pada tali busur ada di
dalam lingkarannya. Kalau hitungan memberi $OT > R$, pasti ada yang salah — pemeriksaan
yang murah.

### Bukti sintetik, untuk perbandingan

Sebut $F$ kaki tegak lurus dari $O$ ke $\ell$, jadi $OF = d$. Sebut $M$ titik potong
$XY$ dengan $OP$.

Karena $X$ dan $Y$ setangkup terhadap garis $OP$, tali busur $XY$ tegak lurus $OP$ dan
$M$ titik tengahnya. Pada segitiga $OXP$ yang siku-siku di $X$, ruas $XM$ adalah garis
tinggi ke sisi miringnya, sehingga

$$OX^2 = OM \cdot OP \quad \Longrightarrow \quad OM \cdot OP = R^2$$

Sekarang sebut $T$ titik potong $XY$ dengan $OF$. Segitiga $OMT$ dan $OFP$ punya sudut
$O$ yang sama, dan keduanya siku-siku — di $M$ dan di $F$. Jadi keduanya sebangun:

$$\frac{OT}{OP} = \frac{OM}{OF} \quad \Longrightarrow \quad
OT = \frac{OM \cdot OP}{OF} = \frac{R^2}{d}$$

tidak bergantung pada $P$ ✓

Bukti ini memperlihatkan **mengapa** hasilnya begitu — kuasa titik $OM \cdot OP = R^2$
yang mengerjakan seluruhnya — sedangkan bukti koordinat memperlihatkan bahwa titik
tetapnya tunggal, dan itu tidak gratis pada bukti sintetiknya.

### Kalau $P$ jatuh tepat di $F$

Perlu diperiksa, sebab bukti sintetik tadi memakai segitiga $OMT$ yang merosot ketika
$M = T$. Untuk $P = F$, garis $OP$ berimpit dengan $OF$, sehingga $M$ dan $T$ memang
titik yang sama, dan

$$OT = OM = \frac{R^2}{OP} = \frac{R^2}{d} \quad ✓$$

Hasilnya tetap. Bukti koordinat menangani kasus ini tanpa perlakuan khusus — ia cuma
nilai $p = 0$ — dan itu keunggulannya.

### Namanya, dan kenapa berguna

Garis $XY$ disebut **garis kutub** (polar) titik $P$ terhadap $\omega$, dan $T$ adalah
kutub garis $\ell$. Yang baru saja dibuktikan adalah satu hal dari sifat timbal balik:

> $T$ ada pada garis kutub $P$ $\iff$ $P$ ada pada garis kutub $T$.

Ruas kanan pernyataan itu langsung menjelaskan soalnya: garis kutub $T$ adalah $\ell$
sendiri, dan setiap $P$ memang ada pada $\ell$ — jadi setiap garis kutub $P$ memang harus
melalui $T$.

Kegunaannya sebagai pemicu: **begitu sebuah soal memuat titik yang bergerak pada satu
garis beserta tali busur singgungnya, cari kutub garis itu.** Jawaban "melalui satu titik
tetap" hampir selalu titik tersebut.

### Pemeriksaan angka

Ambil $R = 2$ dan $\ell : x = 5$, jadi $d = 5$ dan $T = \left(\tfrac45, 0\right)$.

| $P$ | persamaan $XY$: $5x + py = 4$ | apakah $\left(\tfrac45,0\right)$ memenuhi? |
|---|---|---|
| $(5, 0)$ | $5x = 4$ | $5 \cdot \tfrac45 = 4$ ✓ |
| $(5, 4)$ | $5x + 4y = 4$ | $4 + 0 = 4$ ✓ |
| $(5, -20)$ | $5x - 20y = 4$ | $4 - 0 = 4$ ✓ |

Dan $OT = \tfrac45 < 2 = R$ ✓, jadi $T$ di dalam lingkaran seperti dituntut bagian (b).

## Rubrik

- **(a)** Menerjemahkan syarat singgung menjadi $OX \perp XP$, lalu menjadi persamaan
- **(a)** Menurunkan $X \cdot P = R^2$ **dengan memakai** $|X|^2 = R^2$
- **(a)** Menyatakan bahwa $X$ dan $Y$ memenuhi satu persamaan linear yang sama, sehingga
  persamaan itu adalah persamaan garis $XY$ — bukan sekadar mengaku garis $XY$ berbentuk
  demikian
- **(a)** Menuntut persamaan itu berlaku untuk **semua** $p$, lalu menyimpulkan kedua
  syarat $y = 0$ dan $dx = R^2$
- **(a)** Menyatakan letak titik tetapnya dalam bahasa geometri: pada tegak lurus dari
  $O$ ke $\ell$, sejauh $R^2/d$
- **(b)** Membandingkan $R^2/d$ dengan $R$ memakai $d > R$

Bukti sintetik dinilai penuh, asalkan memuat kuasa titik $OM \cdot OP = R^2$ beserta
alasannya, kesebangunan yang dipakai, **dan** penanganan kasus $P = F$ yang membuat
segitiga bantunya merosot. Bukti yang hanya memeriksa dua atau tiga letak $P$ lalu
menyimpulkan "selalu lewat satu titik" tidak memperoleh angka untuk bagian (a).
