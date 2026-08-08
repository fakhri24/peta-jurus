---
id: ind-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [induksi]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan dengan induksi matematika bahwa $7^n - 1$ habis dibagi $6$ untuk setiap bilangan
asli $n$.

## Petunjuk

- Basisnya mudah. Yang perlu dipikirkan adalah bagaimana menghubungkan $7^{k+1}-1$ dengan $7^k-1$.
- Tulis $7^{k+1} - 1 = 7 \cdot 7^k - 1$, lalu sisipkan $-7 + 7$ supaya bentuk $7^k - 1$ muncul.
- Hasilnya $7\left(7^k-1\right) + 6$ — dan kedua sukunya habis dibagi $6$.

## Pembahasan

### Basis

Untuk $n = 1$: $7^1 - 1 = 6$, yang habis dibagi $6$. Benar.

### Langkah induksi

Andaikan benar untuk $n = k$, yaitu $6 \mid \left(7^k - 1\right)$. Artinya ada bilangan
bulat $m$ dengan

$$7^k - 1 = 6m$$

Akan ditunjukkan $6 \mid \left(7^{k+1} - 1\right)$.

**Susun ulang supaya bentuk hipotesis muncul.**

$$7^{k+1} - 1 = 7 \cdot 7^k - 1$$

Sisipkan $-7 + 7$ agar $7^k - 1$ terbentuk:

$$= 7 \cdot 7^k - 7 + 6 = 7\left(7^k - 1\right) + 6$$

**Pakai hipotesis.** Substitusikan $7^k - 1 = 6m$:

$$7^{k+1} - 1 = 7(6m) + 6 = 6(7m + 1)$$

Karena $7m+1$ bilangan bulat, ruas kanan habis dibagi $6$.

### Kesimpulan

Basis benar dan langkah induksinya berlaku, jadi $6 \mid \left(7^n-1\right)$ untuk setiap
bilangan asli $n$. $\blacksquare$

Langkah "sisipkan $-7+7$" adalah gerakan baku pada soal keterbagian dengan induksi.
Tujuannya satu: **memaksa bentuk hipotesis muncul**, supaya ia bisa dipakai. Tanpa itu,
$7 \cdot 7^k - 1$ tidak memberi jalan apa pun.

Ada bukti lain yang jauh lebih pendek lewat faktorisasi:

$$7^n - 1 = (7-1)\left(7^{n-1} + 7^{n-2} + \cdots + 1\right) = 6 \times (\text{bilangan bulat})$$

Bahkan berlaku umum: $a^n - 1$ selalu habis dibagi $a-1$. Tetapi yang dilatih di sini
adalah menyusun langkah induksinya — dan keterampilan itu terpakai justru pada soal yang
tidak punya faktorisasi rapi.

## Rubrik

- Memeriksa basis pada $n = 1$
- Menuliskan hipotesis sebagai $7^k - 1 = 6m$ untuk suatu bilangan bulat $m$ — bukan sekadar "habis dibagi 6"
- Menyusun ulang $7^{k+1}-1$ menjadi $7\left(7^k-1\right) + 6$
- Mensubstitusikan hipotesis dan mengeluarkan faktor $6$
- Menyebut bahwa faktor keduanya bilangan bulat, sehingga keterbagiannya tegak
