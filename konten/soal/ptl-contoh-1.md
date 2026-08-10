---
id: ptl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: geometri
tahap: osn-p
jurus: [ptolemy]
bentuk: isian
kesulitan: 3
jawaban: "7"
---

## Soal

Segitiga sama sisi $ABC$ terletak pada sebuah lingkaran. Titik $P$ berada pada busur $BC$
yang tidak memuat $A$. Diketahui $PB = 2$ dan $PC = 5$.

![Segitiga sama sisi ABC dengan ketiga titik sudutnya pada sebuah lingkaran: A di puncak atas, B di kiri bawah, C di kanan bawah. Titik P berada pada busur BC yang tidak memuat A, lebih dekat ke B daripada ke C. Dari P ditarik ruas ke ketiga titik sudut. Ruas PB panjangnya 2, ruas PC panjangnya 5, dan ruas PA — yang memotong sisi BC — panjangnya belum diketahui dan ditandai tanda tanya](sama-sisi-titik-busur.svg)

Tentukan panjang $PA$.

## Petunjuk

- Keempat titik $A$, $B$, $P$, $C$ terletak pada satu lingkaran. Segiempat apa yang mereka bentuk, dan bagaimana urutannya mengelilingi lingkaran?
- Urutannya $A$, $B$, $P$, $C$. Diagonalnya $AP$ dan $BC$ — dan $AP$ itulah yang ditanyakan.
- Terapkan teorema Ptolemy pada segiempat $ABPC$, lalu manfaatkan bahwa ketiga sisi segitiganya sama panjang.

## Pembahasan

**Kenali segiempat talibusurnya.** Keempat titik $A$, $B$, $P$, $C$ ada pada satu lingkaran.
Urutannya mengelilingi lingkaran adalah $A \to B \to P \to C$, jadi segiempatnya $ABPC$
dengan:

- sisi: $AB$, $BP$, $PC$, $CA$;
- diagonal: $AP$ dan $BC$.

Membaca urutan ini benar adalah seluruh pekerjaan awalnya. Kalau urutannya diacak, yang
disebut "diagonal" bukan diagonal lagi dan kesamaannya gagal.

**Terapkan Ptolemy.** Hasil kali diagonal sama dengan jumlah hasil kali kedua pasang sisi
berhadapan:

$$AP \cdot BC = AB \cdot PC + BP \cdot CA$$

**Manfaatkan bahwa segitiganya sama sisi.** Sebut sisinya $s$, sehingga $AB = BC = CA = s$:

$$AP \cdot s = s \cdot PC + BP \cdot s$$

Bagi kedua ruas dengan $s$, yang boleh karena $s > 0$:

$$AP = PC + BP = 5 + 2 = \boxed{7}$$

### Kenapa hasilnya tidak bergantung pada besar lingkarannya

Perhatikan bahwa $s$ lenyap seluruhnya. Jadi untuk **setiap** segitiga sama sisi dan setiap
titik $P$ pada busur $BC$ berlaku

$$PA = PB + PC$$

Hasil ini terlihat ajaib kalau dikerjakan dengan cara lain, dan itu sebabnya ia salah satu
pemicu paling khas jurus ini: **gambar memuat segitiga sama sisi beserta satu titik di
lingkaran luarnya.**

### Periksa lewat aturan kosinus

Karena $ABPC$ segiempat talibusur, $\angle BPC$ berpelurus dengan $\angle BAC = 60^\circ$,
sehingga $\angle BPC = 120^\circ$. Pada $\triangle BPC$:

$$BC^2 = 2^2 + 5^2 - 2 \cdot 2 \cdot 5 \cos 120^\circ = 4 + 25 + 10 = 39$$

Jadi $s = \sqrt{39} \approx 6{,}245$, dan jari-jari lingkarannya
$R = \dfrac{s}{\sqrt3} = \sqrt{13} \approx 3{,}606$.

Sekarang hitung $PA$ dengan cara lain. Sudut $\angle BPA$ menghadap busur $AB$, sama seperti
sudut keliling $\angle BCA = 60^\circ$, jadi $\angle BPA = 60^\circ$. Pada $\triangle ABP$:

$$AB^2 = PA^2 + PB^2 - 2 \cdot PA \cdot PB \cos 60^\circ$$

$$39 = PA^2 + 4 - 2 PA \quad \Longrightarrow \quad PA^2 - 2PA - 35 = 0
\quad \Longrightarrow \quad (PA-7)(PA+5) = 0$$

Karena panjang positif, $PA = 7$ ✓

Jalan ini jauh lebih panjang, dan itu memang inti perbandingannya: Ptolemy memotong seluruh
perhitungan trigonometri menjadi satu baris.

### Kalau $P$ berada di busur yang lain

Keterangan "busur $BC$ yang tidak memuat $A$" bukan hiasan. Kalau $P$ ada di busur $AB$
misalnya, urutan keliling lingkarannya menjadi $A$, $P$, $B$, $C$, dan segiempatnya $APBC$
dengan diagonal $AB$ dan $PC$. Ptolemy lalu memberi

$$PC = PA + PB$$

yaitu peran ketiganya berputar. Yang selalu berlaku: **jarak ke titik sudut yang paling
jauh sama dengan jumlah jarak ke dua titik sudut lainnya**, dan titik sudut terjauh itu
selalu yang berseberangan dengan busur tempat $P$ berada.

### Bentuk ketaksamaannya

Untuk $P$ di mana pun di bidang — tidak harus pada lingkaran — berlaku ketaksamaan Ptolemy:

$$PA \cdot BC \le AB \cdot PC + BP \cdot CA \quad \Longrightarrow \quad PA \le PB + PC$$

dengan kesamaan tepat ketika $ABPC$ segiempat talibusur dengan urutan itu. Jadi soal ini
sebenarnya kasus **kesamaan** dari sebuah ketaksamaan — dan bentuk ketaksamaannya yang lebih
sering muncul di soal olimpiade.
