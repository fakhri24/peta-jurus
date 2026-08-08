---
id: asb-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [akar-suku-banyak]
bentuk: isian
kesulitan: 2
jawaban: "14"
---

## Soal

Akar-akar persamaan $x^3 + 2x^2 - 5x - 6 = 0$ adalah $a$, $b$, $c$. Tentukan nilai

$$a^2 + b^2 + c^2$$

## Petunjuk

- Bentuk yang ditanya tidak berubah kalau ketiga akarnya ditukar-tukar. Bentuk semacam itu bisa dihitung dari koefisiennya saja.
- Kuadratkan $a+b+c$: hasilnya memuat jumlah kuadrat **dan** jumlah hasil kali berpasangan.
- $(a+b+c)^2 = a^2+b^2+c^2 + 2(ab+ac+bc)$.

## Pembahasan

Ambil dua besaran Vieta yang diperlukan. Di sini $a_3 = 1$, $a_2 = 2$, $a_1 = -5$:

$$a+b+c = -\frac{2}{1} = -2, \qquad ab+ac+bc = \frac{-5}{1} = -5$$

Tulis ulang bentuk yang ditanya. Dari penjabaran kuadrat jumlah tiga suku:

$$(a+b+c)^2 = a^2+b^2+c^2 + 2(ab+ac+bc)$$

sehingga

$$a^2+b^2+c^2 = (a+b+c)^2 - 2(ab+ac+bc)$$

Substitusikan:

$$a^2+b^2+c^2 = (-2)^2 - 2(-5) = 4 + 10 = \boxed{14}$$

Periksa: polinomialnya memfaktor menjadi $(x-2)(x+1)(x+3)$, jadi akarnya $2, -1, -3$. Dan

$$4 + 1 + 9 = 14$$

Cocok.

**Dua tanda yang menentukan di sini.** Pertama, $a+b+c = -2$ bernilai negatif — tetapi
kuadratnya positif, jadi tanda itu lenyap. Kedua, $ab+ac+bc = -5$ juga negatif, dan
mengurangkan dua kalinya berarti **menambah** $10$. Salah satu saja terlewat, jawabannya
meleset jauh.

Bentuk simetris lain yang bisa dihitung dari besaran yang sama:

$$\frac1a + \frac1b + \frac1c = \frac{ab+ac+bc}{abc} = \frac{-5}{6}$$

dengan $abc = -\frac{-6}{1} = 6$.
