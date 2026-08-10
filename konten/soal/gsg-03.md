---
id: gsg-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung, pythagoras]
bentuk: isian
kesulitan: 3
jawaban: "12"
---

## Soal

Dua lingkaran berjari-jari $4$ dan $9$ bersinggungan dari luar. Sebuah garis menyinggung
kedua lingkaran itu, menyentuh yang kecil di $X$ dan yang besar di $Y$.

![Dua lingkaran yang bersinggungan dari luar, yang kecil di kiri dan yang besar di kanan, keduanya menyinggung satu garis mendatar di bawahnya. Titik singgung pada garis itu adalah X untuk lingkaran kecil dan Y untuk lingkaran besar. Kedua pusat dihubungkan oleh ruas yang melewati titik singgung kedua lingkaran, dan tiap jari-jari ke garis mendatar tegak lurus terhadapnya](dua-lingkaran-singgung.svg)

Tentukan panjang $XY$.

## Petunjuk

- Dua kenyataan tersedia gratis: jarak kedua pusat, dan sudut yang dibentuk tiap jari-jari dengan garis singgungnya.
- Jarak kedua pusat $4 + 9 = 13$, dan $PX$ serta $QY$ dua-duanya tegak lurus garis singgungnya.
- Bangun $PXYQ$ adalah trapesium siku-siku. Geser salah satu sisi tegaknya untuk membuat segitiga siku-siku.

## Pembahasan

**Kumpulkan yang gratis.** Sebut pusat lingkaran kecil $P$ dan pusat lingkaran besar $Q$.

- Kedua lingkaran bersinggungan **luar**, jadi $PQ = 4 + 9 = 13$.
- $PX \perp XY$ dan $QY \perp XY$, sebab jari-jari tegak lurus garis singgung.

**Kenali bangunnya.** Karena $PX$ dan $QY$ dua-duanya tegak lurus $XY$, keduanya sejajar, dan
$PXYQ$ adalah **trapesium siku-siku** dengan sisi sejajar $PX = 4$ dan $QY = 9$.

**Ubah menjadi segitiga siku-siku.** Tarik dari $P$ garis sejajar $XY$, memotong $QY$ di $R$.
Maka $PXYR$ persegi panjang, sehingga

$$PR = XY \qquad \text{dan} \qquad YR = PX = 4$$

Segitiga $PRQ$ siku-siku di $R$ dengan sisi miring $PQ = 13$ dan sisi tegak

$$QR = QY - YR = 9 - 4 = 5$$

**Pythagoras.**

$$XY^2 = PR^2 = PQ^2 - QR^2 = 13^2 - 5^2 = 169 - 25 = 144$$

$$XY = \boxed{12}$$

**Periksa.** $(5, 12, 13)$ tripel Pythagoras ✓.

### Bentuk umumnya

$$XY = \sqrt{d^2 - (r_2 - r_1)^2}$$

dengan $d$ jarak kedua pusat. Yang muncul di dalam akar adalah **selisih** jari-jarinya, sebab
yang digeser tadi adalah selisih tingginya.

Untuk garis singgung persekutuan **dalam** — yang lewat di antara kedua lingkaran — bentuknya
berubah menjadi $\sqrt{d^2 - (r_1 + r_2)^2}$, dengan jumlah, bukan selisih. Pada soal ini
kedua lingkarannya bersinggungan sehingga $d = r_1 + r_2$ dan akarnya nol: memang hanya ada
satu garis singgung dalam, dan ia menyentuh keduanya di titik yang sama.

### Kaitan yang enak dicatat

Karena $d = r_1 + r_2$ pada singgungan luar,

$$XY = \sqrt{(r_1+r_2)^2 - (r_2-r_1)^2} = \sqrt{4 r_1 r_2} = 2\sqrt{r_1 r_2}$$

Periksa: $2\sqrt{4 \times 9} = 2 \times 6 = 12$ ✓.

Jadi untuk dua lingkaran yang bersinggungan luar dan menyinggung satu garis yang sama, panjang
ruas singgungnya adalah **dua kali rata-rata geometri jari-jarinya** — bentuk yang muncul lagi
di soal-soal rangkaian lingkaran yang saling menyinggung.

### Jangan tertukar antara kedua jenis singgungan

$$\text{singgung luar: } d = r_1 + r_2 = 13, \qquad \text{singgung dalam: } d = |r_1 - r_2| = 5$$

Gambar sering tidak langsung menunjukkan yang mana, dan memakai rumus yang salah di sini
mengubah $12$ menjadi bilangan khayal. Bacalah kata "dari luar" pada soal sebagai data, bukan
sebagai hiasan.
