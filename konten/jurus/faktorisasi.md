---
id: faktorisasi
nama: Faktorisasi
pilar: aljabar
tahap: osn-k
prasyarat: [manipulasi-aljabar]
contoh: [fkt-contoh-1]
latihan: [fkt-01, fkt-02, fkt-03, fkt-04, fkt-05, fkt-06]
---

## Kapan dipakai

**Ruas kanannya nol.** Begitu sebuah persamaan berbentuk $\ldots = 0$, mengubah ruas kirinya
menjadi hasil kali langsung memberi seluruh penyelesaiannya.

Pemicu kedua, dan ini yang membuat jurus ini terpakai jauh di luar aljabar: soal meminta
**pasangan bilangan bulat** yang memenuhi suatu persamaan. Ubah bentuknya menjadi hasil kali
sama dengan sebuah bilangan tetap, lalu cacah pasangan pembaginya — persamaan berubah dari
tak hingga kemungkinan menjadi daftar yang bisa dihabiskan.

Pemicu ketiga: ada **bentuk yang bisa dikenali** — selisih kuadrat, jumlah atau selisih
pangkat tiga, atau kuadrat sempurna yang tersamar. $x^4 + 4$ terlihat buntu sampai
diingat ia $(x^2+2x+2)(x^2-2x+2)$.

Pemicu keempat, arah sebaliknya: soal meminta membuktikan sebuah bilangan **bukan prima**
atau **habis dibagi** sesuatu. Menemukan satu faktorisasi menyelesaikannya seketika.

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
