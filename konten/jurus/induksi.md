---
id: induksi
nama: Induksi Matematika
pilar: aljabar
tahap: osn-p
prasyarat: [barisan-deret]
contoh: [ind-contoh-1]
latihan: [ind-01, ind-02, ind-03, ind-04, ind-05, ind-06]
---

## Kapan dipakai

Pernyataan dituntut berlaku **untuk setiap bilangan asli $n \ge n_0$**, dan bentuk kasus $n = k+1$ dapat diturunkan/disusun secara sistematis dari kasus $n = k$.

Pemicu kedua: ada **rumus eksplisit yang sudah berhasil ditebak** dari percobaan kasus-kasus kecil, dan kamu perlu membuktikannya secara formal untuk seluruh $n$.

Pemicu ketiga: pembuktian pertaksamaan atau sifat keterbagian yang memuat parameter bilangan asli $n$ di mana langkah $k \to k+1$ memanfaatkan struktur rekursif.

Pemicu keempat: induksi kuat (strong induction), ketika kebenaran kasus $n = k+1$ membutuhkan asumsi bahwa seluruh kasus sebelumnya ($n = 1, 2, \dots, k$) telah bernilai benar secara bersamaan.

## Intinya

Dua langkah, dan keduanya wajib:

1. **Basis.** Tunjukkan pernyataannya benar untuk $n$ terkecil.
2. **Langkah induksi.** Andaikan benar untuk $n = k$, lalu buktikan benar untuk $n = k+1$.

Yang menentukan mutu pembuktian adalah langkah kedua: di situ hipotesis induksi harus
benar-benar **dipakai**, bukan sekadar disebut. Kalau pembuktian $n = k+1$ berjalan tanpa
menyentuh yang $n = k$, biasanya induksinya tidak diperlukan sama sekali — atau ada yang
salah.

**Induksi kuat** mengandaikan pernyataannya benar untuk semua nilai dari basis sampai $k$,
bukan hanya di $k$. Ia diperlukan ketika langkah $k+1$ bersandar pada dua nilai sebelumnya
atau lebih — misalnya pada barisan yang tiap sukunya dibangun dari dua suku sebelumnya.

Untuk deret, pola kerjanya hampir selalu sama: tulis $S_{k+1} = S_k + U_{k+1}$, ganti $S_k$
dengan hipotesis induksi, lalu sederhanakan sampai berbentuk rumus untuk $k+1$.

## Jebakan umum

- **Melewatkan basis.** Tanpa basis, langkah induksi membuktikan pernyataan salah pun bisa
  "berhasil".
- **Basis di tempat yang keliru.** Kalau pernyataannya berlaku untuk $n \ge 3$, basisnya
  $n = 3$.
- **Tidak memakai hipotesis induksi.** Ini bukan soal gaya penulisan; kalau ia tidak
  dipakai, yang kamu tulis bukan pembuktian induksi.
- **Mengubah yang dibuktikan di tengah jalan.** Pernyataan untuk $k+1$ harus dirumuskan
  lebih dulu, lalu dicapai — bukan disesuaikan dengan hasil yang terlanjur keluar.
