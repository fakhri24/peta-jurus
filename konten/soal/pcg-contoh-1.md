---
id: pcg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: uraian
kesulitan: 3
---

## Soal

Dalam sebuah pertemuan, beberapa orang saling berjabat tangan. Sebut $d_i$ banyaknya orang
yang dijabat tangan oleh orang ke-$i$.

Buktikan bahwa

$$\sum_{i} d_i = 2J$$

dengan $J$ banyaknya jabat tangan yang terjadi. Simpulkan bahwa banyaknya orang yang
berjabat tangan dengan **ganjil** banyak orang selalu genap.

## Petunjuk

- Nyatakan lebih dulu apa yang akan dicacah. Bukan orang, dan bukan jabat tangan — melainkan sesuatu yang memuat keduanya.
- Tinjau pasangan $(\text{orang},\ \text{jabat tangan yang ia ikuti})$, lalu hitung banyaknya pasangan itu dengan dua cara.
- Untuk kesimpulan terakhir, pisahkan penjumlahan menjadi suku ganjil dan suku genap.

## Pembahasan

**Nyatakan apa yang dicacah.** Tinjau himpunan

$$T = \{(p, j) : p \text{ seorang peserta},\ j \text{ sebuah jabat tangan yang diikuti } p\}$$

Menyatakan $T$ dengan jelas adalah langkah yang menentukan; setelah itu kedua cara
menghitungnya muncul sendiri.

**Cara A — hitung per orang.** Untuk tiap orang $i$, banyaknya jabat tangan yang ia ikuti
adalah $d_i$. Menjumlahkan atas semua orang:

$$|T| = \sum_i d_i$$

**Cara B — hitung per jabat tangan.** Tiap jabat tangan melibatkan tepat **dua** orang,
sehingga ia menyumbang tepat dua pasangan ke $T$. Menjumlahkan atas semua jabat tangan:

$$|T| = 2J$$

**Kedua cara mencacah himpunan yang sama.** Karena itu

$$\sum_i d_i = 2J \qquad \blacksquare$$

### Akibatnya

Ruas kanan adalah bilangan **genap**, jadi $\sum_i d_i$ genap. Pisahkan penjumlahannya:

$$\sum_{d_i \text{ genap}} d_i \ + \ \sum_{d_i \text{ ganjil}} d_i \ = \ 2J$$

Jumlah pertama genap, sebab tiap sukunya genap. Karena seluruhnya genap, jumlah kedua juga
harus genap.

Jumlah kedua terdiri atas suku-suku ganjil. Jumlah beberapa bilangan ganjil bernilai genap
tepat ketika **banyaknya suku genap**. Maka banyaknya orang dengan $d_i$ ganjil adalah
bilangan genap. $\blacksquare$

### Mengapa cara ini disebut pencacahan ganda

Tidak ada rumus yang dihafal dan tidak ada yang dijabarkan. Yang dikerjakan hanya: pilih
satu himpunan, hitung dari dua sudut, lalu samakan hasilnya. Persamaan yang keluar itulah
jawabannya.

Yang menentukan berhasil tidaknya adalah **pemilihan himpunannya**. Kalau yang dicacah cuma
"orang" atau cuma "jabat tangan", tidak ada dua cara yang berbeda. Himpunan pasangan
$(p, j)$ memuat keduanya sekaligus, dan itu yang membuat dua sudut pandang mungkin.

Bentuk ini akan muncul terus: himpunan yang berguna hampir selalu berupa **pasangan** yang
memenuhi suatu hubungan — siswa dan klub yang diikutinya, titik dan garis yang melewatinya,
baris dan kolom pada sebuah tabel.

### Akibat praktisnya

Karena $\sum_i d_i$ selalu genap, mustahil ada pertemuan lima orang yang setiap orangnya
berjabat tangan dengan tepat tiga orang lain — sebab jumlah derajatnya $15$, ganjil. Satu
persamaan sederhana menutup seluruh kemungkinan tanpa perlu mencoba satu pun susunan.

## Rubrik

- Menyatakan dengan jelas himpunan yang dicacah, yaitu pasangan orang dan jabat tangan yang diikutinya
- Cara A: menghitung $|T| = \sum_i d_i$ dengan alasan tiap orang menyumbang $d_i$ pasangan
- Cara B: menghitung $|T| = 2J$ dengan alasan tiap jabat tangan melibatkan tepat dua orang
- Menyimpulkan kedua hitungan sama karena mencacah himpunan yang sama
- Memisahkan penjumlahan menjadi suku genap dan suku ganjil
- Menyimpulkan jumlah suku ganjilnya genap, sehingga banyaknya suku ganjil genap
