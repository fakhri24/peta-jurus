---
id: dtl-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: teori-bilangan
tahap: osn-p
jurus: [diophantine-taklinear]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Ada berapa tripel bilangan asli $(x, y, z)$ dengan $x \le y \le z$ yang memenuhi

$$\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 1\ ?$$

## Petunjuk

- Memfaktorkan tidak akan menolong di sini. Refleks yang dipakai adalah membatasi ukuran peubahnya.
- Karena $x \le y \le z$, suku $\frac1x$ adalah yang terbesar. Jadi $\frac{3}{x} \ge 1$, yang mengurung $x$ ke rentang sangat sempit.
- Setelah $x$ diketahui, ulangi gagasan yang sama untuk mengurung $y$, lalu $z$ ditentukan.

## Pembahasan

**Kurung $x$.** Karena $x \le y \le z$, suku $\frac1x$ yang terbesar, sehingga

$$1 = \frac1x + \frac1y + \frac1z \ \le\ \frac{3}{x} \quad\Longrightarrow\quad x \le 3$$

Selain itu $\frac1x < 1$ memaksa $x \ge 2$. Jadi $x \in \{2, 3\}$.

**Kasus $x = 2$.** Persamaannya menjadi

$$\frac1y + \frac1z = \frac12$$

Dengan cara yang sama, $\frac12 \le \frac2y$ memberi $y \le 4$; dan $\frac1y < \frac12$
memberi $y \ge 3$.

- $y = 3$: $\frac1z = \frac12 - \frac13 = \frac16$, jadi $z = 6$. Tripelnya $(2,3,6)$.
- $y = 4$: $\frac1z = \frac12 - \frac14 = \frac14$, jadi $z = 4$. Tripelnya $(2,4,4)$.

**Kasus $x = 3$.** Persamaannya menjadi

$$\frac1y + \frac1z = \frac23$$

Di sini $\frac23 \le \frac2y$ memberi $y \le 3$, dan $y \ge x = 3$ memberi $y \ge 3$. Jadi
$y = 3$, sehingga $\frac1z = \frac23 - \frac13 = \frac13$ dan $z = 3$. Tripelnya
$(3,3,3)$.

Seluruhnya ada $\boxed{3}$ tripel:

$$(2,3,6), \qquad (2,4,4), \qquad (3,3,3)$$

Teknik ini — mengurutkan peubah lalu memakai suku terbesar untuk membatasi — mengubah soal
yang tampaknya tak berhingga menjadi pemeriksaan beberapa kasus. Tanpa syarat
$x \le y \le z$, ketiga tripel itu masih sama, hanya terhitung berkali-kali dalam urutan
berbeda.
