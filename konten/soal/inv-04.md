---
id: inv-04
sumber: Latihan 4 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: isian
kesulitan: 4
jawaban: "39916799"
---

## Soal

Di sebuah papan tertulis bilangan $1, 2, 3, \dots, 10$. Sebuah langkah terdiri atas
menghapus dua bilangan $a$ dan $b$, lalu menuliskan

$$ab + a + b$$

Setelah $9$ langkah tersisa satu bilangan. Tentukan bilangan itu.

## Petunjuk

- Soal menanyakan nilai yang **tunggal**, bukan sifatnya. Berarti ada besaran yang benar-benar kekal, bukan sekadar paritasnya.
- Bentuk $ab+a+b$ hampir merupakan hasil kali. Coba tambahkan $1$ padanya dan perhatikan apa yang terjadi.
- Kalau $(x+1)$ untuk tiap bilangan $x$ di papan dikalikan seluruhnya, apakah hasilnya berubah oleh sebuah langkah?

## Pembahasan

**Temukan invariannya.** Bentuk $ab + a + b$ menyerupai hasil kali yang kurang satu suku.
Tambahkan $1$:

$$ab + a + b + 1 = (a+1)(b+1)$$

Inilah petunjuknya. Tinjau besaran

$$P = \prod_{x \text{ di papan}} (x+1)$$

yaitu hasil kali dari $(x+1)$ untuk seluruh bilangan $x$ yang ada di papan.

**Buktikan $P$ tidak berubah.** Sebuah langkah membuang $a$ dan $b$, lalu menulis
$c = ab+a+b$. Faktor yang hilang dari $P$ adalah $(a+1)(b+1)$, dan faktor yang masuk adalah

$$c + 1 = ab + a + b + 1 = (a+1)(b+1)$$

Persis sama. Jadi $P$ **benar-benar kekal** — bukan hanya paritasnya, melainkan nilainya.

**Hitung nilai awalnya.** Bilangan di papan adalah $1$ sampai $10$, sehingga faktornya
adalah $2$ sampai $11$:

$$P_0 = 2 \times 3 \times 4 \times \cdots \times 11 = \frac{11!}{1!} = 39\,916\,800$$

**Simpulkan.** Di akhir tersisa satu bilangan, sebut $N$. Saat itu $P$ hanya terdiri atas
satu faktor:

$$N + 1 = P = P_0 = 39\,916\,800$$

$$N = 39\,916\,800 - 1 = \boxed{39916799}$$

**Perhatikan jawabannya tidak bergantung pada urutan langkah sama sekali.** Ini berbeda dari
soal $|a-b|$, yang hasil akhirnya bisa bermacam-macam asalkan ganjil. Sebabnya di sini
invariannya adalah **nilai** $P$, bukan sekadar sifatnya — dan nilai yang kekal menentukan
jawaban secara tunggal.

Membedakan kedua jenis itu berguna sebagai penunjuk arah:

- Soal menanyakan **sifat** ("buktikan ganjil", "mungkinkah") → cari invarian berupa sifat,
  biasanya paritas atau sisa pembagian.
- Soal menanyakan **nilai tunggal** → cari besaran yang nilainya benar-benar kekal.

**Cara menemukan bentuk $(x+1)$.** Kerjakan kasus terkecil. Dengan dua bilangan $1$ dan $2$,
hasilnya $1\cdot2+1+2 = 5$; perhatikan $5+1 = 6 = 2 \times 3$. Dengan $2$ dan $3$: hasilnya
$11$, dan $11+1 = 12 = 3 \times 4$. Pola $+1$ langsung terlihat, dan dari situ tebakannya
tinggal dibuktikan.
