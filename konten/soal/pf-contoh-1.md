---
id: pf-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: aljabar
tahap: osn
jurus: [persamaan-fungsional]
bentuk: isian
kesulitan: 3
jawaban: "-4"
---

## Soal

Fungsi $f$ memenuhi

$$f(x) + 2f(1-x) = 3x$$

untuk setiap bilangan real $x$. Tentukan nilai $f(2)$.

## Petunjuk

- Rumus $f$ tidak diketahui dan tidak perlu dicari. Yang diketahui hubungan antara $f(x)$ dan $f(1-x)$.
- Substitusikan $x = 2$ untuk memperoleh persamaan yang memuat $f(2)$ dan $f(-1)$.
- Cari substitusi yang **menukar** kedua argumen itu: dari $1-x = 2$ diperoleh $x = -1$.

## Pembahasan

Persamaan itu berlaku untuk **setiap** $x$, jadi kita boleh memasukkan nilai apa pun yang
menguntungkan.

**Substitusikan $x = 2$.** Argumen keduanya menjadi $1 - 2 = -1$:

$$f(2) + 2f(-1) = 6$$

**Substitusikan $x = -1$.** Argumen keduanya menjadi $1 - (-1) = 2$ — kembali ke $f(2)$:

$$f(-1) + 2f(2) = -3$$

Pemilihan itulah kuncinya: substitusi kedua dipilih supaya kedua argumen **bertukar
peran**, sehingga tidak ada nilai baru yang muncul.

**Selesaikan sebagai sistem.** Sebut $A = f(2)$ dan $B = f(-1)$:

$$A + 2B = 6, \qquad B + 2A = -3$$

Kalikan persamaan kedua dengan $2$:

$$2B + 4A = -6$$

Kurangkan persamaan pertama:

$$(2B+4A) - (A+2B) = -6 - 6 \quad\Longrightarrow\quad 3A = -12
\quad\Longrightarrow\quad A = \boxed{-4}$$

Periksa: dari $A = -4$ dan persamaan pertama, $2B = 10$ sehingga $B = 5$. Periksa
persamaan kedua: $5 + 2(-4) = -3$. Cocok.

**Kalau ingin rumus umumnya**, gerakan yang sama bekerja dengan $x$ tetap sebagai huruf.
Substitusikan $x \to 1-x$ pada persamaan aslinya:

$$f(1-x) + 2f(x) = 3(1-x)$$

Sekarang ada dua persamaan dalam $f(x)$ dan $f(1-x)$. Kalikan yang kedua dengan $2$ dan
kurangkan yang pertama:

$$3f(x) = 6 - 6x - 3x \quad\Longrightarrow\quad f(x) = 2 - 3x$$

Periksa $f(2) = 2 - 6 = -4$ — cocok. Dan periksa balik ke persamaan aslinya:
$(2-3x) + 2\left(2 - 3(1-x)\right) = 2-3x + 2(3x-1) = 3x$ ✓.

**Langkah memeriksa balik itu tidak boleh dilewati.** Rangkaian substitusi bisa memperluas
himpunan solusi, jadi fungsi yang diperoleh harus diuji ke persamaan aslinya.
