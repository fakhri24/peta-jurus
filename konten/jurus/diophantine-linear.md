---
id: diophantine-linear
nama: Persamaan Diophantine Linear
pilar: teori-bilangan
tahap: osn-p
prasyarat: [bezout]
contoh: [dl-contoh-1]
latihan: [dl-01, dl-02, dl-03, dl-04, dl-05, dl-06]
---

## Kapan dipakai

Soal berbentuk **$ax + by = c$ dengan $x, y$ diminta bulat**. Jarang ditulis setelanjang
itu — biasanya berbaju cerita: uang pecahan, jumlah hewan, banyak kursi, kombinasi perangko.

Pemicu kedua, yang paling sering menjadi isi soalnya: pertanyaannya bukan "berapa $x$"
melainkan **"ada berapa pasangan"** atau **"adakah"**. Keduanya dijawab tanpa mencari
solusinya satu per satu — yang pertama dengan menghitung $t$ yang membuat kedua peubah
tetap memenuhi syarat soal, yang kedua cukup dengan memeriksa $\gcd(a,b) \mid c$.

Pemicu ketiga: soal menambahkan **syarat tanda atau batas** — $x, y$ tak negatif, atau
kurang dari suatu bilangan. Syarat itu memotong deret solusi yang tak hingga menjadi
hingga, dan biasanya di situlah jawabannya.

Bedakan dari Kongruensi Linear: dua peubah dan satu persamaan itu jurus ini; satu peubah
dengan modulo itu yang sana. Keduanya bersaudara — $ax \equiv b \pmod m$ hanyalah
$ax + my = b$ yang ditulis lain.

## Intinya

$ax + by = c$ punya solusi bulat **tepat ketika** $d = \gcd(a,b)$ membagi $c$.

Kalau ada, seluruh solusinya adalah

$$x = x_0 + \frac{b}{d}t, \qquad y = y_0 - \frac{a}{d}t, \qquad t \in \mathbb{Z}$$

dengan $(x_0, y_0)$ satu solusi apa pun yang berhasil kamu temukan.

Tiga langkah yang selalu sama:

1. Hitung $d = \gcd(a,b)$ dan periksa $d \mid c$. Kalau tidak, jawabannya "tidak ada".
2. Cari satu solusi — lewat Bézout, atau sering cukup dengan mencoba nilai kecil.
3. Tulis keluarga solusinya, lalu terapkan batasan soal (biasanya $x, y > 0$) untuk
   memangkas $t$ menjadi rentang berhingga.

Langkah ketiga itu yang biasanya menjadi seluruh isi soal olimpiade: bukan mencari solusi,
tapi **mencacah berapa banyak** yang memenuhi syarat tambahan.

## Jebakan umum

- **Melupakan syarat $d \mid c$** lalu menghabiskan waktu mencari solusi yang tidak ada.
- **Salah tanda pada keluarga solusi.** $x$ bertambah $b/d$ sementara $y$ **berkurang**
  $a/d$. Cek dengan mensubstitusi balik satu nilai $t$.
- **Lupa "bilangan asli" berarti positif.** Batas $x \ge 1$, bukan $x \ge 0$, dan itu
  sering mengubah cacahnya tepat satu.
