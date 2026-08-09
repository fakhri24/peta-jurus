---
id: sbr-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 2
jawaban: "66"
---

## Soal

Ada berapa penyelesaian bilangan bulat **tak negatif** dari persamaan

$$x_1 + x_2 + x_3 = 10\ ?$$

## Petunjuk

- Bayangkan $10$ benda yang seluruhnya sama akan dibagikan ke tiga wadah yang berbeda. Nilai $x_i$ menyatakan isi wadah ke-$i$.
- Gambarkan $10$ bintang berjajar, lalu sisipkan sekat untuk memisahkannya menjadi tiga kelompok. Berapa sekat yang dibutuhkan?
- Menentukan penyelesaian sama dengan menyusun bintang dan sekat itu berjajar.

## Pembahasan

**Terjemahkan menjadi gambar.** Bayangkan $10$ bintang berjajar dan $2$ sekat yang
membaginya menjadi $3$ kelompok. Misalnya

$$\star\star\star\,|\,\star\star\star\star\star\,|\,\star\star$$

melambangkan $x_1 = 3$, $x_2 = 5$, $x_3 = 2$.

Sekat di ujung atau dua sekat berdampingan melambangkan kelompok kosong, yang memang
diizinkan karena penyelesaiannya boleh bernilai $0$:

$$|\,\star\star\star\star\star\star\star\star\star\star\,| \quad\text{berarti}\quad
x_1 = 0,\ x_2 = 10,\ x_3 = 0$$

**Padanannya sempurna.** Tiap susunan bintang dan sekat memberi tepat satu penyelesaian, dan
tiap penyelesaian memberi tepat satu susunan. Jadi mencacah penyelesaian sama dengan
mencacah susunan.

**Cacah susunannya.** Seluruhnya ada

$$10 + 2 = 12 \text{ tempat}$$

dan sebuah susunan ditentukan sepenuhnya begitu diputuskan **tempat mana yang ditempati
sekat** — sisanya otomatis bintang:

$$\binom{12}{2} = \frac{12 \times 11}{2} = \boxed{66}$$

**Mengapa sekatnya $2$ dan bukan $3$.** Untuk membagi satu barisan menjadi $3$ kelompok
dibutuhkan $3-1 = 2$ pemisah. Memakai $3$ sekat akan menghasilkan $4$ kelompok. Kekeliruan
ini yang paling sering, dan akibatnya jawaban meleset jauh.

**Rumus umumnya** untuk $x_1 + \cdots + x_k = n$ dengan $x_i \ge 0$:

$$\binom{n+k-1}{k-1}$$

**Periksa pada kasus yang bisa didaftar.** Untuk $x_1 + x_2 = 3$ dengan $x_i \ge 0$,
rumusnya memberi $\binom{4}{1} = 4$. Daftarnya memang $(0,3), (1,2), (2,1), (3,0)$ —
tepat $4$.

**Perhatikan objeknya identik, wadahnya berbeda.** Kalau kesepuluh benda justru **berbeda**
dan wadahnya juga berbeda, jawabannya $3^{10}$ — tiap benda memilih wadahnya sendiri. Dua
soal yang bunyinya mirip, jawabannya jauh berbeda.
