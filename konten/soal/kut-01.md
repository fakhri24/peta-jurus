---
id: kut-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik]
bentuk: isian
kesulitan: 2
jawaban: "8"
---

## Soal

Dua talibusur $AB$ dan $CD$ pada sebuah lingkaran berpotongan di titik $P$ di dalam
lingkaran. Diketahui $PA = 6$, $PB = 4$, dan $PC = 3$.

![Sebuah lingkaran dengan dua talibusur yang berpotongan di titik P di dalamnya, di sebelah kanan pusat. Talibusur pertama menghubungkan A di atas dengan B di kanan bawah: jarak dari P ke A adalah 6 dan dari P ke B adalah 4. Talibusur kedua menghubungkan C di kanan atas dengan D di kiri bawah: jarak dari P ke C adalah 3, sedangkan jarak dari P ke D belum diketahui dan ditandai tanda tanya](talibusur-berpotongan.svg)

Tentukan panjang $PD$.

## Petunjuk

- Yang diberikan hasil kali panjang pada gambar berlingkaran — pasangkan panjang-panjang itu dengan benar.
- Kedua panjang pada satu ruas hasil kali harus berasal dari **satu talibusur** yang sama, keduanya diukur dari $P$.
- $PA \cdot PB = PC \cdot PD$.

## Pembahasan

**Pasangkan menurut talibusurnya.** Yang dikalikan adalah kedua bagian dari **satu**
talibusur: $PA$ dengan $PB$ (dari talibusur $AB$), dan $PC$ dengan $PD$ (dari talibusur
$CD$).

$$PA \cdot PB = PC \cdot PD$$

$$6 \times 4 = 3 \times PD$$

$$PD = \frac{24}{3} = \boxed{8}$$

### Periksa lewat panjang talibusurnya

Talibusur $AB$ panjangnya $6 + 4 = 10$; talibusur $CD$ panjangnya $3 + 8 = 11$. Karena
kuasa $P$ bernilai $-24$, jari-jari lingkarannya memenuhi $r^2 - OP^2 = 24$.

Untuk $AB$: setengah talibusur $5$, dan $P$ berjarak $\left|5-6\right| = 1$ dari titik
tengahnya, jadi $OP^2 = \left(r^2 - 25\right) + 1 = r^2 - 24$ ✓

Untuk $CD$: setengah talibusur $5{,}5$, dan $P$ berjarak $\left|5{,}5-3\right| = 2{,}5$ dari
titik tengahnya, jadi $OP^2 = \left(r^2 - 30{,}25\right) + 6{,}25 = r^2 - 24$ ✓

Kedua talibusur memberi nilai $OP$ yang sama, jadi keduanya benar-benar bisa hidup pada satu
lingkaran yang sama. Kalau $PD$ dijawab keliru, kedua perhitungan itu akan bertabrakan.

### Jebakan: memasangkan dari talibusur yang berbeda

Kekeliruan paling sering adalah menulis $PA \cdot PC = PB \cdot PD$, yang memberi
$PD = 18/4 = 4{,}5$. Bentuk itu memasangkan panjang dari **dua** talibusur yang berbeda, dan
tidak ada teorema yang mengatakannya.

Cara mengingat yang aman: satu talibusur memberi **satu** ruas hasil kali. Tuliskan dulu
kedua talibusurnya sebagai pasangan — $(PA, PB)$ dan $(PC, PD)$ — baru samakan hasil
kalinya.

### Kenapa hasil kalinya sama

Karena $\angle PAC$ dan $\angle PDB$ menghadap busur yang sama, yaitu busur $CB$, keduanya
sama besar. Ditambah $\angle APC = \angle DPB$ (bertolak belakang), maka

$$\triangle APC \sim \triangle DPB$$

sehingga $\dfrac{PA}{PD} = \dfrac{PC}{PB}$, yang tak lain $PA \cdot PB = PC \cdot PD$.

Perhatikan urutan hurufnya pada kesebangunan itu — $A \leftrightarrow D$ dan
$C \leftrightarrow B$, **menyilang**, bukan sejajar. Menyalin urutannya sembarangan adalah
sumber kekeliruan pemasangan yang tadi.

### Arah sebaliknya

Kalau suatu saat kamu punya empat titik dan berhasil menunjukkan $PA \cdot PB = PC \cdot PD$
dengan $P$ titik potong $AB$ dan $CD$, maka keempatnya terletak pada satu lingkaran. Jurus
ini karena itu bukan cuma alat menghitung panjang, melainkan juga alat **membuktikan**
segiempat talibusur — dan itu penggunaan yang jauh lebih sering muncul di soal olimpiade.
