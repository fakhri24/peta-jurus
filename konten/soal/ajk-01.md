---
id: ajk-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 1
jawaban: "14"
---

## Soal

Dari kota $A$ ke kota $B$ terdapat $3$ jalan, dan dari kota $B$ ke kota $C$ terdapat $4$
jalan. Selain itu ada $2$ jalan yang langsung menghubungkan $A$ ke $C$ tanpa melewati $B$.

Ada berapa cara berkendara dari $A$ ke $C$?

## Petunjuk

- Perjalanannya ada dua macam yang sama sekali berbeda: lewat $B$, atau tidak lewat $B$. Kerjakan keduanya terpisah.
- Untuk yang lewat $B$, perjalanannya terdiri atas dua bagian berurutan — dan itu dihitung dengan mengalikan.
- Kedua macam perjalanan tidak mungkin terjadi bersamaan, jadi hasilnya dijumlahkan di akhir.

## Pembahasan

Soal ini memakai **kedua aturan sekaligus**, dan itulah yang dilatihnya.

**Kasus 1 — lewat $B$.** Perjalanannya dua tahap berurutan: pilih jalan $A \to B$, lalu
pilih jalan $B \to C$. Tiap pilihan tahap pertama bisa disambung dengan keempat jalan pada
tahap kedua, jadi banyaknya pilihan tahap kedua sama untuk semuanya. Aturan kali berlaku:

$$3 \times 4 = 12$$

**Kasus 2 — langsung.** Ada $2$ jalan.

**Gabungkan.** Kedua kasus **lepas** — satu perjalanan tidak mungkin sekaligus lewat $B$
dan tidak lewat $B$. Karena itu aturan jumlah berlaku:

$$12 + 2 = \boxed{14}$$

**Cara membedakan keduanya** ada pada satu kata. "Ini **lalu** itu" — dua tahap dalam satu
perjalanan yang sama — berarti dikalikan. "Ini **atau** itu" — dua jenis perjalanan yang
berbeda — berarti dijumlahkan.

Kesalahan yang paling sering pada soal semacam ini adalah menuliskan $3 \times 4 \times 2$.
Itu berarti setiap perjalanan melewati ketiga bagian sekaligus, padahal jalan langsung
justru menghindari $B$.
