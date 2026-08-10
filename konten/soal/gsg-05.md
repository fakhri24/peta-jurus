---
id: gsg-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung, sudut-lingkaran]
bentuk: isian
kesulitan: 2
jawaban: "58"
---

## Soal

Garis $PT$ menyinggung sebuah lingkaran di titik $T$. Tali busur $TA$ ditarik sehingga
$\angle PTA = 58^\circ$. Titik $B$ terletak pada busur besar, yaitu di sisi tali busur $TA$
yang berlawanan dengan sisi tempat $P$ berada.

![Lingkaran dengan garis singgung mendatar yang menyentuhnya di titik T di bawah. Titik P pada garis singgung di sebelah kanan T. Tali busur TA ditarik ke titik A di kanan atas lingkaran, dan titik B di kiri atas lingkaran dihubungkan ke T dan ke A. Sudut PTA besarnya 58 derajat dan sudut TBA ditanyakan](singgung-talibusur.svg)

Tentukan besar $\angle TBA$ dalam derajat.

## Petunjuk

- Sudut yang diketahui dibentuk oleh garis singgung dan tali busur, sedangkan yang ditanyakan sudut keliling biasa. Adakah aturan yang menghubungkan keduanya?
- Sudut antara garis singgung dan tali busur sama besar dengan sudut keliling yang menghadap tali busur itu dari busur seberangnya.
- Titik $B$ memang berada di busur seberangnya, jadi aturannya berlaku langsung.

## Pembahasan

**Kenali kedua sudutnya.**

- $\angle PTA$ dibentuk oleh garis singgung $TP$ dan tali busur $TA$.
- $\angle TBA$ adalah sudut keliling yang menghadap tali busur $TA$, diukur dari titik $B$ di
  busur **seberang** $P$.

**Pakai sifat sudut singgung–tali busur.** Keduanya sama besar:

$$\angle TBA = \angle PTA = \boxed{58^\circ}$$

### Kenapa sifat itu benar

Tarik diameter dari $T$, sebut ujung satunya $D$. Karena $TD$ diameter, $\angle TAD = 90^\circ$,
sehingga pada $\triangle TAD$

$$\angle ATD = 90^\circ - \angle ADT$$

Di sisi lain, jari-jari tegak lurus garis singgung di $T$, jadi $\angle PTD = 90^\circ$ dan

$$\angle PTA = 90^\circ - \angle ATD = \angle ADT$$

Terakhir, $\angle ADT$ dan $\angle ABT$ adalah dua sudut keliling yang menghadap tali busur
$TA$ dari sisi yang sama, sehingga keduanya sama besar. Maka $\angle PTA = \angle TBA$.

Penurunan lima baris ini layak dicoba sendiri sekali, sebab ia memakai kedua sifat inti jurus
ini — jari-jari tegak lurus singgung, dan sudut menghadap diameter — dan mengingatkan bahwa
sifat singgung–tali busur bukan aturan baru, melainkan akibat.

### Sisi yang menentukan jawabannya

Kalau $B$ dipindahkan ke busur **kecil** — sisi yang sama dengan $P$ — maka $B$ dan titik-titik
di busur seberang berada di sisi berlawanan terhadap tali busur $TA$, sehingga

$$\angle TBA = 180^\circ - 58^\circ = 122^\circ$$

Satu titik pindah sisi, jawabannya berubah dari $58^\circ$ menjadi $122^\circ$. Karena itu
kalimat "di sisi yang berlawanan dengan $P$" pada soal adalah **data**, bukan keterangan
tambahan.

### Sudut di sisi yang lain dari garis singgung

Kalau $Q$ diambil pada garis singgung di sisi berlawanan dari $P$ terhadap $T$, maka
$\angle QTA$ berpelurus dengan $\angle PTA$:

$$\angle QTA = 180^\circ - 58^\circ = 122^\circ$$

dan ia sama dengan sudut keliling yang menghadap $TA$ dari busur kecil. Jadi aturan yang sama
berlaku di kedua sisi — asalkan tiap sudut dipasangkan dengan busur yang benar.
