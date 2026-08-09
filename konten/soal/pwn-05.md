---
id: pwn-05
sumber: Latihan 5 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: isian
kesulitan: 4
jawaban: "1024"
---

## Soal

Dari papan catur $8 \times 8$ dibuang dua petak: **satu berwarna hitam dan satu berwarna
putih**. Diketahui bahwa sisa papan seperti itu selalu dapat ditutup oleh $31$ domino,
di mana pun kedua petak itu berada.

Ada berapa pasangan petak yang dapat dibuang seperti itu?

## Petunjuk

- Soal tidak menyuruh membuktikan apa pun — kenyataan bahwa penutupannya selalu ada sudah diberikan. Yang diminta hanyalah mencacah pasangannya.
- Hitung berapa petak hitam dan berapa petak putih pada papan penuh.
- Sebuah pasangan ditentukan oleh satu pilihan dari tiap warna, dan kedua pilihan itu tidak saling membatasi.

## Pembahasan

**Hitung persediaan tiap warna.** Papan $8\times8$ punya

$$32 \text{ petak hitam}, \qquad 32 \text{ petak putih}$$

**Cacah pasangannya.** Sebuah pasangan yang sah terdiri atas satu petak hitam dan satu petak
putih. Kedua pilihan itu tidak saling membatasi — petak hitam mana pun dapat dipasangkan
dengan petak putih mana pun, sebab keduanya pasti berbeda petak:

$$32 \times 32 = \boxed{1024}$$

**Mengapa tidak dibagi dua.** Godaannya adalah membagi $2$ karena pasangan $\{a,b\}$ sama
dengan $\{b,a\}$. Di sini pembagian itu **tidak** diperlukan: kedua petak sudah dibedakan
oleh warnanya, sehingga tiap pasangan terhitung tepat sekali. Perkalian $32\times32$
memilih satu hitam dan satu putih, bukan dua petak dari satu kolam yang sama.

Bandingkan dengan pertanyaan "ada berapa cara membuang dua petak sembarang", yang jawabannya
$\binom{64}{2} = 2016$ — di situ pembagian memang diperlukan, sebab keduanya diambil dari
kolam yang sama.

**Bacaan angkanya.** Dari $2016$ pasangan yang mungkin, hanya $1024$ yang menyisakan papan
yang dapat ditutup — sedikit di atas separuhnya. Sisanya, $992$ pasangan, adalah pasangan
sewarna:

$$\binom{32}{2} + \binom{32}{2} = 496 + 496 = 992$$

Periksa: $1024 + 992 = 2016$. Cocok.

**Kekuatan pernyataan yang diberikan soal.** Pewarnaan sendiri hanya membuktikan bahwa
pasangan **sewarna** tidak mungkin ditutup. Ia sama sekali tidak menjamin pasangan berbeda
warna pasti bisa — dan itulah bagian yang jauh lebih sulit.

Kenyataan bahwa setiap pasangan berbeda warna memang selalu bisa ditutup adalah hasil yang
dikenal, dan buktinya tidak memakai pewarnaan sama sekali: papan $8\times8$ dapat ditelusuri
oleh sebuah lintasan tertutup yang melewati tiap petak tepat sekali, dan membuang dua petak
berbeda warna memecah lintasan itu menjadi dua potongan yang panjangnya genap — masing-masing
langsung terisi domino.

Pola "invarian menutup sebagian, konstruksi membuka sisanya" itu berulang di hampir semua
soal ubin yang lengkap.
