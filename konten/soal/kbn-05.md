---
id: kbn-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 4
jawaban: "638"
---

## Soal

Hitunglah

$$\binom{10}{0} + \binom{10}{1} + \binom{10}{2} + \binom{10}{3} + \binom{10}{4} + \binom{10}{5}$$

## Petunjuk

- Menjumlahkan keenam suku satu per satu bisa, tetapi ada jalan yang lebih rapi lewat sifat simetri koefisien binomial.
- Jumlah **seluruh** baris ke-$10$ sudah diketahui nilainya. Perhatikan bagaimana jumlah yang diminta berhubungan dengan separuh baris itu.
- Suku tengah $\binom{10}{5}$ adalah satu-satunya yang tidak punya pasangan, jadi ia harus diperlakukan sendiri.

## Pembahasan

**Berangkat dari jumlah seluruh baris.**

$$\sum_{k=0}^{10} \binom{10}{k} = 2^{10} = 1024$$

**Pakai simetri.** Karena $\binom{10}{k} = \binom{10}{10-k}$, suku-suku baris ini
berpasangan:

$$\binom{10}{0} \leftrightarrow \binom{10}{10}, \quad
\binom{10}{1} \leftrightarrow \binom{10}{9}, \quad \dots, \quad
\binom{10}{4} \leftrightarrow \binom{10}{6}$$

Yang **tidak** punya pasangan hanyalah suku tengah $\binom{10}{5}$, sebab ia berpasangan
dengan dirinya sendiri.

**Pisahkan suku tengahnya.**

$$\binom{10}{5} = \frac{10 \times 9 \times 8 \times 7 \times 6}{5 \times 4 \times 3 \times 2 \times 1} = 252$$

Sisa baris, yaitu $k = 0,\dots,4$ dan $k = 6,\dots,10$, berjumlah

$$1024 - 252 = 772$$

Kedua bagian itu sama besar menurut simetri, sehingga

$$\sum_{k=0}^{4} \binom{10}{k} = \frac{772}{2} = 386$$

**Rangkai.**

$$\sum_{k=0}^{5} \binom{10}{k} = 386 + 252 = \boxed{638}$$

**Periksa dengan menjumlahkan langsung.** Baris ke-$10$ segitiga Pascal:

$$1,\ 10,\ 45,\ 120,\ 210,\ 252,\ 210,\ 120,\ 45,\ 10,\ 1$$

$$1 + 10 + 45 + 120 + 210 + 252 = 638$$

Cocok.

**Bagian yang paling sering keliru** adalah membagi $1024$ dengan $2$ lalu berhenti,
sehingga jawabannya $512$. Itu berlaku kalau barisnya bisa dibelah rata — dan itu terjadi
hanya ketika $n$ **ganjil**, karena di situ tidak ada suku tengah. Untuk $n = 11$, misalnya,

$$\sum_{k=0}^{5} \binom{11}{k} = \frac{2^{11}}{2} = 1024$$

benar apa adanya. Untuk $n$ genap, suku tengahnya harus selalu diperlakukan tersendiri.

**Ganjil-genapnya $n$ menentukan bentuk jawabannya,** dan memeriksa hal itu lebih dulu
menghemat waktu sekaligus menghindari jebakan yang paling umum di soal jenis ini.
