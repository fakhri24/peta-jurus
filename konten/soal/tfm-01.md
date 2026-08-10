---
id: tfm-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [transformasi]
bentuk: isian
kesulitan: 4
jawaban: "150"
---

## Soal

Titik $P$ terletak di dalam segitiga sama sisi $ABC$ dengan $PA = 3$, $PB = 4$, dan $PC = 5$.

![Segitiga sama sisi ABC dengan alas AB mendatar, A di kiri bawah, B di kanan bawah, dan C di puncak atas. Sebuah titik P berada di dalam segitiga, agak ke kanan bawah dekat sisi AB. Dari P ditarik ruas putus-putus ke ketiga titik sudut: PA panjangnya 3, PB panjangnya 4, dan PC panjangnya 5](sama-sisi-titik-dalam.svg)

Tentukan besar sudut $\angle APB$ dalam derajat.

## Petunjuk

- Ketiga panjangnya $3$, $4$, $5$ — bilangan yang biasanya muncul sebagai sisi segitiga siku-siku. Tetapi ketiganya sekarang tersebar dari satu titik, bukan membentuk segitiga.
- Bangunnya sama sisi, jadi memutar $60^\circ$ terhadap salah satu titik sudut memetakan sisi ke sisi. Coba putar $P$ terhadap $B$.
- Setelah $P$ diputar $60^\circ$ terhadap $B$ menjadi $P'$, periksa panjang $PP'$ dan $AP'$.

## Pembahasan

**Kenali pemicunya.** Ada bangun sama sisi, dan tiga panjang yang tersebar dari satu titik.
Memutar $60^\circ$ terhadap titik sudut adalah alat bakunya: putaran itu memetakan sisi ke
sisi, sehingga panjang yang tadinya berjauhan bisa dikumpulkan jadi satu segitiga.

**Putar $P$ terhadap $B$ sebesar $60^\circ$**, dengan arah yang memetakan $C$ ke $A$. Sebut
bayangan $P$ sebagai $P'$.

**Baca apa yang terjadi pada ketiga panjangnya.**

- $BP' = BP = 4$, sebab putaran menjaga jarak ke pusat putarannya;
- $\angle PBP' = 60^\circ$ menurut definisi putarannya, dan bersama $BP = BP'$ itu membuat
  $\triangle BPP'$ **sama sisi**, sehingga $PP' = 4$;
- $AP' = CP = 5$, sebab putaran memetakan ruas $CP$ ke ruas $AP'$.

**Kumpulkan jadi satu segitiga.** Sekarang $\triangle APP'$ punya sisi

$$AP = 3, \qquad PP' = 4, \qquad AP' = 5$$

Karena $3^2 + 4^2 = 5^2$, segitiga itu siku-siku, dengan sudut siku-sikunya di hadapan sisi
$5$ — yaitu **di $P$**:

$$\angle APP' = 90^\circ$$

**Rakit sudut yang ditanya.** Sudut $\angle BPP' = 60^\circ$ karena $\triangle BPP'$ sama
sisi. Karena $B$ dan $A$ berada di sisi yang berlawanan dari garis $PP'$ pada gambar ini,
kedua sudutnya berjumlah:

$$\angle APB = \angle APP' + \angle P'PB = 90^\circ + 60^\circ = \boxed{150^\circ}$$

### Periksa dengan aturan kosinus

Sisi segitiga sama sisinya bisa dihitung dari $\triangle APB$:

$$AB^2 = 3^2 + 4^2 - 2 \cdot 3 \cdot 4 \cos 150^\circ = 25 + 24 \cdot \frac{\sqrt3}{2}
= 25 + 12\sqrt3$$

Jadi $AB = \sqrt{25+12\sqrt3} \approx 6{,}766$. Periksa apakah $P$ dengan jarak $3$, $4$, $5$
memang muat di dalam segitiga sama sisi sebesar itu: dengan $A(0,0)$ dan $B(6{,}766, 0)$,
absis $P$ adalah

$$x = \frac{9 - 16 + 45{,}785}{2 \cdot 6{,}766} = 2{,}866, \qquad
y = \sqrt{9 - 2{,}866^2} = 0{,}887$$

dan jarak dari $P(2{,}866,\ 0{,}887)$ ke $C(3{,}383,\ 5{,}860)$ adalah $5{,}000$ ✓

Ketiga jarak cocok sekaligus, jadi $150^\circ$ benar.

### Kenapa harus diputar terhadap $B$

Sudut yang ditanya $\angle APB$, jadi $C$ adalah titik sudut yang "tidak dipakai" — dan
justru panjang $PC$ yang harus dipindahkan supaya ikut berguna. Putaran terhadap $B$ (atau
terhadap $A$) memindahkan $PC$ ke tempat yang menyentuh $A$ dan $P$.

Kalau diputar terhadap $C$, yang berpindah justru $PA$ atau $PB$, dan sudut yang terakit
bukan $\angle APB$. Aturannya: **putar terhadap titik sudut yang sudutnya ditanyakan.**

### Arah putarannya harus dicoba

Memutar $60^\circ$ searah dan berlawanan jarum jam memberi hasil yang berbeda. Arah yang
salah memetakan $C$ ke titik di luar segitiga, dan $AP'$ tidak lagi sama dengan $CP$ —
perhitungannya tetap jalan, tetapi tidak menjawab apa pun.

Tanda bahwa arahnya benar: **$AP'$ keluar sama dengan salah satu panjang yang diketahui.**
Kalau tidak, balik arahnya.

### Pola yang sama pada persegi

Untuk bangun persegi, sudut putarnya $90^\circ$, dan segitiga $BPP'$ menjadi siku-siku sama
kaki dengan $PP' = BP\sqrt2$ serta $\angle BPP' = 45^\circ$. Selebihnya sama persis. Kenali
polanya, bukan angkanya:

| Bangun | Sudut putar | $PP'$ | $\angle BPP'$ |
|---|---|---|---|
| Segitiga sama sisi | $60^\circ$ | $BP$ | $60^\circ$ |
| Persegi | $90^\circ$ | $BP\sqrt2$ | $45^\circ$ |
