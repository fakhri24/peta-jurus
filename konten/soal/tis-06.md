---
id: tis-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa, luas-bidang]
bentuk: uraian
kesulitan: 3
---

## Soal

Lingkaran dalam segitiga $ABC$ berpusat di $I$, berjari-jari $r$, dan menyinggung sisi $BC$
di $X$, sisi $CA$ di $Y$, serta sisi $AB$ di $Z$. Tulis $L$ untuk luas segitiga dan
$s = \tfrac{a+b+c}{2}$ untuk setengah kelilingnya.

![Segitiga ABC dengan lingkaran dalam berpusat I, menyinggung sisi BC di X, sisi CA di Y, dan sisi AB di Z](segitiga-lingkaran-dalam.svg)

**(a)** Buktikan bahwa $L = rs$.

**(b)** Buktikan bahwa $AY = AZ = s - a$.

## Petunjuk

- Untuk (a), hubungkan $I$ dengan ketiga titik sudut. Segitiga $ABC$ terpecah jadi tiga segitiga — apa yang sama pada ketiganya?
- Untuk (b), mulailah dari sifat yang sudah kamu punya: dua garis singgung dari satu titik sama panjang. Sebut ketiga panjang itu $x$, $y$, $z$.
- Ketiga persamaan $y+z = a$, $z+x = b$, $x+y = c$ punya jumlah yang mudah, dan dari jumlah itu tiap peubahnya bisa dikeluarkan.

## Pembahasan

### Bagian (a)

**Pecah segitiganya dari $I$.** Tarik $IA$, $IB$, dan $IC$. Segitiga $ABC$ terpecah menjadi
tiga segitiga yang tidak bertumpang tindih:

$$L = [IBC] + [ICA] + [IAB]$$

**Tinggi ketiganya sama.** Ambil $BC$, $CA$, $AB$ sebagai alas ketiganya. Tinggi tiap segitiga
adalah jarak dari $I$ ke alasnya — dan jarak itu tepat $r$ untuk ketiganya, sebab $I$ berjarak
sama ke ketiga sisi dan jarak itulah jari-jari lingkaran dalamnya.

$$[IBC] = \tfrac12 a r, \qquad [ICA] = \tfrac12 b r, \qquad [IAB] = \tfrac12 c r$$

**Jumlahkan.**

$$L = \tfrac12 r (a + b + c) = \tfrac12 r \cdot 2s = rs \qquad \blacksquare$$

### Bagian (b)

**Pakai sifat dua garis singgung dari satu titik.** Dari $A$ ditarik dua garis singgung ke
lingkaran dalam, menyentuh di $Y$ dan $Z$, sehingga $AY = AZ$. Sebut panjangnya $x$. Dengan
cara yang sama dari $B$ dan dari $C$:

$$AY = AZ = x, \qquad BZ = BX = y, \qquad CX = CY = z$$

**Tulis ketiga sisinya.** Tiap sisi terbagi oleh titik singgungnya menjadi dua bagian:

$$a = BC = BX + XC = y + z$$

$$b = CA = CY + YA = z + x$$

$$c = AB = AZ + ZB = x + y$$

**Jumlahkan ketiganya.**

$$a + b + c = 2(x+y+z) \quad \Longrightarrow \quad x + y + z = \frac{a+b+c}{2} = s$$

**Kurangkan.** Karena $y + z = a$:

$$x = (x+y+z) - (y+z) = s - a$$

Jadi $AY = AZ = s - a$ $\blacksquare$

Dengan cara yang sama $y = s-b$ dan $z = s-c$.

### Kenapa dua garis singgung dari satu titik sama panjang

Langkah itu dipakai sebagai modal di bagian (b), jadi alasannya patut disebut. Segitiga
$AYI$ dan $AZI$ siku-siku di $Y$ dan $Z$ (jari-jari tegak lurus garis singgung), keduanya
punya sisi miring $AI$ yang sama, dan $IY = IZ = r$. Menurut kekongruenan sisi
miring–sisi siku, $\triangle AYI \cong \triangle AZI$, sehingga $AY = AZ$.

Alternatifnya lewat kuasa titik: kuasa $A$ terhadap lingkaran dalam bernilai $AY^2$ dan juga
$AZ^2$, jadi keduanya sama.

### Periksa pada segitiga 13-14-15

Dengan $a = 14$, $b = 15$, $c = 13$, berlaku $s = 21$ dan $L = 84$.

**(a)** $r = \dfrac{L}{s} = \dfrac{84}{21} = 4$ ✓

**(b)** $x = s-a = 7$, $y = s-b = 6$, $z = s-c = 8$. Periksa: $y+z = 14 = a$ ✓,
$z+x = 15 = b$ ✓, $x+y = 13 = c$ ✓

Ketiga persamaan cocok sekaligus, jadi hasilnya bisa dipercaya.

### Apa yang dibuka kedua hasil ini

Keduanya jarang jadi jawaban akhir, tetapi hampir selalu jadi langkah tengah:

- $L = rs$ menghubungkan **luas** dengan **keliling** — satu-satunya jembatan langsung di
  antara keduanya, dan asal semua rumus jari-jari lingkaran dalam;
- $AY = s-a$ mengubah titik singgung dari "titik yang letaknya tidak diketahui" menjadi
  panjang yang bisa dihitung dari ketiga sisi saja.

Yang kedua sering menjadi kunci pada soal yang menyebut titik singgung lingkaran dalam: begitu
$s-a$, $s-b$, $s-c$ ditulis, soalnya sering berubah jadi soal aljabar biasa.

Sebagai contoh cepat: untuk segitiga siku-siku dengan sisi miring $c$, titik singgung pada
kedua kaki berjarak $s-c$ dari titik sudut siku-sikunya, dan di situ terbentuk persegi
bersisi $r$ — sehingga $r = s - c = \dfrac{a+b-c}{2}$ tanpa menghitung luas sama sekali.

## Rubrik

- **(a)** Menghubungkan $I$ dengan ketiga titik sudut dan menyatakan $L$ sebagai jumlah tiga
  luas
- **(a)** Menyebut bahwa tinggi ketiganya sama dengan $r$, **dengan alasan** $I$ berjarak
  sama ke ketiga sisi
- **(a)** Menjumlahkan dan menyimpulkan $L = rs$
- **(b)** Menyatakan $AY = AZ$, $BZ = BX$, $CX = CY$ beserta alasannya
- **(b)** Menuliskan ketiga sisi sebagai jumlah dua panjang singgung
- **(b)** Menjumlahkan ketiganya untuk memperoleh $x+y+z = s$
- **(b)** Mengurangkan untuk memperoleh $x = s-a$, dan menyimpulkan $AY = AZ = s-a$

Bukti (a) yang tidak menyebut alasan tingginya sama dengan $r$ dinilai tidak lengkap: di
situlah sifat pusat lingkaran dalam dipakai, dan tanpa itu langkahnya berlaku untuk sembarang
titik di dalam segitiga — yang jelas salah.
