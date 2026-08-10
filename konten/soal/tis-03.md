---
id: tis-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa]
bentuk: isian
kesulitan: 4
jawaban: "5"
---

## Soal

Segitiga $ABC$ siku-siku di $A$ dengan $AB = 6$ dan $AC = 8$. Titik $I$ adalah pusat
lingkaran dalamnya dan $O$ pusat lingkaran luarnya.

![Segitiga ABC siku-siku di A, dengan A di kiri bawah, B di kanan pada garis mendatar, dan C di atas A pada garis tegak. Sisi AB panjangnya 6, sisi AC panjangnya 8, dan sisi miring BC panjangnya 10. Lingkaran dalam berpusat I menyinggung ketiga sisinya dari dalam. Lingkaran luar berpusat O melalui ketiga titik sudutnya, dan O terletak tepat di titik tengah sisi miring BC. Ruas putus-putus menghubungkan I dengan O](siku-siku-dalam-luar.svg)

Tentukan nilai $OI^2$.

## Petunjuk

- Kedua titiknya punya letak yang bisa ditulis eksplisit pada segitiga siku-siku. Di mana $O$ berada?
- Pada segitiga siku-siku, $O$ adalah titik tengah sisi miring. Untuk $I$, pakai bahwa jaraknya ke kedua kaki sama-sama $r$.
- Taruh $A$ di titik asal dengan kedua kakinya pada sumbu, lalu tulis koordinat $I$ dan $O$.

## Pembahasan

**Letakkan sumbunya.** Ambil $A(0,0)$, $B(6,0)$, $C(0,8)$. Maka $BC = \sqrt{36+64} = 10$.

**Cari $O$.** Pada segitiga siku-siku, sudut siku-sikunya adalah sudut keliling yang menghadap
sisi miring, jadi sisi miring adalah **garis tengah** lingkaran luarnya. Karena itu

$$O = \text{titik tengah } BC = (3, 4), \qquad R = 5$$

**Cari $I$.** Jarak $I$ ke kedua kaki sama-sama $r$, dan kedua kaki itu berimpit sumbu, jadi

$$I = (r, r)$$

Hitung $r$ dengan $r = \dfrac{L}{s}$:

$$L = \tfrac12 \cdot 6 \cdot 8 = 24, \qquad s = \frac{6+8+10}{2} = 12, \qquad r = \frac{24}{12} = 2$$

Jadi $I = (2, 2)$.

**Hitung.**

$$OI^2 = (3-2)^2 + (4-2)^2 = 1 + 4 = \boxed{5}$$

### Periksa dengan rumus Euler

Untuk **setiap** segitiga berlaku hubungan Euler antara kedua pusat itu:

$$OI^2 = R^2 - 2Rr = R(R - 2r)$$

Di sini $R = 5$ dan $r = 2$:

$$OI^2 = 25 - 2 \cdot 5 \cdot 2 = 25 - 20 = 5 \quad ✓$$

Dua jalan yang sepenuhnya berbeda — satu koordinat, satu rumus umum — memberi angka yang
sama.

Rumus Euler sekaligus membuktikan **ketaksamaan Euler**: karena $OI^2 \ge 0$, berlaku
$R \ge 2r$ untuk setiap segitiga, dengan kesamaan tepat ketika $O = I$, yaitu pada segitiga
sama sisi. Di sini $5 > 4$ ✓.

### Pintasan untuk $r$ pada segitiga siku-siku

Untuk segitiga siku-siku dengan kaki $a$, $b$ dan sisi miring $c$:

$$r = \frac{a + b - c}{2}$$

Di sini $\dfrac{6+8-10}{2} = 2$ ✓, tanpa menghitung luas maupun setengah keliling.

Alasannya lewat panjang titik singgung: jarak dari titik sudut siku-siku ke titik singgung
pada kedua kakinya sama-sama $r$ (karena di situ terbentuk persegi bersisi $r$), sedangkan
menurut rumus umum jarak itu $s - c$. Jadi $r = s - c = \dfrac{a+b+c}{2} - c = \dfrac{a+b-c}{2}$.

### Jebakan: menaruh $I$ di titik tengah, atau $O$ di dalam

Dua kekeliruan yang berpasangan:

- **$O$ dikira di dalam segitiga di "tengah-tengah".** Pada segitiga siku-siku ia justru di
  tepi, tepat di titik tengah sisi miring. Pada segitiga tumpul ia bahkan di luar.
- **$I$ dikira di titik potong garis berat.** Itu titik berat $G$, bukan $I$. Di sini
  $G = \left(\tfrac{0+6+0}{3}, \tfrac{0+0+8}{3}\right) = (2,\ 2{,}67)$ — dekat dengan $I(2,2)$
  tetapi berbeda, dan kedekatan itu justru yang membuat kekeliruannya sulit ketahuan dari
  gambar.

Ciri yang menentukan tetap sama: $I$ berjarak sama ke ketiga **sisi**, $O$ berjarak sama ke
ketiga **titik sudut**, $G$ rata-rata ketiga titik sudut.

### Kalau segitiganya bukan siku-siku

Cara koordinat tetap bisa dipakai, tetapi $O$ tidak lagi terbaca langsung dan harus dicari
sebagai perpotongan dua garis sumbu. Di situ rumus Euler jauh lebih murah: hitung $R$ dan
$r$ dengan $\dfrac{abc}{4L}$ dan $\dfrac{L}{s}$, lalu masukkan.

Contohnya pada segitiga $13$-$14$-$15$: $R = \tfrac{65}{8}$, $r = 4$, sehingga
$OI^2 = \tfrac{65}{8}\left(\tfrac{65}{8} - 8\right) = \tfrac{65}{64}$ — dihitung tanpa
menggambar apa pun.
