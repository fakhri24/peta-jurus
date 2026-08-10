---
id: sdl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [sudut-lingkaran]
bentuk: isian
kesulitan: 2
jawaban: "64"
---

## Soal

Pada lingkaran berpusat $O$, ruas $AB$ adalah diameter dan titik $C$ terletak pada keliling
lingkaran.

![Lingkaran berpusat O dengan AB sebagai diameter mendatar, A di kiri dan B di kanan. Titik C di keliling lingkaran di atas AB. Tali busur AC dan CB digambar, begitu pula jari-jari OC. Sudut CAB besarnya 32 derajat dan sudut COB ditanyakan](lingkaran-diameter-sudut.svg)

Diketahui $\angle CAB = 32^\circ$.

Tentukan besar $\angle COB$ dalam derajat.

## Petunjuk

- Perhatikan kedua sudut itu: yang satu titik sudutnya di keliling, yang satu di pusat. Adakah bagian lingkaran yang sama-sama dihadapi keduanya?
- Keduanya menghadap busur $BC$ yang sama — yang satu dari keliling, yang satu dari pusat.
- Sudut keliling besarnya setengah sudut pusat yang menghadap busur yang sama.

## Pembahasan

**Tentukan busur yang dihadapi masing-masing.** Ini langkah yang menentukan, dan yang paling
sering dilewati.

- $\angle CAB$ bertitik sudut di $A$, yang ada di **keliling**. Kedua kakinya menuju $C$ dan
  $B$, jadi ia menghadap busur $BC$ — tepatnya busur $BC$ yang **tidak** memuat $A$.
- $\angle COB$ bertitik sudut di $O$, yaitu **pusat**. Kedua kakinya menuju $C$ dan $B$, jadi
  ia menghadap busur $BC$ yang sama.

**Pakai hubungan pusat–keliling.** Keduanya menghadap busur yang sama, sehingga

$$\angle COB = 2 \times \angle CAB = 2 \times 32^\circ = \boxed{64^\circ}$$

### Periksa lewat jalan yang sama sekali berbeda

Karena $AB$ diameter, sudut keliling yang menghadapnya siku-siku:

$$\angle ACB = 90^\circ$$

Maka pada $\triangle ABC$,

$$\angle ABC = 180^\circ - 90^\circ - 32^\circ = 58^\circ$$

Sekarang lihat $\triangle OCB$. Karena $OC$ dan $OB$ dua-duanya jari-jari, segitiga itu **sama
kaki**, sehingga $\angle OCB = \angle OBC = 58^\circ$, dan

$$\angle COB = 180^\circ - 58^\circ - 58^\circ = 64^\circ$$

Cocok. Perhatikan bahwa jalan kedua ini sama sekali tidak memakai hubungan pusat–keliling — ia
hanya memakai jari-jari yang sama panjang dan jumlah sudut segitiga. Sesungguhnya itulah bukti
hubungan tersebut, dijalankan pada satu kasus.

### Dua hal gratis yang selalu ada di lingkaran

**Setiap jari-jari sama panjang.** Setiap kali kamu menarik dua jari-jari, kamu mendapat
segitiga sama kaki — dan segitiga sama kaki berarti dua sudut sama besar. Ini sumber sudut
tergampang di seluruh soal lingkaran, dan tidak perlu diberikan soal.

**Diameter berarti sudut siku-siku.** Kalau soal menyebut salah satu tali busur adalah
diameter, itu sama saja dengan memberimu $90^\circ$ di setiap titik keliling secara cuma-cuma.
Kata "diameter" adalah salah satu pemicu paling padat isi di soal geometri.

### Kekeliruan yang paling sering

Menjawab $\angle COB = 32^\circ \div 2 = 16^\circ$ — arah pembagiannya terbalik. Cara
mengingat yang tidak bisa tertukar: **sudut pusat selalu yang lebih besar**, sebab ia berdiri
lebih dekat ke busurnya. Kalau jawabanmu membuat sudut pusat lebih kecil daripada sudut
keliling, kamu membaginya di tempat yang salah.
