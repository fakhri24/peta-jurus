---
id: bilangan-kompleks
nama: Bilangan Kompleks dan Akar Satuan
pilar: aljabar
tahap: osn
prasyarat: [akar-suku-banyak]
contoh: []
latihan: []
---

## Kapan dipakai

Persamaan berbentuk $z^n = 1$ atau $z^n = c$, jumlah yang polanya berulang tiap beberapa
suku, atau soal yang menuntut memilih sebagian koefisien binomial menurut sisanya.

## Intinya

Tulis $i^2 = -1$. Setiap bilangan kompleks bisa ditulis $z = r(\cos\theta + i\sin\theta)$
dengan $r = |z|$.

**Rumus De Moivre** membuat pangkat menjadi mudah:

$$z^n = r^n\left(\cos n\theta + i \sin n\theta\right)$$

**Akar satuan.** Persamaan $z^n = 1$ punya tepat $n$ akar:

$$\omega_k = \cos\frac{2\pi k}{n} + i \sin\frac{2\pi k}{n}, \qquad k = 0, 1, \dots, n-1$$

Dua sifat yang menjadi alasan jurus ini ada:

$$1 + \omega + \omega^2 + \cdots + \omega^{n-1} = 0 \qquad (\omega \ne 1)$$

$$\omega^n = 1 \quad\Longrightarrow\quad \omega^k \text{ hanya bergantung pada } k \bmod n$$

Yang pertama membuat akar satuan bekerja sebagai **penyaring**: menjumlahkan sebuah bentuk
atas seluruh akar satuan menghapus semua suku kecuali yang pangkatnya kelipatan $n$. Itu
cara baku menghitung jumlah koefisien binomial berindeks tertentu.

Untuk $n = 3$, akar tak trivialnya memenuhi $\omega^2 + \omega + 1 = 0$ — hubungan yang
langsung menyederhanakan banyak bentuk.

## Jebakan umum

- **Mengira $\sqrt{ab} = \sqrt{a}\sqrt{b}$ berlaku untuk bilangan negatif.** Dari sana
  lahir "bukti" bahwa $1 = -1$.
- **Lupa akar kompleks berpasangan sekawan** pada polinomial berkoefisien real.
- **Salah menghitung banyak akar.** Persamaan $z^n = c$ dengan $c \ne 0$ selalu punya
  tepat $n$ akar berbeda, bukan satu.
