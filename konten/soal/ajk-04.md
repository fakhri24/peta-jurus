---
id: ajk-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 2
jawaban: "64"
---

## Soal

Ada berapa himpunan bagian dari $\{1, 2, 3, \dots, 8\}$ yang **memuat** $1$ tetapi
**tidak memuat** $2$?

## Petunjuk

- Membentuk sebuah himpunan bagian sama artinya dengan memutuskan, untuk tiap unsur, ikut atau tidak ikut.
- Dua di antara delapan keputusan itu sudah ditetapkan oleh soal, jadi tidak ada pilihan di sana.
- Sisanya bebas sepenuhnya, dan tiap unsur menyumbang dua kemungkinan.

## Pembahasan

Kuncinya melihat pembentukan himpunan bagian sebagai **rangkaian keputusan**: untuk tiap
unsur, ia ikut atau tidak. Ada $8$ unsur, jadi $8$ keputusan.

**Dua keputusan sudah ditetapkan soal:**

- Unsur $1$ **harus** ikut — $1$ cara.
- Unsur $2$ **harus tidak** ikut — $1$ cara.

**Enam keputusan sisanya bebas.** Unsur $3, 4, 5, 6, 7, 8$ masing-masing punya $2$ pilihan,
dan pilihan itu tidak dipengaruhi keputusan mana pun sebelumnya:

$$\underbrace{2 \times 2 \times 2 \times 2 \times 2 \times 2}_{6 \text{ unsur}} = 2^{6} = \boxed{64}$$

**Mengapa unsur yang ditetapkan tidak menyumbang faktor.** Faktor $1$ boleh saja ditulis —
$1 \times 1 \times 2^6$ — tapi tidak mengubah apa pun. Yang menentukan jawaban hanyalah
banyaknya keputusan yang **masih bebas**.

Cara pandang ini terbawa jauh. Seluruh himpunan bagian dari himpunan berukuran $n$ ada
$2^{n}$, karena tiap unsur menyumbang dua kemungkinan. Setiap syarat yang mematok satu
unsur memangkas jawabannya menjadi setengah: di sini dua unsur dipatok, dan $2^8 = 256$
turun menjadi $256 / 4 = 64$.

Coba juga variasinya sebagai latihan sendiri: "memuat $1$ **atau** memuat $2$" bukan lagi
soal yang sama, dan menghitungnya butuh kehati-hatian karena kedua kelompoknya beririsan.
