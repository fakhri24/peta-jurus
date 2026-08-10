---
id: ceva-menelaus
nama: Ceva dan Menelaus
pilar: geometri
tahap: osn-p
prasyarat: [kesebangunan, luas-bidang]
contoh: [cvm-contoh-1]
latihan: [cvm-01, cvm-02, cvm-03, cvm-04, cvm-05, cvm-06]
---

## Kapan dipakai

Soal meminta membuktikan **tiga garis berpotongan di satu titik** (konkuren), atau **tiga
titik terletak pada satu garis** (segaris). Kedua pertanyaan itu pemicu langsung: yang
pertama Ceva, yang kedua Menelaus.

Pemicu kedua: gambar memuat tiga ruas dari ketiga titik sudut segitiga ke sisi
seberangnya, dan soal memberi **perbandingan** pada sisi-sisinya. Bentuk hasil kali tiga
perbandingan itu sidik jari kedua teorema ini.

Cara cepat membedakan mana yang dipakai: kalau garis pemotongnya **melintasi** segitiga
dari luar, itu Menelaus; kalau ketiga ruasnya berangkat dari titik sudut, itu Ceva.

## Intinya

**Teorema Ceva.** Kalau $AD$, $BE$, $CF$ dengan $D$ pada $BC$, $E$ pada $CA$, $F$ pada
$AB$ berpotongan di satu titik, maka

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

**Kebalikannya juga berlaku**, dan justru itu yang dipakai untuk membuktikan konkuren.

**Teorema Menelaus.** Kalau $D$, $E$, $F$ segaris (dengan garis itu memotong ketiga sisi
atau perpanjangannya), maka

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = -1$$

Hasil kalinya **sama persis**, hanya tandanya berbeda — dan itulah satu-satunya yang
membedakan keduanya kalau panjangnya dihitung bertanda. Kalau dipakai tanpa tanda,
keduanya sama-sama bernilai $1$, dan yang membedakan tinggal gambarnya.

**Bentuk trigonometri Ceva**, dipakai kalau yang diketahui sudut, bukan panjang:

$$\frac{\sin \angle BAD}{\sin \angle DAC} \cdot \frac{\sin \angle CBE}{\sin \angle EBA}
\cdot \frac{\sin \angle ACF}{\sin \angle FCB} = 1$$

Bentuk ini yang membuktikan garis bagi dan garis tinggi konkuren tanpa perhitungan panjang
sama sekali.

**Kaitan dengan luas.** Ceva bisa diturunkan seluruhnya dari perbandingan luas: tiap
perbandingan pada sisi sama dengan perbandingan luas dua segitiga bertinggi sama. Kalau
lupa rumusnya, jalan itu selalu bisa ditempuh ulang.

## Jebakan umum

- **Menyusun perbandingan tidak berputar.** Urutannya harus mengelilingi segitiga:
  $B \to D \to C$, lalu $C \to E \to A$, lalu $A \to F \to B$. Satu suku dibalik, hasilnya
  jadi kebalikannya.
- **Memakai Ceva padahal titiknya di perpanjangan sisi.** Masih berlaku, tetapi hanya
  dengan panjang bertanda — dan tandanya harus konsisten untuk ketiga sukunya.
- **Menukar Ceva dengan Menelaus.** Keduanya berbentuk sama; yang membedakan konkuren
  lawan segaris. Salah pilih menghasilkan bukti yang rapi tetapi membuktikan hal lain.
- **Mengira kebalikan Ceva tidak perlu dibuktikan berlaku.** Untuk soal pembuktian
  konkuren, arah yang dipakai justru kebalikannya, dan itu perlu disebut eksplisit di
  lembar jawaban.
