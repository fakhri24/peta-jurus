---
id: drg-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebut $D_n$ banyaknya susunan ulang $n$ objek yang tidak menempatkan satu pun objek di
tempat asalnya.

Buktikan bahwa untuk $n \ge 3$ berlaku

$$D_n = (n-1)\left(D_{n-1} + D_{n-2}\right)$$

dengan alasan pencacahan langsung — bukan dengan menurunkannya dari rumus jumlah.

## Petunjuk

- Tinjau ke mana objek pertama pergi. Ada berapa kemungkinan, dan mengapa banyaknya sama untuk tiap kemungkinan?
- Setelah objek pertama menempati tempat $k$, tinjau objek ke-$k$: apakah ia menempati tempat pertama atau tidak. Dua kemungkinan itu memecah semuanya.
- Untuk kasus "tidak", tunjukkan sisanya adalah persoalan yang sama pada $n-1$ objek — dengan tempat pertama berlaku sebagai tempat terlarang bagi objek ke-$k$.

## Pembahasan

Beri nomor objek dan tempat dengan $1$ sampai $n$; susunan yang dicacah adalah yang tidak
menempatkan objek $i$ di tempat $i$ untuk setiap $i$.

### Langkah 1 — ke mana objek $1$ pergi

Objek $1$ boleh menempati tempat mana pun kecuali tempat $1$, sehingga ada

$$n - 1 \text{ pilihan}$$

Misalkan ia menempati tempat $k$, dengan $k \ne 1$.

Banyaknya susunan yang mungkin setelah itu **sama untuk tiap pilihan $k$** — sebab
penomorannya bisa ditukar tanpa mengubah persoalannya. Karena itu cukup menghitung untuk
satu $k$, lalu mengalikannya dengan $n-1$.

### Langkah 2 — pecah menurut nasib objek $k$

**Kasus A — objek $k$ menempati tempat $1$.** Objek $1$ dan objek $k$ saling bertukar, dan
keduanya sudah selesai. Yang tersisa adalah $n-2$ objek yang harus ditempatkan pada $n-2$
tempat, tanpa satu pun berada di tempat asalnya — persoalan yang sama pada $n-2$ objek.

Menyumbang $D_{n-2}$.

**Kasus B — objek $k$ **tidak** menempati tempat $1$.** Tinjau $n-1$ objek selain objek $1$,
dan $n-1$ tempat selain tempat $k$ — sebab tempat $k$ sudah terisi.

Larangan yang berlaku pada mereka adalah:

- objek $i$ tidak boleh di tempat $i$, untuk tiap $i \ne 1, k$;
- objek $k$ tidak boleh di tempat $1$, menurut andaian kasus ini.

Jadi **tiap objek punya tepat satu tempat terlarang, dan tempat terlarang itu berbeda-beda**
— tepat bentuk persoalan aslinya pada $n-1$ objek, dengan tempat $1$ berperan sebagai
"tempat asal" bagi objek $k$.

Menyumbang $D_{n-1}$.

### Langkah 3 — rangkai

Kedua kasus **lepas** — objek $k$ entah di tempat $1$ entah tidak — dan **menutupi
semuanya**. Untuk tiap pilihan $k$, sumbangannya $D_{n-1} + D_{n-2}$. Karena ada $n-1$
pilihan $k$ dan banyaknya sama untuk masing-masing:

$$D_n = (n-1)\left(D_{n-1} + D_{n-2}\right) \qquad \blacksquare$$

### Bagian yang menentukan seluruh bukti

Langkah yang paling mudah keliru adalah Kasus B. Godaannya adalah menyimpulkan sisanya
"bebas", padahal objek $k$ membawa larangan baru — ia tidak boleh di tempat $1$. Justru
larangan pengganti itulah yang membuat sisanya tetap berbentuk persoalan semula, dan tanpa
menyebutkannya, kemunculan $D_{n-1}$ tidak punya alasan.

Perhatikan pula bahwa larangannya harus **berbeda-beda**: tiap objek punya satu tempat
terlarang, dan tidak ada dua objek yang terlarang di tempat yang sama. Kalau tidak,
persoalannya bukan lagi persoalan yang sama.

### Periksa dengan nilai kecil

$$D_3 = 2(D_2 + D_1) = 2(1+0) = 2$$

Memang hanya ada dua: $231$ dan $312$.

$$D_4 = 3(D_3 + D_2) = 3(2+1) = 9$$

Cocok dengan pendaftaran langsung.

**Batas $n \ge 3$ diperlukan** karena buktinya memakai $D_{n-2}$ dengan $n-2 \ge 1$. Untuk
$n = 2$, Kasus B tidak punya isi — tidak ada objek selain objek $1$ dan objek $k$.

## Rubrik

- Menyatakan objek $1$ punya $n-1$ pilihan tempat
- Menyebut bahwa banyaknya susunan sisa sama untuk tiap pilihan, sebagai alasan sahnya mengalikan dengan $n-1$
- Memecah menurut apakah objek $k$ menempati tempat $1$, dan menyatakan kedua kasus lepas serta lengkap
- Kasus A: menyimpulkan sisanya persoalan yang sama pada $n-2$ objek
- Kasus B: menyatakan larangan baru bagi objek $k$, yaitu tempat $1$
- Kasus B: menunjukkan tiap objek punya tepat satu tempat terlarang yang berbeda-beda, sehingga sisanya persoalan yang sama pada $n-1$ objek
- Merangkai menjadi $D_n = (n-1)(D_{n-1}+D_{n-2})$
