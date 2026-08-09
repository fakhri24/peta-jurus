---
id: tpm-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: isian
kesulitan: 3
jawaban: "6"
---

## Soal

Sebuah tumpukan berisi $n$ batu. Dua pemain bergantian mengambil $1$, $2$, $3$, atau $4$
batu, dan pemain yang tidak bisa melangkah dinyatakan kalah.

Di antara $n = 1, 2, 3, \dots, 30$, ada berapa nilai $n$ yang membuat **pemain pertama
kalah**?

## Petunjuk

- Tentukan dulu pola keadaan kalah dengan mengerjakan mundur dari tumpukan kosong.
- Perhatikan berapa banyak pilihan langkah yang tersedia; angka itu menentukan pola kelipatannya.
- Setelah polanya diketahui, tinggal mencacah berapa nilai dalam rentang yang mengikutinya.

## Pembahasan

**Tandai keadaannya.** Sebut P keadaan yang membuat pemain yang mendapat giliran kalah.

- $0$: tidak bisa melangkah → **P**.
- $1,2,3,4$: bisa mengambil semuanya dan meninggalkan $0$ → **N**.
- $5$: langkahnya menuju $4,3,2,1$ — seluruhnya N → **P**.

Polanya berulang tiap $5$:

$$n \equiv 0 \pmod 5 \ \Longleftrightarrow\ \text{keadaan P}$$

**Buktikan polanya.**

1. Dari $5m$, mengambil $k \in \{1,2,3,4\}$ memberi $5m-k$, yang tidak habis dibagi $5$ →
   selalu N.
2. Dari $n = 5m + r$ dengan $1 \le r \le 4$, ambil $r$ batu dan tersisa $5m$ → P.

**Cacah dalam rentangnya.** Pemain pertama kalah tepat ketika $n$ kelipatan $5$:

$$5,\ 10,\ 15,\ 20,\ 25,\ 30$$

Ada $\boxed{6}$ nilai.

**Cara menghitungnya:** $\left\lfloor \frac{30}{5} \right\rfloor = 6$.

**Bentuk umumnya.** Kalau langkah yang boleh diambil adalah $1$ sampai $k$, keadaan P adalah
kelipatan $k+1$. Alasannya selalu sama: apa pun yang diambil lawan, sisanya dapat
dilengkapi menjadi $k+1$ — sebab kalau lawan mengambil $a$, maka $k+1-a$ berada di antara
$1$ dan $k$, jadi selalu langkah yang sah.

Kemampuan "melengkapi" itu inti seluruh strategi, dan ia yang menjaga lawan selalu berada di
kelipatan $k+1$.

**Perhatikan angka $0$ tidak ikut dicacah,** sebab soal meminta $n$ dari $1$ sampai $30$.
Kalau $n = 0$ ikut dihitung, jawabannya $7$. Membaca batas rentang dengan teliti sama
pentingnya dengan menemukan polanya.
