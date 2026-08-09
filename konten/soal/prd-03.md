---
id: prd-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 2
jawaban: "7/8"
jawaban_alt: ["0,875", "0.875"]
---

## Soal

Tiga koin setimbang dilempar bersamaan.

Berapa peluang muncul **paling sedikit satu** sisi gambar? (Tulis sebagai pecahan paling
sederhana.)

## Petunjuk

- Menghitung "paling sedikit satu" secara langsung menuntut memecah kasus satu gambar, dua gambar, dan tiga gambar.
- Kebalikan dari "paling sedikit satu gambar" adalah "tidak ada gambar sama sekali", dan keadaan itu hanya terjadi dengan satu cara.
- Kurangkan peluang kebalikannya dari $1$.

## Pembahasan

**Ruang sampelnya.** Tiap koin punya $2$ hasil, dan ketiganya tidak saling memengaruhi:

$$|S| = 2^3 = 8$$

Kedelapan hasil itu sama mungkin: AAA, AAG, AGA, AGG, GAA, GAG, GGA, GGG, dengan A untuk
angka dan G untuk gambar.

**Kerjakan lewat kebalikannya.** Kejadian "paling sedikit satu gambar" berkebalikan dengan
"tidak ada gambar sama sekali", yaitu ketiganya angka. Keadaan itu terjadi lewat tepat satu
hasil, yaitu AAA:

$$P(\text{tidak ada gambar}) = \frac18$$

**Kurangkan dari satu.**

$$P(\text{paling sedikit satu gambar}) = 1 - \frac18 = \boxed{\frac78}$$

**Periksa dengan jalan langsung.** Pecah menurut banyaknya gambar:

| Banyak gambar | Cara | Banyaknya |
|---|---|---|
| $1$ | $\binom31$ | $3$ |
| $2$ | $\binom32$ | $3$ |
| $3$ | $\binom33$ | $1$ |

$$\frac{3+3+1}{8} = \frac78$$

Cocok — tetapi menuntut tiga hitungan alih-alih satu.

**"Paling sedikit satu" hampir selalu dikerjakan lewat komplemen,** dan alasannya terlihat
jelas di sini: kebalikannya adalah satu keadaan tunggal yang mudah dihitung, sedangkan
kejadian aslinya terpecah menjadi beberapa kasus.

Keunggulannya makin besar seiring bertambahnya percobaan. Untuk sepuluh koin, peluang
paling sedikit satu gambar adalah

$$1 - \frac{1}{2^{10}} = \frac{1023}{1024}$$

satu hitungan saja — sedangkan jalan langsung menuntut menjumlahkan sepuluh suku.

**Jangan tertukar dengan "tepat satu gambar",** yang jawabannya $\frac38$. Kata "paling
sedikit" dan "tepat" memberi soal yang sama sekali berbeda, dan keduanya sering muncul
berdampingan di naskah ujian.
