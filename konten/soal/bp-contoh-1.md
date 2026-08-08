---
id: bp-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: teori-bilangan
tahap: osn-k
jurus: [bilangan-prima]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Ada berapa bilangan prima $p$ sehingga $p$, $p+2$, dan $p+4$ ketiganya prima?

## Petunjuk

- Coba dulu beberapa nilai kecil. Yang mana yang berhasil?
- $p = 3$ memberi $3, 5, 7$ — semuanya prima. Sekarang buktikan tidak ada yang lain.
- Lihat ketiganya modulo $3$. Di antara $p$, $p+2$, $p+4$, ada berapa yang mungkin habis dibagi $3$?

## Pembahasan

Coba nilai kecil: $p = 3$ memberi $3, 5, 7$ — ketiganya prima. Jadi setidaknya ada satu.

Sekarang tunjukkan tidak ada yang lain. Perhatikan ketiga bilangan itu modulo $3$. Karena
$p + 4 \equiv p + 1 \pmod 3$, ketiganya berturut-turut kongruen dengan

$$p, \quad p+2, \quad p+1 \pmod 3$$

Itu adalah **ketiga sisa yang berbeda** modulo $3$. Jadi salah satunya pasti habis dibagi
$3$ — apa pun nilai $p$.

Sebuah bilangan yang habis dibagi $3$ hanya bisa prima kalau ia sama dengan $3$ sendiri.
Karena $p + 2$ dan $p + 4$ lebih besar dari $3$ (untuk $p$ prima mana pun), yang boleh
bernilai $3$ hanyalah $p$.

Jadi $p = 3$ satu-satunya, dan jawabannya $\boxed{1}$.

Pola ini pantas dihafal: **di antara $n$ bilangan yang selisihnya teratur, sering ada satu
yang dipaksa habis dibagi $n$.** Ia menutup banyak sekali soal "tiga prima berurutan".
