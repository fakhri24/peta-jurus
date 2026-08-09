---
id: psk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-siklik]
bentuk: isian
kesulitan: 2
jawaban: "120"
---

## Soal

Enam orang duduk mengelilingi sebuah meja bundar. Kursinya tidak bernomor, dan dua susunan
dianggap **sama** kalau yang satu dapat diperoleh dari yang lain dengan memutar meja.

Ada berapa susunan tempat duduk yang berbeda?

## Petunjuk

- Susunan melingkar tidak punya "tempat pertama". Cari cara menghilangkan kebebasan memutar itu.
- Patok satu orang di satu tempat, lalu susun sisanya relatif terhadap dia.
- Setelah satu orang dipatok, berapa orang yang tersisa untuk disusun, dan apakah susunannya masih melingkar?

## Pembahasan

**Mengapa $6!$ salah.** Kalau keenam orang disusun seolah-olah berjajar, tiap susunan
melingkar akan terhitung berkali-kali — sebab memutar meja tidak menghasilkan susunan baru,
padahal ia menghasilkan urutan tulisan yang berbeda.

**Patok satu orang.** Pilih satu orang, sebut saja Ani, dan tetapkan dia di satu tempat.
Ini boleh dilakukan **tanpa kehilangan apa pun**: setiap susunan melingkar dapat diputar
sehingga Ani berada di tempat itu, dan hanya ada satu cara memutarnya ke sana.

**Susun sisanya.** Setelah Ani dipatok, lingkaran itu punya arah dan titik awal yang jelas.
Kelima orang lain tinggal disusun searah jarum jam mulai dari sebelah Ani — dan itu susunan
berjajar biasa:

$$5! = \boxed{120}$$

**Cara kedua — bagi dengan banyaknya pemutaran.** Susun keenam orang berjajar: $6! = 720$
cara. Tiap susunan melingkar bersesuaian dengan tepat $6$ susunan berjajar, sekali untuk
tiap kemungkinan pemutaran:

$$\frac{6!}{6} = \frac{720}{6} = 120$$

Cocok, dan secara umum

$$\frac{n!}{n} = (n-1)!$$

**Periksa pada kasus terkecil yang bisa didaftar.** Untuk $3$ orang $A$, $B$, $C$
melingkar, rumusnya memberi $2! = 2$. Memang hanya ada dua: searah jarum jam $A \to B \to
C$, dan $A \to C \to B$. Susunan $BCA$ dan $CAB$ sama dengan yang pertama — cukup diputar.

**Satu hal yang harus diperiksa di tiap soal meja bundar:** apakah kursinya bernomor. Kalau
bernomor, memutar menghasilkan susunan yang berbeda, lingkarannya cuma gambar, dan
jawabannya kembali $6! = 720$. Satu kata di soal memisahkan $120$ dari $720$.
