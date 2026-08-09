---
id: pwn-06
sumber: Latihan 6 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: uraian
kesulitan: 5
---

## Soal

Buktikan bahwa papan $10 \times 10$ **tidak dapat** ditutup seluruhnya oleh ubin $1 \times 4$
(boleh diletakkan mendatar maupun tegak).

(Perhatikan $100 = 25 \times 4$, jadi hitungan petaknya cocok.)

## Petunjuk

- Hitungan petak cocok dan pewarnaan dua warna tidak akan menolong — sebuah ubin $1\times4$ selalu menutup dua petak tiap warna.
- Butuh pewarnaan dengan **empat** warna. Warnai petak $(i,j)$ menurut sisa $i+j$ dibagi $4$, lalu periksa apa yang ditutup sebuah ubin.
- Hitung persediaan tiap warna pada papan $10\times10$, dan periksa apakah keempatnya sama banyak.

## Pembahasan

**Mengapa dua warna gagal.** Ubin $1\times4$ menutup empat petak berjajar, yang pada
pewarnaan papan catur selalu berselang-seling: dua hitam dan dua putih. Selisihnya selalu
nol, dan papan penuh juga berselisih nol. Tidak ada yang bertentangan, jadi pewarnaan dua
warna tidak menutup apa pun.

**Pakai empat warna.** Beri koordinat $(i,j)$ dengan $1 \le i,j \le 10$, lalu warnai petak
itu dengan

$$w(i,j) = (i+j) \bmod 4 \ \in \{0,1,2,3\}$$

**Periksa apa yang ditutup sebuah ubin.**

- **Ubin mendatar** menempati $(i,j), (i,j+1), (i,j+2), (i,j+3)$. Nilai $i+j$ pada keempatnya
  adalah empat bilangan berurutan, sehingga sisanya modulo $4$ adalah $0,1,2,3$ dalam suatu
  urutan.
- **Ubin tegak** menempati $(i,j), (i+1,j), (i+2,j), (i+3,j)$. Nilai $i+j$ juga empat
  bilangan berurutan, dengan kesimpulan yang sama.

Jadi **di mana pun diletakkan dan bagaimana pun arahnya, sebuah ubin $1\times4$ menutup
tepat satu petak dari tiap warna.** Inilah syarat yang membuat pewarnaannya berguna.

**Akibatnya untuk penutupan penuh.** Kalau $25$ ubin menutup seluruh papan, tiap warna harus
tertutup tepat $25$ kali. Maka keempat warna wajib **sama banyaknya** di papan.

**Hitung persediaan tiap warna.** Hitung baris demi baris. Pada baris ke-$i$, nilai $i+j$
berjalan dari $i+1$ sampai $i+10$ — sepuluh bilangan berurutan.

Sepuluh bilangan berurutan memuat tiap sisa modulo $4$ sebanyak $\lfloor 10/4 \rfloor = 2$
kali, ditambah dua sisa tambahan dari dua bilangan terakhir yang tersisa. Jadi tiap baris
menyumbang $3$ petak untuk dua warna dan $2$ petak untuk dua warna lainnya.

Menjumlahkan atas kesepuluh baris, warna yang mendapat sumbangan $3$ bergeser dari baris ke
baris. Hasil akhirnya:

| Warna | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| Banyaknya petak | $25$ | $24$ | $25$ | $26$ |

Jumlahnya $25+24+25+26 = 100$, sesuai.

**Simpulkan.** Keempat warna tidak sama banyaknya — warna $3$ punya $26$ petak sedangkan
warna $1$ hanya $24$. Padahal penutupan penuh menuntut tiap warna tertutup tepat $25$ kali.
Bertentangan, sehingga penutupan mustahil. $\blacksquare$

Perhatikan bahwa cukup **satu** warna yang menyimpang untuk menutup kemungkinan. Warna $3$
saja sudah memberi pertentangannya: $25$ ubin tidak mungkin menutup $26$ petak berwarna
sama, sebab tiap ubin menyentuh warna itu tepat sekali.

### Bentuk umumnya

Hasil ini bagian dari kenyataan yang lebih luas: papan $a \times b$ dapat ditutup ubin
$1 \times k$ **tepat ketika** $k$ membagi $a$ atau $k$ membagi $b$.

Untuk $10 \times 10$ dengan $k = 4$: karena $4 \nmid 10$, penutupan mustahil — sesuai hasil
di atas. Untuk $8 \times 10$ dengan $k = 4$: karena $4 \mid 8$, penutupannya ada, dan mudah
disusun dengan meletakkan ubin mendatar sepanjang tiap baris.

### Pelajaran memilih banyaknya warna

Banyaknya warna dipilih dari **panjang ubinnya**, bukan dari papannya. Ubin sepanjang $k$
menuntut $k$ warna supaya tiap ubin menutup tepat satu petak dari tiap warna.

Karena itu dua warna berguna untuk domino, tiga warna untuk ubin $1\times3$, dan empat warna
di sini. Memakai dua warna untuk ubin $1\times4$ bukan kekeliruan hitung — ia hanya tidak
menghasilkan besaran yang bisa dipertentangkan.

## Rubrik

- Menyatakan pewarnaan dua warna tidak menolong, dengan alasan ubin $1\times4$ menutup dua petak tiap warna
- Menetapkan pewarnaan empat warna, misalnya $(i+j) \bmod 4$
- Menunjukkan ubin mendatar menutup tepat satu petak tiap warna
- Menunjukkan ubin tegak juga menutup tepat satu petak tiap warna
- Menyimpulkan penutupan penuh menuntut keempat warna sama banyaknya
- Menghitung persediaan tiap warna pada papan $10\times10$ dan menunjukkan tidak sama
- Menyimpulkan pertentangannya
