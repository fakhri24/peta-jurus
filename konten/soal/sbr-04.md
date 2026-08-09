---
id: sbr-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 3
jawaban: "55"
---

## Soal

Ada berapa penyelesaian bilangan bulat dari

$$x + y + z = 15$$

yang memenuhi $x \ge 2$, $y \ge 3$, dan $z \ge 1$?

## Petunjuk

- Batas bawahnya berbeda-beda, tetapi seluruhnya jenis yang sama: tiap peubah punya jatah minimum.
- Sisihkan jatah minimum tiap peubah lebih dulu, lalu perhatikan sisa yang boleh dibagikan bebas.
- Setelah penggeseran, syaratnya seragam menjadi tak negatif dan rumus baku bisa dipakai.

## Pembahasan

**Sisihkan jatah minimumnya.** Berikan lebih dulu $2$ untuk $x$, $3$ untuk $y$, dan $1$
untuk $z$. Terpakai

$$2 + 3 + 1 = 6$$

dan yang tersisa untuk dibagikan bebas

$$15 - 6 = 9$$

**Nyatakan dengan penggeseran.** Tulis

$$x' = x - 2, \qquad y' = y - 3, \qquad z' = z - 1$$

Syaratnya kini seragam: $x', y', z' \ge 0$. Substitusikan ke persamaan aslinya:

$$(x'+2) + (y'+3) + (z'+1) = 15 \quad\Longrightarrow\quad x' + y' + z' = 9$$

**Penggeseran ini padanan satu-satu.** Tiap penyelesaian yang memenuhi batas asli memberi
tepat satu penyelesaian tak negatif dari persamaan baru, dan sebaliknya — tinggal
menambahkan kembali jatahnya. Jadi kedua persoalan punya jawaban sama banyaknya.

**Terapkan rumusnya** dengan $n = 9$ dan $k = 3$:

$$\binom{9+3-1}{3-1} = \binom{11}{2} = \frac{11 \times 10}{2} = \boxed{55}$$

**Kunci soal ini adalah menyeragamkan syaratnya lebih dulu.** Rumus baku hanya mengenal dua
bentuk — semua peubah $\ge 0$ atau semua $\ge 1$. Batas bawah yang berbeda-beda tidak
ditangani rumus mana pun secara langsung, dan penggeseran mengubahnya menjadi bentuk yang
dikenal.

**Yang harus diperiksa sebelum menghitung:** apakah sisanya masih tak negatif. Kalau jumlah
seluruh batas bawah melebihi ruas kanan, penyelesaiannya **tidak ada**. Misalnya kalau
soalnya menuntut $x \ge 8$, $y \ge 6$, $z \ge 4$ dengan jumlah $15$, maka $8+6+4 = 18 > 15$
dan jawabannya $0$ — tanpa perlu menghitung apa pun.

**Batas atas adalah perkara lain sama sekali.** Penggeseran tidak menolong untuk syarat
seperti $x \le 7$, sebab menggeser dari atas justru membuat peubahnya bisa negatif. Syarat
semacam itu ditangani dengan membuang penyelesaian yang melanggar.
