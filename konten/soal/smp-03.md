---
id: smp-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 2
jawaban: "3"
---

## Soal

Sebanyak $30$ siswa mengikuti ujian. Nilai yang mungkin adalah bilangan bulat dari $0$
sampai $10$.

Berapa banyak siswa yang **pasti** memperoleh nilai yang sama? Dengan kata lain, tentukan
bilangan $m$ terbesar sehingga dapat dipastikan ada $m$ siswa bernilai sama.

## Petunjuk

- Hitung dulu ada berapa nilai yang mungkin. Perhatikan bahwa $0$ ikut terhitung.
- Kalau $30$ siswa dibagi merata ke seluruh nilai yang mungkin, berapa banyak yang menempati nilai terpadat?
- Jawabannya adalah pembulatan ke atas dari hasil bagi itu.

## Pembahasan

**Hitung sarangnya dengan hati-hati.** Nilai yang mungkin adalah $0, 1, 2, \dots, 10$.
Banyaknya

$$k = 10 - 0 + 1 = 11$$

bukan $10$. Melupakan nilai $0$ adalah kekeliruan yang paling sering di soal semacam ini.

**Terapkan bentuk umum prinsipnya.** Dengan $n$ merpati dan $k$ sarang, ada sarang yang
berisi paling sedikit

$$\left\lceil \frac{n}{k} \right\rceil = \left\lceil \frac{30}{11} \right\rceil
= \left\lceil 2{,}72\ldots \right\rceil = \boxed{3}$$

**Mengapa $3$ dan bukan lebih.** Prinsipnya menjamin paling sedikit $3$, tetapi soal
menanyakan angka **terbesar** yang bisa dipastikan. Jadi harus ditunjukkan bahwa $4$ tidak
bisa dipastikan — yaitu ada pembagian nilai yang tidak pernah membuat empat siswa bernilai
sama.

Sebarkan $30$ siswa ke $11$ nilai dengan paling banyak $3$ siswa per nilai: misalnya $8$
nilai diisi $3$ siswa dan $3$ nilai diisi $2$ siswa.

$$8 \times 3 + 3 \times 2 = 24 + 6 = 30$$

Pembagian ini sah, dan di dalamnya tidak ada nilai yang ditempati $4$ siswa. Jadi $4$ tidak
bisa dipastikan, dan jawabannya tepat $3$.

**Dua bagian itu selalu diperlukan** pada soal "paling sedikit/terbesar yang pasti":
prinsip sarang merpati memberi batasnya, dan sebuah contoh menunjukkan batas itu tidak bisa
dinaikkan lagi.

**Mengapa pembulatannya ke atas.** Kalau semua sarang berisi paling banyak
$\lceil n/k \rceil - 1$, seluruh merpati paling banyak $k\left(\lceil n/k\rceil - 1\right)$,
yang lebih kecil dari $n$. Di sini $11 \times 2 = 22 < 30$ — jadi mustahil semua nilai
ditempati paling banyak dua siswa.
