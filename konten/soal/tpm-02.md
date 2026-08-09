---
id: tpm-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [teori-permainan]
bentuk: isian
kesulitan: 4
jawaban: "10"
---

## Soal

Sebuah tumpukan berisi $n$ batu. Dua pemain bergantian mengambil **$1$, $2$, atau $4$** batu
— tidak boleh $3$. Pemain yang tidak bisa melangkah dinyatakan kalah.

Di antara $n = 1, 2, 3, \dots, 30$, ada berapa nilai $n$ yang membuat pemain pertama kalah?

## Petunjuk

- Polanya tidak lagi sekadar "kelipatan banyaknya pilihan", sebab langkah yang boleh diambil tidak berurutan. Kerjakan mundur satu per satu.
- Buat tabel dari $0$ sampai sekitar $12$, dan tandai tiap keadaan sebelum menebak polanya.
- Setelah polanya terlihat, buktikan kedua arahnya sebelum dipakai.

## Pembahasan

**Kerjakan mundur.** Sebuah keadaan adalah N kalau ada langkah menuju P, dan P kalau seluruh
langkahnya menuju N.

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tanda | P | N | N | P | N | N | P | N | N | P | N | N | P |

Beberapa barisnya, supaya terlihat cara mengisinya:

- $3$: langkahnya menuju $2$ (N), $1$ (N). Mengambil $4$ tidak sah karena batunya cuma $3$.
  Seluruh langkah menuju N → **P**.
- $4$: bisa mengambil $1$ dan menuju $3$ (P) → **N**.
- $6$: langkahnya menuju $5$ (N), $4$ (N), $2$ (N). Seluruhnya N → **P**.

**Polanya.**

$$n \equiv 0 \pmod 3 \ \Longleftrightarrow\ \text{keadaan P}$$

**Buktikan kedua arahnya.**

1. **Dari $n \equiv 0$, setiap langkah menuju N.** Mengambil $1$, $2$, atau $4$ memberi sisa
   $n-1 \equiv 2$, $n-2 \equiv 1$, atau $n-4 \equiv 2 \pmod 3$. Tidak satu pun habis dibagi
   $3$.
2. **Dari $n \not\equiv 0$, ada langkah menuju P.** Kalau $n \equiv 1$, ambil $1$ batu.
   Kalau $n \equiv 2$, ambil $2$ batu. Keduanya langkah yang sah selama batunya cukup.

**Cacah dalam rentangnya.** Kelipatan $3$ dari $1$ sampai $30$:

$$\left\lfloor \frac{30}{3} \right\rfloor = \boxed{10}$$

**Mengapa langkah "$4$" tidak mengubah polanya.** Perhatikan $4 \equiv 1 \pmod 3$, sehingga
mengambil $4$ batu berpengaruh sama dengan mengambil $1$ batu terhadap sisa pembagian oleh
$3$. Ia tidak menambah kemampuan apa pun yang belum dimiliki langkah $1$.

Karena itu permainan ini berperilaku persis seperti permainan dengan langkah $\{1,2\}$, yang
keadaan P-nya memang kelipatan $3$.

**Pelajaran yang dibawa soal ini.** Menebak pola dari bentuk himpunan langkahnya — misalnya
mengira jawabannya kelipatan $4$ karena angka terbesarnya $4$ — akan keliru. Yang menentukan
adalah **sisa pembagian** yang bisa dicapai tiap langkah, dan itu hanya terlihat setelah
tabelnya dikerjakan.

Kebiasaan yang aman: kerjakan tabel sampai polanya berulang sedikitnya dua putaran penuh,
baru tebak, lalu buktikan kedua arahnya.
