---
id: pbr-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 2
jawaban: "151200"
---

## Soal

Ada berapa susunan huruf berbeda yang dapat dibentuk dari seluruh huruf pada kata

$$\textbf{MATEMATIKA}$$

## Petunjuk

- Hitung dulu ada berapa huruf seluruhnya, lalu daftar berapa kali tiap huruf muncul.
- Kalau seluruh hurufnya dianggap berbeda, hasilnya kelebihan — sebab menukar dua huruf yang sama tidak menghasilkan susunan baru.
- Untuk tiap huruf yang berulang, bagi dengan banyaknya cara menukar-nukar huruf itu di antara mereka sendiri.

## Pembahasan

**Daftar hurufnya lebih dulu.** Ini langkah yang tidak boleh dikerjakan tergesa-gesa:

| Huruf | M | A | T | E | I | K |
|---|---|---|---|---|---|---|
| Banyaknya | $2$ | $3$ | $2$ | $1$ | $1$ | $1$ |

Jumlahkan untuk memeriksa: $2+3+2+1+1+1 = 10$. Kata MATEMATIKA memang terdiri atas $10$
huruf. **Selalu lakukan pemeriksaan ini** — salah menghitung berapa kali sebuah huruf
muncul adalah kekeliruan yang paling sering di soal jenis ini.

**Anggap dulu semua huruf berbeda.** Kalau kedua M dibedakan menjadi $M_1, M_2$ dan
seterusnya, susunannya ada

$$10! = 3\,628\,800$$

**Perbaiki kelebihannya.** Sebuah susunan sungguhan, misalnya MATEMATIKA itu sendiri,
terhitung berkali-kali di angka tadi — tepat sebanyak cara menukar-nukar huruf yang sama
di antara mereka sendiri:

$$2! \text{ untuk M}, \qquad 3! \text{ untuk A}, \qquad 2! \text{ untuk T}$$

Huruf yang muncul sekali menyumbang $1! = 1$, jadi tidak berpengaruh.

$$\frac{10!}{2!\,3!\,2!} = \frac{3\,628\,800}{2 \times 6 \times 2}
= \frac{3\,628\,800}{24} = \boxed{151200}$$

**Mengapa pembaginya dikalikan, bukan dijumlahkan.** Penukaran huruf M dan penukaran huruf
A dapat dilakukan **bersamaan** — tiap susunan kedua M dapat dipadankan dengan tiap susunan
ketiga A. Jadi banyaknya salinan tiap susunan adalah $2! \times 3! \times 2!$, bukan
$2!+3!+2!$.

**Periksa pada kata yang cukup kecil untuk didaftar.** Kata BUKU punya $4$ huruf dengan U
sebanyak dua, jadi rumusnya memberi $\frac{4!}{2!} = 12$. Mendaftar seluruhnya memang
memberi $12$ susunan — bukan $24$, sebab menukar kedua U tidak mengubah apa pun.
