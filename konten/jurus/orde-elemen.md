---
id: orde-elemen
nama: Orde Elemen
pilar: teori-bilangan
tahap: osn
prasyarat: [fungsi-euler]
contoh: [oe-contoh-1]
latihan: [oe-01, oe-02, oe-03, oe-04, oe-05, oe-06]
---

## Kapan dipakai

Soal tentang **periode** — kapan $a^k$ berulang, atau mencari $n$ **terkecil** dengan
$a^n \equiv 1$. Kata "terkecil" itu pembedanya dari Fermat Kecil dan Euler, yang hanya
memberi satu pangkat yang berhasil, belum tentu yang terkecil.

Pemicu kedua, dan inilah pemakaian yang paling tajam: soal perlu **membatasi prima yang
mungkin membagi** bentuk seperti $2^n - 1$ atau $a^n + 1$. Setiap prima pembaginya memaksa
orde tertentu, dan orde itu membagi $p-1$ — dua syarat yang bersama-sama menyisakan sangat
sedikit kemungkinan.

Pemicu ketiga: soal menyatakan $a^k \equiv 1$ dan menanyakan **apa yang bisa disimpulkan
tentang $k$**. Jawabannya selalu sama bentuknya: orde membagi $k$. Bukan "$k$ kelipatan
sesuatu yang kebetulan", melainkan keterbagian yang pasti.

Pemicu keempat: soal memuat **barisan sisa yang berulang** dan menanyakan suku ke-$n$-nya.
Panjang putarannya persis ordenya.

Pemicu kelima: soal meminta membuktikan ada **tak hingga prima** berbentuk tertentu, seperti
$p \equiv 1 \pmod n$. Bukti bakunya berjalan lewat orde.

Yang paling sering keliru: menyimpulkan orde sama dengan $p-1$ padahal ia hanya
**membaginya**. Memeriksa pembagi sejati $p-1$ bagian dari pekerjaannya, bukan kehati-hatian
tambahan.

## Intinya

Orde $a$ modulo $n$, ditulis $\operatorname{ord}_n(a)$, adalah bilangan positif terkecil
$d$ dengan $a^d \equiv 1 \pmod n$ (ada asalkan $\gcd(a,n)=1$).

Sifat yang menjadi seluruh isi jurus ini:

$$a^k \equiv 1 \pmod n \quad\Longleftrightarrow\quad \operatorname{ord}_n(a) \mid k$$

Bukan "$k$ kelipatan sesuatu yang mirip" — tepat habis dibagi. Akibat langsungnya,
$\operatorname{ord}_n(a) \mid \varphi(n)$, dan untuk modulus prima
$\operatorname{ord}_p(a) \mid p - 1$.

Dari sini lahir jurus pembatas prima yang sangat berguna:

> Kalau $p \mid 2^n - 1$, maka $\operatorname{ord}_p(2) \mid n$. Digabung dengan
> $\operatorname{ord}_p(2) \mid p-1$, calon $p$ langsung tersaring jadi sedikit sekali.

## Jebakan umum

- **Mengira orde selalu $\varphi(n)$.** Itu hanya batas atas. Orde $2$ modulo $7$ adalah
  $3$, bukan $6$.
- **Menyimpulkan dari $a^k \equiv 1$ bahwa $k$ adalah ordenya.** $k$ hanya kelipatan orde.
- **Lupa syarat $\gcd(a,n) = 1$.** Tanpa itu $a^d \equiv 1$ tidak pernah tercapai.
