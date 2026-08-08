---
id: polinomial-bulat
nama: Polinomial Berkoefisien Bulat
pilar: aljabar
tahap: osn
prasyarat: [suku-banyak, keterbagian]
contoh: []
latihan: []
---

## Kapan dipakai

Polinomial dengan koefisien bulat, dan soal berbicara tentang **keterbagian** atau nilai
bulat — misalnya "buktikan $P(n)$ tidak pernah prima" atau "tentukan semua $n$ bulat
dengan $P(n)$ kuadrat sempurna".

## Intinya

Satu sifat yang menjadi seluruh isi jurus ini:

$$(a - b) \ \big|\ \left(P(a) - P(b)\right) \qquad \text{untuk } a, b \text{ bulat}$$

Alasannya dari faktorisasi $a^k - b^k = (a-b)\left(a^{k-1} + \cdots + b^{k-1}\right)$ pada
tiap suku, lalu dijumlahkan.

Akibat yang paling sering dipakai:

- Kalau $P(a) = P(b)$ untuk $a \ne b$, maka nilai-nilainya berulang dengan periode yang
  dibatasi $a - b$.
- $P(n) \bmod m$ hanya bergantung pada $n \bmod m$. Jadi memeriksa $m$ nilai sudah
  menutup seluruh bilangan bulat.
- Kalau $P(n)$ selalu prima untuk semua $n$, ambil $p = P(0)$; maka $p \mid P(kp)$ untuk
  setiap $k$, sehingga $P(kp)$ hanya bisa $\pm p$ — dan polinomial tak konstan tidak bisa
  bernilai sama berkali-kali.

**Akar rasional.** Kalau $\frac{p}{q}$ akar $P$ dalam bentuk paling sederhana, maka
$p \mid a_0$ dan $q \mid a_n$. Untuk polinomial monik berkoefisien bulat, akibatnya tajam:
akar rasionalnya pasti bulat dan pasti membagi konstanta.

Inilah jurus aljabar pertama yang berprasyarat lintas bidang — pemicunya aljabar, tetapi
alat kerjanya keterbagian.

## Jebakan umum

- **Memakai sifat $(a-b) \mid (P(a)-P(b))$ untuk $a, b$ tak bulat.** Ia menuntut keduanya
  bulat.
- **Lupa koefisiennya harus bulat.** Untuk koefisien rasional, sifatnya gugur.
- **Mengira akar rasional pasti bulat** pada polinomial tak monik. Yang bulat hanya kalau
  koefisien utamanya $1$ atau $-1$.
