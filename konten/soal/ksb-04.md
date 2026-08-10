---
id: ksb-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [kesebangunan]
bentuk: isian
kesulitan: 3
jawaban: "15"
---

## Soal

Pada trapesium $ABCD$, sisi $AB$ sejajar sisi $DC$, dengan $AB = 15$ dan $DC = 10$. Kedua
diagonalnya berpotongan di titik $P$.

![Trapesium ABCD dengan sisi AB mendatar di bawah dan sisi DC mendatar di atas, keduanya sejajar dan AB lebih panjang daripada DC. Kedua diagonalnya, AC dan BD, digambar dan berpotongan di titik P](trapesium-diagonal.svg)

Jika panjang diagonal $AC = 25$, tentukan panjang $AP$.

## Petunjuk

- Perpotongan kedua diagonal membentuk dua segitiga yang saling bertolak belakang di $P$. Perhatikan alas keduanya.
- Segitiga $APB$ dan segitiga $CPD$ punya sudut bertolak belakang di $P$, ditambah sudut dalam berseberangan dari kesejajaran $AB$ dan $DC$.
- Nisbah kesebangunannya sama dengan nisbah kedua sisi sejajarnya, yaitu $15 : 10$.

## Pembahasan

**Temukan kedua segitiga sebangunnya.** Bandingkan $\triangle APB$ dan $\triangle CPD$:

1. $\angle APB = \angle CPD$ — sudut bertolak belakang di $P$;
2. $\angle PAB = \angle PCD$ — sudut dalam berseberangan, sebab $AB \parallel DC$ dipotong
   diagonal $AC$.

Dua pasang sudut sudah cukup:

$$\triangle APB \sim \triangle CPD \quad (\text{Sd-Sd})$$

**Nisbahnya datang dari sisi sejajarnya.** Pasangan yang bersesuaian adalah $AB$ dengan $CD$,
jadi

$$k = \frac{AB}{CD} = \frac{15}{10} = \frac{3}{2}$$

**Terapkan pada diagonal.** Ruas $AP$ bersesuaian dengan $CP$, sehingga

$$\frac{AP}{PC} = \frac{3}{2}$$

Karena $AP + PC = AC = 25$, diagonalnya terbagi menjadi $3 + 2 = 5$ bagian sama besar:

$$AP = \frac{3}{5} \times 25 = \boxed{15}$$

**Periksa.** $PC = 10$, dan $\dfrac{15}{10} = \dfrac{3}{2}$ ✓, serta $15 + 10 = 25$ ✓.

### Kedua diagonal terbagi dengan perbandingan yang sama

Alasan yang sama berlaku untuk diagonal $BD$: $\dfrac{BP}{PD} = \dfrac{3}{2}$ juga. Jadi titik
$P$ membagi **kedua** diagonal dengan perbandingan yang identik — dan perbandingan itu
ditentukan seluruhnya oleh kedua sisi sejajarnya, bukan oleh panjang diagonalnya.

Konsekuensi yang berguna: kamu bisa mengetahui $AP : PC$ tanpa mengetahui satu pun panjang
diagonal.

### Ruas mendatar yang lewat titik potong

Tarik lewat $P$ sebuah ruas sejajar $AB$, memotong kaki $AD$ di $M$ dan kaki $BC$ di $N$.
Dengan kesebangunan yang sama dapat ditunjukkan

$$MN = \frac{2 \times AB \times DC}{AB + DC} = \frac{2 \times 15 \times 10}{25} = 12$$

Bentuk itu disebut rata-rata harmonis kedua sisi sejajarnya. Perhatikan letaknya di antara
$10$ dan $15$, dan lebih dekat ke yang **kecil** — sifat yang selalu dimiliki rata-rata
harmonis, dan pemeriksaan kewajaran yang murah.

Bandingkan dengan ruas sejajar yang lewat titik tengah kaki-kakinya, yang panjangnya
$\dfrac{15 + 10}{2} = 12{,}5$. Keduanya ruas mendatar di dalam trapesium yang sama, tetapi
tingginya berbeda — dan panjangnya pun berbeda.
