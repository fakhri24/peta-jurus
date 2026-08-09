---
id: smp-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: uraian
kesulitan: 3
---

## Soal

Lima titik ditempatkan secara sembarang di dalam sebuah persegi bersisi $2$ (titik boleh
berada di tepinya).

Buktikan bahwa ada dua titik di antaranya yang jaraknya tidak lebih dari $\sqrt{2}$.

## Petunjuk

- Soal meminta membuktikan **ada**, tanpa menyuruh menemukan titiknya. Pikirkan cara memaksa dua titik berdekatan.
- Potong perseginya menjadi beberapa bagian yang lebih kecil. Berapa bagian yang tepat, mengingat titiknya ada lima?
- Kalau dua titik berada di dalam satu bagian, jarak terjauh yang mungkin di antara keduanya adalah panjang diagonal bagian itu.

## Pembahasan

**Susun sarangnya.** Bagi persegi bersisi $2$ menjadi empat persegi bersisi $1$, dengan
memotongnya di tengah secara mendatar dan tegak:

$$2 \times 2 = 4 \text{ bagian}$$

Keempat bagian itu menutupi seluruh persegi besar, sehingga setiap titik pasti berada di
sedikitnya satu bagian. (Titik yang jatuh persis di garis potong berada di lebih dari satu
bagian; pilih saja salah satunya, misalnya yang paling kiri lalu paling bawah. Yang
dibutuhkan hanya bahwa tiap titik dapat ditempatkan ke **tepat satu** bagian.)

**Terapkan prinsipnya.** Ada $5$ titik dan $4$ bagian, dan $5 > 4$. Maka ada satu bagian
yang memuat paling sedikit dua titik. Sebut kedua titik itu $P$ dan $Q$.

**Batasi jaraknya.** $P$ dan $Q$ berada di dalam persegi bersisi $1$ yang sama. Jarak
terjauh antara dua titik di dalam sebuah persegi adalah panjang **diagonalnya**, dan untuk
persegi bersisi $1$:

$$d = \sqrt{1^2 + 1^2} = \sqrt{2}$$

Karena itu

$$PQ \le \sqrt{2} \qquad \blacksquare$$

### Mengapa dipotong menjadi empat

Banyaknya potongan dipilih dari banyaknya titik: dengan $5$ titik, sarang harus **kurang
dari $5$** supaya prinsipnya menggigit. Empat adalah potongan terbanyak yang masih memenuhi
itu, dan potongan yang lebih banyak justru melemahkan kesimpulan — dengan $5$ potongan,
tidak ada yang bisa disimpulkan sama sekali.

Sebaliknya, potongan yang lebih sedikit menghasilkan kesimpulan yang lebih lemah. Kalau
perseginya dibagi dua saja, tiap bagian berukuran $1 \times 2$ dan diagonalnya $\sqrt5$ —
pernyataan yang benar, tetapi jauh lebih longgar daripada yang diminta.

### Batas ini tidak bisa diperbaiki dengan cara yang sama

Tempatkan kelima titik di keempat pojok dan di titik pusat persegi. Jarak dari pusat ke
tiap pojok adalah $\sqrt 2$, dan jarak antar-pojok yang berdekatan adalah $2$. Jarak
terkecil pada susunan ini tepat $\sqrt 2$ — jadi pernyataan soal tidak bisa diperketat
menjadi "kurang dari $\sqrt 2$".

Adanya contoh yang mencapai batas seperti ini adalah tanda bahwa pemotongannya sudah
sepadan dengan soalnya.

## Rubrik

- Membagi persegi menjadi empat persegi bersisi $1$, dan menyebutnya sebagai sarang
- Menyatakan keempat bagian itu menutupi seluruh persegi, sehingga tiap titik masuk salah satunya
- Menerapkan prinsip sarang merpati dengan $5 > 4$ untuk menyimpulkan ada bagian berisi dua titik
- Menghitung diagonal persegi bersisi $1$ sebagai $\sqrt2$
- Menyatakan jarak dua titik di dalam sebuah persegi tidak melebihi diagonalnya, lalu menyimpulkan
- Menangani titik yang jatuh di garis potong, atau menyatakan pemilihannya dengan jelas
