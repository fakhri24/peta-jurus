---
id: eks-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: uraian
kesulitan: 5
---

## Soal

Sebuah graf dengan $n$ titik bersifat **terhubung** — setiap dua titik dapat dihubungkan
lewat rangkaian ruas.

Buktikan bahwa graf itu punya paling sedikit $n-1$ ruas, dan bahwa graf yang tepat punya
$n-1$ ruas **tidak memuat siklus**.

Buktikan bagian pertama dengan prinsip ekstremal.

## Petunjuk

- Untuk bagian pertama, ambil bagian graf yang **terbesar** yang bisa dibangun dengan sedikit ruas, lalu tunjukkan ia harus mencakup seluruh titik.
- Bangun bertahap: mulai dari satu titik, lalu tambahkan ruas yang menyambungkan titik baru. Berapa titik yang bertambah tiap kali?
- Untuk bagian kedua, andaikan ada siklus lalu buang satu ruas darinya, dan periksa apakah grafnya masih terhubung.

## Pembahasan

### Bagian 1 — paling sedikit $n-1$ ruas

**Bangun bertahap dan pilih yang terbesar.** Tinjau seluruh himpunan bagian ruas $F$ yang
tidak memuat siklus, dan pilih $F$ yang **terbanyak ruasnya**. Pilihan ini sah karena
banyaknya ruas berhingga.

Sebut $c$ banyaknya bagian terhubung yang dibentuk $F$ pada himpunan titik graf.

**Amati hubungan antara $|F|$ dan $c$.** Mulai dari keadaan tanpa ruas sama sekali: ada $n$
bagian, satu untuk tiap titik. Tiap kali sebuah ruas dari $F$ ditambahkan, ia
menyambungkan **dua bagian yang berbeda** — kalau kedua ujungnya sudah sebagian, ruas itu
akan menutup siklus, yang dilarang. Jadi tiap ruas mengurangi banyaknya bagian tepat satu:

$$c = n - |F|$$

**Klaim: $c = 1$.** Andaikan $c \ge 2$, yaitu $F$ meninggalkan sedikitnya dua bagian
terpisah. Karena grafnya terhubung, ada ruas $e$ pada graf yang menghubungkan dua bagian
berbeda itu. Menambahkan $e$ ke $F$ tidak menutup siklus — kedua ujungnya berada di bagian
yang berlainan — sehingga $F \cup \{e\}$ juga tanpa siklus dan **lebih banyak ruasnya**.

Itu bertentangan dengan pemilihan $F$ sebagai yang terbanyak. Maka $c = 1$.

**Simpulkan.** Dari $c = n - |F| = 1$ diperoleh $|F| = n-1$. Karena $F$ himpunan bagian dari
seluruh ruas graf:

$$|E| \ \ge\ |F| = n-1 \qquad \blacksquare$$

### Bagian 2 — kalau tepat $n-1$, tidak ada siklus

Andaikan grafnya terhubung, punya tepat $n-1$ ruas, tetapi memuat sebuah siklus $C$.

Ambil sebarang ruas $e$ pada siklus itu, lalu buang. **Grafnya tetap terhubung**: setiap
lintasan yang tadinya memakai $e$ dapat dialihkan lewat sisa siklus $C$, yang masih utuh
menghubungkan kedua ujung $e$.

Sekarang grafnya terhubung dengan $n$ titik dan hanya

$$(n-1) - 1 = n-2$$

ruas. Itu bertentangan dengan Bagian 1, yang menuntut paling sedikit $n-1$ ruas.

Maka graf itu tidak memuat siklus. $\blacksquare$

### Mengapa objek yang dipilih adalah "himpunan ruas tanpa siklus yang terbanyak"

Sifat "terbanyak" dipakai tepat sekali, dan di tempat yang menentukan: ia yang membuat
penambahan ruas $e$ menjadi pertentangan. Kalau yang dipilih sembarang himpunan tanpa
siklus, penambahan itu tidak melanggar apa pun.

Perhatikan juga bahwa besaran yang dipilih harus punya **dua sifat sekaligus**: dibatasi oleh
syarat soal (tanpa siklus) dan diperbesar sampai mentok (terbanyak). Objek hasil pemilihan
itu — pohon rentang — adalah bangun yang berulang kali muncul di soal graf.

### Rangkumannya

Bagian 1 dan 2 bersama-sama memberi ciri pohon:

> Graf terhubung dengan $n$ titik punya tepat $n-1$ ruas **tepat ketika** ia tidak memuat
> siklus.

Batas $n-1$ itu ketat dari kedua arah: graf terhubung tidak bisa punya lebih sedikit, dan
graf tanpa siklus tidak bisa punya lebih banyak. Pohon adalah satu-satunya yang mencapai
keduanya.

## Rubrik

- Memilih himpunan ruas tanpa siklus yang terbanyak, dan menyebut alasan keberadaannya
- Menyatakan hubungan $c = n - |F|$, dengan alasan tiap ruas menyambungkan dua bagian berbeda
- Mengandaikan $c \ge 2$, lalu membangun himpunan yang lebih besar dengan menambahkan ruas penghubung
- Menyatakan pertentangannya dengan pemilihan terbanyak, lalu menyimpulkan $|E| \ge n-1$
- Bagian 2: mengandaikan ada siklus dan membuang satu ruas darinya
- Bagian 2: menunjukkan grafnya tetap terhubung, dengan alasan lintasan dapat dialihkan
- Bagian 2: menurunkan pertentangan dengan hasil Bagian 1
