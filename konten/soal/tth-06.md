---
id: tth-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [turun-tak-hingga]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Ada berapa pasangan $(a, b)$ dengan $a, b \in \{0, 1, 2, 3, 4, 5, 6\}$ yang memenuhi

$$a^2 + b^2 \equiv 0 \pmod 7\ ?$$

## Petunjuk

- Ini langkah pertama dari penurunan pada $x^2 + y^2 = 7z^2$, dipisahkan supaya bisa dilatih sendiri.
- Daftar dulu nilai $a^2 \bmod 7$ untuk $a = 0$ sampai $6$. Himpunannya jauh lebih kecil daripada tujuh nilai.
- Setelah himpunan kuadratnya diketahui, periksa pasangan mana saja yang berjumlah habis dibagi $7$.

## Pembahasan

Hitung dulu seluruh kuadrat modulo $7$:

| $a$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $a^2 \bmod 7$ | $0$ | $1$ | $4$ | $2$ | $2$ | $4$ | $1$ |

Jadi nilai yang mungkin hanya $\{0, 1, 2, 4\}$ — empat dari tujuh.

Sekarang cari pasangan nilai dari himpunan itu yang berjumlah habis dibagi $7$:

- $0 + 0 = 0$ — **habis dibagi $7$**
- $1 + 1 = 2$, $1 + 2 = 3$, $1 + 4 = 5$ — tidak
- $2 + 2 = 4$, $2 + 4 = 6$ — tidak
- $4 + 4 = 8 \equiv 1$ — tidak

Hanya $0 + 0$ yang berhasil. Artinya dibutuhkan $a^2 \equiv 0$ dan $b^2 \equiv 0$, yang
dalam rentang yang diberikan hanya dipenuhi oleh $a = 0$ dan $b = 0$.

Ada $\boxed{1}$ pasangan.

Inilah yang membuat penurunan pada $x^2 + y^2 = 7z^2$ bekerja: begitu $x^2 + y^2$ habis
dibagi $7$, tidak ada pilihan lain selain $7 \mid x$ dan $7 \mid y$. Bandingkan dengan
modulo $5$, di mana kuadratnya $\{0,1,4\}$ dan $1 + 4 = 5$ habis dibagi $5$ — di sana
paksaannya hilang, dan persamaan padanannya memang punya solusi tak nol.
