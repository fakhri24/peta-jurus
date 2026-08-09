---
id: pwn-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: isian
kesulitan: 2
jawaban: "2"
---

## Soal

Dari papan catur $8 \times 8$ dibuang dua petak di sudut yang **berlawanan**.

Berapa **selisih** antara banyaknya petak hitam dan petak putih yang tersisa?

## Petunjuk

- Hitung dulu berapa petak tiap warna pada papan penuh.
- Tentukan warna kedua petak sudut yang dibuang — perhatikan apakah keduanya sewarna.
- Selisihnya adalah besaran yang menutup kemungkinan penutupan domino, jadi hitunglah dengan teliti.

## Pembahasan

**Papan penuh.** Papan $8\times8$ punya $64$ petak, terbagi rata:

$$32 \text{ hitam}, \qquad 32 \text{ putih}$$

**Warna kedua sudut yang dibuang.** Beri koordinat $(i,j)$ dan warnai menurut paritas
$i+j$. Sudut yang berlawanan, misalnya $(1,1)$ dan $(8,8)$, punya

$$1+1 = 2 \qquad \text{dan} \qquad 8+8 = 16$$

Keduanya genap, jadi kedua sudut itu **sewarna**. Sebut keduanya hitam.

**Sisa papan.**

$$32 - 2 = 30 \text{ hitam}, \qquad 32 \text{ putih}$$

**Selisihnya.**

$$32 - 30 = \boxed{2}$$

**Mengapa angka ini yang menentukan.** Sebuah domino selalu menutup tepat satu petak tiap
warna, di mana pun diletakkan. Karena itu penutupan penuh hanya mungkin kalau kedua warna
**sama banyaknya** — yaitu selisihnya nol.

Selisih $2$ berarti penutupan dengan $31$ domino mustahil, dan angka $2$ itu sekaligus
menunjukkan seberapa jauh papannya dari bisa ditutup: paling sedikit dua petak akan selalu
tersisa.

**Bandingkan dengan sudut yang berdekatan.** Kalau yang dibuang $(1,1)$ dan $(1,8)$, maka
$i+j$ bernilai $2$ dan $9$ — berbeda paritas, sehingga keduanya berlainan warna. Sisa
papannya $31$ hitam dan $31$ putih, selisih $0$, dan pewarnaan **tidak menutup** kemungkinan
apa pun.

Bahwa selisihnya nol tidak dengan sendirinya berarti penutupannya bisa; untuk itu diperlukan
konstruksi. Perbedaan antara "tidak terhalang" dan "bisa" adalah hal yang dilatih di latihan
berikutnya.
