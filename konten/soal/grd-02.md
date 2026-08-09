---
id: grd-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [graf-dasar]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Sebuah graf memiliki $6$ titik yang derajatnya berturut-turut

$$1,\ 1,\ 2,\ 2,\ 3,\ 3$$

Ada berapa ruas pada graf itu?

## Petunjuk

- Jumlahkan seluruh derajatnya lebih dulu.
- Angka itu menghitung tiap ruas dua kali, sekali dari masing-masing ujungnya.
- Periksa hasilnya bilangan bulat — kalau tidak, graf semacam itu tidak ada.

## Pembahasan

**Jumlahkan derajatnya.**

$$1 + 1 + 2 + 2 + 3 + 3 = 12$$

**Terapkan lema jabat tangan.**

$$\sum_v \deg(v) = 2|E| \quad\Longrightarrow\quad 12 = 2|E| \quad\Longrightarrow\quad
|E| = \boxed{6}$$

**Periksa daftar derajatnya masuk akal.** Ada beberapa pemeriksaan murah yang selalu layak
dikerjakan:

- **Jumlahnya harus genap.** Di sini $12$, genap. Kalau ganjil, daftar itu mustahil.
- **Banyaknya derajat ganjil harus genap.** Di sini ada dua titik berderajat $1$ dan dua
  berderajat $3$ — seluruhnya empat, genap. Cocok.
- **Tiap derajat paling banyak $n-1$.** Di sini $n = 6$, sehingga derajat paling besar
  yang mungkin adalah $5$. Derajat terbesar pada daftar adalah $3$. Cocok.

**Contoh daftar yang gagal.** Daftar $1, 1, 2, 2, 3, 4$ berjumlah $13$ — ganjil, sehingga
tidak ada graf yang derajatnya seperti itu, tanpa perlu mencoba menggambar apa pun.

Daftar $1, 1, 1, 1, 1, 5$ lolos pemeriksaan jumlah — totalnya $10$, genap — tetapi tetap
mustahil karena alasan lain: titik berderajat $5$ harus terhubung ke kelima titik lain,
sehingga tiap titik lain berderajat paling sedikit $1$, yang di sini terpenuhi... dan
ternyata daftar ini **memang bisa** diwujudkan sebagai bintang. Perbedaan itu menunjukkan
bahwa pemeriksaan jumlah adalah syarat **perlu**, bukan syarat cukup.

**Yang tidak ditentukan oleh derajat.** Daftar derajat tidak menentukan bentuk grafnya.
Untuk daftar $1,1,2,2,3,3$ ada beberapa graf berbeda yang semuanya cocok, dan seluruhnya
punya $6$ ruas. Soal yang menanyakan banyaknya ruas selalu punya jawaban tunggal; soal yang
menanyakan bentuk grafnya biasanya tidak.
