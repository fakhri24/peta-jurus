---
id: graf-dasar
nama: Graf Dasar
pilar: kombinatorika
tahap: osn-p
prasyarat: [pencacahan-ganda]
contoh: []
latihan: []
---

## Kapan dipakai

Soal berbicara tentang **hubungan berpasangan**: siapa berjabat tangan dengan siapa, kota
mana terhubung jalan, tim mana sudah bertanding melawan tim mana, orang yang saling kenal.
Begitu kamu menggambar titik untuk tiap objek dan ruas untuk tiap hubungan, banyak soal
berubah menjadi soal tentang derajat.

Pemicu lain: soal menyebut "setiap dua di antaranya" atau memberi data berapa hubungan yang
dimiliki tiap objek.

## Intinya

Sebuah graf adalah himpunan titik beserta ruas yang menghubungkan pasangan titik. Derajat
sebuah titik, $\deg(v)$, adalah banyaknya ruas yang menyentuhnya.

**Lema jabat tangan** — pencacahan ganda yang paling sering dipakai:

$$\sum_{v} \deg(v) = 2|E|$$

Menjumlahkan derajat berarti menghitung tiap ruas dua kali, sekali dari masing-masing
ujungnya. Akibat langsungnya sering jadi kunci soal: **banyaknya titik berderajat ganjil
selalu genap.**

Graf lengkap $K_n$, yang tiap dua titiknya terhubung, punya

$$\binom{n}{2} = \frac{n(n-1)}{2}$$

ruas — itu banyaknya jabat tangan kalau semua orang bersalaman sekali.

**Pohon** adalah graf terhubung tanpa siklus. Pohon dengan $n$ titik selalu punya tepat
$n-1$ ruas, dan itu batas yang sering dipakai: graf terhubung tidak mungkin punya ruas
lebih sedikit dari itu.

## Jebakan umum

- **Lupa membagi dua.** Jumlah derajat menghitung tiap ruas dua kali; ia bukan banyaknya
  ruas.
- **Mengira grafnya terhubung.** Soal jarang menjanjikannya, dan graf yang terpecah
  beberapa bagian sering justru kasus yang menentukan.
- **Menganggap gambar sebagai bukti.** Satu gambar hanya menunjukkan satu kemungkinan;
  yang membuktikan adalah alasan tentang derajat atau banyaknya ruas.
