---
id: sb-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [suku-banyak]
bentuk: isian
kesulitan: 2
jawaban: "9"
---

## Soal

Diketahui $P(x) = x^3 - 2x^2 + 5x - 1$. Tentukan nilai $P(2)$.

## Petunjuk

- Substitusikan $x = 2$ ke setiap suku, lalu jumlahkan.
- Hitung tiap pangkat lebih dulu: $2^3 = 8$ dan $2^2 = 4$.
- Perhatikan tanda pada suku $-2x^2$.

## Pembahasan

Substitusikan $x = 2$:

$$P(2) = 2^3 - 2\left(2^2\right) + 5(2) - 1 = 8 - 2(4) + 10 - 1$$

$$= 8 - 8 + 10 - 1 = \boxed{9}$$

**Cara kedua: skema Horner.** Susun ulang polinomialnya sebagai perkalian bersarang:

$$P(x) = \Big(\big((x - 2)x + 5\big)x - 1\Big)$$

lalu hitung dari dalam dengan $x = 2$:

$$2 - 2 = 0, \qquad 0 \times 2 + 5 = 5, \qquad 5 \times 2 - 1 = 9$$

Hasil yang sama, tetapi tanpa memangkatkan apa pun — hanya kalikan dan tambah berulang.
Untuk polinomial berderajat tinggi, cara ini jauh lebih hemat dan lebih kecil peluang
salahnya.

Menghitung $P(a)$ akan sering dipakai, dan bukan hanya untuk mencari nilai. **Teorema
sisa** menyatakan $P(a)$ adalah sisa pembagian $P(x)$ oleh $(x-a)$; jadi perhitungan di
atas sekaligus memberitahu bahwa $P(x)$ dibagi $(x-2)$ bersisa $9$.

Kesalahan yang paling sering pada substitusi adalah tanda. Suku $-2x^2$ berarti
$-2 \times x^2$, bukan $(-2x)^2$. Untuk $x$ negatif bedanya makin menentukan: pada
$x = -1$, yang pertama memberi $-2$ dan yang kedua memberi $4$.
