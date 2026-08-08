---
id: fungsi-euler
nama: Fungsi Euler & Teorema Euler
pilar: teori-bilangan
tahap: osn-p
prasyarat: [fermat-kecil, fpb-kpk]
contoh: [fe-contoh-1]
latihan: [fe-01, fe-02, fe-03, fe-04, fe-05, fe-06]
---

## Kapan dipakai

Pangkat besar dengan **modulus komposit** — persis situasi ketika Fermat Kecil tidak bisa
dipakai. Juga saat soal mencacah bilangan yang relatif prima terhadap sesuatu.

## Intinya

$\varphi(n)$ adalah banyaknya bilangan di $\{1, \dots, n\}$ yang relatif prima terhadap
$n$. Dari faktorisasi prima:

$$\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

Contohnya $\varphi(12) = 12 \cdot \frac12 \cdot \frac23 = 4$, yaitu $\{1, 5, 7, 11\}$.

**Teorema Euler.** Kalau $\gcd(a, n) = 1$:

$$a^{\varphi(n)} \equiv 1 \pmod n$$

Ini perumuman Fermat Kecil — untuk $n = p$ prima, $\varphi(p) = p - 1$ dan keduanya
berimpit. Pemakaiannya juga sama: eksponen dipotong modulo $\varphi(n)$.

$\varphi$ bersifat **multiplikatif**: $\varphi(mn) = \varphi(m)\varphi(n)$ asalkan
$\gcd(m,n) = 1$. Sifat ini yang membuat menghitungnya cepat.

## Jebakan umum

- **Melupakan syarat $\gcd(a,n) = 1$.** Tanpa itu teoremanya batal. Untuk $a$ yang berbagi
  faktor dengan $n$, pecah dulu dengan Teorema Sisa Cina.
- **Mengira $\varphi$ multiplikatif tanpa syarat.** $\varphi(4) = 2$ tapi
  $\varphi(2)\varphi(2) = 1$. Syarat relatif prima itu wajib.
- **Memakai $\varphi(n)$ padahal ada eksponen yang lebih kecil.** $\varphi(n)$ selalu
  bekerja, tapi belum tentu yang terkecil — yang terkecil adalah orde elemennya.
