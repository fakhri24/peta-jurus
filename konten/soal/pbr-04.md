---
id: pbr-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 3
jawaban: "30240"
---

## Soal

Dari seluruh huruf pada kata **MATEMATIKA**, ada berapa susunan yang **kedua huruf T-nya
berdampingan**?

## Petunjuk

- Selama kedua T tidak boleh terpisah, keduanya selalu bergerak bersama. Perlakukan keduanya sebagai satu benda.
- Setelah kedua T disatukan, ada berapa benda yang tersisa untuk disusun, dan huruf mana saja yang masih berulang?
- Perhatikan baik-baik apakah isi kesatuan itu masih bisa ditukar. Kedua T sama persis.

## Pembahasan

**Ikat kedua T menjadi satu blok.** Karena keduanya harus berdampingan, mereka tidak pernah
terpisah.

Yang tersisa untuk disusun adalah:

$$[\text{TT}],\ \text{M},\ \text{M},\ \text{A},\ \text{A},\ \text{A},\ \text{E},\ \text{I},\ \text{K}$$

yaitu $9$ benda. Periksa: $1 + 2 + 3 + 1 + 1 + 1 = 9$.

**Huruf yang masih berulang** di antara kesembilan benda itu adalah M sebanyak $2$ dan A
sebanyak $3$. Blok $[\text{TT}]$ hanya ada satu.

$$\frac{9!}{2!\,3!} = \frac{362\,880}{2 \times 6} = \frac{362\,880}{12} = \boxed{30240}$$

**Mengapa tidak dikalikan $2$.** Pada soal berdampingan dengan dua benda **berbeda**, blok
itu masih bisa dibalik sehingga jawabannya dikalikan $2!$. Di sini tidak: kedua T sama
persis, jadi $\text{T}_1\text{T}_2$ dan $\text{T}_2\text{T}_1$ adalah blok yang sama.
Mengalikan $2$ di sini adalah kekeliruan, dan hasilnya dua kali lipat dari yang benar.

**Periksa kewajarannya.** Seluruh susunan MATEMATIKA ada $151\,200$. Bagian yang kedua
T-nya berdampingan:

$$\frac{30\,240}{151\,200} = \frac{1}{5}$$

Masuk akal — pada susunan sepuluh huruf, peluang dua huruf tertentu berdampingan adalah
$\frac{2 \times 9}{10 \times 9} = \frac15$.

**Soal kebalikannya** — kedua T **tidak** berdampingan — dikerjakan dengan mengurangkan:

$$151\,200 - 30\,240 = 120\,960$$

**Kalau yang harus berdampingan adalah huruf yang berbeda,** misalnya E dan I, hitungannya
berubah: blok $[\text{EI}]$ bisa dibalik, jadi jawabannya
$\frac{9!}{2!\,2!\,3!} \times 2 = 15\,120 \times 2 = 30\,240$. Kebetulan sama besarnya di
sini, tetapi jalannya berbeda — dan pada soal lain hasilnya tidak akan kebetulan sama.
