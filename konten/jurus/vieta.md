---
id: vieta
nama: Rumus Vieta
pilar: aljabar
tahap: osn-k
prasyarat: [persamaan-kuadrat]
contoh: []
latihan: []
---

## Kapan dipakai

Soal menanyakan sesuatu **tentang akar-akar** — jumlahnya, hasil kalinya, jumlah
kuadratnya — tetapi tidak menanyakan akarnya sendiri. Itu tanda paling jelas.

## Intinya

Untuk $ax^2 + bx + c = 0$ dengan akar $x_1$ dan $x_2$:

$$x_1 + x_2 = -\frac{b}{a}, \qquad x_1 x_2 = \frac{c}{a}$$

Nilainya diperoleh **tanpa menghitung akarnya**, bahkan ketika akarnya tidak rasional atau
tidak real sama sekali.

Hampir semua soal Vieta menuntut menulis ulang bentuk yang ditanya lewat $x_1+x_2$ dan
$x_1x_2$:

$$x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1x_2$$

$$\frac{1}{x_1} + \frac{1}{x_2} = \frac{x_1+x_2}{x_1x_2}, \qquad
(x_1 - x_2)^2 = (x_1+x_2)^2 - 4x_1x_2$$

Bentuk terakhir menghubungkan Vieta dengan diskriminan: $(x_1-x_2)^2 = D/a^2$.

**Arah sebaliknya** sama bergunanya. Kalau kamu tahu dua bilangan berjumlah $s$ dan
berhasil kali $p$, keduanya adalah akar $t^2 - st + p = 0$ — dan itu cara termurah
menyusun persamaan dari akar yang diminta.

## Jebakan umum

- **Lupa membagi $a$.** Jumlah akarnya $-b/a$, bukan $-b$. Untuk $a = 1$ keduanya sama,
  dan kebiasaan itu menggigit begitu $a \ne 1$.
- **Salah tanda pada jumlah akar.** Ada tanda minus di sana, tidak pada hasil kali.
- **Memakai Vieta tanpa memeriksa akarnya real** pada soal yang menuntut akar real. Vieta
  tetap berlaku untuk akar kompleks; syarat realnya datang dari $D \ge 0$.
