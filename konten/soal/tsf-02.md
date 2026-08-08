---
id: tsf-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [teorema-sisa-faktor]
bentuk: isian
kesulitan: 2
jawaban: "4"
---

## Soal

Tentukan nilai $k$ agar $(x - 2)$ merupakan faktor dari

$$x^3 - 3x^2 + kx - 4$$

## Petunjuk

- Syarat "merupakan faktor" bisa diterjemahkan menjadi syarat tentang nilai.
- $(x-a)$ faktor $P$ tepat ketika $P(a) = 0$.
- Hitung $P(2)$ — hasilnya akan memuat $k$ — lalu samakan dengan nol.

## Pembahasan

**Teorema faktor** menyatakan $(x-a)$ merupakan faktor $P$ tepat ketika $P(a) = 0$.

Alasannya langsung dari teorema sisa: sisa pembagian oleh $(x-a)$ adalah $P(a)$, dan
"merupakan faktor" berarti sisanya nol.

Di sini $a = 2$, jadi syaratnya $P(2) = 0$:

$$P(2) = 2^3 - 3(2)^2 + k(2) - 4 = 8 - 12 + 2k - 4 = 2k - 8$$

Samakan dengan nol:

$$2k - 8 = 0 \quad\Longrightarrow\quad k = \boxed{4}$$

Periksa: dengan $k = 4$ polinomialnya menjadi $x^3-3x^2+4x-4$, dan

$$P(2) = 8 - 12 + 8 - 4 = 0$$

Memang nol, jadi $(x-2)$ faktornya. Membaginya memberi

$$x^3-3x^2+4x-4 = (x-2)\left(x^2 - x + 2\right)$$

Perhatikan bahwa faktor keduanya tidak punya akar real — diskriminannya $1 - 8 = -7 < 0$.
Jadi $x = 2$ adalah satu-satunya akar real, meski derajatnya tiga.

**Pola soal ini sering muncul dengan pembungkus berbeda:** "tentukan $k$ agar habis
dibagi", "agar $x = 2$ akarnya", atau "agar sisanya nol". Ketiganya kalimat yang sama, dan
ketiganya diselesaikan dengan satu substitusi.
