---
id: eul-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [garis-euler, titik-istimewa]
bentuk: isian
kesulitan: 4
jawaban: "10"
---

## Soal

Pada segitiga $ABC$, jari-jari lingkaran luarnya $13$ dan $BC = 24$. Titik $H$ adalah titik
tingginya.

Tentukan panjang $AH$.

## Petunjuk

- Jarak dari titik sudut ke titik tinggi punya hubungan tetap dengan jarak dari pusat lingkaran luar ke sisi seberangnya.
- $AH = 2 \cdot OM$, dengan $M$ titik tengah $BC$ dan $O$ pusat lingkaran luar.
- Hitung $OM$ dengan Pythagoras pada segitiga $OMB$, yang siku-siku karena $OM \perp BC$.

## Pembahasan

**Hitung $OM$.** Misalkan $M$ titik tengah $BC$. Karena $OB = OC = R$, segitiga $OBC$ sama
kaki, sehingga $OM \perp BC$ dan $M$ kaki tegak lurusnya. Pada $\triangle OMB$ yang siku-siku
di $M$:

$$OM = \sqrt{OB^2 - MB^2} = \sqrt{13^2 - 12^2} = \sqrt{169 - 144} = 5$$

**Pakai hubungan $AH = 2\,OM$.**

$$AH = 2 \times 5 = \boxed{10}$$

### Dari mana hubungan $AH = 2\,OM$

Pakai vektor dengan $O$ sebagai titik asal. Yang perlu diketahui satu hal:

$$\overrightarrow{OH} = \overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}$$

Dari situ

$$\overrightarrow{AH} = \overrightarrow{OH} - \overrightarrow{OA}
= \overrightarrow{OB} + \overrightarrow{OC}$$

Sedangkan $M$ titik tengah $BC$, sehingga
$\overrightarrow{OM} = \tfrac12\left(\overrightarrow{OB} + \overrightarrow{OC}\right)$. Maka

$$\overrightarrow{AH} = 2\,\overrightarrow{OM}$$

Jadi bukan hanya panjangnya dua kali — **arahnya pun sama**, sehingga $AH \parallel OM$. Dan
karena $OM \perp BC$, hubungan itu sekaligus mengulang bahwa $AH$ tegak lurus $BC$, yaitu
bahwa $AH$ memang bagian dari garis tinggi.

### Bentuk kedua yang setara

Karena $OM = R\cos A$ — sudut pusat $\angle BOC = 2A$ dan $OM$ separuh garis bagi sudut itu —
hubungan yang sama bisa ditulis

$$AH = 2R\cos A$$

Periksa di sini: $\cos A = \dfrac{OM}{R} = \dfrac{5}{13}$, sehingga
$AH = 2 \cdot 13 \cdot \tfrac{5}{13} = 10$ ✓

Bentuk $2R\cos A$ lebih berguna kalau yang diketahui sudut; bentuk $2\,OM$ lebih berguna
kalau yang diketahui panjang sisi.

### Periksa lewat aturan sinus

Dari $\dfrac{a}{\sin A} = 2R$ diperoleh $\sin A = \dfrac{24}{26} = \dfrac{12}{13}$, sehingga
$\cos A = \pm\tfrac{5}{13}$.

Nilai positif memberi $A \approx 67{,}4^\circ$ dan $AH = 10$; nilai negatif memberi
$A \approx 112{,}6^\circ$ dan $AH = -10$, yang berarti $H$ berada di **seberang** $A$ terhadap
$BC$ dengan jarak $10$.

Jadi panjangnya tetap $10$ pada kedua kemungkinan; yang berbeda letak $H$ terhadap segitiga.
Karena soal hanya menanyakan panjang, jawabannya tunggal — tetapi kalau soal menanyakan
letaknya, kedua kasus wajib disebut.

### Kaitannya dengan lingkaran sembilan titik

Titik tengah $AH$ adalah salah satu dari sembilan titik, dan di sini jaraknya ke $A$ adalah
$5$. Titik $M$ juga salah satu dari sembilan itu. Keduanya bahkan **berseberangan** pada
lingkaran sembilan titik, sehingga jarak keduanya sama dengan garis tengahnya, yaitu $R = 13$.

Hubungan $AH = 2\,OM$ adalah bentuk paling sederhana dari kenyataan itu — dan itu sebabnya ia
muncul berulang kali begitu soal menyebut $H$ bersama $O$.
