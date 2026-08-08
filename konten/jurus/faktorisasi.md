---
id: faktorisasi
nama: Faktorisasi
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: []
latihan: []
---

## Kapan dipakai

Ruas kanan bernilai nol, atau kamu perlu mengubah jumlah menjadi hasil kali supaya bisa
memakai "hasil kali nol" atau mencacah pasangan pembagi.

## Intinya

Empat cara yang menutup hampir semua soal OSN-K:

1. **Faktor persekutuan.** Selalu dicoba lebih dulu.
2. **Pengelompokan.** $ax + ay + bx + by = (a+b)(x+y)$.
3. **Bentuk kuadrat.** $x^2 + (p+q)x + pq = (x+p)(x+q)$ — cari dua bilangan yang
   berjumlah koefisien tengah dan berhasil kali konstanta.
4. **Identitas.** Selisih kuadrat, jumlah dan selisih pangkat tiga.

Yang membuat faktorisasi berharga adalah akibatnya: dari $AB = 0$ langsung diperoleh
$A = 0$ atau $B = 0$. Persamaan berderajat tinggi runtuh menjadi beberapa persamaan
sederhana.

Untuk soal bilangan bulat, akibatnya berbeda tetapi sama kuatnya: dari $AB = n$ dengan $A$
dan $B$ bulat, keduanya harus berupa pasangan pembagi $n$ — dan pembagi $n$ jumlahnya
berhingga.

## Jebakan umum

- **Membagi dengan sesuatu yang mungkin nol.** Dari $x^2 = 3x$, membagi $x$ menghilangkan
  solusi $x = 0$. Pindahkan ruas dan faktorkan: $x(x-3) = 0$.
- **Berhenti setelah satu langkah.** $x^4 - 16 = (x^2-4)(x^2+4)$ masih bisa dilanjutkan
  menjadi $(x-2)(x+2)(x^2+4)$.
- **Memaksa memfaktorkan yang tidak terfaktor** atas bilangan rasional. Periksa
  diskriminannya sebelum menghabiskan waktu.
