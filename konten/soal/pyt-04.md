---
id: pyt-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [pythagoras]
bentuk: isian
kesulitan: 2
jawaban: "8"
---

## Soal

Sebuah trapesium sama kaki mempunyai sisi-sisi sejajar sepanjang $22$ dan $10$, sedangkan
kedua kakinya masing-masing sepanjang $10$.

Tentukan tinggi trapesium itu.

## Petunjuk

- Trapesium tidak punya rumus tinggi sendiri. Potong ia menjadi bangun-bangun yang lebih kamu kenal, lalu kerjakan bagian yang memuat kakinya.
- Tarik garis tinggi dari kedua ujung sisi sejajar yang pendek ke sisi sejajar yang panjang. Gambarnya terbagi menjadi sebuah persegi panjang dan dua segitiga siku-siku.
- Karena trapesiumnya sama kaki, kedua segitiga siku-siku itu kongruen — jadi selisih kedua sisi sejajarnya terbagi rata.

## Pembahasan

**Potong menjadi bangun yang dikenal.** Sebut trapesiumnya $ABCD$ dengan $AB = 22$ (sisi
sejajar panjang), $DC = 10$ (sisi sejajar pendek), dan kaki $AD = BC = 10$. Tarik garis tinggi
dari $D$ dan dari $C$ ke $AB$, dengan kaki berturut-turut $P$ dan $Q$.

Gambarnya kini terbagi menjadi tiga bagian: $\triangle APD$, persegi panjang $PQCD$, dan
$\triangle BQC$.

**Bagi selisihnya.** Karena $PQCD$ persegi panjang, $PQ = DC = 10$. Sisanya adalah $AP$ dan
$QB$, dengan

$$AP + QB = 22 - 10 = 12$$

Karena trapesiumnya **sama kaki**, kedua segitiga siku-siku di ujungnya kongruen, sehingga
$AP = QB$:

$$AP = QB = \frac{12}{2} = 6$$

**Pythagoras pada segitiga ujungnya.** Segitiga $APD$ siku-siku di $P$, dengan sisi miring
$AD = 10$ dan sisi siku-siku $AP = 6$:

$$t^2 = 10^2 - 6^2 = 100 - 36 = 64 \quad \Longrightarrow \quad t = \boxed{8}$$

**Periksa.** Tripel $(6, 8, 10)$ adalah kelipatan dua dari $(3,4,5)$ ✓.

### Langkah yang menentukan bukan Pythagorasnya

Pythagoras di baris terakhir itu bagian termudah. Yang benar-benar menentukan adalah **membagi
$12$ menjadi $6$ dan $6$** — dan itu sah hanya karena trapesiumnya sama kaki.

Kalau kakinya tidak sama panjang, $AP$ dan $QB$ berbeda, dan satu persamaan tidak lagi cukup
untuk menentukan keduanya. Jadi syarat "sama kaki" bukan hiasan di soal ini; ia yang membuat
soalnya punya jawaban tunggal.

### Yang bisa dihitung berikutnya

Setelah tingginya diketahui, seluruh trapesium terbuka:

- Luasnya $\dfrac{22 + 10}{2} \times 8 = 128$.
- Diagonalnya: dari $A(0,0)$ ke $C(16, 8)$, panjangnya $\sqrt{16^2 + 8^2} = \sqrt{320} = 8\sqrt{5}$.

Perhatikan bahwa diagonalnya **tidak** bulat meski semua sisinya bulat. Soal yang menanyakan
diagonal biasanya meminta bentuk akar yang sudah disederhanakan, dan $\sqrt{320}$ bukan bentuk
akhir yang sederhana.
