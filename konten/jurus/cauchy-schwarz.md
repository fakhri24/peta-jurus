---
id: cauchy-schwarz
nama: Ketaksamaan Cauchy-Schwarz
pilar: aljabar
tahap: osn
prasyarat: [am-gm]
contoh: []
latihan: []
---

## Kapan dipakai

AM-GM sudah dicoba dan tidak memberi batas yang cukup ketat. Ciri khasnya: ada **jumlah
kuadrat** dikali jumlah kuadrat, atau pecahan berbentuk $\dfrac{a_i^2}{b_i}$.

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
