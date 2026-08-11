---
id: grd-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: uraian
kesulitan: 3
---

## Soal

Dalam sebuah kelompok yang terdiri atas $5$ orang, mungkinkah setiap orang berkenalan dengan
**tepat $3$** orang lainnya di dalam kelompok itu?

(Perkenalan bersifat timbal balik: kalau $A$ kenal $B$, maka $B$ kenal $A$.)

Buktikan jawabanmu.

## Petunjuk

- Perkenalannya timbal balik, jadi satu perkenalan tercatat pada dua orang sekaligus. Jumlahkan hitungan kenalan seluruh orang dan lihat apa arti angkanya.
- Gambarkan sebagai graf: orang menjadi titik, perkenalan menjadi ruas. Jumlah derajat seluruh titik sama dengan dua kali banyaknya ruas.
- Banyaknya ruas wajib bilangan bulat. Periksa apakah syarat itu terpenuhi.

## Pembahasan

**Terjemahkan ke graf.** Buat graf $G$ dengan $5$ titik, satu untuk tiap orang, dan pasang
ruas di antara dua titik tepat ketika keduanya saling kenal. Perkenalan yang timbal balik
membuat ruasnya tidak berarah — persis graf biasa.

Syarat soal menjadi: **setiap titik berderajat $3$**.

**Jumlahkan derajatnya.**

$$\sum_v \deg(v) = 5 \times 3 = 15$$

**Terapkan lema jabat tangan.** Menjumlahkan derajat berarti mencacah tiap ruas dua kali,
sekali dari masing-masing ujungnya:

$$\sum_v \deg(v) = 2|E|$$

Maka

$$2|E| = 15 \quad\Longrightarrow\quad |E| = \frac{15}{2} = 7{,}5$$

**Simpulkan.** Banyaknya ruas wajib bilangan bulat, sedangkan $7{,}5$ bukan. Karena itu
graf semacam itu tidak ada, dan kelompok seperti yang digambarkan soal **tidak mungkin**
ada. $\blacksquare$

### Bentuk yang lebih langsung

Kesimpulan yang sama bisa dinyatakan lewat akibat lema jabat tangan: **banyaknya titik
berderajat ganjil selalu genap.**

Di sini seluruh $5$ titik berderajat $3$, yang ganjil — jadi ada $5$ titik berderajat
ganjil, dan $5$ bilangan ganjil. Bertentangan.

### Mengapa mencoba menggambar bukan bukti

Mencoba beberapa susunan lalu gagal tidak membuktikan apa pun — mungkin susunan yang benar
belum ditemukan. Yang membuktikan adalah satu persamaan yang menutup **seluruh**
kemungkinan sekaligus, tanpa memeriksa satu susunan pun.

### Kapan keadaan semacam ini mungkin

Syarat perlunya adalah $n \times k$ genap, dengan $n$ banyaknya orang dan $k$ banyaknya
kenalan tiap orang. Jadi:

| $n$ | $k$ | $nk$ | Mungkin? |
|---|---|---|---|
| $5$ | $3$ | $15$ | tidak — ganjil |
| $6$ | $3$ | $18$ | ya |
| $5$ | $4$ | $20$ | ya |
| $5$ | $2$ | $10$ | ya |

Untuk $n = 6$ dan $k = 3$, susunannya memang ada — misalnya enam orang duduk melingkar,
masing-masing kenal kedua tetangganya dan orang di seberangnya.

**Perhatikan syarat $nk$ genap adalah syarat perlu, bukan syarat cukup.** Ia juga menuntut
$k \le n-1$, sebab tidak ada yang bisa berkenalan dengan lebih banyak orang daripada yang
ada. Untuk kedua syarat itu terpenuhi bersamaan, susunannya selalu ada — tetapi menunjukkan
hal itu memerlukan konstruksi, bukan sekadar hitungan.

## Rubrik

- Menerjemahkan soal ke graf: orang sebagai titik, perkenalan sebagai ruas
- Menyatakan syarat soal sebagai "tiap titik berderajat $3$"
- Menghitung jumlah derajat $5 \times 3 = 15$
- Menyatakan lema jabat tangan $\sum \deg(v) = 2|E|$, dengan alasan tiap ruas terhitung dua kali
- Menyimpulkan $|E| = 7{,}5$ bukan bilangan bulat, sehingga graf itu tidak ada
- Menyatakan dengan jelas bahwa kesimpulannya ketidakmungkinan, bukan sekadar kegagalan mencoba
