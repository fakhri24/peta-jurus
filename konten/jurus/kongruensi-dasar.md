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

Soal menyebut **sisa pembagian**, atau memberi bilangan berpangkat besar dan menanyakan
sisanya.

Pemicu kedua, dan inilah pemakaian terpentingnya: soal meminta membuktikan sesuatu **tidak
mungkin** — tidak ada penyelesaian bulat, sebuah bilangan tidak pernah kuadrat sempurna.
Kongruensi adalah alat pembuktian ketidakmungkinan yang paling murah yang kamu punya, dan
selalu layak dicoba lebih dulu daripada yang mahal.

Pemicu ketiga: soal memuat **kuadrat atau pangkat tiga** dengan syarat bulat. Kuadrat hanya
bisa bersisa $0$ atau $1$ modulo $4$, dan $0, 1, 4$ modulo $8$ — kenyataan sesempit itu
menutup banyak persamaan dalam satu baris.

Pemicu keempat: soal menyebut **digit terakhir**, **paritas**, atau "habis dibagi". Ketiganya
kongruensi yang menyamar, berturut-turut modulo $10$, $2$, dan modulusnya sendiri.

Pemicu kelima: ada **pangkat dengan eksponen raksasa**. Cari pangkat kecil yang bersisa $1$,
lalu potong eksponennya — putaran itu selalu ada dan biasanya pendek.

Memilih modulusnya seluruh seninya, dan ia bisa dilatih: coba modulus kecil dulu, dan
perhatikan bilangan yang sudah muncul di soalnya.

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
