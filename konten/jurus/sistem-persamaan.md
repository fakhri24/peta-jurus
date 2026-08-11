---
id: sistem-persamaan
nama: Sistem Persamaan
pilar: aljabar
tahap: osn-k
prasyarat: [faktorisasi]
contoh: [sp-contoh-1]
latihan: [sp-01, sp-02, sp-03, sp-04, sp-05, sp-06]
---

## Kapan dipakai

Ada **beberapa persamaan dan beberapa peubah** sekaligus. Di olimpiade sistemnya jarang
linear, jadi mencari tiap peubah satu per satu biasanya justru jalan terpanjang.

Pemicu kedua, dan ini yang menentukan caranya: sistemnya **tidak berubah saat peubahnya
ditukar**. Begitu $x$ dan $y$ bisa dibalik tanpa mengubah apa pun, berhenti mencari $x$ —
cari $s = x+y$ dan $p = xy$ lebih dulu.

Pemicu ketiga: soal memberi **satu bentuk simetris dan menanyakan bentuk simetris lain** —
diketahui $x+y$ dan $xy$, ditanya $x^2+y^2$ atau $x^3+y^3$. Semuanya bisa ditulis lewat $s$
dan $p$ tanpa pernah menyelesaikan sistemnya.

Waspadai bentuk **siklik** yang bukan simetris penuh: $x \to y \to z \to x$ membiarkan
sistemnya tetap, tetapi menukar dua peubah saja tidak. Di situ $s$ dan $p$ belum cukup, dan
biasanya penyelesaiannya lewat penjumlahan atau pengurangan antarpersamaan.

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
