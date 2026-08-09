---
id: pbr-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [permutasi-berulang]
bentuk: isian
kesulitan: 1
jawaban: "12"
---

## Soal

Ada berapa susunan huruf berbeda yang dapat dibentuk dari seluruh huruf pada kata
**BUKU**?

## Petunjuk

- Kata ini punya empat huruf, tetapi tidak seluruhnya berbeda. Periksa huruf mana yang muncul lebih dari sekali.
- Kalau keempat huruf dianggap berbeda, tiap susunan akan terhitung lebih dari sekali.
- Bagi dengan banyaknya cara menukar huruf yang kembar itu.

## Pembahasan

**Daftar hurufnya.** B, U, K, U — jadi $4$ huruf dengan U muncul $2$ kali dan huruf lain
sekali.

**Anggap dulu semua berbeda:**

$$4! = 24$$

**Perbaiki.** Setiap susunan sungguhan terhitung dua kali, sebab kedua U dapat ditukar tanpa
mengubah apa pun:

$$\frac{4!}{2!} = \frac{24}{2} = \boxed{12}$$

**Periksa dengan mendaftar seluruhnya.** Kata ini cukup kecil untuk ditulis lengkap:

$$\text{BUKU},\ \text{BUUK},\ \text{BKUU},\ \text{UBKU},\ \text{UBUK},\ \text{UKBU}$$

$$\text{UKUB},\ \text{UUBK},\ \text{UUKB},\ \text{KBUU},\ \text{KUBU},\ \text{KUUB}$$

Tepat $12$ susunan.

**Melihat langsung mengapa pembaginya $2$.** Beri tanda sementara pada kedua U menjadi
$U_1$ dan $U_2$. Susunan $B\,U_1\,K\,U_2$ dan $B\,U_2\,K\,U_1$ terhitung sebagai dua hal
berbeda di dalam $4! = 24$ — padahal begitu tandanya dihapus, keduanya sama-sama BUKU.
Setiap susunan punya tepat dua salinan seperti ini, jadi $24$ harus dibagi $2$.

**Bandingkan dengan kata tanpa huruf kembar.** Kata BUKA juga punya empat huruf, tetapi
seluruhnya berbeda, sehingga susunannya $4! = 24$ — dua kali lipat. Satu huruf kembar saja
sudah memangkas jawabannya menjadi setengah.
