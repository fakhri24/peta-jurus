---
id: fpb-01
sumber: Latihan 1 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [fungsi-pembangkit]
bentuk: isian
kesulitan: 3
jawaban: "16"
---

## Soal

Tentukan koefisien $x^{5}$ pada penjabaran

$$\left(1 + x + x^{2}\right)^{4}$$

## Petunjuk

- Menjabarkan seluruhnya terlalu panjang. Bacalah bentuk ini sebagai soal pencacahan.
- Koefisien $x^5$ menghitung banyaknya cara memilih satu suku dari tiap kurung sehingga pangkatnya berjumlah $5$.
- Itu sama dengan mencacah penyelesaian $e_1+e_2+e_3+e_4 = 5$ dengan tiap $e_i \in \{0,1,2\}$.

## Pembahasan

**Baca sebagai soal pencacahan.** Menjabarkan $\left(1+x+x^2\right)^4$ berarti memilih satu
suku dari masing-masing empat kurung, lalu mengalikannya. Kalau dari kurung ke-$i$ dipilih
$x^{e_i}$ dengan $e_i \in \{0,1,2\}$, sumbangannya adalah $x^{e_1+e_2+e_3+e_4}$.

Maka koefisien $x^5$ adalah banyaknya penyelesaian

$$e_1 + e_2 + e_3 + e_4 = 5, \qquad e_i \in \{0,1,2\}$$

**Hitung dengan inklusi–eksklusi.** Tanpa batas atas, banyaknya penyelesaian tak negatif:

$$\binom{5+4-1}{4-1} = \binom83 = 56$$

Kurangi yang melanggar, yaitu yang punya suatu $e_i \ge 3$. Untuk satu $i$ tertentu, geser
$e_i' = e_i - 3$ sehingga jumlahnya menjadi $2$:

$$\binom{2+4-1}{4-1} = \binom53 = 10$$

Ada $4$ pilihan $i$, memberi $4 \times 10 = 40$.

Dua pelanggaran sekaligus menuntut jumlah paling sedikit $3+3 = 6 > 5$, jadi **mustahil** —
irisannya kosong dan tidak ada koreksi lebih lanjut.

$$56 - 40 = \boxed{16}$$

**Periksa dengan simetri.** Penjabaran $\left(1+x+x^2\right)^4$ berderajat $8$, dan
koefisiennya simetris terhadap suku tengah — sebab mengganti tiap $e_i$ dengan $2-e_i$
memetakan jumlah $s$ menjadi $8-s$. Karena itu koefisien $x^5$ sama dengan koefisien $x^3$.

Daftar lengkap koefisiennya:

$$1,\ 4,\ 10,\ 16,\ 19,\ 16,\ 10,\ 4,\ 1$$

Jumlahnya $81 = 3^4$, sesuai substitusi $x = 1$. Koefisien $x^5$ memang $16$, dan simetri
terhadap suku tengah $19$ juga terlihat.

**Mengapa memeriksa irisan itu perlu.** Kalau ruas kanannya lebih besar — misalnya
koefisien $x^{6}$ — dua pelanggaran sekaligus menjadi mungkin, dan mengurangkan begitu saja
akan membuang terlalu banyak. Batas "kapan pelanggaran ganda mungkin" harus selalu diperiksa,
bukan diandaikan.
