---
id: eks-02
sumber: Latihan 2 — susunan sendiri, gaya OSN
pilar: kombinatorika
tahap: osn
jurus: [ekstremal]
bentuk: uraian
kesulitan: 4
---

## Soal

Sebanyak $n$ orang duduk mengelilingi meja bundar. Setiap orang memegang sejumlah permen,
dan seluruhnya berjumlah $S$ permen.

Buktikan bahwa selalu ada seseorang yang memegang permen **tidak lebih sedikit** daripada
rata-rata $\frac{S}{n}$, dan selalu ada seseorang yang memegang **tidak lebih banyak**
daripada rata-rata itu.

Buktikan dengan prinsip ekstremal — bukan dengan pengandaian dan pertentangan.

## Petunjuk

- Pilih orang yang memegang permen **terbanyak**, dan orang yang memegang permen **paling sedikit**.
- Kalau seseorang memegang permen terbanyak, bagaimana jumlah seluruh permen dibandingkan dengan $n$ kali jumlah yang ia pegang?
- Ketidaksamaan itu langsung memberi kesimpulan yang diminta setelah dibagi $n$.

## Pembahasan

Sebut $a_1, a_2, \dots, a_n$ banyaknya permen tiap orang, sehingga

$$a_1 + a_2 + \cdots + a_n = S$$

### Bagian 1 — ada yang tidak kurang dari rata-rata

**Pilih orang yang memegang terbanyak.** Himpunan $\{a_1,\dots,a_n\}$ berhingga dan tidak
kosong, sehingga punya anggota terbesar. Sebut $a_M = \max_i a_i$.

Karena $a_M$ terbesar, tiap suku tidak melebihinya:

$$a_i \le a_M \qquad \text{untuk setiap } i$$

Jumlahkan atas seluruh $i$:

$$S = \sum_{i=1}^{n} a_i \ \le\ \sum_{i=1}^{n} a_M = n\,a_M$$

Bagi dengan $n > 0$:

$$a_M \ \ge\ \frac{S}{n}$$

Jadi orang yang memegang permen terbanyak memegang tidak kurang dari rata-rata.

### Bagian 2 — ada yang tidak lebih dari rata-rata

**Pilih orang yang memegang paling sedikit,** sebut $a_m = \min_i a_i$. Dengan alasan yang
sama:

$$a_i \ge a_m \quad\Longrightarrow\quad S \ge n\,a_m \quad\Longrightarrow\quad
a_m \le \frac{S}{n}$$

$\blacksquare$

### Mengapa keterangan "mengelilingi meja bundar" tidak dipakai

Buktinya sama sekali tidak menyentuh susunan tempat duduk. Yang dipakai hanyalah bahwa
banyaknya orang berhingga dan jumlah permennya $S$. Keterangan tentang meja bundar adalah
kelebihan yang sengaja dipasang.

Mengenali data yang tidak menentukan adalah bagian dari mengerjakan soal olimpiade — dan
kebiasaan memakai setiap keterangan yang diberikan sering justru menyesatkan.

### Mengapa cara ini lebih baik daripada pengandaian

Bukti lewat pertentangan juga bisa: andaikan semua orang memegang **kurang** dari rata-rata,
maka $S < n \cdot \frac{S}{n} = S$, mustahil.

Cara itu benar, tetapi cara ekstremal memberi lebih banyak — ia **menunjuk siapa** orangnya,
yaitu yang memegang terbanyak. Pada soal yang meminta membangun sesuatu, keterangan itu yang
biasanya dipakai di langkah berikutnya.

### Akibat yang sering dipakai

Bentuk yang paling sering muncul di soal olimpiade: kalau $n$ benda dibagi ke dalam beberapa
kelompok, selalu ada kelompok yang isinya paling sedikit rata-rata, dan selalu ada yang
paling banyak rata-rata.

Karena banyaknya benda bilangan bulat, kesimpulannya sering diperkuat menjadi

$$a_M \ \ge\ \left\lceil \frac{S}{n} \right\rceil, \qquad
a_m \ \le\ \left\lfloor \frac{S}{n} \right\rfloor$$

dan bentuk itu persis prinsip sarang merpati.

## Rubrik

- Memilih anggota terbesar, dan menyebut alasan keberadaannya (himpunan berhingga tak kosong)
- Menyatakan $a_i \le a_M$ untuk setiap $i$
- Menjumlahkan menjadi $S \le n\,a_M$ lalu membagi $n$
- Mengerjakan bagian minimum dengan alasan yang setara
- Menyatakan keterangan meja bundar tidak dipakai
- Menyimpulkan kedua bagian dengan lengkap
