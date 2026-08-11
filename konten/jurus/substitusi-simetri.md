---
id: substitusi-simetri
nama: Substitusi dan Kesimetrian
pilar: aljabar
tahap: osn-p
prasyarat: [sistem-persamaan, vieta]
contoh: [ss-contoh-1]
latihan: [ss-01, ss-02, ss-03, ss-04, ss-05, ss-06]
---

## Kapan dipakai

Ada **bentuk yang berulang** di beberapa tempat — $x + \frac1x$, $x^2 + y^2$, $\sqrt{x+1}$.
Begitu satu bentuk muncul lebih dari sekali, memberinya nama biasanya memangkas soalnya
lebih banyak daripada menguraikannya.

Pemicu kedua: **derajatnya tinggi tetapi susunannya teratur** — koefisiennya simetris
membaca dari depan dan dari belakang, seperti $x^4 + x^3 - 4x^2 + x + 1$. Bentuk itu selalu
runtuh menjadi kuadrat setelah dibagi $x^2$ dan diberi satu nama.

Pemicu ketiga: bentuknya **tidak berubah ketika peubahnya ditukar**. Di situ jawabannya
hampir selalu bisa ditulis lewat bentuk simetris dasar, dan mencari tiap peubah adalah
jalan memutar.

Pemicu keempat: ada **akar kuadrat yang mengganggu**. Menamai akarnya, lalu menulis peubah
asalnya lewat nama itu, mengubah persamaan berakar menjadi persamaan biasa — dengan satu
harga yang wajib dibayar di akhir: nama baru itu punya batas sendiri, dan penyelesaian yang
melanggarnya harus dibuang.

## Intinya

Dua gerakan yang berbeda, sering dipakai bersama.

**Beri nama bentuk yang berulang.** Kalau $x + \frac1x$ muncul berkali-kali, sebut ia $t$.
Persamaan berderajat empat sering runtuh jadi kuadrat dengan satu penamaan:

$$x^4 + x^3 - 4x^2 + x + 1 = 0 \ \xrightarrow{\ \div x^2\ }\
\left(x^2 + \frac{1}{x^2}\right) + \left(x + \frac1x\right) - 4 = 0$$

lalu $t = x + \frac1x$ memberi $x^2 + \frac{1}{x^2} = t^2 - 2$, dan sisanya kuadrat biasa.
Polinomial dengan koefisien yang membaca sama dari depan dan belakang hampir selalu
menyerah pada gerakan ini.

**Pakai kesimetrian.** Untuk sistem yang simetris, ganti $x, y$ dengan $s = x+y$ dan
$p = xy$. Untuk tiga peubah, dengan

$$e_1 = x+y+z, \qquad e_2 = xy+yz+zx, \qquad e_3 = xyz$$

Setiap polinomial simetris bisa ditulis lewat $e_1, e_2, e_3$ — dan setelah ketiganya
diketahui, $x, y, z$ adalah akar dari

$$t^3 - e_1 t^2 + e_2 t - e_3 = 0$$

**Substitusi yang menggeser** juga sering menolong: mengganti $x = y + c$ untuk
menghilangkan suku tertentu, misalnya membuang suku kuadrat dari sebuah kubik.

## Jebakan umum

- **Lupa membatasi peubah baru.** Untuk $x$ real tak nol, $t = x + \frac1x$ hanya bisa
  bernilai $|t| \ge 2$. Solusi $t$ di luar itu tidak memberi $x$ real.
- **Membagi dengan $x^2$ tanpa memeriksa $x = 0$.** Periksa dulu apakah $x=0$ solusi.
- **Mengira semua sistem simetris.** Kalau menukar peubah mengubah persamaannya,
  gerakan ini tidak sah.
