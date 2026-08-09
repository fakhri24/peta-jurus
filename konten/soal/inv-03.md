---
id: inv-03
sumber: Latihan 3 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [invarian]
bentuk: isian
kesulitan: 3
jawaban: "0"
---

## Soal

Sebuah kotak berisi $15$ bola putih dan $12$ bola hitam. Sebuah langkah terdiri atas
mengambil **dua** bola dari kotak, lalu memasukkan satu bola baru menurut aturan:

- kalau kedua bola yang diambil **sewarna**, masukkan satu bola **putih**;
- kalau **berbeda warna**, masukkan satu bola **hitam**.

Langkah diulang sampai tersisa satu bola. Ada berapa bola hitam yang tersisa?

## Petunjuk

- Perhatikan hanya banyaknya bola hitam, dan periksa bagaimana angka itu berubah pada tiap jenis pengambilan.
- Ada tiga jenis: dua putih, dua hitam, atau satu masing-masing. Periksa ketiganya.
- Angkanya berubah, tetapi selalu dengan bilangan genap.

## Pembahasan

**Periksa tiap jenis langkah.** Sebut $h$ banyaknya bola hitam.

| Yang diambil | Yang dimasukkan | Perubahan $h$ |
|---|---|---|
| putih, putih | putih | $0$ |
| hitam, hitam | putih | $-2$ |
| putih, hitam | hitam | $0$ |

Baris ketiga perlu diperiksa dengan hati-hati: satu bola hitam keluar, dan satu bola hitam
masuk. Perubahannya $-1 + 1 = 0$.

**Simpulkan invariannya.** Ketiga langkah mengubah $h$ sebesar $0$ atau $-2$, yaitu selalu
genap. Maka

$$h \bmod 2 \text{ kekal}$$

**Nilai awalnya.** Mula-mula $h = 12$, yang **genap**.

**Simpulkan.** Paritas $h$ tetap genap sampai akhir. Di akhir tersisa satu bola, sehingga
$h$ bernilai $0$ atau $1$. Karena harus genap,

$$h = \boxed{0}$$

Jadi bola terakhir berwarna putih.

**Perhatikan proses ini memang berakhir.** Tiap langkah mengambil dua bola dan memasukkan
satu, sehingga isi kotak berkurang tepat satu setiap kali. Dari $27$ bola, setelah $26$
langkah tersisa tepat satu. Banyaknya bola adalah **monovarian** — besaran yang selalu
menurun — dan karena ia bilangan asli, prosesnya tidak bisa berjalan selamanya.

Memeriksa hal ini bukan kelengkapan yang bisa dilewati. Kalau prosesnya tidak dijamin
berakhir, pertanyaan "bola terakhir apa" belum tentu punya jawaban.

**Bandingkan dengan soal sebelumnya.** Aturan tanda $+/-$ dan aturan bola putih/hitam
adalah **aturan yang sama persis**, hanya berganti nama: putih berlaku seperti $+$, hitam
seperti $-$. Yang berbeda cuma bilangan awalnya — $15$ tanda $-$ yang ganjil di sana, $12$
bola hitam yang genap di sini — dan justru itu yang membalik jawabannya.
