---
id: grd-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: isian
kesulitan: 3
jawaban: "16"
---

## Soal

Sebuah graf memiliki $9$ titik dan setiap titiknya berderajat $3$ atau $4$. Diketahui ada
tepat $5$ titik yang berderajat $4$.

Ada berapa ruas pada graf itu?

## Petunjuk

- Hitung dulu ada berapa titik berderajat $3$, lalu jumlahkan seluruh derajatnya.
- Jumlah derajat sama dengan dua kali banyaknya ruas.
- Periksa hasilnya bilangan bulat, dan periksa juga banyaknya titik berderajat ganjil.

## Pembahasan

**Bagi titiknya.** Ada $5$ titik berderajat $4$, sehingga sisanya

$$9 - 5 = 4 \text{ titik berderajat } 3$$

**Jumlahkan derajatnya.**

$$\sum_v \deg(v) = 5 \times 4 + 4 \times 3 = 20 + 12 = 32$$

**Terapkan lema jabat tangan.**

$$2|E| = 32 \quad\Longrightarrow\quad |E| = \boxed{16}$$

**Periksa dengan akibat lema itu.** Titik berderajat ganjil adalah yang berderajat $3$, dan
ada $4$ di antaranya — bilangan genap, sesuai keharusan. Kalau soalnya menyebut $5$ titik
berderajat $3$ dan $4$ titik berderajat $4$, jumlah derajatnya

$$5 \times 3 + 4 \times 4 = 31$$

ganjil, sehingga graf semacam itu **mustahil** — dan itu langsung terbaca dari banyaknya
titik berderajat ganjil yang tidak genap.

**Periksa juga batas atasnya.** Dengan $9$ titik, ruas paling banyak $\binom92 = 36$. Karena
$16 \le 36$, tidak ada yang bertentangan. Derajat terbesar pada soal adalah $4$, dan itu
tidak melebihi $9 - 1 = 8$. Cocok.

**Tiga pemeriksaan yang layak jadi kebiasaan** setiap kali soal memberi daftar derajat:

1. Jumlah derajatnya genap.
2. Banyaknya titik berderajat ganjil genap. (Sebenarnya setara dengan yang pertama, tetapi
   sering lebih cepat dilihat.)
3. Tiap derajat tidak melebihi $n-1$.

Ketiganya syarat **perlu**. Kalau salah satunya gagal, susunannya mustahil dan soal selesai
tanpa menggambar apa pun. Kalau seluruhnya lolos, graf semacam itu biasanya ada — tetapi
menunjukkannya menuntut konstruksi.
