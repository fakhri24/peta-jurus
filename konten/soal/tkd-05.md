---
id: tkd-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [tempat-kedudukan]
bentuk: uraian
kesulitan: 5
---

## Soal

Diberikan dua titik tetap $B$ dan $C$, dan sebuah bilangan real $k$.

**(a)** Buktikan bahwa tempat kedudukan titik $X$ yang memenuhi

$$XB^2 - XC^2 = k$$

adalah sebuah garis yang tegak lurus $BC$, dan buktikan kedua arahnya.

**(b)** Simpulkan bahwa untuk sembarang dua titik $A$ dan $D$ berlaku

$$AD \perp BC \quad \Longleftrightarrow \quad AB^2 - AC^2 = DB^2 - DC^2$$

**(c)** Dengan memakai (b), buktikan bahwa ketiga garis tinggi sebuah segitiga
berpotongan di satu titik.

## Petunjuk

- Untuk (a), beri koordinat dengan $BC$ pada sumbu-$x$. Tuliskan syaratnya, lalu perhatikan suku mana yang saling menghapus.
- Setelah suku $y^2$ hilang, yang tersisa persamaan yang tidak memuat $y$ sama sekali — dan persamaan seperti itu menggambarkan garis tegak.
- Untuk (b), pikirkan $A$ dan $D$ sebagai dua titik pada tempat kedudukan yang sama. Garis mana yang menghubungkan keduanya?
- Untuk (c), namai $H$ titik potong dua garis tinggi, tulis apa yang diberikan (b) untuk masing-masing, lalu jumlahkan.

## Pembahasan

### Bagian (a)

Taruh $B = (0,0)$ dan $C = (d, 0)$ dengan $d = BC > 0$. Untuk $X = (x,y)$:

$$XB^2 - XC^2 = \left(x^2 + y^2\right) - \left[(x-d)^2 + y^2\right]$$

Suku $y^2$ saling menghapus — itu kejadian pokok seluruh soal ini:

$$XB^2 - XC^2 = x^2 - x^2 + 2dx - d^2 = 2dx - d^2$$

**Arah pertama.** Kalau $XB^2 - XC^2 = k$, maka $2dx - d^2 = k$, sehingga

$$x = \frac{k + d^2}{2d}$$

Nilai $x$ itu tunggal dan tidak memuat $y$, jadi $X$ terletak pada garis tegak
$x = \dfrac{k+d^2}{2d}$ — sebuah garis tegak lurus $BC$ ✓

**Arah kedua.** Sebaliknya, ambil sembarang titik pada garis itu, yaitu
$X = \left(\tfrac{k+d^2}{2d},\ y\right)$ dengan $y$ apa saja. Hitungan yang sama memberi

$$XB^2 - XC^2 = 2d \cdot \frac{k+d^2}{2d} - d^2 = k + d^2 - d^2 = k$$

jadi setiap titik garis itu memenuhi syaratnya ✓

Kedua arah terbukti $\blacksquare$

Perhatikan bahwa **tidak ada nilai $k$ yang gagal**: berapa pun $k$, garis itu ada, dan
letaknya bergeser sepanjang $BC$ mengikuti $k$. Untuk $k = 0$ diperoleh $x = \tfrac{d}{2}$
— sumbu ruas $BC$, seperti seharusnya, sebab $XB = XC$.

### Bagian (b)

Sebut $k = AB^2 - AC^2$. Menurut (a), tempat kedudukan titik $X$ dengan
$XB^2 - XC^2 = k$ adalah satu garis $\ell$ tegak lurus $BC$ — dan $A$ ada pada $\ell$.

Karena tegak lurus $BC$ menentukan arah garisnya, $\ell$ adalah **satu-satunya** garis
yang melalui $A$ dan tegak lurus $BC$.

Sekarang untuk $D \ne A$:

$$AD \perp BC
\iff D \text{ ada pada garis lewat } A \text{ yang tegak lurus } BC
\iff D \in \ell$$

$$\iff DB^2 - DC^2 = k = AB^2 - AC^2$$

Langkah terakhir itu memakai **kedua arah** bagian (a): "$D \in \ell \Rightarrow$
selisihnya $k$" adalah arah kedua, dan "selisihnya $k \Rightarrow D \in \ell$" arah
pertama. Tanpa salah satunya, kesetaraan ini tidak tertutup $\blacksquare$

### Bagian (c)

Ambil segitiga $ABC$. Garis tinggi dari $A$ dan garis tinggi dari $B$ tidak sejajar
— yang satu tegak lurus $BC$, yang lain tegak lurus $CA$, dan $BC$ tidak sejajar $CA$.
Jadi keduanya berpotongan; sebut titik potongnya $H$.

