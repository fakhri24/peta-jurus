---
id: gsg-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung]
bentuk: isian
kesulitan: 3
jawaban: "2"
---

## Soal

Segitiga $ABC$ siku-siku di $C$, dengan $AC = 6$ dan $BC = 8$.

Tentukan jari-jari lingkaran dalam segitiga itu.

## Petunjuk

- Perhatikan titik siku-sikunya. Lingkaran dalam menyinggung kedua sisi yang bertemu di sana, dan kedua jari-jari ke titik singgungnya tegak lurus sisi-sisi itu.
- Bangun yang dibentuk pusat lingkaran, titik $C$, dan kedua titik singgung di sisi $CA$ dan $CB$ adalah **persegi** bersisi $r$.
- Panjang singgung dari $C$ karena itu sama dengan $r$ sendiri, dan panjang singgung dari $C$ adalah $s - c$.

## Pembahasan

**Cari sisi miringnya.**

$$AB = \sqrt{6^2 + 8^2} = \sqrt{100} = 10$$

**Perhatikan apa yang khusus di titik siku-siku.** Sebut $I$ pusat lingkaran dalam, dan sebut
titik singgung pada $CA$ dan $CB$ berturut-turut $Y$ dan $X$. Maka $IY \perp CA$ dan
$IX \perp CB$, sedangkan $CA \perp CB$ menurut soal.

Segiempat $CXIY$ karena itu punya **tiga** sudut siku-siku, sehingga yang keempat juga
siku-siku — dan karena $IX = IY = r$, bangunnya adalah **persegi** bersisi $r$. Akibatnya

$$CX = CY = r$$

**Pakai rumus panjang singgung.** Panjang singgung dari $C$ adalah $s - c$ dengan
$c = AB = 10$ dan

$$s = \frac{6 + 8 + 10}{2} = 12$$

sehingga

$$r = CX = s - c = 12 - 10 = \boxed{2}$$

**Periksa lewat $L = rs$.** Luas segitiga siku-siku ini $\tfrac{1}{2} \times 6 \times 8 = 24$,
sehingga

$$r = \frac{L}{s} = \frac{24}{12} = 2 \quad ✓$$

Dua jalan berbeda, angka yang sama.

### Rumus khusus segitiga siku-siku

Dari $r = s - c$ dengan $s = \dfrac{a+b+c}{2}$:

$$r = \frac{a+b+c}{2} - c = \frac{a + b - c}{2}$$

Untuk soal ini: $\dfrac{6 + 8 - 10}{2} = 2$ ✓.

Bentuk ini **hanya** berlaku untuk segitiga siku-siku, dan alasannya persis persegi tadi:
sudut $90^\circ$ di $C$ yang membuat panjang singgung dari $C$ sama dengan $r$ sendiri. Pada
segitiga sembarang, panjang singgung dari sebuah titik sudut tidak ada hubungannya dengan $r$.

### Satu akibat yang enak

Untuk tripel Pythagoras bulat, $a + b - c$ selalu genap, sehingga $r$ selalu **bilangan bulat**.
Periksa pada beberapa tripel:

| Tripel | $a+b-c$ | $r$ |
|---|---|---|
| $(3,4,5)$ | $2$ | $1$ |
| $(6,8,10)$ | $4$ | $2$ |
| $(5,12,13)$ | $4$ | $2$ |
| $(8,15,17)$ | $6$ | $3$ |
| $(7,24,25)$ | $6$ | $3$ |

Pola ini kadang dipakai soal olimpiade dari arah sebaliknya: diberikan $r$ bulat, cari semua
segitiga siku-siku bersisi bulat yang memenuhinya.
