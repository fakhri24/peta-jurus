---
id: barisan-deret
nama: Barisan dan Deret
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: []
latihan: []
---

## Kapan dipakai

Ada pola yang berulang dengan selisih tetap atau rasio tetap — bilangan tersusun, jumlah
berurutan, bunga berlipat, atau soal cerita yang menyebut "bertambah sekian setiap".

## Intinya

**Aritmetika**, beda $b$:

$$U_n = a + (n-1)b, \qquad S_n = \frac{n}{2}\left(2a + (n-1)b\right) = \frac{n}{2}(U_1 + U_n)$$

**Geometri**, rasio $r$:

$$U_n = a r^{n-1}, \qquad S_n = \frac{a\left(r^n - 1\right)}{r - 1} \quad (r \ne 1)$$

Untuk $|r| < 1$, deret tak hingganya menuju

$$S_\infty = \frac{a}{1-r}$$

Bentuk $S_n = \frac{n}{2}(U_1 + U_n)$ layak diingat terpisah: ia membaca deret aritmetika
sebagai "banyaknya suku dikali rata-rata ujung", dan itu sering lebih cepat daripada
memasukkan $a$ dan $b$.

Dua jumlah yang muncul terus-menerus:

$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}, \qquad
1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

## Jebakan umum

- **Salah menghitung banyak suku.** Dari $7$ sampai $31$ dengan beda $3$ ada
  $\frac{31-7}{3} + 1 = 9$ suku, bukan $8$. Tambahan $1$ itu hampir selalu terlupa.
- **Memakai $S_\infty$ tanpa memeriksa $|r| < 1$.** Di luar itu deretnya tidak menuju
  bilangan mana pun.
- **Mengira $U_n = a + nb$.** Sukunya dimulai dari $U_1 = a$, jadi yang benar $(n-1)b$.
