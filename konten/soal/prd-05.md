---
id: prd-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 3
jawaban: "37/42"
jawaban_alt: ["74/84"]
---

## Soal

Dari $5$ pria dan $4$ wanita akan dipilih $3$ orang secara acak.

Berapa peluang terpilih **paling sedikit seorang wanita**? (Tulis sebagai pecahan paling
sederhana.)

## Petunjuk

- "Paling sedikit seorang" menandakan hitungan lewat kebalikannya.
- Kebalikannya adalah "tidak ada wanita sama sekali", yaitu ketiganya pria.
- Hitung peluang kebalikannya lebih dulu, lalu kurangkan dari $1$.

## Pembahasan

**Ruang sampelnya.** Memilih $3$ orang dari $5+4 = 9$ orang, tanpa urutan:

$$|S| = \binom93 = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$$

**Hitung kebalikannya.** "Tidak ada wanita" berarti ketiganya pria, dipilih dari $5$ pria:

$$\binom53 = 10$$

$$P(\text{tidak ada wanita}) = \frac{10}{84} = \frac{5}{42}$$

**Kurangkan dari satu.**

$$P(\text{paling sedikit satu wanita}) = 1 - \frac{5}{42} = \boxed{\frac{37}{42}}$$

**Periksa dengan jalan langsung.** Pecah menurut banyaknya wanita $w$:

| $w$ | wanita | pria | hasil |
|---|---|---|---|
| $1$ | $\binom41 = 4$ | $\binom52 = 10$ | $40$ |
| $2$ | $\binom42 = 6$ | $\binom51 = 5$ | $30$ |
| $3$ | $\binom43 = 4$ | $\binom50 = 1$ | $4$ |

$$\frac{40+30+4}{84} = \frac{74}{84} = \frac{37}{42}$$

Cocok — tiga hitungan berpasangan, dibanding satu hitungan tunggal lewat komplemen.

**Menyederhanakan pecahannya.** $\frac{74}{84}$ dibagi $2$ memberi $\frac{37}{42}$, dan
$37$ bilangan prima sehingga tidak bisa disederhanakan lagi. Memeriksa apakah pecahan sudah
paling sederhana adalah bagian dari menjawab, terutama kalau soal memintanya.

**Kewajarannya.** Nilainya $\frac{37}{42} \approx 0{,}88$ — cukup besar, dan memang masuk
akal: hampir separuh kelompoknya wanita, jadi terpilihnya tiga pria sekaligus adalah
keadaan yang jarang.

**Kebiasaan yang layak dibawa:** setiap kali melihat "paling sedikit", tuliskan dulu apa
kebalikannya sebelum menghitung apa pun. Kalau kebalikannya satu keadaan tunggal,
komplemen hampir pasti jalan tercepat.
