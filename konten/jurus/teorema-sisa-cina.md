---
id: teorema-sisa-cina
nama: Teorema Sisa Cina
pilar: teori-bilangan
tahap: osn-p
prasyarat: [kongruensi-linear]
contoh: [tsc-contoh-1]
latihan: [tsc-01, tsc-02, tsc-03, tsc-04, tsc-05, tsc-06]
---

## Kapan dipakai

Soal memberikan **beberapa syarat sisa pembagian sekaligus** untuk satu bilangan $x$, terhadap beberapa modulus yang saling relatif prima berpasangan — seperti $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$, dan $x \equiv 2 \pmod 7$.

Pemicu kedua, dan inilah fungsi teoretik terpentingnya: **memecah masalah modulo komposit besar** $M = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ menjadi beberapa sub-masalah independen modulo $p_i^{a_i}$ yang jauh lebih mudah dikerjakan.

Pemicu ketiga: membuktikan keberadaan **rentang bilangan komposit yang panjangnya sembarang** — misalnya membuktikan ada 1000 bilangan bulat berurutan yang masing-masing punya faktor prima unik.

Pemicu keempat: soal menanyakan sisa pembagian modulo bilangan komposit seperti $100$ atau $1000$, di mana kita bisa menghitung modulo $4$ dan $25$ (atau modulo $8$ dan $125$) secara terpisah lalu menggabungkannya.

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
