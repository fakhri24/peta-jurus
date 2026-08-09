---
id: pcg-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [pencacahan-ganda]
bentuk: isian
kesulitan: 3
jawaban: "3"
---

## Soal

Sebuah tabel berukuran $8 \times 8$ diisi angka $0$ dan $1$. Setiap **baris** berisi tepat
$3$ angka $1$, dan setiap **kolom** berisi angka $1$ sebanyak yang sama.

Berapa banyak angka $1$ pada setiap kolom?

## Petunjuk

- Hitung seluruh angka $1$ di dalam tabel, baris demi baris.
- Hitung angka yang sama sekali lagi, kali ini kolom demi kolom.
- Kedua hitungan wajib memberi hasil sama, dan dari situ jawabannya keluar.

## Pembahasan

**Nyatakan apa yang dicacah.** Yang dicacah adalah **seluruh angka $1$ di dalam tabel** —
satu himpunan yang sama, dihitung dari dua arah.

**Cara A — baris demi baris.** Ada $8$ baris dan tiap baris berisi $3$ angka $1$:

$$N = 8 \times 3 = 24$$

**Cara B — kolom demi kolom.** Ada $8$ kolom, masing-masing berisi $c$ angka $1$:

$$N = 8c$$

**Samakan.**

$$8c = 24 \quad\Longrightarrow\quad c = \boxed{3}$$

**Inilah bentuk paling murni dari pencacahan ganda:** jumlah seluruh isi tabel dapat
dihitung baris demi baris atau kolom demi kolom, dan keduanya wajib sama.

$$\sum_{i} r_i = \sum_{j} c_j$$

dengan $r_i$ jumlah baris ke-$i$ dan $c_j$ jumlah kolom ke-$j$. Bentuk ini yang berulang
kali muncul di soal olimpiade, sering dengan tabel yang tidak disebut sebagai tabel — ia
bisa berupa daftar keanggotaan, jadwal pertandingan, atau papan permainan.

**Perhatikan syarat "sebanyak yang sama" pada soal itu penting.** Tanpa syarat itu, yang
bisa disimpulkan hanyalah **jumlah** seluruh kolomnya $24$ — sedangkan sebarannya bisa
bermacam-macam, misalnya satu kolom berisi $8$ dan yang lain lebih sedikit.

Yang selalu berlaku tanpa syarat tambahan adalah nilai rata-ratanya:

$$\bar c = \frac{24}{8} = 3$$

Dari situ langsung ikut satu kesimpulan yang sering berguna: pasti ada kolom yang berisi
paling sedikit $3$ angka $1$, dan pasti ada kolom yang berisi paling banyak $3$. Menarik
kesimpulan dari rata-rata semacam ini adalah cara prinsip sarang merpati bekerja sama
dengan pencacahan ganda.
