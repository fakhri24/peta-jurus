---
id: ktg-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri]
bentuk: uraian
kesulitan: 5
---

## Soal

Misalkan $a$, $b$, $c$ panjang sisi sebuah segitiga, $R$ jari-jari lingkaran luarnya,
dan $r$ jari-jari lingkaran dalamnya.

**(a)** Buktikan bahwa

$$abc \ \ge\ (a+b-c)(b+c-a)(c+a-b)$$

dan tentukan kapan kesamaannya berlaku.

**(b)** Dengan memakai bagian (a), buktikan **ketaksamaan Euler**

$$R \ \ge\ 2r$$

## Petunjuk

- Pada bagian (a), ruas kanannya positif justru karena ketiganya sisi segitiga. Beri nama ketiga faktornya, dan lihat apa jadinya ruas kirinya.
- Setelah $a = y+z$, $b = z+x$, $c = x+y$, ketaksamaannya berbunyi $(y+z)(z+x)(x+y) \ge 8xyz$. Terapkan AM-GM pada tiap kurung.
- Untuk (b), tulis $r$ dan $R$ dengan luas: $r = \dfrac{L}{s}$ dan $R = \dfrac{abc}{4L}$, lalu pakai rumus Heron $L^2 = s(s-a)(s-b)(s-c)$.
- Perhatikan bahwa $2(s-a) = b+c-a$. Nisbah $\dfrac{R}{2r}$ akan menyusut menjadi persis pecahan pada bagian (a).

## Pembahasan

### Bagian (a)

**Substitusi Ravi.** Ketiga faktor di ruas kanan positif tepat karena $a$, $b$, $c$
sisi segitiga. Beri nama

$$x = \frac{b+c-a}{2}, \qquad y = \frac{c+a-b}{2}, \qquad z = \frac{a+b-c}{2}$$

Ketiganya positif, dan berlaku

$$a = y+z, \qquad b = z+x, \qquad c = x+y$$

Ketaksamaan yang diminta menjadi

$$(y+z)(z+x)(x+y) \ \ge\ (2z)(2x)(2y) = 8xyz$$

**AM-GM pada tiap kurung.** Untuk bilangan positif,

$$y + z \ \ge\ 2\sqrt{yz}, \qquad z + x \ \ge\ 2\sqrt{zx}, \qquad x + y \ \ge\ 2\sqrt{xy}$$

Ketiga ruasnya positif, jadi ketiganya boleh dikalikan:

$$(y+z)(z+x)(x+y) \ \ge\ 8\sqrt{yz}\sqrt{zx}\sqrt{xy} = 8\sqrt{x^2y^2z^2} = 8xyz$$

$\blacksquare$

**Syarat kesamaan.** Perkalian ketaksamaan berujung sama tepat ketika ketiganya
sekaligus menjadi kesamaan, yaitu $y = z$, $z = x$, dan $x = y$ — jadi $x = y = z$,
yang berarti

$$a = b = c$$

Kesamaannya berlaku tepat pada segitiga **sama sisi** ✓

### Bagian (b)

**Tulis keduanya dengan luas.** Dengan $s = \dfrac{a+b+c}{2}$ dan $L$ luas segitiganya,

$$r = \frac{L}{s}, \qquad R = \frac{abc}{4L}$$

Maka

$$\frac{R}{2r} = \frac{abc}{4L} \cdot \frac{s}{2L} = \frac{abc \cdot s}{8L^2}$$

**Masukkan Heron.** Dari $L^2 = s(s-a)(s-b)(s-c)$, faktor $s$ saling menghapus:

$$\frac{R}{2r} = \frac{abc \cdot s}{8\,s(s-a)(s-b)(s-c)} = \frac{abc}{8(s-a)(s-b)(s-c)}$$

**Kenali penyebutnya.** Perhatikan bahwa

$$2(s-a) = a+b+c-2a = b+c-a$$

dan senada untuk dua lainnya. Jadi

$$8(s-a)(s-b)(s-c) = (b+c-a)(c+a-b)(a+b-c)$$

sehingga

$$\frac{R}{2r} = \frac{abc}{(a+b-c)(b+c-a)(c+a-b)}$$

**Selesaikan dengan bagian (a).** Pembilangnya paling sedikit sama dengan penyebutnya,
dan penyebutnya positif, jadi pecahan itu paling sedikit $1$:

$$\frac{R}{2r} \ \ge\ 1 \quad \Longrightarrow \quad R \ \ge\ 2r \qquad \blacksquare$$

