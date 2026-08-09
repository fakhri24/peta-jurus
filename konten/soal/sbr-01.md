---
id: sbr-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [stars-and-bars]
bentuk: isian
kesulitan: 1
jawaban: "28"
---

## Soal

Enam permen yang **seluruhnya sama** dibagikan kepada tiga anak. Seorang anak boleh tidak
mendapat permen sama sekali.

Ada berapa cara pembagian yang berbeda?

## Petunjuk

- Permennya tidak bisa dibedakan, jadi yang menentukan pembagian hanyalah **berapa** permen yang diterima tiap anak.
- Anaknya berbeda-beda, sehingga memberi $(2,2,2)$ tidak sama dengan memberi $(4,1,1)$.
- Bayangkan enam permen berjajar dan dua sekat yang membaginya menjadi tiga bagian.

## Pembahasan

**Nyatakan sebagai persamaan.** Sebut $x_1, x_2, x_3$ banyaknya permen yang diterima tiap
anak. Karena permennya sama semua, pembagian ditentukan sepenuhnya oleh ketiga bilangan itu:

$$x_1 + x_2 + x_3 = 6, \qquad x_i \ge 0$$

Syarat $x_i \ge 0$ — bukan $x_i \ge 1$ — karena soal mengizinkan seorang anak tidak
kebagian.

**Terapkan rumusnya.** Dengan $n = 6$ permen dan $k = 3$ anak, dibutuhkan $k - 1 = 2$
sekat, sehingga tempatnya $6 + 2 = 8$:

$$\binom{n+k-1}{k-1} = \binom{8}{2} = \frac{8 \times 7}{2} = \boxed{28}$$

**Dua sifat objeknya yang menentukan rumus mana yang dipakai:**

- **Permennya identik.** Kalau permennya berbeda-beda rasa, jawabannya $3^6 = 729$, sebab
  tiap permen memilih sendiri kepada siapa ia diberikan.
- **Anaknya berbeda.** Kalau yang dibagi adalah tiga tumpukan tanpa pemilik, $(4,1,1)$ dan
  $(1,4,1)$ akan dianggap sama, dan jawabannya jauh lebih kecil.

Sebelum memakai rumus apa pun, tetapkan dulu kedua sifat ini. Soal yang bunyinya hampir
sama bisa menuntut hitungan yang sama sekali berbeda.

**Periksa dengan mendaftar sebagian.** Pembagian dengan $x_1 = 0$ menyisakan
$x_2 + x_3 = 6$, yang punya $7$ penyelesaian. Untuk $x_1 = 1$ ada $6$, lalu $5$, $4$, $3$,
$2$, $1$:

$$7+6+5+4+3+2+1 = 28$$

Cocok. Cara memecah menurut nilai peubah pertama seperti ini berguna sebagai pemeriksaan,
dan pada persamaan tiga peubah ia masih cukup pendek dikerjakan.
