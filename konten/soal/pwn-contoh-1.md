---
id: pwn-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: uraian
kesulitan: 3
---

## Soal

Dari sebuah papan catur $8 \times 8$, dua petak di **sudut yang berlawanan** dibuang —
misalnya pojok kiri atas dan pojok kanan bawah. Tersisa $62$ petak.

Buktikan bahwa sisa papan itu **tidak dapat** ditutup seluruhnya oleh $31$ domino
$1 \times 2$.

## Petunjuk

- Menghitung petaknya saja tidak cukup: $62 = 31 \times 2$, jadi tidak ada yang bertentangan di situ. Cari besaran lain.
- Warnai papannya seperti papan catur, lalu perhatikan warna apa saja yang ditutup sebuah domino, di mana pun ia diletakkan.
- Periksa warna kedua petak sudut yang dibuang. Keduanya sewarna atau berbeda?

## Pembahasan

**Mengapa hitungan petak tidak cukup.** Sisa papan punya $62$ petak, dan $31$ domino
menutupi $62$ petak. Angkanya cocok, jadi kalau hanya itu yang diperiksa, penutupan seolah
mungkin. Dibutuhkan besaran yang lebih halus.

**Warnai papannya.** Beri warna hitam dan putih berselang-seling seperti papan catur.
Papan $8 \times 8$ penuh punya

$$32 \text{ petak hitam}, \qquad 32 \text{ petak putih}$$

**Perhatikan apa yang ditutup sebuah domino.** Domino $1 \times 2$ selalu menutupi dua petak
yang **bersebelahan** — mendatar maupun tegak. Pada pewarnaan papan catur, dua petak
bersebelahan selalu berbeda warna. Maka:

> Di mana pun diletakkan dan bagaimana pun arahnya, sebuah domino menutup tepat **satu petak
> hitam dan satu petak putih.**

Inilah syarat yang membuat pewarnaannya berguna: jumlah warna yang ditutup tiap ubin
**tetap**, tidak bergantung pada peletakannya.

**Akibatnya untuk penutupan penuh.** Kalau $31$ domino menutup seluruh sisa papan, maka
petak yang tertutup terdiri atas

$$31 \text{ hitam} \quad \text{dan} \quad 31 \text{ putih}$$

**Periksa persediaan warnanya.** Kedua petak sudut yang berlawanan pada papan catur selalu
**sewarna** — sebut saja keduanya hitam. Setelah dibuang, sisa papan punya

$$32 - 2 = 30 \text{ petak hitam}, \qquad 32 \text{ petak putih}$$

**Simpulkan.** Penutupan menuntut $31$ hitam, sedangkan yang tersedia hanya $30$. Karena itu
penutupan mustahil. $\blacksquare$

### Mengapa kedua sudut berlawanan pasti sewarna

Beri koordinat $(i,j)$ dengan $1 \le i,j \le 8$, dan warnai menurut paritas $i+j$. Pojok
kiri atas $(1,1)$ punya $i+j = 2$; pojok kanan bawah $(8,8)$ punya $i+j = 16$. Keduanya
genap, jadi sewarna.

Sebaliknya $(1,1)$ dan $(1,8)$ — dua sudut yang **berdekatan** — punya $i+j$ bernilai $2$
dan $9$, sehingga berbeda warna. Perbedaan itu yang membuat soal berubah sama sekali kalau
sudut yang dibuang bukan yang berlawanan.

### Arah kesimpulan yang harus dijaga

Bukti ini menunjukkan penutupan **tidak mungkin**. Ia tidak — dan tidak bisa — menunjukkan
bahwa papan yang hitungan warnanya cocok pasti bisa ditutup. Hitungan warna yang cocok
hanya berarti tidak ada halangan **dari pewarnaan itu**; halangan lain bisa saja ada.

Pewarnaan pada dasarnya adalah invarian yang dipilih dengan sengaja: yang kekal adalah
selisih antara warna yang dituntut ubin dan warna yang tersedia papan.

## Rubrik

- Menyatakan bahwa hitungan petak saja tidak cukup, sebab $62 = 31\times2$ tidak bertentangan
- Mewarnai papan seperti papan catur dan menyebut $32$ petak tiap warna
- Menyatakan tiap domino menutup tepat satu petak tiap warna, **di mana pun diletakkan**
- Menyimpulkan penutupan penuh menuntut $31$ petak tiap warna
- Menunjukkan kedua sudut berlawanan sewarna, misalnya lewat paritas $i+j$
- Menghitung persediaan sisa $30$ dan $32$, lalu menyimpulkan pertentangannya
