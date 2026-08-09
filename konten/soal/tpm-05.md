---
id: tpm-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: isian
kesulitan: 4
jawaban: "9"
---

## Soal

Sebuah tumpukan berisi $n$ batu. Dua pemain bergantian mengambil sejumlah batu yang berupa
**bilangan kuadrat sempurna** — yaitu $1$, $4$, $9$, $16$, atau $25$ batu. Pemain yang tidak
bisa melangkah dinyatakan kalah.

Di antara $n = 1, 2, \dots, 30$, ada berapa nilai $n$ yang membuat pemain pertama kalah?

## Petunjuk

- Langkah yang tersedia tidak berjarak tetap, jadi jangan berharap polanya berupa kelipatan sederhana. Kerjakan tabelnya baris demi baris.
- Sebuah keadaan adalah P kalau **semua** langkah yang sah darinya menuju keadaan N.
- Kerjakan sampai $n = 30$, dan berhati-hatilah: polanya di sini tidak sesederhana yang terlihat di awal.

## Pembahasan

**Kerjakan mundur.** Langkah yang boleh diambil adalah $1, 4, 9, 16, 25$ — selama batunya
mencukupi. Sebuah keadaan adalah N kalau ada langkah menuju P.

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tanda | P | N | **P** | N | N | **P** | N | **P** | N | N | **P** |

Beberapa barisnya:

- $1$: ambil $1$, menuju $0$ (P) → **N**.
- $2$: satu-satunya langkah adalah $1$, menuju $1$ (N) → **P**.
- $3$: ambil $1$, menuju $2$ (P) → **N**.
- $5$: langkahnya menuju $4$ (N) dan $1$ (N) → **P**.
- $7$: langkahnya menuju $6$ (N) dan $3$ (N) → **P**.

**Lanjutkan sampai $30$.** Keadaan P yang muncul:

$$2,\ 5,\ 7,\ 10,\ 12,\ 15,\ 17,\ 20,\ 22$$

Ada $\boxed{9}$ nilai.

**Polanya tidak sesederhana yang terlihat.** Sembilan nilai pertama itu mengikuti pola
$n \equiv 0$ atau $2 \pmod 5$, dan mudah tergoda menyimpulkan polanya berulang tiap $5$
selamanya. Tetapi pola itu **rusak** setelah $22$: keadaan $25$, $27$, dan $30$ ternyata
bukan P, sebab langkah $25$ mulai tersedia dan membuka jalan menuju keadaan P yang
sebelumnya tidak terjangkau.

Karena itu jawabannya $9$, bukan $12$ yang akan diperoleh dengan meneruskan pola secara
buta.

**Inilah pelajaran utama soal ini.** Pada permainan dengan langkah yang berjarak tetap —
seperti $1$ sampai $k$ — polanya memang berulang selamanya, dan bisa dibuktikan. Pada
permainan dengan langkah yang **jaraknya makin melebar**, pola awal sering hanya berlaku
sementara: langkah-langkah besar baru mulai berpengaruh setelah tumpukannya cukup banyak.

Karena itu menebak pola dari sepuluh suku pertama berbahaya, dan kebiasaan yang aman adalah:

1. kerjakan tabelnya sampai batas yang ditanyakan, bukan sampai polanya "terlihat";
2. kalau pola dipakai, buktikan kedua arahnya — dan pada permainan seperti ini, pembuktian
   itu biasanya gagal, yang justru pertanda pola tersebut memang tidak berlaku.

**Perhatikan langkah yang tidak sah tidak boleh ikut dipertimbangkan.** Untuk $n = 2$, hanya
langkah $1$ yang tersedia; mengambil $4$ tidak mungkin. Melupakan batas itu akan menandai
$2$ sebagai N dan merusak seluruh tabel di bawahnya.
