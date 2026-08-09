---
id: pwn-04
sumber: Latihan 4 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [pewarnaan]
bentuk: uraian
kesulitan: 5
---

## Soal

Buktikan bahwa papan $8 \times 8$ **tidak dapat** ditutup seluruhnya oleh $15$ ubin
berbentuk T (tetromino T, yaitu empat petak berbentuk huruf T) ditambah satu ubin persegi
$2 \times 2$.

(Perhatikan $15 \times 4 + 4 = 64$, jadi hitungan petaknya cocok.)

## Petunjuk

- Hitungan petak cocok, jadi harus dicari besaran lain. Warnai papannya seperti papan catur.
- Periksa berapa petak hitam yang ditutup sebuah ubin T. Berbeda dari domino, angkanya **tidak** tetap — tetapi selisih hitam dan putihnya punya sifat yang tetap.
- Jumlahkan selisih itu atas seluruh ubin, dan bandingkan dengan selisih pada papan penuh.

## Pembahasan

**Warnai papannya** seperti papan catur: $32$ petak hitam dan $32$ petak putih.

**Periksa ubin T.** Sebuah tetromino T menutupi empat petak: tiga berjajar dan satu menonjol
di tengah. Petak yang menonjol bersebelahan dengan petak tengah, sehingga warnanya berlawanan
dengan petak tengah.

Tiga petak berjajar berwarna selang-seling, jadi terdiri atas dua petak sewarna dengan
ujungnya dan satu petak di tengah yang berlawanan. Menambahkan petak yang menonjol — sewarna
dengan kedua ujung — memberi

$$3 \text{ petak satu warna}, \qquad 1 \text{ petak warna lain}$$

Warna mana yang bertiga bergantung pada peletakannya, tetapi **selisihnya selalu**

$$\pm 2$$

**Periksa ubin persegi $2\times2$.** Ia menutupi dua petak hitam dan dua putih di mana pun
diletakkan, sehingga selisihnya

$$0$$

**Jumlahkan selisihnya.** Sebut $s_i \in \{+2, -2\}$ selisih hitam dikurangi putih untuk
ubin T ke-$i$. Kalau seluruh papan tertutup, jumlah seluruh selisih harus sama dengan
selisih pada papan penuh, yaitu $32 - 32 = 0$:

$$\sum_{i=1}^{15} s_i + 0 = 0$$

**Turunkan pertentangannya.** Bagi persamaan itu dengan $2$:

$$\sum_{i=1}^{15} \frac{s_i}{2} = 0, \qquad \frac{s_i}{2} \in \{+1, -1\}$$

Jadi $15$ bilangan yang masing-masing $+1$ atau $-1$ harus berjumlah nol. Itu menuntut
banyaknya $+1$ sama dengan banyaknya $-1$, sehingga $15$ harus **genap**.

Tetapi $15$ ganjil. Bertentangan. Maka penutupan semacam itu mustahil. $\blacksquare$

### Cara lain menyatakan langkah terakhir

Jumlah $15$ bilangan ganjil selalu ganjil, sedangkan $0$ genap. Karena tiap
$\frac{s_i}{2}$ bernilai $\pm1$ yang ganjil, jumlahnya tidak mungkin nol.

Kedua cara itu sama; yang penting adalah menyandarkan kesimpulan pada **paritas banyaknya
ubin**, bukan pada nilai selisihnya.

### Apa yang berbeda dari soal domino

Pada domino, jumlah warna yang ditutup tiap ubin benar-benar tetap: selalu satu dan satu.
Pada ubin T, jumlahnya **tidak** tetap — bisa tiga hitam atau tiga putih. Sekilas ini
membuat pewarnaan tidak berguna.

Yang menyelamatkan adalah menemukan besaran yang tetap pada tingkat yang lebih longgar:
bukan warna yang ditutup, melainkan **paritas selisihnya**. Tiap ubin T menyumbang selisih
ganjil setelah dibagi dua, dan itu cukup untuk menutup kemungkinan.

Menaikkan tingkat kelonggaran seperti ini — dari "tetap" ke "tetap paritasnya" — adalah
langkah yang sama dengan yang dipakai pada invarian, dan ia yang membuat pewarnaan berlaku
jauh melampaui domino.

## Rubrik

- Menyatakan hitungan petak cocok sehingga dibutuhkan besaran lain
- Mewarnai papan seperti papan catur, menyebut $32$ petak tiap warna
- Menunjukkan ubin T menutup tiga petak satu warna dan satu petak warna lain, dengan alasan letak petak yang menonjol
- Menyatakan selisih ubin T selalu $\pm2$, meskipun warna mana yang bertiga tidak tetap
- Menyatakan ubin $2\times2$ berselisih $0$
- Menyusun persamaan jumlah selisih sama dengan nol
- Menurunkan pertentangan lewat paritas: $15$ bilangan $\pm1$ tidak mungkin berjumlah nol
