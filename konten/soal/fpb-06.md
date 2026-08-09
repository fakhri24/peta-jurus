---
id: fpb-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: uraian
kesulitan: 5
---

## Soal

Barisan $a_0, a_1, a_2, \dots$ memenuhi

$$a_0 = 0, \qquad a_1 = 1, \qquad a_n = a_{n-1} + a_{n-2} \quad (n \ge 2)$$

Tentukan fungsi pembangkitnya

$$A(x) = \sum_{n \ge 0} a_n x^{n}$$

dalam bentuk tertutup, dan jelaskan mengapa kekonvergenan tidak perlu dipersoalkan.

## Petunjuk

- Kalikan rekurensnya dengan $x^n$, lalu jumlahkan atas seluruh $n$ yang berlaku — yaitu $n \ge 2$.
- Nyatakan tiap penjumlahan yang muncul kembali dalam bentuk $A(x)$, dengan hati-hati pada suku-suku awal yang hilang.
- Setelah persamaannya terbentuk, $A(x)$ tinggal diselesaikan secara aljabar biasa.

## Pembahasan

### Menurunkan bentuk tertutupnya

Kalikan rekurensnya dengan $x^n$ dan jumlahkan atas $n \ge 2$ — batas ini penting, sebab
rekurensnya hanya berlaku mulai $n = 2$:

$$\sum_{n \ge 2} a_n x^{n} = \sum_{n \ge 2} a_{n-1}x^{n} + \sum_{n \ge 2} a_{n-2}x^{n}$$

**Nyatakan tiap bagian lewat $A(x)$.**

Ruas kiri kehilangan dua suku pertama:

$$\sum_{n\ge2} a_n x^n = A(x) - a_0 - a_1 x = A(x) - x$$

Suku pertama di ruas kanan, keluarkan satu $x$:

$$\sum_{n\ge2} a_{n-1}x^{n} = x\sum_{n\ge2}a_{n-1}x^{n-1} = x\sum_{m\ge1}a_m x^{m}
= x\left(A(x) - a_0\right) = x\,A(x)$$

Suku kedua, keluarkan $x^2$:

$$\sum_{n\ge2} a_{n-2}x^{n} = x^{2}\sum_{n\ge2}a_{n-2}x^{n-2} = x^{2}\sum_{m\ge0}a_m x^{m}
= x^{2}A(x)$$

**Rangkai.**

$$A(x) - x = x\,A(x) + x^{2}A(x)$$

$$A(x)\left(1 - x - x^{2}\right) = x$$

$$A(x) = \frac{x}{1-x-x^{2}} \qquad \blacksquare$$

### Memeriksa hasilnya

Kalikan kembali dan bandingkan koefisiennya. Dari $A(x)\left(1-x-x^2\right) = x$, koefisien
$x^n$ untuk $n \ge 2$ memberi

$$a_n - a_{n-1} - a_{n-2} = 0$$

yaitu rekurens semula. Koefisien $x^0$ memberi $a_0 = 0$ dan koefisien $x^1$ memberi
$a_1 - a_0 = 1$, yaitu kedua kasus dasarnya. Jadi bentuk tertutupnya memuat seluruh
keterangan barisan itu — tidak lebih, tidak kurang.

Pemeriksaan lain yang cepat: bagi $x$ dengan $1-x-x^2$ secara pembagian panjang, dan
koefisien yang keluar adalah $0, 1, 1, 2, 3, 5, 8, \dots$ — barisan Fibonacci.

### Mengapa kekonvergenan tidak dipersoalkan

$A(x)$ di sini adalah **deret pangkat formal**, bukan fungsi yang akan dievaluasi. Lambang
$x$ tidak pernah diganti bilangan; ia hanya tempat menaruh indeks, sehingga koefisien
$x^n$ dapat dibaca sebagai $a_n$.

Yang dibutuhkan agar seluruh langkah di atas sah hanyalah dua hal, dan keduanya berlaku pada
deret formal tanpa syarat apa pun:

- penjumlahan dan perkalian deret terdefinisi suku demi suku, sehingga tiap koefisien
  ditentukan oleh berhingga banyak perkalian;
- pembagian oleh $1-x-x^2$ sah karena suku tetapnya $1 \ne 0$ — dan sebuah deret formal punya
  balikan tepat ketika suku tetapnya tidak nol.

Karena itu $\frac{x}{1-x-x^2}$ bermakna penuh sebagai deret formal, dan pertanyaan "untuk
$x$ berapa deretnya konvergen" tidak pernah muncul.

Kebetulan deret ini memang konvergen untuk $|x| < \frac1\varphi$, tetapi kenyataan itu tidak
dipakai di mana pun dalam penurunannya.

### Mengapa penyebutnya $1-x-x^2$

Perhatikan penyebutnya adalah rekurensnya sendiri, ditulis terbalik: dari
$a_n = a_{n-1} + a_{n-2}$ diperoleh $1 - x - x^2$. Hubungan itu berlaku umum — rekurens
linear $a_n = p\,a_{n-1} + q\,a_{n-2}$ selalu memberi penyebut $1 - px - qx^2$, dan
pembilangnya ditentukan oleh kasus dasarnya.

Penyebut itu juga berkerabat dengan persamaan karakteristik $x^2 = px + q$: akar-akar
penyebut adalah kebalikan dari akar-akar persamaan karakteristik. Memfaktorkan penyebutnya
lalu memecahnya menjadi pecahan parsial adalah jalan lain menuju rumus tertutup — dan untuk
Fibonacci, jalan itu menghasilkan rumus Binet.

## Rubrik

- Mengalikan rekurens dengan $x^n$ dan menjumlahkan atas $n \ge 2$, dengan batas yang benar
- Menyatakan $\sum_{n\ge2}a_nx^n = A(x) - x$, memperhitungkan kedua suku awal
- Menyatakan $\sum_{n\ge2}a_{n-1}x^n = x\,A(x)$ dengan penggeseran indeks yang benar
- Menyatakan $\sum_{n\ge2}a_{n-2}x^n = x^2A(x)$
- Menyelesaikan menjadi $A(x) = \dfrac{x}{1-x-x^2}$
- Menjelaskan bahwa deretnya formal, sehingga $x$ tidak pernah disubstitusi
- Menyebut alasan pembagian sah, yaitu suku tetap penyebutnya tidak nol
