---
id: koefisien-binomial
nama: Koefisien Binomial dan Identitasnya
pilar: kombinatorika
tahap: osn-k
prasyarat: [kombinasi]
contoh: []
latihan: []
---

## Kapan dipakai

Bentuk $(x+y)^n$ perlu dijabarkan atau satu sukunya dicari, atau soal memuat jumlah
$\binom{n}{k}$ yang polanya harus dikenali. Pemicu lain: soal meminta koefisien suku
tertentu, atau suku yang tidak memuat peubah sama sekali.

## Intinya

$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^{k}$$

Alasannya pencacahan: menjabarkan berarti memilih $x$ atau $y$ dari tiap-tiap $n$ kurung,
dan $\binom{n}{k}$ menghitung berapa cara memilih $y$ sebanyak $k$ kali.

**Aturan Pascal**, yang membangun segitiganya:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

Bacanya: satu objek tertentu ikut terpilih, atau tidak.

Dua jumlah yang harus langsung dikenali:

$$\sum_{k=0}^{n} \binom{n}{k} = 2^{n}, \qquad \sum_{k=0}^{n} (-1)^{k} \binom{n}{k} = 0 \quad (n \ge 1)$$

Yang pertama menghitung seluruh himpunan bagian; yang kedua mengatakan himpunan bagian
berukuran genap dan ganjil sama banyak.

**Identitas Vandermonde**, untuk jumlah hasil kali dua koefisien:

$$\sum_{k} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$$

Tiap identitas di atas punya bacaan pencacahan, dan bacaan itulah yang membuatnya bisa
diingat tanpa dihafal.

## Jebakan umum

- **Tertukar pangkat $x$ dan $y$.** Pada suku dengan $\binom{n}{k}$, pangkat $y$ yang $k$.
- **Salah menomori suku.** "Suku ke-$r$" berarti $k = r-1$, karena penjumlahannya mulai
  dari $k = 0$.
- **Lupa tanda pada $(x-y)^n$.** Sukunya membawa $(-1)^k$, jadi berselang-seling.
