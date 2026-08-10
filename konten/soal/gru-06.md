---
id: gru-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-ruang]
bentuk: uraian
kesulitan: 3
---

## Soal

Diberikan kubus $ABCD.EFGH$.

![Kubus ABCD titik EFGH dengan alas ABCD di bawah dan tutup EFGH di atas, E tepat di atas A. Diagonal ruang dari A ke G digambar tebal, menembus segitiga BDE di titik P yang terletak sepertiga jalan dari A. Segitiga BDE diarsir. Rusuk yang tersembunyi di belakang digambar putus-putus](kubus-diagonal-ruang.svg)

Buktikan bahwa diagonal ruang $AG$ tegak lurus bidang $BDE$.

## Petunjuk

- Untuk membuktikan sebuah garis tegak lurus sebuah **bidang**, tidak cukup menunjukkan ia tegak lurus satu garis pada bidang itu. Apa syarat lengkapnya?
- Sebuah garis tegak lurus bidang kalau ia tegak lurus **dua garis berpotongan** pada bidang itu. Pilih $BD$ dan $BE$.
- Beri koordinat pada kubusnya dengan titik asal di $A$ dan ketiga rusuk di $A$ sebagai sumbu — lalu tegak lurus terbaca dari hasil kali skalar yang bernilai nol.

## Pembahasan

**Beri koordinat.** Misalkan rusuknya $a$. Taruh titik asal di $A$, dengan ketiga rusuk yang
bertemu di $A$ sebagai sumbu:

$$A(0,0,0), \quad B(a,0,0), \quad D(0,a,0), \quad E(0,0,a), \quad G(a,a,a)$$

Pilihan ini sah justru karena $AB$, $AD$, $AE$ saling tegak lurus — sifat kubus, bukan
pengandaian.

**Tuliskan ketiga vektornya.**

$$\vec{AG} = (a, a, a), \qquad \vec{BD} = D - B = (-a, a, 0), \qquad \vec{BE} = E - B = (-a, 0, a)$$

**Periksa tegak lurus terhadap dua garis pada bidang $BDE$.**

$$\vec{AG} \cdot \vec{BD} = a(-a) + a(a) + a(0) = -a^2 + a^2 = 0$$

$$\vec{AG} \cdot \vec{BE} = a(-a) + a(0) + a(a) = -a^2 + a^2 = 0$$

Jadi $AG \perp BD$ dan $AG \perp BE$.

**Pakai syarat tegak lurus bidang.** Garis $BD$ dan $BE$ dua-duanya terletak pada bidang $BDE$
dan **berpotongan** di $B$. Sebuah garis yang tegak lurus dua garis berpotongan pada suatu
bidang tegak lurus seluruh bidang itu. Maka

$$AG \perp \text{bidang } BDE \qquad \blacksquare$$

### Syarat "dua garis berpotongan" tidak boleh dilonggarkan

Tegak lurus terhadap **satu** garis pada bidang jelas tidak cukup — banyak garis miring yang
tegak lurus satu garis tertentu tanpa tegak lurus bidangnya.

Yang lebih halus: tegak lurus terhadap dua garis yang **sejajar** juga tidak cukup, sebab
keduanya hanya menentukan satu arah. Karena itu $BD$ dan $BE$ dipilih — keduanya berpotongan di
$B$, sehingga bersama-sama menentukan seluruh bidang.

Menyebut syarat ini secara eksplisit adalah bagian dari buktinya, bukan formalitas.

### Cara sintetik, tanpa koordinat

$BD \perp AC$ (diagonal persegi $ABCD$ saling tegak lurus) dan $BD \perp AE$ (sebab $AE$ tegak
lurus seluruh bidang alas). Jadi $BD$ tegak lurus dua garis berpotongan pada bidang $ACGE$,
sehingga $BD \perp$ bidang $ACGE$ — dan karena $AG$ terletak pada bidang itu, $BD \perp AG$.

Alasan yang sama dengan huruf yang dipertukarkan memberi $BE \perp AG$, dan buktinya selesai.

Cara ini lebih pendek untuk yang sudah terbiasa, tetapi menuntut kemampuan melihat bidang
$ACGE$ di dalam gambar. Cara koordinat tidak menuntut apa pun selain ketelitian — dan itu
alasan bagus untuk memilihnya di bawah tekanan waktu.

### Apa lagi yang ikut terbaca

Bidang $BDE$ mempunyai persamaan $x + y + z = a$, sedangkan titik pada $AG$ berbentuk
$(t a, t a, t a)$. Keduanya bertemu saat $3ta = a$, yakni

$$t = \tfrac{1}{3}$$

Dengan alasan yang sama, bidang $CFH$ berpersamaan $x + y + z = 2a$ dan memotong $AG$ di
$t = \tfrac{2}{3}$. Jadi **kedua bidang itu membagi diagonal ruang menjadi tiga bagian sama
panjang** — kenyataan yang tidak terlihat sama sekali dari gambar, dan muncul cuma-cuma dari
persamaan bidangnya.

## Rubrik

- Menyatakan syarat garis tegak lurus bidang: tegak lurus dua garis berpotongan pada bidang itu
- Memberi koordinat pada kubus dengan alasan ketiga rusuk di satu pojok saling tegak lurus, atau menempuh jalan sintetik yang setara
- Menuliskan vektor $\vec{AG}$ beserta dua vektor yang terletak pada bidang $BDE$
- Menunjukkan kedua hasil kali skalarnya nol
- Menyebut bahwa kedua garis yang dipakai berpotongan, lalu menyimpulkan $AG$ tegak lurus bidang $BDE$
