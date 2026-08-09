---
id: pcg-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: isian
kesulitan: 3
jawaban: "5120"
---

## Soal

Hitunglah

$$\sum_{k=0}^{10} k \binom{10}{k}
= 0\binom{10}{0} + 1\binom{10}{1} + 2\binom{10}{2} + \cdots + 10\binom{10}{10}$$

## Petunjuk

- Menghitung sebelas suku satu per satu bisa, tetapi ada bacaan pencacahan yang membuatnya selesai dalam satu baris.
- Bayangkan memilih sebuah tim dari $10$ orang, lalu menunjuk seorang ketua dari dalam tim itu. Berapa cara seluruhnya?
- Hitung hal yang sama dengan menunjuk ketuanya lebih dulu, baru memilih anggota lainnya.

## Pembahasan

**Nyatakan apa yang dicacah.** Tinjau himpunan

$$T = \{(\text{tim},\ \text{ketua}) : \text{tim} \subseteq \{1,\dots,10\},\ \text{ketua} \in \text{tim}\}$$

yaitu pasangan berupa sebuah tim beserta seorang ketua yang diambil dari dalam tim itu.
Timnya boleh berukuran berapa pun, asalkan tidak kosong — sebab tim kosong tidak punya
ketua.

**Cara A — pilih tim dulu, baru ketuanya.** Pecah menurut ukuran tim. Tim berukuran $k$ ada
$\binom{10}{k}$, dan tiap tim semacam itu punya $k$ pilihan ketua:

$$|T| = \sum_{k=0}^{10} k \binom{10}{k}$$

Suku $k = 0$ menyumbang nol, sesuai kenyataan bahwa tim kosong tidak menyumbang pasangan
apa pun.

**Cara B — pilih ketua dulu, baru anggota lainnya.** Tunjuk ketuanya lebih dulu: ada $10$
pilihan. Setelah itu, masing-masing dari $9$ orang sisanya bebas ikut atau tidak ikut ke
dalam tim:

$$|T| = 10 \times 2^{9}$$

**Samakan.**

$$\sum_{k=0}^{10} k\binom{10}{k} = 10 \times 2^{9} = 10 \times 512 = \boxed{5120}$$

**Periksa dengan menjumlahkan langsung.** Baris ke-$10$ segitiga Pascal adalah
$1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1$, sehingga

$$0 + 10 + 90 + 360 + 840 + 1260 + 1260 + 840 + 360 + 90 + 10 = 5120$$

Cocok.

**Bentuk umumnya:**

$$\sum_{k=0}^{n} k\binom{n}{k} = n\,2^{\,n-1}$$

**Yang membuat cara B berhasil** adalah pembalikan urutan keputusannya. Cara A memaksa
menjumlahkan atas seluruh ukuran tim, sebab pilihan ketua bergantung pada ukuran itu. Cara
B menunjuk ketua lebih dulu — dan begitu ketuanya tetap, sisa keputusannya menjadi seragam,
sehingga penjumlahannya lenyap.

Mencari urutan keputusan yang membuat penjumlahan lenyap adalah keterampilan inti pada
pencacahan ganda, dan ia terpakai jauh melampaui identitas ini.
