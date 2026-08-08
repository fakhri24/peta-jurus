---
id: algoritma-euklid
nama: Algoritma Euklid
pilar: teori-bilangan
tahap: osn-k
prasyarat: [fpb-kpk]
contoh: [ae-contoh-1]
latihan: [ae-01, ae-02]
---

## Kapan dipakai

Kamu perlu $\gcd$ dari bilangan yang terlalu besar untuk difaktorkan — atau, jauh lebih
sering di olimpiade, kamu perlu $\gcd$ dari dua **bentuk aljabar** seperti
$\gcd(n+1,\, n^2+3)$.

## Intinya

$$\gcd(a, b) = \gcd(b,\ a \bmod b)$$

Ulangi sampai sisanya nol; yang tersisa itulah FPB-nya. Tidak perlu memfaktorkan apa pun.

Untuk olimpiade, bentuk yang paling berguna adalah versi selisihnya:

$$\gcd(a, b) = \gcd(a - b,\ b)$$

Karena setiap pembagi bersama $a$ dan $b$ juga membagi selisihnya. Inilah alat untuk
menjinakkan $\gcd$ berbentuk aljabar: kurangi kelipatan yang pas sampai variabelnya
lenyap dan tinggal konstanta.

> Contoh alurnya: $\gcd(n+1,\, n^2+3)$. Karena $n^2 + 3 = (n+1)(n-1) + 4$, maka
> $\gcd(n+1,\, n^2+3) = \gcd(n+1,\, 4)$ — dan sisanya tinggal memeriksa $n+1$ modulo $4$.

## Jebakan umum

- **Berhenti terlalu cepat.** Hasilnya adalah sisa **tak nol yang terakhir**, bukan sisa
  nol.
- **Lupa bahwa hasilnya masih bersyarat.** $\gcd(n+1, 4)$ belum satu angka — nilainya
  $1$, $2$, atau $4$ tergantung $n$. Soal biasanya menanyakan tepat pada percabangan ini.
- **Mengurangi kelipatan yang tidak menghabiskan variabel.** Pilih pengalinya supaya
  suku berpangkat tertinggi benar-benar hilang.
