---
id: probabilitas-diskret
nama: Probabilitas Diskret
pilar: kombinatorika
tahap: osn-k
prasyarat: [kombinasi]
contoh: [prd-contoh-1]
latihan: [prd-01, prd-02, prd-03, prd-04, prd-05, prd-06]
---

## Kapan dipakai

Ruang sampelnya berhingga dan tiap hasil dasar **sama mungkin**. Begitu kedua syarat itu
terpenuhi, soal peluang berubah jadi dua soal pencacahan: hitung yang diinginkan, hitung
seluruhnya.

Kalau hasilnya tidak sama mungkin — jumlah dua dadu, misalnya — turunkan dulu ke tingkat
yang sama mungkin, yaitu pasangan mata dadunya.

## Intinya

$$P(A) = \frac{|A|}{|S|}$$

dengan $S$ ruang sampel yang tiap anggotanya sama mungkin.

$$P(A^{c}) = 1 - P(A)$$

Bentuk komplemen ini sering jauh lebih pendek, terutama untuk "paling sedikit satu".

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Peluang bersyarat:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$

Dua kejadian **saling bebas** kalau $P(A \cap B) = P(A)P(B)$. Ini sesuatu yang harus
diperiksa atau dinyatakan soal, **bukan** dianggap begitu saja karena kedua kejadiannya
terasa tak berhubungan.

**Satu disiplin yang menyelamatkan banyak soal:** pembilang dan penyebut harus dihitung
dengan cara pandang yang sama. Kalau penyebutnya memperhatikan urutan pengambilan,
pembilangnya juga harus.

## Jebakan umum

- **Ruang sampel yang tidak sama mungkin.** Jumlah dua dadu punya 11 nilai, tapi ke-11
  nilai itu tidak sama peluangnya.
- **Mengalikan peluang untuk kejadian yang tidak bebas.** Pengambilan tanpa pengembalian
  mengubah peluang berikutnya.
- **Pembilang dan penyebut beda cara hitung.** Yang satu menganggap bola sewarna bisa
  dibedakan, yang lain tidak — hasilnya salah walau kedua hitungannya benar sendiri-sendiri.
