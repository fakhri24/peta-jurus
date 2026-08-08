---
id: el-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [eksponen-logaritma]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan nilai $x$ yang memenuhi

$$2^{x+1} + 2^x = 24$$

## Petunjuk

- Kedua suku memuat $2^x$. Keluarkan sebagai faktor persekutuan.
- $2^{x+1} = 2^x \cdot 2$, jadi ruas kirinya $2 \cdot 2^x + 2^x$.
- Setelah menjadi $3 \cdot 2^x = 24$, samakan basisnya.

## Pembahasan

Pisahkan pangkatnya dengan aturan $a^{m+n} = a^m a^n$:

$$2^{x+1} = 2^x \cdot 2^1 = 2 \cdot 2^x$$

Substitusikan:

$$2 \cdot 2^x + 2^x = 24$$

Keluarkan $2^x$ sebagai faktor persekutuan:

$$2^x (2 + 1) = 24 \quad\Longrightarrow\quad 3 \cdot 2^x = 24 \quad\Longrightarrow\quad
2^x = 8$$

Samakan basisnya:

$$2^x = 2^3 \quad\Longrightarrow\quad x = \boxed{3}$$

Periksa: $2^4 + 2^3 = 16 + 8 = 24$. Cocok.

Langkah "samakan basis lalu samakan pangkat" sah karena fungsi $a^x$ dengan $a > 0$ dan
$a \ne 1$ bersifat satu-satu — tidak ada dua pangkat berbeda yang memberi nilai sama.
Syarat $a \ne 1$ itu penting: pada $1^x = 1$, setiap $x$ memenuhi.

Pola "keluarkan pangkat terkecil sebagai faktor" bekerja pada hampir semua persamaan
eksponen dengan beberapa suku sebasis. Untuk $3^{x+2} - 3^x = 72$ misalnya, keluarkan
$3^x$ dan yang tersisa $3^x(9-1) = 72$.
