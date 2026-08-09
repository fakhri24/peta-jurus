---
id: fpb-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 3
jawaban: "9"
---

## Soal

Ada berapa cara membayar tepat $20$ rupiah dengan koin bernilai $1$, $5$, dan $10$ rupiah?
Banyaknya koin tiap jenis tidak dibatasi, dan urutan pembayaran tidak diperhatikan.

## Petunjuk

- Susun satu faktor untuk tiap jenis koin. Untuk koin bernilai $c$ tanpa batas pemakaian, faktornya memuat pangkat kelipatan $c$.
- Jawabannya adalah koefisien $x^{20}$ pada hasil kali ketiga faktor.
- Untuk menghitungnya, pecah menurut banyaknya koin bernilai terbesar — sisanya lebih mudah ditangani.

## Pembahasan

**Susun fungsi pembangkitnya.**

$$F(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^{5}} \cdot \frac{1}{1-x^{10}}$$

Jawabannya adalah $\left[x^{20}\right]F(x)$.

**Hitung dengan memecah menurut koin $10$-an.** Sebut $d$ banyaknya koin $10$-an. Karena
$10d \le 20$, nilainya $0$, $1$, atau $2$.

Untuk sisa $s$ yang dibayar dengan koin $1$ dan $5$, banyaknya cara ditentukan sepenuhnya
oleh berapa koin $5$-an yang dipakai — sisanya otomatis ditutup koin $1$-an. Jadi
banyaknya cara adalah $\left\lfloor \frac{s}{5} \right\rfloor + 1$.

| $d$ | sisa $s$ | cara membayar sisa |
|---|---|---|
| $2$ | $0$ | $1$ |
| $1$ | $10$ | $\left\lfloor \tfrac{10}{5} \right\rfloor + 1 = 3$ |
| $0$ | $20$ | $\left\lfloor \tfrac{20}{5} \right\rfloor + 1 = 5$ |

$$1 + 3 + 5 = \boxed{9}$$

**Periksa dengan mendaftar.** Tulis pembayaran sebagai $(\text{jumlah } 10, \text{jumlah }
5, \text{jumlah } 1)$:

$$(2,0,0),\ (1,2,0),\ (1,1,5),\ (1,0,10),\ (0,4,0),\ (0,3,5),\ (0,2,10),\ (0,1,15),\ (0,0,20)$$

Tepat $9$.

**Mengapa jawabannya tidak sebesar dugaan.** Nilai koinnya saling berkelipatan — $10$
kelipatan $5$, dan $5$ kelipatan $1$ — sehingga banyak kombinasi yang berbeda ternyata
menghasilkan nilai yang sama dan tidak menambah cara baru. Kalau koinnya bernilai $1$, $4$,
dan $7$, jawabannya untuk $20$ rupiah lebih besar meskipun angkanya sepadan.

**Struktur ini yang membuat hitungannya bertingkat.** Karena tiap koin membagi habis koin
yang lebih besar, pemecahan kasus dari nilai terbesar ke terkecil selalu meninggalkan sisa
yang mudah — dan itu sebabnya sistem mata uang di dunia nyata biasanya disusun begitu.

**Kalau pemakaiannya dibatasi,** deretnya tinggal dipotong. Misalnya kalau koin $10$-an
hanya tersedia satu, faktornya menjadi $1 + x^{10}$, dan baris $d = 2$ pada tabel di atas
hilang — jawabannya menjadi $8$.
