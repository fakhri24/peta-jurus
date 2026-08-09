---
id: pbr-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 2
jawaban: "1260"
---

## Soal

Sembilan bola disusun berjajar dalam satu baris: $3$ bola merah, $2$ bola biru, dan $4$
bola hijau. Bola yang sewarna **tidak dapat dibedakan** satu sama lain.

Ada berapa susunan yang berbeda?

## Petunjuk

- Susunan hanya dibedakan oleh warna apa yang menempati tiap tempat, bukan oleh bola mana yang di sana.
- Kalau kesembilan bola diberi nomor dan dianggap berbeda, tiap susunan warna akan terhitung berkali-kali.
- Untuk tiap warna, hitung berapa cara menukar-nukar bola sewarna itu di antara mereka sendiri.

## Pembahasan

**Yang membedakan susunan hanyalah pola warnanya.** Susunan MMMBBHHHH dan susunan yang sama
tetapi bola merah pertama ditukar dengan bola merah kedua adalah susunan yang **sama**,
sebab keduanya tidak bisa dibedakan.

**Anggap dulu kesembilan bola berbeda:**

$$9! = 362\,880$$

**Perbaiki tiap warna.** Menukar bola sewarna tidak mengubah susunannya:

$$3! \text{ untuk merah}, \qquad 2! \text{ untuk biru}, \qquad 4! \text{ untuk hijau}$$

$$\frac{9!}{3!\,2!\,4!} = \frac{362\,880}{6 \times 2 \times 24} = \frac{362\,880}{288} = \boxed{1260}$$

**Cara kedua — pilih tempatnya satu warna pada satu waktu.** Hasilnya sama, dan sering
lebih mudah diikuti:

- Pilih $3$ tempat dari $9$ untuk bola merah: $\binom93 = 84$.
- Dari $6$ tempat sisa, pilih $2$ untuk biru: $\binom62 = 15$.
- Empat tempat terakhir otomatis untuk hijau: $\binom44 = 1$.

$$84 \times 15 \times 1 = 1260$$

Cocok. Kedua cara ini selalu memberi hasil yang sama, sebab

$$\binom{9}{3}\binom{6}{2}\binom{4}{4} = \frac{9!}{3!\,6!} \cdot \frac{6!}{2!\,4!} \cdot 1
= \frac{9!}{3!\,2!\,4!}$$

Faktorial di tengah saling menghapus — dan itu memperlihatkan kedua cara pandang itu memang
satu hal yang sama.

**Soal ini dan soal susunan huruf adalah soal yang sama.** Bola merah, biru, hijau tidak
berbeda perannya dari huruf yang berulang pada sebuah kata. Mengenali dua soal yang
berpakaian berbeda sebagai soal yang sama adalah setengah dari pekerjaan kombinatorika.
