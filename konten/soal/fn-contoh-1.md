---
id: fn-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [fungsi]
bentuk: isian
kesulitan: 2
jawaban: "11"
---

## Soal

Diketahui $f(x) = 2x + 3$ dan $g(x) = x^2$. Tentukan nilai $(f \circ g)(2)$.

## Petunjuk

- Lambang $\circ$ menyatakan komposisi. Yang menentukan adalah urutan pengerjaannya.
- $(f \circ g)(x) = f\left(g(x)\right)$ — dikerjakan **dari dalam ke luar**, jadi $g$ dulu.
- Hitung $g(2)$ lebih dulu, lalu masukkan hasilnya ke $f$.

## Pembahasan

Menurut definisi komposisi,

$$(f \circ g)(x) = f\left(g(x)\right)$$

Urutannya dibaca dari **dalam ke luar**: fungsi yang tertulis di kanan dikerjakan lebih
dulu.

**Langkah pertama.**

$$g(2) = 2^2 = 4$$

**Langkah kedua.** Masukkan hasilnya ke $f$:

$$f(4) = 2(4) + 3 = \boxed{11}$$

**Bandingkan dengan urutan sebaliknya.**

$$(g \circ f)(2) = g\left(f(2)\right) = g(7) = 49$$

Hasilnya sama sekali berbeda. **Komposisi tidak bersifat komutatif** — $f \circ g$ dan
$g \circ f$ umumnya bukan fungsi yang sama, dan menukar urutannya adalah kekeliruan yang
paling sering terjadi pada jurus ini.

Kalau ingin rumus umumnya, substitusikan saja:

$$(f \circ g)(x) = f\left(x^2\right) = 2x^2 + 3$$

Memasukkan $x = 2$ memberi $2(4) + 3 = 11$ — cocok. Untuk satu titik saja, menghitung
bertahap lebih cepat; untuk beberapa titik, mencari rumusnya lebih hemat.
