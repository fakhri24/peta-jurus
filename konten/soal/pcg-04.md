---
id: pcg-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: isian
kesulitan: 3
jawaban: "12"
---

## Soal

Di sebuah perkemahan terdapat $9$ siswa yang dibagi ke dalam beberapa kelompok kerja.
Setiap siswa masuk ke **tepat $4$** kelompok, dan setiap kelompok beranggotakan **tepat
$3$** siswa.

Ada berapa kelompok kerja?

## Petunjuk

- Cacah pasangan (siswa, kelompok yang ia masuki), lalu hitung dari kedua sisi.
- Dari sisi siswa, tiap siswa menyumbang empat pasangan.
- Dari sisi kelompok, tiap kelompok menyumbang tiga pasangan.

## Pembahasan

**Nyatakan apa yang dicacah.**

$$T = \{(s, g) : \text{siswa } s \text{ masuk kelompok } g\}$$

**Dari sisi siswa.**

$$|T| = 9 \times 4 = 36$$

**Dari sisi kelompok.** Sebut $G$ banyaknya kelompok:

$$|T| = 3G$$

**Samakan.**

$$3G = 36 \quad\Longrightarrow\quad G = \boxed{12}$$

**Perhatikan yang tidak dijawab hitungan ini.** Persamaan di atas menunjukkan bahwa
**kalau** susunan semacam itu ada, banyaknya kelompok pasti $12$. Ia tidak membuktikan
susunan itu benar-benar bisa dibuat.

Syarat bilangan bulat adalah **syarat perlu**, bukan syarat cukup. Untuk soal olimpiade
yang menanyakan "mungkinkah", biasanya dibutuhkan dua bagian: hitungan seperti ini untuk
menutup kemungkinan yang salah, dan sebuah susunan nyata untuk menunjukkan sisanya bisa.

**Contoh kegagalan syarat itu.** Kalau soalnya menyebut $9$ siswa yang masing-masing masuk
$4$ kelompok, tetapi tiap kelompok beranggotakan $5$ siswa, maka

$$5G = 36 \quad\Longrightarrow\quad G = 7{,}2$$

bukan bilangan bulat — sehingga susunan seperti itu **mustahil**, tanpa perlu mencoba apa
pun.

**Satu pemeriksaan lagi yang murah.** Tiap kelompok berisi $3$ dari $9$ siswa, dan
seluruhnya ada $\binom93 = 84$ kelompok berbeda yang mungkin. Karena $12 \le 84$, tidak ada
yang bertentangan di situ. Kalau hitungannya menuntut lebih banyak kelompok daripada yang
mungkin ada, susunannya juga mustahil — kecuali kelompok yang isinya sama boleh muncul dua
kali.
