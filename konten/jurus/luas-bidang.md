---
id: luas-bidang
nama: Luas dan Perbandingan Luas
pilar: geometri
tahap: osn-k
prasyarat: [pythagoras]
contoh: [lb-contoh-1]
latihan: [lb-01, lb-02, lb-03, lb-04, lb-05, lb-06]
---

## Kapan dipakai

Yang ditanyakan luas suatu daerah yang **bukan bangun baku** — daerah beririsan, daerah
sisa, atau bagian yang dipotong beberapa garis. Jalannya jarang menghitung langsung;
biasanya memecah jadi bangun yang dikenal, atau mengurangkan dari yang lebih besar.

Pemicu kedua, dan ini yang khas olimpiade: soal memberi **perbandingan** pada suatu sisi
lalu menanyakan perbandingan luas. Di situ luas dipakai sebagai alat, bukan sebagai
jawaban.

Pemicu ketiga yang paling sering luput: soal menanyakan **panjang** — misalnya jarak dari
satu titik ke suatu garis. Menghitung luas segitiga yang sama dengan dua cara berbeda
sering menyelesaikannya dalam satu baris.

## Intinya

**Luas segitiga**, dipilih menurut yang diketahui:

$$L = \tfrac{1}{2} a t = \tfrac{1}{2} ab \sin C = \sqrt{s(s-a)(s-b)(s-c)}$$

dengan $s$ setengah keliling. Bentuk terakhir (Heron) dipakai kalau yang diketahui hanya
ketiga sisinya.

Dua bentuk lain yang menyambung ke jurus lingkaran:

$$L = rs, \qquad L = \frac{abc}{4R}$$

dengan $r$ jari-jari lingkaran dalam dan $R$ jari-jari lingkaran luar. Keduanya sering
jadi jembatan antara soal panjang dan soal lingkaran.

**Dua perbandingan yang menyelesaikan sebagian besar soal:**

- Dua segitiga dengan **tinggi sama** punya perbandingan luas sama dengan perbandingan
  alasnya. Karena itu garis dari titik sudut membagi luas menurut perbandingan pada sisi
  seberangnya.
- Dua segitiga dengan **satu sudut sama besar** punya perbandingan luas
  $\dfrac{L_1}{L_2} = \dfrac{ab}{a'b'}$, dengan $a,b$ dan $a',b'$ sisi-sisi yang mengapit
  sudut itu.

**Luas sebagai persamaan.** Menghitung satu luas dengan dua cara berbeda menghasilkan
persamaan — itu inti banyak soal, termasuk cara termurah membuktikan Heron dipakai dengan
benar.

## Jebakan umum

- **Memakai sisi sebagai tinggi.** Tinggi harus tegak lurus alas yang dipilih; pada
  segitiga tumpul kakinya bisa jatuh di luar segitiga.
- **Perbandingan luas dianggap sama dengan perbandingan sisi.** Kalau bangunnya sebangun
  dengan perbandingan $k$, luasnya berbanding $k^2$.
- **Heron dipakai tanpa memeriksa segitiganya ada.** Kalau ketiga panjangnya tidak
  memenuhi ketaksamaan segitiga, akarnya menjadi bilangan khayal — dan itu tanda soalnya
  dibaca keliru, bukan tanda jawabannya rumit.
- **Menjumlahkan luas daerah yang beririsan.** Bagian yang termasuk dua daerah terhitung
  dua kali; ini inklusi-eksklusi dalam bentuk geometri.
