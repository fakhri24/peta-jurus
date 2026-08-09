---
id: prd-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [probabilitas-diskret]
bentuk: isian
kesulitan: 2
jawaban: "1/6"
jawaban_alt: ["6/36"]
---

## Soal

Dua dadu setimbang bermata $1$ sampai $6$ dilempar bersamaan.

Berapa peluang jumlah kedua mata dadu sama dengan $7$? (Tulis sebagai pecahan paling
sederhana.)

## Petunjuk

- Tentukan dulu ruang sampelnya, dan pastikan tiap anggotanya sama mungkin. Perhatikan apakah yang dicatat adalah jumlahnya atau pasangan matanya.
- Bedakan kedua dadu — anggap satu merah dan satu biru — supaya tiap hasil punya peluang yang sama.
- Daftar pasangan yang jumlahnya $7$, lalu bagi dengan banyaknya seluruh pasangan.

## Pembahasan

**Susun ruang sampel yang sama mungkin.** Bedakan kedua dadu, misalnya satu merah dan satu
biru. Hasil percobaan dicatat sebagai pasangan terurut $(m, b)$:

$$|S| = 6 \times 6 = 36$$

Ketiga puluh enam pasangan ini **sama mungkin**, karena tiap dadu setimbang dan keduanya
tidak saling memengaruhi.

**Daftar hasil yang diinginkan.** Pasangan yang jumlahnya $7$:

$$(1,6),\ (2,5),\ (3,4),\ (4,3),\ (5,2),\ (6,1)$$

Ada $6$ pasangan. Perhatikan $(2,5)$ dan $(5,2)$ dihitung **terpisah** — keduanya hasil yang
berbeda begitu dadunya dibedakan.

**Hitung peluangnya.**

$$P = \frac{6}{36} = \boxed{\frac16}$$

**Mengapa dadunya harus dibedakan.** Kalau ruang sampelnya diambil sebagai jumlah yang
mungkin — yaitu $2, 3, \dots, 12$, sebanyak $11$ nilai — dan dijawab $\frac1{11}$, hasilnya
**salah**. Sebabnya kesebelas jumlah itu tidak sama mungkin: jumlah $7$ terjadi lewat enam
pasangan, sedangkan jumlah $2$ hanya lewat $(1,1)$.

Inilah syarat yang paling sering dilanggar di soal peluang. Rumus
$P(A) = \frac{|A|}{|S|}$ **hanya berlaku kalau tiap anggota $S$ sama mungkin**, dan
memeriksanya adalah langkah pertama, bukan langkah tambahan.

**Sebaran lengkapnya** memperlihatkan hal itu sekaligus:

| Jumlah | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Banyaknya | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ |

Jumlahkan untuk memeriksa: seluruhnya $36$. Jumlah $7$ memang yang paling sering muncul,
dan itu sebabnya ia dipakai di banyak permainan dadu.
