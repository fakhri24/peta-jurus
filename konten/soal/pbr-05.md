---
id: pbr-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 3
jawaban: "60"
---

## Soal

Ada berapa bilangan **berbeda** yang dapat dibentuk dengan menyusun seluruh angka berikut,
masing-masing dipakai tepat sekali?

$$1,\ 1,\ 2,\ 2,\ 2,\ 3$$

## Petunjuk

- Angka yang sama tidak bisa dibedakan, jadi menukar dua angka $2$ tidak menghasilkan bilangan yang lain.
- Hitung berapa kali tiap angka muncul, lalu periksa jumlahnya.
- Perhatikan tidak ada angka $0$ di sini, sehingga tidak perlu memikirkan larangan angka pertama.

## Pembahasan

**Daftar angkanya.**

| Angka | $1$ | $2$ | $3$ |
|---|---|---|---|
| Banyaknya | $2$ | $3$ | $1$ |

Jumlahnya $2 + 3 + 1 = 6$, jadi bilangan yang dibentuk terdiri atas $6$ angka.

**Hitung.**

$$\frac{6!}{2!\,3!\,1!} = \frac{720}{2 \times 6 \times 1} = \frac{720}{12} = \boxed{60}$$

**Mengapa tidak ada penyesuaian untuk angka pertama.** Pada soal bilangan, biasanya harus
diperiksa apakah angka pertama boleh $0$ — sebab $0$ di depan membuat bilangannya lebih
pendek. Di sini angka yang tersedia hanya $1$, $2$, $3$, sehingga larangan itu tidak pernah
berlaku dan seluruh $60$ susunan memang bilangan enam angka yang sah.

Kalau angkanya diganti menjadi $0, 0, 2, 2, 2, 3$, hitungannya bertambah satu langkah:
seluruh susunan ada $\frac{6!}{2!\,3!} = 60$, lalu dikurangi susunan yang diawali $0$.
Susunan yang diawali $0$ berarti menyusun $0,2,2,2,3$ pada lima tempat sisanya, yaitu
$\frac{5!}{3!} = 20$. Jawabannya menjadi $60 - 20 = 40$.

**Menyatakan ulang soal sebagai soal susunan huruf.** Bilangan yang dicari tidak berbeda
sedikit pun dari susunan huruf pada kata khayalan "112223". Angka, huruf, dan bola berwarna
adalah pakaian yang berbeda untuk satu persoalan yang sama — dan mengenalinya menghemat
banyak waktu di ujian.

**Periksa dengan kasus yang lebih kecil.** Dari angka $1,1,2$ rumusnya memberi
$\frac{3!}{2!} = 3$, dan memang hanya ada $112$, $121$, $211$.
