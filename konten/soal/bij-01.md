---
id: bij-01
sumber: Latihan 1 — susunan sendiri, gaya OSN-P
pilar: kombinatorika
tahap: osn-p
jurus: [bijeksi]
bentuk: isian
kesulitan: 2
jawaban: "210"
---

## Soal

Sebuah semut berada di titik $(0,0)$ pada kisi persegi dan hendak menuju $(6,4)$. Ia hanya
boleh melangkah satu satuan ke kanan atau satu satuan ke atas.

Ada berapa jalur yang mungkin?

## Petunjuk

- Ubah jalurnya menjadi barisan. Berapa langkah yang dibutuhkan seluruhnya, dan apakah angka itu sama untuk tiap jalur?
- Catat jalurnya sebagai barisan huruf K dan A, lalu periksa bahwa tiap barisan semacam itu memang memberi jalur yang sah.
- Menentukan barisan sama dengan memilih langkah keberapa saja yang ke atas.

## Pembahasan

**Ubah jalur menjadi barisan.** Untuk sampai dari $(0,0)$ ke $(6,4)$, semut harus melangkah
$6$ kali ke kanan dan $4$ kali ke atas, seluruhnya

$$6 + 4 = 10 \text{ langkah}$$

Angka ini sama untuk tiap jalur, sebab semut tidak pernah mundur.

Catat jalurnya sebagai barisan sepanjang $10$ dari huruf K dan A.

**Periksa padanannya ke dua arah.**

- Tiap jalur memberi tepat satu barisan.
- Tiap barisan yang memuat tepat $6$ huruf K dan $4$ huruf A memberi tepat satu jalur —
  jalankan saja langkahnya berurutan; ia selalu berakhir di $(6,4)$.

Jadi mencacah jalur sama dengan mencacah barisan.

**Cacah barisannya.** Sebuah barisan ditentukan sepenuhnya begitu diputuskan langkah
keberapa saja yang ke atas:

$$\binom{10}{4} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = \boxed{210}$$

**Boleh juga dari sisi K:** $\binom{10}{6} = 210$. Hasilnya sama, sesuai
$\binom nk = \binom n{n-k}$.

**Rumus umumnya** untuk $(0,0) \to (m,n)$:

$$\binom{m+n}{n}$$

**Periksa dengan rekursi.** Banyaknya jalur ke sebuah titik sama dengan jumlah jalur ke
titik di kirinya dan di bawahnya. Mengisi kisi $6\times4$ dengan aturan itu — persis
segitiga Pascal yang dimiringkan — memberi $210$ di pojok kanan atas. Dua cara yang sangat
berbeda bertemu di angka yang sama.

**Kalau ada titik yang harus dihindari,** cara barisan tidak langsung berlaku, dan yang
dipakai adalah pengurangan: hitung seluruh jalur, lalu kurangi jalur yang melewati titik
terlarang. Jalur yang melewati sebuah titik dihitung dengan mengalikan jalur menuju titik
itu dengan jalur dari titik itu ke tujuan.
