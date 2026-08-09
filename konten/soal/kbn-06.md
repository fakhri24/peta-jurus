---
id: kbn-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa untuk setiap bilangan bulat $n \ge 0$ berlaku

$$\binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{n} = 2^{n}$$

Buktikan dengan **dua cara**: lewat teorema binomial, dan lewat alasan pencacahan.

## Petunjuk

- Cara pertama: teorema binomial berlaku untuk sebarang $x$ dan $y$. Pilih nilai yang membuat seluruh pangkatnya menjadi $1$.
- Cara kedua: ruas kiri menghitung sesuatu dengan memecahnya menurut ukuran. Sesuatu apa?
- Untuk cara kedua, hitung benda yang sama dengan cara lain — keputusan demi keputusan, bukan ukuran demi ukuran.

## Pembahasan

### Cara pertama — substitusi ke teorema binomial

Teorema binomial menyatakan, untuk sebarang $x$ dan $y$,

$$(x+y)^{n} = \sum_{k=0}^{n} \binom{n}{k}\, x^{\,n-k}\, y^{\,k}$$

Ambil $x = 1$ dan $y = 1$. Maka $x^{\,n-k} = 1$ dan $y^{\,k} = 1$ untuk setiap $k$, sehingga
ruas kanannya menjadi jumlah koefisiennya saja:

$$(1+1)^{n} = \sum_{k=0}^{n} \binom{n}{k}$$

Ruas kiri bernilai $2^{n}$. Maka

$$\sum_{k=0}^{n} \binom{n}{k} = 2^{n} \qquad \blacksquare$$

### Cara kedua — hitung himpunan bagian dengan dua cara

Tinjau himpunan $S$ yang beranggotakan $n$ benda, dan cacah **seluruh himpunan bagiannya**.

**Cara A — pecah menurut ukuran.** Setiap himpunan bagian punya ukuran tertentu, yaitu
salah satu dari $0, 1, 2, \dots, n$. Banyaknya himpunan bagian berukuran $k$ adalah
$\binom{n}{k}$, menurut arti koefisien binomial itu sendiri.

Kelompok-kelompok ini **lepas** — satu himpunan bagian tidak mungkin punya dua ukuran
berbeda — dan **menutupi semuanya**, sebab tiap himpunan bagian punya ukuran. Jadi aturan
jumlah berlaku:

$$\sum_{k=0}^{n} \binom{n}{k}$$

**Cara B — keputusan demi keputusan.** Membentuk himpunan bagian sama artinya dengan
memutuskan, untuk tiap benda, ia ikut atau tidak. Ada $n$ benda dan tiap keputusan punya $2$
kemungkinan yang tidak dipengaruhi keputusan lain:

$$\underbrace{2 \times 2 \times \cdots \times 2}_{n} = 2^{n}$$

**Kedua cara mencacah himpunan yang sama,** yaitu seluruh himpunan bagian dari $S$. Karena
itu hasilnya wajib sama:

$$\sum_{k=0}^{n} \binom{n}{k} = 2^{n} \qquad \blacksquare$$

### Mengapa cara kedua lebih berharga

Cara pertama benar, tetapi ia meminjam teorema binomial — yang buktinya sendiri bersandar
pada pencacahan yang sama. Cara kedua berdiri sendiri dan **menjelaskan** kesamaannya: kedua
ruas adalah dua cara menghitung benda yang sama.

Pola itu, menghitung satu himpunan dengan dua cara lalu menyamakan hasilnya, adalah cara
baku membuktikan identitas koefisien binomial. Identitas lain keluar dari pilihan himpunan
yang berbeda:

- Memilih ketua sekaligus timnya memberi $\sum_k k\binom{n}{k} = n\,2^{n-1}$.
- Memecah menurut apakah satu benda tertentu ikut memberi aturan Pascal,
  $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

**Periksa untuk $n = 3$.** Ruas kiri: $1 + 3 + 3 + 1 = 8$. Ruas kanan: $2^3 = 8$. Daftar
himpunan bagiannya memang $8$ — satu kosong, tiga berukuran satu, tiga berukuran dua, dan
satu berisi semuanya.

## Rubrik

- Menuliskan teorema binomial dengan benar
- Mensubstitusi $x = y = 1$ dan menjelaskan mengapa seluruh pangkatnya menjadi $1$
- Menyimpulkan $(1+1)^n = 2^n$
- Cara kedua: menyatakan dengan jelas benda apa yang dicacah, yaitu seluruh himpunan bagian
- Cara kedua A: memecah menurut ukuran, dan menyebut kelompoknya lepas serta lengkap
- Cara kedua B: menghitung $2^n$ lewat keputusan ikut atau tidak untuk tiap unsur
- Menyimpulkan kedua ruas sama karena mencacah himpunan yang sama
