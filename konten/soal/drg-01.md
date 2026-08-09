---
id: drg-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [derangement]
bentuk: isian
kesulitan: 2
jawaban: "9"
---

## Soal

Empat surat dimasukkan secara acak ke dalam empat amplop yang sudah bertuliskan alamat,
satu surat per amplop.

Ada berapa cara sehingga **tidak ada** surat yang masuk ke amplop yang benar?

## Petunjuk

- Ini persoalan baku dengan lambang tersendiri. Cari nilainya untuk empat objek.
- Bentuk rekursifnya sering paling cepat: nilai untuk $n$ dapat dihitung dari dua nilai sebelumnya.
- Nilai awalnya adalah $0$ untuk satu objek dan $1$ untuk dua objek.

## Pembahasan

Yang dicari adalah $D_4$.

**Cara pertama — rekurens.**

$$D_n = (n-1)\left(D_{n-1} + D_{n-2}\right)$$

dengan $D_1 = 0$ dan $D_2 = 1$.

$$D_3 = 2\left(D_2 + D_1\right) = 2(1+0) = 2$$

$$D_4 = 3\left(D_3 + D_2\right) = 3(2+1) = \boxed{9}$$

**Cara kedua — rumus jumlah.**

$$D_4 = 4!\left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right)
= 24\left(1 - 1 + \tfrac12 - \tfrac16 + \tfrac1{24}\right) = 24 \times \tfrac{9}{24} = 9$$

**Cara ketiga — daftar seluruhnya.** Untuk $n = 4$ ini masih mungkin dan berguna sebagai
pemeriksaan. Tulis surat sebagai $1,2,3,4$ dan amplop pada urutan yang sama; yang dicari
adalah susunan yang tiap tempatnya tidak ditempati angka yang sesuai:

$$2143,\ 2341,\ 2413,\ 3142,\ 3412,\ 3421,\ 4123,\ 4312,\ 4321$$

Tepat $9$ susunan.

**Mengapa mengurangkan sekali saja salah.** Godaan yang wajar adalah menulis
$4! - 4 \times 3! = 24 - 24 = 0$, seolah setiap surat yang benar dibuang sekali. Hasil $0$
jelas keliru — daftar di atas menunjukkan ada sembilan. Sebabnya susunan yang membuat dua
surat benar terhitung dua kali di dalam $4 \times 3!$, sehingga yang dibuang terlalu banyak.

**Barisannya tumbuh cepat:**

$$0,\ 1,\ 2,\ 9,\ 44,\ 265,\ 1854,\ \dots$$

dan sangat dekat dengan $\frac{n!}{e}$ — nyatanya $D_n$ adalah bilangan bulat terdekat dari
$\frac{n!}{e}$ untuk setiap $n \ge 1$. Untuk $n = 4$: $\frac{24}{e} \approx 8{,}83$, dan
bilangan bulat terdekatnya memang $9$. Sifat itu cara tercepat memeriksa jawaban.
