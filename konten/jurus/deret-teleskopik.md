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

Deret panjang dengan suku berbentuk **pecahan yang penyebutnya hasil kali dua bilangan
berdekatan** — $\frac{1}{k(k+1)}$, $\frac{1}{(2k-1)(2k+1)}$. Bentuk itu selalu bisa dipecah
menjadi selisih dua pecahan.

Pemicu kedua, dan inilah tandanya yang paling dapat diandalkan: soal punya **banyak suku
tetapi menuntut nilai eksak**. Jumlah seribu suku yang jawabannya harus persis berarti
hampir semuanya dirancang untuk saling menghapus.

Pemicu ketiga: sukunya memuat **selisih dua bentuk berurutan** yang sudah terlihat —
$\sqrt{k+1} - \sqrt{k}$, atau $\frac{1}{k!} - \frac{1}{(k+1)!}$. Di situ tidak ada yang
perlu dipecah; jumlahnya langsung runtuh ke dua ujungnya.

Pemicu keempat: bentuknya belum berupa selisih tetapi punya **pembilang yang mencurigakan
rapi**, seperti $\frac{2k+1}{k^2(k+1)^2}$. Pembilang seperti itu biasanya sisa dari
pengurangan dua pecahan, dan mengembalikannya adalah seluruh pekerjaannya.

Pemicu kelima: soal berupa **hasil kali**, bukan jumlah, dengan tiap faktor berbentuk
$1 - \frac1{k^2}$ atau serupa. Gagasan yang sama berlaku — yang saling menghapus faktor,
bukan suku.

Yang wajib ditulis dan paling sering hilang: **apa yang tersisa di kedua ujung**. Jawaban
yang menyebut "dan seterusnya saling menghapus" tanpa menunjukkan sisanya belum lengkap.

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
