---
id: tis-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa]
bentuk: uraian
kesulitan: 3
---

## Soal

Pada segitiga $ABC$, titik $I$ adalah pusat lingkaran dalam dan $H$ titik tinggi.

**(a)** Buktikan bahwa $\angle BIC = 90^\circ + \tfrac12 \angle A$.

**(b)** Untuk segitiga **lancip**, buktikan bahwa $\angle BHC = 180^\circ - \angle A$.

## Petunjuk

- Untuk (a), pandang $\triangle IBC$ saja. Berapa besar sudutnya di $B$ dan di $C$?
- Untuk (b), cari segiempat yang memuat $H$ dan titik sudut $A$, dengan dua sudut siku-siku dari kaki-kaki garis tingginya.
- Pada kedua bagian, langkah terakhirnya sama: ganti $\angle B + \angle C$ dengan $180^\circ - \angle A$.

## Pembahasan

### Bagian (a)

**Pakai sifat yang mendefinisikan $I$.** Titik $I$ adalah perpotongan ketiga garis bagi. Jadi
$BI$ membagi $\angle B$ menjadi dua sama besar, dan $CI$ membagi $\angle C$:

$$\angle IBC = \tfrac12 \angle B, \qquad \angle ICB = \tfrac12 \angle C$$

**Jumlahkan sudut $\triangle IBC$.**

$$\angle BIC = 180^\circ - \angle IBC - \angle ICB = 180^\circ - \tfrac12\left(\angle B + \angle C\right)$$

**Ganti dengan $\angle A$.** Karena $\angle A + \angle B + \angle C = 180^\circ$:

$$\angle B + \angle C = 180^\circ - \angle A$$

$$\angle BIC = 180^\circ - \tfrac12\left(180^\circ - \angle A\right)
= 180^\circ - 90^\circ + \tfrac12 \angle A = 90^\circ + \tfrac12 \angle A \qquad \blacksquare$$

### Bagian (b)

**Namai kakinya.** Misalkan garis tinggi dari $B$ memotong $CA$ di $E$, dan garis tinggi dari
$C$ memotong $AB$ di $F$. Keduanya melalui $H$.

**Pakai segiempat $AEHF$.** Karena segitiganya lancip, $E$ berada di dalam ruas $CA$, $F$ di
dalam ruas $AB$, dan $H$ di dalam segitiga — sehingga $A$, $E$, $H$, $F$ benar-benar membentuk
segiempat.

Dua sudutnya siku-siku:

$$\angle AEH = 90^\circ \ \left(BE \perp CA\right), \qquad
\angle AFH = 90^\circ \ \left(CF \perp AB\right)$$

**Jumlahkan sudut segiempatnya**, yang selalu $360^\circ$:

$$\angle A + 90^\circ + \angle EHF + 90^\circ = 360^\circ
\quad \Longrightarrow \quad \angle EHF = 180^\circ - \angle A$$

**Pindahkan ke sudut yang diminta.** Karena $B$, $H$, $E$ segaris dan $C$, $H$, $F$ segaris,
sudut $\angle BHC$ bertolak belakang dengan $\angle EHF$, sehingga keduanya sama besar:

$$\angle BHC = 180^\circ - \angle A \qquad \blacksquare$$

### Kenapa (b) memerlukan "lancip" dan (a) tidak

Bagian (a) tidak pernah menyentuh letak $I$: ia hanya memakai bahwa $BI$ dan $CI$ garis bagi,
dan itu berlaku pada segitiga apa pun. Pusat lingkaran dalam **selalu** di dalam segitiga,
jadi $\triangle IBC$ selalu terbentuk.

Bagian (b) berbeda. Turunan di atas memakai segiempat $AEHF$, dan segiempat itu hanya
terbentuk kalau kedua kakinya di dalam sisinya dan $H$ di dalam segitiga — yaitu kalau
segitiganya lancip. Untuk segitiga tumpul, $H$ keluar dan turunannya gugur.

Kesimpulannya sendiri masih bisa bertahan atau berubah, bergantung sudut mana yang tumpul,
dan itu harus diperiksa terpisah — bukan diandaikan.

### Cara kedua untuk (b), lewat segiempat talibusur

Karena $\angle AEH = \angle AFH = 90^\circ$, titik $E$ dan $F$ sama-sama memandang ruas $AH$
dengan sudut siku-siku. Maka $A$, $E$, $H$, $F$ terletak pada satu lingkaran — yang
berdiameter $AH$.

Pada segiempat talibusur, dua sudut yang berhadapan berjumlah $180^\circ$. Sudut $\angle A$
dan $\angle EHF$ berhadapan, sehingga

$$\angle EHF = 180^\circ - \angle A$$

langsung, tanpa menjumlahkan keempat sudutnya.

Kedua jalan sama panjang, tetapi jalan ini menyisakan sesuatu: lingkaran berdiameter $AH$
sering diperlukan lagi di langkah berikutnya pada soal yang lebih panjang, dan
menemukannya sekarang berarti tidak perlu mencarinya nanti.

### Pola "huruf yang hilang"

Kedua hasil punya bentuk yang sama: sudut yang dipandang dari titik istimewa terhadap sisi
$BC$ hanya bergantung pada $\angle A$ — sudut yang **tidak muncul** di lambang $\angle BIC$
maupun $\angle BHC$.

Hal yang sama berlaku untuk pusat lingkaran luar, $\angle BOC = 2\angle A$ pada segitiga
dengan $\angle A$ lancip. Ketiganya bisa diingat sebagai satu baris:

$$\angle BOC = 2A, \qquad \angle BIC = 90^\circ + \tfrac{A}{2}, \qquad \angle BHC = 180^\circ - A$$

Periksa pada segitiga sama sisi, $A = 60^\circ$: ketiganya memberi $120^\circ$ ✓ — memang
harus, sebab di sana $O$, $I$, dan $H$ menyatu jadi satu titik.

## Rubrik

- **(a)** Menyatakan $\angle IBC = \tfrac12 \angle B$ dan $\angle ICB = \tfrac12 \angle C$
  dengan alasan $I$ perpotongan garis bagi
- **(a)** Menjumlahkan sudut $\triangle IBC$ dan mengganti $\angle B + \angle C$ dengan
  $180^\circ - \angle A$
- **(a)** Menyederhanakan sampai bentuk yang diminta
- **(b)** Menamai kedua kaki garis tinggi dan menyebut bahwa $A$, $E$, $H$, $F$ membentuk
  segiempat karena segitiganya lancip
- **(b)** Menyatakan kedua sudut siku-sikunya beserta alasannya
- **(b)** Memakai jumlah sudut segiempat untuk memperoleh $\angle EHF = 180^\circ - \angle A$
- **(b)** Menyebut kesegarisan $B$, $H$, $E$ dan $C$, $H$, $F$ sebagai alasan
  $\angle BHC = \angle EHF$

Bukti (b) yang tidak menyebut mengapa $AEHF$ benar-benar segiempat dinilai tidak lengkap:
di situlah keterangan "lancip" dipakai, dan tanpa itu langkah jumlah sudutnya menggantung.
