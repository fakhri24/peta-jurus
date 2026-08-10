---
id: ptl-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy, kesebangunan]
bentuk: uraian
kesulitan: 4
---

## Soal

Diberikan segiempat talibusur $ABCD$ dengan titik-titik sudutnya terurut mengelilingi
lingkaran.

Buktikan teorema Ptolemy:

$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

## Petunjuk

- Ruas kanannya jumlah dua suku, ruas kirinya satu hasil kali. Jadi diagonal $AC$ perlu **dipecah dua** oleh sebuah titik.
- Ambil titik $K$ pada diagonal $AC$ sedemikian sehingga $\angle ABK = \angle DBC$. Dengan pilihan itu, dua pasang segitiga menjadi sebangun.
- Pasangan pertama $\triangle ABK \sim \triangle DBC$; pasangan kedua $\triangle KBC \sim \triangle ABD$. Tulis perbandingan sisinya, lalu jumlahkan.

## Pembahasan

**Buat titik bantunya.** Pilih titik $K$ pada diagonal $AC$ sehingga

$$\angle ABK = \angle DBC$$

Titik seperti ini ada dan tunggal. Alasannya: karena urutan kelilingnya $A$, $B$, $C$, $D$,
titik $D$ berada pada busur $CA$ yang tidak memuat $B$, sehingga sinar $BD$ terletak **di
dalam** sudut $\angle ABC$ dan

$$\angle ABD + \angle DBC = \angle ABC$$

Khususnya $\angle DBC < \angle ABC$. Maka sinar dari $B$ yang membentuk sudut sebesar
$\angle DBC$ dengan $BA$, diukur ke arah dalam sudut $\angle ABC$, juga terletak di dalam
sudut itu — dan setiap sinar dari $B$ yang di dalam $\angle ABC$ memotong ruas $AC$ tepat
sekali.

**Pasangan sebangun pertama: $\triangle ABK$ dan $\triangle DBC$.**

- $\angle ABK = \angle DBC$ menurut pilihan $K$;
- $\angle BAK = \angle BAC = \angle BDC$, sebab keduanya sudut keliling yang menghadap busur
  $BC$ yang sama.

Dua pasang sudut sama besar, maka $\triangle ABK \sim \triangle DBC$, sehingga

$$\frac{AK}{DC} = \frac{AB}{DB} \quad \Longrightarrow \quad AK \cdot DB = AB \cdot DC \tag{1}$$

**Pasangan sebangun kedua: $\triangle KBC$ dan $\triangle ABD$.**

Karena $BK$ berada di dalam $\angle ABC$, berlaku $\angle ABK + \angle KBC = \angle ABC$.
Dari langkah sebelumnya, $\angle ABD + \angle DBC = \angle ABC$ juga. Samakan keduanya:

$$\angle ABK + \angle KBC = \angle ABD + \angle DBC$$

Karena $\angle ABK = \angle DBC$ menurut pilihan $K$, kedua suku itu bisa dicoret dan tersisa

$$\angle KBC = \angle ABD$$

Sudut kedua:

- $\angle ADB = \angle ACB = \angle KCB$, sebab keduanya sudut keliling yang menghadap busur
  $AB$ yang sama.

Maka $\triangle KBC \sim \triangle ABD$, sehingga

$$\frac{KC}{AD} = \frac{BC}{BD} \quad \Longrightarrow \quad KC \cdot BD = AD \cdot BC \tag{2}$$

**Jumlahkan (1) dan (2).**

$$AK \cdot BD + KC \cdot BD = AB \cdot CD + AD \cdot BC$$

$$\left(AK + KC\right) \cdot BD = AB \cdot CD + BC \cdot AD$$

Karena $K$ terletak **pada ruas** $AC$, berlaku $AK + KC = AC$, sehingga

$$AC \cdot BD = AB \cdot CD + BC \cdot AD \qquad \blacksquare$$

### Dari mana ide titik $K$

Ruas kanan punya dua suku, ruas kiri satu hasil kali dengan faktor $BD$ yang muncul di
keduanya. Kalau $BD$ difaktorkan keluar, yang tersisa harus berbentuk "sesuatu ditambah
sesuatu sama dengan $AC$" — dan satu-satunya cara alami memecah $AC$ jadi dua bagian adalah
menaruh sebuah titik padanya.

Setelah itu tinggal mencari titik yang membuat kedua bagiannya punya arti. Syarat
$\angle ABK = \angle DBC$ dipilih justru supaya pasangan sebangunnya terbentuk.

Pola ini layak diingat melampaui buktinya sendiri: **kalau sebuah kesamaan berbentuk
"satu = jumlah dua", carilah titik yang memecah salah satu ruasnya.**

### Langkah yang paling sering hilang

Tiga hal, dan ketiganya soal letak, bukan soal hitungan:

1. **$K$ benar-benar ada pada ruas $AC$**, bukan di perpanjangannya. Kalau tidak,
   $AK + KC \ne AC$ dan langkah terakhirnya gugur.
2. **Kedua pasang sudut keliling menghadap busur yang sama.** Menyebut "sudut keliling" saja
   tidak cukup; busurnya harus disebut.
3. **Urutan $A$, $B$, $C$, $D$ mengelilingi lingkaran** dipakai di kedua tempat itu. Untuk
   urutan yang diacak, pernyataannya sendiri salah.

### Kenapa ketaksamaannya berlaku untuk empat titik sembarang

Kalau keempat titik tidak setalibusur, kesamaan sudut kelilingnya gugur dan kedua segitiga
tidak lagi sebangun. Yang bertahan: titik $K$ masih bisa dibuat, dan kedua hubungan menjadi
ketaksamaan yang arahnya sama.

Hasilnya

$$AC \cdot BD \ \le\ AB \cdot CD + BC \cdot AD$$

untuk empat titik sembarang, dengan kesamaan tepat saat keempatnya setalibusur dengan urutan
yang benar. Bukti lengkapnya lebih rapi dengan inversi, tetapi arah ketaksamaannya sudah bisa
diraba dari sini.

## Rubrik

- Membuat titik $K$ pada $AC$ dengan syarat $\angle ABK = \angle DBC$, dan menyebut alasan
  titik itu ada di dalam ruas $AC$
- Menyatakan $\triangle ABK \sim \triangle DBC$ dengan **kedua** pasangan sudutnya beserta
  alasan masing-masing, termasuk busur yang dihadapi sudut kelilingnya
- Menurunkan $AK \cdot BD = AB \cdot CD$
- Menunjukkan $\angle ABD = \angle KBC$ dengan menambahkan $\angle KBC$ pada kedua ruas
- Menyatakan $\triangle KBC \sim \triangle ABD$ beserta alasan sudut kedua, dan menurunkan
  $KC \cdot BD = BC \cdot AD$
- Menjumlahkan keduanya dan memakai $AK + KC = AC$ untuk menutup buktinya

Bukti yang memakai inversi berpusat di salah satu titik sudut dinilai penuh, asalkan
rumus jarak setelah inversi dinyatakan dan dipakai dengan benar.
