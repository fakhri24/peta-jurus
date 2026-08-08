---
id: kongruensi-linear
nama: Kongruensi Linear
pilar: teori-bilangan
tahap: osn-p
prasyarat: [kongruensi-dasar, bezout]
contoh: [kl-contoh-1]
latihan: [kl-01, kl-02, kl-03, kl-04, kl-05, kl-06]
---

## Kapan dipakai

Soal meminta menyelesaikan $ax \equiv b \pmod m$, atau kamu tiba di bentuk itu di
tengah jalan dan ingin "membagi" kedua ruas.

## Intinya

$ax \equiv b \pmod m$ punya solusi tepat ketika $d = \gcd(a, m)$ membagi $b$. Kalau ada,
solusinya **tepat $d$ buah** yang berbeda modulo $m$.

Kasus yang paling sering: $\gcd(a,m) = 1$. Di situ solusinya tunggal, yaitu
$x \equiv a^{-1} b \pmod m$, dengan $a^{-1}$ dari Bézout.

Inilah jawaban tepat atas pertanyaan "kapan boleh membagi dalam kongruensi": boleh
mengalikan dengan invers, dan invers hanya ada kalau pembaginya relatif prima terhadap
modulusnya. Kalau tidak relatif prima, modulusnya ikut menyusut:

$$ad \equiv bd \pmod m \quad\Longrightarrow\quad a \equiv b \ \left(\bmod \frac{m}{\gcd(d,m)}\right)$$

## Jebakan umum

- **Mencoret faktor bersama tanpa mengecilkan modulusnya.** Dari $2x \equiv 4 \pmod 6$
  bukan $x \equiv 2 \pmod 6$, melainkan $x \equiv 2 \pmod 3$ — yang berarti dua solusi
  modulo $6$, yaitu $2$ dan $5$.
- **Menjawab satu solusi padahal ada $d$.** Kalau soal menanyakan "berapa banyak $x$",
  cacahnya persis $\gcd(a,m)$.
- **Mencari invers padahal tidak ada.** Periksa $\gcd(a,m) = 1$ lebih dulu.
