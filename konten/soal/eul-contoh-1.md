---
id: eul-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler]
bentuk: isian
kesulitan: 4
jawaban: "8"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 15$, $BC = 7$, dan $CA = 13$. Titik $O$ adalah pusat
lingkaran luarnya dan $H$ titik tingginya.

![Segitiga ABC yang ketiga sisinya berbeda panjang, dengan alas BC mendatar, B di kiri bawah, C di kanan bawah, dan puncak A di atas agak ke kiri. Di dalamnya digambar sebuah garis lurus yang melalui empat titik sekaligus: titik tinggi H, pusat lingkaran sembilan titik N, titik berat G, dan pusat lingkaran luar O, terurut demikian sepanjang garis itu. Jarak dari H ke G tepat dua kali jarak dari G ke O, dan N tepat di tengah antara H dan O. Garis itu disebut garis Euler](segitiga-garis-euler.svg)

Tentukan panjang $OH$.

## Petunjuk

- Jarak antara kedua titik itu tidak perlu dicari lewat koordinat: ada rumus yang menyatakannya hanya dengan $R$ dan ketiga sisinya.
- $OH^2 = 9R^2 - \left(a^2+b^2+c^2\right)$. Jadi yang perlu dihitung lebih dulu adalah $R$.
- Cari $R$ lewat $R = \dfrac{abc}{4L}$, dengan $L$ dari rumus Heron.

## Pembahasan

**Kumpulkan yang diperlukan.** Dengan $a = BC = 7$, $b = CA = 13$, $c = AB = 15$:

$$a^2 + b^2 + c^2 = 49 + 169 + 225 = 443$$

**Hitung $R^2$ tanpa menyentuh akar.** Setengah kelilingnya $\tfrac{35}{2}$ — pecahan yang
merepotkan, jadi pakai bentuk kuadrat rumus Heron yang seluruhnya bilangan bulat:

$$16L^2 = 2a^2b^2 + 2b^2c^2 + 2c^2a^2 - a^4 - b^4 - c^4$$

$$= 2(49)(169) + 2(169)(225) + 2(225)(49) - 2401 - 28561 - 50625$$

$$= 16562 + 76050 + 22050 - 81587 = 33075$$

Lalu dari $R = \dfrac{abc}{4L}$:

$$R^2 = \frac{(abc)^2}{16L^2} = \frac{\left(7 \cdot 13 \cdot 15\right)^2}{33075}
= \frac{1365^2}{33075} = \frac{1863225}{33075} = \frac{169}{3}$$

**Masukkan ke rumus Euler.**

$$OH^2 = 9R^2 - \left(a^2+b^2+c^2\right) = 9 \cdot \frac{169}{3} - 443 = 507 - 443 = 64$$

$$OH = \boxed{8}$$

### Kenapa lewat $R^2$, bukan $R$

Perhatikan bahwa $R = \dfrac{13}{\sqrt3}$ — bilangan berakar yang kalau dibulatkan akan
membawa kesalahan ke jawaban akhirnya. Rumus Eulernya memakai $R^2$, jadi akarnya tidak
pernah perlu diambil.

Kebiasaan yang berguna pada soal lingkaran luar: **hitung $R^2$ langsung sebagai
$\dfrac{(abc)^2}{16L^2}$**, dan biarkan $16L^2$ tetap bulat. Bentuk kuadrat Heron dibuat
persis untuk itu.

### Periksa dengan koordinat

Taruh $B(0,0)$, $C(7,0)$. Absis $A$ dari dua kali Pythagoras:

$$x = \frac{c^2 - b^2 + a^2}{2a} = \frac{225 - 169 + 49}{14} = \frac{105}{14} = 7{,}5$$

$$y = \sqrt{225 - 56{,}25} = \sqrt{168{,}75} \approx 12{,}990$$

Pusat lingkaran luarnya berabsis $\tfrac72 = 3{,}5$ (pada sumbu $BC$), dan hitungan
lengkapnya memberi $O \approx (3{,}5;\ 6{,}640)$ serta

$$H = \left(7{,}5;\ -0{,}289\right)$$

$$OH = \sqrt{4^2 + 6{,}928^2} = \sqrt{16 + 48} = 8 \quad ✓$$

Sekalian terlihat bahwa $A$ berabsis $7{,}5$, sedikit di sebelah kanan $C(7,0)$. Itu tanda
$\angle C$ tumpul, dan memang

$$\cos C = \frac{a^2+b^2-c^2}{2ab} = \frac{49+169-225}{182} = -\frac{7}{182} \approx -0{,}038$$

jadi $\angle C \approx 92{,}2^\circ$ — nyaris siku-siku tetapi tumpul. Akibatnya $H$ jatuh
**di luar** segitiga, tepat di bawah $BC$. Rumus Eulernya tidak peduli: ia hanya memakai
panjang sisi dan $R$.

(Kebetulan yang enak dilihat: $\cos B = \dfrac{49+225-169}{210} = \dfrac12$, jadi
$\angle B = 60^\circ$ tepat.)

### Periksa perbandingan $2:1$

Titik beratnya $G = \left(\tfrac{0+7+7{,}5}{3},\ \tfrac{12{,}990}{3}\right)
\approx \left(4{,}833;\ 4{,}330\right)$.

$$HG \approx \sqrt{2{,}667^2 + 4{,}619^2} \approx 5{,}333, \qquad
GO \approx \sqrt{1{,}333^2 + 2{,}309^2} \approx 2{,}667$$

Nisbahnya $2{,}000$ ✓, dan $HG + GO = 8 = OH$ ✓ — jadi ketiganya memang segaris dengan $G$ di
antara $H$ dan $O$.

### Kapan rumusnya memberi nol

$OH = 0$ berarti $O = H$, dan itu hanya terjadi pada segitiga **sama sisi**, di mana keempat
titik istimewanya menyatu. Rumusnya memberi

$$9R^2 = a^2+b^2+c^2$$

Untuk sama sisi bersisi $s$ berlaku $R = \tfrac{s}{\sqrt3}$, sehingga $9R^2 = 3s^2 = a^2+b^2+c^2$ ✓

Karena $OH^2 \ge 0$ selalu, rumus itu sekaligus membuktikan ketaksamaan

$$a^2+b^2+c^2 \ \le\ 9R^2$$

untuk setiap segitiga, dengan kesamaan tepat pada yang sama sisi. Itu contoh khas bagaimana
sebuah kesamaan geometri melahirkan ketaksamaan cuma-cuma.
