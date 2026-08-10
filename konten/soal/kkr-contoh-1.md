---
id: kkr-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kekongruenan]
bentuk: uraian
kesulitan: 2
---

## Soal

Pada segiempat $ABCD$, sisi $AB$ sejajar sisi $DC$ dan $AB = DC$.

![Segiempat ABCD dengan sisi AB mendatar di bawah dan sisi DC mendatar di atas, keduanya ditandai sama panjang dan sejajar. Diagonal AC digambar sehingga segiempat itu terbagi menjadi segitiga ABC dan segitiga CDA](segiempat-sisi-sejajar.svg)

Buktikan bahwa $AD = BC$.

## Petunjuk

- Ruas $AD$ dan $BC$ berada di dua sisi gambar yang berjauhan dan tidak berada pada satu segitiga. Apa yang bisa kamu tambahkan ke gambar supaya keduanya masuk ke dalam segitiga?
- Tarik diagonal $AC$. Sekarang $AD$ ada di dalam $\triangle CDA$ dan $BC$ ada di dalam $\triangle ABC$ — buktikan kedua segitiga itu kongruen.
- Kamu punya sepasang sisi sama panjang dari soal, satu sisi yang dipakai bersama, dan satu pasang sudut dari kesejajaran. Periksa apakah sudut itu diapit kedua sisi tersebut.

## Pembahasan

**Kenali bentuk soalnya.** Yang diminta adalah dua ruas **sama panjang**, dan kedua ruas itu
tidak berada pada satu segitiga. Itu pemicu paling khas jurus ini: cari dua segitiga yang
masing-masing memuat salah satunya, lalu buktikan keduanya kongruen.

Tetapi pada gambar semula belum ada segitiga sama sekali — yang ada cuma segiempat. Jadi
langkah pertamanya **membuat** segitiganya.

**Tarik diagonal $AC$.** Diagonal itu memotong segiempat menjadi $\triangle ABC$ dan
$\triangle CDA$. Ruas $BC$ ada di segitiga pertama, ruas $DA$ ada di segitiga kedua. Sekarang
soalnya berubah menjadi: buktikan kedua segitiga itu kongruen.

**Kumpulkan bahannya, satu per satu.**

1. **$AB = CD$** — diberikan soal.
2. **$AC = CA$** — sisi yang dipakai bersama kedua segitiga. Ini pasangan sisi sama panjang
   yang sah, dan justru unsur inilah yang paling sering terlewat.
3. **$\angle BAC = \angle DCA$** — karena $AB \parallel DC$ dipotong garis $AC$, keduanya
   sudut dalam berseberangan.

**Periksa susunannya sebelum menyebut namanya.** Pada $\triangle BAC$, sudut $\angle BAC$
terletak di antara sisi $AB$ dan sisi $AC$. Pada $\triangle DCA$, sudut $\angle DCA$ terletak
di antara sisi $CD$ dan sisi $CA$. Jadi sudut yang diketahui memang **diapit** kedua sisi yang
diketahui — susunannya S-Sd-S, dan itu syarat kekongruenan yang sah.

$$\triangle BAC \cong \triangle DCA \quad (\text{S-Sd-S})$$

**Baca akibatnya dengan urutan yang benar.** Penulisan $\triangle BAC \cong \triangle DCA$
memasangkan $B \leftrightarrow D$, $A \leftrightarrow C$, $C \leftrightarrow A$. Maka sisi
$BC$ bersesuaian dengan sisi $DA$:

$$BC = DA$$

Jadi $AD = BC$. $\blacksquare$

### Mengapa urutan huruf itu penting

Kalau kesimpulannya ditulis $\triangle ABC \cong \triangle CDA$, pasangannya menjadi
$A \leftrightarrow C$, $B \leftrightarrow D$, $C \leftrightarrow A$ — dan itu **juga** benar
di sini. Tetapi menulis $\triangle ABC \cong \triangle ACD$ salah, meski kedua segitiga itu
memang kongruen, sebab urutan hurufnya mengklaim $AB = AC$, yang tidak diketahui benar.

Kebiasaan yang menyelamatkan: tulis pasangan titiknya lebih dulu di kertas coret, baru susun
pernyataan kongruennya mengikuti pasangan itu.

### Yang tidak boleh dipakai

Godaan terbesar pada soal ini adalah menjawab, "$AB \parallel DC$ dan $AB = DC$, jadi $ABCD$
jajaran genjang, jadi sisi berhadapannya sama panjang." Kalimat itu **melompati** bagian yang
justru diminta: bahwa sepasang sisi sejajar dan sama panjang mengakibatkan bangunnya jajaran
genjang adalah pernyataan yang perlu dibuktikan, dan buktinya persis apa yang baru saja kita
kerjakan.

Menggunakan sesuatu yang setara dengan yang hendak dibuktikan namanya berputar, dan itu
kekeliruan yang paling mahal dalam soal pembuktian — hasilnya benar, tetapi tidak ada yang
terbukti.

### Apa lagi yang ikut terbukti secara gratis

Setelah dua segitiga dinyatakan kongruen, **semua** unsur bersesuaiannya ikut sama, bukan
hanya yang tadi dicari. Di sini ikut terbukti

$$\angle BCA = \angle DAC$$

dan itu sudut dalam berseberangan pada garis $AD$ dan $BC$ yang dipotong $AC$ — yang berarti
$AD \parallel BC$. Jadi $ABCD$ memang jajaran genjang, dan sekarang kenyataan itu sudah
**dibuktikan**, bukan diandaikan.

Kebiasaan memeriksa unsur yang belum terpakai adalah salah satu sumber langkah lanjutan
tergampang di soal geometri.

## Rubrik

- Menarik diagonal $AC$ (atau $BD$) sebagai garis bantu, dan menyebut alasan menariknya
- Menyebut $AB = CD$ dari soal
- Menyebut $AC$ sisi yang dipakai bersama kedua segitiga
- Menurunkan $\angle BAC = \angle DCA$ dari $AB \parallel DC$ dengan menyebut sudut dalam berseberangan
- Memeriksa bahwa sudut itu diapit kedua sisi, lalu menyebut S-Sd-S
- Menuliskan kekongruenannya dengan pasangan titik yang berurutan benar
- Menyimpulkan $AD = BC$ sebagai sisi bersesuaian, bukan sebagai sifat jajaran genjang yang diandaikan
