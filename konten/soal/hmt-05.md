---
id: hmt-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti, garis-singgung]
bentuk: uraian
kesulitan: 4
---

## Soal

Dua lingkaran $\omega_1$ dan $\omega_2$ bersinggungan di titik $T$. Sebuah garis melalui $T$
memotong $\omega_1$ lagi di $P$ dan $\omega_2$ lagi di $Q$.

**(a)** Buktikan bahwa garis singgung $\omega_1$ di $P$ sejajar garis singgung $\omega_2$ di
$Q$.

**(b)** Buktikan bahwa untuk **dua** garis lewat $T$, yang memotong $\omega_1$ di $P_1, P_2$
dan $\omega_2$ di $Q_1, Q_2$, berlaku $P_1P_2 \parallel Q_1Q_2$.

## Petunjuk

- Titik singgung dua lingkaran adalah pusat homoteti yang memetakan satu ke lainnya. Apa yang dipetakannya menjadi apa?
- Homoteti memetakan $\omega_1$ ke $\omega_2$ dan memetakan tiap garis lewat $T$ ke dirinya sendiri, jadi ia memetakan $P$ ke $Q$.
- Sifat pokok homoteti: setiap garis dipetakan ke garis yang **sejajar** dengannya. Cukup tunjukkan bahwa garis yang satu adalah peta garis yang lain.

## Pembahasan

### Modal untuk kedua bagian

Karena $\omega_1$ dan $\omega_2$ bersinggungan di $T$, titik $T$ adalah pusat homoteti yang
memetakan $\omega_1$ ke $\omega_2$. Sebut homoteti itu $h$, dengan faktor

$$k = \pm\frac{r_2}{r_1}$$

bertanda positif kalau keduanya bersinggungan dari dalam, negatif kalau dari luar.

**Alasan $T$ pusatnya.** Homoteti berpusat $T$ dengan faktor $k$ memetakan pusat $O_1$ ke
titik pada sinar $TO_1$ berjarak $|k| \cdot TO_1 = r_2$ dari $T$ — dan karena kedua lingkaran
bersinggungan, $T$, $O_1$, $O_2$ segaris dengan $TO_1 = r_1$ dan $TO_2 = r_2$. Jadi $O_1$
terpetakan ke $O_2$, dan jari-jari $r_1$ terpetakan ke $r_2$. Lingkaran ke lingkaran.

**$h$ memetakan $P$ ke $Q$.** Homoteti memetakan setiap garis lewat pusatnya ke dirinya
sendiri, jadi garis $TPQ$ terpetakan ke dirinya. Titik $P$ pada $\omega_1$, jadi $h(P)$ pada
$\omega_2$; dan $h(P)$ pada garis $TPQ$. Titik pada $\omega_2$ yang juga pada garis itu ada
dua: $T$ dan $Q$. Karena $h(P) = T$ hanya kalau $P = T$, maka

$$h(P) = Q$$

### Bagian (a)

Sebut $t_1$ garis singgung $\omega_1$ di $P$.

Homoteti memetakan lingkaran ke lingkaran dan memetakan garis ke garis **sejajar**. Karena
$t_1$ menyentuh $\omega_1$ tepat di satu titik, yaitu $P$, bayangannya $h(t_1)$ menyentuh
$h(\omega_1) = \omega_2$ tepat di satu titik, yaitu $h(P) = Q$.

Jadi $h(t_1)$ adalah garis singgung $\omega_2$ di $Q$, sebut $t_2$. Karena homoteti menjaga
kesejajaran,

$$t_1 \parallel t_2 \qquad \blacksquare$$

### Bagian (b)

Terapkan hasil di atas pada masing-masing garis: $h(P_1) = Q_1$ dan $h(P_2) = Q_2$.

Homoteti memetakan ruas ke ruas: bayangan garis $P_1P_2$ adalah garis $Q_1Q_2$. Karena
homoteti memetakan tiap garis ke garis yang sejajar dengannya,

$$P_1P_2 \parallel Q_1Q_2 \qquad \blacksquare$$

Sekalian diperoleh perbandingan panjangnya cuma-cuma:

$$\frac{Q_1Q_2}{P_1P_2} = |k| = \frac{r_2}{r_1}$$

### Bukti (a) tanpa homoteti, untuk perbandingan

Andaikan kedua lingkaran bersinggungan dari dalam. Jari-jari $O_1P$ dan $O_2Q$ dibandingkan
lewat dua segitiga sama kaki:

- $\triangle TO_1P$ sama kaki, sebab $O_1T = O_1P = r_1$, jadi
  $\angle O_1TP = \angle O_1PT$;
- $\triangle TO_2Q$ sama kaki, sebab $O_2T = O_2Q = r_2$, jadi
  $\angle O_2TQ = \angle O_2QT$.

Sudut $\angle O_1TP$ dan $\angle O_2TQ$ adalah sudut yang sama, sebab $T$, $O_1$, $O_2$
segaris dan $T$, $P$, $Q$ segaris. Maka $\angle O_1PT = \angle O_2QT$, sehingga
$O_1P \parallel O_2Q$.

Garis singgung tegak lurus jari-jari di titik singgungnya, jadi $t_1 \perp O_1P$ dan
$t_2 \perp O_2Q$. Dua garis yang tegak lurus pada dua garis sejajar juga sejajar, maka
$t_1 \parallel t_2$ ✓

Bukti ini sah dan lebih dasar, tetapi perhatikan ongkosnya: ia perlu diulang untuk kasus
bersinggungan dari luar, dan ia tidak memberi bagian (b) dengan cuma-cuma. Bukti homoteti
menangani keduanya sekaligus karena tanda $k$ sudah menampung perbedaan kasusnya.

### Kenapa ini pemicu yang layak dihafal

Kesimpulannya berbunyi: **pada dua lingkaran yang bersinggungan, setiap garis lewat titik
singgungnya menghasilkan pasangan titik yang "bersesuaian", dan bangun apa pun yang dirakit
dari titik-titik itu di lingkaran satu sebangun-sejajar dengan bangun padanannya di
lingkaran lain.**

Karena itu, begitu soal memuat dua lingkaran bersinggungan, langkah pertama yang hampir
selalu berguna adalah menamai titik singgungnya sebagai pusat homoteti — bahkan sebelum
tahu akan dipakai untuk apa.

## Rubrik

- Menyatakan bahwa $T$ adalah pusat homoteti yang memetakan $\omega_1$ ke $\omega_2$,
  **beserta alasannya** lewat kesegarisan $T$, $O_1$, $O_2$ dan besar faktornya $r_2/r_1$
- Menyebut tanda $k$ mengikuti bersinggungan dalam atau luar
- Menunjukkan $h(P) = Q$ dengan alasan garis lewat pusat terpetakan ke dirinya sendiri, dan
  menyingkirkan kemungkinan $h(P) = T$
- **(a)** Menyatakan bahwa bayangan garis singgung adalah garis singgung, dengan alasan
  homoteti menjaga banyaknya titik potong
- **(a)** Memakai sifat homoteti memetakan garis ke garis sejajar untuk menutup buktinya
- **(b)** Menerapkan $h(P_1) = Q_1$ dan $h(P_2) = Q_2$, lalu menyimpulkan kesejajarannya

Bukti (a) lewat dua segitiga sama kaki dinilai penuh, asalkan kesegarisan $T$, $O_1$, $O_2$
disebut sebagai alasan kedua sudut di $T$ sama, dan kasus bersinggungan dari luar ikut
ditangani atau dinyatakan serupa dengan alasan yang jelas.
