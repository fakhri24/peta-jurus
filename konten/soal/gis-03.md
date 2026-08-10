---
id: gis-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "5"
---

## Soal

Pada segitiga $ABC$ diketahui $AB = 4$, $BC = 15$, dan $CA = 13$. Dari titik $C$ ditarik
garis tinggi ke **garis** $AB$, memotongnya tegak lurus di titik $D$.

![Segitiga ABC dengan sudut di A tumpul. Sisi AB mendatar, dengan A di tengah gambar dan B di sebelah kanannya, panjangnya 4. Titik C berada jauh di kiri atas, dengan CA panjangnya 13 dan CB panjangnya 15. Dari C ditarik garis tinggi ke garis AB. Karena sudut A tumpul, kakinya jatuh di titik D pada perpanjangan sisi BA di sebelah kiri A — bukan di antara A dan B. Ruas dari D ke A digambar putus-putus sebagai perpanjangan, dan sudut di D siku-siku](segitiga-tumpul-kaki-luar.svg)

Tentukan panjang $AD$.

## Petunjuk

- Soal menulis "garis $AB$", bukan "sisi $AB$". Kata itu dipilih dengan sengaja.
- Periksa dulu jenis segitiganya: bandingkan $AB^2 + CA^2$ dengan $BC^2$.
- Misalkan $AD = x$ dan $CD = t$. Tulis Pythagoras pada $\triangle ADC$ dan pada $\triangle BDC$, ingat bahwa $BD = AD + AB$.

## Pembahasan

**Periksa jenis segitiganya lebih dulu.**

$$AB^2 + CA^2 = 16 + 169 = 185 \ <\ 225 = BC^2$$

Karena kuadrat sisi terpanjang **melebihi** jumlah kuadrat dua sisi lainnya, sudut di
hadapannya tumpul. Sisi terpanjang $BC$, dan sudut di hadapannya adalah $\angle A$. Jadi
$\angle A$ tumpul — dan itu berarti kaki garis tinggi dari $C$ jatuh di **perpanjangan**
$BA$, di luar ruas $AB$.

**Susun dua Pythagoras.** Misalkan $AD = x$ dan $CD = t$. Karena $D$ di luar ruas pada sisi
$A$, jarak dari $D$ ke $B$ adalah $x + 4$, bukan $4 - x$:

$$\triangle ADC: \quad x^2 + t^2 = 13^2 = 169$$

$$\triangle BDC: \quad (x+4)^2 + t^2 = 15^2 = 225$$

**Kurangkan.**

$$(x+4)^2 - x^2 = 56 \quad \Longrightarrow \quad 8x + 16 = 56 \quad \Longrightarrow \quad x = \boxed{5}$$

Sekalian: $t^2 = 169 - 25 = 144$, jadi $CD = 12$.

### Periksa lewat luas

Luas segitiga bisa dihitung dua jalan yang berbeda. Dengan Heron, $s = \tfrac{4+15+13}{2} = 16$:

$$L = \sqrt{16 (16-4)(16-15)(16-13)} = \sqrt{16 \cdot 12 \cdot 1 \cdot 3} = \sqrt{576} = 24$$

Dengan alas $AB$ dan tinggi $CD$:

$$L = \tfrac{1}{2} \times 4 \times 12 = 24 \quad ✓$$

Perhatikan bahwa alasnya tetap $AB = 4$, meskipun kaki tingginya di luar ruas itu. Tinggi
diukur ke **garisnya**, dan alas tetap sisinya.

### Kalau tandanya diabaikan

Kalau $D$ dianggap berada di antara $A$ dan $B$, persamaan keduanya menjadi
$(4-x)^2 + t^2 = 225$. Kurangkan dengan yang pertama:

$$16 - 8x = 56 \quad \Longrightarrow \quad x = -5$$

Tanda negatifnya bukan kecelakaan — ia **memberitahu** bahwa $D$ ada di arah yang
berlawanan dari yang diandaikan, sejauh $5$. Jadi aljabarnya memperbaiki sendiri
pengandaian yang salah, asal hasil negatifnya dibaca, bukan langsung diambil nilai
mutlaknya sebagai jawaban.

### Kapan kaki garis tinggi keluar

Kaki garis tinggi dari $C$ jatuh di luar ruas $AB$ tepat ketika salah satu dari $\angle A$
atau $\angle B$ tumpul. Pemeriksaannya murah dan sebaiknya jadi kebiasaan sebelum menggambar:

$$\angle A \text{ tumpul} \iff a^2 > b^2 + c^2$$

dengan $a$ sisi di hadapan $A$. Pada soal ini $225 > 185$, jadi ketahuan sejak sebelum satu
garis pun ditarik. Soal olimpiade sering memakai segitiga tumpul justru karena gambar yang
digambar kira-kira hampir selalu keluar lancip.
