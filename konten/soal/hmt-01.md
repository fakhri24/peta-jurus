---
id: hmt-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti, garis-singgung]
bentuk: isian
kesulitan: 4
jawaban: "12"
---

## Soal

Dua lingkaran berjari-jari $4$ dan $9$ bersinggungan dari luar. Sebuah garis menyinggung
keduanya, dengan kedua lingkaran berada di sisi yang sama dari garis itu.

Tentukan jarak antara kedua titik singgungnya.

## Petunjuk

- Bersinggungan dari luar berarti jarak kedua pusatnya sama dengan jumlah jari-jarinya.
- Kedua jari-jari ke titik singgungnya tegak lurus garis yang sama, jadi keduanya sejajar. Bangun apa yang terbentuk kalau salah satunya digeser?
- Turunkan tegak lurus dari pusat lingkaran kecil ke jari-jari lingkaran besar; terbentuk segitiga siku-siku dengan sisi miring $r_1+r_2$ dan satu kaki $r_2-r_1$.

## Pembahasan

**Hitung jarak kedua pusatnya.** Bersinggungan dari luar:

$$d = O_1O_2 = 4 + 9 = 13$$

**Bentuk segitiga siku-sikunya.** Misalkan garis singgungnya menyentuh lingkaran kecil di
$A$ dan lingkaran besar di $B$. Jari-jari $O_1A$ dan $O_2B$ keduanya tegak lurus garis yang
sama, jadi $O_1A \parallel O_2B$, dan $ABO_2O_1$ trapesium siku-siku.

Turunkan tegak lurus dari $O_1$ ke $O_2B$, mengenainya di $K$. Maka $O_1AB K$ persegi
panjang, sehingga

$$O_1K = AB, \qquad KB = O_1A = 4, \qquad O_2K = 9 - 4 = 5$$

**Pakai Pythagoras pada $\triangle O_1KO_2$**, yang siku-siku di $K$:

$$AB^2 = O_1K^2 = O_1O_2^2 - O_2K^2 = 13^2 - 5^2 = 169 - 25 = 144$$

$$AB = \boxed{12}$$

### Rumus umumnya

Perhitungan tadi berlaku untuk dua lingkaran mana pun yang berjarak pusat $d$:

$$\text{singgung persekutuan luar} = \sqrt{d^2 - \left(r_2 - r_1\right)^2}$$

$$\text{singgung persekutuan dalam} = \sqrt{d^2 - \left(r_2 + r_1\right)^2}$$

Untuk lingkaran yang bersinggungan luar, $d = r_1 + r_2$, sehingga bentuk pertamanya
menyusut jadi

$$\sqrt{\left(r_1+r_2\right)^2 - \left(r_2-r_1\right)^2} = \sqrt{4 r_1 r_2} = 2\sqrt{r_1 r_2}$$

Periksa: $2\sqrt{4 \times 9} = 2 \times 6 = 12$ ✓

Bentuk $2\sqrt{r_1r_2}$ itu layak dikenali — ia rata-rata geometri yang muncul di banyak
soal lingkaran bersinggungan.

Perhatikan pula bahwa singgung persekutuan **dalam** di sini panjangnya
$\sqrt{169 - 169} = 0$: memang, untuk lingkaran yang bersinggungan luar, kedua garis
singgung dalamnya menyatu menjadi satu garis di titik singgungnya.

### Di mana homotetinya

Garis singgung persekutuan luar itu melalui **pusat homoteti luar** kedua lingkaran. Alasannya
langsung: homoteti berpusat di sana memetakan lingkaran kecil ke lingkaran besar, dan garis
lewat pusat homoteti terpetakan ke dirinya sendiri — jadi kalau ia menyinggung yang satu, ia
menyinggung yang lain.

Periksa dengan angka: pusat homoteti luar $E$ memenuhi $\dfrac{EO_1}{EO_2} = \dfrac49$ dengan
$E$ di luar ruas $O_1O_2$, sehingga $EO_1 = \dfrac{13 \times 4}{9-4} = 10{,}4$. Titik itu
memang terletak pada garis singgungnya.

Itu sebabnya kedua garis singgung persekutuan luar berpotongan di satu titik, dan titik itu
punya nama.

### Kalau salah satu lingkaran lebih besar dari jaraknya

Rumus di atas hanya berlaku selama isi akarnya tak negatif. Untuk singgung persekutuan luar,
syaratnya $d \ge \left|r_2 - r_1\right|$ — yaitu lingkaran yang satu tidak berada seluruhnya
di dalam lingkaran yang lain.

Kalau $d = \left|r_2-r_1\right|$ (bersinggungan dalam), panjangnya nol dan kedua titik
singgungnya menyatu. Kalau $d < \left|r_2-r_1\right|$, tidak ada garis singgung persekutuan
sama sekali. Memeriksa syarat itu lebih dulu menghemat perhitungan yang akarnya negatif.
