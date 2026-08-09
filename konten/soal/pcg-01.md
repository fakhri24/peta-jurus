---
id: pcg-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: isian
kesulitan: 2
jawaban: "15"
---

## Soal

Dalam sebuah pertemuan yang dihadiri $10$ orang, setiap orang berjabat tangan dengan tepat
$3$ orang lainnya.

Ada berapa jabat tangan yang terjadi?

## Petunjuk

- Jangan mencoba mendaftar siapa berjabat tangan dengan siapa. Hitung sesuatu yang lebih mudah lebih dulu.
- Jumlahkan, untuk tiap orang, banyaknya jabat tangan yang ia ikuti. Apa yang sebenarnya dihitung angka itu?
- Tiap jabat tangan melibatkan dua orang, jadi ia terhitung dua kali di dalam jumlah tadi.

## Pembahasan

**Hitung dari sisi orang.** Tiap orang mengikuti $3$ jabat tangan, dan ada $10$ orang:

$$10 \times 3 = 30$$

**Baca angka itu dengan benar.** Angka $30$ **bukan** banyaknya jabat tangan. Ia menghitung
pasangan (orang, jabat tangan yang ia ikuti) — dan tiap jabat tangan menyumbang **dua**
pasangan semacam itu, sekali untuk masing-masing pihak.

**Hitung dari sisi jabat tangan.** Kalau banyaknya jabat tangan adalah $J$, maka banyaknya
pasangan itu juga $2J$. Kedua hitungan mencacah himpunan yang sama:

$$2J = 30 \quad\Longrightarrow\quad J = \boxed{15}$$

**Kekeliruan yang paling sering** adalah menjawab $30$. Ia muncul dari menghitung dengan
benar tetapi salah membaca apa yang dihitung — dan itulah sebabnya kebiasaan menyebutkan
**apa yang sedang dicacah** sebelum menjumlahkan begitu berharga.

**Periksa kewajarannya.** Kalau semua orang berjabat tangan dengan semua orang, jabat
tangannya $\binom{10}{2} = 45$, yaitu tiap orang mengikuti $9$ jabat tangan. Di sini tiap
orang hanya mengikuti $3$, yaitu sepertiganya, sehingga $45 \times \frac13 = 15$. Cocok.

**Periksa juga apakah keadaannya mungkin.** Jumlah derajat $30$ genap, sehingga tidak ada
yang bertentangan. Kalau soalnya menyebut $5$ orang yang masing-masing berjabat tangan
dengan tepat $3$ orang, jumlahnya $15$ — ganjil, sehingga $J = 7{,}5$ dan keadaan itu
**mustahil**. Memeriksa hal ini sebelum menjawab mencegah menuliskan bilangan pecahan pada
soal yang jawabannya wajib bulat.
