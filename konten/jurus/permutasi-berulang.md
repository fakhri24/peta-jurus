---
id: permutasi-berulang
nama: Permutasi dengan Unsur Sama
pilar: kombinatorika
tahap: osn-k
prasyarat: [permutasi]
contoh: [pbr-contoh-1]
latihan: [pbr-01, pbr-02, pbr-03, pbr-04, pbr-05, pbr-06]
---

## Kapan dipakai

Menyusun objek berjajar seperti permutasi biasa, tapi **sebagian objeknya tidak bisa
dibedakan**. Pemicu paling khas: menyusun huruf sebuah kata yang punya huruf kembar, atau
menjajar bola yang sewarna.

Kalau kamu sudah menulis $n!$ lalu merasa hasilnya kelebihan, biasanya ini jurusnya.

## Intinya

Kalau dari $n$ objek ada $n_1$ yang sejenis, $n_2$ sejenis lain, sampai $n_r$, banyaknya
susunan berbeda adalah

$$\frac{n!}{n_1!\, n_2! \cdots n_r!} \qquad \text{dengan } n_1 + n_2 + \cdots + n_r = n$$

Alasan pembaginya sama dengan alasan pada kombinasi. Anggap dulu semua objek berbeda —
ada $n!$ susunan. Tiap susunan sungguhan lalu terhitung berkali-kali, tepat sebanyak cara
menukar-nukar objek sejenis di antara mereka sendiri, yaitu $n_1! \cdots n_r!$. Membaginya
mengembalikan hitungan ke satu kali per susunan.

Kata **BUKU** punya $\frac{4!}{2!} = 12$ susunan, bukan $24$: dua huruf U tidak bisa
dibedakan.

Cara lain memandangnya: pilih dulu tempat untuk jenis pertama, lalu jenis kedua dari sisa,
dan seterusnya. Hasilnya sama, dan kadang lebih mudah diikuti:

$$\binom{n}{n_1}\binom{n-n_1}{n_2}\cdots$$

## Jebakan umum

- **Lupa membagi sama sekali,** sehingga tiap susunan terhitung berkali-kali.
- **Menjumlahkan pembaginya.** Yang benar $n_1!\cdot n_2!$, bukan $(n_1 + n_2)!$ dan bukan
  $n_1! + n_2!$.
- **Menganggap sama objek yang sebenarnya berbeda.** Dua bola merah yang bernomor tetap
  bisa dibedakan, dan di situ pembaginya tidak berlaku.
