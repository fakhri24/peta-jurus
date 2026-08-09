---
id: psk-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 2
jawaban: "240"
---

## Soal

Tujuh orang duduk mengelilingi meja bundar tanpa nomor kursi. Dua orang di antaranya, Ani
dan Budi, ingin duduk **berdampingan**.

Ada berapa susunan tempat duduk yang berbeda?

## Petunjuk

- Selama keduanya harus berdampingan, mereka bergerak bersama. Perlakukan keduanya sebagai satu kesatuan.
- Setelah keduanya disatukan, berapa benda yang duduk melingkar, dan berapa susunan melingkarnya?
- Ani dan Budi masih bisa bertukar tempat di dalam kesatuan itu, dan keduanya orang yang berbeda.

## Pembahasan

**Ikat keduanya menjadi satu blok.** Yang duduk melingkar sekarang adalah

$$[\text{Ani–Budi}], \ C, \ D, \ E, \ F, \ G$$

yaitu $6$ benda.

**Susun melingkar.** Meja tetap bundar dan kursinya tetap tidak bernomor:

$$(6-1)! = 5! = 120$$

**Susunan di dalam blok.** Ani bisa di kiri Budi atau di kanannya, dan pada meja bundar
kedua keadaan itu **berbeda** — tetangga kiri dan tetangga kanan bukan hal yang sama:

$$2! = 2$$

**Gabungkan.**

$$120 \times 2 = \boxed{240}$$

**Bagian yang paling sering keliru** adalah memakai $(7-1)!$ untuk langkah pertama. Setelah
Ani dan Budi disatukan, yang duduk melingkar tinggal $6$ benda — bukan $7$. Blok itu
menempati satu kedudukan di lingkaran, meskipun ia memakai dua kursi.

**Periksa kewajarannya.** Seluruh susunan tujuh orang melingkar ada $6! = 720$. Bagian yang
Ani dan Budi-nya berdampingan:

$$\frac{240}{720} = \frac13$$

Masuk akal: pada meja bundar berisi tujuh orang, Ani punya $6$ orang lain yang mungkin, dan
$2$ di antaranya duduk bersebelahan dengannya. Peluangnya $\frac26 = \frac13$. Cocok.

**Soal kebalikannya** — Ani dan Budi tidak berdampingan — dikerjakan dengan mengurangkan:

$$720 - 240 = 480$$
