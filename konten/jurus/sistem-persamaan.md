---
id: sistem-persamaan
nama: Sistem Persamaan
pilar: aljabar
tahap: osn-k
prasyarat: [faktorisasi]
contoh: []
latihan: []
---

## Kapan dipakai

Ada beberapa persamaan dan beberapa peubah sekaligus. Di olimpiade, sistemnya jarang
linear — biasanya simetris atau bisa dibuat simetris.

## Intinya

Untuk sistem linear, tiga cara baku: substitusi, eliminasi, dan penjumlahan berbobot.
Yang terakhir sering paling cepat pada soal simetris.

Yang lebih berharga adalah **memakai kesimetrian**. Kalau sistemnya tidak berubah saat
peubahnya ditukar, jangan cari tiap peubah — cari bentuk simetrisnya lebih dulu:

$$s = x + y, \qquad p = xy$$

Hampir semua bentuk simetris bisa ditulis lewat $s$ dan $p$:

$$x^2 + y^2 = s^2 - 2p, \qquad x^3 + y^3 = s^3 - 3ps, \qquad
\frac1x + \frac1y = \frac{s}{p}$$

Setelah $s$ dan $p$ diketahui, $x$ dan $y$ adalah akar dari

$$t^2 - st + p = 0$$

**Menjumlahkan dan mengurangkan seluruh persamaan** juga sering membuka jalan pada sistem
simetris — hasilnya biasanya jauh lebih sederhana daripada persamaan aslinya.

## Jebakan umum

- **Kehilangan solusi saat membagi.** Membagi dua persamaan menghilangkan kasus penyebutnya
  nol; periksa kasus itu terpisah.
- **Lupa memeriksa $s^2 \ge 4p$.** Tanpa itu, $x$ dan $y$ yang diperoleh tidak real.
- **Menukar peran $s$ dan $p$** pada rumus $x^3+y^3$. Cek dengan angka kecil kalau ragu.
