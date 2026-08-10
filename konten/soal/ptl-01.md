---
id: ptl-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy]
bentuk: isian
kesulitan: 3
jawaban: "27"
---

## Soal

Pada segiempat talibusur $ABCD$ diketahui $AB = 13$, $BC = 15$, $CD = 21$, $DA = 25$, dan
panjang diagonal $AC = 24$.

Tentukan panjang diagonal $BD$.

## Petunjuk

- Keempat titiknya pada satu lingkaran dan yang ditanya diagonal — itu pemicu langsung untuk Ptolemy.
- Pasangan sisi berhadapan pada $ABCD$ adalah $AB$ dengan $CD$, dan $BC$ dengan $AD$.
- $AC \cdot BD = AB \cdot CD + BC \cdot AD$.

## Pembahasan

**Tulis Ptolemy dengan pasangan yang benar.** Sisi berhadapan pada $ABCD$ adalah $AB$ dengan
$CD$, dan $BC$ dengan $AD$ — bukan $AB$ dengan $BC$:

$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

**Masukkan angkanya.**

$$24 \cdot BD = 13 \times 21 + 15 \times 25 = 273 + 375 = 648$$

$$BD = \frac{648}{24} = \boxed{27}$$

### Periksa bahwa segiempatnya memang ada

Angka yang rapi tidak menjamin gambarnya ada. Untuk segiempat talibusur bersisi $a$, $b$,
$c$, $d$ berturut-turut, kedua diagonalnya memenuhi

$$AC^2 = \frac{(ac+bd)(ad+bc)}{ab+cd}, \qquad BD^2 = \frac{(ac+bd)(ab+cd)}{ad+bc}$$

Dengan $a = 13$, $b = 15$, $c = 21$, $d = 25$:

$$ac+bd = 273 + 375 = 648, \qquad ad+bc = 325 + 315 = 640, \qquad ab+cd = 195 + 525 = 720$$

$$AC^2 = \frac{648 \times 640}{720} = 576 \quad \Longrightarrow \quad AC = 24 \quad ✓$$

$$BD^2 = \frac{648 \times 720}{640} = 729 \quad \Longrightarrow \quad BD = 27 \quad ✓$$

Kedua diagonalnya bulat sekaligus — segiempat semacam ini disebut **segiempat Brahmagupta**,
dan angkanya memang disusun dari sana supaya jawabannya tidak berkoma.

### Jebakan: menukar pasangan sisi berhadapan

Kalau ditulis $AC \cdot BD = AB \cdot BC + CD \cdot AD$, hasilnya

$$13 \times 15 + 21 \times 25 = 195 + 525 = 720 \quad \Longrightarrow \quad BD = 30$$

Bilangan bulat yang meyakinkan dan salah. Cara memastikannya: pada segiempat $ABCD$, dua
sisi disebut berhadapan kalau **tidak berbagi titik sudut**. Sisi $AB$ dan $BC$ berbagi $B$,
jadi keduanya bertetangga, bukan berhadapan.

Pemeriksaan cepat: pada ruas kanan Ptolemy, keempat huruf $A$, $B$, $C$, $D$ harus muncul
tepat sekali di tiap suku hasil kali — $AB \cdot CD$ ✓ dan $BC \cdot AD$ ✓. Bentuk
$AB \cdot BC$ memuat $B$ dua kali dan tidak memuat $D$, jadi pasti salah.

### Luasnya, kalau ditanya

Untuk segiempat talibusur, rumus Brahmagupta memberi luas hanya dari keempat sisinya:

$$L = \sqrt{(s-a)(s-b)(s-c)(s-d)}, \qquad s = \frac{a+b+c+d}{2} = \frac{74}{2} = 37$$

$$L = \sqrt{24 \times 22 \times 16 \times 12} = \sqrt{101376} \approx 318{,}4$$

Ia perluasan langsung rumus Heron: kalau salah satu sisinya menyusut jadi nol, segiempatnya
menjadi segitiga dan rumusnya kembali menjadi Heron.

### Kenapa Ptolemy tidak cukup sendirian

Perhatikan bahwa Ptolemy hanya memberi **hasil kali** kedua diagonal, bukan masing-masing.
Soal ini bisa dijawab karena satu diagonalnya sudah diketahui.

Kalau keduanya belum diketahui, yang diperlukan satu persamaan lagi — biasanya **Ptolemy
kedua**, yang memberi perbandingan $\dfrac{AC}{BD}$ dari keempat sisinya saja. Hasil kali
dan perbandingan bersama-sama menentukan keduanya.
