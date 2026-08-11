---
id: ketaksamaan-dasar
nama: Ketaksamaan Dasar
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: [kt-contoh-1]
latihan: [kt-01, kt-02, kt-03, kt-04, kt-05, kt-06]
---

## Kapan dipakai

Soal meminta **nilai terbesar atau terkecil**, atau meminta membuktikan satu bentuk tidak
pernah melebihi bentuk lain. Tanda $\ge$ atau $\le$ di soal yang harus dibuktikan itu
pemicu paling terang di seluruh aljabar.

Pemicu kedua: bentuknya bisa ditulis sebagai **jumlah kuadrat**. Begitu satu ruas menjadi
$(a-b)^2 + (b-c)^2 + \ldots$, ketaksamaannya selesai — dan syarat kesamaannya ikut terbaca
langsung dari kapan tiap kuadrat bernilai nol.

Pemicu ketiga: soal memuat **selisih yang dikuadratkan tanpa disebut** — $a^2 + b^2$
dibandingkan dengan $2ab$, atau $\frac ab + \frac ba$ dibandingkan dengan $2$. Keduanya
$(a-b)^2 \ge 0$ yang ditulis ulang.

Pemicu keempat: soal meminta membuktikan sebuah bentuk **selalu tak negatif** untuk semua
nilai peubahnya. Melengkapkan kuadrat menjawabnya, dan kalau tidak bisa, biasanya
pernyataannya memang salah.

Bedakan dari Ketaksamaan AM-GM: kalau yang tetap adalah jumlah atau hasil kalinya, dan yang
lain ditanyakan, itu AM-GM. Di sini yang dipakai kuadrat, bukan rata-rata.

## Intinya

Satu fakta yang menjadi dasar hampir semua ketaksamaan aljabar:

$$x^2 \ge 0 \quad \text{untuk setiap } x \text{ real}$$

dengan kesamaan tepat ketika $x = 0$. Semua yang lain dibangun dari situ.

Contoh terpenting, dan yang paling sering langsung dipakai:

$$a^2 + b^2 \ge 2ab$$

sebab selisihnya $(a-b)^2 \ge 0$. Untuk $a, b > 0$, membaginya dengan $ab$ memberi

$$\frac{a}{b} + \frac{b}{a} \ge 2$$

Aturan kerjanya selalu sama: **pindahkan semuanya ke satu ruas, lalu tunjukkan sisanya
jumlah kuadrat.** Kalau berhasil, ketaksamaannya terbukti sekaligus dengan syarat
kesamaannya.

Sifat operasi yang harus dijaga:

- Menambah bilangan apa pun tidak mengubah arah.
- Mengalikan dengan bilangan **positif** tidak mengubah arah; dengan **negatif**,
  arahnya berbalik.
- Mengkuadratkan hanya aman kalau kedua ruas tak negatif.

## Jebakan umum

- **Mengalikan dengan sesuatu yang belum diketahui tandanya.** Kalau tandanya belum
  dipastikan, arah ketaksamaannya tidak bisa dipertahankan.
- **Lupa menyebut kapan kesamaan tercapai.** Soal nilai maksimum belum selesai sebelum
  ditunjukkan nilai itu benar-benar dicapai.
- **Membalik ketaksamaan saat mengambil kebalikan** tanpa memastikan keduanya sepositif.
