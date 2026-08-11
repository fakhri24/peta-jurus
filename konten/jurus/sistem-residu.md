---
id: sistem-residu
nama: Sistem Residu
pilar: teori-bilangan
tahap: osn-p
prasyarat: [kongruensi-dasar]
contoh: [sr-contoh-1]
latihan: [sr-01, sr-02, sr-03, sr-04, sr-05, sr-06]
---

## Kapan dipakai

Soal meminta menganalisis sifat yang berlaku untuk **seluruh kemungkinan sisa pembagian** modulo $m$ secara serentak.

Pemicu kedua: perkalian himpunan sisa dengan $a$ yang relatif prima terhadap $m$. Jika $\gcd(a, m) = 1$, perkalian $\{a \cdot 0, a \cdot 1, \dots, a \cdot (m-1)\}$ hanya meletakkan ulang (mengocok) sisa-sisa tersebut tanpa ada yang bertabrakan.

Pemicu ketiga: pembuktian teorema-teorema struktur kongruensi, seperti Teorema Fermat Kecil atau Euler, yang mengalikan seluruh anggota sistem residu tereduksi lalu membagi dengan produknya.

Pemicu keempat: soal menghitung **banyaknya solusi** persamaan kongruensi dalam satu rentang lengkap $0$ sampai $m-1$.

## Intinya

Sistem residu lengkap modulo $m$ adalah himpunan yang memuat tepat satu wakil dari setiap
kelas sisa, biasanya $\{0, 1, \dots, m-1\}$. Sistem residu **tereduksi** hanya memuat
yang relatif prima terhadap $m$; banyaknya adalah $\varphi(m)$.

Sifat yang membuat semuanya bekerja:

> Kalau $\gcd(a, m) = 1$ dan $x$ menjelajahi seluruh sistem residu lengkap, maka $ax$ juga
> menjelajahi seluruh sistem residu lengkap — hanya urutannya teracak.

Artinya **mengalikan dengan bilangan yang relatif prima itu sekadar mengocok kartu**:
tidak ada kelas sisa yang hilang, tidak ada yang muncul dua kali. Dari satu pengamatan
inilah Teorema Fermat Kecil dan Teorema Euler dibuktikan — keduanya hanya soal mengalikan
seluruh kartu yang sudah dikocok itu.

Syarat $\gcd(a,m)=1$ tidak bisa dilepas. Modulo $6$, mengalikan dengan $2$ memampatkan
enam kelas menjadi tiga saja.

## Jebakan umum

- **Melupakan syarat relatif prima.** Tanpa itu, pengocokan berubah jadi pemampatan dan
  seluruh argumennya batal.
- **Mengira sistem residu harus $\{0,\dots,m-1\}$.** Boleh apa saja asal satu wakil per
  kelas. Untuk modulo ganjil, memakai wakil simetris $\{-\frac{m-1}{2}, \dots,
  \frac{m-1}{2}\}$ sering memangkas separuh pekerjaan.
