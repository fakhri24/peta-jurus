---
id: drg-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 3
jawaban: "44"
---

## Soal

Lima orang menitipkan topi mereka, lalu topi itu dikembalikan secara acak — satu topi untuk
tiap orang.

Ada berapa cara pengembalian sehingga **tidak seorang pun** menerima topinya sendiri?

## Petunjuk

- Hitung dulu seluruh pengembalian tanpa syarat, lalu buang yang melanggar.
- "Melanggar" berarti ada paling sedikit satu orang yang menerima topinya sendiri — dan kelompok-kelompok pelanggarnya saling beririsan.
- Sebut $A_i$ himpunan pengembalian yang membuat orang ke-$i$ menerima topinya sendiri, lalu hitung ukuran irisannya.

## Pembahasan

**Seluruh pengembalian.** Lima topi dibagikan ke lima orang, satu-satu:

$$5! = 120$$

**Susun kelompok pelanggarnya.** Sebut $A_i$ himpunan pengembalian yang membuat orang
ke-$i$ menerima topinya sendiri. Yang diminta adalah pengembalian yang tidak masuk satu pun
$A_i$:

$$D_5 = 5! - |A_1 \cup A_2 \cup \cdots \cup A_5|$$

**Hitung ukuran irisannya.** Kalau $k$ orang tertentu dipaksa menerima topinya sendiri,
sisanya $5-k$ topi bebas dibagikan:

$$\left|A_{i_1} \cap \cdots \cap A_{i_k}\right| = (5-k)!$$

Banyaknya cara memilih $k$ orang itu adalah $\binom5k$.

**Rangkai dengan inklusi–eksklusi.**

$$|A_1 \cup \cdots \cup A_5| = \sum_{k=1}^{5} (-1)^{k-1}\binom5k (5-k)!$$

$$= \binom51 4! - \binom52 3! + \binom53 2! - \binom54 1! + \binom55 0!$$

$$= 120 - 60 + 20 - 5 + 1 = 76$$

$$D_5 = 120 - 76 = \boxed{44}$$

**Bentuk umumnya.** Menyusun ulang perhitungan di atas memberi

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$

Periksa untuk $n = 5$:

$$120\left(1 - 1 + \tfrac12 - \tfrac16 + \tfrac1{24} - \tfrac1{120}\right)
= 120 \times \tfrac{44}{120} = 44$$

**Nilai yang layak dihafal:**

$$D_1 = 0, \quad D_2 = 1, \quad D_3 = 2, \quad D_4 = 9, \quad D_5 = 44, \quad D_6 = 265$$

Perhatikan $D_1 = 0$ — satu orang tidak punya topi lain untuk diterima. Menulisnya $1$
merusak seluruh rekursinya.

**Kekeliruan yang paling sering** adalah mengurangkan sekali saja: $120 - 5 \times 4! = 0$.
Itu keliru karena pengembalian yang membuat **dua** orang menerima topinya sendiri
terhitung dua kali di dalam $5 \times 4!$, sehingga terlalu banyak yang dibuang. Kelompok
pelanggarnya beririsan, dan justru itu yang menuntut inklusi–eksklusi.

**Kewajarannya.** Nisbah $\frac{44}{120} \approx 0{,}367$. Untuk $n$ besar, nisbah itu
mendekati $\frac1e \approx 0{,}368$ — dan sudah sangat dekat bahkan di $n = 5$.
