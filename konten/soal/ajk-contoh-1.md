---
id: ajk-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 2
jawaban: "20000"
---

## Soal

Sebuah sandi terdiri atas **dua huruf berbeda** yang diambil dari A, B, C, D, E, diikuti
**tiga angka** dari $0$ sampai $9$ yang boleh berulang.

Ada berapa sandi yang mungkin?

## Petunjuk

- Sandinya terbentuk dari beberapa keputusan berurutan. Tulis dulu daftar keputusannya, satu per satu.
- Bagian huruf dan bagian angka tidak saling memengaruhi, jadi banyaknya pilihan tiap bagian bisa dihitung sendiri lalu digabungkan.
- Untuk huruf: pilihan kedua tinggal empat karena huruf pertama sudah terpakai. Untuk angka: tiap tempat tetap punya sepuluh pilihan.

## Pembahasan

Sandi ini terbentuk lewat lima keputusan berurutan, dan seluruhnya dikerjakan dengan
**aturan kali**.

**Bagian huruf.** Huruf pertama bisa dipilih $5$ cara. Setelah satu huruf terpakai, huruf
kedua tinggal $4$ pilihan — karena soal meminta dua huruf yang **berbeda**.

$$5 \times 4 = 20$$

**Bagian angka.** Tiap tempat angka punya $10$ pilihan, dan pilihannya **tidak menyusut**
karena angka boleh berulang.

$$10 \times 10 \times 10 = 10^3 = 1000$$

**Gabungkan.** Setiap pilihan huruf bisa dipasangkan dengan setiap pilihan angka:

$$20 \times 1000 = \boxed{20000}$$

**Yang membuat aturan kali sah di sini.** Syaratnya bukan sekadar "ada beberapa langkah",
melainkan banyaknya pilihan langkah berikutnya harus **sama** apa pun hasil langkah
sebelumnya. Periksa: huruf kedua selalu punya tepat $4$ pilihan, huruf mana pun yang
terpilih pertama. Angka kedua selalu punya $10$, angka mana pun yang sebelumnya. Kedua
syarat terpenuhi.

Kalau syarat itu tidak terpenuhi, aturan kali belum boleh dipakai apa adanya. Misalnya
kalau soal berbunyi "huruf kedua harus berada sesudah huruf pertama menurut abjad", maka A
di tempat pertama menyisakan $4$ pilihan tetapi D menyisakan hanya $1$ — dan hitungannya
harus dipecah jadi kasus.
