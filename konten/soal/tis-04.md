---
id: tis-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "110"
---

## Soal

Pada segitiga lancip $ABC$ diketahui $\angle A = 50^\circ$ dan $\angle B = 60^\circ$. Titik
$H$ adalah titik tinggi segitiga itu.

Tentukan besar $\angle AHB$ dalam derajat.

## Petunjuk

- Titik tinggi adalah perpotongan ketiga garis tinggi, jadi di sekitarnya banyak sudut siku-siku. Cari segiempat yang dua sudutnya siku-siku.
- Perhatikan segiempat yang dibentuk oleh $A$, kaki garis tinggi dari $A$, $B$, dan kaki garis tinggi dari $B$.
- Sudut $\angle AHB$ hanya bergantung pada $\angle C$, bukan pada $\angle A$ maupun $\angle B$.

## Pembahasan

**Lengkapi sudut ketiganya.**

$$\angle C = 180^\circ - 50^\circ - 60^\circ = 70^\circ$$

**Cari hubungan $\angle AHB$ dengan $\angle C$.** Misalkan garis tinggi dari $A$ memotong
$BC$ di $D$, dan garis tinggi dari $B$ memotong $CA$ di $E$. Keduanya melalui $H$.

Perhatikan segiempat $CDHE$ — titik sudutnya $C$, kaki $D$, titik tinggi $H$, dan kaki $E$.
Dua sudutnya siku-siku:

$$\angle HDC = 90^\circ \ (AD \perp BC), \qquad \angle HEC = 90^\circ \ (BE \perp CA)$$

Jumlah sudut segiempat $360^\circ$, sehingga

$$\angle DHE = 360^\circ - 90^\circ - 90^\circ - \angle C = 180^\circ - \angle C$$

Sudut $\angle AHB$ bertolak belakang dengan $\angle DHE$ — sebab $A$, $H$, $D$ segaris dan
$B$, $H$, $E$ segaris — sehingga keduanya sama besar:

$$\angle AHB = 180^\circ - \angle C$$

**Hitung.**

$$\angle AHB = 180^\circ - 70^\circ = \boxed{110^\circ}$$

### Periksa ketiga sudut di sekeliling $H$

Dengan cara yang sama:

$$\angle BHC = 180^\circ - \angle A = 130^\circ, \qquad
\angle AHC = 180^\circ - \angle B = 120^\circ$$

Ketiganya mengelilingi $H$ sepenuhnya, jadi jumlahnya harus $360^\circ$:

$$110 + 130 + 120 = 360 \quad ✓$$

Pemeriksaan ini menangkap kesalahan pemasangan huruf dengan sekali hitung: kalau salah satu
sudut dipasangkan ke sudut segitiga yang keliru, jumlahnya tidak lagi $360^\circ$.

### Jangan tertukar: yang menentukan $\angle AHB$ adalah $\angle C$

Godaannya besar untuk menjawab $180^\circ - 50^\circ$ atau $180^\circ - 60^\circ$, karena
kedua sudut itu yang disebutkan soal. Yang benar justru sudut **ketiga** — yang tidak
disebut, dan yang titik sudutnya tidak muncul di lambang $\angle AHB$.

Pola yang menyelamatkan: pada $\angle AHB$, huruf yang **hilang** adalah $C$, dan itulah
sudut yang menentukan.

Bandingkan dengan pusat lingkaran dalam: pada $\angle BIC = 90^\circ + \tfrac12 A$, huruf
yang hilang juga $A$. Pola "huruf yang hilang" berlaku untuk ketiga titik istimewa sekaligus.

### Kalau segitiganya tumpul

Keterangan "lancip" di soal ini bukan hiasan, tetapi akibatnya lebih halus daripada yang
diduga. Kalau segitiganya tumpul, $H$ jatuh di **luar** segitiga dan segiempat $CDHE$ tidak
lagi terbentuk seperti di atas — jadi turunan di atas gugur, dan kesimpulannya harus
diperiksa ulang, bukan langsung dianggap gugur juga.

Hasilnya bercabang menurut **sudut mana** yang tumpul:

- $\angle A$ dan $\angle B$ keduanya lancip (termasuk saat $\angle C$ tumpul) →
  $\angle AHB = 180^\circ - \angle C$, sama seperti kasus lancip. Untuk $\angle C = 110^\circ$
  misalnya, $\angle AHB = 70^\circ$.
- salah satu dari $\angle A$ atau $\angle B$ tumpul → $\angle AHB = \angle C$. Untuk
  $\angle A = 120^\circ$, $\angle B = \angle C = 30^\circ$, sudut $\angle AHB$ keluar
  $30^\circ$, bukan $150^\circ$.

Pola di baliknya: yang menentukan bukan letak $H$ terhadap segitiga, melainkan apakah $H$ dan
$C$ berada di sisi yang sama dari garis $AB$. Kalau sesisi, sudutnya $\angle C$; kalau
berseberangan, pelurusnya.

Karena itu, pada soal titik tinggi, **periksa dulu jenis segitiganya** sebelum memakai rumus.
Titik tinggi satu-satunya di antara keempat titik istimewa yang bisa keluar dari segitiga —
dan satu-satunya yang rumus sudutnya ikut berubah karenanya.

### Sudut yang sama dari ketiga titik istimewa

Untuk segitiga lancip dengan $\angle C = 70^\circ$:

| Titik | Sudut memandang $AB$ | Nilai |
|---|---|---|
| Titik tinggi $H$ | $180^\circ - C$ | $110^\circ$ |
| Pusat dalam $I$ | $90^\circ + \tfrac12 C$ | $125^\circ$ |
| Pusat luar $O$ | $2C$ | $140^\circ$ |

Ketiganya berbeda, dan ketiganya melebihi $\angle C$ sendiri. Yang menjelaskannya sudut
keliling: ketiga titik itu berada di dalam lingkaran luar, dan sebuah ruas dipandang dengan
sudut lebih besar dari titik di dalam lingkaran daripada dari titik pada lingkarannya.
