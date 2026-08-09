---
id: eks-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: isian
kesulitan: 4
jawaban: "25"
---

## Soal

Sebuah graf memiliki $10$ titik dan **tidak memuat segitiga** — yaitu tidak ada tiga titik
yang ketiganya saling terhubung.

Paling banyak ada berapa ruas pada graf itu?

## Petunjuk

- Pilih titik yang berderajat **terbesar**, lalu perhatikan tetangga-tetangganya.
- Kalau grafnya tanpa segitiga, dua tetangga dari titik yang sama tidak boleh saling terhubung.
- Setelah batasnya diperoleh, tunjukkan batas itu tercapai dengan memberi contoh graf yang nyata.

## Pembahasan

Soal seperti ini selalu punya dua bagian: **batas atas** yang dibuktikan, dan **contoh** yang
mencapainya.

### Bagian 1 — batas atasnya

**Pilih titik berderajat terbesar,** sebut $v$ dengan $\deg(v) = d$. Pilihan ini sah karena
titiknya berhingga.

**Tetangga $v$ tidak saling terhubung.** Kalau dua tetangga $v$ terhubung, ketiganya bersama
$v$ membentuk segitiga — yang dilarang. Jadi himpunan tetangga $v$, sebut $A$ dengan
$|A| = d$, tidak punya ruas di dalamnya.

Sebut $B$ himpunan titik sisanya, $|B| = 10 - d$.

**Setiap ruas menyentuh $B$.** Karena $A$ tidak punya ruas di dalamnya, tiap ruas punya
sedikitnya satu ujung di $B$.

**Hitung ruasnya lewat derajat titik di $B$.** Tiap titik berderajat paling banyak $d$ —
sebab $v$ yang terbesar:

$$|E| \ \le\ \sum_{u \in B} \deg(u) \ \le\ |B| \cdot d = (10-d)\,d$$

**Maksimumkan batasnya.** Bentuk $d(10-d)$ mencapai nilai terbesar di $d = 5$:

$$5 \times 5 = 25$$

Jadi $|E| \le 25$.

### Bagian 2 — batas itu tercapai

Ambil graf bipartit lengkap $K_{5,5}$: bagi kesepuluh titik menjadi dua kelompok berisi lima,
lalu hubungkan setiap titik pada kelompok pertama dengan setiap titik pada kelompok kedua.

$$|E| = 5 \times 5 = 25$$

**Graf ini tidak memuat segitiga.** Segitiga menuntut tiga titik yang saling terhubung, dan
di antara tiga titik mana pun pasti ada dua yang sekelompok — sedangkan titik sekelompok
tidak pernah terhubung.

Karena batas atasnya $25$ dan ada graf yang mencapainya:

$$\boxed{25}$$

### Mengapa kedua bagian diperlukan

Bagian 1 saja hanya menunjukkan ruasnya **tidak lebih dari** $25$; mungkin saja yang
sebenarnya bisa dicapai hanya $20$. Bagian 2 saja hanya menunjukkan $25$ **bisa** dicapai;
mungkin ada graf lain dengan lebih banyak ruas.

Soal "paling banyak berapa" selalu menuntut keduanya, dan jawaban yang hanya memuat satu di
antaranya belum selesai.

### Bentuk umumnya

Hasil ini dikenal sebagai **teorema Mantel**: graf tanpa segitiga dengan $n$ titik punya
paling banyak

$$\left\lfloor \frac{n^{2}}{4} \right\rfloor$$

ruas, dan batas itu dicapai oleh graf bipartit lengkap yang kedua kelompoknya sama besar
(atau berbeda satu, kalau $n$ ganjil).

Periksa untuk $n = 10$: $\left\lfloor \frac{100}{4} \right\rfloor = 25$. Untuk $n = 5$:
$\left\lfloor \frac{25}{4} \right\rfloor = 6$, dicapai oleh $K_{2,3}$.

Perhatikan bahwa bagian yang menuntut gagasan adalah pemilihan titik berderajat terbesar.
Tanpa sifat "terbesar" itu, ketaksamaan $\deg(u) \le d$ tidak punya alasan, dan seluruh
hitungannya runtuh.
