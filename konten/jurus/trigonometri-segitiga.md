---
id: trigonometri-segitiga
nama: Aturan Sinus dan Kosinus
pilar: geometri
tahap: osn-p
prasyarat: [pythagoras, luas-bidang]
contoh: [trg-contoh-1]
latihan: [trg-01, trg-02, trg-03, trg-04, trg-05, trg-06]
---

## Kapan dipakai

Soal mencampur **panjang dan sudut** pada segitiga yang tidak siku-siku. Pythagoras tidak
bisa dipakai, kesebangunan tidak ada, tetapi cukup unsur diketahui untuk menghitung —
biasanya tiga unsur.

Aturan mana yang dipakai ditentukan oleh unsur yang diketahui:

- diketahui **dua sisi dan sudut apitnya**, atau **ketiga sisi** → aturan kosinus;
- diketahui **dua sudut dan satu sisi**, atau **dua sisi dan sudut di hadapan salah
  satunya** → aturan sinus.

Pemicu ketiga yang khas olimpiade: soal menyebut jari-jari lingkaran **luar**. Bentuk
lengkap aturan sinus memuat $2R$, jadi ia jembatan langsung antara sudut dan lingkaran
luar.

## Intinya

**Aturan kosinus**, perluasan Pythagoras ke sudut sembarang:

$$c^2 = a^2 + b^2 - 2ab\cos C$$

Kalau $C = 90^\circ$ suku terakhirnya hilang dan ia kembali menjadi Pythagoras. Bentuk
yang dibalik dipakai kalau ketiga sisinya diketahui:

$$\cos C = \frac{a^2+b^2-c^2}{2ab}$$

**Aturan sinus**, lengkap dengan jari-jari lingkaran luar:

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

Bagian $2R$ itu yang sering menyelesaikan soal olimpiade, dan justru yang paling sering
tidak diajarkan.

**Luas dengan sudut:**

$$L = \tfrac{1}{2} ab \sin C$$

**Hubungan yang berlaku pada setiap segitiga**, karena $A+B+C = 180^\circ$:

$$\sin(A+B) = \sin C, \qquad \cos(A+B) = -\cos C$$

Keduanya sering memangkas ekspresi trigonometri yang terlihat buntu.

## Jebakan umum

- **Kasus mendua pada aturan sinus.** Kalau yang diketahui dua sisi dan sudut yang **tidak**
  diapitnya, bisa ada dua segitiga yang memenuhi — satu lancip, satu tumpul. Periksa
  keduanya, jangan langsung ambil hasil kalkulator.
- **Salah pasangan pada aturan kosinus.** Sudut $C$ harus yang **berhadapan** dengan sisi
  $c$; tertukar sekali, seluruh perhitungannya salah tanpa terlihat aneh.
- **Lupa tanda kosinus pada sudut tumpul.** Untuk $C > 90^\circ$ nilai $\cos C$ negatif,
  jadi $c^2$ justru lebih besar dari $a^2+b^2$ — dan tanda minus di rumus tetap ditulis
  minus.
- **Memakai $\sin$ pada sudut yang bukan sudut segitiga.** Sudut apit harus benar-benar
  sudut di antara kedua sisi yang dipakai pada rumus luas.
