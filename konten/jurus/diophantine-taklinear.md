---
id: diophantine-taklinear
nama: Diophantine Taklinear
pilar: teori-bilangan
tahap: osn-p
prasyarat: [turun-tak-hingga, tau-sigma]
contoh: []
latihan: []
---

## Kapan dipakai

Persamaan dengan solusi bulat yang memuat hasil kali atau pangkat — $xy + ax + by = c$,
$x^2 - y^2 = n$, atau pecahan seperti $\frac1x + \frac1y = \frac1n$.

## Intinya

Tidak ada satu rumus. Yang ada empat refleks, dicoba berurutan:

1. **Faktorkan.** Ubah jadi (sesuatu)(sesuatu) = konstanta, lalu cacah pasangan
   pembaginya. Untuk $xy + ax + by$, tambahkan $ab$ ke kedua ruas:
   $(x+b)(y+a) = c + ab$. Ini *pemfaktoran Simon*, dan ia menyelesaikan lebih banyak soal
   daripada yang pantas.
2. **Selisih kuadrat.** $x^2 - y^2 = (x-y)(x+y)$. Perhatikan kedua faktornya selalu
   berparitas sama — itu sendiri sudah membatasi banyak.
3. **Ambil modulo.** Untuk membuktikan tidak ada solusi. Modulo $4$, $8$, $9$ dulu.
4. **Batasi ukurannya.** Kalau $x \le y \le z$, maka $\frac1x$ adalah yang terbesar, dan
   itu memaksa $x$ kecil. Sisanya diperiksa dengan tangan.

Refleks keempat sering terlupa padahal paling ampuh untuk soal pecahan satuan: begitu $x$
terkurung di rentang kecil, soalnya berubah jadi pencacahan berhingga.

## Jebakan umum

- **Faktorisasi tanpa menyaring.** Setelah $(x+b)(y+a) = N$, kamu masih harus membuang
  pasangan yang membuat $x$ atau $y$ jatuh di luar syarat soal.
- **Melupakan pembagi negatif** ketika soal membolehkan bilangan bulat sembarang.
- **Menghabiskan waktu mencari solusi yang tidak ada.** Kalau lima menit tidak ada gerak,
  cobalah membuktikan sebaliknya lewat modulo.
