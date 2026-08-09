---
id: pbr-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: uraian
kesulitan: 3
---

## Soal

Misalkan tersedia $n$ benda yang terbagi ke dalam $r$ jenis: $n_1$ benda berjenis pertama,
$n_2$ berjenis kedua, sampai $n_r$ berjenis ke-$r$, dengan

$$n_1 + n_2 + \cdots + n_r = n$$

Benda sejenis tidak dapat dibedakan satu sama lain.

Buktikan bahwa banyaknya susunan berjajar yang berbeda adalah

$$\frac{n!}{n_1!\,n_2!\cdots n_r!}$$

Buktikan dengan **dua cara**: lewat pemberian tanda sementara, dan lewat pemilihan tempat
jenis demi jenis.

## Petunjuk

- Cara pertama: beri nomor sementara pada benda sejenis supaya semuanya bisa dibedakan, hitung susunannya, lalu tentukan berapa kali tiap susunan sungguhan terhitung.
- Cara kedua: pilih tempat untuk jenis pertama, lalu jenis kedua dari tempat yang tersisa, dan seterusnya sampai habis.
- Untuk cara kedua, tunjukkan hasil kali koefisien binomialnya menyusut menjadi bentuk yang diminta.

## Pembahasan

### Cara pertama — beri tanda sementara

Beri nomor pada benda sejenis sehingga seluruh $n$ benda dapat dibedakan. Susunannya
sekarang ada

$$n!$$

Sekarang hapus nomornya, dan tanyakan: **satu susunan sungguhan berasal dari berapa susunan
bernomor?**

Ambil sebuah susunan sungguhan. Tempat mana yang ditempati jenis pertama sudah tertentu;
yang masih bebas hanyalah nomor mana menempati tempat yang mana di antara tempat-tempat
itu, dan ada $n_1!$ cara. Hal yang sama berlaku untuk tiap jenis, dan pilihan antar-jenis
dapat dilakukan bersamaan. Jadi tiap susunan sungguhan berasal dari tepat

$$n_1!\,n_2!\cdots n_r!$$

susunan bernomor.

Karena **setiap** susunan sungguhan punya sama banyaknya salinan, pembagiannya sah:

$$\frac{n!}{n_1!\,n_2!\cdots n_r!} \qquad \blacksquare$$

Syarat "sama banyaknya" itu bukan formalitas. Pembagian hanya boleh dipakai ketika tiap
hasil terhitung dengan kelipatan yang **sama**; kalau sebagian terhitung dua kali dan
sebagian tiga kali, membagi dengan angka tunggal akan salah.

### Cara kedua — pilih tempat jenis demi jenis

Ada $n$ tempat berjajar.

- Pilih $n_1$ tempat untuk jenis pertama: $\dbinom{n}{n_1}$ cara.
- Dari $n - n_1$ tempat sisa, pilih $n_2$ untuk jenis kedua: $\dbinom{n-n_1}{n_2}$ cara.
- Dan seterusnya, sampai jenis terakhir mengisi seluruh tempat yang tersisa.

Hasilnya

$$\binom{n}{n_1}\binom{n-n_1}{n_2}\binom{n-n_1-n_2}{n_3}\cdots$$

Tuliskan tiga faktor pertamanya dengan faktorial:

$$\frac{n!}{n_1!\,(n-n_1)!} \cdot \frac{(n-n_1)!}{n_2!\,(n-n_1-n_2)!}
\cdot \frac{(n-n_1-n_2)!}{n_3!\,\cdots}$$

Penyebut tiap faktor menghapus pembilang faktor berikutnya. Setelah seluruh rantainya
menyusut, yang tersisa

$$\frac{n!}{n_1!\,n_2!\cdots n_r!} \qquad \blacksquare$$

Faktor terakhirnya bernilai $1$, sebab jenis terakhir tidak punya pilihan — seluruh tempat
sisa memang miliknya.

### Perbandingan kedua cara

Cara pertama lebih cepat ditulis, tetapi bertumpu pada langkah yang harus dijaga: bahwa tiap
susunan punya jumlah salinan yang sama.

Cara kedua tidak pernah menghitung apa pun dua kali, jadi tidak perlu pembenaran itu. Ia
juga langsung memperlihatkan mengapa rumus ini dan koefisien binomial adalah kerabat: untuk
$r = 2$, hasilnya persis $\binom{n}{n_1}$.

## Rubrik

- Cara pertama: menyatakan pemberian tanda sementara dan menghitung $n!$ susunan bernomor
- Cara pertama: menghitung banyaknya susunan bernomor yang memberi satu susunan sungguhan sebagai $n_1!\cdots n_r!$
- Cara pertama: menyebut bahwa jumlah salinan itu **sama** untuk tiap susunan, sebagai alasan sahnya pembagian
- Cara kedua: menuliskan hasil kali koefisien binomial dengan batas yang benar di tiap langkah
- Cara kedua: memperlihatkan penghapusan faktorial antar-faktor
- Menyimpulkan kedua cara memberi bentuk yang sama
