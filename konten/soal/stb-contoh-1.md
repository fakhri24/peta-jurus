---
id: stb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [segiempat-talibusur]
bentuk: isian
kesulitan: 3
jawaban: "64"
---

## Soal

Pada segitiga lancip $ABC$, dari $B$ ditarik garis tinggi yang memotong $AC$ tegak lurus di
$E$, dan dari $C$ ditarik garis tinggi yang memotong $AB$ tegak lurus di $F$.

![Segitiga ABC dengan alas BC mendatar dan puncak A di atas. Dari B ditarik garis tinggi ke sisi AC yang memotongnya tegak lurus di E, dan dari C ditarik garis tinggi ke sisi AB yang memotongnya tegak lurus di F. Kedua kaki itu dihubungkan oleh ruas EF](segitiga-dua-garis-tinggi.svg)

Diketahui $\angle ABC = 64^\circ$.

Tentukan besar $\angle AEF$ dalam derajat.

## Petunjuk

- Gambarnya memuat dua sudut siku-siku. Perhatikan ruas mana yang dihadapi keduanya.
- Sudut $\angle BEC$ dan $\angle BFC$ dua-duanya $90^\circ$ dan dua-duanya menghadap ruas $BC$. Apa artinya bagi keempat titik $B$, $C$, $E$, $F$?
- Setelah keempatnya terbukti pada satu lingkaran, pakai sudut luar segiempat talibusur pada titik $E$.

## Pembahasan

**Kenali pemicunya.** Di gambar ada **dua sudut siku-siku yang menghadap ruas yang sama**:

$$\angle BEC = 90^\circ \qquad \text{dan} \qquad \angle BFC = 90^\circ$$

keduanya menghadap $BC$. Itu pemicu paling produktif jurus ini.

**Simpulkan keempat titiknya setalibusur.** Sudut siku-siku yang menghadap suatu ruas berarti
titik sudutnya berada pada lingkaran berdiameter ruas itu. Karena $E$ dan $F$ dua-duanya
melihat $BC$ dengan sudut $90^\circ$, keduanya berada pada lingkaran berdiameter $BC$ — dan
$B$ serta $C$ jelas berada di sana juga.

Jadi $B$, $C$, $E$, $F$ terletak pada **satu lingkaran**, yang berpusat di titik tengah $BC$.

**Pakai lingkarannya untuk memindahkan sudut.** Pada segiempat talibusur $BFEC$, sudut luar di
salah satu titik sudut sama dengan sudut dalam di titik seberangnya. Sudut $\angle AEF$ adalah
sudut luar di $E$ — sebab $A$, $E$, $C$ segaris — dan titik seberangnya adalah $B$:

$$\angle AEF = \angle FBC = \angle ABC = 64^\circ$$

$$\boxed{64^\circ}$$

### Menemukan lingkarannya bukan jawaban

Ini jebakan yang disebut di halaman jurus, dan soal ini dirancang untuk melatihnya. Banyak
jawaban berhenti setelah menuliskan "$B$, $C$, $E$, $F$ setalibusur" — padahal pernyataan itu
belum menjawab apa pun.

Lingkaran adalah **alat pemindah sudut**. Nilainya baru muncul di langkah berikutnya, saat
sudut di satu sudut gambar dipindahkan ke sudut yang lain. Kalau setelah menemukan
lingkarannya tidak ada sudut yang berpindah, lingkarannya belum dipakai.

### Cara kedua: lewat kesebangunan

Karena $\angle AEB = \angle AFC = 90^\circ$ dan sudut di $A$ dipakai bersama,
$\triangle AEB \sim \triangle AFC$, sehingga

$$\frac{AE}{AF} = \frac{AB}{AC} \quad \Longrightarrow \quad \frac{AE}{AB} = \frac{AF}{AC}$$

Dipadu sudut $A$ yang sama, ini memberi $\triangle AEF \sim \triangle ABC$ menurut S-Sd-S,
sehingga $\angle AEF = \angle ABC = 64^\circ$ ✓.

Dua jalan yang sepenuhnya berbeda memberi angka yang sama — pemeriksaan yang jauh lebih
meyakinkan daripada mengulang jalan yang sama.

### Yang ikut terbukti

Dari kesebangunan $\triangle AEF \sim \triangle ABC$ juga terbaca

$$\angle AFE = \angle ACB = 180^\circ - 64^\circ - \angle BAC$$

Dengan $\angle ABC = 64^\circ$, kalau soal juga memberi $\angle BAC = 66^\circ$, maka
$\angle ACB = 50^\circ$ dan $\angle AFE = 50^\circ$.

Perhatikan bahwa $\angle AEF$ tidak bergantung pada $\angle BAC$ sama sekali — ia selalu sama
dengan $\angle ABC$, berapa pun bentuk segitiga lancipnya.

### Kenapa "lancip" disebut di soal

Kalau segitiganya tumpul, salah satu kaki garis tinggi jatuh di **perpanjangan** sisinya, bukan
di dalamnya. Keempat titiknya tetap setalibusur — kenyataan itu tidak bergantung pada bentuk
segitiga — tetapi $A$, $E$, $C$ tidak lagi tersusun seperti yang diandaikan, sehingga
"$\angle AEF$ adalah sudut luar di $E$" perlu ditinjau ulang.

Syarat semacam ini menjaga gambarnya tunggal. Perhatikan tiap kali soal menyebutnya.
