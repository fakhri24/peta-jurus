---
id: psk-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 1
jawaban: "24"
---

## Soal

Lima orang duduk mengelilingi meja bundar tanpa nomor kursi. Susunan yang hanya berbeda
oleh pemutaran dianggap sama.

Ada berapa susunan tempat duduk yang berbeda?

## Petunjuk

- Karena tidak ada kursi yang bisa dibedakan, tidak ada tempat yang bisa disebut "pertama".
- Patok satu orang di satu tempat untuk menghilangkan kebebasan memutar.
- Sisanya disusun relatif terhadap orang yang dipatok itu.

## Pembahasan

**Patok satu orang.** Tetapkan satu orang di satu tempat. Langkah ini menghilangkan seluruh
kebebasan memutar, dan tidak ada susunan yang hilang karenanya — setiap susunan melingkar
punya tepat satu cara diputar supaya orang itu berada di tempat yang dipatok.

**Susun sisanya.** Empat orang tersisa disusun searah jarum jam:

$$(5-1)! = 4! = \boxed{24}$$

**Periksa lewat pembagian.** Susunan berjajar ada $5! = 120$, dan tiap susunan melingkar
bersesuaian dengan $5$ di antaranya:

$$\frac{120}{5} = 24$$

**Perhatikan yang sebenarnya dicacah.** Yang membedakan dua susunan melingkar bukan siapa
duduk di kursi mana, melainkan **siapa duduk di sebelah siapa**. Karena itu keterangan
"kursinya tidak bernomor" bukan hiasan — ia yang menentukan seluruh jawabannya.

**Dua pertanyaan yang wajib diperiksa di tiap soal meja bundar:**

1. **Apakah kursinya dapat dibedakan?** Kalau bernomor, jawabannya $n!$.
2. **Apakah membalik lingkaran menghasilkan susunan yang sama?** Untuk orang yang duduk,
   tidak — tetangga kiri dan tetangga kanan berbeda. Untuk benda seperti manik pada gelang
   yang boleh dibalik, ya, dan jawabannya harus dibagi $2$ lagi.

Di soal ini keduanya sudah dijawab: kursinya tidak bernomor, dan orang yang duduk
membedakan kiri dari kanan. Jadi jawabannya tepat $(n-1)!$.
