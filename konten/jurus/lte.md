---
id: lte
nama: Lifting the Exponent
pilar: teori-bilangan
tahap: osn
prasyarat: [legendre-faktorial, orde-elemen]
contoh: [lte-contoh-1]
latihan: [lte-01, lte-02, lte-03, lte-04, lte-05, lte-06]
---

## Kapan dipakai

Soal menanyakan **pangkat tertinggi sebuah prima** yang membagi $a^n \pm b^n$. Ciri
khasnya: ada selisih atau jumlah pangkat, dan yang ditanya keterbagian oleh **pangkat**
prima — bukan sekadar oleh primanya.

Pemicu kedua: soal menyebut bentuk seperti **$3^{100} - 1$** dan menanyakan berapa kali
suatu prima membaginya. Jurus lain menjawab "habis dibagi atau tidak"; hanya jurus ini yang
menjawab "berapa kali".

Pemicu ketiga: soal meminta mencari **$n$ terkecil** agar $p^k$ membagi $a^n - b^n$. Rumusnya
dibalik — $v_p(n)$ yang dicari, dan jawabannya jatuh langsung tanpa satu pun nilai dicoba.

Pemicu keempat: soal memberi persamaan Diophantine yang memuat **pangkat dengan eksponen
peubah**, seperti $2^x - 3^y = 1$. Menghitung $v_p$ kedua ruas sering memaksa eksponennya
menjadi kecil, dan sisanya diperiksa satu per satu.

Syarat yang wajib diperiksa dan paling sering dilewat: $p$ harus membagi $a-b$ (atau $a+b$)
tetapi **tidak** membagi $a$ maupun $b$. Dan $p = 2$ punya rumus sendiri — memakai rumus
prima ganjil di sana adalah kesalahan yang tidak berbunyi, ia hanya memberi angka yang
salah.

## Intinya

Tulis $v_p(x)$ untuk pangkat $p$ dalam $x$. Kalau $p$ prima ganjil, $p \mid a - b$, dan
$p \nmid a$, $p \nmid b$:

$$v_p(a^n - b^n) = v_p(a - b) + v_p(n)$$

Kalau $n$ ganjil, $p \mid a + b$, dan $p$ tidak membagi $a$ maupun $b$:

$$v_p(a^n + b^n) = v_p(a + b) + v_p(n)$$

Untuk $p = 2$ rumusnya berbeda dan harus diingat terpisah. Untuk $n$ genap:

$$v_2(a^n - b^n) = v_2(a-b) + v_2(a+b) + v_2(n) - 1$$

Nilai jurus ini: soal yang tampak menuntut perhitungan raksasa selesai dalam dua baris.

## Jebakan umum

- **Melupakan syaratnya.** $p \mid a - b$ itu wajib. Tanpa itu rumusnya memberi angka yang
  salah — dan tetap terlihat masuk akal.
- **Memakai rumus $p$ ganjil untuk $p = 2$.** Kasus $2$ punya rumus sendiri. Ini kesalahan
  paling sering pada jurus ini.
- **Memakai bentuk $a^n + b^n$ untuk $n$ genap.** Bentuk itu hanya berlaku untuk $n$ ganjil.
