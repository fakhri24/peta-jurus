---
id: kut-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik, segiempat-talibusur]
bentuk: uraian
kesulitan: 4
---

## Soal

Pada segitiga lancip $ABC$, garis tinggi dari $A$ memotong $BC$ di $D$, dan garis tinggi
dari $B$ memotong $CA$ di $E$. Kedua garis tinggi itu berpotongan di $H$.

![Segitiga ABC lancip dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas. Dari A ditarik garis tinggi ke alas, memotongnya tegak lurus di titik D di antara B dan C. Dari B ditarik garis tinggi ke sisi AC, memotongnya tegak lurus di titik E. Kedua garis tinggi itu berpotongan di titik H di dalam segitiga](segitiga-dua-tinggi-bertemu.svg)

Buktikan bahwa $HA \cdot HD = HB \cdot HE$.

## Petunjuk

- Bentuk yang diminta adalah hasil kali dua panjang sama dengan hasil kali dua panjang lain, dengan satu titik yang dipakai bersama. Kalau ada lingkaran lewat keempat ujungnya, bentuk itu langsung jadi.
- Cari lingkaran yang melalui $A$, $B$, $D$, dan $E$. Petunjuknya dua sudut siku-siku.
- Sudut $\angle ADB$ dan $\angle AEB$ keduanya $90^\circ$, jadi $D$ dan $E$ memandang ruas $AB$ dengan sudut yang sama.

## Pembahasan

**Temukan lingkarannya.** Garis tinggi dari $A$ tegak lurus $BC$, jadi $\angle ADB = 90^\circ$.
Garis tinggi dari $B$ tegak lurus $CA$, jadi $\angle AEB = 90^\circ$.

Titik yang memandang sebuah ruas dengan sudut $90^\circ$ terletak pada lingkaran yang ruas
itu menjadi garis tengahnya — kebalikan dari teorema sudut pada setengah lingkaran. Karena
$D$ dan $E$ sama-sama memandang $AB$ dengan sudut $90^\circ$, keduanya berada pada lingkaran
berdiameter $AB$.

Sebut lingkaran itu $\omega$; ia memuat $A$, $B$, $D$, dan $E$.

**Kenali kedua talibusurnya.** Pada $\omega$:

- $A$, $H$, $D$ segaris karena ketiganya pada garis tinggi dari $A$ — jadi $AD$ talibusur
  $\omega$ yang melalui $H$;
- $B$, $H$, $E$ segaris karena ketiganya pada garis tinggi dari $B$ — jadi $BE$ talibusur
  $\omega$ yang melalui $H$.

**Terapkan kuasa titik.** Karena segitiganya lancip, $H$ berada di dalam segitiga, dan
karena itu di dalam $\omega$. Dua talibusur $AD$ dan $BE$ berpotongan di $H$, maka

$$HA \cdot HD = HB \cdot HE \qquad \blacksquare$$

### Kenapa dua sudut siku-siku itu yang jadi pemicunya

Tanpa lingkaran, pernyataan yang diminta terlihat seperti soal kesebangunan biasa — dan
memang bisa dikerjakan begitu: $\triangle AHE \sim \triangle BHD$ karena keduanya siku-siku
dan punya sudut bertolak belakang di $H$. Dari situ

$$\frac{HA}{HB} = \frac{HE}{HD} \quad \Longrightarrow \quad HA \cdot HD = HB \cdot HE$$

Kedua jalan sah. Yang membuat jalan lingkaran lebih berharga adalah **apa yang ikut
terbawa**: begitu diketahui $A$, $B$, $D$, $E$ setalibusur, seluruh perbendaharaan sudut
keliling ikut tersedia — misalnya $\angle CDE = \angle CAB$, yang biasanya jadi langkah
berikutnya pada soal yang lebih panjang.

Aturan praktisnya: **dua sudut siku-siku yang memandang satu ruas yang sama adalah pengumuman
adanya lingkaran.** Itu salah satu pemicu paling sering muncul di geometri olimpiade.

### Kalau segitiganya tumpul

Andai $\angle C$ tumpul, $H$ jatuh di luar segitiga, dan $D$ maupun $E$ jatuh di perpanjangan
sisinya. Lingkaran berdiameter $AB$ tetap memuat keempat titik itu, karena alasannya cuma
kedua sudut siku-siku — dan sudut siku-sikunya tidak hilang.

Yang berubah: $H$ sekarang di **luar** $\omega$, sehingga yang berlaku bentuk dua garis potong
dari titik luar. Kesimpulannya sama persis, $HA \cdot HD = HB \cdot HE$, karena kedua bentuk
kuasa titik itu berbunyi sama.

Jadi keterangan "lancip" di soal ini bukan syarat kebenarannya, melainkan penyederhana:
tanpa itu, bukti yang lengkap harus menyebut letak $H$ dan memakai bentuk kuasa yang sesuai.

### Titik ketiga yang muncul cuma-cuma

$H$ adalah titik potong dua garis tinggi, jadi ia **titik tinggi** segitiga $ABC$ — dan garis
tinggi dari $C$ pasti melewatinya juga. Dengan $F$ kaki garis tinggi dari $C$, cara yang sama
memberi

$$HC \cdot HF = HA \cdot HD = HB \cdot HE$$

karena semuanya sama dengan nilai mutlak kuasa $H$ terhadap lingkaran yang bersangkutan.
Ketiga hasil kali itu sama — hasil yang lebih kuat daripada yang diminta soal, dan diperoleh
tanpa pekerjaan tambahan.

## Rubrik

- Menyatakan $\angle ADB = 90^\circ$ dan $\angle AEB = 90^\circ$ beserta alasannya
- Menyimpulkan bahwa $D$ dan $E$ terletak pada lingkaran berdiameter $AB$, dengan menyebut
  kebalikan teorema sudut pada setengah lingkaran sebagai alasannya
- Menyatakan bahwa $A$, $H$, $D$ segaris dan $B$, $H$, $E$ segaris, sehingga $AD$ dan $BE$
  adalah talibusur lingkaran itu yang melalui $H$
- Menyebut bahwa $H$ berada di dalam lingkaran itu, sebagai alasan memakai bentuk talibusur
  berpotongan
- Menerapkan kuasa titik dan menuliskan kesimpulannya

Bukti lewat kesebangunan $\triangle AHE \sim \triangle BHD$ dinilai penuh, asalkan kedua
sudut yang dipakai disebut — satu siku-siku, satu bertolak belakang — dan perbandingan
sisinya ditulis mengikuti padanan hurufnya.
