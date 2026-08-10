---
id: gan-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: geometri
tahap: osn-k
jurus: [geometri-analitik]
bentuk: isian
kesulitan: 3
jawaban: "4"
---

## Soal

Titik $P$ bergerak pada bidang sedemikian sehingga jaraknya ke $A(0,0)$ selalu **dua kali**
jaraknya ke $B(6,0)$. Tempat kedudukan $P$ ternyata berupa sebuah lingkaran.

Tentukan jari-jari lingkaran itu.

## Petunjuk

- Tulis $P$ sebagai $(x, y)$ dan terjemahkan syarat soal menjadi satu persamaan.
- Bekerja dengan kuadrat jaraknya jauh lebih enak daripada dengan akarnya: $PA = 2PB$ setara dengan $PA^2 = 4PB^2$.
- Setelah disederhanakan, susun bentuk kuadrat sempurna untuk membaca pusat dan jari-jarinya.

## Pembahasan

**Terjemahkan syaratnya.** Tulis $P = (x,y)$. Syarat $PA = 2PB$ setara dengan

$$PA^2 = 4\,PB^2$$

Mengkuadratkan sah di sini sebab kedua ruas tidak negatif — dan ia menghapus seluruh akar
sebelum perhitungan dimulai.

$$x^2 + y^2 = 4\left[(x-6)^2 + y^2\right]$$

**Jabarkan dan rapikan.**

$$x^2 + y^2 = 4\left(x^2 - 12x + 36 + y^2\right)$$

$$x^2 + y^2 = 4x^2 - 48x + 144 + 4y^2$$

$$0 = 3x^2 + 3y^2 - 48x + 144$$

Bagi dengan $3$:

$$x^2 + y^2 - 16x + 48 = 0$$

**Susun kuadrat sempurna.**

$$\left(x^2 - 16x + 64\right) + y^2 = -48 + 64$$

$$(x - 8)^2 + y^2 = 16$$

Lingkaran berpusat $(8, 0)$ dengan

$$r = \sqrt{16} = \boxed{4}$$

### Periksa pada dua titik yang mudah

Lingkarannya memotong sumbu $x$ di $x = 4$ dan $x = 12$.

- Di $(4,0)$: $PA = 4$ dan $PB = |4-6| = 2$, dan $4 = 2 \times 2$ ✓
- Di $(12,0)$: $PA = 12$ dan $PB = 6$, dan $12 = 2 \times 6$ ✓

Kedua titik itu tidak lain **pembagi dalam dan pembagi luar** ruas $AB$ dengan perbandingan
$2 : 1$ — dan keduanya selalu menjadi ujung diameter lingkaran ini. Itu cara tercepat memeriksa
jawabanmu: cari dua titik pada garis $AB$ yang memenuhi syaratnya, lalu jarak keduanya adalah
diameter.

Di sini: dari $4$ ke $12$ berjarak $8$, sehingga $r = 4$ ✓ tanpa menjabarkan apa pun.

### Nama dan bentuk umumnya

Tempat kedudukan titik yang perbandingan jaraknya ke dua titik tetap bernilai tetap $k \ne 1$
disebut **lingkaran Apollonius**. Kalau $k = 1$, tempat kedudukannya bukan lingkaran melainkan
**sumbu ruas $AB$** — sebuah garis.

Perbedaan itu terbaca dari perhitungannya: dengan $k = 1$, suku $x^2$ dan $y^2$ saling
meniadakan seluruhnya dan yang tersisa persamaan linear. Jadi kasus istimewa itu bukan
pengecualian yang perlu dihafal; ia muncul sendiri dari aljabarnya.

### Jangan lupa memeriksa arah pengkuadratan

Syarat $PA = 2PB$ menjadi $PA^2 = 4PB^2$, bukan $PA^2 = 2PB^2$. Faktor yang lupa dikuadratkan
adalah kekeliruan paling sering di soal tempat kedudukan — dan hasilnya tetap berupa lingkaran
yang tampak masuk akal, hanya salah jari-jari.
