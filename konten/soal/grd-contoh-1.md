---
id: grd-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: isian
kesulitan: 3
jawaban: "30"
---

## Soal

Dalam sebuah jaringan terdapat $15$ kota. Setiap kota terhubung jalan langsung dengan tepat
$4$ kota lainnya.

Ada berapa ruas jalan dalam jaringan itu?

## Petunjuk

- Gambarkan sebagai graf: kota menjadi titik, jalan menjadi ruas. Derajat sebuah titik adalah banyaknya ruas yang menyentuhnya.
- Jumlahkan derajat seluruh titik, lalu tanyakan apa yang sebenarnya dihitung angka itu.
- Tiap ruas punya dua ujung, sehingga ia terhitung dua kali di dalam jumlah tadi.

## Pembahasan

**Terjemahkan ke graf.** Kota menjadi titik, jalan menjadi ruas. Tiap titik berderajat $4$,
dan ada $15$ titik.

**Jumlahkan derajatnya.**

$$\sum_v \deg(v) = 15 \times 4 = 60$$

**Baca angka itu dengan benar.** Angka $60$ bukan banyaknya ruas. Menjumlahkan derajat
berarti mencacah pasangan (titik, ruas yang menyentuhnya) — dan **tiap ruas menyumbang dua
pasangan**, sekali dari masing-masing ujungnya.

**Lema jabat tangan.**

$$\sum_v \deg(v) = 2|E| \quad\Longrightarrow\quad 60 = 2|E| \quad\Longrightarrow\quad
|E| = \boxed{30}$$

**Periksa keadaannya memang mungkin.** Jumlah derajat $60$ genap, sehingga tidak ada yang
bertentangan. Kalau soalnya menyebut $15$ kota yang masing-masing terhubung ke tepat $3$
kota, jumlah derajatnya $45$ — ganjil — sehingga $|E| = 22{,}5$ dan jaringan seperti itu
**mustahil**.

Pemeriksaan itu murah dan sering menjadi seluruh isi soal olimpiade: yang ditanyakan bukan
berapa banyak, melainkan apakah susunannya bisa ada.

**Akibat yang selalu ikut.** Karena $\sum_v \deg(v)$ selalu genap, banyaknya titik yang
**berderajat ganjil** selalu genap. Bukti singkatnya: pisahkan penjumlahan menjadi suku
genap dan suku ganjil; yang pertama genap, sehingga yang kedua juga harus genap — dan jumlah
beberapa bilangan ganjil genap tepat ketika banyaknya suku genap.

**Periksa juga apakah jumlahnya masuk akal.** Dengan $15$ titik, ruas paling banyak adalah
$\binom{15}{2} = 105$. Karena $30 \le 105$, tidak ada yang bertentangan. Kalau hitungannya
menuntut lebih banyak ruas daripada yang mungkin, susunannya juga mustahil — kecuali ruas
ganda diizinkan.
