---
id: turun-tak-hingga
nama: Turun Tak Hingga
pilar: teori-bilangan
tahap: osn-p
prasyarat: [bilangan-prima, kongruensi-dasar]
contoh: [tth-contoh-1]
latihan: [tth-01, tth-02, tth-03, tth-04, tth-05, tth-06]
---

## Kapan dipakai

Soal meminta **membuktikan tidak ada solusi bulat positif**, dan kongruensi saja tidak
cukup untuk menutupnya. Urutan mencobanya tetap: modulo dulu, karena jauh lebih murah;
jurus ini untuk persamaan yang lolos setiap modulus yang kamu coba.

Pemicu kedua, dan inilah sidik jarinya: persamaannya **homogen** — tiap sukunya berderajat
sama, seperti $x^3 + 2y^3 = 4z^3$. Bentuk itu mengizinkan seluruh solusi dibagi faktor
persekutuannya, dan pembagian itulah yang menghasilkan solusi lebih kecil.

Pemicu ketiga: soal meminta membuktikan sebuah bilangan **irasional**, atau bahwa suatu
perbandingan tidak pernah bulat. Keduanya pernyataan ketiadaan yang sama, berpakaian lain.

Pemicu keempat: kamu sudah menemukan solusi yang jelas seperti $(0,0,0)$ dan soal meminta
menunjukkan **tidak ada yang lain**. Yang dibuktikan bukan ketiadaan seluruhnya, melainkan
ketiadaan yang tak sepele — dan itu bentuk baku jurus ini.

## Intinya

Andaikan ada solusi. Tunjukkan bahwa dari solusi itu bisa dibuat solusi lain yang **lebih
kecil** tapi tetap bulat positif. Ulangi tanpa henti — mustahil, karena bilangan bulat
positif tidak bisa turun selamanya. Jadi solusi awalnya tidak pernah ada.

Bentuk yang paling praktis: ambil solusi dengan nilai **terkecil**, lalu turunkan lagi.
Kontradiksinya langsung terlihat.

> Alurnya pada $x^2 + y^2 = 3z^2$: modulo $3$, kuadrat hanya bernilai $0$ atau $1$, jadi
> $x^2 + y^2 \equiv 0$ memaksa $3 \mid x$ dan $3 \mid y$. Tulis $x = 3x_1$, $y = 3y_1$,
> maka $3x_1^2 + 3y_1^2 = z^2$ — sehingga $3 \mid z$ juga. Kini $(x/3, y/3, z/3)$ solusi
> yang lebih kecil. Turun tanpa dasar, jadi tidak ada solusi tak nol.

Perhatikan pasangannya: kongruensi yang memaksa keterbagian, lalu penurunan yang memanen
kontradiksi. Keduanya hampir selalu muncul bersama.

## Jebakan umum

- **Lupa mengecualikan solusi nol.** $(0,0,0)$ biasanya memang solusi; yang dibuktikan
  tidak ada adalah solusi tak nol.
- **Penurunannya tidak benar-benar menurun.** Pastikan solusi barunya bulat **dan** benar-
  benar lebih kecil. Kalau ukurannya bisa tetap, argumennya bocor.
- **Berhenti di kongruensi.** Kongruensi hanya memaksa keterbagian; penurunannya yang
  menutup soal.
