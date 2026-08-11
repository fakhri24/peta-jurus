---
id: cauchy-schwarz
nama: Ketaksamaan Cauchy-Schwarz
pilar: aljabar
tahap: osn
prasyarat: [am-gm]
contoh: [cs-contoh-1]
latihan: [cs-01, cs-02, cs-03, cs-04, cs-05, cs-06]
---

## Kapan dipakai

AM-GM sudah dicoba dan tidak memberi batas yang cukup ketat. Ciri khasnya: ada **jumlah
kuadrat dikali jumlah kuadrat**, atau kuadrat sebuah jumlah dibandingkan dengan keduanya.

Pemicu kedua, dan inilah bentuk yang paling sering muncul di OSN: ruas yang ditanya berupa
**jumlah pecahan dengan pembilang kuadrat** — $\sum \frac{a_i^2}{b_i}$. Bentuk Engel
menjawabnya dalam satu baris, dan mengenalinya lebih berharga daripada menghafal bentuk
bakunya.

Pemicu ketiga: soal memuat pecahan seperti $\frac{1}{a} + \frac{1}{b} + \frac{1}{c}$ dengan
$a+b+c$ diketahui. Pembilangnya bisa ditulis $1 = 1^2$, dan bentuk Engel berlaku — pemicu
yang mudah terlewat justru karena kuadratnya tidak terlihat.

Pemicu keempat: soal menuntut batas yang **kesamaannya tercapai saat peubahnya sebanding**,
bukan saat semuanya sama. Itu pembeda pokoknya dari AM-GM, dan sering satu-satunya cara
memilih di antara keduanya sebelum mencoba.

Pemicu kelima: ada **dua barisan bilangan** yang dipasangkan dan hasil kalinya dijumlahkan.
Bentuk $\sum a_i b_i$ adalah sisi kiri ketaksamaan ini apa adanya.

## Intinya

$$\left(\sum a_i b_i\right)^2 \ \le\ \left(\sum a_i^2\right)\left(\sum b_i^2\right)$$

dengan kesamaan tepat ketika kedua barisan **sebanding** — yaitu ada $\lambda$ dengan
$a_i = \lambda b_i$ untuk semua $i$.

Bentuk yang paling sering langsung dipakai di olimpiade adalah **bentuk Engel**, kadang
disebut lema Titu:

$$\frac{a_1^2}{b_1} + \frac{a_2^2}{b_2} + \cdots + \frac{a_n^2}{b_n}
\ \ge\ \frac{\left(a_1 + a_2 + \cdots + a_n\right)^2}{b_1 + b_2 + \cdots + b_n}$$

untuk $b_i > 0$. Begitu kamu melihat jumlah pecahan berpembilang kuadrat, ini gerakan
pertama.

Bedanya dengan AM-GM layak diingat: AM-GM menukar jumlah dengan hasil kali, sedangkan
Cauchy-Schwarz menukar **jumlah hasil kali** dengan hasil kali jumlah. Kalau soalnya
memuat kendala berbentuk jumlah dan yang ditanya juga jumlah, Cauchy-Schwarz biasanya
lebih cocok.

Menyiapkan bentuknya adalah bagian tersulit. Sering satu suku perlu ditulis ulang, misalnya
$a = \dfrac{a^2}{a}$, supaya bentuk Engel bisa dipasang.

## Jebakan umum

- **Memakai bentuk Engel dengan penyebut tak positif.** Syarat $b_i > 0$ wajib.
- **Salah memasangkan $a_i$ dan $b_i$.** Pemasangan yang keliru tetap memberi ketaksamaan
  yang benar, tetapi batasnya tidak berguna.
- **Lupa memeriksa kesamaan.** Syaratnya kesebandingan, bukan kesamaan seperti pada AM-GM.