Kesamaannya, mengikuti bagian (a), berlaku tepat pada segitiga sama sisi — dan di sana
memang $R = 2r$: untuk sama sisi bersisi $s_0$ berlaku $R = \dfrac{s_0}{\sqrt3}$ dan
$r = \dfrac{s_0}{2\sqrt3}$ ✓

### Yang menarik dari (b)

Kedua ketaksamaan itu ternyata **pernyataan yang sama**, ditulis dengan dua kosakata
berbeda. Bukan "(a) menolong membuktikan (b)", melainkan

$$\frac{R}{2r} = \frac{abc}{(a+b-c)(b+c-a)(c+a-b)}$$

sebuah **kesamaan** — sehingga $R \ge 2r$ dan bagian (a) setara sepenuhnya, termasuk
syarat kesamaannya.

Itu pola yang sering muncul: sebuah ketaksamaan geometri yang terlihat rumit ternyata
ketaksamaan aljabar sederhana yang sedang menyamar. Pekerjaan yang sesungguhnya adalah
menemukan kesamaan yang menghubungkan keduanya — di sini, lewat luas.

### Periksa dengan angka

| Segitiga | $R$ | $r$ | $R/2r$ | $abc$ | $(a{+}b{-}c)(b{+}c{-}a)(c{+}a{-}b)$ |
|---|---|---|---|---|---|
| $1,1,1$ | $\tfrac{1}{\sqrt3}$ | $\tfrac{1}{2\sqrt3}$ | $1$ | $1$ | $1$ |
| $3,4,5$ | $2{,}5$ | $1$ | $1{,}25$ | $60$ | $2 \cdot 6 \cdot 4 = 48$ |
| $5,5,8$ | $\tfrac{25}{6}$ | $\tfrac{4}{3}$ | $1{,}5625$ | $200$ | $2 \cdot 8 \cdot 8 = 128$ |

Baris kedua diperiksa langsung: $\dfrac{60}{48} = 1{,}25 = \dfrac{R}{2r}$ ✓, dan baris
ketiga $\dfrac{200}{128} = 1{,}5625$ ✓ — kesamaannya berlaku, bukan cuma ketaksamaannya.

### Kekeliruan yang paling sering pada bagian (a)

Menerapkan AM-GM pada ketiga faktor ruas kanan sekaligus:

$$(a+b-c)(b+c-a)(c+a-b) \ \le\ \left(\frac{(a+b-c)+(b+c-a)+(c+a-b)}{3}\right)^3
= \left(\frac{a+b+c}{3}\right)^3$$

Itu benar, tetapi tidak menyelesaikan apa pun: yang harus dibandingkan dengan ruas kanan
adalah $abc$, dan $\left(\tfrac{a+b+c}{3}\right)^3 \ge abc$ — arahnya **terbalik** dari
yang dibutuhkan. Dua ketaksamaan yang arahnya berlawanan tidak bisa disambung.

Substitusi Ravi menghindari jebakan itu karena ia tidak menaksir kedua ruas secara
terpisah, melainkan mengubah keduanya menjadi bentuk yang bisa dibandingkan kurung demi
kurung.

## Rubrik

- **(a)** Menyatakan substitusi Ravi **beserta alasan $x,y,z > 0$** — yaitu bahwa itu
  persis syarat segitiganya
- **(a)** Menerapkan AM-GM pada masing-masing $y+z$, $z+x$, $x+y$
- **(a)** Menyebut bahwa ketiga ketaksamaan boleh dikalikan karena semua ruasnya positif
- **(a)** Menyimpulkan syarat kesamaan $x=y=z$, lalu menerjemahkannya kembali menjadi
  $a=b=c$
- **(b)** Menuliskan $r = L/s$ dan $R = abc/(4L)$, lalu membentuk nisbah $R/(2r)$
- **(b)** Memakai Heron untuk menghapus $L^2$
- **(b)** Mengenali $2(s-a) = b+c-a$ dan menyusun penyebutnya menjadi bentuk bagian (a)
- **(b)** Menutup dengan bagian (a) dan menyatakan syarat kesamaannya

Bukti (b) lewat rumus Euler $OI^2 = R^2 - 2Rr$ dinilai penuh, asalkan rumus itu
**diturunkan**, bukan dikutip begitu saja — sebab dari $OI^2 \ge 0$ ketaksamaannya
memang langsung keluar, dan seluruh isi soalnya justru pindah ke penurunan rumus itu.
