---
id: ktg-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [ketaksamaan-geometri]
bentuk: uraian
kesulitan: 4
---

## Soal

Misalkan $a$, $b$, $c$ panjang sisi sebuah segitiga.

**(a)** Buktikan bahwa

$$\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \ <\ 2$$

**(b)** Tunjukkan bahwa angka $2$ tidak bisa diperkecil: untuk setiap $\varepsilon > 0$
ada segitiga yang membuat jumlah itu lebih besar daripada $2 - \varepsilon$.

**(c)** Buktikan bahwa untuk **sembarang** bilangan positif $a$, $b$, $c$ — tanpa syarat
segitiga — jumlah yang sama selalu paling sedikit $\dfrac{3}{2}$.

## Petunjuk

- Pada bagian (a), tiap suku ditaksir sendiri-sendiri. Yang diketahui tentang penyebutnya cuma satu hal, dan hal itu datang dari syarat ketiga sisinya.
- Ganti penyebut $b+c$ dengan sesuatu yang lebih kecil tetapi seragam untuk ketiga suku — dan $\tfrac{a+b+c}{2}$ adalah calonnya.
- Untuk (b), jangan cari segitiga yang hampir sama kaki. Coba $a = 1$, $b = t$, $c = t + \tfrac12$ dengan $t$ besar.
- Untuk (c), pasangkan tiap suku dengan $1$: perhatikan bahwa $\dfrac{a}{b+c} + 1 = \dfrac{a+b+c}{b+c}$.

## Pembahasan

### Bagian (a)

**Yang diketahui tentang penyebutnya.** Syarat segitiga memberi $b + c > a$. Tambahkan
$b+c$ ke kedua ruas:

$$2(b+c) > a+b+c \quad \Longrightarrow \quad b+c > \frac{a+b+c}{2}$$

**Perkecil penyebutnya, perbesar pecahannya.** Karena $a > 0$ dan penyebutnya positif,
mengganti $b+c$ dengan sesuatu yang lebih kecil membuat pecahannya lebih besar:

$$\frac{a}{b+c} \ <\ \frac{a}{\frac{a+b+c}{2}} = \frac{2a}{a+b+c}$$

Dua ketaksamaan senada berlaku untuk kedua suku lainnya. Jumlahkan ketiganya:

$$\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b}
\ <\ \frac{2a + 2b + 2c}{a+b+c} = 2 \qquad \blacksquare$$

Perhatikan bahwa ketaksamaannya **tegas**, sebab $b+c > a$ tegas untuk segitiga
sungguhan.

### Bagian (b)

Batas $2$ tidak pernah tercapai, tetapi bisa didekati sedekat-dekatnya. Ambil

$$a = 1, \qquad b = t, \qquad c = t + \tfrac12 \qquad (t > \tfrac12)$$

Ketiganya sisi segitiga: $a + b = t+1 > t + \tfrac12 = c$ ✓, dan dua syarat lainnya jelas.

$$\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b}
= \frac{1}{2t + \tfrac12} + \frac{t}{t + \tfrac32} + \frac{t + \tfrac12}{t+1}$$

Untuk $t \to \infty$: suku pertama menuju $0$, dan kedua suku sisanya masing-masing
menuju $1$. Jadi jumlahnya menuju $2$, dan untuk $t$ yang cukup besar ia melampaui
$2 - \varepsilon$ berapa pun $\varepsilon > 0$ ✓

| $t$ | sisi | jumlah |
|---|---|---|
| $1$ | $1, 1, \tfrac32$ | $\approx 1{,}550$ |
| $5$ | $1, 5, \tfrac{11}{2}$ | $\approx 1{,}781$ |
| $50$ | $1, 50, \tfrac{101}{2}$ | $\approx 1{,}971$ |
| $500$ | $1, 500, \tfrac{1001}{2}$ | $\approx 1{,}997$ |

**Segitiga yang mana yang mendekatkannya.** Ini bagian yang paling mudah keliru.
Segitiga merosot yang **sama kaki** — $a = b = 1$, $c \to 2$ — tidak membawa ke $2$
sama sekali:

