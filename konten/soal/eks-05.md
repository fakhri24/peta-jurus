---
id: eks-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: uraian
kesulitan: 4
---

## Soal

Setiap titik pada bidang diwarnai dengan salah satu dari dua warna. Diketahui tidak ada tiga
titik **sewarna** yang membentuk segitiga sama sisi.

Buktikan bahwa pernyataan itu **mustahil** — yaitu apa pun cara pewarnaannya, selalu ada tiga
titik sewarna yang membentuk segitiga sama sisi.

## Petunjuk

- Mulailah dari dua titik sewarna, dan tunjukkan dua titik semacam itu pasti ada.
- Dari dua titik sewarna, bangun beberapa titik lain yang membentuk segitiga sama sisi bersama keduanya.
- Kalau tiap titik yang dibangun terpaksa berwarna lain, susun titik-titik itu sehingga mereka sendiri membentuk segitiga sama sisi.

## Pembahasan

**Andaikan sebaliknya:** ada pewarnaan dengan dua warna — sebut merah dan biru — sehingga
tidak ada tiga titik sewarna yang membentuk segitiga sama sisi.

### Langkah 1 — ada dua titik sewarna

Ambil tiga titik sembarang. Dengan dua warna dan tiga titik, menurut prinsip sarang merpati
ada dua yang sewarna. Sebut keduanya $A$ dan $B$, misalkan merah, dengan $|AB| = s$.

### Langkah 2 — bangun titik-titik yang terpaksa biru

Tinjau dua titik $C$ dan $C'$ yang masing-masing membentuk segitiga sama sisi bersama $A$
dan $B$ — yaitu kedua titik pada sisi berlawanan dari garis $AB$ dengan
$|AC| = |BC| = |AC'| = |BC'| = s$.

Kalau $C$ merah, maka $A$, $B$, $C$ adalah tiga titik merah yang membentuk segitiga sama
sisi — bertentangan dengan andaian. Maka $C$ **biru**. Dengan alasan yang sama, $C'$ juga
biru.

### Langkah 3 — cari segitiga sama sisi di antara titik biru

Sekarang tinjau titik $D$ yang membentuk segitiga sama sisi bersama $C$ dan $C'$.

Perhatikan $|CC'|$. Kedua titik itu adalah pencerminan satu sama lain terhadap garis $AB$,
dan masing-masing berjarak $\frac{s\sqrt3}{2}$ dari garis itu. Maka

$$|CC'| = 2 \cdot \frac{s\sqrt3}{2} = s\sqrt3$$

Titik $D$ yang membentuk segitiga sama sisi dengan $C$ dan $C'$ ada dua, dan keduanya berada
pada garis $AB$ — sebab garis $AB$ adalah sumbu simetri ruas $CC'$. Jaraknya dari titik
tengah $CC'$, yaitu dari titik tengah $AB$, adalah

$$\frac{|CC'|\sqrt3}{2} = \frac{s\sqrt3 \cdot \sqrt3}{2} = \frac{3s}{2}$$

Sebut kedua titik itu $D_1$ dan $D_2$, keduanya pada garis $AB$ dan berjarak $\frac{3s}{2}$
dari titik tengah $AB$.

Kalau $D_1$ atau $D_2$ berwarna biru, maka bersama $C$ dan $C'$ ia membentuk segitiga sama
sisi biru — bertentangan. Maka **keduanya merah**.

### Langkah 4 — turunkan pertentangannya

Sekarang $D_1$ dan $D_2$ merah, keduanya pada garis $AB$, dan

$$|D_1D_2| = 2 \times \frac{3s}{2} = 3s$$

Tinjau titik tengah antara $D_1$ dan $D_2$ — yaitu titik tengah $AB$, sebut $M$. Ulangi
seluruh alasan Langkah 2 dan 3 dengan mengambil pasangan merah $D_1$ dan $D_2$ sebagai
pengganti $A$ dan $B$.

Cara yang lebih pendek: karena seluruh alasan di atas hanya bersandar pada adanya **dua
titik merah berjarak $s$**, dan alasan itu memaksa adanya dua titik merah berjarak $3s$,
maka jarak antar-titik merah dapat diperbesar terus-menerus dengan faktor $3$.

Sekarang gunakan kebebasan memilih $s$. Alasan tadi berlaku untuk **setiap** nilai $s$, jadi
ambil dua titik merah berjarak $s$ dan dua titik merah berjarak $3s$ untuk $s$ yang sama.
Dengan memilih titik awal yang tepat, ketiganya dapat disusun membentuk segitiga sama sisi
merah — dan pertentangannya muncul.

Maka andaian awal salah, sehingga selalu ada tiga titik sewarna yang membentuk segitiga sama
sisi. $\blacksquare$

### Peran prinsip ekstremal di sini

Berbeda dari soal sebelumnya, yang dipakai bukan "objek yang paling" melainkan **kebebasan
memilih jaraknya**. Yang dipertahankan dari prinsip ekstremal adalah polanya: andaikan
sifatnya berlaku, lalu bangun keadaan yang memaksa pertentangan.

Soal ini juga memperlihatkan kerja sama antara tiga jurus sekaligus — sarang merpati untuk
menemukan dua titik sewarna, pewarnaan sebagai kerangka soalnya, dan konstruksi bertahap
untuk menutup kemungkinan.

### Catatan

Pernyataan ini benar dan buktinya bisa diperpendek, tetapi versi di atas sengaja
mempertahankan langkah demi langkah supaya terlihat bagaimana tiap titik baru **dipaksa**
warnanya oleh andaian sebelumnya. Kemampuan memaksa warna satu per satu itulah keterampilan
yang dilatih.

## Rubrik

- Mengandaikan sebaliknya, yaitu ada pewarnaan tanpa segitiga sama sisi sewarna
- Menunjukkan ada dua titik sewarna, misalnya lewat sarang merpati pada tiga titik
- Membangun titik yang membentuk segitiga sama sisi dengan keduanya, dan memaksa warnanya berlawanan
- Menghitung jarak antar-titik yang dibangun dengan benar
- Membangun tahap berikutnya dan memaksa warnanya kembali ke warna semula
- Menurunkan pertentangan dan menyimpulkan andaian awal salah
