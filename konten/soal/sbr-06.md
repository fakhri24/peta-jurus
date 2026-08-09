---
id: sbr-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa banyaknya penyelesaian bilangan bulat tak negatif dari

$$x_1 + x_2 + \cdots + x_k = n$$

adalah

$$\binom{n+k-1}{k-1}$$

Buktikan dengan membangun padanan satu-satu antara penyelesaian dan susunan bintang serta
sekat, dan tunjukkan padanan itu memang satu-satu ke dua arah.

## Petunjuk

- Wakilkan tiap penyelesaian sebagai barisan $n$ bintang dan beberapa sekat. Tentukan lebih dulu berapa sekat yang dibutuhkan.
- Jelaskan cara membaca sebuah susunan kembali menjadi penyelesaian — itulah arah sebaliknya dari padanannya.
- Setelah padanannya sah, mencacah penyelesaian berubah menjadi mencacah susunan, dan itu soal memilih tempat.

## Pembahasan

### Membangun padanannya

**Dari penyelesaian ke susunan.** Ambil sebuah penyelesaian $(x_1, x_2, \dots, x_k)$. Tulis

$$\underbrace{\star\cdots\star}_{x_1}\ \mid\ \underbrace{\star\cdots\star}_{x_2}
\ \mid\ \cdots\ \mid\ \underbrace{\star\cdots\star}_{x_k}$$

yaitu $x_1$ bintang, sebuah sekat, $x_2$ bintang, sebuah sekat, dan seterusnya.

Untuk memisahkan $k$ kelompok dibutuhkan $k-1$ sekat. Banyaknya bintang seluruhnya adalah
$x_1 + \cdots + x_k = n$, sehingga panjang barisannya

$$n + k - 1$$

dan panjang itu **sama untuk setiap penyelesaian**.

Peubah yang bernilai $0$ tetap terwakili — ia muncul sebagai kelompok kosong, yaitu dua
sekat berdempetan atau sekat di ujung barisan.

**Dari susunan kembali ke penyelesaian.** Ambil sebarang barisan sepanjang $n+k-1$ yang
terdiri atas $n$ bintang dan $k-1$ sekat. Bacalah banyaknya bintang sebelum sekat pertama
sebagai $x_1$, di antara sekat pertama dan kedua sebagai $x_2$, dan seterusnya, dengan
bintang setelah sekat terakhir sebagai $x_k$.

Bilangan yang diperoleh seluruhnya tak negatif, dan jumlahnya persis banyaknya bintang,
yaitu $n$. Jadi hasil pembacaan itu memang sebuah penyelesaian yang sah.

**Kedua arah saling meniadakan.** Menulis penyelesaian menjadi susunan lalu membacanya
kembali mengembalikan bilangan yang sama; begitu pula sebaliknya. Karena itu padanannya
satu-satu dan pada, sehingga kedua himpunan sama banyaknya.

### Mencacah susunannya

Sebuah susunan ditentukan sepenuhnya begitu diputuskan **tempat mana yang ditempati sekat**
— sisanya otomatis bintang. Jadi tinggal memilih $k-1$ tempat dari $n+k-1$:

$$\binom{n+k-1}{k-1} \qquad \blacksquare$$

Boleh juga dilihat dari sisi bintangnya, memilih $n$ tempat dari $n+k-1$:

$$\binom{n+k-1}{n}$$

Kedua bentuk itu sama, sebab $(n+k-1) - (k-1) = n$.

### Mengapa arah sebaliknya perlu diperiksa

Menuliskan padanan satu arah saja hanya membuktikan bahwa penyelesaiannya **tidak lebih
banyak** daripada susunannya. Untuk menyimpulkan keduanya sama banyaknya, harus ditunjukkan
tidak ada susunan yang terlewat — dan itu yang dikerjakan oleh cara pembacaan di atas.

Pemeriksaan ini bukan formalitas. Kalau sekatnya dilarang berdempetan, pembacaan tetap
berjalan tetapi sebagian penyelesaian — yang memuat peubah bernilai $0$ — tidak lagi punya
susunan padanannya. Rumus yang keluar dari situ adalah $\binom{n-1}{k-1}$, yaitu rumus untuk
penyelesaian **positif**. Perbedaan antara kedua rumus itu persis terletak pada apakah sekat
boleh berdempetan.

## Rubrik

- Menyatakan wakilan penyelesaian sebagai barisan bintang dan sekat, dengan $k-1$ sekat
- Menghitung panjang barisannya sebagai $n+k-1$, dan menyebut panjang itu sama untuk tiap penyelesaian
- Menjelaskan bahwa peubah bernilai $0$ terwakili sebagai kelompok kosong
- Menjelaskan cara membaca susunan kembali menjadi penyelesaian
- Memeriksa hasil pembacaan memang penyelesaian yang sah, yaitu tak negatif dan berjumlah $n$
- Menyimpulkan padanannya satu-satu ke dua arah, sehingga kedua himpunan sama banyaknya
- Mencacah susunan sebagai pemilihan $k-1$ tempat dari $n+k-1$
