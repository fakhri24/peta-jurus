---
id: smp-contoh-1
sumber: Contoh terpandu — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [sarang-merpati]
bentuk: isian
kesulitan: 2
jawaban: "13"
---

## Soal

Paling sedikit berapa orang harus berkumpul supaya **pasti** ada dua orang di antaranya
yang berulang tahun pada bulan yang sama?

## Petunjuk

- Soal tidak menanyakan berapa banyak kemungkinan, melainkan berapa yang membuat sesuatu tidak bisa dihindari lagi. Pikirkan keadaan terburuk.
- Bayangkan sekelompok orang yang bulan lahirnya sebisa mungkin berbeda semua. Paling banyak berapa orang yang bisa dikumpulkan seperti itu?
- Setelah kelompok terbesar tanpa dua orang sebulan itu ditemukan, tambahkan satu orang lagi.

## Pembahasan

**Tentukan sarangnya.** Sarang di sini adalah bulan lahir, dan banyaknya

$$k = 12$$

Merpatinya adalah orang.

**Cari keadaan terburuk.** Bayangkan sekelompok orang yang bulan lahirnya berbeda semua.
Paling banyak, kelompok itu berisi $12$ orang — satu untuk tiap bulan. Dengan $12$ orang,
masih mungkin tidak ada dua yang sebulan.

**Tambah satu.** Begitu orang ke-$13$ datang, bulan lahirnya pasti salah satu dari $12$
bulan yang sudah terpakai. Maka pasti ada dua orang yang sebulan.

$$\boxed{13}$$

**Mengapa jawabannya bukan $12$.** Pertanyaan "paling sedikit berapa supaya **pasti**"
selalu punya dua bagian, dan keduanya perlu:

1. **Dengan $13$ orang, selalu terjadi.** Ini yang dijamin prinsip sarang merpati.
2. **Dengan $12$ orang, belum tentu terjadi.** Ini ditunjukkan dengan **contoh**: satu
   orang untuk tiap bulan.

Bagian kedua sering dilewati, padahal tanpanya jawabannya belum lengkap. Ia yang
membuktikan angka itu memang paling kecil, bukan sekadar cukup.

**Yang tidak dikatakan prinsip ini.** Ia tidak menyebut bulan mana yang berisi dua orang,
dan tidak menyebut siapa keduanya. Ia hanya menjamin ada. Soal yang menanyakan "bulan apa"
memang meminta hal lain sama sekali.

**Bentuk umumnya.** Untuk $k$ sarang, jawaban pertanyaan semacam ini adalah $k+1$. Kalau
yang diminta "pasti ada **tiga** yang sebulan", jawabannya $2k+1 = 25$ — karena keadaan
terburuknya dua orang untuk tiap bulan.
