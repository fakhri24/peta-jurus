---
id: deret-teleskopik
nama: Deret Teleskopik
pilar: aljabar
tahap: osn-p
prasyarat: [barisan-deret, faktorisasi]
contoh: [tel-contoh-1]
latihan: [tel-01, tel-02, tel-03, tel-04, tel-05, tel-06]
---

## Kapan dipakai

Deret panjang dengan suku berbentuk pecahan yang penyebutnya hasil kali dua bilangan
berdekatan, atau selisih yang polanya rapi. Ciri paling terang: banyak suku, tetapi soal
menuntut nilai **eksak**.

## Intinya

Gagasannya satu kalimat: **tulis tiap suku sebagai selisih dua bentuk yang berurutan**,
lalu biarkan bagian tengahnya saling menghapus.

$$\sum_{k=1}^{n} \left(f(k) - f(k+1)\right) = f(1) - f(n+1)$$

Seluruh isi tengah lenyap; yang tersisa hanya dua ujung.

Bentuk yang paling sering muncul:

$$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$$

sehingga

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

Lebih umum, pecahan parsial menyediakan selisihnya:

$$\frac{1}{k(k+d)} = \frac{1}{d}\left(\frac{1}{k} - \frac{1}{k+d}\right)$$

Untuk $d > 1$, yang tersisa bukan dua suku melainkan $d$ suku di tiap ujung — dan itu
bagian yang paling sering salah dihitung.

Teleskop juga bekerja di luar pecahan: $k \cdot k! = (k+1)! - k!$, dan
$\sqrt{k+1} - \sqrt{k} = \dfrac{1}{\sqrt{k+1}+\sqrt{k}}$.

## Jebakan umum

- **Salah menghitung sisa di ujung.** Untuk selisih berjarak $d$, yang tersisa $d$ suku di
  awal dan $d$ suku di akhir, bukan satu.
- **Lupa faktor $\frac{1}{d}$** pada pecahan parsial.
- **Menuliskan pola tanpa memeriksanya.** Tulis tiga suku pertama dan dua suku terakhir
  secara nyata sebelum menyimpulkan apa yang menghapus apa.
