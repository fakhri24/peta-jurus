---
id: fungsi
nama: Fungsi dan Sifatnya
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: []
latihan: []
---

## Kapan dipakai

Soal memberi aturan $f$ dan menanyakan nilai di suatu titik, atau menanyakan komposisi,
invers, dan sifat seperti ganjil–genap.

## Intinya

Fungsi adalah aturan yang memberi **tepat satu** keluaran untuk tiap masukan. Dari sana
lahir seluruh sifat yang dipakai.

**Komposisi.** $(f \circ g)(x) = f(g(x))$ — dikerjakan dari dalam ke luar. Urutannya
penting: $f \circ g$ dan $g \circ f$ umumnya berbeda.

**Invers.** $f^{-1}$ ada tepat ketika $f$ satu-satu. Cara mencarinya: tulis $y = f(x)$,
selesaikan $x$ dalam $y$, lalu tukar nama. Sifat yang berguna:

$$f\left(f^{-1}(x)\right) = x, \qquad (f \circ g)^{-1} = g^{-1} \circ f^{-1}$$

Perhatikan urutan terbalik pada yang kedua.

**Ganjil dan genap.** $f$ genap kalau $f(-x) = f(x)$, ganjil kalau $f(-x) = -f(x)$.
Sifat ini sering memangkas soal: pada fungsi ganjil, $f(0) = 0$ otomatis.

**Refleks olimpiade:** kalau soal memberi hubungan seperti $f(x) + 2f(1-x) = x$, jangan
mencari rumus $f$ langsung. Ganti $x$ dengan $1-x$ untuk memperoleh persamaan kedua, lalu
selesaikan keduanya sebagai sistem dua peubah $f(x)$ dan $f(1-x)$.

## Jebakan umum

- **Membalik urutan komposisi.** $(f \circ g)$ berarti $g$ dulu.
- **Mencari invers fungsi yang tidak satu-satu** tanpa membatasi domainnya.
- **Mengira $f^{-1}(x) = \dfrac{1}{f(x)}$.** Lambangnya sama, artinya sama sekali berbeda.
