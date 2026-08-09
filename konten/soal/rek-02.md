---
id: rek-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [rekursi]
bentuk: isian
kesulitan: 3
jawaban: "144"
---

## Soal

Ada berapa barisan sepanjang $10$ yang tiap sukunya $0$ atau $1$, dengan syarat **tidak ada
dua angka $1$ yang berdampingan**?

## Petunjuk

- Beri nama untuk jawaban panjang $n$, lalu pecah menurut suku terakhirnya.
- Kalau suku terakhirnya $0$, tidak ada syarat tambahan pada sisanya. Kalau $1$, suku sebelumnya sudah dipaksa.
- Kerjakan panjang $1$ dan $2$ dengan mendaftar, supaya kasus dasarnya pasti benar.

## Pembahasan

Sebut $b_n$ banyaknya barisan panjang $n$ yang memenuhi syarat.

**Pecah menurut suku terakhir.**

- **Berakhir $0$.** Sisa barisannya adalah barisan sah sepanjang $n-1$, tanpa syarat
  tambahan — sebab $0$ di ujung tidak pernah melanggar apa pun. Banyaknya $b_{n-1}$.
- **Berakhir $1$.** Suku sebelumnya **harus** $0$, kalau tidak ada dua angka $1$
  berdampingan. Jadi barisannya berakhir dengan $\dots 0\,1$, dan bagian di depannya adalah
  barisan sah sepanjang $n-2$. Banyaknya $b_{n-2}$.

Kedua kelompok lepas — suku terakhir tidak mungkin $0$ sekaligus $1$ — dan menutupi
semuanya. Maka

$$b_n = b_{n-1} + b_{n-2}$$

**Kasus dasarnya**, dengan mendaftar:

$$b_1 = 2 \quad (0,\ 1)$$

$$b_2 = 3 \quad (00,\ 01,\ 10) \ \text{--- barisan } 11 \text{ dibuang}$$

**Hitung.**

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $b_n$ | $2$ | $3$ | $5$ | $8$ | $13$ | $21$ | $34$ | $55$ | $89$ | $\boxed{144}$ |

**Periksa $b_3 = 5$ dengan mendaftar:** $000, 001, 010, 100, 101$. Tepat $5$ — barisan
$011$, $110$, dan $111$ dibuang.

**Rekurensnya sama dengan soal tangga, kasus dasarnya berbeda.** Di soal tangga barisannya
$1, 2, 3, 5, 8, \dots$; di sini $2, 3, 5, 8, \dots$ — bergeser satu suku. Karena itu
menyalin jawaban dari soal yang "polanya sama" tanpa memeriksa kasus dasarnya adalah cara
tercepat mendapat jawaban yang salah.

**Yang menentukan pemecahan kasusnya** adalah pertanyaan: bagian mana dari barisan yang
**membatasi** apa yang boleh ditulis berikutnya? Di sini hanya suku terakhir yang penting —
syaratnya cuma menyangkut tetangga langsung. Kalau syaratnya "tidak ada **tiga** angka $1$
berturut-turut", yang harus diingat adalah dua suku terakhir, dan rekurensnya menjadi orde
tiga.
