---
id: lte
nama: Lifting the Exponent
pilar: teori-bilangan
tahap: osn
prasyarat: [legendre-faktorial, orde-elemen]
contoh: []
latihan: []
---

## Kapan dipakai

Soal menanyakan **pangkat tertinggi sebuah prima** yang membagi $a^n \pm b^n$. Ciri
khasnya: ada selisih atau jumlah pangkat, dan yang ditanya keterbagian oleh pangkat prima.

## Intinya

Tulis $v_p(x)$ untuk pangkat $p$ dalam $x$. Kalau $p$ prima ganjil, $p \mid a - b$, dan
$p \nmid a$, $p \nmid b$:

$$v_p(a^n - b^n) = v_p(a - b) + v_p(n)$$

Kalau $n$ ganjil, $p \mid a + b$, dan $p$ tidak membagi $a$ maupun $b$:

$$v_p(a^n + b^n) = v_p(a + b) + v_p(n)$$

Untuk $p = 2$ rumusnya berbeda dan harus diingat terpisah. Untuk $n$ genap:

$$v_2(a^n - b^n) = v_2(a-b) + v_2(a+b) + v_2(n) - 1$$

Nilai jurus ini: soal yang tampak menuntut perhitungan raksasa selesai dalam dua baris.

## Jebakan umum

- **Melupakan syaratnya.** $p \mid a - b$ itu wajib. Tanpa itu rumusnya memberi angka yang
  salah — dan tetap terlihat masuk akal.
- **Memakai rumus $p$ ganjil untuk $p = 2$.** Kasus $2$ punya rumus sendiri. Ini kesalahan
  paling sering pada jurus ini.
- **Memakai bentuk $a^n + b^n$ untuk $n$ genap.** Bentuk itu hanya berlaku untuk $n$ ganjil.
