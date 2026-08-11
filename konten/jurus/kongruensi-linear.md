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

Soal meminta menyelesaikan **$ax \equiv b \pmod m$** — atau kamu tiba di bentuk itu di
tengah jalan dan ingin "membagi" kedua ruas.

Pemicu kedua, dan justru yang paling sering: **keinginan membagi dalam kongruensi.** Begitu
muncul dorongan mencoret faktor yang sama di kedua ruas, berhentilah — di sinilah
pertanyaan itu dijawab. Boleh mengalikan dengan invers, dan invers hanya ada kalau
pembaginya relatif prima terhadap modulusnya.

Pemicu ketiga: soal menanyakan **berapa banyak** penyelesaian, bukan penyelesaiannya.
Jawabannya $\gcd(a,m)$ kalau ia membagi $b$, dan nol kalau tidak — tanpa satu pun
penyelesaian perlu dicari.

Pemicu keempat: soal mencari **invers** sebuah bilangan modulo $m$, sering tanpa menyebutnya
begitu — "tentukan $x$ dengan $7x \equiv 1 \pmod{30}$".

Bedakan dari Persamaan Diophantine Linear: satu peubah dengan modulo di sini, dua peubah
tanpa modulo di sana. Isinya teorema yang sama, ditulis dua cara.

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
