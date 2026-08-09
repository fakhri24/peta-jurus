---
id: sbr-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 2
jawaban: "84"
---

## Soal

Sepuluh bola yang **seluruhnya sama** dimasukkan ke dalam $4$ kotak yang **bernomor** $1$
sampai $4$. Tiap kotak harus berisi **paling sedikit satu** bola.

Ada berapa cara pengisian yang berbeda?

## Petunjuk

- Nyatakan dulu sebagai persamaan: berapa bola di tiap kotak, dan berapa jumlahnya.
- Syarat "paling sedikit satu" menjadikan tiap peubahnya positif, bukan tak negatif.
- Sisihkan satu bola untuk tiap kotak lebih dulu, lalu bagikan sisanya bebas.

## Pembahasan

**Nyatakan sebagai persamaan.** Sebut $x_i$ banyaknya bola di kotak ke-$i$. Bolanya identik
sehingga hanya jumlahnya yang berarti, sedangkan kotaknya bernomor sehingga bisa dibedakan:

$$x_1 + x_2 + x_3 + x_4 = 10, \qquad x_i \ge 1$$

**Sisihkan jatah wajibnya.** Masukkan lebih dulu satu bola ke tiap kotak. Terpakai $4$ bola,
tersisa

$$10 - 4 = 6$$

yang kini boleh dibagikan bebas, termasuk seluruhnya ke satu kotak.

**Terapkan rumusnya** dengan $n = 6$ dan $k = 4$:

$$\binom{6+4-1}{4-1} = \binom93 = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = \boxed{84}$$

Atau langsung dengan rumus penyelesaian positif:

$$\binom{n-1}{k-1} = \binom{10-1}{4-1} = \binom93 = 84$$

**Perhatikan kata "bernomor" pada soal.** Ia yang membuat kotaknya bisa dibedakan, sehingga
pengisian $(4,2,2,2)$ berbeda dari $(2,4,2,2)$. Kalau kotaknya justru **tidak** bisa
dibedakan, kedua pengisian itu dianggap sama dan jawabannya jauh lebih kecil — persoalan
semacam itu tidak diselesaikan rumus ini sama sekali.

Empat kemungkinan yang harus selalu dipisahkan sebelum menghitung:

| Bola | Kotak | Diselesaikan dengan |
|---|---|---|
| identik | berbeda | rumus ini |
| berbeda | berbeda | $k^{n}$, tiap bola memilih kotaknya |
| identik | identik | pemartisian bilangan, bukan rumus ini |
| berbeda | identik | pemartisian himpunan, bukan rumus ini |

Membaca soal untuk menentukan baris mana yang berlaku adalah separuh pekerjaannya.

**Periksa dengan syarat yang lebih longgar.** Tanpa syarat "paling sedikit satu",
jawabannya $\binom{13}{3} = 286$. Lebih besar dari $84$, sebagaimana seharusnya.
