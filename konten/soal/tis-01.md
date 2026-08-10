---
id: tis-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [titik-istimewa, garis-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "15"
---

## Soal

Pada segitiga $ABC$, titik $G$ adalah titik beratnya. Diketahui $GA = 8$, $GB = 6$, dan
$GA \perp GB$.

Tentukan panjang garis berat dari $C$.

## Petunjuk

- Sudut siku-siku di $G$ membuat $\triangle AGB$ siku-siku. Apa yang bisa langsung dihitung darinya?
- Garis berat dari $C$ menuju titik tengah $AB$. Sebut titik itu $M$ — dan perhatikan bahwa $M$ juga titik tengah sisi miring $\triangle AGB$.
- Pada segitiga siku-siku, garis berat ke sisi miring panjangnya setengah sisi miring itu.

## Pembahasan

**Pakai sudut siku-sikunya.** Segitiga $AGB$ siku-siku di $G$, jadi

$$AB = \sqrt{GA^2 + GB^2} = \sqrt{64 + 36} = 10$$

**Perhatikan titik tengah $AB$.** Sebut $M$ titik tengah $AB$. Ia titik ujung garis berat
dari $C$ — tetapi sekaligus **titik tengah sisi miring** segitiga siku-siku $AGB$.

Pada segitiga siku-siku, garis berat ke sisi miring panjangnya setengah sisi miring itu,
sebab titik tengah sisi miring adalah pusat lingkaran luarnya:

$$GM = \tfrac12 AB = 5$$

**Pakai perbandingan titik berat.** Titik berat membagi tiap garis berat dengan perbandingan
$2 : 1$ diukur dari titik sudut, jadi $GM$ adalah sepertiga garis berat dari $C$:

$$m_c = 3 \cdot GM = 3 \times 5 = \boxed{15}$$

### Periksa lewat koordinat

Ambil $G$ di titik asal, $A(8,0)$, $B(0,6)$ — sesuai $GA = 8$, $GB = 6$, dan tegak lurus.

Karena $G$ titik berat, $\dfrac{A+B+C}{3} = G = (0,0)$, sehingga

$$C = -(A+B) = (-8, -6)$$

Titik tengah $AB$ adalah $M(4, 3)$, dan

$$CM = \sqrt{(4+8)^2 + (3+6)^2} = \sqrt{144 + 81} = \sqrt{225} = 15 \quad ✓$$

Sekalian periksa perbandingannya: $CG = \sqrt{64+36} = 10$ dan $GM = \sqrt{16+9} = 5$, jadi
$CG : GM = 2 : 1$ ✓

### Jebakan: perbandingan dipakai terbalik

Dari titik sudut ke $G$ **dua** bagian; dari $G$ ke titik tengah sisi **satu** bagian. Kalau
dibalik, $GM$ dianggap dua pertiga garis beratnya dan jawabannya keluar $7{,}5$.

Cara mengingat tanpa hafalan: titik berat adalah titik seimbang, dan ia selalu lebih dekat ke
sisi daripada ke titik sudut — sebab sisi punya "lebih banyak segitiga" di sekitarnya. Jadi
bagian yang pendek adalah yang ke sisi.

### Sisi-sisi segitiganya, kalau ditanya

Dari koordinat tadi: $AB = 10$, dan

$$BC = \sqrt{(-8-0)^2 + (-6-6)^2} = \sqrt{64+144} = \sqrt{208}, \qquad
CA = \sqrt{(-8-8)^2 + 36} = \sqrt{292}$$

Periksa dengan identitas yang berlaku pada setiap segitiga:

$$GA^2 + GB^2 + GC^2 = \tfrac13\left(a^2+b^2+c^2\right)$$

Ruas kiri $64 + 36 + 100 = 200$; ruas kanan $\tfrac13(208 + 292 + 100) = \tfrac13(600) = 200$ ✓

Identitas itu turunan langsung dari rumus panjang garis berat, dan berguna tiap kali soal
memberi jarak dari titik berat ke titik sudut.

### Kenapa soal ini tidak memerlukan panjang sisinya

Perhatikan bahwa jawabannya keluar tanpa pernah menghitung $BC$ atau $CA$. Yang dipakai cuma
dua hal: sifat garis berat ke sisi miring, dan perbandingan $2:1$.

Kebiasaan yang berguna: **kalau soal memberi jarak dari titik berat, terjemahkan dulu jadi
panjang garis berat** dengan mengalikan $\tfrac32$. Setelah itu soalnya kembali jadi soal
garis berat biasa.
