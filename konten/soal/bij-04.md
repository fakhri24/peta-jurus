---
id: bij-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 4
jawaban: "35"
---

## Soal

Ada berapa barisan sepanjang $10$ yang tiap sukunya $0$ atau $1$, memuat **tepat empat**
angka $1$, dan **tidak ada dua angka $1$ yang berdampingan**?

## Petunjuk

- Susun dulu keenam angka $0$, lalu perhatikan celah-celah yang terbentuk di antara dan di ujungnya.
- Menempatkan tiap angka $1$ pada celah yang berbeda menjamin syaratnya terpenuhi dengan sendirinya.
- Periksa arah sebaliknya: dari sebarang barisan yang sah, celah mana yang ditempati tiap angka $1$?

## Pembahasan

**Susun angka nolnya dulu.** Ada $10 - 4 = 6$ angka $0$. Jajarkan seluruhnya:

$$\_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_\ 0\ \_$$

Enam angka $0$ membentuk $7$ celah, termasuk kedua ujungnya.

**Bangun padanannya.** Tempatkan keempat angka $1$ pada **celah yang berbeda-beda**.

- Kalau tiap celah menampung paling banyak satu angka $1$, maka di antara dua angka $1$
  mana pun pasti ada sedikitnya satu angka $0$ — jadi syaratnya terpenuhi.
- Sebaliknya, dari sebarang barisan sah, tiap angka $1$ menempati sebuah celah di antara
  angka nolnya, dan tidak ada dua angka $1$ pada celah yang sama — sebab kalau ada, keduanya
  berdampingan.

Kedua arah saling meniadakan, jadi padanannya satu-satu dan pada.

**Cacah pemilihannya.** Angka $1$ tidak dapat dibedakan satu sama lain, sehingga yang
dihitung hanyalah **celah mana** yang terpakai:

$$\binom{7}{4} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \boxed{35}$$

**Bentuk umumnya** — barisan sepanjang $n$ dengan tepat $k$ angka $1$ tanpa dua yang
berdampingan:

$$\binom{n-k+1}{k}$$

Periksa: $n = 10$, $k = 4$ memberi $\binom74 = 35$.

**Syarat agar ada jawabannya sama sekali.** Rumus di atas bernilai nol kalau
$k > n-k+1$, yaitu kalau angka $1$-nya terlalu banyak untuk dipisahkan. Untuk $n = 10$,
paling banyak $k = 5$ — barisan $1010101010$. Dengan $k = 6$ jawabannya $0$, dan itu bisa
disimpulkan tanpa menghitung.

**Cara celah ini yang menggantikan pengurangan.** Menghitung lewat "seluruhnya dikurangi
yang melanggar" akan sulit di sini, sebab "ada dua angka $1$ berdampingan" bisa terjadi pada
beberapa pasangan sekaligus dan kelompoknya saling beririsan. Menyusun langsung supaya
syaratnya terpenuhi menghindari seluruh persoalan itu.

**Bandingkan dengan soal yang tidak mematok banyaknya angka $1$.** Kalau syaratnya hanya
"tidak ada dua angka $1$ berdampingan" tanpa menyebut ada berapa, jawabannya $144$ — dan
menjumlahkan rumus di atas atas seluruh $k$ memang memberi angka itu:

$$\binom{11}{0}+\binom{10}{1}+\binom92+\binom83+\binom74+\binom65 = 1+10+36+56+35+6 = 144$$
