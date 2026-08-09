---
id: prd-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: uraian
kesulitan: 3
---

## Soal

Seorang siswa mengerjakan soal "dua dadu setimbang dilempar; berapa peluang jumlah matanya
$5$?" dengan cara berikut.

> Jumlah yang mungkin adalah $2, 3, 4, \dots, 12$, seluruhnya ada $11$ nilai. Salah satunya
> adalah $5$. Jadi peluangnya $\frac{1}{11}$.

Jelaskan mengapa penalaran itu **salah**, lalu hitung peluang yang benar disertai alasannya.

## Petunjuk

- Rumus "banyaknya hasil yang diinginkan dibagi banyaknya seluruh hasil" punya satu syarat yang tidak disebut siswa itu.
- Periksa apakah jumlah $2$ dan jumlah $7$ sama-sama mudah terjadi. Kalau tidak, ruang sampelnya tidak memenuhi syarat itu.
- Susun ulang ruang sampelnya sebagai pasangan mata dadu, dan jelaskan mengapa pasangan itu sama mungkin.

## Pembahasan

### Mengapa penalaran itu salah

Rumus

$$P(A) = \frac{|A|}{|S|}$$

**tidak berlaku untuk sebarang ruang sampel.** Ia menuntut satu syarat: setiap anggota $S$
harus **sama mungkin**. Siswa itu memakai $S = \{2,3,\dots,12\}$ tanpa memeriksa syarat
tersebut — dan syarat itu tidak terpenuhi.

Buktinya sederhana. Jumlah $2$ hanya dapat terjadi lewat satu cara, yaitu kedua dadu
menunjukkan $1$. Sementara jumlah $7$ dapat terjadi lewat enam cara:

$$(1,6),\ (2,5),\ (3,4),\ (4,3),\ (5,2),\ (6,1)$$

Jadi jumlah $7$ **enam kali lebih mungkin** daripada jumlah $2$. Kesebelas nilai itu bukan
hasil yang setara, melainkan kelompok-kelompok berukuran berbeda.

Kalau penalaran siswa itu benar, seluruh jumlah akan berpeluang $\frac1{11}$ dan totalnya
$1$ — tetapi kenyataannya berbeda, dan itu bisa diperiksa siapa pun dengan melempar dadu
cukup banyak kali.

### Hitungan yang benar

**Susun ruang sampel yang sama mungkin.** Bedakan kedua dadu, misalnya satu merah dan satu
biru, lalu catat hasilnya sebagai pasangan terurut $(m,b)$:

$$S = \{(m,b) : 1 \le m \le 6,\ 1 \le b \le 6\}, \qquad |S| = 36$$

**Mengapa pasangan-pasangan ini sama mungkin.** Tiap dadu setimbang, sehingga keenam matanya
sama mungkin; dan hasil satu dadu tidak memengaruhi dadu lainnya. Karena itu tiap pasangan
berpeluang $\frac16 \times \frac16 = \frac1{36}$.

**Daftar hasil yang diinginkan.** Pasangan yang jumlahnya $5$:

$$(1,4),\ (2,3),\ (3,2),\ (4,1)$$

Ada $4$ pasangan. Perhatikan $(2,3)$ dan $(3,2)$ dihitung terpisah — begitu dadunya
dibedakan, keduanya hasil yang berlainan.

**Hitung.**

$$P(\text{jumlah } 5) = \frac{4}{36} = \frac19 \qquad \blacksquare$$

### Pelajaran yang lebih luas

Kekeliruan siswa itu bukan kekeliruan berhitung, melainkan kekeliruan **memilih ruang
sampel**. Ia memakai ruang sampel yang sah sebagai daftar kemungkinan, tetapi tidak sah
sebagai dasar rumus peluang.

Aturan praktisnya: **turunkan ruang sampel sampai ke tingkat yang paling rinci** — yaitu
tingkat yang setiap hasilnya benar-benar setara — lalu hitung di situ. Menjumlahkan atau
mengelompokkan boleh dilakukan setelahnya.

Kekeliruan serupa muncul dalam banyak bentuk: menganggap "menang atau kalah" berpeluang
masing-masing $\frac12$, atau menganggap dua anak dalam keluarga memberi tiga keadaan
setara ("dua putra, dua putri, satu-satu") — padahal yang terakhir terjadi lewat dua cara.

## Rubrik

- Menyatakan bahwa rumus $\frac{|A|}{|S|}$ menuntut anggota $S$ sama mungkin
- Menunjukkan syarat itu tidak terpenuhi, dengan membandingkan berapa cara terjadinya dua jumlah yang berbeda
- Menyusun ruang sampel yang benar sebagai pasangan terurut, dan menyebut $|S| = 36$
- Menjelaskan mengapa pasangan terurut itu sama mungkin
- Mendaftar keempat pasangan yang berjumlah $5$, termasuk menghitung $(2,3)$ dan $(3,2)$ terpisah
- Menyimpulkan peluangnya $\frac19$
