---
id: cvm-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus, garis-istimewa]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan dengan teorema Ceva bahwa ketiga garis bagi sudut sebuah segitiga berpotongan di
satu titik.

## Petunjuk

- Yang dibuktikan **konkuren**, jadi yang dipakai adalah kebalikan teorema Ceva — sebut itu eksplisit sejak awal.
- Tiap garis bagi memotong sisi seberangnya menurut perbandingan tertentu. Perbandingan apa?
- Setelah ketiga perbandingannya ditulis, kalikan dan lihat apa yang saling meniadakan.

## Pembahasan

**Nyatakan arah yang dipakai.** Yang akan dibuktikan adalah konkuren, jadi yang dipakai
adalah **kebalikan teorema Ceva**:

> Jika $D$ pada $BC$, $E$ pada $CA$, $F$ pada $AB$ memenuhi
> $\dfrac{BD}{DC} \cdot \dfrac{CE}{EA} \cdot \dfrac{AF}{FB} = 1$, maka $AD$, $BE$, $CF$
> berpotongan di satu titik.

Menyebut ini di awal bukan formalitas: teorema Ceva sendiri berbunyi ke arah yang berlawanan,
dan memakainya untuk membuktikan konkuren adalah kekeliruan logika yang lengkap tanpa
terlihat.

**Namai titik potongnya.** Misalkan garis bagi dari $A$ memotong $BC$ di $D$, dari $B$
memotong $CA$ di $E$, dan dari $C$ memotong $AB$ di $F$. Tulis $a = BC$, $b = CA$, $c = AB$.

**Pakai teorema garis bagi pada masing-masing.** Garis bagi membagi sisi seberangnya menurut
perbandingan kedua sisi yang mengapit sudutnya:

$$\frac{BD}{DC} = \frac{AB}{AC} = \frac{c}{b}$$

$$\frac{CE}{EA} = \frac{BC}{BA} = \frac{a}{c}$$

$$\frac{AF}{FB} = \frac{CA}{CB} = \frac{b}{a}$$

Perhatikan bahwa ketiganya disusun dengan pola yang sama — dari titik sudut pertama sisi itu,
lewat titik baginya, ke titik sudut kedua — sehingga sisi pengapitnya juga terbaca berurut.

**Kalikan ketiganya.**

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}
= \frac{c}{b} \cdot \frac{a}{c} \cdot \frac{b}{a} = 1$$

Tiap huruf muncul tepat sekali di pembilang dan sekali di penyebut, jadi semuanya saling
meniadakan.

**Simpulkan.** Menurut kebalikan teorema Ceva, ketiga garis bagi $AD$, $BE$, $CF$ berpotongan
di satu titik $\blacksquare$

### Satu langkah yang tidak boleh dilewati

Kebalikan Ceva menuntut ketiga titiknya berada **di dalam** sisinya (atau, dalam versi
bertanda, dengan tanda yang konsisten). Untuk garis bagi **dalam**, syarat itu selalu
terpenuhi: garis bagi dalam dari $A$ berada di antara sinar $AB$ dan $AC$, sehingga ia
memotong ruas $BC$ di titik antara $B$ dan $C$.

Menyebutkannya satu kalimat sudah cukup, dan tanpa itu buktinya menggantung.

### Titik potongnya punya nama

Titik yang baru saja dibuktikan ada adalah **pusat lingkaran dalam**, ditulis $I$. Ia berjarak
sama ke ketiga sisi, dan itu bisa dilihat dari sifat garis baginya: setiap titik pada garis
bagi sudut $A$ berjarak sama ke sisi $AB$ dan $AC$.

Perhatikan bahwa Ceva membuktikan **keberadaan** titik potongnya, sedangkan sifat berjarak
sama datang dari sumber lain. Keduanya sering dicampur; yang satu tentang konkuren, yang lain
tentang jarak.

### Cara yang sama untuk garis berat dan garis tinggi

Pola buktinya berulang dan patut dihafal sebagai pola, bukan sebagai tiga bukti terpisah.

**Garis berat.** Ketiga perbandingannya $1$, karena tiap garis berat menuju titik tengah:

$$1 \cdot 1 \cdot 1 = 1$$

sehingga ketiganya konkuren — di titik berat.

**Garis tinggi.** Di sini bentuk trigonometri Ceva lebih murah:

$$\frac{\sin \angle BAD}{\sin \angle DAC} \cdot \frac{\sin \angle CBE}{\sin \angle EBA}
\cdot \frac{\sin \angle ACF}{\sin \angle FCB} = 1$$

Untuk garis tinggi, $\angle BAD = 90^\circ - \angle B$ dan $\angle DAC = 90^\circ - \angle C$,
dan seterusnya berputar. Hasil kalinya

$$\frac{\cos B}{\cos C} \cdot \frac{\cos C}{\cos A} \cdot \frac{\cos A}{\cos B} = 1$$

Tiap kosinus muncul sekali di atas dan sekali di bawah — struktur yang sama persis dengan
bukti garis bagi di atas. Titik potongnya titik tinggi.

## Rubrik

- Menyatakan bahwa yang dipakai adalah **kebalikan** teorema Ceva, bukan teorema Ceva
- Menamai ketiga titik potong garis bagi dengan sisi seberangnya
- Menuliskan ketiga perbandingan lewat teorema garis bagi, dengan urutan huruf yang benar
- Mengalikan ketiganya dan menunjukkan hasilnya $1$
- Menyebut bahwa ketiga titiknya berada di dalam sisinya, sebagai syarat sahnya memakai
  kebalikan Ceva
- Menuliskan kesimpulan bahwa ketiga garis bagi konkuren

Bukti yang langsung menulis "menurut Ceva ketiganya konkuren" tanpa menyebut arah
kebalikannya dinilai tidak lengkap: yang ditulis adalah kebalikan dari yang dipakai.
