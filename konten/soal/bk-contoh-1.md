---
id: bk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: aljabar
tahap: osn
jurus: [bilangan-kompleks]
bentuk: isian
kesulitan: 2
jawaban: "-1"
---

## Soal

Tentukan nilai $i^{2026}$.

## Petunjuk

- Hitung beberapa pangkat pertama $i$ dan cari polanya.
- $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$ — lalu berulang.
- Karena siklusnya $4$, yang menentukan hanyalah sisa $2026$ dibagi $4$.

## Pembahasan

Hitung pangkat pertama $i$:

$$i^1 = i, \qquad i^2 = -1, \qquad i^3 = i^2 \cdot i = -i, \qquad i^4 = i^2 \cdot i^2 = 1$$

Setelah empat langkah nilainya kembali ke $1$, jadi pangkatnya **berulang dengan periode
$4$**.

Bagi eksponennya oleh $4$:

$$2026 = 4 \times 506 + 2$$

Maka

$$i^{2026} = \left(i^4\right)^{506} \times i^2 = 1^{506} \times (-1) = \boxed{-1}$$

**Cara membaca sisanya:** sisa $0$ memberi $1$, sisa $1$ memberi $i$, sisa $2$ memberi
$-1$, sisa $3$ memberi $-i$. Di sini sisanya $2$.

Untuk memeriksa sisa pembagian oleh $4$ dengan cepat, cukup lihat **dua digit terakhir**:
$26 = 6 \times 4 + 2$, jadi $2026 \equiv 2 \pmod 4$. Cocok.

Perhatikan bahwa struktur ini persis sama dengan mencari sisa pangkat dalam kongruensi:
temukan pangkat terkecil yang memberi $1$, lalu potong eksponennya. Bedanya di sini
siklusnya selalu $4$ dan tidak perlu dicari.

Akar keempat dari $1$ adalah $1$, $i$, $-1$, $-i$ — dan keempatnya persis nilai yang
muncul dalam siklus di atas. Itu bukan kebetulan: pangkat $i$ menjelajahi seluruh akar
keempat satuan.
