---
id: gan-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: isian
kesulitan: 2
jawaban: "54"
---

## Soal

Persegi $ABCD$ mempunyai panjang sisi $12$. Titik $M$ adalah titik tengah sisi $BC$, dan titik
$N$ adalah titik tengah sisi $CD$.

Tentukan luas segitiga $AMN$.

## Petunjuk

- Bangunnya penuh sudut siku-siku dan titik tengah, tetapi miskin sudut yang bisa dikejar. Adakah cara menaruh bangunnya supaya semua titiknya punya alamat yang mudah?
- Taruh titik asal di salah satu titik sudut persegi, dengan kedua sisinya berimpit sumbu. Lalu tulis koordinat kelima titiknya.
- Setelah koordinatnya ada, luas segitiga bisa dihitung langsung dari koordinat ketiga titik sudutnya.

## Pembahasan

**Pilih letak sumbunya.** Koordinat boleh diletakkan di mana saja, dan pilihan itulah yang
menentukan panjang perhitungannya. Taruh titik asal di $D$, dengan sisi $DC$ pada sumbu $x$ dan
sisi $DA$ pada sumbu $y$:

$$D(0,0), \quad C(12,0), \quad B(12,12), \quad A(0,12)$$

Kedua titik tengahnya langsung terbaca:

$$M = \left(\frac{12+12}{2}, \frac{12+0}{2}\right) = (12, 6), \qquad
N = \left(\frac{12+0}{2}, \frac{0+0}{2}\right) = (6, 0)$$

**Pakai rumus luas dari koordinat.**

$$L = \tfrac{1}{2}\left| x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2) \right|$$

dengan $(x_1,y_1) = A(0,12)$, $(x_2,y_2) = M(12,6)$, $(x_3,y_3) = N(6,0)$:

$$L = \tfrac{1}{2}\left| 0(6-0) + 12(0-12) + 6(12-6) \right|$$

$$= \tfrac{1}{2}\left| 0 - 144 + 36 \right| = \tfrac{1}{2} \times 108 = \boxed{54}$$

### Periksa lewat pengurangan

Cara ini tidak memerlukan rumus koordinat sama sekali, dan bagus dipakai sebagai pemeriksa.
Luas $\triangle AMN$ adalah luas persegi dikurangi tiga segitiga siku-siku di sudut-sudutnya:

$$[ABM] = \tfrac{1}{2} \times 12 \times 6 = 36$$

$$[MCN] = \tfrac{1}{2} \times 6 \times 6 = 18$$

$$[AND] = \tfrac{1}{2} \times 6 \times 12 = 36$$

$$[AMN] = 144 - 36 - 18 - 36 = 54 \quad ✓$$

Dua jalan yang sepenuhnya berbeda memberi angka yang sama.

### Mengapa letak sumbunya penting

Coba bandingkan: kalau titik asal ditaruh di **pusat** persegi, koordinatnya menjadi
$A(-6,6)$, $B(6,6)$, $C(6,-6)$, $D(-6,-6)$, $M(6,0)$, $N(0,-6)$. Rumusnya tetap memberi $54$ —
tetapi separuh bilangannya bertanda negatif, dan peluang salah tanda naik tajam.

Aturan praktisnya: **taruh titik asal di titik sudut siku-siku, dan sumbunya berimpit dengan
sisi.** Dengan begitu sebanyak mungkin koordinat bernilai nol, dan nol adalah bilangan yang
paling murah dihitung.

### Nisbahnya, yang tidak bergantung pada ukuran

$$\frac{[AMN]}{[ABCD]} = \frac{54}{144} = \frac{3}{8}$$

Nisbah ini berlaku untuk persegi berukuran berapa pun — sisi $12$ hanya menentukan angkanya,
bukan bentuknya. Kalau soal memberi sisi $s$, jawabannya $\tfrac{3}{8}s^2$, dan mengerjakannya
dengan huruf sejak awal kadang justru lebih pendek daripada dengan angka.

### Kapan koordinat **bukan** jalan terbaik

Jurus ini kuat justru pada soal seperti ini: banyak sudut siku-siku, banyak titik tengah, dan
tidak ada lingkaran. Untuk soal yang penuh sudut keliling dan tali busur, koordinat biasanya
bentuk terpanjang dari jawaban yang sama — di sana jurus sintetik jauh lebih pendek.
