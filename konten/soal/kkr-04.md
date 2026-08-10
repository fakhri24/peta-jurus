---
id: kkr-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kekongruenan]
bentuk: uraian
kesulitan: 2
---

## Soal

Pada segitiga $ABC$ berlaku $AB = AC$. Titik $P$ terletak pada sisi $AB$ dan titik $Q$
terletak pada sisi $AC$, sedemikian sehingga $AP = AQ$.

Buktikan bahwa $BQ = CP$.

## Petunjuk

- Ruas $BQ$ dan $CP$ berpotongan di tengah gambar dan tidak berada pada satu segitiga. Cari dua segitiga yang masing-masing memuat satu di antaranya.
- Pandang $\triangle ABQ$ dan $\triangle ACP$. Keduanya berbagi sesuatu di titik $A$ yang tidak perlu dihitung sama sekali.
- Sudut di $A$ dipakai bersama kedua segitiga, dan ia terapit oleh sisi-sisi yang panjangnya sudah diketahui sama.

## Pembahasan

**Pilih dua segitiganya.** Ruas $BQ$ adalah sisi $\triangle ABQ$, dan ruas $CP$ adalah sisi
$\triangle ACP$. Kalau kedua segitiga itu kongruen, kesimpulannya langsung didapat.

**Kumpulkan bahannya.**

1. $AB = AC$ — diberikan;
2. $AQ = AP$ — diberikan;
3. $\angle BAQ = \angle CAP$ — keduanya **sudut yang sama**, yaitu $\angle BAC$. Karena $P$
   pada $AB$ maka sinar $AP$ berimpit dengan sinar $AB$, dan karena $Q$ pada $AC$ maka sinar
   $AQ$ berimpit dengan sinar $AC$.

**Periksa susunannya.** Pada $\triangle ABQ$, sudut $\angle BAQ$ terletak di antara sisi $AB$
dan sisi $AQ$. Pada $\triangle ACP$, sudut $\angle CAP$ terletak di antara sisi $AC$ dan sisi
$AP$. Sudutnya diapit kedua sisi yang diketahui, jadi susunannya **S-Sd-S**:

$$\triangle ABQ \cong \triangle ACP \quad (\text{S-Sd-S})$$

**Baca sisi yang bersesuaian.** Pasangannya $A \leftrightarrow A$, $B \leftrightarrow C$,
$Q \leftrightarrow P$, sehingga sisi $BQ$ bersesuaian dengan sisi $CP$:

$$BQ = CP \qquad \blacksquare$$

### Sudut yang dipakai bersama

Bahan ketiga di atas layak diperhatikan, sebab ia tidak berbentuk "dua sudut yang kebetulan
sama besar" melainkan **satu sudut yang sama, dipandang dari dua segitiga**. Sama seperti sisi
berimpit pada soal lain, unsur semacam ini gratis — tidak perlu dihitung, tidak perlu
diturunkan — dan justru karena gratis, ia yang paling sering terlewat.

Isyaratnya di gambar: dua segitiga yang **berbagi satu titik sudut** dan sisi-sisinya terletak
pada sinar yang sama.

### Yang ikut terbukti tanpa tambahan pekerjaan

Dari kekongruenan yang sama juga didapat $\angle ABQ = \angle ACP$. Dipadu dengan
$\angle ABC = \angle ACB$ (karena $AB = AC$), pengurangannya memberi

$$\angle QBC = \angle PCB$$

yang berarti segitiga yang dibentuk $B$, $C$, dan titik potong $BQ$ dengan $CP$ juga sama
kaki. Soal lanjutan sering menanyakan tepat hal itu, dan jawabannya sudah tersedia dari
langkah yang sudah dikerjakan.

### Dua cara menuliskan kesimpulan yang salah

- Menulis $\triangle ABQ \cong \triangle APC$: pasangan hurufnya mengklaim $AB = AP$, padahal
  $P$ ada **pada** $AB$ sehingga $AP < AB$. Kekongruenannya benar, penulisannya salah, dan
  kesimpulan yang dibaca darinya akan salah.
- Menyebut alasannya "S-S-S" dengan berpikir $BQ = CP$ sebagai sisi ketiga. Itu memakai apa
  yang hendak dibuktikan sebagai bahan buktinya sendiri.

## Rubrik

- Memilih $\triangle ABQ$ dan $\triangle ACP$ sebagai dua segitiga yang dibandingkan
- Menyebut $AB = AC$ dan $AQ = AP$ dari soal
- Menyatakan bahwa sudut di $A$ dipakai bersama kedua segitiga, dengan alasan $P$ pada $AB$ dan $Q$ pada $AC$
- Memeriksa bahwa sudut itu diapit kedua sisi, lalu menyebut S-Sd-S
- Menuliskan kekongruenannya dengan pasangan titik yang berurutan benar
- Menyimpulkan $BQ = CP$ sebagai sisi bersesuaian
