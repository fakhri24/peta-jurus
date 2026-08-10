---
id: kut-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik]
bentuk: isian
kesulitan: 3
jawaban: "9"
---

## Soal

Dari titik $P$ di luar sebuah lingkaran ditarik dua garis potong. Garis pertama menembus
lingkaran di $A$ lalu $B$, dengan $PA = 4$ dan $AB = 5$. Garis kedua menembusnya di $C$ lalu
$D$, dengan $PC = 3$.

Tentukan panjang $CD$.

## Petunjuk

- Hubungan hasil kalinya memakai jarak dari $P$ ke **kedua** titik potong, bukan panjang talibusur di dalam lingkaran.
- Yang diberikan $AB$, bukan $PB$. Ubah dulu: $PB = PA + AB$.
- Setelah $PD$ ketemu, ingat bahwa yang ditanya $CD = PD - PC$.

## Pembahasan

**Ubah keterangan menjadi jarak dari $P$.** Ini seluruh jebakan soal ini. Titik $A$ terletak
di antara $P$ dan $B$, jadi

$$PB = PA + AB = 4 + 5 = 9$$

**Pakai kuasa titik.**

$$PA \cdot PB = PC \cdot PD$$

$$4 \times 9 = 3 \times PD \quad \Longrightarrow \quad PD = 12$$

**Kembalikan ke yang ditanya.**

$$CD = PD - PC = 12 - 3 = \boxed{9}$$

### Dua kekeliruan yang mengintai

**Pertama:** menulis $PA \cdot AB = PC \cdot CD$, yaitu $4 \times 5 = 3 \times CD$ sehingga
$CD = 20/3$. Bentuk itu memakai panjang talibusur di dalam lingkaran, padahal kuasa titik
memakai jarak dari $P$ ke kedua titik potong. Untuk titik di **luar** lingkaran, ruas $PA$
seluruhnya berada di luar dan tetap ikut dihitung.

**Kedua:** berhenti di $PD = 12$ dan menuliskannya sebagai jawaban. Soal menanyakan $CD$,
bukan $PD$. Kebiasaan yang menyelamatkan: setelah selesai menghitung, baca ulang kalimat
terakhir soalnya.

### Periksa dengan kuasa titiknya

Kuasa $P$ bernilai

$$k(P) = PA \cdot PB = 4 \times 9 = 36$$

Periksa lewat garis potong kedua: $PC \cdot PD = 3 \times 12 = 36$ ✓

Nilai itu sekaligus berarti garis singgung dari $P$ panjangnya $\sqrt{36} = 6$, dan
$OP^2 - r^2 = 36$. Kalau soal berikutnya menanyakan garis singgungnya, jawabannya sudah ada
tanpa perhitungan baru — itu memang kegunaan menghitung kuasanya sebagai satu angka, bukan
sekadar menyamakan dua ruas.

### Batas yang harus dipenuhi

Karena $P$ di luar lingkaran, untuk tiap garis potong berlaku $PC < PD$ — titik yang lebih
dekat selalu ditembus lebih dulu. Di sini $3 < 12$ ✓.

Kalau perhitunganmu memberi $PD < PC$, ada yang terbalik: entah penamaan titiknya, entah
letak $P$ yang sebenarnya di dalam lingkaran. Pemeriksaan urutan itu sederhana dan menangkap
banyak kekeliruan sekaligus.

### Kenapa hubungannya sama persis dengan yang di dalam

Untuk $P$ di dalam lingkaran, hubungannya $PA \cdot PB = PC \cdot PD$. Untuk $P$ di luar,
bunyinya sama persis. Yang berubah cuma tandanya kalau panjangnya diukur **bertanda**: di
dalam, $\overrightarrow{PA}$ dan $\overrightarrow{PB}$ berlawanan arah sehingga hasil
kalinya negatif; di luar keduanya searah sehingga positif.

Itulah sebabnya kuasa titik $OP^2 - r^2$ ditulis dengan tanda: satu rumus yang menaungi
kedua letak, dan tandanya yang memberitahu $P$ ada di dalam atau di luar.
