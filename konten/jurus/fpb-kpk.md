---
id: fpb-kpk
nama: FPB & KPK
pilar: teori-bilangan
tahap: osn-k
prasyarat: [algoritma-pembagian, bilangan-prima]
contoh: [fk-contoh-1]
latihan: [fk-01, fk-02, fk-03, fk-04, fk-05, fk-06]
---

## Kapan dipakai

Soal menyebut **faktor persekutuan terbesar (FPB)**, **kelipatan persekutuan terkecil (KPK)**, pecahan paling sederhana, atau kata **relatif prima** / *saling asing*.

Pemicu kedua: soal memberikan nilai $\gcd(a, b)$ dan $\operatorname{lcm}(a, b)$ sekaligus, atau hubungan antara keduanya. Pemisalan $a = gx$ dan $b = gy$ dengan $\gcd(x, y) = 1$ langsung mengubah soal menjadi aljabar yang jauh lebih sederhana.

Pemicu ketiga: soal menanyakan FPB dari dua bilangan yang bergantung pada $n$, seperti $\gcd(2n+1, 3n+2)$. Sifat $\gcd(a, b) = \gcd(a, b - ka)$ dipakai untuk mengeliminasi $n$.

Pemicu keempat: soal meminta membuktikan pecahan $\frac{A(n)}{B(n)}$ **tak dapat disederhanakan** untuk semua $n$. Ini sama saja dengan membuktikan $\gcd(A(n), B(n)) = 1$.

Pemicu kelima: hubungan dasar $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = ab$ yang dipakai untuk menukar bentuk perkalian dengan bentuk persekutuan.

## Intinya

Lewat faktorisasi prima, dengan $\gcd$ mengambil pangkat terkecil dan $\operatorname{lcm}$
pangkat terbesar:

$$\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$$

Rumus ini sering jadi jalan pintas: kalau soal memberi $\gcd$ dan $\operatorname{lcm}$,
kamu langsung tahu hasil kalinya.

Dua bilangan disebut **relatif prima** kalau $\gcd(a,b) = 1$. Ini syarat yang muncul
di mana-mana, dan gunanya satu: **memisahkan**. Kalau $\gcd(m,n) = 1$ dan keduanya
membagi $N$, maka $mn \mid N$. Tanpa syarat relatif prima, kesimpulan itu palsu —
$4 \mid 12$ dan $6 \mid 12$ tapi $24 \nmid 12$.

Trik yang sering menolong: tulis $a = d\alpha$, $b = d\beta$ dengan $d = \gcd(a,b)$ dan
$\gcd(\alpha, \beta) = 1$. Soal yang tadinya berantakan biasanya langsung rapi.

## Jebakan umum

- **Memakai "$m \mid N$ dan $n \mid N$ berarti $mn \mid N$" tanpa memeriksa
  $\gcd(m,n) = 1$.** Ini kesalahan paling sering di seluruh teori bilangan tingkat awal.
- **Mengira $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$ berlaku untuk tiga bilangan.**
  Tidak. Untuk tiga bilangan rumusnya lain sama sekali.
- **Lupa $\gcd(a, 0) = a$.** Muncul sebagai kasus batas di algoritma Euklid.
