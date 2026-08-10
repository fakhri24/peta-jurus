---
id: gis-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [garis-istimewa]
bentuk: isian
kesulitan: 3
jawaban: "22"
---

## Soal

Pada segitiga $ABC$ diketahui $BC = 14$, $CA = 21$, dan $AB = 25$. Titik $M$ adalah titik
tengah sisi $BC$.

Tentukan panjang $AM$.

## Petunjuk

- Ruas dari titik sudut ke titik tengah sisi seberangnya punya nama sendiri, dan panjangnya bisa dihitung langsung dari ketiga sisi.
- Yang dicari adalah panjang garis berat dari $A$. Ada rumus yang menghubungkannya dengan $a$, $b$, dan $c$.
- $m_a^2 = \dfrac{2b^2 + 2c^2 - a^2}{4}$, dengan $a = BC$ sisi yang dipotong.

## Pembahasan

**Kenali ruasnya.** $M$ titik tengah $BC$, jadi $AM$ adalah **garis berat** dari $A$ — bukan
garis tinggi dan bukan garis bagi. Perbedaan itu menentukan seluruh perhitungan berikutnya.

**Pakai rumus garis berat.** Dengan penamaan baku $a = BC = 14$, $b = CA = 21$, $c = AB = 25$:

$$m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4} = \frac{2(21)^2 + 2(25)^2 - 14^2}{4}$$

$$= \frac{882 + 1250 - 196}{4} = \frac{1936}{4} = 484$$

$$AM = \sqrt{484} = \boxed{22}$$

### Menurunkannya lewat Stewart, supaya tidak perlu dihafal

Rumus di atas kasus khusus dari **teorema Stewart**. Untuk titik $D$ pada $BC$ dengan
$BD = m$, $DC = n$, dan $AD = d$:

$$b^2 m + c^2 n = a\left(d^2 + mn\right)$$

Untuk garis berat, $m = n = \tfrac{a}{2} = 7$:

$$21^2 \cdot 7 + 25^2 \cdot 7 = 14\left(d^2 + 49\right)$$

$$3087 + 4375 = 7462 = 14 d^2 + 686$$

$$14 d^2 = 6776 \quad \Longrightarrow \quad d^2 = 484 \quad \Longrightarrow \quad d = 22$$

Angka yang sama, dan satu rumus ini juga memberi panjang garis bagi kalau $m : n$ diganti.
Menghafal satu Stewart lebih hemat daripada menghafal dua rumus turunannya.

### Periksa lewat koordinat

Taruh $B(0,0)$ dan $C(14,0)$. Absis $A$ diperoleh dari dua kali Pythagoras:

$$x^2 + y^2 = 625, \qquad (x-14)^2 + y^2 = 441$$

Kurangkan: $28x - 196 = 184$, sehingga $x = \tfrac{95}{7}$ dan $y^2 = 625 - \tfrac{9025}{49}
= \tfrac{21600}{49}$.

Dengan $M(7,0)$:

$$AM^2 = \left(\tfrac{95}{7} - 7\right)^2 + \tfrac{21600}{49}
= \tfrac{2116}{49} + \tfrac{21600}{49} = \tfrac{23716}{49} = 484 \quad ✓$$

Jalan ketiga yang sepenuhnya berbeda memberi angka yang sama.

### Mengapa garis berat, bukan garis tinggi

Godaan terbesar pada soal semacam ini adalah menganggap $AM$ tegak lurus $BC$. Ia tidak.
Kaki garis tinggi dari $A$ jatuh di $x = \tfrac{95}{7} \approx 13{,}57$ — hampir menempel
$C$, jauh sekali dari $M(7,0)$.

Keduanya berimpit **hanya** kalau $AB = AC$. Karena $25 \ne 21$, mengira $AM \perp BC$ di
sini memberi $\sqrt{625 - 49} = 24$, sebuah angka yang terlihat wajar dan sepenuhnya salah.

### Nilainya tidak bergantung pada gambar

Perhatikan bahwa rumus garis berat hanya memakai ketiga panjang sisi. Ia tidak peduli
segitiganya lancip atau tumpul, dan tidak peduli bagaimana kamu menggambarnya. Itu ciri
rumus yang aman dipakai tanpa gambar — berbeda dengan panjang kaki garis tinggi, yang
tandanya berubah kalau kakinya jatuh di perpanjangan sisi.
