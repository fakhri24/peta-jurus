---
id: psk-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 3
jawaban: "144"
---

## Soal

Empat pria dan empat wanita duduk mengelilingi meja bundar tanpa nomor kursi, dengan syarat
pria dan wanita duduk **berselang-seling**.

Ada berapa susunan tempat duduk yang berbeda?

## Petunjuk

- Dudukkan dulu salah satu kelompok secara melingkar, lalu perhatikan celah yang terbentuk di antara mereka.
- Kalau keempat pria sudah duduk melingkar, ada berapa celah, dan apa yang terjadi kalau tiap celah diisi seorang wanita?
- Perhatikan hanya **satu** kelompok yang disusun melingkar. Setelah kelompok pertama duduk, celahnya sudah bisa dibedakan satu sama lain.

## Pembahasan

**Langkah 1 — dudukkan para pria melingkar.** Kursinya tidak bernomor, jadi ini susunan
melingkar biasa:

$$(4-1)! = 3! = 6$$

**Langkah 2 — tandai celahnya.** Empat pria yang duduk melingkar membentuk tepat $4$ celah,
masing-masing di antara dua pria yang bersebelahan. Mengisi tiap celah dengan seorang wanita
memaksa susunannya berselang-seling — dan itu satu-satunya cara memenuhi syarat soal,
karena delapan orang dengan empat pria dan empat wanita hanya bisa berselang-seling kalau
tiap celah antar-pria berisi tepat satu wanita.

**Langkah 3 — dudukkan para wanita.** Di sini letak bagian yang paling mudah keliru:
**celah-celah itu sudah bisa dibedakan satu sama lain**, sebab masing-masing ditandai oleh
pasangan pria yang mengapitnya. Jadi menempatkan wanita ke celah bukan lagi susunan
melingkar, melainkan susunan berjajar biasa:

$$4! = 24$$

**Gabungkan.**

$$6 \times 24 = \boxed{144}$$

**Mengapa hanya satu kelompok yang memakai $(n-1)!$.** Kebebasan memutar meja sudah habis
terpakai pada langkah pertama. Begitu para pria duduk, lingkarannya punya penanda yang
tetap, dan segala sesuatu setelah itu dihitung seperti susunan biasa.

Memakai $(4-1)!$ dua kali — sehingga jawabannya $6 \times 6 = 36$ — adalah kekeliruan yang
paling sering di soal ini. Ia berarti membuang kebebasan memutar dua kali, padahal
kebebasan itu hanya ada sekali.

**Bentuk umumnya** untuk $n$ pria dan $n$ wanita berselang-seling di meja bundar:

$$(n-1)! \times n!$$

Periksa untuk $n = 2$: rumusnya memberi $1 \times 2 = 2$, dan memang ada dua susunan —
kedua wanita bisa bertukar tempat, sementara kedua pria sudah tertentu setelah pemutaran
dibuang.

**Kalau banyaknya pria dan wanita tidak sama,** berselang-seling menjadi mustahil di meja
bundar. Lima pria dan empat wanita, misalnya, pasti menyisakan dua pria berdampingan.
