---
id: tsf-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Ada berapa akar rasional dari persamaan

$$2x^3 - 3x^2 - 3x + 2 = 0\ ?$$

## Petunjuk

- Kandidat akar rasional pada polinomial berkoefisien bulat bisa disaring lebih dulu — jumlahnya berhingga.
- Kalau $\frac{p}{q}$ akar dalam bentuk paling sederhana, maka $p$ membagi konstanta dan $q$ membagi koefisien utama.
- Di sini konstantanya $2$ dan koefisien utamanya $2$, jadi kandidatnya sedikit.

## Pembahasan

**Saring kandidatnya.** Untuk polinomial berkoefisien bulat, kalau $\frac{p}{q}$ akar
dalam bentuk paling sederhana, maka

$$p \mid a_0 = 2, \qquad q \mid a_n = 2$$

Jadi $p \in \{\pm1, \pm2\}$ dan $q \in \{1, 2\}$, memberi kandidat

$$\pm 1, \qquad \pm 2, \qquad \pm \tfrac12$$

Enam kandidat saja — dari tak hingga banyak bilangan rasional.

**Uji satu per satu** dengan teorema faktor.

$$P(1) = 2 - 3 - 3 + 2 = -2 \ne 0$$
$$P(-1) = -2 - 3 + 3 + 2 = 0 \quad \checkmark$$
$$P(2) = 16 - 12 - 6 + 2 = 0 \quad \checkmark$$
$$P\!\left(\tfrac12\right) = 2 \cdot \tfrac18 - 3 \cdot \tfrac14 - \tfrac32 + 2
= \tfrac14 - \tfrac34 - \tfrac32 + 2 = 0 \quad \checkmark$$

Tiga akar ditemukan: $-1$, $2$, dan $\frac12$. Karena derajatnya $3$, tidak mungkin ada
akar keempat — jadi kandidat sisanya tidak perlu diuji.

Ada $\boxed{3}$ akar rasional.

Periksa lewat pemfaktoran:

$$2x^3-3x^2-3x+2 = (x+1)(x-2)(2x-1)$$

Jabarkan sebagian untuk memastikan: $(x+1)(x-2) = x^2-x-2$, lalu dikali $(2x-1)$ memberi
$2x^3-2x^2-4x-x^2+x+2 = 2x^3-3x^2-3x+2$. Cocok.

Periksa juga lewat Vieta: hasil kali akarnya harus $-\frac{a_0}{a_n} = -1$, dan memang
$(-1)(2)\left(\frac12\right) = -1$.

**Aturan akar rasional adalah penyaring, bukan jaminan.** Ia memberi daftar kandidat
berhingga, tetapi tidak menjanjikan satu pun di antaranya benar-benar akar. Polinomial
$x^3 - 2$ misalnya punya kandidat $\pm1, \pm2$ — dan tidak satu pun berhasil, sebab akar
sesungguhnya $\sqrt[3]{2}$ tidak rasional.
