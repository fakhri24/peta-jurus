---
id: smp-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 3
jawaban: "8"
---

## Soal

Beberapa bilangan bulat dipilih secara sembarang — tidak harus berurutan, tidak harus
positif.

Paling sedikit berapa bilangan harus dipilih supaya **pasti** ada dua di antaranya yang
**selisihnya habis dibagi $7$**?

## Petunjuk

- Selisih dua bilangan habis dibagi $7$ tepat ketika keduanya bersisa sama saat dibagi $7$. Mulailah dari situ.
- Ada berapa kemungkinan sisa pembagian oleh $7$? Jangan lupa sisa $0$ ikut terhitung.
- Kelompokkan bilangan menurut sisanya, lalu tanyakan kapan dua bilangan terpaksa jatuh ke kelompok yang sama.

## Pembahasan

**Terjemahkan syaratnya menjadi sesuatu yang bisa dijadikan sarang.** Untuk dua bilangan
bulat $a$ dan $b$:

$$7 \mid (a - b) \quad\Longleftrightarrow\quad a \equiv b \pmod 7$$

yaitu keduanya bersisa sama saat dibagi $7$. Terjemahan inilah langkah yang menentukan;
tanpanya, sarang yang berguna tidak akan terlihat.

**Sarangnya sisa pembagian oleh $7$:**

$$0, 1, 2, 3, 4, 5, 6$$

Banyaknya

$$k = 7$$

Perhatikan sisa $0$ ikut dihitung — inilah sebabnya sarangnya $7$, bukan $6$.

**Keadaan terburuk.** Dengan $7$ bilangan, masih mungkin tidak ada dua yang bersisa sama:
ambil satu wakil untuk tiap sisa, misalnya

$$1,\ 2,\ 3,\ 4,\ 5,\ 6,\ 7$$

Sisanya berturut-turut $1,2,3,4,5,6,0$ — seluruhnya berbeda, jadi tidak ada dua yang
selisihnya habis dibagi $7$.

**Bilangan kedelapan.** Sisanya harus salah satu dari ketujuh sisa yang ada, dan semuanya
sudah terpakai. Maka ada dua bilangan bersisa sama, dan selisihnya habis dibagi $7$.

$$\boxed{8}$$

**Bentuk umumnya:** dari $n+1$ bilangan bulat sembarang, pasti ada dua yang selisihnya
habis dibagi $n$. Ini salah satu pemakaian prinsip sarang merpati yang paling sering muncul
di olimpiade, dan pengenalnya selalu sama — soal berbicara tentang **keterbagian** sebuah
selisih.

**Perhatikan bahwa bilangannya boleh negatif dan boleh sangat besar,** dan itu tidak
mengubah apa pun. Sisa pembagian oleh $7$ tetap hanya ada tujuh kemungkinan, berapa pun
bilangannya. Kekuatan jurus ini justru di situ: himpunan yang tak berhingga tetap bisa
dikurung ke dalam sarang yang berhingga.
