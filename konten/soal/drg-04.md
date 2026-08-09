---
id: drg-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 3
jawaban: "45"
---

## Soal

Lima surat dimasukkan secara acak ke dalam lima amplop bertuliskan alamat, satu surat per
amplop.

Ada berapa cara sehingga **tepat satu** surat masuk ke amplop yang benar?

## Petunjuk

- Pecah menjadi dua keputusan: surat mana yang benar, lalu apa yang terjadi pada empat sisanya.
- Kata "tepat satu" menuntut keempat surat sisanya seluruhnya salah amplop.
- Sisanya adalah persoalan yang sama pada empat objek.

## Pembahasan

**Langkah 1 — pilih surat yang benar.** Satu dari lima:

$$\binom51 = 5$$

**Langkah 2 — pastikan empat sisanya seluruhnya salah.** Ini persoalan yang sama pada $4$
objek:

$$D_4 = 9$$

**Gabungkan.**

$$5 \times 9 = \boxed{45}$$

**Bandingkan dengan tiga soal yang bunyinya mirip,** dan perhatikan betapa berbedanya
jawabannya:

| Pertanyaan | Hitungan | Hasil |
|---|---|---|
| Tidak ada yang benar | $D_5$ | $44$ |
| Tepat satu benar | $\binom51 D_4$ | $45$ |
| Paling sedikit satu benar | $5! - D_5$ | $76$ |

Ketiganya dipisahkan oleh beberapa kata saja di soal, dan membaca kata itu dengan benar
adalah separuh pekerjaannya.

**Periksa lewat jumlah seluruhnya.** Seluruh kemungkinan banyaknya surat yang benar harus
berjumlah $5! = 120$:

$$\underbrace{44}_{m=0} + \underbrace{45}_{m=1} + \underbrace{\binom52 D_3 = 10 \times 2 = 20}_{m=2}
+ \underbrace{\binom53 D_2 = 10 \times 1 = 10}_{m=3} + \underbrace{\binom54 D_1 = 0}_{m=4}
+ \underbrace{1}_{m=5}$$

$$44 + 45 + 20 + 10 + 0 + 1 = 120$$

Cocok.

**Perhatikan kejanggalan yang menarik:** "tepat satu benar" ($45$) ternyata **lebih banyak**
daripada "tidak ada yang benar" ($44$), meskipun hanya selisih satu. Itu bukan kekeliruan —
untuk $n = 5$ kedua angka itu memang hampir sama, dan sifat $D_n \approx \frac{n!}{e}$
beserta $\binom n1 D_{n-1} \approx \frac{n!}{e}$ menjelaskan mengapa keduanya selalu
berdekatan.

**Kekeliruan yang paling sering** adalah memakai $4!$ untuk langkah kedua, sehingga
jawabannya $5 \times 24 = 120$ — yaitu seluruh susunan yang ada. Angka itu jelas keliru
karena tidak semua susunan punya tepat satu surat benar, dan kejanggalan itu langsung
terlihat kalau hasilnya dibandingkan dengan $5!$.
