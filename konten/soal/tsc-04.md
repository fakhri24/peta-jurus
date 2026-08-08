---
id: tsc-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [teorema-sisa-cina, fungsi-euler]
bentuk: isian
kesulitan: 3
jawaban: "649"
---

## Soal

Tentukan tiga angka terakhir dari $7^{2026}$.

## Petunjuk

- Tiga angka terakhir berarti modulo $1000$. Modulus itu bukan pangkat prima — pecah dulu.
- $1000 = 8 \times 125$, dan keduanya relatif prima. Kerjakan modulo $8$ dan modulo $125$ secara terpisah.
- Setelah kedua sisanya diperoleh, gabungkan kembali dengan substitusi seperti biasa.

## Pembahasan

Tiga angka terakhir berarti sisa modulo $1000$. Karena

$$1000 = 8 \times 125, \qquad \gcd(8, 125) = 1$$

Teorema Sisa Cina membolehkan soal ini dipecah menjadi dua soal yang jauh lebih kecil.

**Modulo $8$.** Karena $7 \equiv -1 \pmod 8$:

$$7^{2026} \equiv (-1)^{2026} = 1 \pmod 8$$

**Modulo $125$.** Di sini $\gcd(7,125) = 1$, jadi Teorema Euler berlaku dengan

$$\varphi(125) = 125 - 25 = 100$$

Karena $2026 = 100 \times 20 + 26$:

$$7^{2026} \equiv 7^{26} \pmod{125}$$

Hitung bertahap: $7^2 = 49$, lalu

$$7^4 = 49^2 = 2401 = 19 \times 125 + 26 \equiv 26$$

$$7^8 \equiv 26^2 = 676 = 5 \times 125 + 51 \equiv 51$$

$$7^{16} \equiv 51^2 = 2601 = 20 \times 125 + 101 \equiv 101$$

Karena $26 = 16 + 8 + 2$:

$$7^{26} \equiv 101 \times 51 \times 49 \pmod{125}$$

Hitung bertahap: $101 \times 51 = 5151 = 41 \times 125 + 26 \equiv 26$, lalu
$26 \times 49 = 1274 = 10 \times 125 + 24 \equiv 24$.

Jadi $7^{2026} \equiv 24 \pmod{125}$.

**Gabungkan.** Dicari $x$ dengan

$$x \equiv 1 \pmod 8, \qquad x \equiv 24 \pmod{125}$$

Dari yang kedua, tulis $x = 125t + 24$. Masukkan ke yang pertama:

$$125t + 24 \equiv 1 \pmod 8$$

Karena $125 = 15 \times 8 + 5 \equiv 5$ dan $24 \equiv 0 \pmod 8$:

$$5t \equiv 1 \pmod 8$$

Invers $5$ modulo $8$ adalah $5$, sebab $5 \times 5 = 25 \equiv 1$. Maka
$t \equiv 5 \pmod 8$, tulis $t = 8s + 5$:

$$x = 125(8s + 5) + 24 = 1000s + 649$$

Tiga angka terakhirnya adalah $\boxed{649}$.

Perhatikan pembagian kerjanya: modulo $8$ diselesaikan dalam satu baris karena
$7 \equiv -1$, sementara modulo $125$ memerlukan Teorema Euler. Memecah $1000$ bukan
sekadar mempercepat — ia mengubah satu soal sulit menjadi satu soal sepele dan satu soal
sedang.
