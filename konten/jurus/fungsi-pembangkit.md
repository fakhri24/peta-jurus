---
id: fungsi-pembangkit
nama: Fungsi Pembangkit
pilar: kombinatorika
tahap: osn
prasyarat: [koefisien-binomial, rekursi]
contoh: [fpb-contoh-1]
latihan: [fpb-01, fpb-02, fpb-03, fpb-04, fpb-05, fpb-06]
---

## Kapan dipakai

Pencacahan dengan **kendala berlapis** pada tiap jenis objek, atau rekurens yang rumus
tertutupnya dicari. Pemicu yang khas: "berapa cara membayar $n$ rupiah dengan pecahan
tertentu, tiap pecahan boleh dipakai paling banyak sekian kali".

Kalau kendalanya cuma satu jenis, biasanya ada jalan yang lebih pendek. Fungsi pembangkit
baru sepadan ongkosnya ketika kendalanya bermacam-macam sekaligus.

## Intinya

Simpan seluruh barisan $a_0, a_1, a_2, \dots$ sebagai satu benda:

$$A(x) = \sum_{n \ge 0} a_n x^{n}$$

$x$ di sini bukan bilangan yang akan disubstitusi — ia cuma tempat menaruh indeks. Karena
itu kekonvergenan tidak jadi soal; yang dipakai deret formal.

**Yang membuatnya berguna adalah perkaliannya.** Mengalikan dua deret berarti memasangkan
pilihan dari keduanya, dan koefisien $x^n$ pada hasilnya menghitung pasangan yang jumlahnya
$n$. Jadi satu faktor untuk tiap jenis objek, dan pangkat di dalam faktor itu menyatakan
pilihan yang diperbolehkan untuk jenis tersebut.

Deret yang harus dikenali seketika:

$$\frac{1}{1-x} = \sum_{n \ge 0} x^{n}, \qquad \frac{1-x^{m+1}}{1-x} = \sum_{n=0}^{m} x^{n}$$

$$\frac{1}{(1-x)^{k}} = \sum_{n \ge 0} \binom{n+k-1}{k-1} x^{n}, \qquad (1+x)^{n} = \sum_{k} \binom{n}{k} x^{k}$$

Yang ketiga persis rumus membagi objek identik, dan itu bukan kebetulan: keduanya
menghitung hal yang sama dengan bahasa yang berbeda.

## Jebakan umum

- **Mencemaskan kekonvergenan.** Deretnya formal; tidak ada nilai $x$ yang dimasukkan.
- **Salah menyusun faktornya.** Satu faktor untuk tiap **jenis** objek. Batas pemakaian
  diwujudkan dengan memotong deretnya, bukan dengan menambah faktor baru.
- **Berhenti setelah dapat fungsinya.** Jawabannya adalah koefisien $x^n$, dan menariknya
  keluar sering bagian yang paling banyak kerjanya.
