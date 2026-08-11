---
id: fungsi
nama: Fungsi dan Sifatnya
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: [fn-contoh-1]
latihan: [fn-01, fn-02, fn-03, fn-04, fn-05, fn-06]
---

## Kapan dipakai

Soal **memberi aturan $f$ secara utuh** lalu menanyakan nilainya di suatu titik, atau
menanyakan **komposisi** dan **invers**. Ciri paling terang: ada $f(g(x))$, $f^{-1}$, atau
$f \circ f$ yang harus diuraikan.

Pemicu kedua: soal menyebut **ganjil–genap**, atau memberi kesamaan seperti $f(-x) = f(x)$
dan menanyakan akibatnya. Yang ditanya biasanya bukan $f$-nya, melainkan simetri yang
mengikutinya.

Pemicu ketiga: soal menyusun $f$ berulang kali — $f(f(f(x)))$ atau $f^{2026}(x)$ — dan
menanyakan hasilnya. Bentuk itu hampir selalu berputar; cari panjang putarannya, jangan
menguraikan semuanya.

Bedakan dari Persamaan Fungsional: kalau rumus $f$ **tidak** diberikan dan yang diketahui
hanya sebuah kesamaan yang berlaku untuk semua $x$, itu jurus yang lain — dan jauh lebih
berat.

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
