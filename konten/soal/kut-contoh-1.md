---
id: kut-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [kuasa-titik]
bentuk: isian
kesulitan: 3
jawaban: "16"
---

## Soal

Sebuah lingkaran berjari-jari $13$ dan titik $P$ berjarak $5$ dari pusatnya. Sebuah
talibusur melalui $P$ terbagi oleh $P$ menjadi dua bagian, dan salah satunya panjangnya $9$.

Tentukan panjang bagian yang lain.

## Petunjuk

- Soal tidak memberitahu arah talibusurnya, jadi jawabannya tidak boleh bergantung pada arah itu. Besaran apa yang sama untuk **semua** talibusur lewat $P$?
- Hasil kali kedua bagiannya tetap, dan nilainya ditentukan oleh jari-jari serta jarak $P$ ke pusat.
- Untuk titik di dalam lingkaran, hasil kali itu $r^2 - OP^2$.

## Pembahasan

**Kenali besaran yang tidak berubah.** Kuasa titik $P$ terhadap lingkaran berpusat $O$
berjari-jari $r$ adalah

$$k(P) = OP^2 - r^2 = 5^2 - 13^2 = 25 - 169 = -144$$

Tandanya negatif, dan itu memang menandakan $P$ berada **di dalam** lingkaran. Untuk
talibusur $AB$ yang melalui $P$, hasil kali kedua bagiannya sama dengan nilai mutlaknya:

$$PA \cdot PB = r^2 - OP^2 = 144$$

**Selesaikan.**

$$9 \cdot PB = 144 \quad \Longrightarrow \quad PB = \boxed{16}$$

### Periksa lewat Pythagoras, tanpa memakai kuasa titik sama sekali

Talibusurnya panjang $9 + 16 = 25$, jadi jarak dari pusat ke talibusur itu memenuhi

$$d^2 = r^2 - \left(\tfrac{25}{2}\right)^2 = 169 - 156{,}25 = 12{,}75$$

Titik tengah talibusur, sebut $M$, berjarak $\left|12{,}5 - 9\right| = 3{,}5$ dari $P$. Karena
$OM \perp AB$, segitiga $OMP$ siku-siku di $M$:

$$OP^2 = OM^2 + MP^2 = 12{,}75 + 12{,}25 = 25 \quad \Longrightarrow \quad OP = 5 \quad ✓$$

Cocok dengan yang diketahui. Pemeriksaan ini menempuh jalan yang sepenuhnya berbeda — cuma
Pythagoras dua kali — jadi ia benar-benar menguji.

### Dari mana rumusnya

Ambil talibusur istimewa lewat $P$: yang melalui pusat, yaitu garis tengahnya. Ia terbagi
menjadi

$$r - OP = 13 - 5 = 8 \qquad \text{dan} \qquad r + OP = 13 + 5 = 18$$

Hasil kalinya $8 \times 18 = 144$. Karena teorema talibusur berpotongan menjamin hasil kali
itu **sama untuk semua** talibusur lewat $P$, angka $144$ berlaku untuk talibusur mana pun —
termasuk yang di soal:

$$PA \cdot PB = (r - OP)(r + OP) = r^2 - OP^2$$

Jadi rumus kuasa titik bukan hafalan tambahan; ia teorema talibusur berpotongan yang
diterapkan pada satu talibusur yang paling mudah dihitung.

### Kalau $P$ di luar lingkaran

Bentuknya sama, tandanya berbeda. Untuk $OP > r$ kuasanya positif, dan

$$PA \cdot PB = OP^2 - r^2 = PT^2$$

dengan $PT$ panjang garis singgung dari $P$. Jadi satu rumus $\left|OP^2 - r^2\right|$
menaungi ketiga bentuk yang biasanya diajarkan terpisah: dua talibusur berpotongan, dua
garis potong dari titik luar, dan garis singgung bersama garis potong.

Yang membedakan hanya letak $P$, dan itu terbaca dari tanda kuasanya.

### Talibusur terpendek lewat $P$

Karena hasil kalinya tetap $144$, kedua bagiannya paling seimbang ketika keduanya
$\sqrt{144} = 12$ — dan menurut AM-GM itulah saat jumlahnya paling kecil. Jadi talibusur
terpendek lewat $P$ panjangnya $24$, dan ia tegak lurus $OP$.

Talibusur terpanjangnya jelas garis tengah, $26$. Semua talibusur lewat $P$ karena itu
panjangnya di antara $24$ dan $26$ — termasuk yang di soal, $25$ ✓.
