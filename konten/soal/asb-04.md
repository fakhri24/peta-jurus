---
id: asb-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak, manipulasi-aljabar]
bentuk: isian
kesulitan: 3
jawaban: "21"
---

## Soal

Akar-akar persamaan $x^3 - 3x^2 + 2 = 0$ adalah $a$, $b$, $c$. Tentukan nilai

$$a^3 + b^3 + c^3$$

## Petunjuk

- Perhatikan bahwa koefisien $x$ bernilai nol. Itu bukan kelalaian penulisan soal — ia menyederhanakan salah satu besaran yang akan kamu pakai.
- Ada jalan yang tidak menuntut identitas apa pun: tiap akar memenuhi persamaannya sendiri.
- Dari $a^3 = 3a^2 - 2$, jumlahkan ketiganya dan yang tersisa memuat $a^2+b^2+c^2$.

## Pembahasan

**Ambil besaran Vieta.** Perhatikan koefisien $x$ bernilai $0$:

$$a+b+c = 3, \qquad ab+ac+bc = \frac{0}{1} = 0, \qquad abc = -\frac{2}{1} = -2$$

**Pakai persamaannya sendiri.** Karena $a$ akar, ia memenuhi

$$a^3 - 3a^2 + 2 = 0 \quad\Longrightarrow\quad a^3 = 3a^2 - 2$$

Hal yang sama berlaku untuk $b$ dan $c$. Jumlahkan ketiganya:

$$a^3+b^3+c^3 = 3\left(a^2+b^2+c^2\right) - 6$$

**Hitung jumlah kuadratnya.**

$$a^2+b^2+c^2 = (a+b+c)^2 - 2(ab+ac+bc) = 3^2 - 2(0) = 9$$

Substitusikan:

$$a^3+b^3+c^3 = 3(9) - 6 = 27 - 6 = \boxed{21}$$

**Cara kedua, lewat identitas.**

$$a^3+b^3+c^3 - 3abc = (a+b+c)\left(a^2+b^2+c^2 - ab-ac-bc\right)$$

Substitusikan: ruas kanan $= 3(9 - 0) = 27$, sehingga

$$a^3+b^3+c^3 = 27 + 3abc = 27 + 3(-2) = 21$$

Hasil yang sama.

**Cara pertama lebih layak dikuasai.** Ia tidak menuntut mengingat identitas apa pun, dan
bekerja untuk pangkat berapa pun: untuk $a^4+b^4+c^4$, kalikan $a^3 = 3a^2-2$ dengan $a$
sekali lagi lalu ulangi penurunannya. Identitas hanya membantu sampai pangkat tiga.

Perhatikan pula bahwa koefisien $x$ yang nol membuat $ab+ac+bc = 0$ — dan itu memangkas
banyak perhitungan. Melihat koefisien yang hilang sebagai **keterangan**, bukan sebagai
kelalaian penulisan soal, adalah kebiasaan yang berguna.
