---
id: kbn-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [koefisien-binomial]
bentuk: isian
kesulitan: 2
jawaban: "1"
---

## Soal

Tentukan **jumlah seluruh koefisien** pada penjabaran

$$(2x - 3)^{4}$$

## Petunjuk

- Jangan menjabarkan satu per satu lalu menjumlahkannya. Ada jalan pintas yang selalu berlaku.
- Kalau penjabarannya ditulis $a_0 + a_1x + a_2x^2 + \cdots$, apa yang terjadi kalau $x$ diganti $1$?
- Substitusikan $x = 1$ ke bentuk aslinya, dan hitung.

## Pembahasan

**Jalan pintasnya.** Tulis penjabarannya sebagai

$$(2x-3)^4 = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4$$

Substitusikan $x = 1$. Setiap $x^j$ menjadi $1$, sehingga ruas kanan menjadi persis jumlah
seluruh koefisiennya:

$$a_0 + a_1 + a_2 + a_3 + a_4$$

Sementara ruas kirinya

$$(2 \cdot 1 - 3)^4 = (-1)^4 = \boxed{1}$$

**Periksa dengan menjabarkan.** Bentuk ini cukup kecil untuk diperiksa penuh:

$$(2x-3)^4 = 16x^4 - 96x^3 + 216x^2 - 216x + 81$$

Jumlahkan koefisiennya:

$$16 - 96 + 216 - 216 + 81 = 1$$

Cocok — dan perbandingan itu memperlihatkan berapa banyak kerja yang dihemat jalan pintas
tadi.

**Substitusi nilai adalah alat baku pada soal koefisien.** Beberapa yang sering dipakai:

| Yang dicari | Substitusi |
|---|---|
| Jumlah seluruh koefisien | $x = 1$ |
| Jumlah berselang-seling $a_0 - a_1 + a_2 - \cdots$ | $x = -1$ |
| Suku konstan $a_0$ | $x = 0$ |

Menggabungkan dua yang pertama memberi lebih banyak lagi. Untuk penjabaran ini,
$x = -1$ memberi $(-5)^4 = 625$, sehingga

$$\text{jumlah koefisien pangkat genap} = \frac{1 + 625}{2} = 313$$

$$\text{jumlah koefisien pangkat ganjil} = \frac{1 - 625}{2} = -312$$

Periksa: $16 + 216 + 81 = 313$ dan $-96 - 216 = -312$. Cocok.

**Perhatikan tanda negatif tidak boleh dilupakan.** Menghitung $(2+3)^4 = 625$ adalah
kekeliruan yang paling sering di soal ini — yang disubstitusi adalah $x$, bukan tanda pada
bentuknya.
