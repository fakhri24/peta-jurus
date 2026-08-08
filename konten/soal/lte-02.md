---
id: lte-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Tentukan pangkat tertinggi $7$ yang membagi $8^{49} - 1$.

## Petunjuk

- Kenali bentuknya sebagai $a^n - b^n$ dengan $b = 1$, lalu periksa syarat $p \mid a - b$.
- $a - b = 7$, jadi syaratnya terpenuhi untuk $p = 7$.
- $49 = 7^2$, jadi suku $v_7(n)$ bukan nol — di situlah sebagian besar pangkatnya berasal.

## Pembahasan

Tulis $8^{49} - 1 = 8^{49} - 1^{49}$, jadi $a = 8$, $b = 1$, $n = 49$.

**Periksa syaratnya.** Prima $p = 7$ ganjil, $a - b = 7$ sehingga $7 \mid a - b$, dan $7$
tidak membagi $8$ maupun $1$. Terpenuhi.

**Terapkan rumusnya.**

$$v_7\left(8^{49} - 1\right) = v_7(8-1) + v_7(49) = v_7(7) + v_7\left(7^2\right)
= 1 + 2 = \boxed{3}$$

Jadi $343$ membagi $8^{49} - 1$, sedangkan $7^4 = 2401$ tidak.

Perhatikan peran eksponennya. Kalau $n$ diganti $48$ — yang tidak memuat faktor $7$ sama
sekali — maka $v_7(48) = 0$ dan jawabannya turun menjadi $1$. Jadi seluruh tambahan
pangkat di sini datang dari $49 = 7^2$, bukan dari besarnya eksponen.

Bentuk $8^{49} - 1$ juga bisa dibaca sebagai $2^{147} - 1$. Menuliskannya begitu justru
menyembunyikan strukturnya: syarat $p \mid a - b$ gagal untuk $a = 2$, $b = 1$, sebab
$7 \nmid 1$. Memilih penulisan yang tepat adalah bagian dari jurus ini.
