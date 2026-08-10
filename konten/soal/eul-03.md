---
id: eul-03
sumber: Latihan 3 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler]
bentuk: isian
kesulitan: 4
jawaban: "10"
---

## Soal

Pada segitiga $ABC$, jari-jari lingkaran luarnya $10$ dan titik $H$ adalah titik tingginya.
Titik $M$ adalah titik tengah $BC$, dan titik $K$ adalah titik tengah ruas $AH$.

![Segitiga ABC lancip dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas. Ketiga garis tingginya digambar putus-putus dan bertemu di titik tinggi H di dalam segitiga. Sebuah lingkaran digambar melalui sembilan titik sekaligus: ketiga titik tengah sisi, ketiga kaki garis tinggi, dan ketiga titik tengah ruas dari H ke tiap titik sudut. Pusatnya N, dan jari-jarinya setengah jari-jari lingkaran luar segitiga. Tiga di antara kesembilan titik itu diberi nama sebagai wakil tiap keluarga: M titik tengah BC, D kaki garis tinggi dari A, dan K titik tengah ruas AH](lingkaran-sembilan-titik.svg)

Tentukan panjang $MK$.

## Petunjuk

- Soal tidak menyebutkan bentuk segitiganya sama sekali, hanya $R$. Jadi jawabannya tidak boleh bergantung pada bentuknya.
- Titik tengah sisi dan titik tengah ruas dari $H$ ke titik sudut sama-sama termasuk **sembilan titik**. Keduanya ada pada satu lingkaran berjari-jari $\tfrac{R}{2}$.
- Tunjukkan bahwa $M$ dan $K$ **berseberangan** pada lingkaran itu, yaitu $MK$ garis tengahnya.

## Pembahasan

**Kenali keduanya sebagai anggota sembilan titik.** Titik $M$ adalah titik tengah sisi $BC$,
dan $K$ titik tengah ruas $AH$. Keduanya termasuk kesembilan titik, jadi keduanya berada pada
lingkaran sembilan titik yang berpusat $N$ berjari-jari

$$r_N = \frac{R}{2} = 5$$

**Tunjukkan keduanya berseberangan.** Pakai vektor dengan $O$ sebagai titik asal, dan modal
tunggal $\overrightarrow{OH} = \overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}$.

$$\overrightarrow{OM} = \tfrac12\left(\overrightarrow{OB}+\overrightarrow{OC}\right), \qquad
\overrightarrow{OK} = \tfrac12\left(\overrightarrow{OA}+\overrightarrow{OH}\right)$$

Titik tengah $MK$:

$$\tfrac12\left(\overrightarrow{OM}+\overrightarrow{OK}\right)
= \tfrac14\left(\overrightarrow{OB}+\overrightarrow{OC}+\overrightarrow{OA}+\overrightarrow{OH}\right)
= \tfrac14\left(\overrightarrow{OH}+\overrightarrow{OH}\right)
= \tfrac12\,\overrightarrow{OH}$$

Itu tak lain $N$, titik tengah $OH$. Jadi $N$ adalah titik tengah $MK$, sehingga $MK$ **garis
tengah** lingkaran sembilan titik.

**Selesaikan.**

$$MK = 2 r_N = 2 \times 5 = \boxed{10}$$

Perhatikan hasilnya: $MK = R$, berapa pun bentuk segitiganya.

### Periksa dengan segitiga yang bisa dihitung

Ambil lingkaran luar berjari-jari $10$ berpusat di titik asal, dengan

$$A(0, 10), \qquad B(-8, -6), \qquad C(6, -8)$$

Ketiganya berjarak $10$ dari pusat ✓. Maka $H = A+B+C = (-2, -4)$, dan

$$M = \left(\tfrac{-8+6}{2},\ \tfrac{-6-8}{2}\right) = (-1, -7), \qquad
K = \left(\tfrac{0-2}{2},\ \tfrac{10-4}{2}\right) = (-1, 3)$$

$$MK = \sqrt{0 + 10^2} = 10 \quad ✓$$

Sekalian, $N = \tfrac12 H = (-1,-2)$, dan jaraknya ke $M$ maupun ke $K$ sama-sama $5$ ✓ —
$N$ memang titik tengahnya.

### Kenapa soalnya tidak menyebut bentuk segitiganya

Karena jawabannya memang tidak bergantung padanya. Itu sendiri petunjuk: **kalau soal
memberi satu besaran saja dan menanyakan panjang, besaran yang ditanyakan pasti hanya
bergantung pada yang diberikan.**

Membaca kekurangan keterangan sebagai petunjuk — bukan sebagai soal yang tidak lengkap —
adalah kebiasaan yang sering menghemat setengah pekerjaan.

### Pasangan berseberangan yang lain

Perhitungan tadi tidak memakai apa pun yang khas $A$, jadi hal yang sama berlaku untuk kedua
pasangan lainnya. Pada lingkaran sembilan titik, tiga pasang berikut selalu berseberangan:

| Titik tengah sisi | berseberangan dengan | titik tengah ruas dari $H$ |
|---|---|---|
| titik tengah $BC$ | ↔ | titik tengah $AH$ |
| titik tengah $CA$ | ↔ | titik tengah $BH$ |
| titik tengah $AB$ | ↔ | titik tengah $CH$ |

Ketiga garis tengah itu berpotongan di $N$, dan masing-masing panjangnya $R$.

### Yang menyusul dari sini

Karena $MK$ garis tengah, setiap titik pada lingkaran sembilan titik memandang $MK$ dengan
sudut $90^\circ$. Kaki garis tinggi dari $A$ — sebut $D$ — memenuhi $\angle MDK = 90^\circ$
sebab $D$ ada pada $BC$ (garis $M$) dan pada $AH$ (garis $K$), dan keduanya tegak lurus.

Jadi $D$ **wajib** berada pada lingkaran itu. Itulah cara termurah membuktikan bahwa ketiga
kaki garis tinggi ikut termasuk sembilan titik — dan langkah itu memakai persis hasil yang
baru saja diperoleh.
