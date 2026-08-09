---
id: ajk-05
sumber: Latihan 5 — susunan sendiri, gaya OSN-K
pilar: kombinatorika
tahap: osn-k
jurus: [aturan-pencacahan]
bentuk: isian
kesulitan: 3
jawaban: "294"
---

## Soal

Dari $8$ orang akan dipilih seorang ketua, seorang sekretaris, dan seorang bendahara.
Tidak ada yang boleh merangkap dua jabatan.

Salah seorang di antara mereka, sebut saja Ali, bersedia menjabat apa saja **kecuali
ketua**. Ada berapa susunan pengurus yang mungkin?

## Petunjuk

- Hitung dulu tanpa memedulikan keberatan Ali, lalu singkirkan susunan yang melanggarnya.
- Susunan yang melanggar adalah yang menempatkan Ali sebagai ketua — dan di situ jabatan ketua sudah tidak punya pilihan lagi.
- Ada jalan lain yang juga sah: pecah menjadi kasus Ali tidak menjabat dan Ali menjabat salah satu dari dua jabatan sisanya. Kedua jalan harus memberi hasil sama.

## Pembahasan

**Jalan pertama — hitung seluruhnya lalu buang yang melanggar.**

Tanpa keberatan siapa pun, ketiga jabatan diisi tiga orang berbeda dari $8$ orang, dan
jabatannya dapat dibedakan sehingga urutannya berarti:

$$8 \times 7 \times 6 = 336$$

Susunan yang melanggar adalah yang menjadikan Ali ketua. Di situ jabatan ketua tinggal $1$
cara, lalu sekretaris dan bendahara diisi dari $7$ orang sisanya:

$$1 \times 7 \times 6 = 42$$

Kurangkan:

$$336 - 42 = \boxed{294}$$

**Jalan kedua — pecah jadi kasus.** Susunan yang sah dibagi menurut peran Ali, dan ketiga
kasus di bawah ini lepas serta menutupi semuanya:

- **Ali tidak menjabat.** Ketiga jabatan diisi dari $7$ orang lain:
  $7 \times 6 \times 5 = 210$.
- **Ali sekretaris.** Ketua dan bendahara dari $7$ orang lain: $7 \times 6 = 42$.
- **Ali bendahara.** Dengan alasan yang sama: $42$.

$$210 + 42 + 42 = 294$$

Cocok.

**Mana yang dipilih?** Jalan pertama hampir selalu lebih pendek ketika larangannya cuma
satu. Jalan kedua menjadi lebih baik ketika larangannya bertumpuk — misalnya kalau ada dua
orang yang masing-masing menolak jabatan berbeda, karena di situ "yang melanggar" sendiri
sudah terdiri atas beberapa kelompok yang beririsan.

Mengerjakan keduanya seperti di atas juga cara memeriksa diri sendiri yang murah. Kalau
kedua jalan memberi angka berbeda, salah satunya melewatkan kasus.
