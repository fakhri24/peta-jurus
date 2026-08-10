---
id: tis-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "4"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 13$, $BC = 14$, dan $CA = 15$.

Tentukan jari-jari lingkaran dalam segitiga itu.

## Petunjuk

- Lingkaran dalam berpusat di titik yang berjarak sama ke ketiga **sisi**, dan jarak itulah jari-jarinya.
- Jari-jari lingkaran dalam terhubung dengan luas dan keliling: $r = \dfrac{L}{s}$ dengan $s$ setengah keliling.
- Hitung $s$ lebih dulu, lalu $L$ dengan rumus Heron.

## Pembahasan

**Hitung setengah kelilingnya.**

$$s = \frac{13 + 14 + 15}{2} = 21$$

**Hitung luasnya dengan Heron.**

$$L = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{21 \cdot 7 \cdot 6 \cdot 8}$$

dengan $a = BC = 14$, $b = CA = 15$, $c = AB = 13$, sehingga $s-a = 7$, $s-b = 6$, $s-c = 8$.

$$L = \sqrt{21 \cdot 336} = \sqrt{7056} = 84$$

**Pakai $r = \dfrac{L}{s}$.**

$$r = \frac{84}{21} = \boxed{4}$$

### Dari mana rumus $r = \dfrac{L}{s}$

Hubungkan pusat lingkaran dalam $I$ dengan ketiga titik sudut. Segitiga $ABC$ terpecah
menjadi tiga segitiga: $IBC$, $ICA$, $IAB$. Tinggi ketiganya, diukur dari $I$ ke sisi yang
menjadi alasnya, sama-sama $r$ — sebab $I$ berjarak sama ke ketiga sisi:

$$L = \tfrac12 a r + \tfrac12 b r + \tfrac12 c r = \tfrac12 r (a+b+c) = rs$$

Jadi rumusnya bukan hafalan terpisah, melainkan luas yang dihitung dengan cara memecahnya.

### Periksa lewat tinggi segitiganya

Luas $84$ bisa diuji ulang tanpa Heron. Kaki garis tinggi dari $A$ ke $BC$ membagi $BC$
menjadi $x$ dan $14 - x$ dengan

$$13^2 - x^2 = 15^2 - (14-x)^2$$

$$169 - x^2 = 225 - 196 + 28x - x^2 \quad \Longrightarrow \quad 28x = 140 \quad \Longrightarrow \quad x = 5$$

Tingginya $\sqrt{169 - 25} = 12$, sehingga $L = \tfrac12 \cdot 14 \cdot 12 = 84$ ✓

Segitiga $13$-$14$-$15$ memang terkenal karena tingginya bulat: ia dua segitiga siku-siku
$5$-$12$-$13$ dan $9$-$12$-$15$ yang direkatkan pada sisi $12$.

### Sekalian: jari-jari lingkaran luar

$$R = \frac{abc}{4L} = \frac{13 \cdot 14 \cdot 15}{4 \cdot 84} = \frac{2730}{336} = \frac{65}{8} = 8{,}125$$

Perhatikan bahwa $R > r$, dan memang harus — lingkaran luar melalui ketiga titik sudut,
lingkaran dalam menyinggung ketiga sisi dari dalam.

Lebih tepat lagi, **ketaksamaan Euler** menjamin $R \ge 2r$ untuk setiap segitiga, dengan
kesamaan hanya pada segitiga sama sisi. Di sini $8{,}125 \ge 8$ ✓ — nyaris kesamaan, dan itu
masuk akal sebab $13$, $14$, $15$ hampir sama panjang.

### Panjang dari titik sudut ke titik singgung

Sebagai bonus yang sering ditanyakan di soal berikutnya: kalau lingkaran dalam menyinggung
$BC$ di $X$, $CA$ di $Y$, dan $AB$ di $Z$, maka

$$AY = AZ = s-a = 7, \qquad BZ = BX = s-b = 6, \qquad CX = CY = s-c = 8$$

Periksa: $BX + XC = 6 + 8 = 14 = BC$ ✓, $AZ + ZB = 7 + 6 = 13 = AB$ ✓,
$AY + YC = 7 + 8 = 15 = CA$ ✓

Angka $7$, $6$, $8$ itu persis yang sudah muncul di dalam akar Heron tadi. Bukan kebetulan:
rumus Heron dan panjang titik singgung sama-sama tersusun dari $s-a$, $s-b$, $s-c$.

### Jangan tertukar dengan pusat lingkaran luar

Kekeliruan paling sering di seluruh jurus ini: mengira titik yang berjarak sama ke ketiga
**titik sudut** adalah pusat lingkaran dalam. Bukan — itu pusat lingkaran **luar**.

| | Perpotongan | Berjarak sama ke |
|---|---|---|
| Pusat dalam $I$ | ketiga garis bagi | ketiga **sisi** |
| Pusat luar $O$ | ketiga garis sumbu | ketiga **titik sudut** |

Cara mengingat: garis bagi soal **sudut**, dan titik pada garis bagi berjarak sama ke kedua
sisi yang mengapitnya. Garis sumbu soal **ruas**, dan titik pada sumbu ruas berjarak sama ke
kedua ujungnya.
