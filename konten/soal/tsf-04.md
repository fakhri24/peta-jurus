---
id: tsf-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor, sistem-persamaan]
bentuk: isian
kesulitan: 3
jawaban: "7"
---

## Soal

Polinomial $P(x)$ dibagi $(x-1)$ bersisa $3$, dan dibagi $(x-2)$ bersisa $5$. Misalkan
$S(x)$ adalah sisa pembagian $P(x)$ oleh $(x-1)(x-2)$. Tentukan nilai $S(3)$.

## Petunjuk

- Sisa pembagian oleh polinomial berderajat dua berbentuk apa? Derajatnya harus kurang dari dua.
- Tulis $P(x) = (x-1)(x-2)Q(x) + px + q$, lalu masukkan $x = 1$ dan $x = 2$.
- Kedua substitusi menghapus $Q$ seluruhnya, menyisakan sistem dua persamaan.

## Pembahasan

**Bentuk sisanya.** Karena pembaginya berderajat $2$, sisanya berderajat kurang dari $2$ —
yaitu berbentuk linear:

$$P(x) = (x-1)(x-2)\,Q(x) + px + q$$

Dua bilangan tak diketahui, $p$ dan $q$, jadi dibutuhkan dua persamaan.

**Substitusikan $x = 1$.** Faktor $(x-1)$ lenyap, sehingga seluruh suku $Q$ hilang:

$$P(1) = p + q$$

Dan menurut teorema sisa, $P(1)$ adalah sisa pembagian oleh $(x-1)$, yaitu $3$:

$$p + q = 3$$

**Substitusikan $x = 2$.** Dengan cara yang sama:

$$P(2) = 2p + q = 5$$

**Selesaikan sistemnya.** Kurangkan persamaan pertama dari yang kedua:

$$p = 2 \quad\Longrightarrow\quad q = 3 - 2 = 1$$

Jadi sisanya

$$S(x) = 2x + 1$$

dan

$$S(3) = 2(3) + 1 = \boxed{7}$$

Periksa: $S(1) = 3$ dan $S(2) = 5$ — cocok dengan kedua keterangan soal.

**Perhatikan bahwa $Q$ tidak pernah dicari, dan memang tidak bisa.** Soal tidak memberi
cukup keterangan untuk menentukan $P$ seluruhnya — ada tak hingga banyak polinomial yang
memenuhi kedua syarat itu. Yang tertentu hanyalah sisanya, dan itu yang ditanya.

Pola ini berlaku umum. Untuk pembagi berderajat $3$, sisanya berbentuk $ax^2+bx+c$ dengan
**tiga** bilangan tak diketahui — jadi dibutuhkan tiga keterangan. Menyiapkan bentuk sisa
yang benar adalah langkah pertama, dan salah menebak derajatnya membuat sistemnya tidak
bisa diselesaikan.
