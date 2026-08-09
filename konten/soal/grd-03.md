---
id: grd-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: isian
kesulitan: 2
jawaban: "19"
---

## Soal

Sebuah jaringan komputer terdiri atas $20$ komputer. Jaringan itu **terhubung** — setiap dua
komputer dapat saling berkirim pesan, langsung atau lewat komputer lain — dan tidak memuat
**siklus**, yaitu tidak ada rangkaian sambungan yang berputar kembali ke titik awal.

Ada berapa kabel yang menghubungkan komputer-komputer itu?

## Petunjuk

- Graf yang terhubung dan tidak memuat siklus punya nama sendiri, dan banyaknya ruasnya selalu tertentu.
- Bangun grafnya bertahap: mulai dari satu titik, lalu tambahkan titik satu per satu.
- Tiap titik yang ditambahkan membawa berapa ruas, kalau grafnya harus tetap terhubung dan tetap tanpa siklus?

## Pembahasan

**Kenali bangunnya.** Graf yang terhubung dan tidak memuat siklus disebut **pohon**.

**Bangun bertahap.** Mulai dari satu titik, tanpa ruas. Tambahkan titik satu per satu, dan
perhatikan tiap titik baru:

- Ia harus membawa **paling sedikit satu** ruas, sebab kalau tidak, ia terputus dan grafnya
  tidak lagi terhubung.
- Ia tidak boleh membawa **dua atau lebih** ruas ke bagian yang sudah ada, sebab dua jalur
  menuju bagian yang sama akan menutup sebuah siklus.

Jadi tiap titik baru membawa **tepat satu** ruas. Setelah titik pertama, ada $20 - 1 = 19$
titik yang ditambahkan:

$$|E| = \boxed{19}$$

**Rumus umumnya:** pohon dengan $n$ titik punya tepat $n-1$ ruas.

**Periksa dengan lema jabat tangan.** Jumlah derajatnya $2 \times 19 = 38$, tersebar pada
$20$ titik — jadi rata-rata derajatnya $1{,}9$, sedikit di bawah $2$. Masuk akal untuk
sebuah pohon, yang memang jaringan paling hemat.

**Mengapa angka $n-1$ begitu sering muncul.** Ia adalah batas dari dua arah sekaligus:

- Graf terhubung dengan $n$ titik punya **paling sedikit** $n-1$ ruas.
- Graf tanpa siklus dengan $n$ titik punya **paling banyak** $n-1$ ruas.

Pohon adalah graf yang mencapai kedua batas itu sekaligus — dan itu sebabnya ia sering jadi
kasus ekstrem pada soal olimpiade. Kalimat seperti "jaringan paling hemat yang tetap
terhubung" hampir selalu berarti pohon.

**Akibat praktisnya.** Kalau sebuah jaringan berisi $20$ komputer punya $19$ kabel dan tetap
terhubung, ia pasti pohon — sehingga **memutus satu kabel mana pun** akan memecahnya menjadi
dua bagian yang tidak saling terhubung. Tidak ada kabel cadangan sama sekali, dan itu
konsekuensi langsung dari tidak adanya siklus.
