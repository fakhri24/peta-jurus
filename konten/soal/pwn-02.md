---
id: pwn-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: isian
kesulitan: 3
jawaban: "13"
---

## Soal

Sebuah papan $5 \times 5$ diwarnai berselang-seling seperti papan catur, dengan keempat
petak sudutnya **berwarna hitam**.

Ada berapa petak hitam pada papan itu?

## Petunjuk

- Papan berukuran ganjil tidak terbagi rata antara kedua warna. Jangan langsung membagi dua.
- Warnai menurut paritas $i+j$, lalu hitung berapa pasangan $(i,j)$ yang jumlahnya genap.
- Boleh juga dihitung baris demi baris: baris ganjil dan baris genap punya banyak petak hitam yang berbeda.

## Pembahasan

**Papan berukuran ganjil tidak terbagi rata.** Kesalahan yang wajar adalah menjawab
$\frac{25}{2}$, yang bahkan bukan bilangan bulat. Untuk papan bersisi ganjil, satu warna
selalu lebih banyak — yaitu warna yang menempati sudut-sudutnya.

**Hitung baris demi baris.** Beri koordinat $(i,j)$ dengan $1 \le i,j \le 5$, dan warnai
hitam ketika $i+j$ genap. Petak $(1,1)$ punya $i+j = 2$, genap — sesuai soal, sudutnya
hitam.

| Baris $i$ | petak hitam | banyaknya |
|---|---|---|
| $1$ | $j = 1,3,5$ | $3$ |
| $2$ | $j = 2,4$ | $2$ |
| $3$ | $j = 1,3,5$ | $3$ |
| $4$ | $j = 2,4$ | $2$ |
| $5$ | $j = 1,3,5$ | $3$ |

$$3 + 2 + 3 + 2 + 3 = \boxed{13}$$

Petak putihnya $25 - 13 = 12$.

**Rumus umumnya** untuk papan $n \times n$ dengan $n$ ganjil dan sudut hitam:

$$\text{hitam} = \frac{n^2+1}{2}, \qquad \text{putih} = \frac{n^2-1}{2}$$

Periksa untuk $n = 5$: $\frac{26}{2} = 13$ dan $\frac{24}{2} = 12$. Cocok.

**Akibat langsungnya.** Papan $5\times5$ **tidak dapat** ditutup seluruhnya oleh domino,
sebab $25$ ganjil sehingga jumlahnya saja sudah tidak cocok. Yang lebih menarik: paling
banyak $12$ domino yang bisa diletakkan, dan sisa satu petak yang tidak tertutup pasti
berwarna **hitam** — sebab $12$ domino menutup $12$ petak tiap warna, sehingga yang tersisa
adalah kelebihan warna hitam.

Kesimpulan itu tidak bisa diperoleh dari hitungan petak saja. Ia menunjukkan pewarnaan tidak
hanya menutup kemungkinan, tetapi juga **memberi keterangan** tentang penutupan yang memang
bisa dilakukan.

**Ketimpangan warna adalah alat yang berulang kali dipakai** pada soal papan bersisi ganjil,
dan langkah pertamanya selalu sama: tentukan warna sudutnya, sebab itu yang menentukan warna
mana yang berlebih.
