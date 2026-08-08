---
id: dtl-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 3
jawaban: "2"
---

## Soal

Ada berapa pasangan bilangan asli $(x, y)$ dengan $x \le y$ yang memenuhi

$$xy = 3(x + y)\ ?$$

## Petunjuk

- Pindahkan semuanya ke satu ruas dulu, lalu lihat apakah bentuknya bisa difaktorkan dengan tambahan konstanta.
- Dari $xy - 3x - 3y = 0$, tambahkan $9$ ke kedua ruas.
- Setelah menjadi $(x-3)(y-3) = 9$, buktikan kedua faktornya harus positif sebelum mencacah.

## Pembahasan

Pindahkan dan faktorkan:

$$xy - 3x - 3y = 0 \quad\Longrightarrow\quad xy - 3x - 3y + 9 = 9
\quad\Longrightarrow\quad (x-3)(y-3) = 9$$

**Kedua faktornya positif.** Hasil kalinya $9 > 0$, jadi $x-3$ dan $y-3$ bertanda sama.
Andaikan keduanya negatif: maka $x \le 2$ dan $y \le 2$, sehingga $xy \le 4$ sementara
$3(x+y) \ge 6$ — mustahil. Jadi keduanya positif.

Kasus salah satu nol juga gugur, karena hasil kalinya akan $0$, bukan $9$.

**Cacah pasangan pembagi.** Pasangan $(d, e)$ dengan $de = 9$ dan $d \le e$:

$$(1, 9), \qquad (3, 3)$$

Masing-masing memberi

$$(x, y) = (4, 12), \qquad (6, 6)$$

Ada $\boxed{2}$ pasangan.

Periksa: $4 \times 12 = 48$ dan $3(4 + 12) = 48$. Benar. Juga $6 \times 6 = 36$ dan
$3(6+6) = 36$.

Langkah membuktikan kedua faktor positif sering dilewati, padahal ia yang mencegah
pasangan seperti $(-1, -9)$ ikut terhitung. Pada soal ini pasangan negatif memberi
$x = 2$, $y = -6$ — bukan bilangan asli, tetapi baru ketahuan setelah diperiksa.