**Singkirkan dulu kasus $H$ berimpit dengan titik sudut.** Kalau $H = A$, maka garis
tinggi dari $B$ melalui $A$, sehingga $BA \perp CA$ dan segitiganya siku-siku di $A$.
Dalam hal itu garis tinggi dari $C$ adalah garis $CA$ sendiri, yang juga melalui
$A = H$ — jadi ketiganya bertemu di $A$ dan tidak ada yang perlu dibuktikan lagi. Kasus
$H = B$ senada. Selanjutnya anggap $H \ne A$ dan $H \ne B$, supaya $AH$ dan $BH$ memang
garis.

**Terjemahkan tiap garis tinggi dengan (b).**

Dari $AH \perp BC$:

$$AB^2 - AC^2 = HB^2 - HC^2 \tag{1}$$

Dari $BH \perp CA$:

$$BC^2 - BA^2 = HC^2 - HA^2 \tag{2}$$

**Jumlahkan (1) dan (2).** Di ruas kanan, $HC^2$ saling menghapus:

$$AB^2 - AC^2 + BC^2 - BA^2 = HB^2 - HA^2$$

Di ruas kiri, $AB^2$ dan $BA^2$ saling menghapus:

$$BC^2 - AC^2 = HB^2 - HA^2$$

Tulis ulang dengan urutan yang cocok untuk (b), yaitu selisih terhadap $A$ lalu $B$:

$$CA^2 - CB^2 = HA^2 - HB^2$$

Menurut (b) — dipakai pada pasangan titik $C$, $H$ dan ruas $AB$ — itu tepat berarti

$$CH \perp AB$$

Jadi garis $CH$ adalah garis tinggi dari $C$, sehingga garis tinggi ketiga juga melalui
$H$. Ketiganya berpotongan di satu titik $\blacksquare$

Titik itu adalah **titik tinggi** segitiga $ABC$.

### Kenapa bukti ini rapi

Bukti baku kesejajaran garis tinggi biasanya lewat segitiga bantu: perbesar $ABC$
menjadi segitiga yang garis tingginya menjadi sumbu ruas. Bukti itu bagus tetapi
memerlukan konstruksi tambahan.

Bukti di atas tidak memerlukan konstruksi apa pun. Yang dikerjakannya adalah menukar
**tegak lurus** — hubungan yang sulit dijumlahkan — menjadi **selisih kuadrat jarak** —
besaran yang boleh dijumlahkan begitu saja. Setelah pertukaran itu, seluruh isinya cuma
dua suku yang saling menghapus.

Pola itu berlaku umum, dan layak dibawa ke soal lain: **kalau beberapa syarat tegak lurus
harus digabungkan, ubah dulu masing-masing menjadi persamaan selisih kuadrat.**

### Hubungannya dengan garis kuasa

Bandingkan bagian (a) dengan soal garis kuasa. Kuasa titik $X$ terhadap lingkaran
berpusat $B$ berjari-jari $R_1$ adalah $XB^2 - R_1^2$, jadi syarat kuasa sama berbunyi

$$XB^2 - R_1^2 = XC^2 - R_2^2 \quad \Longleftrightarrow \quad XB^2 - XC^2 = R_1^2 - R_2^2$$

Itu persis bentuk bagian (a) dengan $k = R_1^2 - R_2^2$. Jadi **garis kuasa dua lingkaran
adalah kasus khusus tempat kedudukan ini**, dan alasan garis kuasa selalu tegak lurus
garis pusat adalah alasan yang sama: suku $y^2$ saling menghapus.

Sekalian keluar bahwa ketiga garis kuasa dari tiga lingkaran berpotongan di satu titik —
dibuktikan dengan penjumlahan yang persis sama seperti bagian (c).

## Rubrik

- **(a)** Memberi koordinat dengan $BC$ pada satu sumbu, dan menunjukkan suku $y^2$
  saling menghapus
- **(a)** Menyelesaikan $x$ dan menyatakan bahwa jawabannya tidak memuat $y$, sehingga
  garisnya tegak lurus $BC$
- **(a)** Mengerjakan **arah kedua** secara terpisah — mengambil sembarang titik pada
  garis itu dan menghitung ulang selisihnya
- **(b)** Menyatakan bahwa garis lewat $A$ yang tegak lurus $BC$ hanya satu, dan bahwa
  garis itulah tempat kedudukan dari (a)
- **(b)** Merangkai kesetaraannya dengan kedua arah (a) terpakai
- **(c)** Mendefinisikan $H$ sebagai perpotongan dua garis tinggi, **beserta alasan
  keduanya memang berpotongan**
- **(c)** Menuliskan kedua persamaan dari (b) dan menjumlahkannya
- **(c)** Menyimpulkan $CH \perp AB$ lewat (b), bukan lewat pengamatan gambar

Bukti (c) dengan cara lain — segitiga bantu, koordinat, atau vektor — dinilai penuh,
asalkan lengkap. Bukti yang menyatakan "ketiga garis tinggi jelas bertemu karena
gambarnya begitu" tidak memperoleh angka untuk bagian (c).
