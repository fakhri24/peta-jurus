---
id: ptl-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy]
bentuk: isian
kesulitan: 4
jawaban: "7/9"
jawaban_alt: ["0,777777778", "0.777777778", "21/27"]
---

## Soal

Pada segiempat talibusur $ABCD$ diketahui $AB = 8$, $BC = 15$, $CD = 24$, dan $DA = 25$.
Tidak ada panjang diagonal yang diketahui.

Tentukan nilai $\dfrac{AC}{BD}$.

## Petunjuk

- Teorema Ptolemy yang biasa memberi **hasil kali** kedua diagonal, bukan perbandingannya. Itu belum cukup.
- Ada bentuk kedua yang memberi perbandingan diagonalnya langsung dari keempat sisinya.
- $\dfrac{AC}{BD} = \dfrac{AB \cdot AD + CB \cdot CD}{BA \cdot BC + DA \cdot DC}$ — perhatikan bahwa pembilangnya mengumpulkan sisi-sisi yang menempel pada $A$ dan pada $C$, penyebutnya yang menempel pada $B$ dan pada $D$.

## Pembahasan

**Kenapa Ptolemy biasa belum cukup.** Bentuk yang biasa memberi

$$AC \cdot BD = AB \cdot CD + BC \cdot AD = 8 \times 24 + 15 \times 25 = 192 + 375 = 567$$

Satu persamaan, dua bilangan yang belum diketahui. Untuk memisahkan keduanya diperlukan satu
hubungan lagi.

**Pakai Ptolemy kedua.**

$$\frac{AC}{BD} = \frac{AB \cdot AD + CB \cdot CD}{BA \cdot BC + DA \cdot DC}$$

Cara membaca susunannya: pembilangnya menjumlahkan hasil kali kedua sisi yang berpangkal di
$A$ dan kedua sisi yang berpangkal di $C$ — yaitu kedua ujung diagonal $AC$. Penyebutnya
melakukan hal yang sama untuk $B$ dan $D$.

$$\frac{AC}{BD} = \frac{8 \times 25 + 15 \times 24}{8 \times 15 + 25 \times 24}
= \frac{200 + 360}{120 + 600} = \frac{560}{720} = \boxed{\frac79}$$

### Kedua diagonalnya sekaligus

Sekarang hasil kali dan perbandingannya sudah ada, jadi keduanya tertentu. Tulis $AC = 7k$
dan $BD = 9k$:

$$7k \cdot 9k = 567 \quad \Longrightarrow \quad 63k^2 = 567 \quad \Longrightarrow \quad k^2 = 9
\quad \Longrightarrow \quad k = 3$$

$$AC = 21, \qquad BD = 27$$

Keduanya bulat — segiempat ini pun segiempat Brahmagupta.

### Periksa dengan rumus diagonal

$$AC^2 = \frac{(ac+bd)(ad+bc)}{ab+cd}, \qquad BD^2 = \frac{(ac+bd)(ab+cd)}{ad+bc}$$

dengan $a = 8$, $b = 15$, $c = 24$, $d = 25$:

$$ac+bd = 192+375 = 567, \qquad ad+bc = 200+360 = 560, \qquad ab+cd = 120+600 = 720$$

$$AC^2 = \frac{567 \times 560}{720} = 441 \quad \Longrightarrow \quad AC = 21 \quad ✓$$

$$BD^2 = \frac{567 \times 720}{560} = 729 \quad \Longrightarrow \quad BD = 27 \quad ✓$$

Perhatikan bahwa rumus diagonal itu sebenarnya Ptolemy pertama dan kedua yang sudah
digabungkan: hasil bagi keduanya memberi $\dfrac{AC^2}{BD^2} = \dfrac{(ad+bc)^2}{(ab+cd)^2}$,
dan hasil kalinya memberi $AC^2 BD^2 = (ac+bd)^2$.

Jadi kamu hanya perlu mengingat salah satu pasangan, bukan ketiganya.

### Kenapa perbandingannya begitu

Bagi segiempat menjadi dua segitiga oleh diagonal $AC$, lalu tulis luasnya. Perbandingan
$\dfrac{AC}{BD}$ pada akhirnya turun dari perbandingan luas dan aturan sinus di lingkaran
yang sama, tempat tiap talibusur berbanding lurus dengan sinus sudut kelilingnya.

Yang perlu diingat untuk lembar jawaban: **Ptolemy kedua bukan konsekuensi sepele dari yang
pertama**, dan kalau dipakai ia perlu disebut namanya, bukan diturunkan diam-diam.

### Kapan bentuk kedua ini dipakai

Ia jarang muncul, dan justru itu alasannya berharga: soal yang memberi **keempat sisi tanpa
satu pun diagonal** lalu menanyakan diagonalnya hampir selalu ingin bentuk ini — atau rumus
diagonal yang setara dengannya.

Kalau soal sudah memberi satu diagonal, Ptolemy biasa jauh lebih pendek. Bacalah keterangan
soalnya dulu, baru pilih bentuknya.
