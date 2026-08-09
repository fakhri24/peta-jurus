---
id: invarian
nama: Invarian dan Monovarian
pilar: kombinatorika
tahap: osn-p
prasyarat: [sarang-merpati]
contoh: [inv-contoh-1]
latihan: [inv-01, inv-02, inv-03, inv-04, inv-05, inv-06]
---

## Kapan dipakai

Soal berisi **proses** — satu langkah yang boleh diulang sesukanya — dan menanyakan apakah
suatu keadaan bisa dicapai, atau apakah prosesnya pasti berhenti. Pemicunya: "mungkinkah
setelah beberapa langkah…", "buktikan tidak mungkin", "tunjukkan proses berakhir".

Ciri yang menolong: kamu sudah mencoba beberapa kali dan selalu gagal mencapai targetnya.
Itu tanda ada sesuatu yang tidak pernah berubah, dan tugasmu menemukannya.

## Intinya

**Invarian** adalah besaran yang nilainya tidak berubah oleh langkah apa pun. Kalau
nilainya berbeda antara keadaan awal dan keadaan target, targetnya tidak bisa dicapai —
berapa pun banyaknya langkah.

Yang paling sering menolong: paritas, jumlah atau selisih modulo suatu bilangan, banyaknya
objek berjenis tertentu modulo dua, dan warna.

**Monovarian** adalah besaran yang selalu berubah ke satu arah saja. Kalau ia selalu turun
dan nilainya bilangan asli, prosesnya tidak bisa berjalan selamanya — karena tidak ada
barisan turun tak berhingga di bilangan asli. Itu cara baku membuktikan proses berhenti.

Cara memakainya selalu tiga langkah: tebak besarannya, **buktikan tiap langkah tidak
mengubahnya**, lalu bandingkan awal dengan target. Langkah kedua yang paling sering
dilewati, dan ia yang menentukan sah atau tidaknya.

Invarian membuktikan **tidak mungkin**. Ia tidak pernah membuktikan mungkin.

## Jebakan umum

- **Menyimpulkan "bisa dicapai" karena invariannya cocok.** Cocok itu syarat perlu, bukan
  cukup. Untuk menunjukkan bisa, tunjukkan urutan langkahnya.
- **Ada langkah yang belum diperiksa.** Kalau prosesnya punya beberapa jenis langkah,
  besaran itu harus tetap pada **semuanya**, termasuk yang jarang dipakai.
- **Monovarian yang bisa turun selamanya.** Besaran yang selalu berkurang tapi bernilai
  real tidak menjamin proses berhenti; yang menjamin adalah nilainya bulat dan terbatas di
  bawah.
