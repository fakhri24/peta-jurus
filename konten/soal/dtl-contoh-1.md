---
id: dtl-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Ada berapa pasangan bilangan asli $(x, y)$ yang memenuhi $x^2 - y^2 = 45$?

## Petunjuk

- Refleks pertama untuk persamaan tak linear: bisakah ruas kirinya difaktorkan?
- $x^2 - y^2 = (x-y)(x+y)$, jadi soalnya berubah menjadi mencacah pasangan pembagi $45$.
- Perhatikan syarat tambahannya: $x - y$ dan $x + y$ harus berparitas sama, dan keduanya positif dengan $x - y < x + y$.

## Pembahasan

Faktorkan ruas kiri:

$$(x - y)(x + y) = 45$$

Karena $x, y$ asli dan $x^2 > y^2$, kedua faktornya positif dengan $x - y < x + y$.

**Syarat paritas.** Jumlah kedua faktor adalah $(x-y) + (x+y) = 2x$, yang genap. Dua
bilangan berjumlah genap pasti berparitas sama. Di sini $45$ ganjil, jadi kedua faktornya
otomatis ganjil — syarat itu terpenuhi sendiri.

**Cacah pasangan pembagi.** Pasangan $(d, e)$ dengan $de = 45$ dan $d < e$:

$$(1, 45), \qquad (3, 15), \qquad (5, 9)$$

Masing-masing memberi $x = \dfrac{d+e}{2}$ dan $y = \dfrac{e-d}{2}$:

| $(d, e)$ | $x$ | $y$ |
|---|---|---|
| $(1, 45)$ | $23$ | $22$ |
| $(3, 15)$ | $9$ | $6$ |
| $(5, 9)$ | $7$ | $2$ |

Ketiganya memberi $x, y$ bilangan asli. Jadi ada $\boxed{3}$ pasangan.

Periksa satu: $9^2 - 6^2 = 81 - 36 = 45$. Benar.

Syarat paritas itu yang sering terlupa, dan ia menggigit begitu ruas kanannya genap. Untuk
$x^2 - y^2 = 30$, pasangan $(2, 15)$ memang berhasil kali $30$, tetapi paritasnya berbeda
sehingga $x$ dan $y$ tidak bulat.
