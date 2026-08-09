---
id: stars-and-bars
nama: Membagi Objek Identik
pilar: kombinatorika
tahap: osn-k
prasyarat: [kombinasi, permutasi-berulang]
contoh: []
latihan: []
---

## Kapan dipakai

Membagi objek yang **identik** ke dalam wadah yang **berbeda**. Bentuk bakunya: banyaknya
penyelesaian bilangan bulat dari

$$x_1 + x_2 + \cdots + x_k = n$$

Pemicu di soal cerita: membagikan permen sejenis kepada beberapa anak, menaruh bola sewarna
ke kotak bernomor, atau memilih $n$ benda dari $k$ jenis dengan pengulangan diperbolehkan.

Perhatikan arahnya — objek identik, wadah berbeda. Kalau terbalik, ini bukan jurusnya.

## Intinya

Bayangkan $n$ bintang berjajar dan $k-1$ sekat yang membaginya jadi $k$ kelompok. Tiap
susunan bintang dan sekat memberi tepat satu penyelesaian, dan sebaliknya. Yang dicacah
tinggal susunan dari $n + k - 1$ benda dengan dua jenis:

Untuk $x_i \ge 0$:

$$\binom{n+k-1}{k-1}$$

Untuk $x_i \ge 1$, sisihkan dulu satu untuk tiap wadah lalu bagikan sisanya:

$$\binom{n-1}{k-1}$$

**Batas bawah lain diselesaikan dengan menggeser.** Kalau disyaratkan $x_i \ge 2$, tulis
$y_i = x_i - 2$; syaratnya kembali menjadi $y_i \ge 0$ dengan jumlah yang berkurang.

**Batas atas tidak bisa ditangani langsung.** Syarat seperti $x_i \le 5$ menuntut inklusi–
eksklusi: hitung tanpa batas, lalu kurangi yang melanggar.

## Jebakan umum

- **Arahnya terbalik.** Objek berbeda ke wadah identik adalah persoalan lain sama sekali,
  dan rumus ini tidak berlaku di sana.
- **Tertukar antara $\ge 0$ dan $\ge 1$.** Bedanya cuma satu kata di soal, tapi rumusnya
  berbeda.
- **Memaksakan batas atas.** Tidak ada penyesuaian sederhana untuk $x_i \le c$; yang ada
  hanya membuang kasus yang melanggar.
