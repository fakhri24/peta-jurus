---
id: ptolemy
nama: Teorema Ptolemy
pilar: geometri
tahap: osn-p
prasyarat: [segiempat-talibusur, trigonometri-segitiga]
contoh: [ptl-contoh-1]
latihan: [ptl-01, ptl-02, ptl-03, ptl-04, ptl-05, ptl-06]
---

## Kapan dipakai

Gambar memuat **segiempat talibusur**, dan soal berbicara tentang **hasil kali panjang**
atau tentang **diagonalnya**. Begitu keempat titik terletak pada satu lingkaran dan yang
ditanyakan menyangkut diagonal, Ptolemy calon pertama.

Pemicu kedua yang sering luput: gambar hanya memuat **segitiga sama sisi dengan satu titik
di lingkaran luarnya**. Ptolemy pada segiempat yang terbentuk langsung memberi hubungan
$PA = PB + PC$ — hasil yang terlihat ajaib kalau dikerjakan dengan cara lain.

Pemicu ketiga: soal meminta membuktikan **ketaksamaan** yang memuat hasil kali panjang
pada empat titik sembarang. Itu bentuk ketaksamaan Ptolemy, dan kesamaannya tercapai tepat
saat keempatnya setalibusur.

## Intinya

**Teorema Ptolemy.** Untuk segiempat talibusur $ABCD$ dengan diagonal $AC$ dan $BD$:

$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

Dibaca dengan kata: hasil kali diagonal sama dengan jumlah hasil kali kedua pasang sisi
berhadapan.

**Ketaksamaan Ptolemy.** Untuk **empat titik sembarang** pada bidang:

$$AC \cdot BD \le AB \cdot CD + BC \cdot AD$$

dan kesamaannya berlaku tepat ketika $ABCD$ segiempat talibusur dengan urutan titik yang
benar. Bentuk ini yang membuat Ptolemy berguna di soal ketaksamaan, bukan hanya di soal
panjang.

**Ptolemy kedua**, untuk perbandingan diagonalnya:

$$\frac{AC}{BD} = \frac{AB \cdot AD + CB \cdot CD}{BA \cdot BC + DA \cdot DC}$$

Dipakai jauh lebih jarang, tetapi menyelesaikan soal yang menanyakan perbandingan diagonal
tanpa memberi panjang diagonalnya.

**Kegunaan tak terduga.** Ptolemy pada segiempat talibusur di dalam lingkaran satuan
menurunkan rumus $\sin(x+y)$ — itu asal-usul teorema ini pada tabel busur Ptolemaios.

## Jebakan umum

- **Urutan titik tidak berkeliling.** $ABCD$ harus terurut mengelilingi lingkaran. Kalau
  urutannya diacak, yang disebut "diagonal" bukan diagonal lagi dan kesamaannya gagal.
- **Memakai kesamaan pada segiempat yang belum terbukti talibusur.** Untuk yang bukan
  talibusur hanya berlaku ketaksamaannya, dengan tanda kurang dari.
- **Menukar pasangan sisi berhadapan.** Yang dikalikan $AB$ dengan $CD$, dan $BC$ dengan
  $AD$ — bukan $AB$ dengan $BC$.
- **Mengira Ptolemy hanya untuk mencari panjang.** Kegunaan terbesarnya di olimpiade
  justru pada soal ketaksamaan dan pada segitiga sama sisi.
