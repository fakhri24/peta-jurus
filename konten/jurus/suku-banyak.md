---
id: suku-banyak
nama: Suku Banyak
pilar: aljabar
tahap: osn-p
prasyarat: [persamaan-kuadrat]
contoh: [sb-contoh-1]
latihan: [sb-01, sb-02, sb-03, sb-04, sb-05, sb-06]
---

## Kapan dipakai

Ada polinomial berderajat tiga ke atas, atau soal berbicara tentang derajat, koefisien,
dan pembagian antar-polinomial.

## Intinya

Tulis $P(x) = a_n x^n + \cdots + a_1 x + a_0$ dengan $a_n \ne 0$; derajatnya $n$.

**Pembagian bersusun.** Untuk polinomial $P$ dan pembagi $D$ tak nol, ada $Q$ dan $R$
tunggal dengan

$$P(x) = D(x) Q(x) + R(x), \qquad \deg R < \deg D$$

Bentuknya persis algoritma pembagian pada bilangan bulat, dan dipakai dengan cara yang
sama.

Akibat yang paling sering dipakai: sisa pembagian oleh polinomial berderajat $d$ selalu
berderajat kurang dari $d$. Jadi sisa pembagian oleh $(x-a)(x-b)$ berbentuk $px + q$ —
dua bilangan tak diketahui, dan soalnya berubah menjadi mencari keduanya.

**Aturan derajat** yang sering menutup soal tanpa perhitungan:

$$\deg(PQ) = \deg P + \deg Q, \qquad \deg(P + Q) \le \max(\deg P, \deg Q)$$

Ketaksamaan pada yang kedua bisa ketat kalau suku tertingginya saling menghapus.

Polinomial berderajat $n$ punya paling banyak $n$ akar. Akibatnya: kalau dua polinomial
berderajat $\le n$ bernilai sama di $n+1$ titik berbeda, keduanya polinomial yang sama.
Itu senjata utama pada soal "tentukan $P$".

## Jebakan umum

- **Lupa sisa bisa berupa polinomial**, bukan bilangan. Sisa pembagian oleh kuadrat adalah
  bentuk linear.
- **Mengira koefisien utama boleh nol.** Derajat ditentukan oleh koefisien tak nol
  tertinggi; kalau ia memuat parameter, kasus nolnya harus diperiksa.
- **Menyimpulkan dua polinomial sama dari beberapa titik saja** tanpa memastikan
  jumlah titiknya melebihi derajatnya.
