---
id: teorema-sisa-cina
nama: Teorema Sisa Cina
pilar: teori-bilangan
tahap: osn-p
prasyarat: [kongruensi-linear]
contoh: []
latihan: []
---

## Kapan dipakai

Ada **beberapa syarat sisa sekaligus**: "bersisa 2 kalau dibagi 3, bersisa 3 kalau dibagi
5, bersisa 2 kalau dibagi 7". Atau — pemakaian yang lebih dalam — kamu ingin memecah satu
soal modulo besar menjadi beberapa soal modulo pangkat prima yang lebih mudah.

## Intinya

Kalau $m_1, m_2, \dots, m_k$ saling relatif prima berpasangan, maka sistem

$$x \equiv a_1 \pmod{m_1}, \quad \dots, \quad x \equiv a_k \pmod{m_k}$$

punya solusi **tunggal** modulo $M = m_1 m_2 \cdots m_k$.

Cara membacanya yang lebih berguna: bekerja modulo $M$ itu **sama saja** dengan bekerja
modulo tiap $m_i$ secara terpisah. Jadi soal modulo $1000$ boleh dipecah jadi modulo $8$
dan modulo $125$ — dua soal kecil menggantikan satu soal besar.

Untuk sistem kecil, tidak perlu rumus. Ambil kongruensi dengan modulus terbesar, tulis
$x = a_k + m_k t$, substitusikan ke kongruensi berikutnya, selesaikan $t$, ulangi.

## Jebakan umum

- **Modulusnya tidak relatif prima.** Teoremanya batal. Sistem seperti $x \equiv 1
  \pmod 4$ dan $x \equiv 2 \pmod 6$ harus diperiksa kecocokannya dengan tangan — kadang
  ada solusi, kadang tidak sama sekali.
- **Menjawab satu bilangan, padahal jawabannya satu kelas.** Solusinya adalah $x \equiv r
  \pmod M$ — bilangan yang memenuhi ada tak hingga banyaknya.
- **Salah menghitung $M$.** Modulus gabungannya hasil kali, bukan jumlah atau KPK dari
  sesuatu yang lain.
