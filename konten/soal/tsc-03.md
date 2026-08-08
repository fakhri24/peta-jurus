---
id: tsc-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina]
bentuk: isian
kesulitan: 2
jawaban: "14"
---

## Soal

Ada berapa bilangan asli $n \le 1000$ yang bersisa $3$ jika dibagi $8$ dan bersisa $5$
jika dibagi $9$?

## Petunjuk

- Selesaikan sistemnya lebih dulu; pencacahan baru masuk akal setelah bentuk solusinya diketahui.
- Karena $\gcd(8,9) = 1$, solusinya satu kelas modulo $72$ — jadi bilangan yang dicari berjarak $72$.
- Setelah solusi terkecil ditemukan, cacah berapa suku barisan itu yang tidak melebihi $1000$.

## Pembahasan

**Selesaikan sistemnya.** Dari $n \equiv 5 \pmod 9$, tulis

$$n = 9t + 5$$

Masukkan ke $n \equiv 3 \pmod 8$:

$$9t + 5 \equiv 3 \pmod 8 \quad\Longrightarrow\quad t \equiv -2 \equiv 6 \pmod 8$$

sebab $9 \equiv 1 \pmod 8$. Tulis $t = 8s + 6$:

$$n = 9(8s + 6) + 5 = 72s + 59$$

Jadi solusinya persis bilangan yang bersisa $59$ dibagi $72$ — satu kelas modulo
$8 \times 9 = 72$, sesuai Teorema Sisa Cina.

**Cacah yang tidak melebihi $1000$.** Bilangannya

$$59,\ 131,\ 203,\ \ldots$$

Dituntut $72s + 59 \le 1000$, yaitu

$$72s \le 941 \quad\Longrightarrow\quad s \le \frac{941}{72} = 13{,}07\ldots$$

Karena $s \ge 0$ bulat, nilai yang mungkin $s = 0, 1, \ldots, 13$ — sebanyak
$\boxed{14}$ bilangan.

Periksa ujungnya: $s = 13$ memberi $n = 72 \times 13 + 59 = 936 + 59 = 995 \le 1000$,
sedangkan $s = 14$ memberi $1067$ yang sudah melewati batas. Dan $995 = 8 \times 124 + 3$,
$995 = 9 \times 110 + 5$. Benar.

Pola ini berulang di banyak soal pencacahan: menyelesaikan sistem lebih dulu mengubah dua
syarat sisa menjadi satu barisan aritmetika, dan mencacah barisan aritmetika itu perkara
sepele.