$$\frac{1}{1+c} + \frac{1}{c+1} + \frac{c}{2} \ \longrightarrow\
\frac13 + \frac13 + 1 = \frac53 \approx 1{,}667$$

Yang diperlukan bukan sekadar merosot, melainkan merosot **dan** timpang: satu sisi
jauh lebih pendek daripada dua sisi lain yang panjangnya hampir sama. Di situ dua suku
terakhir masing-masing mendekati $1$ sementara suku pertama menghilang.

### Bagian (c)

Tambahkan $1$ ke tiap suku:

$$\frac{a}{b+c} + 1 = \frac{a+b+c}{b+c}$$

Sebut $S = a+b+c$. Maka

$$\left(\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b}\right) + 3
= S\left(\frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b}\right)$$

Ketiga penyebut itu berjumlah $2S$. Dengan AM-HM pada ketiganya,

$$\frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b} \ \ge\ \frac{9}{(b+c)+(c+a)+(a+b)} = \frac{9}{2S}$$

sehingga

$$\left(\text{jumlah}\right) + 3 \ \ge\ S \cdot \frac{9}{2S} = \frac92
\quad \Longrightarrow \quad \text{jumlah} \ \ge\ \frac92 - 3 = \frac32 \qquad \blacksquare$$

Kesamaannya tepat ketika ketiga penyebutnya sama, yaitu $a = b = c$.

### Yang sebenarnya diajarkan soal ini

Dua batas, dan cuma **satu** yang memerlukan syarat segitiga:

| Batas | Perlu syarat segitiga? | Tercapai? |
|---|---|---|
| $\ge \tfrac32$ | tidak — berlaku untuk positif sembarang | ya, saat $a=b=c$ |
| $< 2$ | **ya** | tidak, hanya didekati |

Tanpa syarat segitiga, batas atasnya hilang sama sekali: ambil $a = 1$, $b = c = \delta$
dengan $\delta$ kecil, maka $\dfrac{a}{b+c} = \dfrac{1}{2\delta}$ membesar tanpa batas.

Itulah jebakan pertama yang ditulis di halaman jurus ini — memperlakukan $a$, $b$, $c$
sebagai peubah bebas. Pada bagian (c) perlakuan itu sah dan tidak merugikan apa pun;
pada bagian (a) ia menghapus satu-satunya bahan yang membuat pernyataannya benar.

### Catatan tentang (c)

Ketaksamaan pada bagian (c) dikenal sebagai **ketaksamaan Nesbitt**. Buktinya di atas
memakai AM-HM; jalur lain lewat substitusi $u = b+c$, $v = c+a$, $w = a+b$ atau lewat
penataan ulang. Semuanya tidak menyentuh syarat segitiga sedikit pun — dan memang tidak
perlu.

## Rubrik

- **(a)** Menurunkan $b+c > \tfrac{a+b+c}{2}$ dari syarat segitiga, dengan langkahnya
  terlihat
- **(a)** Menyatakan bahwa memperkecil penyebut memperbesar pecahan — dan bahwa itu sah
  karena pembilang serta penyebutnya positif
- **(a)** Menjumlahkan ketiga taksiran dan menyimpulkan batas $2$; ketaksamaan tegas,
  bukan $\le$
- **(b)** Memberi satu keluarga segitiga yang eksplisit **beserta pemeriksaan bahwa
  ketiganya memang sisi segitiga**, lalu menghitung limitnya
- **(b)** Menyebut bahwa segitiga merosot yang sama kaki **tidak** cukup, atau setidaknya
  memilih keluarga yang timpang dengan sadar
- **(c)** Bukti lengkap batas $\tfrac32$ dengan satu ketaksamaan baku yang disebut namanya
- **(c)** Menyatakan syarat kesamaannya $a=b=c$

Bagian (b) dinilai penuh untuk keluarga mana pun yang sah — misalnya $a=1$, $b=t$,
$c=t+1$ — asalkan syarat segitiganya diperiksa dan limitnya dihitung, bukan hanya
ditebak dari satu-dua contoh angka.
