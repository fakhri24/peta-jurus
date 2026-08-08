---
id: lte-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: teori-bilangan
tahap: osn
jurus: [lte]
bentuk: isian
kesulitan: 2
jawaban: "6"
---

## Soal

Tentukan pangkat tertinggi $3$ yang membagi $10^{81} - 1$.

## Petunjuk

- Bentuknya selisih pangkat, dan yang ditanya pangkat prima yang membaginya. Periksa dulu apakah syarat rumusnya terpenuhi.
- Tulis $10^{81} - 1 = 10^{81} - 1^{81}$, jadi $a = 10$ dan $b = 1$. Syaratnya: $3 \mid a - b$, serta $3 \nmid a$ dan $3 \nmid b$.
- Rumusnya $v_3(a^n - b^n) = v_3(a-b) + v_3(n)$. Hitung kedua sukunya.

## Pembahasan

Tulis bentuknya sebagai selisih pangkat dengan basis yang jelas:

$$10^{81} - 1 = 10^{81} - 1^{81}$$

sehingga $a = 10$, $b = 1$, dan $n = 81$.

**Periksa syaratnya.** Prima $p = 3$ ganjil. Lalu

$$a - b = 9, \qquad 3 \mid 9 \quad\checkmark$$

dan $3 \nmid 10$ serta $3 \nmid 1$ — keduanya terpenuhi. Rumus LTE boleh dipakai:

$$v_3\left(a^n - b^n\right) = v_3(a - b) + v_3(n)$$

**Hitung kedua sukunya.**

$$v_3(a - b) = v_3(9) = 2, \qquad v_3(n) = v_3(81) = v_3\left(3^4\right) = 4$$

Maka

$$v_3\left(10^{81} - 1\right) = 2 + 4 = \boxed{6}$$

Artinya $3^6 = 729$ membagi $10^{81} - 1$, sedangkan $3^7$ tidak.

Bilangan $10^{81} - 1$ adalah bilangan yang seluruh $81$ digitnya $9$. Hasil di atas bisa
diperiksa sebagian dengan aturan digit: jumlah digitnya $81 \times 9 = 729 = 3^6$, yang
memang habis dibagi $9$ — meski aturan digit saja tidak cukup untuk memberi pangkat
penuhnya.

Perhatikan pemeriksaan syarat di awal. Tanpa $3 \mid a - b$, rumusnya tetap memberi angka
— dan angka itu salah. Itu jebakan utama jurus ini.
