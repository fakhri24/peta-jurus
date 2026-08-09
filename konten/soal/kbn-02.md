---
id: kbn-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 2
jawaban: "20"
---

## Soal

Tentukan **suku konstan** — yaitu suku yang tidak memuat $x$ — pada penjabaran

$$\left(x + \frac{1}{x}\right)^{6}$$

## Petunjuk

- Tuliskan bentuk umum sukunya lebih dulu, lalu kumpulkan pangkat $x$ dari kedua bagian.
- Ingat $\frac{1}{x} = x^{-1}$, jadi bagian kedua menyumbang pangkat negatif.
- Suku konstan adalah yang jumlah pangkatnya nol. Selesaikan persamaannya untuk mencari sukunya.

## Pembahasan

**Tuliskan bentuk umum sukunya.**

$$\left(x + \frac1x\right)^6 = \sum_{k=0}^{6} \binom{6}{k}\, x^{\,6-k} \left(\frac1x\right)^{k}$$

**Kumpulkan pangkat $x$.** Tulis $\frac1x = x^{-1}$:

$$x^{\,6-k} \cdot x^{-k} = x^{\,6-2k}$$

**Cari yang berpangkat nol.**

$$6 - 2k = 0 \quad\Longrightarrow\quad k = 3$$

**Hitung koefisiennya.**

$$\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = \boxed{20}$$

**Langkah yang menentukan adalah menyatukan pangkatnya lebih dulu.** Tanpa itu, mudah
tergoda mencari $k$ yang membuat $6-k = 0$, yang keliru — pangkat $x$ pada sebuah suku
adalah jumlah sumbangan **kedua** bagian, dan bagian kedua menyumbang pangkat negatif.

**Perhatikan syarat keberadaannya.** Persamaan $6 - 2k = 0$ kebetulan punya penyelesaian
bulat. Kalau pangkatnya ganjil, misalnya $\left(x+\frac1x\right)^{7}$, maka $7-2k = 0$
tidak punya penyelesaian bulat — dan penjabarannya **tidak punya suku konstan sama
sekali**. Memeriksa hal ini bagian dari menjawab, bukan tambahan.

**Bentuk umum yang layak dikenali.** Untuk $\left(x^{a} + x^{-b}\right)^{n}$, pangkat suku
ke-$k$ adalah

$$a(n-k) - bk = an - (a+b)k$$

Suku yang dicari ada tepat ketika $\frac{an - p}{a+b}$ bernilai bulat di antara $0$ dan
$n$, dengan $p$ pangkat yang diminta. Menyelesaikan satu persamaan linear seperti ini
adalah seluruh isi soal jenis ini, betapa pun rumit tampilannya.
