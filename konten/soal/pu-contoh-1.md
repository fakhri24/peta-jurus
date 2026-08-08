---
id: pu-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: aljabar
tahap: osn
jurus: [penataan-ulang]
bentuk: isian
kesulitan: 2
jawaban: "32"
---

## Soal

Bilangan $4$, $5$, dan $6$ akan dipasangkan satu-satu dengan bilangan $1$, $2$, dan $3$.
Tentukan nilai **terbesar** dari jumlah ketiga hasil kalinya.

## Petunjuk

- Ada enam cara memasangkan. Coba beberapa dan perhatikan pola mana yang memberi hasil besar.
- Untuk memperbesar jumlah hasil kali, pasangkan bilangan besar dengan bilangan besar.
- Urutkan kedua kelompok, lalu pasangkan berurutan.

## Pembahasan

**Ketaksamaan penataan ulang** menyatakan: di antara semua cara memasangkan dua kelompok
bilangan, jumlah hasil kalinya paling besar ketika keduanya **diurutkan searah** — besar
dengan besar, kecil dengan kecil.

Urutkan kedua kelompok menaik:

$$1 \le 2 \le 3, \qquad 4 \le 5 \le 6$$

Pasangkan berurutan:

$$1 \times 4 + 2 \times 5 + 3 \times 6 = 4 + 10 + 18 = \boxed{32}$$

**Periksa seluruh kemungkinan** — hanya ada enam, jadi bisa didaftar:

| Pasangan untuk $1,2,3$ | Jumlah |
|---|---|
| $4, 5, 6$ | $4+10+18 = 32$ |
| $4, 6, 5$ | $4+12+15 = 31$ |
| $5, 4, 6$ | $5+8+18 = 31$ |
| $5, 6, 4$ | $5+12+12 = 29$ |
| $6, 4, 5$ | $6+8+15 = 29$ |
| $6, 5, 4$ | $6+10+12 = 28$ |

Yang terbesar memang $32$, dari pemasangan searah; yang terkecil $28$, dari pemasangan
berlawanan arah. Semua pemasangan lain berada di antaranya — persis yang dinyatakan
ketaksamaannya.

**Alasannya bisa dilihat pada satu penukaran.** Misalkan $a \le b$ dan $x \le y$.
Bandingkan dua cara memasangkan:

$$(ax + by) - (ay + bx) = a(x-y) + b(y-x) = (b-a)(y-x) \ \ge\ 0$$

Jadi pemasangan searah selalu tidak kalah. Setiap pemasangan sembarang bisa diubah menjadi
pemasangan searah lewat rangkaian penukaran semacam itu, dan tiap penukaran tidak pernah
mengurangi jumlahnya.
