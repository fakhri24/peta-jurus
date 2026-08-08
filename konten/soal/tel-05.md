---
id: tel-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 3
jawaban: "719"
---

## Soal

Tentukan nilai dari

$$1 \cdot 1! + 2 \cdot 2! + 3 \cdot 3! + 4 \cdot 4! + 5 \cdot 5!$$

## Petunjuk

- Menghitung langsung bisa, tetapi carilah dulu apakah tiap suku bisa ditulis sebagai selisih dua faktorial.
- Perhatikan $(k+1)! - k!$ dan jabarkan: $(k+1)! = (k+1) \cdot k!$.
- Hasilnya $(k+1)! - k! = k \cdot k!$ — persis bentuk tiap suku di soal.

## Pembahasan

Cari bentuk selisihnya. Karena $(k+1)! = (k+1) \cdot k!$,

$$(k+1)! - k! = (k+1)\cdot k! - k! = \left[(k+1) - 1\right] k! = k \cdot k!$$

Jadi tiap suku di soal **sudah** berupa selisih dua faktorial berurutan.

Tuliskan deretnya:

$$\left(2! - 1!\right) + \left(3! - 2!\right) + \left(4! - 3!\right) + \left(5! - 4!\right)
+ \left(6! - 5!\right)$$

Bagian tengahnya saling menghapus, menyisakan

$$6! - 1! = 720 - 1 = \boxed{719}$$

Periksa dengan menghitung langsung:

$$1 + 4 + 18 + 96 + 600 = 719$$

Cocok — tetapi jalur teleskop tidak menuntut menghitung satu pun faktorial selain yang
terakhir.

Bentuk umumnya:

$$\sum_{k=1}^{n} k \cdot k! = (n+1)! - 1$$

Keuntungannya baru terasa pada $n$ yang besar. Untuk $n = 20$, menghitung langsung berarti
menjumlahkan dua puluh bilangan raksasa; lewat teleskop, jawabannya $21! - 1$ dalam satu
baris.

**Pelajaran yang lebih umum:** teleskop tidak terbatas pada pecahan. Setiap kali kamu bisa
menulis suku ke-$k$ sebagai $f(k+1) - f(k)$ untuk suatu $f$, deretnya runtuh menjadi dua
ujung. Yang berbeda hanya cara menemukan $f$-nya.
