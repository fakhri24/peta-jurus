---
id: smp-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 1
jawaban: "4"
---

## Soal

Sebuah laci berisi banyak sekali kaus kaki dengan tiga warna: merah, biru, dan hijau. Kaus
kaki diambil satu per satu **dalam gelap**, sehingga warnanya tidak bisa dilihat.

Paling sedikit berapa kaus kaki harus diambil supaya pasti didapat sepasang yang sewarna?

## Petunjuk

- Bayangkan nasib paling sial: setiap kaus kaki yang terambil ternyata warnanya belum pernah muncul.
- Paling banyak berapa kaus kaki yang bisa terambil sebelum terpaksa ada warna yang berulang?
- Setelah itu, satu pengambilan lagi sudah tidak punya warna baru untuk dituju.

## Pembahasan

**Sarangnya warna, merpatinya kaus kaki.** Banyaknya sarang:

$$k = 3$$

**Keadaan terburuk.** Kalau tiga kaus kaki yang terambil ternyata merah, biru, dan hijau —
masing-masing satu — belum ada sepasang yang sewarna. Jadi $3$ belum menjamin apa pun.

**Pengambilan keempat.** Warnanya harus salah satu dari ketiga warna yang ada, dan
ketiganya sudah terpakai. Maka pasti ada dua kaus kaki sewarna.

$$\boxed{4}$$

**Perhatikan bahwa banyaknya kaus kaki di laci tidak disebut,** dan memang tidak
dibutuhkan. Yang menentukan jawaban hanyalah banyaknya **warna**. Kalau lacinya berisi
seribu kaus kaki atau sepuluh, jawabannya tetap $4$ — asalkan tiap warna tersedia paling
sedikit dua.

Kelebihan keterangan seperti ini sering membuat ragu. Kebiasaan yang menolong: sebelum
menghitung, tuliskan dulu apa yang menjadi sarang. Begitu tertulis "sarangnya warna, ada
tiga", jelas bahwa jumlah kaus kaki tidak ikut menentukan.

**Kalau warnanya bertambah menjadi lima,** jawabannya $6$. Kalau yang diminta **dua**
pasang sewarna, keadaan terburuknya berubah dan jawabannya bukan lagi sekadar $k+1$ —
cobalah pikirkan sendiri berapa.
