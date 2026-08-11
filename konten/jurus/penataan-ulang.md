---
id: penataan-ulang
nama: Ketaksamaan Penataan Ulang
pilar: aljabar
tahap: osn
prasyarat: [am-gm]
contoh: [pu-contoh-1]
latihan: [pu-01, pu-02, pu-03, pu-04, pu-05, pu-06]
---

## Kapan dipakai

Ada dua barisan bilangan dan soal membandingkan **jumlah hasil kali berpasangan** pada
urutan yang berbeda-beda. Kata "permutasi", "urutan", atau "dipasangkan" di soal ketaksamaan
itu pemicu langsung.

Pemicu kedua, dan inilah yang membuatnya sering menjadi kunci: ketaksamaannya **tidak
simetris penuh melainkan siklik** — $\frac{a}{b} + \frac{b}{c} + \frac{c}{a}$. AM-GM
memperlakukan semua suku sama dan karena itu sering memberi batas yang terlalu longgar; di
sini urutannya justru yang dipakai.

Pemicu ketiga: soal mengizinkan **menganggap $a \ge b \ge c$** tanpa kehilangan keumuman.
Kalimat itu sendiri tanda bahwa jurus ini yang dimaksud, sebab urutan baru berarti sesudah
ada yang diurutkan.

Pemicu keempat: soal meminta **nilai terbesar atau terkecil sebuah penataan** — bagaimana
memasangkan dua deret angka agar jumlah hasil kalinya paling besar. Jawabannya searah untuk
terbesar, berlawanan arah untuk terkecil, dan tidak perlu satu pun penataan dicoba.

Ketaksamaan Chebyshev adalah akibat langsungnya, jadi soal yang membandingkan rata-rata
hasil kali dengan hasil kali rata-rata juga bermuara ke sini.

## Intinya

Misalkan $a_1 \le a_2 \le \cdots \le a_n$ dan $b_1 \le b_2 \le \cdots \le b_n$. Maka di
antara semua cara memasangkan kedua barisan,

$$\underbrace{\sum a_i b_i}_{\text{searah}} \ \ge\ \sum a_i b_{\sigma(i)}
\ \ge\ \underbrace{\sum a_i b_{n+1-i}}_{\text{berlawanan arah}}$$

untuk permutasi $\sigma$ apa pun.

Kalimatnya: **pasangkan besar dengan besar untuk hasil terbesar; besar dengan kecil untuk
hasil terkecil.** Itu saja isinya, dan ia jauh lebih sering berguna daripada yang terlihat.

Akibat langsung yang sering dipakai — **ketaksamaan Chebyshev**: kalau kedua barisan
terurut searah,

$$\frac{1}{n}\sum a_i b_i \ \ge\ \left(\frac{1}{n}\sum a_i\right)\left(\frac{1}{n}\sum b_i\right)$$

Untuk ketaksamaan simetris, gerakan bakunya: **andaikan tanpa mengurangi keumuman**
$a \ge b \ge c$. Kesimetrian soal membuat pengandaian itu sah, dan setelah urutannya
tetap, penataan ulang bisa dipasang.

## Jebakan umum

- **Lupa mengurutkan.** Ketaksamaannya berbicara tentang barisan **terurut**; tanpa itu
  pernyataannya tidak bermakna.
- **Mengklaim "tanpa mengurangi keumuman" pada bentuk yang tidak simetris.** Kalau menukar
  peubah mengubah soal, pengandaian urutan tidak sah.
- **Memakainya pada barisan yang tandanya campur** tanpa memeriksa akibatnya terhadap arah.
