---
id: sdl-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [sudut-lingkaran]
bentuk: isian
kesulitan: 3
jawaban: "120"
---

## Soal

Titik $A$, $B$, dan $C$ terletak pada lingkaran berpusat $O$, dengan $O$ di dalam segitiga
$ABC$. Diketahui $\angle OAB = 25^\circ$ dan $\angle OCB = 35^\circ$.

![Lingkaran berpusat O dengan tiga titik A, B, dan C di kelilingnya: A di kiri bawah, B di atas, dan C di kanan. Ketiganya dihubungkan ke O oleh jari-jari, dan tali busur AB serta BC digambar. Sudut OAB besarnya 25 derajat, sudut OCB besarnya 35 derajat, dan sudut AOC ditanyakan](lingkaran-tiga-jari-jari.svg)

Tentukan besar $\angle AOC$ dalam derajat, yakni sudut yang tidak memuat $B$ di dalamnya.

## Petunjuk

- Ketiga ruas dari $O$ ke keliling punya satu sifat bersama yang tidak disebut soal. Apa akibatnya pada segitiga-segitiga kecil di gambar?
- $OA = OB = OC$ karena ketiganya jari-jari, jadi $\triangle OAB$ dan $\triangle OBC$ dua-duanya sama kaki.
- Cari $\angle AOB$ dan $\angle BOC$ lebih dulu, lalu ingat bahwa ketiga sudut di titik $O$ berjumlah $360^\circ$.

## Pembahasan

**Panen sifat yang tidak disebut soal.** Karena $A$, $B$, $C$ pada lingkaran berpusat $O$,

$$OA = OB = OC$$

Akibatnya $\triangle OAB$ dan $\triangle OBC$ keduanya segitiga **sama kaki** — dan segitiga
sama kaki mengubah sudut yang diketahui menjadi sudut kedua secara cuma-cuma.

**Kerjakan $\triangle OAB$.** Karena $OA = OB$, sudut alasnya sama besar:

$$\angle OBA = \angle OAB = 25^\circ$$

$$\angle AOB = 180^\circ - 25^\circ - 25^\circ = 130^\circ$$

**Kerjakan $\triangle OBC$.** Karena $OB = OC$,

$$\angle OBC = \angle OCB = 35^\circ$$

$$\angle BOC = 180^\circ - 35^\circ - 35^\circ = 110^\circ$$

**Tutup putarannya.** Ketiga sudut di sekeliling titik $O$ berjumlah satu putaran penuh:

$$\angle AOB + \angle BOC + \angle AOC = 360^\circ$$

$$130^\circ + 110^\circ + \angle AOC = 360^\circ \quad \Longrightarrow \quad
\angle AOC = \boxed{120^\circ}$$

### Periksa lewat sudut keliling

Sudut $\angle ABC$ adalah sudut keliling yang menghadap busur $AC$ yang tidak memuat $B$, dan
$\angle AOC$ adalah sudut pusat yang menghadap busur yang sama. Jadi seharusnya
$\angle AOC = 2 \angle ABC$.

Dari perhitungan tadi,

$$\angle ABC = \angle ABO + \angle OBC = 25^\circ + 35^\circ = 60^\circ$$

dan benar $2 \times 60^\circ = 120^\circ$ ✓.

Pemeriksaan ini bukan sekadar penenang hati — ia memakai hubungan yang **berbeda** dari yang
dipakai saat menghitung, jadi kekeliruan di jalan pertama tidak akan ikut terbawa ke jalan
kedua.

### Bentuk umum yang layak dikenali

Perhitungan di atas berlaku untuk sudut berapa pun. Kalau $\angle OAB = \alpha$ dan
$\angle OCB = \gamma$, cara yang sama memberi $\angle ABC = \alpha + \gamma$. Jadi:

> Sudut sebuah segitiga sama dengan **jumlah** kedua sudut yang dibentuk jari-jari lingkaran
> luar dengan kedua sisinya di titik itu.

### Mengapa syarat "$O$ di dalam segitiga" perlu

Kalau $\angle ABC$ tumpul, pusat lingkaran jatuh **di luar** $\triangle ABC$, dan ketiga sudut
di $O$ tidak lagi berjumlah $360^\circ$ dengan cara yang sama — salah satunya menjadi selisih,
bukan jumlah. Perhitungannya masih bisa dijalankan, tetapi baris "$130 + 110 + x = 360$"
berubah bentuk.

Karena itu syarat pada soal bukan hiasan. Setiap kali kamu memakai penjumlahan sudut di
sekeliling satu titik, periksa dulu bahwa titik itu memang berada di tempat yang kamu kira.
