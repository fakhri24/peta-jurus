---
id: cvm-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ceva-menelaus]
bentuk: isian
kesulitan: 3
jawaban: "10"
---

## Soal

Pada segitiga $ABC$, ruas $AD$, $BE$, dan $CF$ berpotongan di satu titik, dengan $D$ pada
$BC$, $E$ pada $CA$, dan $F$ pada $AB$.

Diketahui $BD = 3$, $DC = 5$, $CE = 4$, $EA = 6$, dan $AB = 14$.

Tentukan panjang $AF$.

## Petunjuk

- Ceva memberi perbandingan $\dfrac{AF}{FB}$, bukan panjang $AF$ langsung.
- Setelah perbandingannya diperoleh, pakai bahwa $AF + FB = AB = 14$.
- $\dfrac{BD}{DC} \cdot \dfrac{CE}{EA} \cdot \dfrac{AF}{FB} = 1$.

## Pembahasan

**Pakai Ceva untuk memperoleh perbandingannya.**

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

$$\frac{3}{5} \cdot \frac{4}{6} \cdot \frac{AF}{FB} = 1$$

$$\frac{3}{5} \cdot \frac{2}{3} = \frac{2}{5}, \qquad
\frac{2}{5} \cdot \frac{AF}{FB} = 1 \quad \Longrightarrow \quad \frac{AF}{FB} = \frac52$$

**Ubah perbandingan jadi panjang.** Karena $F$ terletak di dalam ruas $AB$, kedua bagiannya
berjumlah $AB$:

$$AF + FB = 14, \qquad \frac{AF}{FB} = \frac52$$

Bagi $14$ menjadi $5 + 2 = 7$ bagian:

$$AF = \frac{5}{7} \times 14 = \boxed{10}, \qquad FB = \frac{2}{7} \times 14 = 4$$

### Periksa

$$\frac{AF}{FB} = \frac{10}{4} = \frac52 \quad ✓, \qquad 10 + 4 = 14 \quad ✓$$

Lalu periksa Ceva dengan angka aslinya:

$$\frac{3}{5} \cdot \frac{4}{6} \cdot \frac{10}{4} = \frac{3 \cdot 4 \cdot 10}{5 \cdot 6 \cdot 4}
= \frac{120}{120} = 1 \quad ✓$$

### Yang tidak diperlukan soal ini

Panjang $BC = 3 + 5 = 8$ dan $CA = 4 + 6 = 10$ ikut diketahui, tetapi tidak dipakai sama
sekali. Itu bukan kelebihan keterangan yang menyesatkan, melainkan sifat Ceva: ia hanya
peduli pada **perbandingan** di tiap sisi, tidak pada panjang sisinya.

Akibat praktisnya, semua segitiga dengan perbandingan yang sama memberi jawaban yang sama.
Kalau soal cuma memberi $BD : DC = 3 : 5$ tanpa panjangnya, jawabannya tetap $AF = 10$.

### Periksa apakah segitiganya benar-benar ada

Dengan $BC = 8$, $CA = 10$, $AB = 14$: ketaksamaan segitiga menuntut $8 + 10 > 14$ ✓,
$8 + 14 > 10$ ✓, $10 + 14 > 8$ ✓. Jadi segitiganya sah.

Pemeriksaan ini tidak selalu perlu, tetapi berguna saat soal memberi banyak panjang
sekaligus: soal yang angkanya tidak konsisten kadang muncul, dan lebih baik ketahuan di awal
daripada setelah setengah halaman perhitungan.

### Titik potongnya siapa

Tiga ruas dari titik sudut yang konkuren belum tentu punya nama. Kalau ketiganya garis berat,
titik potongnya titik berat; kalau garis bagi, pusat lingkaran dalam; kalau garis tinggi,
titik tinggi.

Di sini bukan salah satu pun: $BD : DC = 3 : 5 \ne 1 : 1$, jadi $AD$ bukan garis berat; dan
kalau $AD$ garis bagi maka $BD : DC$ harus sama dengan $AB : AC = 14 : 10 = 7 : 5$, padahal
$3 : 5$. Titik potongnya cuma sebuah titik biasa — dan Ceva tidak memerlukan namanya.
