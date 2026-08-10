---
id: segiempat-talibusur
nama: Segiempat Talibusur
pilar: geometri
tahap: osn-k
prasyarat: [sudut-lingkaran]
contoh: [stb-contoh-1]
latihan: [stb-01, stb-02, stb-03, stb-04, stb-05, stb-06]
---

## Kapan dipakai

Soal menyebut empat titik **terletak pada satu lingkaran** — atau, jauh lebih sering,
tidak menyebutnya sama sekali dan justru memintamu membuktikannya. Pemicunya: ada dua
sudut yang berjumlah $180^\circ$, atau dua sudut sama besar yang menghadap ruas yang sama
dari sisi yang sama.

Pemicu yang paling produktif di soal olimpiade: gambar memuat **dua sudut siku-siku yang
menghadap ruas yang sama**. Keempat titiknya langsung terletak pada satu lingkaran
berdiameter ruas itu, dan biasanya seluruh soal terbuka dari sana.

Kalau soal memberi banyak sudut yang tampaknya tidak berhubungan, cari empat titik
setalibusur. Menemukannya mengubah sudut di satu sudut gambar menjadi sudut di sudut yang
lain.

## Intinya

**Sifat.** Kalau $ABCD$ segiempat talibusur, maka sudut yang berhadapan berjumlah lurus:

$$\angle A + \angle C = \angle B + \angle D = 180^\circ$$

dan sudut luar pada satu titik sudut sama dengan sudut dalam di titik seberangnya.

**Kebalikannya berlaku, dan itu yang paling banyak dipakai.** Keempat titik terletak pada
satu lingkaran kalau salah satu terpenuhi:

- sepasang sudut berhadapan berjumlah $180^\circ$;
- $\angle ACB = \angle ADB$, yakni dua titik melihat ruas $AB$ dengan sudut sama besar
  dari **sisi yang sama**;
- hasil kali potongan diagonalnya memenuhi hubungan kuasa titik.

**Luas.** Untuk segiempat talibusur dengan sisi $a,b,c,d$ dan setengah keliling $s$,

$$L = \sqrt{(s-a)(s-b)(s-c)(s-d)}$$

Bentuk ini (Brahmagupta) adalah perluasan Heron; kalau $d = 0$ ia kembali menjadi Heron.

## Jebakan umum

- **Dua sudut sama besar dari sisi berlawanan.** Kalau kedua titik berada di sisi
  berlawanan terhadap ruas itu, yang berlaku bukan "sama besar" melainkan "berjumlah
  $180^\circ$". Salah sisi berarti salah kesimpulan.
- **Mengira setiap segiempat punya lingkaran luar.** Hanya yang sudut berhadapannya
  berjumlah lurus. Persegi panjang dan segitiga sama kaki terpancung punya; jajaran genjang
  miring tidak.
- **Memakai Brahmagupta pada segiempat sembarang.** Rumus itu khusus segiempat talibusur;
  untuk yang lain hasilnya terlalu besar.
- **Berhenti setelah menemukan lingkarannya.** Menemukan empat titik setalibusur bukan
  jawaban — ia alat untuk memindahkan sudut. Kalau setelah itu tidak ada sudut yang
  dipindahkan, lingkarannya belum dipakai.
