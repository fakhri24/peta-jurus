---
id: uji-keterbagian
nama: Uji Keterbagian & Digit
pilar: teori-bilangan
tahap: osn-k
prasyarat: [kongruensi-dasar]
contoh: [uk-contoh-1]
latihan: [uk-01, uk-02, uk-03, uk-04, uk-05, uk-06]
---

## Kapan dipakai

Soal berbicara tentang **angka penyusun** bilangan: jumlah digit, digit terakhir, membalik
urutan digit, atau mencari digit yang hilang. Ciri paling terang: bilangannya ditulis
sebagai $\overline{ab}$ atau $\overline{abc}$, bukan sebagai satu huruf.

Pemicu kedua: soal menuntut **digit terakhir dari bilangan berpangkat besar** — angka satuan
$7^{2026}$. Itu pertanyaan modulo $10$, dan jawabannya selalu berputar dengan periode
pendek.

Pemicu ketiga: soal **membalik atau memindahkan digit** dan membandingkan hasilnya dengan
bilangan asalnya. Menulis keduanya lewat $\sum d_i 10^i$ mengubah kalimat tentang digit
menjadi persamaan biasa, dan selisihnya hampir selalu memuat faktor $9$ atau $11$.

Pemicu keempat: soal menyebut **palindrom**, atau bilangan yang seluruh digitnya sama —
$\underbrace{11\ldots1}_{n}$. Bentuk berulang seperti itu punya penulisan tertutup yang jauh
lebih mudah dikerjakan daripada digitnya satu per satu.

Yang menyatukan keempatnya satu baris: $N = \sum_i d_i \cdot 10^i$. Setiap uji keterbagian
lahir dari melihat $10^i$ modulo sesuatu, jadi menghafal ujinya kurang berguna daripada
mengingat asalnya.

## Intinya

Kuncinya satu baris. Bilangan dengan digit $d_k \dots d_1 d_0$ bernilai

$$N = \sum_{i} d_i \cdot 10^i$$

Semua uji keterbagian lahir dari melihat $10^i$ modulo sesuatu:

- $10 \equiv 1 \pmod 9$, jadi $N \equiv$ jumlah digitnya $\pmod 9$. Hal yang sama berlaku
  modulo $3$.
- $10 \equiv -1 \pmod{11}$, jadi $N \equiv$ jumlah digit berselang-seling $\pmod{11}$.
- $10^3 = 1000 \equiv 1 \pmod{37}$, jadi digit yang dikelompokkan tiga-tiga bekerja untuk $37$.
- $2^k \mid 10^k$, jadi keterbagian oleh $8$ hanya bergantung pada tiga digit terakhir.

Satu fakta turunan yang sering menutup soal: **sebuah bilangan dan jumlah digitnya selalu
kongruen modulo $9$.** Karena itu keduanya punya sisa yang sama — dan itu memasung
kemungkinan yang harus diperiksa.

## Jebakan umum

- **Mengira digit boleh bernilai berapa pun.** Digit selalu $0$–$9$, dan digit terdepan
  tidak boleh $0$. Batas ini biasanya justru yang menyelesaikan soalnya.
- **Menghitung jumlah digit terus-menerus tanpa alasan.** Yang lestari adalah sisanya
  modulo $9$, bukan jumlah digitnya sendiri.
- **Lupa banyaknya digit ikut dibatasi.** Bilangan tiga digit ada di antara $100$ dan
  $999$ — dua kurungan yang sering menghabiskan kasus.
