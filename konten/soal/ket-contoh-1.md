---
id: ket-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [keterbagian]
bentuk: isian
kesulitan: 2
jawaban: "19"
---

## Soal

Tentukan jumlah semua bilangan bulat positif $n$ sehingga $n + 3$ membagi $n^2 + 7$.

## Petunjuk

- Kamu tidak bisa berbuat apa-apa selama bentuknya masih $n^2 + 7$. Ubah dulu jadi kelipatan $n+3$ ditambah sisa.
- Bagi $n^2 + 7$ dengan $n + 3$ seperti membagi polinomial biasa. Berapa sisanya?
- $n^2 + 7 = (n+3)(n-3) + 16$. Karena $n+3$ jelas membagi suku pertama, syaratnya tinggal $n + 3 \mid 16$.

## Pembahasan

Tulis ulang dengan membagi bersusun:

$$n^2 + 7 = (n+3)(n-3) + 16$$

Suku $(n+3)(n-3)$ pasti habis dibagi $n+3$. Jadi menurut sifat pertama keterbagian,

$$(n+3) \mid (n^2+7) \iff (n+3) \mid 16$$

Karena $n$ bulat positif, $n + 3 \ge 4$. Pembagi $16$ yang bernilai minimal $4$ adalah
$4, 8, 16$, sehingga $n \in \{1, 5, 13\}$.

Ketiganya perlu dicek balik: $n=1 \to 4 \mid 8$; $n=5 \to 8 \mid 32$; $n=13 \to 16 \mid 176$. Semua benar.

Jumlahnya $1 + 5 + 13 = \boxed{19}$.
