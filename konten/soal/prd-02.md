---
id: prd-02
sumber: Latihan 2 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 2
jawaban: "5/14"
jawaban_alt: ["10/28"]
---

## Soal

Sebuah kotak berisi $5$ bola merah dan $3$ bola putih. Dua bola diambil **sekaligus** secara
acak.

Berapa peluang kedua bola yang terambil berwarna merah? (Tulis sebagai pecahan paling
sederhana.)

## Petunjuk

- Kata "sekaligus" menentukan cara menghitungnya: yang dicacah adalah kumpulan dua bola, bukan urutan pengambilan.
- Hitung banyaknya cara mengambil dua bola dari seluruh isi kotak, lalu banyaknya cara mengambil dua bola merah.
- Pastikan pembilang dan penyebut dihitung dengan cara pandang yang sama — keduanya tanpa memperhatikan urutan.

## Pembahasan

**Ruang sampelnya.** Kotak berisi $5 + 3 = 8$ bola. Mengambil dua bola sekaligus berarti
memilih kumpulan dua bola, tanpa urutan:

$$|S| = \binom{8}{2} = \frac{8 \times 7}{2} = 28$$

**Hasil yang diinginkan.** Kedua bola merah, artinya dua bola dipilih dari $5$ bola merah:

$$|A| = \binom{5}{2} = \frac{5 \times 4}{2} = 10$$

**Hitung.**

$$P(A) = \frac{10}{28} = \boxed{\frac{5}{14}}$$

**Cara kedua — anggap diambil berurutan.** Hasilnya harus sama, dan memeriksanya berguna:

$$P = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

Bola pertama merah dengan peluang $\frac58$; setelah satu bola merah keluar, tersisa $4$
merah dari $7$ bola, sehingga bola kedua merah dengan peluang $\frac47$.

**Kedua cara sah asalkan dipakai sampai selesai.** Yang salah adalah mencampurnya —
misalnya menghitung penyebut dengan memperhatikan urutan ($8 \times 7 = 56$) tetapi
pembilang tanpa urutan ($\binom52 = 10$), yang memberi $\frac{10}{56}$ dan keliru.

**Perhatikan pecahan kedua pada cara berurutan: $\frac47$, bukan $\frac58$.** Pengambilan
di sini **tanpa pengembalian**, sehingga kejadian kedua bergantung pada yang pertama.
Mengalikan $\frac58 \times \frac58$ berarti menganggap keduanya bebas — yang hanya benar
kalau bolanya dikembalikan sebelum pengambilan kedua.

**Untuk pembanding,** kalau bolanya dikembalikan, jawabannya
$\frac58 \times \frac58 = \frac{25}{64}$. Angkanya lebih besar, dan itu masuk akal: dengan
pengembalian, bola merah tidak pernah berkurang.
