---
id: kut-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik]
bentuk: isian
kesulitan: 4
jawaban: "12"
---

## Soal

Titik $P$ terletak di dalam sebuah lingkaran. Sebuah talibusur melalui $P$ terbagi olehnya
menjadi dua bagian sepanjang $4$ dan $9$. Talibusur kedua melalui $P$ terbagi menjadi dua
bagian yang **sama panjang**.

Tentukan panjang talibusur kedua.

## Petunjuk

- Talibusur pertama menetapkan satu bilangan yang berlaku untuk semua talibusur lewat $P$. Bilangan apa?
- Kalau kedua bagian talibusur kedua sama panjang, sebutlah masing-masing $x$. Persamaan apa yang harus dipenuhi $x$?
- $x \cdot x = 4 \cdot 9$.

## Pembahasan

**Hitung kuasa $P$ dari talibusur pertama.**

$$PA \cdot PB = 4 \times 9 = 36$$

Angka $36$ ini berlaku untuk **setiap** talibusur yang lewat $P$ — itulah arti "kuasa titik".

**Terapkan pada talibusur kedua.** Kedua bagiannya sama panjang, sebut masing-masing $x$:

$$x \cdot x = 36 \quad \Longrightarrow \quad x = 6$$

$$\text{panjang talibusur kedua} = 2x = \boxed{12}$$

### Talibusur kedua itu yang terpendek

Perhatikan apa yang baru saja terjadi. Untuk semua talibusur lewat $P$, hasil kali kedua
bagiannya tetap $36$. Menurut AM-GM,

$$\frac{u+v}{2} \ \ge\ \sqrt{uv} = 6 \quad \Longrightarrow \quad u + v \ge 12$$

dengan kesamaan tepat saat $u = v$. Jadi talibusur yang terbagi sama panjang oleh $P$ adalah
talibusur **terpendek** yang melalui $P$ — dan panjangnya $12$.

Talibusur pertama panjangnya $4 + 9 = 13 > 12$ ✓, konsisten.

### Bagaimana rupanya

Talibusur yang titik tengahnya tepat di $P$ pastilah tegak lurus $OP$: jarak dari pusat ke
sebuah talibusur diukur ke titik tengahnya, dan kalau titik tengah itu $P$, maka
$OP \perp$ talibusur.

Jadi talibusur terpendek lewat $P$ selalu yang tegak lurus $OP$ — hasil yang muncul berulang
di soal olimpiade, dan yang barusan diturunkan tanpa kalkulus sama sekali.

### Sekalian: jari-jari dan letak $P$

Soal tidak menyebutnya, dan memang tidak perlu — tetapi kalau ditanya, keduanya terkunci
oleh satu persamaan saja:

$$r^2 - OP^2 = 36$$

Jadi ada tak hingga banyak lingkaran yang cocok: $r = 10$ dengan $OP = 8$, $r = 6{,}5$
dengan $OP = 2{,}5$, dan seterusnya. Yang tidak berubah pada semuanya adalah kedua
talibusurnya, dan itulah sebabnya soal ini punya jawaban tunggal meski lingkarannya tidak
tertentu.

Coba sendiri dengan $r = 10$, $OP = 8$: setengah talibusur terpendek adalah
$\sqrt{100 - 64} = 6$ ✓, jadi panjangnya $12$ ✓.

### Kenapa keterangan "sama panjang" cukup

Godaan pertamanya adalah mencari jari-jari lingkarannya lebih dulu, dan di situ soalnya
terasa kurang keterangan. Memang kurang — tetapi yang ditanyakan tidak memerlukannya.

Kebiasaan yang berguna pada soal kuasa titik: **hitung kuasanya sebagai satu angka lebih
dulu**, sebelum memikirkan lingkarannya. Kuasa adalah satu-satunya hal yang dibagi bersama
oleh semua garis lewat $P$, dan sering ia satu-satunya yang benar-benar dibutuhkan.
