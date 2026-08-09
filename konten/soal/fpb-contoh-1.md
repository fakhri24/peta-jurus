---
id: fpb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 3
jawaban: "10"
---

## Soal

Ada berapa cara membayar tepat $10$ rupiah dengan koin bernilai $1$, $2$, dan $5$ rupiah?
Banyaknya koin tiap jenis tidak dibatasi, dan urutan pembayaran tidak diperhatikan.

## Petunjuk

- Tiap jenis koin menyumbang satu faktor pada sebuah hasil kali deret. Tuliskan faktor untuk koin $1$ rupiah lebih dulu.
- Untuk koin bernilai $c$, pangkat yang mungkin adalah kelipatan $c$ — sebab memakai $m$ koin menyumbang nilai $mc$.
- Jawabannya adalah koefisien $x^{10}$ pada hasil kali ketiga faktor itu.

## Pembahasan

**Susun satu faktor untuk tiap jenis koin.** Memakai $m$ koin bernilai $c$ menyumbang nilai
$mc$, sehingga jenis koin itu diwakili oleh

$$1 + x^{c} + x^{2c} + x^{3c} + \cdots = \frac{1}{1-x^{c}}$$

Ketiga jenis koin memberi

$$F(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2} \cdot \frac{1}{1-x^5}$$

**Mengapa perkaliannya menghitung yang benar.** Mengalikan ketiga deret berarti memilih satu
suku dari tiap faktor — yaitu memutuskan berapa koin dari tiap jenis — lalu menjumlahkan
pangkatnya. Koefisien $x^{10}$ karena itu menghitung banyaknya pilihan yang jumlah nilainya
tepat $10$, yakni persis yang ditanyakan.

**Hitung koefisiennya.** Untuk soal sekecil ini, cara terpendek adalah memecah menurut
banyaknya koin $5$ rupiah.

| Koin $5$-an | Sisa | Cara membayar sisa dengan $1$ dan $2$ |
|---|---|---|
| $2$ | $0$ | $1$ |
| $1$ | $5$ | koin $2$-an: $0,1,2$ → $3$ |
| $0$ | $10$ | koin $2$-an: $0,\dots,5$ → $6$ |

Untuk sisa $s$ yang dibayar dengan koin $1$ dan $2$, banyaknya cara adalah
$\left\lfloor \frac{s}{2} \right\rfloor + 1$ — sebab banyaknya koin $2$-an menentukan
seluruhnya, dan sisanya ditutup koin $1$-an.

$$1 + 3 + 6 = \boxed{10}$$

**Mengapa fungsi pembangkit tetap layak dipelajari** kalau pemecahan kasus sudah cukup di
sini: karena pemecahan kasus tumbuh cepat. Untuk lima jenis koin dan nilai $100$, tabel
seperti di atas menjadi tidak terkelola, sedangkan bentuk hasil kalinya tidak berubah sama
sekali — hanya faktornya bertambah.

**Bentuk umumnya.** Untuk jenis koin bernilai $c_1, \dots, c_r$ tanpa batas pemakaian:

$$F(x) = \prod_{i=1}^{r} \frac{1}{1-x^{c_i}}$$

**Kalau pemakaiannya dibatasi,** deretnya tinggal dipotong. Misalnya kalau koin $5$-an hanya
tersedia satu, faktornya menjadi $1 + x^5$ — bukan deret tak hingga. Kemampuan menyatakan
batasan sebagai pemotongan deret itulah yang membuat jurus ini unggul pada soal berkendala
banyak.

**Perhatikan urutan tidak diperhatikan,** dan bentuk hasil kali di atas memang menghitung
begitu: yang dipilih adalah **berapa** koin tiap jenis, bukan urutan pembayarannya.
