---
id: gsg-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [garis-singgung]
bentuk: uraian
kesulitan: 3
---

## Soal

Lingkaran dalam segitiga $ABC$ menyinggung sisi $BC$ di $X$, sisi $CA$ di $Y$, dan sisi $AB$
di $Z$. Tulis $a = BC$, $b = CA$, $c = AB$, dan $s = \dfrac{a+b+c}{2}$.

![Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung sisi BC di X, sisi CA di Y, dan sisi AB di Z. Jari-jari IX digambar putus-putus dan tegak lurus sisi BC](segitiga-lingkaran-dalam.svg)

Buktikan bahwa

$$AY = AZ = s - a$$

## Petunjuk

- Enam panjang muncul di gambar, tetapi tidak semuanya berbeda. Pasangan mana yang pasti sama panjang, dan mengapa?
- Dua garis singgung dari satu titik luar sama panjang, jadi cukup **tiga** peubah untuk keenam panjang itu.
- Tiap sisi segitiga terpecah menjadi dua peubah, jadi kamu punya tiga persamaan. Jumlahkan ketiganya.

## Pembahasan

**Kurangi enam panjang menjadi tiga peubah.** Dari tiap titik sudut ada dua garis singgung ke
lingkaran dalam, dan dua garis singgung dari satu titik luar sama panjang. Maka

$$AY = AZ, \qquad BZ = BX, \qquad CX = CY$$

Namai ketiganya:

$$x = AY = AZ, \qquad y = BZ = BX, \qquad z = CX = CY$$

**Susun tiga persamaan dari ketiga sisinya.** Tiap titik singgung terletak **di dalam** sisinya,
sehingga tiap sisi terbagi menjadi tepat dua potongan:

$$a = BC = BX + XC = y + z$$

$$b = CA = CY + YA = z + x$$

$$c = AB = AZ + ZB = x + y$$

**Jumlahkan ketiganya.**

$$a + b + c = 2(x + y + z) \quad \Longrightarrow \quad x + y + z = \frac{a+b+c}{2} = s$$

**Kurangkan yang tidak memuat $x$.**

$$x = (x + y + z) - (y + z) = s - a$$

Karena $x = AY = AZ$, maka $AY = AZ = s - a$. $\blacksquare$

### Dua yang lain, tanpa pekerjaan tambahan

Pengurangan yang sama dengan persamaan yang lain memberi

$$y = s - b, \qquad z = s - c$$

Perhatikan polanya: **tiap panjang singgung adalah $s$ dikurangi sisi di hadapan titik sudutnya.**
Panjang dari $A$ memakai $a = BC$, yaitu sisi yang tidak menyentuh $A$ sama sekali.

### Langkah yang paling sering dilewati

Bukti ini menganggap ketiga titik singgungnya berada **di dalam** sisinya, sehingga tiap sisi
benar-benar terbagi dua. Itu benar untuk lingkaran **dalam** pada segitiga mana pun — termasuk
yang tumpul — sebab pusatnya selalu di dalam segitiga.

Untuk lingkaran singgung **luar** hal itu tidak berlaku: titik singgungnya bisa jatuh di
perpanjangan sisi, sehingga "$a = y + z$" berubah menjadi selisih. Karena itu panjang
singgungnya pun berbeda — bentuknya menjadi $s$ sendiri, bukan $s - a$.

Setiap kali sebuah persamaan bertumpu pada "titik ini terletak di antara kedua titik itu",
sebutkan alasannya. Di situlah bukti geometri paling sering bocor.

### Kegunaannya

Ketiga bilangan $s-a$, $s-b$, $s-c$ muncul di banyak tempat sekaligus:

- panjang singgung dari ketiga titik sudut, seperti yang baru dibuktikan;
- di dalam rumus Heron, $L = \sqrt{s(s-a)(s-b)(s-c)}$;
- pada segitiga siku-siku di $C$, jari-jari lingkaran dalamnya tepat $s - c$.

Ketiganya juga persis peubah pengganti pada substitusi Ravi, yang akan kamu temui di jurus
ketaksamaan geometri: setiap segitiga bisa ditulis dengan $x$, $y$, $z$ positif sembarang — dan
alasan mengapa **positif sembarang** sudah cukup adalah bukti di atas, dibaca terbalik.

## Rubrik

- Menyebut sifat dua garis singgung dari satu titik luar sama panjang, dan memakainya untuk ketiga titik sudut
- Menamai ketiga panjang singgung dengan tiga peubah
- Menuliskan ketiga sisi sebagai jumlah dua peubah, dengan alasan titik singgungnya terletak di dalam sisinya
- Menjumlahkan ketiga persamaan dan menyimpulkan $x + y + z = s$
- Mengurangkan persamaan yang tepat untuk mendapat $x = s - a$, lalu menyimpulkan $AY = AZ = s-a$
