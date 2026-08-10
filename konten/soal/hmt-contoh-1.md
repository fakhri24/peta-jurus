---
id: hmt-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: geometri
tahap: osn
jurus: [homoteti]
bentuk: isian
kesulitan: 4
jawaban: "8"
---

## Soal

Dua lingkaran berjari-jari $3$ dan $9$ bersinggungan dari dalam di titik $T$. Sebuah garis
melalui $T$ memotong lingkaran kecil lagi di $P$ dan lingkaran besar lagi di $Q$. Diketahui
$TP = 4$.

![Dua lingkaran bersinggungan dari dalam di titik T yang berada di sebelah kanan. Lingkaran besar berjari-jari 9 berpusat di O, dan lingkaran kecil berjari-jari 3 berada di dalamnya, menempel di T. Sebuah garis lurus ditarik dari T ke arah kiri atas; ia memotong lingkaran kecil di titik P dan meneruskan sampai memotong lingkaran besar di titik Q, dengan P terletak di antara T dan Q. Panjang TP adalah 4, sedangkan PQ belum diketahui](dua-lingkaran-dalam-garis.svg)

Tentukan panjang $PQ$.

## Petunjuk

- Soal tidak menyebutkan arah garisnya, jadi jawabannya tidak boleh bergantung pada arah itu. Apa yang tetap untuk semua garis lewat $T$?
- Titik singgung dua lingkaran adalah pusat homoteti yang memetakan lingkaran satu ke lingkaran lainnya. Berapa faktornya?
- Faktornya nisbah jari-jarinya, $k = \tfrac93 = 3$, dan homoteti itu memetakan $P$ ke $Q$.

## Pembahasan

**Kenali pusat homotetinya.** Kedua lingkaran bersinggungan di $T$, jadi $T$ adalah pusat
homoteti yang memetakan lingkaran kecil ke lingkaran besar. Faktornya nisbah jari-jarinya:

$$k = \frac{9}{3} = 3$$

Karena keduanya bersinggungan **dari dalam** — lingkaran kecil ada di dalam yang besar —
faktornya positif, sehingga bayangan sebuah titik terletak sepihak dengan aslinya terhadap
$T$.

**Terapkan pada $P$.** Homoteti berpusat $T$ memetakan tiap titik lingkaran kecil ke titik
lingkaran besar, dan ia memetakan garis lewat $T$ ke dirinya sendiri. Jadi bayangan $P$
adalah titik lain tempat garis itu memotong lingkaran besar, yaitu $Q$:

$$TQ = k \cdot TP = 3 \times 4 = 12$$

**Selesaikan.** Karena $k > 0$, titik $P$ berada di antara $T$ dan $Q$:

$$PQ = TQ - TP = 12 - 4 = \boxed{8}$$

### Periksa dengan koordinat

Taruh pusat lingkaran besar di $O(0,0)$ dengan jari-jari $9$, sehingga $T(9,0)$. Lingkaran
kecil berjari-jari $3$ dan menyinggung dari dalam di $T$, jadi pusatnya $O_1(6,0)$.

Untuk garis lewat $T$ dengan arah satuan $\vec u$, titik potong keduanya diperoleh dari
$\left|T + t\vec u - O\right| = $ jari-jari, yang memberi

$$t = -2\left(T - O\right)\cdot \vec u$$

Untuk lingkaran kecil, $T - O_1 = (3,0)$, jadi $TP = -6u_x$; untuk lingkaran besar,
$T - O = (9,0)$, jadi $TQ = -18u_x$. Nisbahnya **selalu** $3$, apa pun arah $\vec u$ ✓

Agar $TP = 4$, ambil $u_x = -\tfrac23$. Maka $TQ = 12$ dan $PQ = 8$ ✓

Perhitungan ini sekaligus menunjukkan mengapa jawabannya tidak bergantung pada arah
garisnya: kedua panjangnya sama-sama sebanding dengan $u_x$, dan faktor itu lenyap saat
dibagi.

### Kenapa homoteti, bukan kuasa titik

Godaannya memakai kuasa titik, sebab ada dua lingkaran dan sebuah garis. Tetapi kuasa titik
bekerja pada **satu** lingkaran dengan dua garis; di sini keadaannya terbalik — satu garis,
dua lingkaran. Alat untuk itu homoteti.

Pembeda praktisnya: kuasa titik menghubungkan **hasil kali** panjang, homoteti
menghubungkan **nisbah** panjang. Soal ini memberi satu panjang dan meminta satu panjang,
tanpa hasil kali sama sekali.

### Kalau bersinggungan dari luar

Ganti keadaannya: kedua lingkaran bersinggungan dari **luar** di $T$. Pusat homotetinya
tetap $T$, tetapi faktornya menjadi **negatif**:

$$k = -\frac{9}{3} = -3$$

Bayangan $P$ kini di seberang $T$, sehingga $T$ berada di antara $P$ dan $Q$, dan

$$PQ = TP + TQ = 4 + 12 = 16$$

Jadi tanda $k$ bukan rincian: ia yang menentukan apakah kedua panjang dikurangkan atau
dijumlahkan. Membaca "dalam" atau "luar" pada soal adalah langkah pertama, bukan langkah
terakhir.

### Yang ikut terbawa

Karena homoteti menjaga kesejajaran, garis singgung lingkaran kecil di $P$ **sejajar** garis
singgung lingkaran besar di $Q$. Begitu pula jari-jari $O_1P$ sejajar $OQ$.

Kedua akibat itu sering menjadi langkah berikutnya pada soal yang lebih panjang — dan
keduanya diperoleh tanpa perhitungan tambahan sama sekali, cuma dari sifat homotetinya.
