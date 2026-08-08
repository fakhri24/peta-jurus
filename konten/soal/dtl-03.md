---
id: dtl-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 3
jawaban: "0"
---

## Soal

Ada berapa pasangan bilangan bulat $(x, y)$ dengan $x > 0$ dan $y \ge 0$ yang memenuhi

$$x^2 - y^2 = 2026\ ?$$

## Petunjuk

- Faktorkan seperti biasa, lalu periksa syarat paritas kedua faktornya sebelum mencacah apa pun.
- $(x-y) + (x+y) = 2x$ selalu genap, jadi $x-y$ dan $x+y$ berparitas sama.
- Kalau keduanya genap, hasil kalinya habis dibagi $4$. Periksa $2026$ terhadap $4$.

## Pembahasan

Faktorkan:

$$(x - y)(x + y) = 2026$$

**Syarat paritas.** Jumlah kedua faktor adalah $2x$, yang genap — jadi $x-y$ dan $x+y$
berparitas sama. Ada dua kemungkinan:

- Keduanya ganjil. Maka hasil kalinya ganjil. Tetapi $2026$ genap, jadi mustahil.
- Keduanya genap. Maka hasil kalinya habis dibagi $4$.

**Periksa $2026$ terhadap $4$.** Karena

$$2026 = 2 \times 1013$$

dan $1013$ ganjil, maka $2026$ habis dibagi $2$ tetapi tidak habis dibagi $4$:

$$2026 = 4 \times 506 + 2$$

Jadi kemungkinan kedua juga mustahil.

Kedua kemungkinan gugur, sehingga tidak ada solusi sama sekali. Jawabannya $\boxed{0}$.

Bilangan yang **tidak** bisa ditulis sebagai selisih dua kuadrat persis bilangan yang
bersisa $2$ modulo $4$ — yaitu genap tetapi bukan kelipatan $4$. Semua bilangan ganjil bisa
($n = \left(\frac{n+1}{2}\right)^2 - \left(\frac{n-1}{2}\right)^2$), dan semua kelipatan
$4$ juga bisa.

Perhatikan bahwa mencari pasangan pembagi $2026$ satu per satu akan memakan waktu lama dan
tetap berujung nihil. Memeriksa paritas lebih dulu menutup soal dalam dua baris.
