---
id: fkt-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Ada berapa akar real dari persamaan

$$x^3 - 4x = 0\ ?$$

## Petunjuk

- Ruas kanannya nol. Itu keadaan yang paling menguntungkan — hasil kali bernilai nol hanya kalau salah satu bagiannya nol.
- Keluarkan faktor persekutuannya lebih dulu, lalu lihat sisanya.
- Setelah menjadi $x(x^2-4) = 0$, faktor keduanya masih bisa dipecah lagi.

## Pembahasan

Ruas kanan bernilai nol, jadi faktorkan ruas kiri.

Faktor persekutuannya $x$:

$$x^3 - 4x = x\left(x^2 - 4\right)$$

Faktor keduanya selisih kuadrat, jadi masih bisa dipecah:

$$x\left(x^2-4\right) = x(x-2)(x+2)$$

Persamaannya menjadi

$$x(x-2)(x+2) = 0$$

Hasil kali bernilai nol tepat ketika salah satu faktornya nol:

$$x = 0, \qquad x = 2, \qquad x = -2$$

Ada $\boxed{3}$ akar real.

**Perhatikan jebakan terbesarnya.** Godaan pertama adalah menulis $x^3 = 4x$ lalu membagi
kedua ruas dengan $x$, memberi $x^2 = 4$ dan hanya dua akar. Solusi $x = 0$ hilang, karena
membagi dengan $x$ diam-diam mengandaikan $x \ne 0$.

Aturannya: **jangan membagi, pindahkan lalu faktorkan.** Membagi dengan sesuatu yang bisa
bernilai nol selalu berisiko menghilangkan solusi.

Perhatikan juga langkah kedua. Berhenti di $x(x^2-4) = 0$ tetap memberi jawaban benar di
sini, tetapi kebiasaan memfaktorkan sampai tuntas menyelamatkan pada soal yang lebih
rumit.
