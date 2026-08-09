---
id: rekursi
nama: Rekursi dan Relasi Rekurens
pilar: kombinatorika
tahap: osn-p
prasyarat: [kombinasi, induksi]
contoh: [rek-contoh-1]
latihan: [rek-01, rek-02, rek-03, rek-04, rek-05, rek-06]
---

## Kapan dipakai

Jawaban untuk $n$ bisa disusun dari jawaban untuk $n$ yang lebih kecil. Pemicunya: soal
bergantung pada $n$ dan menanyakan nilainya untuk $n$ yang besar, atau strukturnya
berbunyi "lalu ditambahkan satu lagi" — satu ubin lagi, satu anak tangga lagi, satu huruf
lagi.

Cara memancingnya selalu sama: hitung tangan untuk $n = 1, 2, 3, 4$, lalu tanyakan apa
yang terjadi pada langkah terakhir.

## Intinya

Sebuah rekurens selalu punya dua bagian, dan keduanya wajib: **kasus dasar** dan **langkah
yang menghubungkan**.

Menyusun langkahnya berarti memutuskan satu hal: keadaan berukuran $n$ dipecah menurut apa
yang terjadi di ujungnya. Kasus-kasusnya harus lepas dan menutupi semuanya — syarat yang
sama dengan aturan jumlah, karena memang itu yang sedang dipakai.

$$a_n = a_{n-1} + a_{n-2}$$

Untuk rekurens linear homogen orde dua

$$a_n = p\,a_{n-1} + q\,a_{n-2}$$

rumus tertutupnya dicari lewat persamaan karakteristik $x^2 = px + q$. Kalau akarnya $r_1$
dan $r_2$ berbeda,

$$a_n = A\,r_1^{\,n} + B\,r_2^{\,n}$$

dengan $A$ dan $B$ ditentukan dari kasus dasar.

Kalau rumus tertutupnya ditebak dari beberapa suku pertama, **tebakan itu harus dibuktikan
dengan induksi** — kecocokan pada empat suku pertama bukan bukti.

## Jebakan umum

- **Kasus dasar kurang.** Rekurens orde dua butuh dua nilai awal; satu saja membuat
  barisannya tidak tertentu.
- **Kasus yang tumpang tindih.** Kalau satu keadaan bisa masuk dua cabang, hitungannya
  kelebihan — dan biasanya baru ketahuan setelah dicocokkan dengan hitungan tangan.
- **Langsung mengejar rumus tertutup.** Banyak soal cuma minta nilai untuk $n$ kecil;
  rekurensnya sendiri sudah jawabannya.
