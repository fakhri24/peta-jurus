---
id: kut-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik, garis-singgung]
bentuk: isian
kesulitan: 3
jawaban: "5"
---

## Soal

Dari titik $P$ di luar sebuah lingkaran ditarik garis singgung $PT$ dan sebuah garis potong
yang melalui pusat lingkaran, menembusnya di $A$ lalu di $B$ dengan $A$ lebih dekat ke $P$.
Diketahui $PT = 12$ dan $PA = 8$.

![Sebuah lingkaran berpusat O dengan titik P di luarnya, di sebelah kanan. Dari P ditarik garis singgung yang menyentuh lingkaran di titik T di kiri atas, dan jari-jari OT digambar putus-putus tegak lurus terhadap garis singgung itu. Dari P juga ditarik garis potong mendatar yang melewati pusat lingkaran, menembusnya di titik A yang lebih dekat ke P dan titik B di seberangnya, sehingga AB adalah garis tengah. Jarak dari P ke A adalah 8, dan panjang garis singgung PT adalah 12](singgung-garis-potong.svg)

Tentukan jari-jari lingkaran itu.

## Petunjuk

- Garis singgung dan garis potong dari satu titik luar terhubung oleh satu hubungan hasil kali.
- $PT^2 = PA \cdot PB$. Dari situ $PB$ bisa dihitung.
- Karena garis potongnya **melalui pusat**, ruas $AB$ punya nama khusus. Apa hubungannya dengan jari-jari?

## Pembahasan

**Pakai hubungan singgung–potong.**

$$PT^2 = PA \cdot PB$$

$$12^2 = 8 \cdot PB \quad \Longrightarrow \quad PB = \frac{144}{8} = 18$$

**Manfaatkan bahwa garis potongnya lewat pusat.** Karena $A$ dan $B$ ada pada satu garis
lurus lewat pusat, ruas $AB$ adalah **garis tengah**:

$$AB = PB - PA = 18 - 8 = 10 \quad \Longrightarrow \quad r = \frac{10}{2} = \boxed{5}$$

### Periksa lewat definisi kuasa titik

Jarak dari $P$ ke pusat: $OP = PA + r = 8 + 5 = 13$. Maka

$$k(P) = OP^2 - r^2 = 169 - 25 = 144 = PT^2 \quad ✓$$

Segitiga $OTP$ siku-siku di $T$ dengan sisi $5$, $12$, $13$ — tripel Pythagoras yang
terkenal. Ia muncul di sini bukan kebetulan: angkanya memang disusun dari tripel itu, dan
mengenalinya adalah cara tercepat memeriksa seluruh soal dalam satu tarikan napas.

### Kenapa $PT^2 = PA \cdot PB$

Sudut $\angle PTA$ antara garis singgung $PT$ dan talibusur $TA$ sama besar dengan sudut
keliling $\angle TBA$ yang menghadap busur $TA$ di seberangnya — itu sudut antara tali busur
dan garis singgung. Dengan sudut $\angle P$ yang dipakai bersama:

$$\triangle PTA \sim \triangle PBT$$

sehingga $\dfrac{PT}{PB} = \dfrac{PA}{PT}$, yaitu $PT^2 = PA \cdot PB$.

Perhatikan bahwa $T$ muncul di kedua segitiga pada posisi yang berbeda — sekali sebagai
titik kedua, sekali sebagai titik ketiga. Itu ciri khas kesebangunan yang melahirkan kuadrat.

### Kaitan dengan dua garis singgung yang sama panjang

Kalau dari $P$ ditarik garis singgung kedua, menyentuh di $T'$, maka $PT'^2$ juga sama dengan
$PA \cdot PB$ — hasil kali yang sama, karena garis potongnya sama. Maka

$$PT'^2 = PT^2 \quad \Longrightarrow \quad PT' = PT$$

Jadi sifat "dua garis singgung dari satu titik sama panjang" adalah akibat langsung dari
kuasa titik, bukan fakta terpisah yang perlu dihafal sendiri.

### Kalau garis potongnya tidak lewat pusat

Hubungan $PT^2 = PA \cdot PB$ tetap berlaku — ia tidak peduli garis potongnya lewat pusat
atau tidak. Yang gugur hanya langkah terakhir: $AB$ tidak lagi garis tengah, sehingga
jari-jarinya tidak bisa dibaca dari $AB$.

Jadi keterangan "melalui pusat" di soal ini justru bekerja pada langkah yang **bukan** kuasa
titik. Membaca keterangan soal sebagai "yang mana dipakai untuk apa" sering lebih berguna
daripada membacanya sekaligus.
