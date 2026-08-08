---
id: kongruensi-dasar
nama: Kongruensi
pilar: teori-bilangan
tahap: osn-k
prasyarat: [algoritma-pembagian]
contoh: [kd-contoh-1]
latihan: [kd-01, kd-02, kd-03, kd-04, kd-05, kd-06]
---

## Kapan dipakai

Hampir selalu, begitu soal menyebut sisa pembagian — dan terutama saat kamu ingin
**membuktikan sesuatu tidak mungkin**. Kongruensi adalah alat pembuktian
ketidakmungkinan yang paling murah yang kamu punya.

## Intinya

$a \equiv b \pmod{m}$ berarti $m \mid (a - b)$.

Kekuatannya: kongruensi boleh **dijumlah, dikurang, dan dikali** seperti persamaan biasa.
Jadi seluruh refleks aljabarmu tetap terpakai, hanya saja dunianya menyusut jadi $m$
bilangan.

Pola pemakaian yang paling berhasil: kalau kamu curiga sebuah persamaan tidak punya
solusi bulat, **ambil modulo yang tepat** dan tunjukkan kedua ruas tidak pernah cocok.

Modulo yang paling sering berguna, karena himpunan nilainya sempit:

| Bentuk | Modulo | Nilai yang mungkin |
|---|---|---|
| $x^2$ | $4$ | $0, 1$ |
| $x^2$ | $8$ | $0, 1, 4$ |
| $x^2$ | $3$ | $0, 1$ |
| $x^3$ | $9$ | $0, 1, 8$ |

Contoh cara pakainya: $x^2 + y^2 = 3z^2$ tidak punya solusi bulat tak nol, dan itu
ketahuan hanya dengan melihat semuanya modulo $4$.

## Jebakan umum

- **Membagi kedua ruas sembarangan.** Ini kesalahan terbesar. Dari
  $6 \equiv 12 \pmod{6}$ tidak boleh disimpulkan $1 \equiv 2 \pmod 6$. Pembagian hanya sah
  kalau pembaginya relatif prima terhadap modulusnya.
- **Memangkatkan eksponennya dengan aturan modulo yang sama.** $a^k \bmod m$ tidak
  ditentukan oleh $k \bmod m$. Eksponen punya aturannya sendiri — itu wilayah Fermat dan
  Euler.
- **Memilih modulo asal-asalan.** Modulo yang berguna adalah yang membuat himpunan nilai
  ruas kiri dan ruas kanan tidak beririsan. Kalau tidak menghasilkan tabrakan, ganti.
