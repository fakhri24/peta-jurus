---
id: fkt-06
sumber: Latihan 6 — susunan sendiri, gaya OSN-K
pilar: aljabar
tahap: osn-k
jurus: [faktorisasi]
bentuk: uraian
kesulitan: 3
---

## Soal

Buktikan bahwa $n^4 + 4$ bukan bilangan prima untuk setiap bilangan asli $n > 1$.

## Petunjuk

- Sebuah bilangan bukan prima kalau ia bisa ditulis sebagai hasil kali dua bilangan yang keduanya lebih dari $1$. Carilah penulisan semacam itu.
- Bentuk $n^4+4$ tidak terlihat bisa difaktorkan — sampai kamu menambahkan lalu mengurangkan sesuatu. Coba lengkapkan menjadi kuadrat sempurna.
- $n^4 + 4 = \left(n^2+2\right)^2 - (2n)^2$, dan itu selisih kuadrat.

## Pembahasan

Bentuknya tidak punya faktor yang terlihat, jadi ciptakan satu dengan **menambah lalu
mengurangkan** suku yang sama:

$$n^4 + 4 = n^4 + 4n^2 + 4 - 4n^2$$

Tiga suku pertama membentuk kuadrat sempurna:

$$= \left(n^2 + 2\right)^2 - (2n)^2$$

Sekarang bentuknya selisih kuadrat, jadi bisa difaktorkan:

$$n^4 + 4 = \left(n^2 + 2 - 2n\right)\left(n^2 + 2 + 2n\right)$$

**Tunjukkan kedua faktornya lebih dari $1$.** Ini langkah yang menutup pembuktian —
faktorisasi saja belum membuktikan apa-apa kalau salah satu faktornya bisa bernilai $1$.

Faktor kedua jelas besar: untuk $n \ge 1$,

$$n^2 + 2n + 2 \ge 1 + 2 + 2 = 5 > 1$$

Faktor pertama perlu sedikit kerja. Lengkapkan kuadratnya:

$$n^2 - 2n + 2 = (n-1)^2 + 1$$

Untuk $n > 1$ berlaku $(n-1)^2 \ge 1$, sehingga

$$n^2 - 2n + 2 \ge 2 > 1$$

Jadi $n^4+4$ tertulis sebagai hasil kali dua bilangan asli yang masing-masing lebih dari
$1$, sehingga ia komposit. $\blacksquare$

Syarat $n > 1$ tidak bisa dibuang. Untuk $n = 1$ diperoleh $n^4 + 4 = 5$, yang prima —
dan di situ faktor pertamanya bernilai $(1-1)^2 + 1 = 1$, tepat kasus yang dikecualikan.

Contohnya untuk $n = 2$: $16 + 4 = 20 = 2 \times 10$, dan memang $n^2-2n+2 = 2$ serta
$n^2+2n+2 = 10$.

Faktorisasi ini dikenal sebagai **identitas Sophie Germain**, dan bentuk umumnya

$$a^4 + 4b^4 = \left(a^2 - 2ab + 2b^2\right)\left(a^2 + 2ab + 2b^2\right)$$

## Rubrik

- Menambah dan mengurangkan $4n^2$ untuk membentuk kuadrat sempurna
- Mengenali hasilnya sebagai selisih kuadrat $\left(n^2+2\right)^2 - (2n)^2$
- Menuliskan faktorisasinya secara eksplisit
- Membuktikan faktor kedua lebih dari $1$
- Membuktikan faktor pertama lebih dari $1$, misalnya lewat $(n-1)^2 + 1$ — langkah ini yang menutup pembuktian
- Menyebut bahwa syarat $n > 1$ diperlukan, dengan $n = 1$ sebagai kasus yang gagal
