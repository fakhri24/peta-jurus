---
id: tsf-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor]
bentuk: isian
kesulitan: 2
jawaban: "0"
---

## Soal

Tentukan sisa pembagian $8x^3 + 4x - 3$ oleh $(2x - 1)$.

## Petunjuk

- Pembaginya berkoefisien bukan satu. Tentukan dulu nilai $x$ yang membuatnya nol.
- $2x - 1 = 0$ tepat di $x = \frac12$.
- Sisanya adalah $P\!\left(\frac12\right)$.

## Pembahasan

Pembaginya bukan berbentuk $(x-a)$ apa adanya, jadi cari dulu akarnya:

$$2x - 1 = 0 \quad\Longrightarrow\quad x = \frac{1}{2}$$

Teorema sisa tetap berlaku dengan nilai itu. Alasannya: tulis

$$P(x) = (2x-1)Q(x) + r$$

dengan $r$ konstanta karena derajat pembaginya $1$. Masukkan $x = \frac12$; faktor
$(2x-1)$ lenyap, menyisakan $P\!\left(\frac12\right) = r$.

Hitung:

$$P\!\left(\tfrac12\right) = 8\left(\tfrac12\right)^3 + 4\left(\tfrac12\right) - 3
= 8 \cdot \tfrac18 + 2 - 3 = 1 + 2 - 3 = \boxed{0}$$

Sisanya nol, yang berarti $(2x-1)$ **merupakan faktor** dari $8x^3+4x-3$.

Periksa dengan membagi:

$$8x^3 + 4x - 3 = (2x-1)\left(4x^2 + 2x + 3\right)$$

Jabarkan untuk memastikan: $8x^3+4x^2+6x - 4x^2-2x-3 = 8x^3+4x-3$. Cocok.

**Kekeliruan yang sering terjadi** adalah memakai $P(1)$ atau $P(2)$ — membaca angka pada
pembagi alih-alih mencari akarnya. Aturannya selalu sama: **nolkan pembaginya, lalu
substitusikan nilai itu.**

Perhatikan pula bahwa sisanya tetap sama seandainya pembaginya ditulis
$\left(x - \frac12\right)$. Yang berubah hanya hasil baginya — ia menjadi dua kali lipat,
sebab $2x-1 = 2\left(x-\frac12\right)$.
