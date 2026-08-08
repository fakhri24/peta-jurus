---
id: tel-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: aljabar
tahap: osn-p
jurus: [deret-teleskopik]
bentuk: isian
kesulitan: 2
jawaban: "99"
---

## Soal

Tentukan bilangan asli $n$ yang memenuhi

$$\frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \cdots + \frac{1}{n(n+1)} = \frac{99}{100}$$

## Petunjuk

- Cari dulu bentuk umum jumlahnya sebagai fungsi dari $n$, baru samakan dengan yang diketahui.
- Setelah diteleskopkan, jumlahnya $1 - \frac{1}{n+1}$.
- Sederhanakan menjadi $\frac{n}{n+1}$, lalu samakan dengan $\frac{99}{100}$.

## Pembahasan

Pecah tiap suku menjadi selisih:

$$\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$$

Bagian tengahnya saling menghapus, menyisakan dua ujung:

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n+1-1}{n+1} = \frac{n}{n+1}$$

Samakan dengan yang diketahui:

$$\frac{n}{n+1} = \frac{99}{100}$$

Kalikan silang:

$$100n = 99(n+1) = 99n + 99 \quad\Longrightarrow\quad n = \boxed{99}$$

Periksa: $\frac{99}{99+1} = \frac{99}{100}$. Cocok.

Ada jalan yang lebih cepat lagi. Bentuk $\frac{n}{n+1}$ selalu berupa pecahan yang
pembilangnya tepat satu kurang dari penyebutnya — dan $\frac{99}{100}$ memang begitu, jadi
$n = 99$ terbaca langsung tanpa mengalikan silang.

Perhatikan pula apa yang dikatakan bentuk umum itu. Karena $\frac{n}{n+1} = 1 -
\frac{1}{n+1}$, jumlahnya selalu **kurang dari $1$** berapa pun $n$-nya, tetapi bisa
sedekat apa pun ke $1$. Untuk $n$ yang membesar tanpa batas, jumlahnya menuju $1$ — dan
itulah nilai deret tak hingganya.
