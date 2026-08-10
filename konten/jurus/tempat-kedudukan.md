---
id: tempat-kedudukan
nama: Tempat Kedudukan
pilar: geometri
tahap: osn
prasyarat: [sudut-lingkaran, geometri-analitik, kuasa-titik]
contoh: [tkd-contoh-1]
latihan: [tkd-01, tkd-02, tkd-03, tkd-04, tkd-05, tkd-06]
---

## Kapan dipakai

Soal berbicara tentang titik yang **bergerak** sementara yang lain tetap, lalu menanyakan
jalur yang dilaluinya — atau menanyakan sesuatu yang ternyata tetap meski titiknya
berpindah. Kata pemicunya: "tentukan tempat kedudukan", "buktikan selalu melalui satu
titik tetap", "tunjukkan panjangnya tidak bergantung pada".

Pemicu kedua yang lebih halus: soal punya **satu derajat kebebasan** yang tidak dibatasi.
Kalau sebuah titik bebas bergerak pada suatu garis atau lingkaran dan pertanyaannya tidak
menyebut posisinya, jawabannya pasti tidak bergantung pada posisi itu — dan itu sendiri
petunjuk.

Pemicu ketiga: soal menanyakan **berapa banyak** titik yang memenuhi beberapa syarat
sekaligus. Jawabannya banyaknya titik potong beberapa tempat kedudukan.

## Intinya

Menentukan tempat kedudukan berarti membuktikan **dua arah**: setiap titik yang memenuhi
syarat ada pada bangun itu, dan setiap titik pada bangun itu memenuhi syaratnya. Melewatkan
arah kedua adalah kekeliruan paling sering, dan biasanya membuat jawabannya kelebihan
bagian.

**Tempat kedudukan baku yang wajib dikenali:**

| Syarat | Tempat kedudukannya |
|---|---|
| berjarak tetap dari satu titik | lingkaran |
| berjarak sama dari dua titik | sumbu ruas penghubungnya |
| berjarak sama dari dua garis berpotongan | sepasang garis bagi sudutnya |
| berjarak tetap dari sebuah garis | dua garis sejajar |
| melihat ruas $AB$ dengan sudut tetap | dua busur bercermin pada $AB$ |
| berkuasa sama terhadap dua lingkaran | garis kuasa |
| perbandingan jarak ke dua titik tetap $\ne 1$ | lingkaran Apollonius |

Dua baris terakhir yang paling sering muncul di soal olimpiade, dan keduanya paling jarang
diajarkan.

**Lingkaran Apollonius.** Tempat kedudukan titik $P$ dengan $\dfrac{PA}{PB} = k$ tetap dan
$k \ne 1$ adalah lingkaran yang diameternya menghubungkan kedua titik pembagi $AB$ — yang
membagi dalam dan yang membagi luar dengan perbandingan $k$. Untuk $k = 1$ ia merosot
menjadi sumbu ruas.

**Dua cara mengerjakannya.** Cara sintetik: kenali syaratnya sebagai salah satu baris di
tabel. Cara analitik: beri koordinat, tulis syaratnya sebagai persamaan, lalu kenali
bentuk persamaannya. Cara kedua selalu berhasil dan sering lebih panjang; cara pertama
lebih pendek kalau polanya terlihat.

## Jebakan umum

- **Hanya membuktikan satu arah.** Menunjukkan setiap titik yang memenuhi syarat ada pada
  lingkaran itu belum menjawab; harus ditunjukkan juga tidak ada titik lingkaran itu yang
  tidak memenuhi.
- **Lupa membuang titik yang tidak sah.** Tempat kedudukannya sering berupa bangun baku
  **dikurangi beberapa titik** — misalnya titik yang membuat segitiganya merosot jadi
  garis.
- **Mengira perbandingan jarak tetap memberi garis.** Hanya kalau perbandingannya $1$;
  selain itu lingkaran Apollonius.
- **Menganggap kasus merosot tidak perlu disebut.** Nilai $k = 1$ dan sudut $90^\circ$
  sering mengubah bentuk jawabannya, dan pemeriksa mencari keduanya.
