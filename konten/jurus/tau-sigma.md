---
id: tau-sigma
nama: Banyaknya & Jumlah Faktor
pilar: teori-bilangan
tahap: osn-k
prasyarat: [bilangan-prima]
contoh: [ts-contoh-1]
latihan: [ts-01, ts-02, ts-03, ts-04, ts-05, ts-06]
---

## Kapan dipakai

Soal menghitung **ada berapa** faktor sebuah bilangan, **menjumlahkan** seluruh faktornya,
atau memberi syarat seperti "punya tepat 12 faktor".

Pemicu kedua, dan ini arah yang paling sering dipakai olimpiade: syaratnya **dibalik** —
diketahui $\tau(n) = 12$, dicari $n$ terkecil. Soal berubah dari menghitung menjadi memecah
$12$ menjadi hasil kali $(a_i+1)$, lalu memasangkan pangkat terbesar dengan prima terkecil.

Pemicu ketiga: soal menyebut **banyaknya faktor ganjil atau genap**. Banyaknya faktor ganjil
tepat ketika bilangannya kuadrat sempurna — karena hanya di situ ada faktor yang berpasangan
dengan dirinya sendiri. Pengamatan itu menyelesaikan sekelas soal "lampu yang ditekan
berulang" tanpa satu pun faktor dihitung.

Pemicu keempat: soal berbicara tentang **bilangan sempurna** atau membandingkan $\sigma(n)$
dengan $2n$. Itu $\sigma$ yang menyamar.

Prasyarat yang tak tertulis: keduanya rumus **atas faktorisasi prima**, jadi soal yang
angkanya belum difaktorkan menuntut itu lebih dulu.

## Intinya

Kalau $n = p_1^{a_1} \cdots p_k^{a_k}$, maka

$$\tau(n) = (a_1+1)(a_2+1)\cdots(a_k+1)$$

$$\sigma(n) = \prod_i \frac{p_i^{a_i+1} - 1}{p_i - 1}$$

Rumus $\tau$ lahir dari pencacahan langsung: setiap faktor dibentuk dengan memilih pangkat
$p_i$ dari $0$ sampai $a_i$ — ada $a_i + 1$ pilihan, dan pilihannya saling bebas.

Soal olimpiade biasanya membalik arahnya: diberi $\tau(n) = 12$, cari $n$ yang memenuhi.
Karena $12 = 12 = 6\cdot2 = 4\cdot3 = 3\cdot2\cdot2$, pola pangkatnya cuma beberapa
kemungkinan — dan pencacahannya berhingga.

Satu fakta yang sering jadi kunci: **$\tau(n)$ ganjil tepat ketika $n$ kuadrat sempurna**,
karena faktor selalu berpasangan $d \leftrightarrow n/d$ kecuali saat $d = \sqrt{n}$.

## Jebakan umum

- **Lupa menambah satu.** Pangkat $a$ memberi $a+1$ pilihan, bukan $a$.
- **Mengalikan $\tau$ pada bilangan yang tidak relatif prima.** $\tau$ multiplikatif hanya
  saat $\gcd(m,n)=1$.
- **Melupakan $1$ dan $n$ sendiri** saat menghitung faktor dengan tangan.
