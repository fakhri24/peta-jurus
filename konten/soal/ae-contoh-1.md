---
id: ae-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [algoritma-euklid]
bentuk: isian
kesulitan: 3
jawaban: "63"
---

## Soal

Tentukan $\gcd\left(2^{12} - 1,\ 2^{18} - 1\right)$.

## Petunjuk

- Jangan hitung kedua bilangannya. Pakai versi selisih dari algoritma Euklid.
- $2^{18} - 1 = 2^{6}\left(2^{12} - 1\right) + \left(2^{6} - 1\right)$.
- Langkah itu menurunkan $18$ jadi $12$, lalu $12$ jadi $6$ — persis algoritma Euklid pada eksponennya.

## Pembahasan

Kuncinya satu langkah pembagian bersusun:

$$2^{18} - 1 = 2^{6}\left(2^{12} - 1\right) + \left(2^{6} - 1\right)$$

(periksa: $2^6 \cdot 2^{12} - 2^6 + 2^6 - 1 = 2^{18} - 1$). Maka

$$\gcd\left(2^{18}-1,\ 2^{12}-1\right) = \gcd\left(2^{12}-1,\ 2^{6}-1\right)$$

Ulangi: $2^{12} - 1 = 2^{6}\left(2^{6}-1\right) + \left(2^{6}-1\right)$, sehingga
$2^6 - 1$ membagi $2^{12}-1$ dan prosesnya berhenti.

$$\gcd\left(2^{12}-1,\ 2^{18}-1\right) = 2^{6} - 1 = \boxed{63}$$

Yang sebenarnya terjadi: **eksponennya sendiri yang menjalani algoritma Euklid.** Ini
berlaku umum,

$$\gcd\left(a^m - 1,\ a^n - 1\right) = a^{\gcd(m,n)} - 1$$

dan di sini $\gcd(12,18) = 6$. Identitas ini pantas dihafal — ia muncul terus di OSN-P
ke atas.
