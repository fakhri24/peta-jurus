---
id: stb-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [segiempat-talibusur]
bentuk: isian
kesulitan: 3
jawaban: "80"
---

## Soal

Segiempat $ABCD$ mempunyai keempat titik sudut pada satu lingkaran, dan kedua diagonalnya
digambar. Diketahui $\angle ADB = 42^\circ$ dan $\angle BDC = 38^\circ$.

![Segiempat ABCD yang keempat titik sudutnya pada satu lingkaran, dengan A di kiri, B di kanan atas, C di kanan, dan D di bawah. Kedua diagonalnya digambar. Di titik D, diagonal DB membagi sudut ADC menjadi sudut ADB 42 derajat dan sudut BDC 38 derajat](segiempat-talibusur-diagonal.svg)

Tentukan nilai $\angle ACB + \angle BAC$ dalam derajat.

## Petunjuk

- Keempat sudut yang disebut soal bertitik sudut di tempat yang berbeda-beda. Untuk tiap sudut, tentukan dulu tali busur mana yang dihadapinya.
- Sudut $\angle ADB$ dan $\angle ACB$ sama-sama menghadap tali busur $AB$ dari sisi yang sama.
- Kerjakan hal yang sama untuk $\angle BDC$ dan $\angle BAC$, yang sama-sama menghadap $BC$.

## Pembahasan

**Tentukan tali busur yang dihadapi tiap sudut.** Ini seluruh isi soalnya; sisanya penjumlahan.

| Sudut | Titik sudutnya | Tali busur yang dihadapi |
|---|---|---|
| $\angle ADB$ | $D$ | $AB$ |
| $\angle ACB$ | $C$ | $AB$ |
| $\angle BDC$ | $D$ | $BC$ |
| $\angle BAC$ | $A$ | $BC$ |

**Pasangan pertama.** Sudut $\angle ADB$ dan $\angle ACB$ sama-sama menghadap tali busur $AB$,
dan titik $C$ serta $D$ berada di **sisi yang sama** terhadap $AB$ — keduanya di busur yang
sama. Maka keduanya sama besar:

$$\angle ACB = \angle ADB = 42^\circ$$

**Pasangan kedua.** Dengan alasan yang sama untuk tali busur $BC$, dengan $A$ dan $D$ di sisi
yang sama:

$$\angle BAC = \angle BDC = 38^\circ$$

**Jumlahkan.**

$$\angle ACB + \angle BAC = 42^\circ + 38^\circ = \boxed{80^\circ}$$

### Bacaan lain dari jawabannya

Karena $\angle ACB$ dan $\angle BAC$ adalah dua sudut segitiga $ABC$, sudut ketiganya

$$\angle ABC = 180^\circ - 80^\circ = 100^\circ$$

Dan periksa: $\angle ADC = \angle ADB + \angle BDC = 42^\circ + 38^\circ = 80^\circ$. Karena
$B$ dan $D$ berhadapan pada segiempat talibusur, seharusnya $\angle ABC + \angle ADC =
180^\circ$ — dan benar $100^\circ + 80^\circ = 180^\circ$ ✓.

Pemeriksaan ini memakai sifat yang berbeda dari yang dipakai menghitung, jadi ia benar-benar
menguji, bukan sekadar mengulang.

### Kesalahan "sisi yang sama" yang menentukan segalanya

Dua sudut keliling yang menghadap tali busur yang sama:

- dari **sisi yang sama** — sama besar;
- dari **sisi berlawanan** — berjumlah $180^\circ$.

Kalau pada soal ini $C$ dan $D$ dianggap berada di sisi berlawanan terhadap $AB$, jawabannya
menjadi $138^\circ$, bukan $42^\circ$ — dan tidak ada tanda apa pun pada perhitungannya bahwa
itu salah.

Karena itu jangan pernah melewati langkah "sisi mana". Pada gambar, urutan titiknya di
keliling — $A$, $B$, $C$, $D$ berurutan — yang menentukannya.

### Melihatnya sebagai satu gerakan

Yang baru saja terjadi: dua sudut yang semula bertumpuk di titik $D$ **dipindahkan** ke dua
titik lain, $C$ dan $A$, tempat keduanya berguna. Itu kegunaan sesungguhnya dari lingkaran di
soal geometri — bukan menghitung, melainkan memindahkan.
