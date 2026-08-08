---
id: tsf-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor]
bentuk: isian
kesulitan: 2
jawaban: "-1"
---

## Soal

Tentukan sisa pembagian $x^3 + 2x^2 - 5x + 1$ oleh $(x - 1)$.

## Petunjuk

- Membagi bersusun bisa, tetapi untuk pembagi berbentuk $(x-a)$ ada jalan satu langkah.
- Tulis $P(x) = (x-a)Q(x) + r$ dengan $r$ konstanta, lalu masukkan $x = a$.
- Di sini $a = 1$, jadi sisanya cukup dihitung sebagai $P(1)$.

## Pembahasan

**Teorema sisa.** Sisa pembagian $P(x)$ oleh $(x-a)$ adalah $P(a)$.

Alasannya satu baris. Menurut algoritma pembagian,

$$P(x) = (x-a)\,Q(x) + r$$

dengan $\deg r < \deg(x-a) = 1$, sehingga $r$ konstanta. Masukkan $x = a$: faktor $(x-a)$
lenyap, menyisakan

$$P(a) = 0 \cdot Q(a) + r = r$$

Di sini $a = 1$:

$$P(1) = 1^3 + 2(1)^2 - 5(1) + 1 = 1 + 2 - 5 + 1 = \boxed{-1}$$

Periksa dengan pembagian bersusun:

$$x^3+2x^2-5x+1 = (x-1)\left(x^2 + 3x - 2\right) - 1$$

Cocok — tetapi jalur teorema sisa hanya menuntut satu substitusi, tanpa mencari $Q$ sama
sekali.

**Teorema faktor** adalah kasus khususnya: $(x-a)$ merupakan faktor $P$ tepat ketika
sisanya nol, yaitu ketika $P(a) = 0$. Di sini $P(1) = -1 \ne 0$, jadi $(x-1)$ **bukan**
faktor.

Keduanya mengubah pertanyaan tentang **pembagian** menjadi pertanyaan tentang **nilai** —
dan menghitung nilai jauh lebih murah daripada membagi. Itulah seluruh isi jurus ini.
