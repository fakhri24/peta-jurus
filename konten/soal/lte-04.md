---
id: lte-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 3
jawaban: "4"
---

## Soal

Tentukan pangkat tertinggi $2$ yang membagi $3^{100} - 1$.

## Petunjuk

- Primanya $2$, jadi rumus untuk prima ganjil **tidak** berlaku. Kasus ini punya rumus sendiri.
- Untuk $n$ genap: $v_2(a^n - b^n) = v_2(a-b) + v_2(a+b) + v_2(n) - 1$.
- Di sini $a = 3$, $b = 1$, $n = 100$. Hitung ketiga sukunya, lalu jangan lupa dikurangi $1$.

## Pembahasan

Tulis $3^{100} - 1 = 3^{100} - 1^{100}$, jadi $a = 3$, $b = 1$, $n = 100$.

**Pilih rumus yang benar.** Primanya $2$, sehingga rumus untuk prima ganjil tidak berlaku.
Karena $n = 100$ genap, yang dipakai

$$v_2\left(a^n - b^n\right) = v_2(a - b) + v_2(a + b) + v_2(n) - 1$$

**Hitung ketiga sukunya.**

$$v_2(a - b) = v_2(2) = 1$$
$$v_2(a + b) = v_2(4) = 2$$
$$v_2(n) = v_2(100) = v_2\left(2^2 \times 25\right) = 2$$

Maka

$$v_2\left(3^{100} - 1\right) = 1 + 2 + 2 - 1 = \boxed{4}$$

Jadi $16$ membagi $3^{100} - 1$, sedangkan $32$ tidak.

Ini kesalahan paling sering pada jurus ini: memakai rumus prima ganjil untuk $p = 2$. Kalau
dipaksakan, hasilnya $v_2(2) + v_2(100) = 1 + 2 = 3$ — meleset satu, dan tidak ada yang
menandai bahwa itu salah.

Periksa dengan tangan pada kasus kecil: $3^2 - 1 = 8$ memberi $v_2 = 3$, sedangkan rumus
genap memberi $1 + 2 + 1 - 1 = 3$ $\checkmark$, dan rumus ganjil akan memberi $1 + 1 = 2$
$\times$.

Untuk $n$ ganjil, kasus $p = 2$ jauh lebih sederhana: $v_2(a^n - b^n) = v_2(a-b)$ saja.
